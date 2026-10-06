## 2026-09-29T08:49:32Z

You are the Worker for Chapter 09: Ketenagakerjaan dan Pendidikan (Milestone M2).

Your working directory is:
/home/alfzki/Documents/OSL/.agents/teamwork/worker_ch09/

You MUST read:
- /home/alfzki/Documents/OSL/.agents/teamwork/ORIGINAL_REQUEST.md
- /home/alfzki/Documents/OSL/.agents/teamwork/PROJECT.md
- /home/alfzki/Documents/OSL/.agents/teamwork/explorer_status_1/analysis.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Exclusive file ownership:
- `internal/lessons/chapter-09/*`
- `internal/textbook/chapter-09.md`
- `open/chapters/chapter-09.html`
- `internal/reports/chapter-09-audit.json`

Tasks:
1. Setup reference textbook:
   Copy `extracted/Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md` to `internal/textbook/chapter-09.md`.
2. Author all 6 concept points in `internal/lessons/chapter-09/` using the proven dual-compatible schema:
   - `9.1.1-konsep-bekerja-minimal-1-jam-dan-angkatan-kerja.json` (ICLS 13, PUK 15+, BUK <15, AK, BAK, Susenas & Sakernas, slide 4-20)
   - `9.1.2-tingkat-partisipasi-angkatan-kerja-tpak.json` (TPAK = AK / PUK * 100, analisis gender & wilayah, slide 21-36)
   - `9.1.3-tingkat-pengangguran-terbuka-tpt.json` (TPT = Penganggur / AK * 100, 4 kategori penganggur BPS, rekonstruksi UAS 2022/2023 Esai 1: TPAK 64.29%, TPT 22.22%)
   - `9.1.4-setengah-penganggur-vs-pekerja-paruh-waktu.json` (Batas 35 jam kerja, pembagi Penduduk Bekerja PB, TSP = 14.29% vs TPPW, EXT-1 Formal vs Informal status pekerjaan KBLI/KBJI, slide 37-45)
   - `9.2.1-angka-partisipasi-murni-apm-dan-kasar-apk.json` (APM = Siswa usia jenjang / Penduduk usia jenjang * 100, APK, APM <= 100%, APM <= APK, APK can > 100%, slide 46-60)
   - `9.2.2-angka-partisipasi-sekolah-aps.json` (APS kelompok umur 7-12, 13-15, 16-18, 19-24, EXT-2 AMH 15+ & RLS komposit IPM, slide 61-75)
   Each JSON must have BOTH 8 root keys (`point_id`, `title`, `importance`, `curriculum_alignment`, `grounding`, `theory`, `numerical_example`, `exam_pitfalls`) AND study-teach keys (`textbook`, `chapter_id`, `chapter_title`, `section`, `mode`, `points`).
   Grounding citation format: `[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide N]` or `[Kuesioner_SAK.AGS25-AK.md, hal. N]`.
   Each `numerical_example` must have executable Python verification code and verified expected output.
3. Compile chapter lecture:
   `uv run python .agents/skills/study-teach/scripts/build_chapter_lecture.py internal/lessons/chapter-09/ --publish .`
   producing `internal/lessons/chapter-09/chapter-09.md` and `open/chapters/chapter-09.html`.
4. Audit Chapter 9:
   `uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter 9`
   Verify `internal/reports/chapter-09-audit.json` has `"verdict": "pass"`.
5. Verify offline HTML:
   `uv run python .agents/skills/exam-sprint-builder/scripts/verify_html.py open/chapters/chapter-09.html`
   Must pass all 4 checks!
