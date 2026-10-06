## 2026-09-29T08:49:32Z

You are the Worker for Chapter 11: Statistik Produksi Pertanian dan Industri (Milestone M4).

Your working directory is:
/home/alfzki/Documents/OSL/.agents/teamwork/worker_ch11/

You MUST read:
- /home/alfzki/Documents/OSL/.agents/teamwork/ORIGINAL_REQUEST.md
- /home/alfzki/Documents/OSL/.agents/teamwork/PROJECT.md
- /home/alfzki/Documents/OSL/.agents/teamwork/explorer_status_1/analysis.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Exclusive file ownership:
- `internal/lessons/chapter-11/*`
- `internal/textbook/chapter-11.md`
- `open/chapters/chapter-11.html`
- `internal/reports/chapter-11-audit.json`

Tasks:
1. Setup reference textbook:
   Copy `extracted/Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md` to `internal/textbook/chapter-11.md`.
2. Author all 5 concept points in `internal/lessons/chapter-11/` using the proven dual-compatible schema:
   - `11.1.1-kerangka-sampel-area-ksa-padi.json` (Stratifikasi tutupan lahan, segmen 300x300m, subsegmen 100x100m, 9 titik amatan, fase vegetatif/generatif/panen, slide 4-18)
   - `11.1.2-metode-ubinan-produktivitas.json` (Plot 2.5m x 2.5m = 6.25 m2, multiplier 1600 kg/ha, 16 ku/ha, 1.6 ton/ha, rekonstruksi UAS 2022/2023 Esai 2a Pak Sakri: timbangan 4.5 kg -> 72 ku/ha = 7.2 ton/ha, slide 19-27)
   - `11.1.3-survei-konversi-gabah-ke-beras-skgb.json` (Angka konversi SKGB: GKP ke GKG 83.38%, GKG ke Beras 64.02%, slide 28-35)
   - `11.2.1-survei-industri-besar-dan-sedang-ibs.json` (Definisi IBS tenaga kerja >= 20 orang, direktori industri, nilai tambah, EXT-5 Nilai Pekerjaan Konstruksi NK = (NP - NS) * %NR = 6.4 Miliar, slide 36-48)
   - `11.2.2-survei-industri-mikro-dan-kecil-imk.json` (Batasan TK mikro 1-4, kecil 5-19, karakteristik informal, slide 49-59)
   Each JSON must have BOTH 8 root keys (`point_id`, `title`, `importance`, `curriculum_alignment`, `grounding`, `theory`, `numerical_example`, `exam_pitfalls`) AND study-teach keys (`textbook`, `chapter_id`, `chapter_title`, `section`, `mode`, `points`).
   Grounding citation format: `[Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide N]`.
   Each `numerical_example` must have executable Python verification code and verified expected output.
3. Compile chapter lecture:
   `uv run python .agents/skills/study-teach/scripts/build_chapter_lecture.py internal/lessons/chapter-11/ --publish .`
   producing `internal/lessons/chapter-11/chapter-11.md` and `open/chapters/chapter-11.html`.
4. Audit Chapter 11:
   `uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter 11`
   Verify `internal/reports/chapter-11-audit.json` has `"verdict": "pass"`.
5. Verify offline HTML:
   `uv run python .agents/skills/exam-sprint-builder/scripts/verify_html.py open/chapters/chapter-11.html`
   Must pass all 4 checks!

Write your progress in `.agents/teamwork/worker_ch11/progress.md` and handoff report in `.agents/teamwork/worker_ch11/handoff.md`.
When done, message parent (ID: 676a7321-ccd2-4a35-9634-165a5b3da2c8).
