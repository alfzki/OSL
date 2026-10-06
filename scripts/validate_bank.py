#!/usr/bin/env python3
"""
scripts/validate_bank.py
Validator skema dan integritas bank soal (bank/soal.json).
Menolak butir soal apabila:
1. Sumber kosong atau tidak valid
2. ID duplikat
3. Soal nyaris identik (deteksi kemiripan leksikal > 85%)
4. Kunci PG tidak ada dalam daftar opsi
5. Field wajib hilang
6. Asal 'suplemen' tanpa label '[SUPLEMEN]'
"""

import sys
import json
import re
import difflib
from pathlib import Path
from typing import List, Dict, Any, Tuple

REQUIRED_FIELDS = [
    "id", "topik", "bab", "jenis", "kesulitan",
    "soal", "jawaban", "penjelasan", "sumber",
    "asal", "keyakinan", "status_review"
]

VALID_JENIS = {"pg", "isian", "esai", "hitungan"}
VALID_KESULITAN = {1, 2, 3}
VALID_ASAL = {"materi", "soal-lama", "suplemen"}
VALID_KEYAKINAN = {"tinggi", "sedang", "rendah"}
VALID_STATUS_REVIEW = {"belum", "lulus", "gagal"}


def normalize_text_for_similarity(text: str) -> str:
    """Normalisasi teks untuk menghitung kemiripan (fuzzy duplicate)."""
    text = text.lower()
    text = re.sub(r'[\W_]+', ' ', text)
    stop_words = {
        "apakah", "bagaimana", "berikut", "ini", "yang", "dan", "di", "ke",
        "dari", "adalah", "merupakan", "menurut", "anda", "pemahaman",
        "dalam", "untuk", "pada", "oleh", "suatu", "sebutkan", "jelaskan",
        "tentang", "atau", "apa", "berapa", "hitunglah", "tentukan"
    }
    # Pertahankan token alfanumerik termasuk simbol indikator 2 karakter (p0, p1, p2, it, ib, dll)
    tokens = [w for w in text.split() if w not in stop_words]
    return " ".join(tokens)


def calculate_similarity(text1: str, text2: str) -> float:
    """Hitung rasio kesamaan urutan karakter/kata."""
    norm1 = normalize_text_for_similarity(text1)
    norm2 = normalize_text_for_similarity(text2)
    if not norm1 or not norm2:
        return 0.0
    return difflib.SequenceMatcher(None, norm1, norm2).ratio()


def is_duplicate_or_near_identical(item_a: Dict[str, Any], item_b: Dict[str, Any]) -> Tuple[bool, float, str]:
    """Deteksi duplikasi atau kemiripan ekstrem tanpa false positive pada indikator berbeda."""
    soal_a = item_a.get("soal", "")
    soal_b = item_b.get("soal", "")
    
    # 1. Exact raw match
    if soal_a.strip().lower() == soal_b.strip().lower():
        return True, 1.0, "Teks soal persis identik"
        
    norm_a = normalize_text_for_similarity(soal_a)
    norm_b = normalize_text_for_similarity(soal_b)
    
    if not norm_a or not norm_b:
        return False, 0.0, ""
        
    # 2. Normalized exact match
    if norm_a == norm_b:
        jawaban_a = str(item_a.get("jawaban", "")).strip().lower()
        jawaban_b = str(item_b.get("jawaban", "")).strip().lower()
        if jawaban_a == jawaban_b:
            return True, 1.0, "Teks soal dan kunci jawaban ternormalisasi identik"
        else:
            return True, 1.0, "Teks pertanyaan ternormalisasi identik"
            
    sim = difflib.SequenceMatcher(None, norm_a, norm_b).ratio()
    
    # 3. High fuzzy similarity (>= 0.85)
    if sim >= 0.85:
        jawaban_a = str(item_a.get("jawaban", "")).strip().lower()
        jawaban_b = str(item_b.get("jawaban", "")).strip().lower()
        
        tokens_a = set(norm_a.split())
        tokens_b = set(norm_b.split())
        diff_tokens = (tokens_a ^ tokens_b)
        
        # Pengecekan indikator statistik spesifik dan angka unik
        distinguishing_markers = {"p0", "p1", "p2", "it", "ib", "tpk", "ntp", "ihk", "sbh", "fgt", "lorenz", "gini"}
        has_distinguishing_indicator = any(m in diff_tokens for m in distinguishing_markers)
        has_diff_numbers = any(re.search(r'\d', tok) for tok in diff_tokens)
        
        # Jika jawaban berbeda dan terdapat parameter/indikator/angka pembeda yang jelas, bukan duplikat
        if (jawaban_a != jawaban_b) and (has_distinguishing_indicator or has_diff_numbers):
            return False, sim, ""
            
        return True, sim, f"Kemiripan teks {sim*100:.1f}% tanpa pembeda indikator/jawaban yang cukup"
        
    return False, sim, ""


def validate_item(idx: int, item: Dict[str, Any]) -> List[str]:
    """Validasi skema dan aturan semantik pada satu butir soal."""
    errors = []
    item_id = item.get("id", f"INDEX_{idx}")
    
    # 1. Cek kelengkapan field wajib
    missing = [f for f in REQUIRED_FIELDS if f not in item]
    if missing:
        errors.append(f"[{item_id}] Field wajib hilang: {', '.join(missing)}")
        
    # 2. Cek tipe dan nilai enum
    jenis = item.get("jenis")
    if jenis not in VALID_JENIS:
        errors.append(f"[{item_id}] Nilai 'jenis' tidak valid: '{jenis}'. Wajib salah satu dari {VALID_JENIS}")
        
    kesulitan = item.get("kesulitan")
    if kesulitan not in VALID_KESULITAN:
        errors.append(f"[{item_id}] Nilai 'kesulitan' harus bernilai 1, 2, atau 3 (diterima: '{kesulitan}')")
        
    asal = item.get("asal")
    if asal not in VALID_ASAL:
        errors.append(f"[{item_id}] Nilai 'asal' tidak valid: '{asal}'. Wajib salah satu dari {VALID_ASAL}")
        
    keyakinan = item.get("keyakinan")
    if keyakinan not in VALID_KEYAKINAN:
        errors.append(f"[{item_id}] Nilai 'keyakinan' tidak valid: '{keyakinan}'. Wajib salah satu dari {VALID_KEYAKINAN}")
        
    status_review = item.get("status_review")
    if status_review not in VALID_STATUS_REVIEW:
        errors.append(f"[{item_id}] Nilai 'status_review' tidak valid: '{status_review}'. Wajib salah satu dari {VALID_STATUS_REVIEW}")
        
    # 3. Validasi sumber
    sumber = item.get("sumber")
    if not isinstance(sumber, list) or len(sumber) == 0:
        errors.append(f"[{item_id}] 'sumber' wajib berupa array/list dan tidak boleh kosong")
    else:
        for s_idx, s in enumerate(sumber):
            if not isinstance(s, str) or not s.strip():
                errors.append(f"[{item_id}] 'sumber[{s_idx}]' tidak boleh berupa string kosong")
            else:
                has_page_ref = bool(re.search(r'(slide|hal|halaman)\s*\.?\s*\d+', s, re.IGNORECASE))
                is_suplemen_source = "[suplemen" in s.lower() or asal == "suplemen"
                if not has_page_ref and not is_suplemen_source:
                    errors.append(
                        f"[{item_id}] 'sumber[{s_idx}]' ('{s}') wajib mencantumkan nomor slide atau halaman (contoh: '[nama-file, slide/hal. N]')"
                    )
                
    # 4. Validasi opsi dan kunci untuk PG
    if jenis == "pg":
        opsi = item.get("opsi")
        jawaban = str(item.get("jawaban", "")).strip()
        
        if not opsi:
            errors.append(f"[{item_id}] Soal jenis 'pg' wajib menyertakan field 'opsi'")
        elif isinstance(opsi, dict):
            # Format opsi standar: {"A": "...", "B": "...", ...}
            if jawaban not in opsi:
                errors.append(
                    f"[{item_id}] Kunci jawaban '{jawaban}' tidak ditemukan dalam opsi dictionary {list(opsi.keys())}"
                )
        elif isinstance(opsi, list):
            # Format opsi list: ["A. ...", "B. ..."]
            valid_keys = []
            for opt in opsi:
                match = re.match(r"^([A-Ea-e])[\.\)\s]", str(opt).strip())
                if match:
                    valid_keys.append(match.group(1).upper())
                else:
                    valid_keys.append(str(opt).strip())
            if jawaban.upper() not in valid_keys and jawaban not in opsi:
                errors.append(
                    f"[{item_id}] Kunci jawaban '{jawaban}' tidak cocok dengan opsi list yang disediakan"
                )
        else:
            errors.append(f"[{item_id}] Format 'opsi' harus berupa dictionary atau list")
            
    # 5. Aturan Asal Suplemen
    if asal == "suplemen":
        combined_text = f"{item.get('soal', '')} {item.get('penjelasan', '')} {' '.join(str(s) for s in item.get('sumber', []))}"
        if "[SUPLEMEN]" not in combined_text:
            errors.append(
                f"[{item_id}] Butir soal dengan asal 'suplemen' WAJIB menyertakan label '[SUPLEMEN]' pada teks soal, penjelasan, atau sumber"
            )
            
    # 6. Validasi non-empty teks
    for str_field in ["soal", "jawaban", "penjelasan", "topik"]:
        val = item.get(str_field)
        if not isinstance(val, str) or not val.strip():
            errors.append(f"[{item_id}] Teks '{str_field}' tidak boleh kosong")
            
    return errors


def validate_bank(file_path: Path) -> Tuple[bool, List[str]]:
    """Validasi keseluruhan berkas bank soal."""
    if not file_path.exists():
        return False, [f"Berkas bank soal tidak ditemukan: {file_path}"]
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Format JSON pada {file_path} rusak/invalid: {e}"]
        
    if not isinstance(data, list):
        return False, [f"Root bank soal harus berupa array/list JSON. Ditemukan: {type(data).__name__}"]
        
    errors = []
    ids_seen = {}
    
    # Validasi per item
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"Elemen pada index {idx} bukan objek JSON: {item}")
            continue
            
        item_id = item.get("id")
        # Cek ID duplikat
        if item_id:
            if item_id in ids_seen:
                errors.append(
                    f"Duplikasi ID terdeteksi: '{item_id}' digunakan pada index {ids_seen[item_id]} dan index {idx}"
                )
            else:
                ids_seen[item_id] = idx
                
        item_errors = validate_item(idx, item)
        errors.extend(item_errors)
        
    # Cek kemiripan soal (Fuzzy Collision)
    total_items = len(data)
    for i in range(total_items):
        item_a = data[i]
        if not isinstance(item_a, dict) or "soal" not in item_a:
            continue
        soal_a = item_a.get("soal", "")
        id_a = item_a.get("id", f"Item_{i}")
        
        for j in range(i + 1, total_items):
            item_b = data[j]
            if not isinstance(item_b, dict) or "soal" not in item_b:
                continue
            soal_b = item_b.get("soal", "")
            id_b = item_b.get("id", f"Item_{j}")
            
            is_dup, sim, reason = is_duplicate_or_near_identical(item_a, item_b)
            if is_dup:
                errors.append(
                    f"Soal duplikat/nyaris identik ({reason}) antara [{id_a}] dan [{id_b}]:\n"
                    f"   A: \"{soal_a[:80]}...\"\n"
                    f"   B: \"{soal_b[:80]}...\""
                )
                
    is_valid = len(errors) == 0
    return is_valid, errors


def main():
    root_dir = Path(__file__).resolve().parent.parent
    target_path = root_dir / "bank" / "soal.json"
    
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
        
    print(f"[*] Menjalankan validasi bank soal: {target_path}")
    is_valid, errors = validate_bank(target_path)
    
    if is_valid:
        with open(target_path, "r", encoding="utf-8") as f:
            total = len(json.load(f))
        print(f"\n[SUKSES] Seluruh {total} butir soal valid dan memenuhi seluruh aturan integritas skema!")
        sys.exit(0)
    else:
        print(f"\n[GAGAL] Ditemukan {len(errors)} pelanggaran aturan integritas:")
        for idx, err in enumerate(errors, 1):
            print(f"  {idx}. {err}")
        print("\nSilakan perbaiki kesalahan di atas sebelum melanjutkan.")
        sys.exit(1)


if __name__ == "__main__":
    main()
