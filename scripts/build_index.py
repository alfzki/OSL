#!/usr/bin/env python3
"""
scripts/build_index.py
Membangun indeks materi terstruktur (index/materi.json) dari teks yang telah diekstrak.
Setiap elemen memuat: bab/file, slide/halaman, judul, ringkasan 1-2 kalimat,
kata kunci, dan format rujukan sumber resmi [nama-file, slide/hal. N].
Juga menyediakan antarmuka pencarian CLI instan agar agen dapat mencari konteks
secara presisi tanpa memuat seluruh berkas.
"""

import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any

# Stopwords sederhana Bahasa Indonesia & Inggris untuk ekstraksi kata kunci
STOPWORDS = {
    "dan", "di", "ke", "dari", "yang", "pada", "untuk", "dengan", "adalah", "ini",
    "itu", "atau", "sebagai", "dalam", "bisa", "oleh", "suatu", "tidak", "akan",
    "juga", "antara", "serta", "terhadap", "secara", "lebih", "dapat", "bagi",
    "harus", "hanya", "namun", "karena", "maka", "tentang", "slide", "halaman",
    "catatan", "gambar", "pertemuan", "the", "and", "of", "to", "in", "for", "is",
    "on", "that", "by", "this", "with", "from", "be", "are", "at", "as", "an"
}

STATISTICAL_TERMS = {
    "kemiskinan", "ketimpangan", "gini", "lorenz", "fgt", "p0", "p1", "p2",
    "garis kemiskinan", "makanan", "non-makanan", "dklm", "headcount",
    "ketenagakerjaan", "sakernas", "icls", "angkatan kerja", "pengangguran",
    "tpt", "tpak", "setengah pengangguran", "pekerja paruh waktu", "formal", "informal",
    "kesehatan", "morbiditas", "mortalitas", "imunisasi", "stunting", "sdgs",
    "tpb", "aki", "akb", "u5mr", "jamkesmas", "bpjs", "rawat inap", "rawat jalan",
    "produksi", "ntp", "nilai tukar petani", "it", "ib", "hortikultura", "palawija",
    "perkebunan", "peternakan", "perikanan", "spdt", "shped", "harga produsen",
    "perdagangan", "harga", "ihk", "inflasi", "laspeyres", "paasche", "sbh",
    "survei biaya hidup", "diagram timbang", "month to month", "year on year",
    "year to date", "inti", "bergejolak", "diatur pemerintah", "poldis", "mppa", "mpp",
    "ekspor", "impor", "fob", "cif", "merchanting", "sna 2008", "trade openness",
    "neraca perdagangan", "terms of trade", "pariwisata", "tpk", "wisman", "wisnus",
    "tingkat penghunian kamar", "panjang menginap", "akomodasi", "malam kamar"
}


def clean_snippet(text: str) -> str:
    """Bersihkan teks dari tautan gambar markdown dan markup berlebih."""
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'>.*?\n', '', text)
    text = re.sub(r'#+\s*', '', text)
    text = re.sub(r'\|.*?\|', '', text)  # buang tabel raw
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_keywords(text: str, max_keywords: int = 8) -> List[str]:
    """Ekstrak kata kunci penting dari teks slide/halaman."""
    lower_text = text.lower()
    found_terms = []
    
    # 1. Cari exact match dari kamus istilah statistik
    for term in sorted(STATISTICAL_TERMS, key=lambda x: -len(x)):
        if re.search(r'\b' + re.escape(term) + r'\b', lower_text):
            found_terms.append(term)
            if len(found_terms) >= max_keywords:
                break
                
    # 2. Tambahkan kata-kata unik bermakna jika masih kurang
    words = re.findall(r'\b[a-zA-Z]{4,}\b', lower_text)
    freq = {}
    for w in words:
        if w not in STOPWORDS and w not in found_terms:
            freq[w] = freq.get(w, 0) + 1
            
    sorted_words = sorted(freq.keys(), key=lambda w: freq[w], reverse=True)
    for w in sorted_words:
        if len(found_terms) >= max_keywords:
            break
        found_terms.append(w)
        
    return found_terms


def generate_summary(text: str) -> str:
    """Buat ringkasan 1-2 kalimat dari teks."""
    clean = clean_snippet(text)
    # Bersihkan nomor slide/halaman di awal teks
    clean = re.sub(r'^\d+\s+', '', clean).strip()
    if not clean:
        return "Slide visual atau tanpa teks naratif."
        
    # Ambil 1-2 kalimat awal
    sentences = re.split(r'(?<=[.!?])\s+', clean)
    summary_sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    
    if not summary_sentences:
        return clean[:120] + "..." if len(clean) > 120 else clean
        
    summary = " ".join(summary_sentences[:2])
    if len(summary) > 200:
        summary = summary[:197] + "..."
    return summary


def extract_title(unit_body: str, unit_type: str, unit_num: int) -> str:
    """Ekstrak judul deskriptif dari isi unit, melewati nomor halaman/slide atau tabel."""
    lines = [l.strip() for l in unit_body.splitlines() if l.strip()]
    
    # 1. Prioritas utama: baris heading Markdown (#, ##, ###)
    for l in lines:
        if l.startswith("#") and not l.startswith("## " + unit_type):
            clean_h = re.sub(r'^#+\s*', '', l).strip()
            if clean_h and not clean_h.isdigit() and len(clean_h) > 2:
                return clean_h[:77] + "..." if len(clean_h) > 80 else clean_h
                
    # 2. Prioritas kedua: baris teks substantif pertama (bukan gambar, blockquote, tabel, garis pembatas)
    for l in lines:
        if l.startswith("![") or l.startswith(">") or l.startswith("|") or l.startswith("---") or l.startswith("***"):
            continue
        clean_l = re.sub(r'^#+\s*', '', l).strip()
        # Lewati digit murni (nomor slide / halaman) atau simbol pendek
        if clean_l.isdigit() or len(clean_l) <= 2 or clean_l in ["...", "---"]:
            continue
        if re.match(r'^(slide|halaman|page)\s*\d+$', clean_l, re.IGNORECASE):
            continue
        return clean_l[:77] + "..." if len(clean_l) > 80 else clean_l
        
    return f"{unit_type} {unit_num}"


def parse_extracted_file(md_path: Path) -> List[Dict[str, Any]]:
    """Urai berkas markdown hasil ekstraksi menjadi segmen-segmen per slide/halaman."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Ambil judul berkas asli
    header_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
    file_title = header_match.group(1).strip() if header_match else md_path.stem
    
    source_match = re.search(r'Sumber Asli:\s*`(.+?)`', content)
    original_source = source_match.group(1).strip() if source_match else str(md_path)
    original_filename = Path(original_source).name
    
    # Pisahkan per slide / halaman
    pattern = r'(?m)^##\s+(Slide|Halaman)\s+(\d+)\s*$'
    splits = re.split(pattern, content)
    
    segments = []
    # splits format: [preamble, type_1, num_1, body_1, type_2, num_2, body_2, ...]
    if len(splits) > 1:
        for i in range(1, len(splits), 3):
            unit_type = splits[i]
            unit_num = int(splits[i+1])
            unit_body = splits[i+2].strip() if i+2 < len(splits) else ""
            
            clean_body = clean_snippet(unit_body)
            title = extract_title(unit_body, unit_type, unit_num)
                
            unit_abbr = "slide" if unit_type == "Slide" else "hal."
            rujukan = f"[{original_filename}, {unit_abbr} {unit_num}]"
            
            summary = generate_summary(unit_body)
            keywords = extract_keywords(unit_body)
            
            seg_id = f"{md_path.stem}_{unit_type}_{unit_num}"
            
            segments.append({
                "id": seg_id,
                "file_sumber": original_filename,
                "path_sumber_asli": original_source,
                "berkas_ekstraksi": f"extracted/{md_path.name}",
                "tipe_unit": unit_type,
                "nomor_unit": unit_num,
                "judul": title,
                "ringkasan": summary,
                "kata_kunci": keywords,
                "rujukan_sumber": rujukan,
                "panjang_karakter": len(clean_body)
            })
            
    return segments


def build_index():
    root_dir = Path(__file__).resolve().parent.parent
    extracted_dir = root_dir / "extracted"
    index_dir = root_dir / "index"
    index_dir.mkdir(parents=True, exist_ok=True)
    
    output_index_file = index_dir / "materi.json"
    
    md_files = sorted([f for f in extracted_dir.glob("*.md") if f.name != "_laporan.md"])
    print(f"[*] Membangun indeks materi dari {len(md_files)} berkas di {extracted_dir}...")
    
    all_segments = []
    file_stats = {}
    
    for md_file in md_files:
        segs = parse_extracted_file(md_file)
        all_segments.extend(segs)
        file_stats[md_file.name] = len(segs)
        print(f"  -> {md_file.name}: {len(segs)} segmen diindeks")
        
    index_payload = {
        "metadata": {
            "total_berkas": len(md_files),
            "total_segmen": len(all_segments),
            "tanggal_dibuat": "2026-09-29",
            "aturan_penggunaan": "Cari segmen relevan terlebih dahulu. Muat hanya potongan slide/halaman yang dibutuhkan, jangan memuat seluruh berkas."
        },
        "segmen": all_segments
    }
    
    with open(output_index_file, "w", encoding="utf-8") as f:
        json.dump(index_payload, f, ensure_ascii=False, indent=2)
        
    print(f"\n[SUKSES] Indeks berhasil dibangun: {output_index_file}")
    print(f"         Total {len(all_segments)} segmen slide/halaman terdata.")
    return output_index_file


def search_index(query: str, limit: int = 5):
    """Pencarian cepat kata kunci di dalam indeks."""
    root_dir = Path(__file__).resolve().parent.parent
    index_file = root_dir / "index" / "materi.json"
    
    if not index_file.exists():
        print("Indeks belum ada. Menjalankan pembuatan indeks terlebih dahulu...")
        build_index()
        
    with open(index_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    q_lower = query.lower()
    terms = q_lower.split()
    
    matches = []
    for seg in data["segmen"]:
        score = 0
        search_blob = f"{seg['judul']} {seg['ringkasan']} {' '.join(seg['kata_kunci'])} {seg['file_sumber']}".lower()
        
        # Exact match query
        if q_lower in search_blob:
            score += 10
            
        # Per-term match
        for t in terms:
            if t in seg["judul"].lower():
                score += 5
            elif t in [k.lower() for k in seg["kata_kunci"]]:
                score += 4
            elif t in seg["ringkasan"].lower():
                score += 2
                
        if score > 0:
            matches.append((score, seg))
            
    matches.sort(key=lambda x: x[0], reverse=True)
    
    print(f"\n=== Hasil Pencarian Indeks untuk: '{query}' ({len(matches)} kecocokan) ===")
    if not matches:
        print("Tidak ditemukan segmen materi yang relevan.")
        return
        
    for idx, (score, m) in enumerate(matches[:limit], 1):
        print(f"\n{idx}. {m['rujukan_sumber']} (Skor Relevansi: {score})")
        print(f"   Judul     : {m['judul']}")
        print(f"   Ringkasan : {m['ringkasan']}")
        print(f"   Kata Kunci: {', '.join(m['kata_kunci'])}")
        print(f"   Lokasi    : {m['berkas_ekstraksi']}")


def main():
    parser = argparse.ArgumentParser(description="Pembangun & Penelusur Indeks Materi OSL")
    parser.add_argument("--build", action="store_true", help="Bangun ulang index/materi.json")
    parser.add_argument("--search", "-s", type=str, help="Cari kata kunci dalam materi")
    parser.add_argument("--limit", "-n", type=int, default=5, help="Jumlah hasil pencarian maksimal")
    
    args = parser.parse_args()
    
    if args.search:
        search_index(args.search, limit=args.limit)
    else:
        build_index()


if __name__ == "__main__":
    main()
