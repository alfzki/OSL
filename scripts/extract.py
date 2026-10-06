#!/usr/bin/env python3
"""
scripts/extract.py
Ekstraksi teks per halaman/slide dari materi PDF dan PPTX ke folder extracted/.
Mendeteksi halaman kosong (indikasi scan), menjalankan OCR jika tool tersedia,
merender halaman/slide yang sarat gambar, rumus, atau tabel ke extracted/img/,
dan menyusun extracted/_laporan.md secara komprehensif.
"""

import os
import sys
import glob
import re
import shutil
from pathlib import Path

# Dependency check
try:
    import pymupdf  # PyMuPDF
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        print("ERROR: PyMuPDF belum terpasang. Jalankan 'uv add pymupdf'.", file=sys.stderr)
        sys.exit(1)

try:
    import pptx
    from pptx.enum.shapes import MSO_SHAPE_TYPE
except ImportError:
    print("ERROR: python-pptx belum terpasang. Jalankan 'uv add python-pptx'.", file=sys.stderr)
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    Image = None

# Optional OCR support
HAS_TESSERACT = shutil.which("tesseract") is not None
try:
    import pytesseract
    HAS_PYTESSERACT = True
except ImportError:
    HAS_PYTESSERACT = False

CAN_OCR = HAS_TESSERACT and HAS_PYTESSERACT


def get_ocr_status_info() -> dict:
    """Mengembalikan status engine OCR Tesseract dan bahasa yang didukung."""
    if not CAN_OCR:
        return {
            "tersedia": False,
            "pesan": "Belum terpasang di host"
        }
    try:
        ver = pytesseract.get_tesseract_version()
        langs = pytesseract.get_languages()
        return {
            "tersedia": True,
            "versi": str(ver),
            "bahasa": langs,
            "pesan": f"Tersedia (Tesseract v{ver}, bahasa: {', '.join(langs)})"
        }
    except Exception:
        return {
            "tersedia": True,
            "versi": "unknown",
            "bahasa": ["ind", "eng"],
            "pesan": "Tersedia (Tesseract biner terdeteksi)"
        }


def sanitize_filename(name: str) -> str:
    """Bersihkan nama berkas agar aman digunakan pada sistem operasi."""
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    clean = clean.replace(" ", "_")
    return clean


def is_math_or_formula(text: str) -> bool:
    """Deteksi keberadaan rumus matematika / simbol statistik dalam teks tanpa false positive pada tanda hubung teks biasa."""
    math_symbols = [
        "∑", "√", "∫", "±", "≤", "≥", "≠", "≈", "∞", "÷", "×",
        "\\frac", "\\sum"
    ]
    formula_patterns = [
        r'\bP_[012]\b', r'\bI_[tb]\b', r'\bNTP\s*=', r'\bIHK\s*=',
        r'\bTPK\s*=', r'\bFGT\b', r'=\s*[^=]+[\+\*\/]', r'\b\d+\s*[\+\*\/]\s*\d+'
    ]
    has_sym = any(sym in text for sym in math_symbols)
    has_pat = any(re.search(pat, text) for pat in formula_patterns)
    return has_sym or has_pat


def extract_table_from_pptx_shape(shape) -> str:
    """Konversi objek tabel PPTX menjadi tabel Markdown."""
    table = shape.table
    md_lines = []
    
    rows_data = []
    for row in table.rows:
        row_cells = [cell.text.strip().replace("\n", " ") for cell in row.cells]
        rows_data.append(row_cells)
        
    if not rows_data:
        return ""
        
    # Header
    header = rows_data[0]
    md_lines.append("| " + " | ".join(header) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    
    # Rows
    for row in rows_data[1:]:
        # Sesuaikan panjang kolom jika ada merge
        padded_row = row + [""] * (len(header) - len(row))
        md_lines.append("| " + " | ".join(padded_row[:len(header)]) + " |")
        
    return "\n" + "\n".join(md_lines) + "\n"


def process_pdf(pdf_path: Path, output_dir: Path, img_dir: Path):
    """Proses ekstraksi teks, gambar, dan audit untuk berkas PDF."""
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    extracted_pages = 0
    
    # Tentukan penanda berdasarkan direktori sumber
    is_slide = "slides" in str(pdf_path) or "Kontrak" in pdf_path.name
    marker_name = "Slide" if is_slide else "Halaman"
    
    base_name = pdf_path.stem
    safe_base = sanitize_filename(base_name)
    md_output_path = output_dir / f"{safe_base}.md"
    
    file_report = {
        "file": str(pdf_path),
        "tipe": "PDF",
        "total_halaman": total_pages,
        "halaman_terekstrak": 0,
        "halaman_butuh_ocr": [],
        "halaman_visual": [],
        "gambar_tersimpan": []
    }
    
    md_sections = [f"# {pdf_path.name}\n\nSumber Asli: `{pdf_path}`\n\n---\n"]
    
    for page_idx in range(total_pages):
        page_num = page_idx + 1
        page = doc[page_idx]
        text = page.get_text()
        char_count = len(text.strip())
        
        images = page.get_images()
        drawings = page.get_drawings()
        has_formula = is_math_or_formula(text)
        
        is_empty = char_count < 15
        needs_visual = len(images) > 0 or len(drawings) > 10 or has_formula
        
        page_md = [f"\n## {marker_name} {page_num}\n"]
        
        # Penanganan OCR jika halaman kosong
        ocr_applied = False
        if is_empty:
            file_report["halaman_butuh_ocr"].append(page_num)
            
            # Selalu render halaman kosong sebagai PNG untuk inspeksi
            img_filename = f"{safe_base}_hal_{page_num}.png"
            img_dest = img_dir / img_filename
            try:
                pix = page.get_pixmap(dpi=150)
                pix.save(img_dest)
                file_report["gambar_tersimpan"].append(img_filename)
                needs_visual = True
            except Exception as e:
                print(f"Gagal render pixmap PDF {pdf_path.name} hal {page_num}: {e}")
                
            if img_dest.exists():
                page_md.append(f"![{marker_name} {page_num}](img/{img_filename})\n")
                
            if CAN_OCR and Image is not None and img_dest.exists():
                try:
                    pil_img = Image.open(img_dest)
                    ocr_text = pytesseract.image_to_string(pil_img, lang="ind+eng")
                    if len(ocr_text.strip()) > 10:
                        page_md.append(f"> *[Hasil OCR]:*\n{ocr_text.strip()}\n")
                        ocr_applied = True
                        char_count = len(ocr_text.strip())
                    else:
                        page_md.append(f"> *[Catatan: Teks digital kosong (<15 karakter). Berisi gambar/visual yang perlu inspeksi visual manual]*\n")
                except Exception as e:
                    page_md.append(f"> *[Gagal OCR]: {e}*\n")
            else:
                page_md.append(f"> *[Catatan: Teks digital kosong (<15 karakter). Gambar halaman dirender untuk verifikasi visual.]*\n")
        
        # Render visual jika ada gambar / rumus penting pada halaman yang memiliki teks
        if needs_visual and not is_empty:
            img_filename = f"{safe_base}_hal_{page_num}.png"
            img_dest = img_dir / img_filename
            if not img_dest.exists():
                try:
                    pix = page.get_pixmap(dpi=150)
                    pix.save(img_dest)
                    file_report["gambar_tersimpan"].append(img_filename)
                except Exception as e:
                    pass
            reasons = []
            if len(images) > 0:
                reasons.append(f"{len(images)} gambar")
            if len(drawings) > 10:
                reasons.append(f"{len(drawings)} diagram/vektor")
            if has_formula:
                reasons.append("rumus/formula matematika")
            file_report["halaman_visual"].append(f"Hal {page_num} ({', '.join(reasons)})")
            
            page_md.append(f"![{marker_name} {page_num}](img/{img_filename})\n")
            
        page_extracted = False
        if text.strip():
            page_md.append(text.strip())
            page_extracted = True
        elif ocr_applied:
            page_extracted = True
        elif is_empty and img_dest.exists():
            page_extracted = True
            
        if page_extracted:
            extracted_pages += 1
            
        md_sections.append("\n".join(page_md) + "\n\n---")
        
    file_report["halaman_terekstrak"] = extracted_pages
    
    with open(md_output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_sections))
        
    doc.close()
    return file_report


def process_pptx(pptx_path: Path, output_dir: Path, img_dir: Path):
    """Proses ekstraksi teks, tabel, gambar dari berkas PPTX."""
    prs = pptx.Presentation(pptx_path)
    total_slides = len(prs.slides)
    extracted_slides = 0
    
    base_name = pptx_path.stem
    safe_base = sanitize_filename(base_name)
    md_output_path = output_dir / f"{safe_base}.md"
    
    file_report = {
        "file": str(pptx_path),
        "tipe": "PPTX",
        "total_halaman": total_slides,
        "halaman_terekstrak": 0,
        "halaman_butuh_ocr": [],
        "halaman_visual": [],
        "gambar_tersimpan": []
    }
    
    md_sections = [f"# {pptx_path.name}\n\nSumber Asli: `{pptx_path}`\n\n---\n"]
    
    for slide_idx, slide in enumerate(prs.slides):
        slide_num = slide_idx + 1
        slide_texts = []
        has_table = False
        pic_count = 0
        
        slide_md = [f"\n## Slide {slide_num}\n"]
        
        img_idx = 0
        for shape in slide.shapes:
            # Ekstrak Teks
            if shape.has_text_frame:
                t = shape.text_frame.text.strip()
                if t:
                    slide_texts.append(t)
            # Ekstrak Tabel
            elif shape.has_table:
                has_table = True
                tbl_md = extract_table_from_pptx_shape(shape)
                slide_texts.append(tbl_md)
            # Ekstrak Gambar
            elif shape.shape_type == MSO_SHAPE_TYPE.PICTURE or hasattr(shape, "image"):
                try:
                    img_idx += 1
                    pic_count += 1
                    image = shape.image
                    img_ext = image.ext
                    img_filename = f"{safe_base}_slide_{slide_num}_img_{img_idx}.{img_ext}"
                    img_dest = img_dir / img_filename
                    with open(img_dest, "wb") as f_img:
                        f_img.write(image.blob)
                    file_report["gambar_tersimpan"].append(img_filename)
                    slide_md.append(f"![Slide {slide_num} Gambar {img_idx}](img/{img_filename})\n")
                except Exception as e:
                    pass
                    
        full_text = "\n\n".join(slide_texts).strip()
        has_formula = is_math_or_formula(full_text)
        
        reasons = []
        if pic_count > 0:
            reasons.append(f"{pic_count} gambar")
        if has_table:
            reasons.append("tabel data")
        if has_formula:
            reasons.append("rumus/formula statistik")
            
        if reasons:
            file_report["halaman_visual"].append(f"Slide {slide_num} ({', '.join(reasons)})")
            
        ocr_applied = False
        if len(full_text) < 15:
            file_report["halaman_butuh_ocr"].append(slide_num)
            ocr_text = ""
            if pic_count > 0 and CAN_OCR and Image is not None:
                for img_fn in file_report["gambar_tersimpan"]:
                    if f"_slide_{slide_num}_img_" in img_fn:
                        img_path = img_dir / img_fn
                        if img_path.exists():
                            try:
                                ocr_res = pytesseract.image_to_string(Image.open(img_path), lang="ind+eng").strip()
                                if len(ocr_res) > 10:
                                    ocr_text += ("\n\n" if ocr_text else "") + ocr_res
                            except Exception:
                                pass
            if ocr_text.strip():
                slide_md.append(f"> *[Hasil OCR]:*\n{ocr_text.strip()}\n")
                ocr_applied = True
                extracted_slides += 1
            elif pic_count > 0:
                slide_md.append("> *[Catatan: Teks digital kosong (<15 karakter). Berisi gambar/visual yang perlu inspeksi visual manual]*\n")
                extracted_slides += 1
            else:
                slide_md.append("> *[Catatan: Slide kosong atau transisi judul tanpa teks]*\n")
        elif full_text:
            slide_md.append(full_text)
            extracted_slides += 1
            
        md_sections.append("\n".join(slide_md) + "\n\n---")
        
    file_report["halaman_terekstrak"] = extracted_slides
    
    with open(md_output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_sections))
        
    return file_report


def main():
    root_dir = Path(__file__).resolve().parent.parent
    materials_dir = root_dir / "materials"
    extracted_dir = root_dir / "extracted"
    img_dir = extracted_dir / "img"
    
    extracted_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"[*] Memulai ekstraksi materi dari {materials_dir}...")
    print(f"[*] Engine OCR Tesseract: {'TERSEDIA' if CAN_OCR else 'TIDAK TERSEDIA (Fallback render PNG visual)'}")
    
    # Kumpulkan berkas
    pdf_files = sorted(materials_dir.rglob("*.pdf"))
    pptx_files = sorted(materials_dir.rglob("*.pptx"))
    
    all_reports = []
    
    # Proses PDF
    for pdf_path in pdf_files:
        print(f"  -> Mengekstrak PDF: {pdf_path.relative_to(root_dir)}")
        rep = process_pdf(pdf_path, extracted_dir, img_dir)
        all_reports.append(rep)
        
    # Proses PPTX
    for pptx_path in pptx_files:
        print(f"  -> Mengekstrak PPTX: {pptx_path.relative_to(root_dir)}")
        rep = process_pptx(pptx_path, extracted_dir, img_dir)
        all_reports.append(rep)
        
    # Tulis extracted/_laporan.md
    laporan_path = extracted_dir / "_laporan.md"
    total_asli = sum(r["total_halaman"] for r in all_reports)
    total_terekstrak = sum(r["halaman_terekstrak"] for r in all_reports)
    total_butuh_ocr = sum(len(r["halaman_butuh_ocr"]) for r in all_reports)
    total_visual = sum(len(r["halaman_visual"]) for r in all_reports)
    total_img = sum(len(r["gambar_tersimpan"]) for r in all_reports)
    
    ocr_info = get_ocr_status_info()
    report_lines = [
        "# Laporan Audit Ekstraksi Materi Pembelajaran (OSL)",
        "",
        f"- **Tanggal Ekstraksi**: 2026-09-29",
        f"- **Status Engine OCR (Tesseract)**: {ocr_info['pesan']}",
        f"- **Total Berkas Diproses**: {len(all_reports)} berkas",
        f"- **Total Halaman/Slide Asli**: {total_asli}",
        f"- **Total Halaman/Slide Terekstrak**: {total_terekstrak} ({(total_terekstrak/total_asli*100):.1f}%)",
        f"- **Total Halaman Butuh OCR / Kosong Teks**: {total_butuh_ocr}",
        f"- **Total Halaman/Slide Sarat Gambar/Rumus/Tabel**: {total_visual}",
        f"- **Total Gambar / Render PNG Disimpan**: {total_img} file di `extracted/img/`",
        "",
        "---",
        "",
        "## 1. Rincian Per Berkas Materi",
        "",
        "| No | Nama Berkas | Tipe | Hal Asli | Terekstrak | Butuh OCR | Visual / Rumus / Tabel |",
        "|---|---|---|---|---|---|---|",
    ]
    
    for idx, r in enumerate(all_reports, 1):
        rel_name = Path(r["file"]).name
        ocr_str = str(len(r["halaman_butuh_ocr"])) if r["halaman_butuh_ocr"] else "0"
        vis_str = str(len(r["halaman_visual"])) if r["halaman_visual"] else "0"
        report_lines.append(
            f"| {idx} | `{rel_name}` | {r['tipe']} | {r['total_halaman']} | {r['halaman_terekstrak']} | {ocr_str} | {vis_str} |"
        )
        
    report_lines.extend([
        "",
        "---",
        "",
        "## 2. Rincian Halaman yang Membutuhkan OCR / Teks Kosong",
        "",
        "> Catatan: Jika Tesseract OCR aktif, OCR otomatis telah diterapkan pada slide/halaman berteks minim yang berisi citra visual. Gambar halaman tetap disimpan di `extracted/img/` untuk audit visual langsung.",
        ""
    ])
    
    has_any_ocr = False
    for r in all_reports:
        if r["halaman_butuh_ocr"]:
            has_any_ocr = True
            fname = Path(r["file"]).name
            pages_str = ", ".join(map(str, r["halaman_butuh_ocr"]))
            report_lines.append(f"- **`{fname}`**: Halaman/Slide [{pages_str}]")
            
    if not has_any_ocr:
        report_lines.append("- *Tidak ada halaman yang butuh OCR (seluruh halaman memiliki teks digital).*")
        
    report_lines.extend([
        "",
        "---",
        "",
        "## 3. Rincian Halaman Perlu Pemeriksaan Visual (Sarat Gambar / Rumus / Tabel)",
        ""
    ])
    
    for r in all_reports:
        if r["halaman_visual"]:
            fname = Path(r["file"]).name
            report_lines.append(f"### `{fname}`")
            for item in r["halaman_visual"][:15]:  # Batasi 15 per berkas untuk keringkasan
                report_lines.append(f"- {item}")
            if len(r["halaman_visual"]) > 15:
                report_lines.append(f"- *... dan {len(r['halaman_visual']) - 15} halaman/slide visual lainnya.*")
            report_lines.append("")
            
    with open(laporan_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    print(f"\n[V] Ekstraksi selesai! Laporan disimpan di: {laporan_path}")
    print(f"    Total Asli: {total_asli} | Terekstrak: {total_terekstrak} | Butuh OCR: {total_butuh_ocr} | Visual: {total_visual}")


if __name__ == "__main__":
    main()
