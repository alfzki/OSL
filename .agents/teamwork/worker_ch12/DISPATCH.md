## 2026-09-29T08:49:32Z

You are the Worker for Chapter 12: Perdagangan dan Indikator Harga (Milestone M5).

Your working directory is:
/home/alfzki/Documents/OSL/.agents/teamwork/worker_ch12/

You MUST read:
- /home/alfzki/Documents/OSL/.agents/teamwork/ORIGINAL_REQUEST.md
- /home/alfzki/Documents/OSL/.agents/teamwork/PROJECT.md
- /home/alfzki/Documents/OSL/.agents/teamwork/explorer_status_1/analysis.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Exclusive file ownership:
- `internal/lessons/chapter-12/*`
- `internal/textbook/chapter-12.md`
- `open/chapters/chapter-12.html`
- `internal/reports/chapter-12-audit.json`

Tasks:
1. Setup reference textbook:
   Copy `extracted/Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md` to `internal/textbook/chapter-12.md`.
2. Author all 8 concept points in `internal/lessons/chapter-12/` using the proven dual-compatible schema:
   - `12.1.1-margin-perdagangan-dan-pengangkutan-mpp.json` (Margin MPP formula multiplikatif BPS, slide 4-9)
   - `12.1.2-survei-pola-distribusi-perdagangan-poldis.json` (Pemetaan rantai pasok distribusi komoditas strategis, slide 10-13)
   - `12.2.1-ihk-rumus-modified-laspeyres.json` (Formulasi Modified Laspeyres berantai relatif harga $I_t = \sum (P_t/P_{t-1} \times W_{t-1})$, SBH 2018/2022, rekonstruksi UAS 2022/2023 Esai 2b.1: IHK Mei 2023 = 114.84, ytd = 1.10%, yoy = 4.01%, slide 14-20)
   - `12.2.2-tiga-laju-inflasi-bps-mtom-yony-ytd.json` (m-to-m, y-on-y, y-to-d, slide 21-26)
   - `12.2.3-disagregasi-inflasi-inti-bergejolak-administered.json` (Komponen inti/core, volatile foods, administered prices, slide 27-32)
   - `12.3.1-konsep-dan-rasio-ntp-it-per-ib.json` (Rasio NTP = It / Ib * 100, dekomposisi Ib ke IKRT dan BPPBM, rekonstruksi UAS 2022/2023 Esai 2b.3: NTP Apr = 110.58, It Mei = 128.61, NTP Mei = 110.20, inflasi perdesaan 0.40%, slide 33-36)
   - `12.3.2-nilai-tukar-usaha-petani-ntup.json` (NTUP = It / BPPBM * 100, NTUP Apr = 110.92, slide 37-38)
   - `12.3.3-lima-subsektor-penyusun-ntp.json` (5 subsektor: Padi/Palawija, Hortikultura, Perkebunan Rakyat, Peternakan, Perikanan tangkap/budidaya, EXT-6 Indeks Kemahalan Konstruksi IKK & Country Product Dummy CPD, slide 39-40)
   Each JSON must have BOTH 8 root keys (`point_id`, `title`, `importance`, `curriculum_alignment`, `grounding`, `theory`, `numerical_example`, `exam_pitfalls`) AND study-teach keys (`textbook`, `chapter_id`, `chapter_title`, `section`, `mode`, `points`).
   Grounding citation format: `[Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide N]` or `[indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.md, hal. N]`.
   Each `numerical_example` must have executable Python verification code and verified expected output.
3. Compile chapter lecture:
   `uv run python .agents/skills/study-teach/scripts/build_chapter_lecture.py internal/lessons/chapter-12/ --publish .`
   producing `internal/lessons/chapter-12/chapter-12.md` and `open/chapters/chapter-12.html`.
4. Audit Chapter 12:
   `uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter 12`
   Verify `internal/reports/chapter-12-audit.json` has `"verdict": "pass"`.
5. Verify offline HTML:
   `uv run python .agents/skills/exam-sprint-builder/scripts/verify_html.py open/chapters/chapter-12.html`
   Must pass all 4 checks!
