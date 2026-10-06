## 2026-09-29T08:49:32Z

You are the Worker for Chapter 13: Ekspor-Impor, Terms of Trade, dan Pariwisata (Milestone M6).

Your working directory is:
/home/alfzki/Documents/OSL/.agents/teamwork/worker_ch13/

You MUST read:
- /home/alfzki/Documents/OSL/.agents/teamwork/ORIGINAL_REQUEST.md
- /home/alfzki/Documents/OSL/.agents/teamwork/PROJECT.md
- /home/alfzki/Documents/OSL/.agents/teamwork/explorer_status_1/analysis.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Exclusive file ownership:
- `internal/lessons/chapter-13/*`
- `internal/textbook/chapter-13.md`
- `open/chapters/chapter-13.html`
- `internal/reports/chapter-13-audit.json`

Tasks:
1. Setup reference textbook:
   Copy `extracted/Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md` to `internal/textbook/chapter-13.md`.
2. Author all 7 concept points in `internal/lessons/chapter-13/` using the proven dual-compatible schema:
   - `13.1.1-valuasi-ekspor-impor-fob-vs-cif.json` (Ekspor FOB, Impor CIF, PEB & PIB, konversi valuta kurs transaksi, slide 4-9)
   - `13.1.2-barang-dagangan-tanpa-masuk-pabean-merchanting.json` (Merchanting goods SNA 2008, barang tanpa lalu lintas pabean fisik, selisih jual-beli ekspor neto, slide 10-15)
   - `13.1.3-net-barter-terms-of-trade-nbtot.json` (NBToT = Px / Pm * 100, EXT-7 Indeks Spesialisasi Perdagangan ISP = (X - M)/(X + M) 4 tahapan siklus produk, rekonstruksi UAS 2022/2023 PG 24, 25, 26: ISP Karet = 0.36, tahap substitusi impor, ToT = 105, EXT-8 RCA Balassa & Openness Ratio, slide 16-24)
   - `13.1.4-gross-barter-dan-income-tot.json` (GBToT = Qm / Qx * 100 [SUPLEMEN], Income ToT = NBToT * Qx / 100 kapasitas impor, slide 25-28)
   - `13.2.1-definisi-wisman-dan-wisnus.json` (Kriteria UNWTO durasi < 1 tahun, bukan mencari nafkah/bekerja di tempat tujuan, slide 29-35)
   - `13.2.2-tingkat-penghunian-kamar-tpk-hotel.json` (TPK = malam kamar terpakai / malam kamar tersedia * 100, pembagi rooms * days open, rekonstruksi TPK 60%, slide 36-39)
   - `13.2.3-rata-rata-lama-menginap-tamu-rlmt.json` (RLMT = total malam tamu menginap / total tamu datang, rekonstruksi RLMT 2.50 malam, slide 40-43)
   Each JSON must have BOTH 8 root keys (`point_id`, `title`, `importance`, `curriculum_alignment`, `grounding`, `theory`, `numerical_example`, `exam_pitfalls`) AND study-teach keys (`textbook`, `chapter_id`, `chapter_title`, `section`, `mode`, `points`).
   Grounding citation format: `[Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide N]`.
   Each `numerical_example` must have executable Python verification code and verified expected output.
3. Compile chapter lecture:
   `uv run python .agents/skills/study-teach/scripts/build_chapter_lecture.py internal/lessons/chapter-13/ --publish .`
   producing `internal/lessons/chapter-13/chapter-13.md` and `open/chapters/chapter-13.html`.
4. Audit Chapter 13:
   `uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter 13`
   Verify `internal/reports/chapter-13-audit.json` has `"verdict": "pass"`.
5. Verify offline HTML:
   `uv run python .agents/skills/exam-sprint-builder/scripts/verify_html.py open/chapters/chapter-13.html`
   Must pass all 4 checks!
