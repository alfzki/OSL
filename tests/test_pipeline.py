#!/usr/bin/env python3
"""
tests/test_pipeline.py
Automated test suite verifying all OSL exam preparation infrastructure components:
1. Bank schema validator & semantic edge case testing
2. Source grounding & citation checks
3. Title extraction & search indexing
4. Backtest prediction engine (< 2 fallback and >= 2 evaluation)
5. Question sampling & checklist generator
6. Spaced repetition tracker integrity
"""

import sys
import os
import json
import subprocess
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from scripts.validate_bank import validate_bank, validate_item, is_duplicate_or_near_identical
from scripts.build_index import extract_title, search_index, parse_extracted_file
from scripts.backtest import (
    detect_past_exam_years,
    run_longitudinal_backtest,
    generate_syllabus_fallback_report,
    split_into_question_items,
    analyze_exam_dataset,
    TOPIC_DEFINITIONS
)
from scripts.extract import CAN_OCR, get_ocr_status_info


def test_validator_on_real_bank():
    print("[TEST 1] Testing validator on bank/soal.json...")
    bank_path = ROOT_DIR / "bank" / "soal.json"
    is_valid, errors = validate_bank(bank_path)
    assert is_valid, f"bank/soal.json failed validation: {errors}"
    with open(bank_path) as f:
        data = json.load(f)
    assert len(data) >= 10, f"Expected at least 10 items in sample bank, got {len(data)}"
    
    # Check coverage of types and origins
    jenis_set = {item["jenis"] for item in data}
    asal_set = {item["asal"] for item in data}
    assert {"pg", "isian", "esai", "hitungan"}.issubset(jenis_set), f"Missing jenis: {jenis_set}"
    assert {"materi", "soal-lama", "suplemen"}.issubset(asal_set), f"Missing asal: {asal_set}"
    print(f"  -> PASS: All {len(data)} items valid with complete coverage of types and origins.")


def test_validator_edge_cases():
    print("[TEST 2] Testing validator semantic edge cases and rejection rules...")
    
    base_item = {
        "id": "TEST-001",
        "topik": "Indikator Kemiskinan",
        "bab": "Pertemuan 8",
        "jenis": "pg",
        "kesulitan": 2,
        "soal": "Apa itu kemiskinan?",
        "opsi": {"A": "Pilihan A", "B": "Pilihan B"},
        "jawaban": "A",
        "penjelasan": "Penjelasan detail",
        "sumber": ["Pertemuan 8.pptx, slide 10"],
        "asal": "materi",
        "keyakinan": "tinggi",
        "status_review": "lulus"
    }
    
    # 1. Missing required field
    bad_item = dict(base_item)
    del bad_item["jawaban"]
    errs = validate_item(0, bad_item)
    assert any("Field wajib hilang" in e for e in errs), "Failed to catch missing field"
    
    # 2. Empty source list
    bad_item = dict(base_item, sumber=[])
    errs = validate_item(0, bad_item)
    assert any("tidak boleh kosong" in e for e in errs), "Failed to catch empty source list"
    
    # 3. Source missing slide or page number
    bad_item = dict(base_item, sumber=["Pertemuan 8 OSL.pptx"])
    errs = validate_item(0, bad_item)
    assert any("wajib mencantumkan nomor slide atau halaman" in e for e in errs), "Failed to catch source without slide/page"
    
    # 4. PG key not in options
    bad_item = dict(base_item, jawaban="C")
    errs = validate_item(0, bad_item)
    assert any("Kunci jawaban 'C' tidak ditemukan" in e for e in errs), "Failed to catch invalid PG key"
    
    # 5. Suplemen origin without [SUPLEMEN] label
    bad_item = dict(base_item, asal="suplemen", sumber=["[SUPLEMEN: ILO 2013], hal. 5"])
    bad_item["penjelasan"] = "Penjelasan tanpa label"
    bad_item["soal"] = "Teks soal tanpa label"
    # Wait: here sumber has [SUPLEMEN: ...] so it might be accepted. Let's remove [SUPLEMEN] from everywhere:
    bad_item["sumber"] = ["Publikasi Luar, hal. 10"]
    errs = validate_item(0, bad_item)
    assert any("WAJIB menyertakan label '[SUPLEMEN]'" in e for e in errs), "Failed to catch unlabeled suplemen"
    
    # 6. False collision prevention on statistical indicators (P0 vs P1)
    q1 = {"soal": "Berapakah nilai P0 dari data konsumsi berikut?", "jawaban": "0.15"}
    q2 = {"soal": "Berapakah nilai P1 dari data konsumsi berikut?", "jawaban": "0.04"}
    is_dup, sim, reason = is_duplicate_or_near_identical(q1, q2)
    assert not is_dup, f"False collision triggered on P0 vs P1! sim={sim}"
    
    # 7. True duplicate detection
    q3 = {"soal": "Berapakah nilai P0 dari data konsumsi berikut?", "jawaban": "0.15"}
    q4 = {"soal": "Berapakah nilai P0 dari data konsumsi berikut ini?", "jawaban": "0.15"}
    is_dup, sim, reason = is_duplicate_or_near_identical(q3, q4)
    assert is_dup, "True duplicate was not caught!"
    
    print("  -> PASS: All validator edge cases and semantic rejection rules verified.")


def test_index_quality():
    print("[TEST 3] Testing index quality and title extraction...")
    index_path = ROOT_DIR / "index" / "materi.json"
    assert index_path.exists(), "index/materi.json does not exist"
    
    with open(index_path) as f:
        data = json.load(f)
        
    segments = data["segmen"]
    assert len(segments) >= 600, f"Expected >= 600 segments, got {len(segments)}"
    
    # Check that no title is a bare number or empty or table row
    odd_titles = [s for s in segments if s["judul"].isdigit() or s["judul"] in ["---", ""] or s["judul"].startswith("|")]
    assert len(odd_titles) == 0, f"Found {len(odd_titles)} odd titles in index!"
    
    # Verify title extractor on sample
    sample_body = "1\n\nSUB TOPIK:\nPendahuluan\nIsu Global"
    title = extract_title(sample_body, "Slide", 2)
    assert title == "SUB TOPIK:", f"Expected 'SUB TOPIK:', got {title}"
    print(f"  -> PASS: Index contains {len(segments)} segments with 0 numeric/malformed titles.")


def test_backtest_pipeline():
    print("[TEST 4] Testing backtest pipeline (< 2 fallback & >= 2 hold-out evaluation)...")
    past_exams_dir = ROOT_DIR / "materials" / "past-exams"
    extracted_dir = ROOT_DIR / "extracted"
    exam_files = detect_past_exam_years(past_exams_dir, extracted_dir=extracted_dir)
    assert len(exam_files) == 1, f"Expected 1 official exam, got {len(exam_files)}"
    
    # 1. Fallback report generation
    test_rep_1 = ROOT_DIR / "docs" / "test_fallback_rep.md"
    generate_syllabus_fallback_report(exam_files, test_rep_1)
    assert test_rep_1.exists(), "Fallback report not created"
    with open(test_rep_1) as f:
        content = f.read()
    assert "BACKTEST DITANGGUHKAN" in content
    assert "16,67%" in content
    test_rep_1.unlink()
    
    # 2. Simulated multi-year backtest
    test_rep_2 = ROOT_DIR / "docs" / "test_multiyear_rep.md"
    sim_train = [("2021-2022", past_exams_dir / "soal_latihan_uas.md")]
    uas_target = (extracted_dir / "Soal_UAS_2022-2023.md") if (extracted_dir / "Soal_UAS_2022-2023.md").exists() else (past_exams_dir / "Soal UAS 2022-2023.pdf")
    sim_test = ("2022-2023", uas_target)
    run_longitudinal_backtest(sim_train, sim_test, test_rep_2)
    assert test_rep_2.exists(), "Multiyear report not created"
    with open(test_rep_2) as f:
        content = f.read()
    assert "Top-3 Topic Hit Rate" in content
    assert "Mean Absolute Error" in content
    test_rep_2.unlink()
    
    print("  -> PASS: Backtest pipeline verified for both fallback and evaluation branches.")


def test_tracker_integrity():
    print("[TEST 5] Testing progress/tracker.json integrity...")
    tracker_path = ROOT_DIR / "progress" / "tracker.json"
    with open(tracker_path) as f:
        tracker = json.load(f)
        
    bank_path = ROOT_DIR / "bank" / "soal.json"
    with open(bank_path) as f:
        bank = json.load(f)
        
    bank_ids = {item["id"] for item in bank}
    tracker_ids = set(tracker["riwayat_soal"].keys())
    assert bank_ids == tracker_ids, f"Bank IDs and tracker IDs mismatch: {bank_ids ^ tracker_ids}"
    assert tracker["metadata"]["interval_spaced_repetition_hari"] == [1, 3, 7, 14]
    print(f"  -> PASS: Tracker perfectly tracks all {len(bank_ids)} items with spaced repetition schedule.")


def test_ocr_engine_integration():
    print("[TEST 6] Testing OCR engine availability and integration...")
    assert shutil.which("tesseract") is not None, "Tesseract binary not found on PATH"
    assert CAN_OCR is True, "CAN_OCR flag should be True when tesseract and pytesseract are available"
    
    ocr_info = get_ocr_status_info()
    assert ocr_info["tersedia"] is True, "get_ocr_status_info reported ocr not available"
    assert "ind" in ocr_info["bahasa"] and "eng" in ocr_info["bahasa"], f"Expected ind and eng in languages, got {ocr_info['bahasa']}"
    
    laporan_path = ROOT_DIR / "extracted" / "_laporan.md"
    assert laporan_path.exists(), "extracted/_laporan.md does not exist"
    with open(laporan_path, encoding="utf-8") as f:
        laporan_text = f.read()
    assert "Tersedia" in laporan_text, "OCR status in _laporan.md should say 'Tersedia'"
    print(f"  -> PASS: Tesseract engine active ({ocr_info['pesan']}) and integrated into extraction reports.")


def test_exam_corpora_and_cross_evaluation():
    print("[TEST 7] Testing available past-exam corpora and cross-material evaluation...")
    latihan_path = ROOT_DIR / "materials" / "past-exams" / "soal_latihan_uas.md"
    uas_md_path = ROOT_DIR / "extracted" / "Soal_UAS_2022-2023.md"
    uas_pdf_path = ROOT_DIR / "materials" / "past-exams" / "Soal UAS 2022-2023.pdf"
    
    assert latihan_path.exists(), "materials/past-exams/soal_latihan_uas.md must exist"
    assert uas_md_path.exists() or uas_pdf_path.exists(), "Soal UAS 2022-2023 must exist in extracted/ or materials/past-exams/"
    
    # Test question parsing on both corpora with exact question counts
    uas_target = uas_md_path if uas_md_path.exists() else uas_pdf_path
    
    with open(latihan_path, encoding="utf-8") as f:
        latihan_raw = f.read()
    lat_items = split_into_question_items(latihan_raw)
    assert len(lat_items) == 50, f"Expected exactly 50 questions from soal_latihan_uas.md, got {len(lat_items)}"
    
    uas_items = split_into_question_items(uas_md_path.read_text(encoding="utf-8"))
    assert len(uas_items) == 42, f"Expected exactly 42 questions from Soal_UAS_2022-2023.md, got {len(uas_items)}"
    
    # Test edge case robustness of question splitter
    edge_text = """
# Intro Preamble
Berikut ini instruksi ujian yang panjangnya lebih dari 25 karakter.

##### Pertanyaan 1
Soal pertama dengan heading level 5.
- A. Opsi A
- B. Opsi B

1.Soal Tanpa Spasi Setelah Titik
Soal kedua dengan penomoran rapat.
- A. Opsi A
- B. Opsi B

Tabel Angka:
Inflasi perdesaan:
0.14
2.50

2. Soal Essay Ekonomi (Skor 30)
Jelaskan konsep berikut ini.
"""
    edge_split = split_into_question_items(edge_text)
    assert len(edge_split) == 3, f"Expected 3 question items from edge text (skipping preamble & decimal 0.14), got {len(edge_split)}"
    
    # Test cross-analysis metrics
    lat_stats = analyze_exam_dataset([latihan_path])
    uas_stats = analyze_exam_dataset([uas_target])
    
    # Verify accurate item types (PG vs Essay)
    assert lat_stats["jenis_counts"]["pg"] == 50, f"Expected 50 PG questions in latihan, got {lat_stats['jenis_counts']}"
    assert uas_stats["jenis_counts"]["pg"] == 40, f"Expected 40 PG questions in UAS, got {uas_stats['jenis_counts']['pg']}"
    assert uas_stats["jenis_counts"]["esai"] == 2, f"Expected 2 essay questions in UAS, got {uas_stats['jenis_counts']['esai']}"
    
    pw = lat_stats["bab_weights"]
    pr = lat_stats["ranked_topics"]
    aw = uas_stats["bab_weights"]
    ar = uas_stats["ranked_topics"]
    
    top_5_hits = sum(1 for b in pr[:5] if b in ar[:5])
    top_5_hit_rate = (top_5_hits / 5) * 100
    mae = sum(abs(pw[b] - aw[b]) for b in TOPIC_DEFINITIONS) / len(TOPIC_DEFINITIONS)
    
    assert top_5_hit_rate >= 60.0, f"Expected Top-5 hit rate >= 60%, got {top_5_hit_rate}%"
    assert mae <= 12.0, f"Expected MAE <= 12%, got {mae}%"
    
    # Check that generated backtest report reflects both datasets
    backtest_rep = ROOT_DIR / "docs" / "laporan_backtest.md"
    assert backtest_rep.exists(), "docs/laporan_backtest.md does not exist"
    with open(backtest_rep, encoding="utf-8") as f:
        rep_text = f.read()
    assert "soal_latihan_uas.md" in rep_text
    assert "Soal_UAS_2022-2023" in rep_text
    assert "Evaluasi Silang Empiris" in rep_text
    
    print(f"  -> PASS: Both exam corpora parsed accurately (Latihan: {len(lat_items)}, UAS: {len(uas_items)}). Cross-eval MAE: {mae:.2f}%.")


def test_skills_integration_and_step3_deliverables():
    print("[TEST 8] Testing 9 skills integration & Step 3 syllabus deliverables...")
    skills_dir = ROOT_DIR / ".agents" / "skills"
    assert skills_dir.exists(), ".agents/skills directory does not exist"
    
    expected_skills = [
        "exam-sprint-builder",
        "exam-forecast",
        "exam-question-predictor",
        "study-assistant",
        "study-teach",
        "study-quiz",
        "study-mindmap",
        "study-feynman",
        "study-img"
    ]
    
    for skill_name in expected_skills:
        skill_path = skills_dir / skill_name
        assert skill_path.exists(), f"Skill directory missing: {skill_name}"
        skill_md = skill_path / "SKILL.md"
        assert skill_md.exists(), f"SKILL.md missing in {skill_name}"
        content = skill_md.read_text(encoding="utf-8")
        assert "name:" in content, f"YAML frontmatter 'name:' missing in {skill_name}/SKILL.md"
        assert "description:" in content, f"YAML frontmatter 'description:' missing in {skill_name}/SKILL.md"

    # Verify documentation integration
    for doc in ["README.md", "CLAUDE.md", "AGENTS.md"]:
        doc_content = (ROOT_DIR / doc).read_text(encoding="utf-8")
        for skill_name in expected_skills:
            assert skill_name in doc_content, f"Skill {skill_name} not documented in {doc}"

    # Verify Step 3 deliverables & documentation
    step3_doc = ROOT_DIR / "docs" / "konfirmasi_cakupan_silabus.md"
    assert step3_doc.exists(), "docs/konfirmasi_cakupan_silabus.md does not exist"
    step3_text = step3_doc.read_text(encoding="utf-8")
    for req in ["Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13"]:
        assert req in step3_text, f"{req} missing in docs/konfirmasi_cakupan_silabus.md"
    assert "Study Priority Matrix" in step3_text or "Matriks Prioritas" in step3_text
    assert "Human Checkpoint" in step3_text or "Titik Kendali Manusia" in step3_text
    assert "HIGH CONFIDENCE" in step3_text and "Contoh Soal Prediksi" in step3_text

    forecast_doc = ROOT_DIR / "forecasts" / "OSL" / "uas-forecast-2026.md"
    assert forecast_doc.exists(), "forecasts/OSL/uas-forecast-2026.md does not exist"
    fc_text = forecast_doc.read_text(encoding="utf-8")
    assert "Topic Weighting Matrix" in fc_text
    assert "Format & Blueprint Prediction" in fc_text

    # Verify study-assistant workspace state contract
    val_script = ROOT_DIR / ".agents" / "skills" / "study-assistant" / "scripts" / "validate_workspace.py"
    res = subprocess.run([sys.executable, str(val_script), str(ROOT_DIR), "-q"], capture_output=True, text=True)
    assert res.returncode == 0, f"validate_workspace.py failed on study workspace: {res.stderr}"

    # Verify study-mindmap generated artifacts
    mindmaps_dir = ROOT_DIR / "internal" / "mindmaps"
    assert (mindmaps_dir / "book.html").exists(), "internal/mindmaps/book.html missing"
    book_html = (mindmaps_dir / "book.html").read_text(encoding="utf-8")
    for ch_id in range(8, 14):
        assert f"chapter-{ch_id:02d}.html" in [p.name for p in mindmaps_dir.glob("*.html")], f"Missing chapter-{ch_id:02d}.html"
        assert f"Pertemuan {ch_id}" in book_html, f"Pertemuan {ch_id} missing from book.html"

    # Verify study-assistant dashboard and digest
    assert (ROOT_DIR / "open" / "dashboard.html").exists(), "open/dashboard.html missing"
    assert (ROOT_DIR / "internal" / "state" / "digest.md").exists(), "internal/state/digest.md missing"
    digest_text = (ROOT_DIR / "internal" / "state" / "digest.md").read_text(encoding="utf-8")
    assert "知识点 39 个" in digest_text or "39" in digest_text

    # Verify exam-style profile and question bank integration
    assert (ROOT_DIR / "internal" / "state" / "exam-style.md").exists(), "internal/state/exam-style.md missing"
    assert (ROOT_DIR / "question-bank" / "question-bank.json").exists(), "question-bank/question-bank.json missing"
    with open(ROOT_DIR / "question-bank" / "question-bank.json", encoding="utf-8") as f:
        qb_data = json.load(f)
    assert len(qb_data.get("entries", [])) >= 10, f"Expected >= 10 entries in question-bank.json, got {len(qb_data.get('entries', []))}"
    
    print("  -> PASS: All 9 skills, study workspace state, mindmap artifacts, and Step 3 syllabus confirmation fully verified.")


def main():
    print("=" * 65)
    print("RUNNING COMPLETE PIPELINE AUDIT FOR OSL EXAM PREPARATION SETUP")
    print("=" * 65)
    test_validator_on_real_bank()
    test_validator_edge_cases()
    test_index_quality()
    test_backtest_pipeline()
    test_tracker_integrity()
    test_ocr_engine_integration()
    test_exam_corpora_and_cross_evaluation()
    test_skills_integration_and_step3_deliverables()
    print("=" * 65)
    print("ALL TESTS PASSED! Pipeline setup is robust, accurate, and verified.")
    print("=" * 65)


if __name__ == "__main__":
    main()

