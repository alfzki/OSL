#!/usr/bin/env python3
"""
Unit tests for past exam interactive applications and datasets:
- output/soal_latihan_uas_50.json & output/kuis_soal_latihan_uas_50.html
- output/soal_uas_2022_2023.json & output/kuis_uas_2022_2023.html
- output/pembahasan_50_soal_uas.json & output/kuis_pembahasan_50_soal_uas.html
"""

import unittest
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class TestPastExamApps(unittest.TestCase):

    def test_soal_latihan_uas_50_integrity(self):
        json_path = ROOT_DIR / "output" / "soal_latihan_uas_50.json"
        html_path = ROOT_DIR / "output" / "kuis_soal_latihan_uas_50.html"

        self.assertTrue(json_path.exists(), "soal_latihan_uas_50.json must exist")
        self.assertTrue(html_path.exists(), "kuis_soal_latihan_uas_50.html must exist")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(data), 50, "Should contain exactly 50 items")

        for idx, item in enumerate(data, start=1):
            self.assertEqual(item["id"], idx, f"Item id should match {idx}")
            self.assertTrue(len(item["stem"].strip()) > 0, f"Item {idx} stem should not be empty")
            self.assertEqual(set(item["options"].keys()), {"A", "B", "C", "D"}, f"Item {idx} should have options A,B,C,D")
            for opt_char, opt_text in item["options"].items():
                self.assertFalse(opt_text.startswith("*"), f"Item {idx} option {opt_char} should not start with markdown asterisk: '{opt_text}'")
                self.assertTrue(len(opt_text.strip()) > 0, f"Item {idx} option {opt_char} text should not be empty")
            self.assertIn(item["correct"], {"A", "B", "C", "D"}, f"Item {idx} correct key must be A, B, C, or D")
            self.assertTrue(len(item["explanation"].strip()) > 0, f"Item {idx} explanation should not be empty")
            self.assertTrue(item["citation"].startswith("[") and item["citation"].endswith("]"), f"Item {idx} citation must be formatted with brackets")

        # Specific spot-checks for verified mappings
        # Item 1: Poldis (not SDG 3)
        item1 = data[0]
        self.assertIn("Survei Pola Distribusi Perdagangan", item1["stem"])
        self.assertEqual(item1["correct"], "C")
        self.assertIn("Output sektor perdagangan", item1["options"]["C"])
        self.assertEqual(item1["category"], "Perdagangan Domestik & Harga")

        # Item 6: SDG 3 (not Poldis)
        item6 = data[5]
        self.assertIn("Tujuan 3", item6["stem"])
        self.assertEqual(item6["correct"], "B")
        self.assertEqual(item6["category"], "Kesehatan, Sanitasi & Perumahan")

        # Verify HTML file
        html_content = html_path.read_text(encoding="utf-8")
        self.assertGreater(len(html_content), 10000, "HTML file should be sufficiently populated")
        self.assertIn("MathJax", html_content)
        self.assertIn("Survei Pola Distribusi Perdagangan", html_content)

    def test_uas_2022_2023_integrity(self):
        json_path = ROOT_DIR / "output" / "soal_uas_2022_2023.json"
        html_path = ROOT_DIR / "output" / "kuis_uas_2022_2023.html"

        self.assertTrue(json_path.exists(), "soal_uas_2022_2023.json must exist")
        self.assertTrue(html_path.exists(), "kuis_uas_2022_2023.html must exist")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("questions_pg", data)
        self.assertIn("questions_essay", data)
        self.assertEqual(len(data["questions_pg"]), 40, "UAS 2022-2023 should have 40 PG items")
        self.assertEqual(len(data["questions_essay"]), 2, "UAS 2022-2023 should have 2 Essay items")

        for item in data["questions_pg"]:
            self.assertEqual(set(item["options"].keys()), {"A", "B", "C", "D"})
            self.assertIn(item["correct"], {"A", "B", "C", "D"})
            self.assertTrue(len(item["explanation"]) > 0)
            self.assertTrue(item["citation"].startswith("["))

        for item in data["questions_essay"]:
            self.assertTrue(len(item["problem"]) > 0)
            self.assertTrue(len(item["solution"]) > 0)
            self.assertIn("rubric", item)

        html_content = html_path.read_text(encoding="utf-8")
        self.assertGreater(len(html_content), 20000)
        self.assertIn("MathJax", html_content)

    def test_pembahasan_50_soal_uas_integrity(self):
        json_path = ROOT_DIR / "output" / "pembahasan_50_soal_uas.json"
        html_path = ROOT_DIR / "output" / "kuis_pembahasan_50_soal_uas.html"

        self.assertTrue(json_path.exists(), "pembahasan_50_soal_uas.json must exist")
        self.assertTrue(html_path.exists(), "kuis_pembahasan_50_soal_uas.html must exist")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(data), 50)
        for item in data:
            self.assertIn("distractors", item)
            self.assertIn("meeting", item)
            self.assertIn("citation", item)

        html_content = html_path.read_text(encoding="utf-8")
        self.assertGreater(len(html_content), 20000)


if __name__ == "__main__":
    unittest.main()
