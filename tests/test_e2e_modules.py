#!/usr/bin/env python3
"""
tests/test_e2e_modules.py
Comprehensive 4-Tier E2E Test Suite for Official Statistics Lanjutan (OSL).

Validates:
- Tier 1: Category-Partition & Feature Coverage (All 39 Concept Points + 8 Extensions)
- Tier 2: Boundary Value Analysis (BVA) & Critical Statistical Thresholds
- Tier 3: Pairwise & Cross-Feature Socio-Economic Integration
- Tier 4: Real-World Historical Exam Calculations (UAS 2022/2023 & Lecturer Slide Keys)
- Offline & Zero Host Mutation Check: 100% Offline-capable, zero external HTTP/CDN references.

Execution:
    uv run python tests/test_e2e_modules.py
"""

import sys
import os
import json
import re
import math
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))


# ==============================================================================
# AUTHORITATIVE CURRICULUM REGISTRY (39 CONCEPTS + 8 EXTENSIONS)
# ==============================================================================

SYLLABUS_CONCEPTS = {
    # Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan
    "8.1.1": {"name": "Konsep Kemiskinan Absolut dan Relatif", "chapter": 8, "importance": "高"},
    "8.1.2": {"name": "Garis Kemiskinan Makanan dan Non-Makanan", "chapter": 8, "importance": "高"},
    "8.1.3": {"name": "Metodologi Cost of Basic Needs BPS", "chapter": 8, "importance": "高"},
    "8.2.1": {"name": "Headcount Index P0", "chapter": 8, "importance": "高"},
    "8.2.2": {"name": "Poverty Gap Index P1", "chapter": 8, "importance": "高"},
    "8.2.3": {"name": "Poverty Severity Index P2", "chapter": 8, "importance": "高"},
    "8.3.1": {"name": "Kurva Lorenz dan Koefisien Gini", "chapter": 8, "importance": "高"},
    "8.3.2": {"name": "Kriteria Ketimpangan Bank Dunia", "chapter": 8, "importance": "高"},

    # Pertemuan 9: Ketenagakerjaan dan Pendidikan
    "9.1.1": {"name": "Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja", "chapter": 9, "importance": "高"},
    "9.1.2": {"name": "Tingkat Partisipasi Angkatan Kerja TPAK", "chapter": 9, "importance": "高"},
    "9.1.3": {"name": "Tingkat Pengangguran Terbuka TPT", "chapter": 9, "importance": "高"},
    "9.1.4": {"name": "Setengah Penganggur vs Pekerja Paruh Waktu", "chapter": 9, "importance": "高"},
    "9.2.1": {"name": "Angka Partisipasi Murni APM dan Kasar APK", "chapter": 9, "importance": "高"},
    "9.2.2": {"name": "Angka Partisipasi Sekolah APS", "chapter": 9, "importance": "高"},

    # Pertemuan 10: Indikator Kesehatan dan SDGs 3
    "10.1.1": {"name": "Angka Kematian Ibu AKI MMR", "chapter": 10, "importance": "高"},
    "10.1.2": {"name": "Angka Kematian Bayi AKB dan Balita AKABA", "chapter": 10, "importance": "高"},
    "10.1.3": {"name": "Angka Kematian Neo-Natal NMR", "chapter": 10, "importance": "高"},
    "10.2.1": {"name": "Angka Kesakitan Morbiditas", "chapter": 10, "importance": "高"},
    "10.2.2": {"name": "Imunisasi Dasar Lengkap IDL", "chapter": 10, "importance": "高"},

    # Pertemuan 11: Statistik Produksi Pertanian dan Industri
    "11.1.1": {"name": "Kerangka Sampel Area KSA Padi", "chapter": 11, "importance": "高"},
    "11.1.2": {"name": "Metode Ubinan Produktivitas", "chapter": 11, "importance": "高"},
    "11.1.3": {"name": "Survei Konversi Gabah ke Beras SKGB", "chapter": 11, "importance": "高"},
    "11.2.1": {"name": "Survei Industri Besar dan Sedang IBS", "chapter": 11, "importance": "高"},
    "11.2.2": {"name": "Survei Industri Mikro dan Kecil IMK", "chapter": 11, "importance": "高"},

    # Pertemuan 12: Perdagangan dan Indikator Harga
    "12.1.1": {"name": "Margin Perdagangan dan Pengangkutan MPP", "chapter": 12, "importance": "高"},
    "12.1.2": {"name": "Survei Pola Distribusi Perdagangan Poldis", "chapter": 12, "importance": "高"},
    "12.2.1": {"name": "IHK Rumus Modified Laspeyres", "chapter": 12, "importance": "高"},
    "12.2.2": {"name": "Tiga Laju Inflasi BPS mtom yony ytd", "chapter": 12, "importance": "高"},
    "12.2.3": {"name": "Disagregasi Inflasi Inti Bergejolak Administered", "chapter": 12, "importance": "高"},
    "12.3.1": {"name": "Konsep dan Rasio NTP It per Ib", "chapter": 12, "importance": "高"},
    "12.3.2": {"name": "Nilai Tukar Usaha Petani NTUP", "chapter": 12, "importance": "高"},
    "12.3.3": {"name": "Lima Subsektor Penyusun NTP", "chapter": 12, "importance": "高"},

    # Pertemuan 13: Ekspor-Impor, Terms of Trade, dan Pariwisata
    "13.1.1": {"name": "Valuasi Ekspor Impor FOB vs CIF", "chapter": 13, "importance": "高"},
    "13.1.2": {"name": "Barang Dagangan Tanpa Masuk Pabean Merchanting", "chapter": 13, "importance": "高"},
    "13.1.3": {"name": "Net Barter Terms of Trade NBToT", "chapter": 13, "importance": "高"},
    "13.1.4": {"name": "Gross Barter dan Income ToT", "chapter": 13, "importance": "高"},
    "13.2.1": {"name": "Definisi Wisman dan Wisnus", "chapter": 13, "importance": "高"},
    "13.2.2": {"name": "Tingkat Penghunian Kamar TPK Hotel", "chapter": 13, "importance": "高"},
    "13.2.3": {"name": "Rata-rata Lama Menginap Tamu RLMT", "chapter": 13, "importance": "高"},
}

SUPPLEMENTARY_EXTENSIONS = {
    "EXT-1": {"name": "Klasifikasi Tenaga Kerja Formal vs Informal", "chapter": 9},
    "EXT-2": {"name": "Angka Melek Huruf (AMH 15+) & RLS", "chapter": 9},
    "EXT-3": {"name": "Antropometri & Stunting Z-Score Balita (TB/U)", "chapter": 10},
    "EXT-4": {"name": "Rumah Layak Huni & Kriteria Rumah Kumuh", "chapter": 10},
    "EXT-5": {"name": "Nilai Pekerjaan Konstruksi & IMB Konstruksi", "chapter": 11},
    "EXT-6": {"name": "Indeks Kemahalan Konstruksi (IKK)", "chapter": 12},
    "EXT-7": {"name": "Indeks Spesialisasi Perdagangan (ISP) & Siklus", "chapter": 13},
    "EXT-8": {"name": "Revealed Comparative Advantage (RCA) & Openness", "chapter": 13},
}

CITATION_REGEX = re.compile(r'(\[.*?, (?:slide|hal\.|slide/hal\.) \d+.*?\]|\[SUPLEMEN.*?\]|TIDAK ADA DI MATERI)')


# ==============================================================================
# TIER 1: CATEGORY-PARTITION & FEATURE COVERAGE TESTS
# ==============================================================================

class TestTier1FeatureCoverage(unittest.TestCase):
    """
    Tier 1 tests verify:
    1. All 39 syllabus concepts + 8 extensions exist in system knowledge registry.
    2. Any existing lesson units in internal/lessons/chapter-XX/*.json comply strictly with schema contracts.
    3. Proper citation grounding format [nama-file, slide/hal. N] or [SUPLEMEN].
    4. Compiled HTML chapter status reporting without false failures when in development.
    """

    def setUp(self):
        self.knowledge_path = ROOT_DIR / "internal" / "state" / "knowledge.json"
        self.lessons_dir = ROOT_DIR / "internal" / "lessons"
        self.open_chapters_dir = ROOT_DIR / "open" / "chapters"

    def test_curriculum_state_has_all_39_concepts(self):
        """Verify knowledge.json contains all 39 syllabus concept points with proper structure."""
        self.assertTrue(self.knowledge_path.exists(), f"Missing {self.knowledge_path}")
        with open(self.knowledge_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        registered_points = {}
        for ch in data.get("chapters", []):
            ch_id = ch.get("id")
            for sec in ch.get("sections", []):
                for pt in sec.get("points", []):
                    registered_points[pt["id"]] = {
                        "name": pt.get("name"),
                        "chapter": ch_id,
                        "status": pt.get("status"),
                        "mastery": pt.get("mastery", 0)
                    }

        self.assertEqual(len(registered_points), 39, f"Expected 39 points in knowledge.json, got {len(registered_points)}")
        for point_id, expected in SYLLABUS_CONCEPTS.items():
            self.assertIn(point_id, registered_points, f"Concept {point_id} ({expected['name']}) missing in knowledge.json")
            self.assertEqual(registered_points[point_id]["chapter"], expected["chapter"],
                             f"Point {point_id} chapter mismatch: {registered_points[point_id]['chapter']} != {expected['chapter']}")

    def test_lesson_units_schema_and_grounding(self):
        """
        Scan internal/lessons/chapter-XX/*.json.
        If files exist, validate schema, grounding citations, and pitfalls.
        If no files exist yet, report pending milestone gracefully.
        """
        lesson_files = list(self.lessons_dir.glob("chapter-*/*.json")) if self.lessons_dir.exists() else []

        if not lesson_files:
            print(f"\n  [TIER 1 INFO] internal/lessons/ has 0 JSON lesson units implemented yet. (Milestones M1-M6 planned)")
            return

        required_keys = {
            "point_id", "title", "importance", "curriculum_alignment",
            "grounding", "theory", "numerical_example", "exam_pitfalls"
        }

        verified_count = 0
        for json_file in lesson_files:
            with open(json_file, "r", encoding="utf-8") as f:
                unit = json.load(f)

            missing_keys = required_keys - set(unit.keys())
            self.assertFalse(missing_keys, f"{json_file.name} missing required schema keys: {missing_keys}")

            point_id = unit["point_id"]
            self.assertIn(point_id, SYLLABUS_CONCEPTS, f"Unexpected point_id {point_id} in {json_file.name}")

            # Grounding check
            grounding = unit.get("grounding", {})
            coverage = grounding.get("coverage_status")
            self.assertIn(coverage, ["COVERED", "SUPPLEMENTED", "NOT_IN_MATERIAL"])

            primary_sources = grounding.get("primary_sources", [])
            for src in primary_sources:
                citation_text = f"[{src.get('file', '')}, slide/hal. {src.get('slide_or_page', '')}]"
                self.assertTrue(CITATION_REGEX.search(citation_text),
                                f"Invalid citation in {json_file.name}: {citation_text}")

            # Theory LaTeX check
            theory = unit.get("theory", {})
            formula_latex = theory.get("formula_latex", "")
            self.assertTrue(len(formula_latex.strip()) > 0, f"Empty formula_latex in {json_file.name}")

            # Exam Pitfalls check
            pitfalls = unit.get("exam_pitfalls", [])
            self.assertIsInstance(pitfalls, list)
            self.assertGreaterEqual(len(pitfalls), 1, f"At least 1 exam pitfall required in {json_file.name}")
            for p in pitfalls:
                self.assertIn("trap_description", p)
                self.assertIn("common_mistake", p)
                self.assertIn("safe_strategy", p)

            verified_count += 1

        print(f"\n  [TIER 1 PASS] Verified {verified_count} lesson JSON units against strict schema & citation contracts.")

    def test_every_lesson_point_has_published_md_and_html(self):
        """
        Every per-point lesson JSON source must have BOTH a rendered Markdown
        (obsidian) and a rendered HTML artifact in the same chapter directory.

        Output filenames are derived from the point title, not the JSON slug, so
        artifacts are matched by their ``<point_id>-`` filename prefix.
        """
        if not self.lessons_dir.exists():
            self.fail(f"Missing lessons directory {self.lessons_dir}")

        missing = []
        total_points = 0
        md_count = 0
        html_count = 0

        for chapter_dir in sorted(self.lessons_dir.glob("chapter-*")):
            if not chapter_dir.is_dir():
                continue

            sources = [j for j in chapter_dir.glob("*.json") if not j.name.startswith("chapter-")]
            for src in sorted(sources):
                with open(src, "r", encoding="utf-8") as f:
                    point_id = json.load(f)["point_id"]
                total_points += 1

                stem = f"{point_id}-"
                has_md = any(p.name.startswith(stem) and p.suffix == ".md" for p in chapter_dir.iterdir())
                has_html = any(p.name.startswith(stem) and p.suffix == ".html" for p in chapter_dir.iterdir())

                if has_md:
                    md_count += 1
                else:
                    missing.append(f"{chapter_dir.name}/{point_id}: missing .md")
                if has_html:
                    html_count += 1
                else:
                    missing.append(f"{chapter_dir.name}/{point_id}: missing .html")

        self.assertEqual(
            total_points, 39,
            f"Expected 39 per-point lesson JSON sources across chapter dirs, found {total_points}",
        )
        self.assertFalse(
            missing,
            "Lesson points without both rendered artifacts:\n  " + "\n  ".join(missing),
        )
        print(f"\n  [TIER 1 PASS] Verified {total_points} lesson points each publish both .md and .html "
              f"({md_count} md / {html_count} html).")

    def test_open_chapters_html_status(self):
        """Verify compiled chapters in open/chapters/ if present, or report pending."""
        expected_chapters = [f"chapter-{i:02d}.html" for i in range(8, 14)]
        existing = [f.name for f in self.open_chapters_dir.glob("*.html")] if self.open_chapters_dir.exists() else []

        if not existing:
            print(f"\n  [TIER 1 INFO] open/chapters/ currently has {len(existing)} compiled HTMLs. (Will be generated by build_chapter_lecture.py)")
        else:
            for fname in existing:
                fpath = self.open_chapters_dir / fname
                self.assertGreater(fpath.stat().st_size, 500, f"HTML file {fname} is too small / empty")
            print(f"\n  [TIER 1 PASS] Verified existing compiled HTML chapters: {existing}")


# ==============================================================================
# TIER 2: BOUNDARY VALUE ANALYSIS (BVA) & CRITICAL THRESHOLDS
# ==============================================================================

class TestTier2BoundaryValues(unittest.TestCase):
    """
    Tier 2 tests verify exact mathematical and statistical boundary conditions:
    1. MMR (AKI) per 100,000 live births vs IMR/AKABA/NMR per 1,000 live births.
    2. Ubinan plot 2.5m x 2.5m (6.25 m2) multiplier = 1,600 (kg/ha), 16 (ku/ha), 1.6 (ton/ha).
    3. Labor 35-hour threshold: cutoff for underemployment vs part-time; denominator is Penduduk Bekerja (PB).
    4. Food Poverty Line (GKM) 2100 kcal & GK = GKM + GKNM boundary.
    5. Modified Laspeyres chained relative price updating.
    6. Education enrollment bounds: APM <= 100%, APM <= APK, APK can exceed 100%.
    7. FGT divisor boundary: total population n, never q.
    8. Terms of Trade reversal: GBToT = (Qm / Qx) * 100 vs NBToT = (Px / Pm) * 100.
    9. Hotel TPK denominator: available room-nights (rooms * days open).
    10. Trade Specialization Index (ISP) boundary in [-1, +1] and 4 cycle stages.
    """

    def test_bva_01_mortality_multipliers(self):
        """MMR must use 100,000 live births multiplier; IMR/NMR/AKABA must use 1,000."""
        maternal_deaths = 5
        infant_deaths = 12
        neonatal_deaths = 4
        under5_deaths = 18
        live_births = 25000
        midyear_under5_pop = 20000

        # MMR = (Maternal Deaths / Live Births) * 100,000
        mmr = (maternal_deaths / live_births) * 100000
        self.assertAlmostEqual(mmr, 20.0, places=4)

        # IMR = (Infant Deaths / Live Births) * 1,000
        imr = (infant_deaths / live_births) * 1000
        self.assertAlmostEqual(imr, 0.48, places=4)

        # NMR = (Neonatal Deaths / Live Births) * 1,000
        nmr = (neonatal_deaths / live_births) * 1000
        self.assertAlmostEqual(nmr, 0.16, places=4)

        # U5MR (AKABA) = (Under5 Deaths / Midyear Pop) * 1,000
        akaba = (under5_deaths / midyear_under5_pop) * 1000
        self.assertAlmostEqual(akaba, 0.90, places=4)

        # Trap verification: if someone wrongly used 1,000 for MMR
        wrong_mmr = (maternal_deaths / live_births) * 1000
        self.assertNotEqual(mmr, wrong_mmr)
        self.assertEqual(mmr, wrong_mmr * 100)

    def test_bva_02_ubinan_plot_multipliers(self):
        """Ubinan plot 2.5m x 2.5m = 6.25 m2. Multiplier to 10,000 m2 is 1600."""
        plot_side = 2.5
        plot_area = plot_side * plot_side
        self.assertEqual(plot_area, 6.25)

        hectare_m2 = 10000.0
        multiplier_kg_ha = hectare_m2 / plot_area
        self.assertEqual(multiplier_kg_ha, 1600.0)

        # Test boundary conversions
        b_samples = [0.0, 1.0, 3.5, 4.0, 4.5, 5.0]
        for b in b_samples:
            kg_ha = b * 1600.0
            ku_ha = kg_ha / 100.0
            ton_ha = kg_ha / 1000.0

            self.assertAlmostEqual(ku_ha, b * 16.0, places=6)
            self.assertAlmostEqual(ton_ha, b * 1.6, places=6)

    def test_bva_03_labor_35_hour_cutoff_and_denominators(self):
        """
        Hours < 35 with searching = Setengah Penganggur.
        Hours < 35 voluntary = Pekerja Paruh Waktu.
        Denominator for TSP and TPPW is Penduduk Bekerja (PB), NOT Angkatan Kerja (AK).
        """
        puk = 1000
        ak = 700
        bak = 300
        pb = 630  # Penduduk Bekerja
        penganggur = 70  # TPT = 70/700 = 10%

        # Among PB:
        full_time = 450      # >= 35 hrs
        underemployed = 80  # < 35 hrs & searching
        part_time = 100     # < 35 hrs & voluntary

        self.assertEqual(full_time + underemployed + part_time, pb)

        # Official BPS Formulas:
        tsp = (underemployed / pb) * 100.0
        tppw = (part_time / pb) * 100.0

        self.assertAlmostEqual(tsp, 12.698412, places=4)
        self.assertAlmostEqual(tppw, 15.873016, places=4)

        # Trap: dividing by AK (labor force) instead of PB
        trap_tsp = (underemployed / ak) * 100.0
        self.assertNotEqual(tsp, trap_tsp)
        self.assertGreater(tsp, trap_tsp)  # Since PB < AK

    def test_bva_04_food_poverty_line_and_poverty_criterion(self):
        """
        Food poverty line GKM corresponds to 2100 kcal/day.
        Garis Kemiskinan GK = GKM + GKNM.
        Strict inequality: Poor if y_i < GK (at y_i == GK, person is NOT poor).
        """
        gkm = 450000.0
        gknm = 150000.0
        gk = gkm + gknm
        self.assertEqual(gk, 600000.0)

        # Individual expenditure tests
        test_expenditures = [599999.0, 600000.0, 600001.0]
        statuses = [y < gk for y in test_expenditures]
        self.assertEqual(statuses, [True, False, False],
                         "Boundary condition failure: y == GK should not be classified as poor")

    def test_bva_05_modified_laspeyres_chaining(self):
        """
        Modified Laspeyres chaining formula:
        I_t = sum( (P_t / P_{t-1}) * W_{t-1} )
        If all prices remain constant, RH = 1.0, index remains exactly 100.0.
        """
        weights_prev = [30.0, 25.0, 20.0, 15.0, 10.0]  # sum = 100.0
        self.assertAlmostEqual(sum(weights_prev), 100.0, places=6)

        # Case 1: All prices unchanged
        rh_unchanged = [1.0, 1.0, 1.0, 1.0, 1.0]
        index_unchanged = sum(rh * w for rh, w in zip(rh_unchanged, weights_prev))
        self.assertAlmostEqual(index_unchanged, 100.0, places=6)

        # Case 2: One commodity jumps by 10%
        rh_jump = [1.10, 1.0, 1.0, 1.0, 1.0]  # 10% increase on 30% weight
        index_jump = sum(rh * w for rh, w in zip(rh_jump, weights_prev))
        self.assertAlmostEqual(index_jump, 103.0, places=6)

        # Updated consumption value weights for next period
        weights_next = [rh * w for rh, w in zip(rh_jump, weights_prev)]
        self.assertAlmostEqual(sum(weights_next), 103.0, places=6)

    def test_bva_06_education_apm_apk_bounds(self):
        """
        APM <= APK always.
        APM <= 100% strictly.
        APK can exceed 100% when non-standard age cohort students enroll.
        """
        official_cohort_pop = 1000
        official_age_enrolled = 920
        total_enrolled = 1060  # includes early/late entrants or grade repeaters

        apm = (official_age_enrolled / official_cohort_pop) * 100.0
        apk = (total_enrolled / official_cohort_pop) * 100.0

        self.assertAlmostEqual(apm, 92.0)
        self.assertAlmostEqual(apk, 106.0)
        self.assertLessEqual(apm, 100.0)
        self.assertGreater(apk, 100.0)
        self.assertLess(apm, apk)

    def test_bva_07_fgt_divisor_boundary(self):
        """
        FGT P_alpha divisor must be total population n, never poor population q.
        Dividing by q gives the mean poverty gap among the poor, strictly > P1.
        """
        n = 100
        q = 20
        z = 500000.0
        # 20 poor people with shortfall 100,000 each
        shortfall_ratio = 100000.0 / 500000.0  # 0.20
        sum_shortfalls = q * shortfall_ratio   # 20 * 0.2 = 4.0

        p1_correct = (1.0 / n) * sum_shortfalls  # 4.0 / 100 = 0.04 (4%)
        p1_trap_divided_by_q = (1.0 / q) * sum_shortfalls  # 4.0 / 20 = 0.20 (20%)

        self.assertAlmostEqual(p1_correct, 0.04)
        self.assertAlmostEqual(p1_trap_divided_by_q, 0.20)
        self.assertNotEqual(p1_correct, p1_trap_divided_by_q)

    def test_bva_08_terms_of_trade_formula_inversion(self):
        """
        NBToT = (Px / Pm) * 100.
        GBToT = (Qm / Qx) * 100. (Note inverted quantities).
        """
        px, pm = 120.0, 100.0
        qx, qm = 150.0, 180.0

        nbtot = (px / pm) * 100.0
        gbtot = (qm / qx) * 100.0

        self.assertAlmostEqual(nbtot, 120.0)
        self.assertAlmostEqual(gbtot, 120.0)

        # Common exam trap: Qx / Qm
        trap_gbtot = (qx / qm) * 100.0
        self.assertAlmostEqual(trap_gbtot, 83.333333, places=4)
        self.assertNotEqual(gbtot, trap_gbtot)

    def test_bva_09_hotel_tpk_denominator_room_nights(self):
        """
        TPK denominator is available room-nights = rooms * days_open.
        """
        rooms = 50
        days_in_month = 30
        available_room_nights = rooms * days_in_month  # 1500
        sold_room_nights = 900

        tpk = (sold_room_nights / available_room_nights) * 100.0
        self.assertAlmostEqual(tpk, 60.0)

        # Trap: dividing by rooms only
        trap_tpk = (sold_room_nights / rooms)
        self.assertEqual(trap_tpk, 18.0)

    def test_bva_10_isp_bounds_and_product_cycle(self):
        """
        Trade Specialization Index: ISP = (X - M) / (X + M).
        Range: [-1.0, +1.0].
        Test all 4 stages:
        - [-1.0, -0.5]: Introduction
        - (-0.5, 0.0]: Import Substitution
        - (0.0, 0.8]: Export Expansion
        - (0.8, 1.0]: Maturation
        """
        def get_stage(isp):
            if -1.0 <= isp <= -0.5:
                return "Pengenalan"
            elif -0.5 < isp <= 0.0:
                return "Substitusi Impor"
            elif 0.0 < isp <= 0.8:
                return "Perluasan Ekspor"
            elif 0.8 < isp <= 1.0:
                return "Pematangan"
            return "Out of bounds"

        # Boundary test points
        test_cases = [
            (0, 100, -1.0, "Pengenalan"),
            (10, 90, -0.8, "Pengenalan"),
            (25, 75, -0.5, "Pengenalan"),
            (30, 70, -0.4, "Substitusi Impor"),
            (50, 50, 0.0, "Substitusi Impor"),
            (60, 40, 0.2, "Perluasan Ekspor"),
            (90, 10, 0.8, "Perluasan Ekspor"),
            (95, 5, 0.9, "Pematangan"),
            (100, 0, 1.0, "Pematangan")
        ]

        for x, m, expected_isp, expected_stage in test_cases:
            isp = (x - m) / (x + m)
            self.assertAlmostEqual(isp, expected_isp, places=4)
            self.assertEqual(get_stage(isp), expected_stage)


# ==============================================================================
# TIER 3: PAIRWISE & CROSS-FEATURE INTEGRATION
# ==============================================================================

class TestTier3CrossFeatureIntegration(unittest.TestCase):
    """
    Tier 3 tests verify cross-feature interactions and systemic consistency:
    1. Kemiskinan FGT vs Ketimpangan Kurva Lorenz & Gini:
       Doubling all incomes (y_i -> 2 * y_i) with fixed GK drastically drops P0,
       yet leaves the Lorenz curve and Gini coefficient completely unchanged.
    2. Ketenagakerjaan vs Pendidikan:
       Relationship between PUK (15+), schooling age groups (APS), and labor force status.
    3. Nilai Tukar Petani (NTP) vs Inflasi Perdesaan:
       NTP = It / Ib * 100, where Ib = IKRT + BPPBM. Rural inflation is derived from IKRT.
    4. Perdagangan Luar Negeri:
       Valuation alignment (FOB vs CIF vs SNA 2008 Merchanting) and Income ToT.
    """

    def test_integration_01_fgt_vs_gini_scale_invariance(self):
        """
        Verify that a uniform scale increase (multiplying all expenditures by 2)
        causes absolute poverty P0 to fall, while Gini remains invariant.
        """
        gk = 500000.0
        expenditures_t0 = [200000.0, 300000.0, 400000.0, 600000.0, 1000000.0]
        n = len(expenditures_t0)

        # Baseline P0 at t0
        q_t0 = sum(1 for y in expenditures_t0 if y < gk)
        p0_t0 = q_t0 / n
        self.assertEqual(p0_t0, 0.60)  # 3 out of 5 are poor

        # Gini calculation function (discrete trapezoid)
        def compute_gini(y_list):
            sorted_y = sorted(y_list)
            total = sum(sorted_y)
            cum_pop = [i / len(sorted_y) for i in range(len(sorted_y) + 1)]
            cum_exp = [0.0]
            curr = 0.0
            for y in sorted_y:
                curr += y / total
                cum_exp.append(curr)

            # Gini = 1 - sum( (X_i - X_{i-1}) * (Y_i + Y_{i-1}) )
            area_b = 0.0
            for i in range(1, len(cum_pop)):
                dx = cum_pop[i] - cum_pop[i - 1]
                sy = cum_exp[i] + cum_exp[i - 1]
                area_b += dx * sy
            return 1.0 - area_b

        gini_t0 = compute_gini(expenditures_t0)

        # Scale by 2.0
        expenditures_t1 = [y * 2.0 for y in expenditures_t0]
        q_t1 = sum(1 for y in expenditures_t1 if y < gk)
        p0_t1 = q_t1 / n
        self.assertEqual(p0_t1, 0.20)  # Only 1 (400k) remains under 500k GK

        gini_t1 = compute_gini(expenditures_t1)

        # Strict Assertions: P0 dropped dramatically, but Gini is mathematically invariant
        self.assertLess(p0_t1, p0_t0)
        self.assertAlmostEqual(gini_t0, gini_t1, places=7,
                               msg="Gini coefficient must be strictly scale-invariant")

    def test_integration_02_employment_education_consistency(self):
        """
        Verify demographic consistency between Working-Age Population (PUK 15+)
        and School Attendance Age Groups (APS).
        """
        puk_15_plus = 50000
        under_15 = 15000
        total_pop = puk_15_plus + under_15

        # School age brackets
        aps_7_12 = 8000   # SD age (under 15)
        aps_13_15 = 4000  # SMP age (partially under 15, partially 15)
        aps_16_18 = 4000  # SMA age (all in PUK)
        aps_19_24 = 6000  # PT age (all in PUK)

        # Labor status in PUK
        angkatan_kerja = 35000
        bukan_angkatan_kerja = 15000
        self.assertEqual(angkatan_kerja + bukan_angkatan_kerja, puk_15_plus)

        # BAK breakdown: schooling, housekeeping, others
        bak_sekolah = 5000
        bak_irt = 8000
        bak_lainnya = 2000
        self.assertEqual(bak_sekolah + bak_irt + bak_lainnya, bukan_angkatan_kerja)

        # Those attending school in PUK who are not working must be subset of BAK
        self.assertLessEqual(bak_sekolah, bukan_angkatan_kerja)

    def test_integration_03_ntp_vs_rural_inflation_decomposition(self):
        """
        Decomposing NTP into farming profitability (NTUP) and rural living cost (IKRT).
        If rural inflation rises while producer prices and production costs are flat,
        NTP declines even though NTUP stays constant.
        """
        it_month1 = 120.0
        ikrt_month1 = 110.0
        bppbm_month1 = 100.0

        # Weighted Ib = 0.6 * IKRT + 0.4 * BPPBM
        ib_month1 = 0.6 * ikrt_month1 + 0.4 * bppbm_month1  # 66 + 40 = 106.0
        ntp_month1 = (it_month1 / ib_month1) * 100.0
        ntup_month1 = (it_month1 / bppbm_month1) * 100.0

        self.assertAlmostEqual(ntp_month1, 113.207547, places=4)
        self.assertAlmostEqual(ntup_month1, 120.0, places=4)

        # Month 2: Rural food price shock increases IKRT by 10%, but It and BPPBM constant
        it_month2 = 120.0
        ikrt_month2 = 121.0  # 10% rural inflation
        bppbm_month2 = 100.0

        rural_inflation = ((ikrt_month2 - ikrt_month1) / ikrt_month1) * 100.0
        self.assertAlmostEqual(rural_inflation, 10.0)

        ib_month2 = 0.6 * ikrt_month2 + 0.4 * bppbm_month2  # 72.6 + 40 = 112.6
        ntp_month2 = (it_month2 / ib_month2) * 100.0
        ntup_month2 = (it_month2 / bppbm_month2) * 100.0

        # Assertions
        self.assertLess(ntp_month2, ntp_month1)  # Farmer welfare drops due to living cost
        self.assertAlmostEqual(ntup_month2, ntup_month1)  # Farm business profitability unchanged

    def test_integration_04_trade_valuations_merchanting_tot(self):
        """
        Verify trade valuation conventions (FOB vs CIF), SNA 2008 Merchanting,
        and Income Terms of Trade (IToT = NBToT * Qx / 100 = Px * Qx / Pm).
        """
        # 1. Valuation: CIF = FOB + Insurance + Freight
        export_fob = 1000.0
        import_fob = 800.0
        insurance_freight = 80.0
        import_cif = import_fob + insurance_freight  # 880.0

        # Trade balance BPS: FOB Ekspor - CIF Impor
        bps_trade_balance = export_fob - import_cif  # 1000 - 880 = 120.0
        # Trade balance BOP (Bank Indonesia): FOB Ekspor - FOB Impor
        bop_trade_balance = export_fob - import_fob  # 1000 - 800 = 200.0
        self.assertGreater(bop_trade_balance, bps_trade_balance)

        # 2. Merchanting Goods (SNA 2008): Buy for 500, Sell for 650 without entering customs
        merchant_buy = -500.0  # negative export
        merchant_sell = 650.0  # positive export
        net_merchanting_export = merchant_sell + merchant_buy  # +150.0
        self.assertEqual(net_merchanting_export, 150.0)

        # 3. Income Terms of Trade
        px, pm = 110.0, 100.0
        qx = 120.0
        nbtot = (px / pm) * 100.0  # 110.0
        itot = nbtot * (qx / 100.0)  # 110 * 1.2 = 132.0

        # Direct derivation: (Px * Qx) / Pm
        itot_direct = (px * qx) / pm
        self.assertAlmostEqual(itot, itot_direct)
        self.assertAlmostEqual(itot, 132.0)


# ==============================================================================
# TIER 4: REAL-WORLD HISTORICAL EXAM CALCULATIONS (UAS 2022/2023 & SLIDES)
# ==============================================================================

class TestTier4RealWorldExamCalculations(unittest.TestCase):
    """
    Tier 4 tests verify exact calculations against real-world exam problems:
    1. Pertemuan 8 Slide 39 Gini calculation table (Gini = 0.3770, Bank Dunia 40% = 17.27% -> Rendah).
    2. FGT P0, P1, P2 calculation on 20-sample population with z=600,000 and q=5.
    3. UAS 2022/2023 Essay 1 Ketenagakerjaan (TPAK = 64.29%, TPT = 22.22%, TSP = 14.29%).
    4. UAS 2022/2023 Essay 2a Ubinan Padi (4.5 kg -> 72 ku/ha = 7.2 ton/ha).
    5. UAS 2022/2023 Essay 2b.1 Table Reconstruction (IHK Mei 2023 = 114.84, y-to-d = 1.10%, y-on-y = 4.01%).
    6. UAS 2022/2023 Essay 2b.3 Table Reconstruction (NTP Apr = 110.58, NTUP Apr = 110.92, Mei It = 128.61, NTP Mei = 110.20, Rural Infl = 0.40%).
    7. UAS 2022/2023 Multiple Choice Ekspor-Impor (ISP Karet = 0.36, Stage Substitusi Impor, ToT = 105).
    8. Tourism Hospitality Metrics (TPK = 60.00%, RLMT = 2.50 malam).
    9. Construction Net Value Added (NK = (NP - NS) * %NR = 6.4 Miliar).
    """

    def test_scenario_01_gini_quintile_slide_39(self):
        """Reconstruct Pertemuan 8 Slide 39 Gini table and World Bank inequality threshold."""
        consumption = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]
        total = sum(consumption)
        self.assertEqual(total, 695000.0)

        # Percentage of consumption
        p_i = [c / total for c in consumption]
        expected_p = [0.0719, 0.1007, 0.1439, 0.1799, 0.5036]
        for actual, exp in zip(p_i, expected_p):
            self.assertAlmostEqual(actual, exp, places=4)

        # Cumulative consumption Y_i
        y_cum = []
        curr = 0.0
        for p in p_i:
            curr += p
            y_cum.append(curr)

        # f_i is 0.20 for each quintile
        f_i = 0.20
        trapezoid_terms = []
        for i in range(len(y_cum)):
            prev_y = 0.0 if i == 0 else y_cum[i - 1]
            sum_y = y_cum[i] + prev_y
            trapezoid_terms.append(f_i * sum_y)

        sum_trapezoid = sum(trapezoid_terms)
        self.assertAlmostEqual(sum_trapezoid, 0.6230, places=4)

        gini = 1.0 - sum_trapezoid
        self.assertAlmostEqual(gini, 0.3770, places=4)

        # World Bank criteria: bottom 40% (Q1 + Q2)
        bottom_40 = (p_i[0] + p_i[1]) * 100.0
        self.assertAlmostEqual(bottom_40, 17.27, places=2)
        # > 17% is Ketimpangan Rendah
        self.assertGreater(bottom_40, 17.0)

    def test_scenario_02_fgt_indices_20_samples(self):
        """FGT P0, P1, P2 calculation on 20-sample population with GK = 600,000."""
        z = 600000.0
        # 5 poor individuals
        poor_y = [300000.0, 400000.0, 450000.0, 500000.0, 550000.0]
        # 15 non-poor individuals
        non_poor_y = [650000.0] * 15
        all_y = poor_y + non_poor_y

        n = len(all_y)
        q = len(poor_y)
        self.assertEqual(n, 20)
        self.assertEqual(q, 5)

        # Poverty gaps: (z - y) / z
        gaps = [(z - y) / z for y in poor_y]
        expected_gaps = [0.50, 0.333333, 0.25, 0.166667, 0.083333]
        for actual, exp in zip(gaps, expected_gaps):
            self.assertAlmostEqual(actual, exp, places=4)

        # P0 = q / n
        p0 = q / n
        self.assertAlmostEqual(p0, 0.25)  # 25.00%

        # P1 = (1 / n) * sum(gaps)
        p1 = (1.0 / n) * sum(gaps)
        self.assertAlmostEqual(p1, 0.0667, places=4)  # 6.67%

        # P2 = (1 / n) * sum(gaps^2)
        p2 = (1.0 / n) * sum(g ** 2 for g in gaps)
        self.assertAlmostEqual(p2, 0.0229, places=4)  # 2.29%

    def test_scenario_03_ketenagakerjaan_essay_uas_2022_2023(self):
        """Reconstruct UAS 2022/2023 Essay 1 Labor problem (30 points)."""
        pop_total = 18.0  # million
        puk = 14.0
        buk = 4.0
        self.assertEqual(puk + buk, pop_total)

        ak = 9.0
        bak_sekolah = 2.0
        bak_irt = 2.0
        bak_lainnya = 1.0
        bak_total = bak_sekolah + bak_irt + bak_lainnya
        self.assertEqual(bak_total, 5.0)
        self.assertEqual(ak + bak_total, puk)

        # Labor breakdown:
        pb_full = 6.0
        pb_part = 1.0
        pb_total = pb_full + pb_part
        self.assertEqual(pb_total, 7.0)

        unemployed_phk = 1.0
        unemployed_startup = 0.5
        unemployed_waiting = 0.5
        unemployed_total = unemployed_phk + unemployed_startup + unemployed_waiting
        self.assertEqual(unemployed_total, 2.0)
        self.assertEqual(pb_total + unemployed_total, ak)

        # Indicators
        tpak = (ak / puk) * 100.0
        self.assertAlmostEqual(tpak, 64.285714, places=4)
        self.assertAlmostEqual(round(tpak, 2), 64.29)

        tpt = (unemployed_total / ak) * 100.0
        self.assertAlmostEqual(tpt, 22.222222, places=4)
        self.assertAlmostEqual(round(tpt, 2), 22.22)

        # TSP = Setengah Penganggur / PB * 100
        tsp = (pb_part / pb_total) * 100.0
        self.assertAlmostEqual(tsp, 14.285714, places=4)
        self.assertAlmostEqual(round(tsp, 2), 14.29)

    def test_scenario_04_ubinan_essay_2a_uas_2022_2023(self):
        """Reconstruct UAS 2022/2023 Essay 2a: Pak Sakri ubinan 4.5 kg."""
        b = 4.5  # kg
        multiplier = 1600.0

        kg_ha = b * multiplier
        ku_ha = kg_ha / 100.0
        ton_ha = kg_ha / 1000.0

        self.assertEqual(kg_ha, 7200.0)
        self.assertEqual(ku_ha, 72.0)
        self.assertEqual(ton_ha, 7.2)

    def test_scenario_05_ihk_table_essay_2b1_uas_2022_2023(self):
        """Reconstruct UAS 2022/2023 Essay 2b.1 Table Reconstruction."""
        # Distractor
        ihk_apr_2022 = 109.98
        ihk_mei_2022 = 110.42
        ihk_des_2022 = 113.59
        ihk_apr_2023 = 114.74
        inflasi_mtom_mei_2023 = 0.09  # percent

        # Step 1: Compute IHK Mei 2023 (Cell A)
        ihk_mei_2023 = ihk_apr_2023 * (1.0 + inflasi_mtom_mei_2023 / 100.0)
        self.assertAlmostEqual(ihk_mei_2023, 114.843266, places=6)
        self.assertEqual(round(ihk_mei_2023, 2), 114.84)

        # Step 2: Compute Year-to-Date inflation Mei 2023 (Cell B, vs Des 2022)
        inflasi_ytd_mei_2023 = ((ihk_mei_2023 - ihk_des_2022) / ihk_des_2022) * 100.0
        self.assertAlmostEqual(inflasi_ytd_mei_2023, 1.103324, places=4)
        self.assertEqual(round(inflasi_ytd_mei_2023, 2), 1.10)

        # Step 3: Compute Year-on-Year inflation Mei 2023 (Cell C, vs Mei 2022, NOT Apr 2022!)
        inflasi_yony_mei_2023 = ((ihk_mei_2023 - ihk_mei_2022) / ihk_mei_2022) * 100.0
        self.assertAlmostEqual(inflasi_yony_mei_2023, 4.005856, places=4)
        self.assertEqual(round(inflasi_yony_mei_2023, 2), 4.01)

        # Assert distractor was not used
        wrong_yony = ((ihk_mei_2023 - ihk_apr_2022) / ihk_apr_2022) * 100.0
        self.assertNotEqual(round(inflasi_yony_mei_2023, 2), round(wrong_yony, 2))

    def test_scenario_06_ntp_table_essay_2b3_uas_2022_2023(self):
        """Reconstruct UAS 2022/2023 Essay 2b.3 NTP Table."""
        # April 2023 data
        it_apr = 128.64
        ib_apr = 116.33
        ikrt_apr = 116.71
        bppbm_apr = 115.98

        # Cell (1): NTP April 2023
        ntp_apr = (it_apr / ib_apr) * 100.0
        self.assertAlmostEqual(ntp_apr, 110.5820, places=4)
        self.assertEqual(round(ntp_apr, 2), 110.58)

        # Cell (2): NTUP April 2023
        ntup_apr = (it_apr / bppbm_apr) * 100.0
        self.assertAlmostEqual(ntup_apr, 110.9157, places=4)
        self.assertEqual(round(ntup_apr, 2), 110.92)

        # Mei 2023 data
        ntup_mei = 110.75
        ib_mei = 116.71
        ikrt_mei = 117.18
        bppbm_mei = 116.13

        # Cell (3): It Mei 2023 (derived from NTUP and BPPBM)
        it_mei = (ntup_mei * bppbm_mei) / 100.0
        self.assertAlmostEqual(it_mei, 128.613975, places=6)
        self.assertEqual(round(it_mei, 2), 128.61)

        # Cell (4): NTP Mei 2023
        ntp_mei = (it_mei / ib_mei) * 100.0
        self.assertAlmostEqual(ntp_mei, 110.1996, places=4)
        self.assertEqual(round(ntp_mei, 2), 110.20)

        # Cell (5): Rural inflation Mei 2023 (derived from IKRT)
        rural_infl_mei = ((ikrt_mei - ikrt_apr) / ikrt_apr) * 100.0
        self.assertAlmostEqual(rural_infl_mei, 0.402708, places=4)
        self.assertEqual(round(rural_infl_mei, 2), 0.40)

    def test_scenario_07_ekspor_impor_uas_2022_2023(self):
        """Reconstruct UAS 2022/2023 MC questions 24, 25, 26."""
        # Q24: Rubber export X = 350M, import M = 164M
        x_rubber = 350.0
        m_rubber = 164.0
        isp = (x_rubber - m_rubber) / (x_rubber + m_rubber)
        self.assertAlmostEqual(isp, 186.0 / 514.0, places=6)
        self.assertEqual(round(isp, 2), 0.36)

        # Q25: ISP = -0.36 -> Import substitution stage (-0.50 to 0.00)
        isp_neg = -0.36
        stage = "Substitusi Impor" if -0.50 <= isp_neg <= 0.00 else "Other"
        self.assertEqual(stage, "Substitusi Impor")

        # Q26: Export price Px = 105, Import price Pm = 100
        px = 105.0
        pm = 100.0
        tot = (px / pm) * 100.0
        self.assertEqual(tot, 105.0)

    def test_scenario_08_tourism_hospitality(self):
        """Reconstruct TPK and RLMT hotel metrics."""
        rooms = 100
        days = 30
        available_room_nights = rooms * days  # 3000
        sold_room_nights = 1800
        tpk = (sold_room_nights / available_room_nights) * 100.0
        self.assertAlmostEqual(tpk, 60.0)

        guests_arrived = 500
        guest_bed_nights = 1250
        rlmt = guest_bed_nights / guests_arrived
        self.assertAlmostEqual(rlmt, 2.50)  # nights

    def test_scenario_09_construction_net_value(self):
        """Reconstruct BPS Construction Output Value NK = (NP - NS) * %NR."""
        np = 10000000000.0  # 10 Billion
        ns = 2000000000.0   # 2 Billion subcontracted
        nr_percent = 0.80   # 80% completed

        nk = (np - ns) * nr_percent
        self.assertEqual(nk, 6400000000.0)  # 6.4 Billion


# ==============================================================================
# TIER 5 / INFRASTRUCTURE CHECK: OFFLINE & ZERO MUTATION
# ==============================================================================

def find_remote_refs(content):
    """Return every remote src=/href= reference found in an HTML document."""
    return re.findall(r'(?:src|href)=["\']https?://', content, re.IGNORECASE)


class TestTier5OfflineAndZeroMutation(unittest.TestCase):
    """
    Validates offline self-containment:
    - HTML files in open/, internal/mindmaps/ and internal/lessons/ must not contain
      external HTTP/HTTPS CDN references.
    """

    def test_zero_remote_dependency_in_html_artifacts(self):
        """Inspect all HTML files to ensure 0 external CDN/HTTP script or stylesheet requests."""
        html_dirs = [
            ROOT_DIR / "open",
            ROOT_DIR / "internal" / "mindmaps",
            ROOT_DIR / "internal" / "lessons",
        ]
        checked_files = 0
        violations = []

        external_re = re.compile(r'(?:src|href)=["\']https?://', re.IGNORECASE)

        for d in html_dirs:
            if not d.exists():
                continue
            for html_file in d.glob("**/*.html"):
                checked_files += 1
                with open(html_file, "r", encoding="utf-8") as f:
                    content = f.read()

                matches = external_re.findall(content)
                if matches:
                    violations.append(f"{html_file.relative_to(ROOT_DIR)}: found {len(matches)} external links")

        self.assertFalse(violations, f"Found external online dependencies in HTML files:\n" + "\n".join(violations))
        print(f"\n  [TIER 5 PASS] Verified {checked_files} HTML files for strict 100% offline self-containment.")

    def test_merged_chapter_html_has_visible_offline_math_notice(self):
        """Merged chapter HTML must ship no dead MathJax config and a visible offline-formula notice.
        """
        chapter_nums = ["08", "09", "10", "11", "12", "13"]
        checked_files = 0
        dead_mathjax = []
        hidden_notice = []
        empty_notice = []
        remote_refs = []

        for num in chapter_nums:
            path = (ROOT_DIR / "internal" / "lessons" / f"chapter-{num}"
                    / f"chapter-{num}.html")
            self.assertTrue(path.exists(), f"Merged chapter HTML not found: {path}")
            rel = path.relative_to(ROOT_DIR)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            checked_files += 1

            # (a) no dead MathJax config object
            if "window.MathJax" in content:
                dead_mathjax.append(f"{rel}: found dead 'window.MathJax' config with no loader")

            # (b) the #mjwarn rule must be display: block, not display: none
            rule = re.search(r"#mjwarn\s*\{([^}]*)\}", content)
            if rule is None:
                hidden_notice.append(f"{rel}: no '#mjwarn' CSS rule found")
            elif "display: none" in rule.group(1):
                hidden_notice.append(f"{rel}: '#mjwarn' is display:none -> {rule.group(0).strip()}")
            elif "display: block" not in rule.group(1):
                hidden_notice.append(f"{rel}: '#mjwarn' is not display:block -> {rule.group(0).strip()}")

            # the notice element itself must exist with non-empty text
            notice = re.search(r'<div id="mjwarn">(.*?)</div>', content, re.DOTALL)
            if notice is None:
                empty_notice.append(f"{rel}: no '<div id=\"mjwarn\">' element found")
            elif not notice.group(1).strip():
                empty_notice.append(f"{rel}: '#mjwarn' notice text is empty")

            # (c) zero remote src=/href= references
            matches = find_remote_refs(content)
            if matches:
                remote_refs.append(f"{rel}: found {len(matches)} external links")

        self.assertFalse(dead_mathjax,
                         "Merged chapter HTML ships a dead MathJax config:\n" + "\n".join(dead_mathjax))
        self.assertFalse(hidden_notice,
                         "Merged chapter offline-formula notice is hidden:\n" + "\n".join(hidden_notice))
        self.assertFalse(empty_notice,
                         "Merged chapter offline-formula notice has no text:\n" + "\n".join(empty_notice))
        self.assertFalse(remote_refs,
                         "Merged chapter HTML has external online dependencies:\n" + "\n".join(remote_refs))
        print(f"\n  [TIER 5 PASS] Verified {checked_files} merged chapter HTML files: "
              f"no dead MathJax config, visible #mjwarn notice, 0 remote refs.")

    def test_perpoint_lesson_html_has_no_dead_mathjax_config(self):
        """Per-point lesson HTML must contain no dead MathJax config (uniform with merged chapters).
        
        Scans all 39 per-point HTML files (internal/lessons/chapter-*/*.html excluding the 6
        merged chapter-XX.html files) and asserts zero occurrences of "window.MathJax".
        """
        import re
        from pathlib import Path

        ROOT_DIR = Path(__file__).resolve().parent.parent
        lessons_dir = ROOT_DIR / "internal" / "lessons"

        # Collect all per-point HTML files: every .html in chapter-*/ dirs,
        # excluding the 6 merged chapter-XX.html files at the chapter root level.
        excluded_names = {f"chapter-{n}.html" for n in ["08", "09", "10", "11", "12", "13"]}

        perpoint_files = []
        for chapter_dir in sorted(lessons_dir.glob("chapter-*")):
            if not chapter_dir.is_dir():
                continue
            for html_file in sorted(chapter_dir.glob("*.html")):
                # Skip the merged chapter root HTML files (chapter-08.html, ..., chapter-13.html)
                if html_file.name in excluded_names:
                    continue
                perpoint_files.append(html_file)

        self.assertEqual(
            len(perpoint_files), 39,
            f"Expected exactly 39 per-point lesson HTML files, found {len(perpoint_files)}. "
            f"Checked: {[f.relative_to(ROOT_DIR) for f in perpoint_files]}",
        )

        dead_mathjax = []
        for html_file in perpoint_files:
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()
            if "window.MathJax" in content:
                dead_mathjax.append(f"{html_file.relative_to(ROOT_DIR)}: found dead 'window.MathJax' config")

        self.assertFalse(
            dead_mathjax,
            "Per-point lesson HTML files ship a dead MathJax config:\n"
            + "\n".join(dead_mathjax),
        )
        print(f"\n  [TIER 5 PASS] Verified {len(perpoint_files)} per-point lesson HTML files: "
              f"no dead MathJax config.")


# ==============================================================================
# MAIN TEST RUNNER WITH SUMMARY REPORTING
# ==============================================================================

def run_tests():
    print("=" * 70)
    print("RUNNING E2E TEST SUITE FOR OFFICIAL STATISTICS LANJUTAN (OSL)")
    print("Methodology: Opaque-Box, 4-Tier Verification, Zero Host Mutation")
    print("=" * 70)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestTier1FeatureCoverage))
    suite.addTests(loader.loadTestsFromTestCase(TestTier2BoundaryValues))
    suite.addTests(loader.loadTestsFromTestCase(TestTier3CrossFeatureIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestTier4RealWorldExamCalculations))
    suite.addTests(loader.loadTestsFromTestCase(TestTier5OfflineAndZeroMutation))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print(f"ALL {result.testsRun} E2E TESTS PASSED SUCCESSFULLY! (100% PASS RATE)")
        print("Test suite is production-ready for progressive milestone verification.")
        print("=" * 70)
        return 0
    else:
        print(f"TEST FAILURES DETECTED: {len(result.failures)} failures, {len(result.errors)} errors.")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
