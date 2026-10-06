#!/usr/bin/env python3
"""
scripts/sample_check.py
Memilih sampel 10 butir soal acak (atau seluruhnya jika <= 10) dari bank/soal.json
untuk diinspeksi secara manual oleh pengguna atau reviewer, dengan penekanan khusus
pada verifikasi rumus, angka, dan sitasi sumber.
"""

import sys
import json
import random
import argparse
from pathlib import Path
from typing import List, Dict, Any


def format_item_card(idx: int, item: Dict[str, Any]) -> str:
    """Format satu butir soal ke dalam kartu inspeksi yang rapi."""
    card = []
    card.append(f"{'='*75}")
    card.append(f"INSPEKSI BUTIR #{idx}: [{item.get('id')}] - {item.get('topik')} ({item.get('bab')})")
    card.append(f"Jenis: {item.get('jenis').upper()} | Tingkat Kesulitan: {item.get('kesulitan')}/3 | Keyakinan: {item.get('keyakinan').upper()}")
    card.append(f"Asal: {item.get('asal').upper()} | Status Review Saat Ini: {item.get('status_review').upper()}")
    card.append(f"{'-'*75}")
    card.append("SOAL:")
    card.append(f"{item.get('soal')}\n")
    
    if item.get("jenis") == "pg" and "opsi" in item:
        card.append("OPSI PILIHAN:")
        opsi = item.get("opsi")
        if isinstance(opsi, dict):
            for k in sorted(opsi.keys()):
                card.append(f"  [{k}] {opsi[k]}")
        elif isinstance(opsi, list):
            for opt in opsi:
                card.append(f"  - {opt}")
        card.append("")
        
    card.append(f"KUNCI JAWABAN : {item.get('jawaban')}")
    card.append(f"PEMBAHASAN    : {item.get('penjelasan')}")
    card.append(f"SUMBER SITASI : {', '.join(item.get('sumber', []))}")
    card.append(f"{'-'*75}")
    card.append("CHECKLIST EVALUASI MANUAL:")
    card.append("  [ ] Sitasi sesuai dan tepat menunjuk halaman/slide sumber")
    card.append("  [ ] Fakta & definisi selaras dengan materi resmi")
    if item.get("jenis") == "hitungan":
        card.append("  [!] WAJIB HITUNGAN: Angka dan rumus telah diverifikasi dengan eksekusi kode")
    elif item.get("jenis") == "pg":
        card.append("  [ ] Opsi pengecoh (distraktor) logis dan bebas dari ambiguitas")
    elif item.get("jenis") == "isian":
        card.append("  [ ] Kunci isian singkat, spesifik, dan tidak menimbulkan ambiguitas sinonim")
    elif item.get("jenis") == "esai":
        card.append("  [ ] Rubrik esai memuat poin kunci konsep, metodologi, dan implikasi kebijakan")
    if item.get("asal") == "suplemen":
        card.append("  [!] ASAL SUPLEMEN: Wajib berlabel [SUPLEMEN] dan terpisah dari penjelasan utama")
    card.append("  [ ] Keputusan: [ ] LULUS   [ ] GAGAL / PERLU REVISI")
    card.append(f"{'='*75}\n")
    return "\n".join(card)


def sample_questions(bank_file: Path, sample_size: int = 10, jenis_filter: str = None, seed: int = None):
    """Pilih sampel butir soal dari bank soal."""
    if not bank_file.exists():
        print(f"ERROR: Berkas bank soal {bank_file} tidak ditemukan!", file=sys.stderr)
        sys.exit(1)
        
    with open(bank_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    if not isinstance(data, list) or len(data) == 0:
        print("Bank soal kosong.", file=sys.stderr)
        sys.exit(1)
        
    filtered = data
    if jenis_filter:
        filtered = [it for it in data if it.get("jenis") == jenis_filter.lower()]
        if not filtered:
            print(f"Tidak ada butir soal dengan jenis '{jenis_filter}'.", file=sys.stderr)
            sys.exit(1)
            
    if seed is not None:
        random.seed(seed)
        
    actual_size = min(sample_size, len(filtered))
    sampled = random.sample(filtered, actual_size)
    
    print(f"\n[*] Mengambil {actual_size} sampel butir soal dari total {len(filtered)} butir (Filter Jenis: {jenis_filter or 'Semua'})...\n")
    
    cards = []
    for idx, item in enumerate(sampled, 1):
        card_text = format_item_card(idx, item)
        print(card_text)
        cards.append(card_text)
        
    return cards


def main():
    parser = argparse.ArgumentParser(description="Pemeriksa Sampel Manual Bank Soal (OSL)")
    parser.add_argument("--n", type=int, default=10, help="Jumlah sampel soal yang diambil (default: 10)")
    parser.add_argument("--jenis", type=str, choices=["pg", "isian", "esai", "hitungan"], help="Filter jenis soal spesifik")
    parser.add_argument("--seed", type=int, help="Seed angka acak untuk reproducibility")
    parser.add_argument("--bank", type=str, default="bank/soal.json", help="Path ke berkas bank soal")
    
    args = parser.parse_args()
    root_dir = Path(__file__).resolve().parent.parent
    bank_path = root_dir / args.bank
    
    sample_questions(bank_path, sample_size=args.n, jenis_filter=args.jenis, seed=args.seed)


if __name__ == "__main__":
    main()
