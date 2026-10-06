# Analisis Menyeluruh Arsitektur, Status Berkas, Perkakas, & Materi Sumber OSL (Milestone M0 / Baseline Explorer)

**Tanggal/Waktu Analisis**: 2026-09-29T15:15:00+07:00  
**Penyusun**: Codebase & Architecture Explorer (`explorer_status_1`)  
**Lingkungan Kerja**: `/home/alfzki/Documents/OSL`  
**Integritas Host**: Zero Host Mutation (`uv run python`)  

---

## 1. Audit Status Berkas Pembelajaran & Bab (Lesson & Chapter Audit)

### 1.1 Status Direktori `internal/lessons/`
Pemeriksaan dilakukan pada seluruh struktur direktori bab (Chapter 08 s.d. 13):
- **Chapter 08** (`internal/lessons/chapter-08/`): **ADA** (16 berkas).
- **Chapter 09** (`internal/lessons/chapter-09/`): **BELUM ADA** (direktori belum dibuat).
- **Chapter 10** (`internal/lessons/chapter-10/`): **BELUM ADA** (direktori belum dibuat).
- **Chapter 11** (`internal/lessons/chapter-11/`): **BELUM ADA** (direktori belum dibuat).
- **Chapter 12** (`internal/lessons/chapter-12/`): **BELUM ADA** (direktori belum dibuat).
- **Chapter 13** (`internal/lessons/chapter-13/`): **BELUM ADA** (direktori belum dibuat).

### 1.2 Status Pekerjaan `worker_m1` pada Chapter 08
`worker_m1` telah menghasilkan 6 berkas JSON konsep, 5 berkas Markdown, dan 5 berkas HTML pada `internal/lessons/chapter-08/`:
1. `8.1.1-kemiskinan-absolut-relatif.json` (12.082 byte), `8.1.1-Konsep-Kemiskinan-Absolut-dan-Relatif.md` (11.896 byte), `8.1.1-Konsep-Kemiskinan-Absolut-dan-Relatif.html` (25.686 byte).
2. `8.1.2-garis-kemiskinan-makanan-non-makanan.json` (10.926 byte), `8.1.2-Garis-Kemiskinan-Makanan-dan-Non-Makanan.md` (10.751 byte), `8.1.2-Garis-Kemiskinan-Makanan-dan-Non-Makanan.html` (24.667 byte).
3. `8.1.3-metodologi-cost-of-basic-needs-bps.json` (12.315 byte), `8.1.3-Metodologi-Cost-of-Basic-Needs-BPS.md` (12.162 byte), `8.1.3-Metodologi-Cost-of-Basic-Needs-BPS.html` (26.037 byte).
4. `8.2.1-headcount-index-p0.json` (9.014 byte), `8.2.1-Headcount-Index-P0.md` (8.856 byte), `8.2.1-Headcount-Index-P0.html` (22.384 byte).
5. `8.2.2-poverty-gap-index-p1.json` (10.895 byte), `8.2.2-Poverty-Gap-Index-P1.md` (10.711 byte), `8.2.2-Poverty-Gap-Index-P1.html` (24.233 byte).
6. `8.2.3-poverty-severity-index-p2.json` (11.657 byte) — *belum dikompilasi ke .md dan .html*.

#### Butir yang Belum Dikerjakan di Chapter 08:
- **8.3.1 (Kurva Lorenz dan Koefisien Gini)**: Belum dibuat.
- **8.3.2 (Kriteria Ketimpangan Bank Dunia)**: Belum dibuat.
- **Kompilasi Bab Penuh**: `chapter-08.md` dan `chapter-08.html` belum digenerasikan ke `internal/lessons/chapter-08/` maupun ke `open/chapters/chapter-08.html`.
- **Status Audit Bab**: Perintah `uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter 8` menghasilkan status **`blocked`** (exit code 1) karena 8.3.1 dan 8.3.2 belum ada.

### 1.3 Audit Kepatuhan Skema JSON (Akar Masalah Kegagalan Uji E2E)
Ditemukan diskrepansi struktural penting antara format yang ditulis `worker_m1` dan format yang divalidasi oleh `tests/test_e2e_modules.py`:
- **Format yang Divalidasi oleh `tests/test_e2e_modules.py` (baris 154-157) & `PROJECT.md` (baris 78-85)**:
  Membutuhkan 8 top-level keys:
  `["point_id", "title", "importance", "curriculum_alignment", "grounding", "theory", "numerical_example", "exam_pitfalls"]`.
- **Format yang Ditulis oleh `worker_m1`**:
  Mengikuti format asli `study-teach` (`build_lecture.py` / `build_chapter_lecture.py`):
  Top-level keys: `["textbook", "chapter_id", "chapter_title", "section", "mode", "points"]`, di mana data konsep berada di dalam elemen array `points[0]`.

#### Resolusi Kompatibilitas Bersama (Dual-Compatibility):
Baik `build_chapter_lecture.py` maupun `tests/test_e2e_modules.py` **tidak melarang** field tambahan di level teratas. Sehingga, agar suatu file JSON memenuhi kedua validator secara serentak (100% lulus E2E dan 100% kompatibel dengan pipeline `study-teach`), berkas JSON per poin wajib memuat **KEDUA kumpulan kunci**:
```json
{
  "point_id": "8.1.1",
  "title": "Konsep Kemiskinan Absolut dan Relatif",
  "importance": "高",
  "curriculum_alignment": {
    "pertemuan": 8,
    "silabus_topic": "Kemiskinan dan Ketimpangan",
    "bps_subject": "Indikator Kemiskinan"
  },
  "grounding": {
    "primary_sources": [
      {
        "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
        "slide_or_page": "4-13",
        "content": "Definisi kemiskinan absolut vs relatif dan standar PPP"
      }
    ],
    "supplemental_sources": [],
    "coverage_status": "COVERED"
  },
  "theory": {
    "intuition": "...",
    "bps_definition": "...",
    "boundary_conditions": "...",
    "formula_latex": "$$z_{\\text{abs}} = \\text{konstan riil}, \\quad z_{\\text{rel}} = k \\cdot \\text{Median}(Y)$$"
  },
  "numerical_example": {
    "problem_statement": "...",
    "data_table": "...",
    "step_by_step_solution": "...",
    "python_verification_code": "...",
    "expected_output": "..."
  },
  "exam_pitfalls": [
    {
      "trap_description": "Transformasi skala seragam terhadap kemiskinan relatif",
      "common_mistake": "Menganggap kenaikan pendapatan 20% seragam menurunkan kemiskinan relatif",
      "safe_strategy": "Ingat bahwa median ikut naik sehingga garis relatif naik proporsional; kemiskinan relatif tidak berubah"
    }
  ],
  "textbook": "Official Statistics Lanjutan (OSL)",
  "chapter_id": 8,
  "chapter_title": "Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan",
  "section": "8.1 Konsep dan Metodologi Garis Kemiskinan BPS",
  "mode": "deep",
  "points": [
    {
      "id": "8.1.1",
      "name": "Konsep Kemiskinan Absolut dan Relatif",
      "importance": "高",
      "source_ref": "[Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 4-13]",
      "exam_focus": "...",
      "intuition": "...",
      "formal": "...",
      "pitfalls": "...",
      "examples": [ ... ]
    }
  ]
}
```

### 1.4 Status Direktori Terkait Lainnya
- **`internal/textbook/`**:
  - `chapter-08.md` (26.013 byte) **ADA** (disalin dari berkas ekstraksi Bab 8).
  - `chapter-09.md` s.d. `chapter-13.md` **BELUM ADA**. Harus disalin dari berkas di `extracted/` sebelum audit masing-masing bab dijalankan.
- **`open/chapters/`**:
  - Saat ini **KOSONG**. File `chapter-08.html` s.d. `chapter-13.html` akan diproduksi oleh opsi `--publish .` pada `build_chapter_lecture.py`.
- **`internal/mindmaps/`**:
  - `book.html` (17.773 byte) **ADA**.
  - `chapter-08.html` (11.749 byte) s.d. `chapter-13.html` (11.503 byte) **LENGKAP TERSEDIA** (7 berkas).
- **`internal/state/`**:
  - `knowledge.json`: 39 konsep silabus terdaftar lengkap (status saat ini seluruhnya `'未学'`).
  - `progress.json`: posisi saat ini pada Chapter 8.

---

## 2. Audit Perkakas & Skrip Pembelajaran (Tools & Scripts Audit)

Berikut adalah daftar perkakas utama, lokasi berkas, fungsi, dan perintah CLI resmi untuk menjalankannya:

| No | Perkakas | Lokasi Skrip | Fungsi & Output | Perintah CLI Eksekusi |
|---|---|---|---|---|
| 1 | **Unit Lesson Builder** | `.agents/skills/study-teach/scripts/build_lecture.py` | Mengompilasi 1 berkas JSON pelajaran menjadi Markdown & HTML individual | `uv run python .agents/skills/study-teach/scripts/build_lecture.py internal/lessons/chapter-XX/<unit>.json` |
| 2 | **Chapter Aggregator & Publisher** | `.agents/skills/study-teach/scripts/build_chapter_lecture.py` | Menggabungkan seluruh JSON unit dalam bab menjadi `chapter-XX.md` dan HTML terpadu di `open/chapters/chapter-XX.html` | `uv run python .agents/skills/study-teach/scripts/build_chapter_lecture.py internal/lessons/chapter-XX/ --publish .` |
| 3 | **Chapter Auditor** | `.agents/skills/study-assistant/scripts/audit_chapter.py` | Memeriksa kelengkapan poin konsep thd `knowledge.json` & materi primer di `internal/textbook/chapter-XX.md`. Output: `internal/reports/chapter-XX-audit.json` | `uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter XX` |
| 4 | **Question Bank Manager** | `.agents/skills/study-quiz/scripts/bank.py` | Menelan contoh soal dari berkas kuliah ke bank soal global (`question-bank/question-bank.json`) dan statistik per poin | `uv run python .agents/skills/study-quiz/scripts/bank.py . add-lecture <lecture.json>`<br>`uv run python .agents/skills/study-quiz/scripts/bank.py . stats` |
| 5 | **Mindmap Generator** | `.agents/skills/study-mindmap/scripts/build_mindmap.py` | Mengompilasi visualisasi interaktif pohon materi dari `knowledge.json` ke `internal/mindmaps/` | `uv run python .agents/skills/study-mindmap/scripts/build_mindmap.py internal/state/knowledge.json --book`<br>`uv run python .agents/skills/study-mindmap/scripts/build_mindmap.py internal/state/knowledge.json --chapter XX` |
| 6 | **Dashboard Builder** | `.agents/skills/study-assistant/scripts/build_dashboard.py` | Memperbarui dashboard progres belajar `open/dashboard.html` dan `internal/state/digest.md` | `uv run python .agents/skills/study-assistant/scripts/build_dashboard.py .` |
| 7 | **Workspace Validator** | `.agents/skills/study-assistant/scripts/validate_workspace.py` | Memvalidasi integritas state `knowledge.json` dan `progress.json` sesuai kontrak | `uv run python .agents/skills/study-assistant/scripts/validate_workspace.py .` |
| 8 | **HTML Offline Verifier** | `.agents/skills/exam-sprint-builder/scripts/verify_html.py` | Memverifikasi kepatuhan 100% offline (0 tautan remote HTTP/CDN) pada berkas HTML | `uv run python .agents/skills/exam-sprint-builder/scripts/verify_html.py <berkas.html>` |
| 9 | **Materi Searcher & Indexer** | `scripts/build_index.py` | Menelusuri potongan materi dan sitasi cepat berbasis indeks kata kunci | `uv run python scripts/build_index.py --search "<kata_kunci>"` |

---

## 3. Pemetaan Materi Sumber & Sitasi Presisi (Pertemuan 8 s.d. 13)

Berikut adalah inventarisasi berkas sumber di `extracted/` dan `materials/` beserta rentang slide dan topik intinya:

| Bab | Pertemuan & Topik Silabus | Berkas Sumber Ekstraksi | Berkas Asli di `materials/` | Rentang Slide / Hal. Kunci | Topik Inti & Konsep Silabus |
|---|---|---|---|---|---|
| **Ch 08** | **Pertemuan 8: Kemiskinan & Ketimpangan** (8 konsep) | `extracted/Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md` | `materials/slides/Pertemuan 8 OSL Indikator Sosial (1) Indikator Kemiskinan dan Ketimpangan _ new.pptx` | Slide 4–13 (Konsep & Relatif), Slide 14–22 (CBN, GKM, GKNM), Slide 23–32 (FGT $P_0, P_1, P_2$), Slide 33–44 (Lorenz, Gini, Bank Dunia) | 8.1.1 (Absolut vs Relatif), 8.1.2 (GKM 2100 kkal & GKNM), 8.1.3 (CBN Susenas), 8.2.1 ($P_0$), 8.2.2 ($P_1$), 8.2.3 ($P_2$), 8.3.1 (Lorenz & Gini), 8.3.2 (Kriteria Bank Dunia) |
| **Ch 09** | **Pertemuan 9: Ketenagakerjaan & Pendidikan** (6 konsep + 2 ekstensi) | `extracted/Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md`<br>+ `extracted/Kuesioner_SAK.AGS25-AK.md` | `materials/slides/Pertemuan 9 Indikator Ketenagakerjaan dan Pendidikan.pptx`<br>+ `materials/notes/Kuesioner SAK.AGS25-AK.pdf` | Slide 4–20 (ICLS 13, PUK, Bekerja $\ge$ 1 Jam), Slide 21–36 (TPAK, TPT), Slide 37–45 (Setengah Penganggur & Paruh Waktu, Formal/Informal), Slide 46–75 (APK, APM, APS, AMH, RLS) | 9.1.1 (Bekerja $\ge 1$ jam, AK/BAK), 9.1.2 (TPAK), 9.1.3 (TPT 4 kategori), 9.1.4 (Setengah Penganggur vs Paruh Waktu), 9.2.1 (APM & APK), 9.2.2 (APS), EXT-1 (Formal/Informal), EXT-2 (AMH & RLS) |
| **Ch 10** | **Pertemuan 10: Kesehatan & SDGs 3** (5 konsep + 2 ekstensi) | `extracted/Pertemuan_10_Indikator_Kesehatan.md` | `materials/slides/Pertemuan 10 Indikator Kesehatan.pptx` | Slide 4–35 (AKI, AKB, AKABA, NMR), Slide 36–65 (Morbiditas, IDL, Gizi/Stunting), Slide 66–91 (Sanitasi, Air Minum & Rumah Layak Huni) | 10.1.1 (AKI MMR per 100.000 KH), 10.1.2 (AKB IMR & AKABA U5MR), 10.1.3 (NMR 0-28 hari), 10.2.1 (Morbiditas), 10.2.2 (IDL), EXT-3 (Antropometri & Stunting TB/U), EXT-4 (Rumah Layak Huni) |
| **Ch 11** | **Pertemuan 11: Statistik Produksi & KSA** (5 konsep + 1 ekstensi) | `extracted/Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md` | `materials/slides/Pertemuan 11 OSL Indikator Ekonomi (1) Produksi.pdf` | Slide 4–18 (KSA Padi, Segmen 300x300, Subsegmen), Slide 19–35 (Metode Ubinan 2.5x2.5, Konversi Gabah SKGB), Slide 36–59 (IBS $\ge 20$, IMK, Nilai Pekerjaan Konstruksi) | 11.1.1 (KSA Padi), 11.1.2 (Ubinan Produktivitas, multiplier 1600), 11.1.3 (SKGB GKP ke GKG 83.38%, GKG ke Beras 64.02%), 11.2.1 (IBS), 11.2.2 (IMK), EXT-5 (Nilai Konstruksi $NK = (NP - NS) \times \%NR$) |
| **Ch 12** | **Pertemuan 12: Perdagangan & Harga** (8 konsep + 1 ekstensi) | `extracted/Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md`<br>+ `extracted/indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.md` | `materials/slides/Pertemuan 12 OSL Indikator Ekonomi (2) Perdagangan&Harga.pdf`<br>+ `materials/notes/indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.pdf` | Slide 4–13 (MPP, Rantai Pasok Poldis), Slide 14–26 (IHK Modified Laspeyres, SBH, 3 Laju Inflasi: m-to-m, y-on-y, y-to-d), Slide 27–32 (Disagregasi Inti, Bergejolak, Administered), Slide 33–40 (NTP $I_t/I_b$, NTUP, 5 Subsektor NTP) | 12.1.1 (Margin MPP), 12.1.2 (Survei Poldis), 12.2.1 (IHK Modified Laspeyres), 12.2.2 (3 Laju Inflasi BPS), 12.2.3 (Disagregasi Inflasi), 12.3.1 (Rasio NTP $I_t/I_b$), 12.3.2 (NTUP), 12.3.3 (5 Subsektor NTP), EXT-6 (IKK & Metode CPD) |
| **Ch 13** | **Pertemuan 13: Ekspor-Impor & Pariwisata** (7 konsep + 2 ekstensi) | `extracted/Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md` | `materials/slides/Pertemuan 13 OSL Indikator Ekonomi (3) X-M, KTI, Pariwisata.pdf` | Slide 4–15 (Valuasi Ekspor FOB, Impor CIF, Merchanting Goods SNA 2008), Slide 16–28 (Terms of Trade: Net Barter, Gross Barter, Income ToT, ISP, RCA, Openness), Slide 29–43 (Wisman, Wisnus, Hotel TPK, RLMT) | 13.1.1 (FOB vs CIF, PEB & PIB), 13.1.2 (Merchanting Goods SNA 2008), 13.1.3 (Net Barter ToT), 13.1.4 (Gross Barter & Income ToT), 13.2.1 (Wisman & Wisnus), 13.2.2 (TPK Hotel), 13.2.3 (RLMT), EXT-7 (ISP & Siklus Produk), EXT-8 (RCA & Openness) |

---

## 4. Hasil Eksekusi Uji Garis Dasar (Baseline Test Execution)

### 4.1 Eksekusi `uv run python tests/test_pipeline.py`
- **Waktu Eksekusi**: 2026-09-29T15:08:40+07:00
- **Exit Code**: **0 (SUCCESS)**
- **Hasil**: 8/8 test suites lulus sempurna:
  1. Validator `bank/soal.json` lulus (10 butir valid).
  2. Validator kasus batas semantik dan aturan penolakan lulus.
  3. Indeks materi memuat 610 segmen dengan judul bersih.
  4. Pipeline backtest longitudinal lulus (MAE silang: 8,73%).
  5. Integritas `progress/tracker.json` terverifikasi.
  6. Engine OCR Tesseract v5.5.3 terdeteksi dan aktif.
  7. Korpus ujian lampau (Latihan: 50 soal, UAS 2022/2023: 42 soal) terurai akurat.
  8. Integrasi 9 skill & deliverable silabus terverifikasi.

### 4.2 Eksekusi `uv run python tests/test_e2e_modules.py`
- **Waktu Eksekusi**: 2026-09-29T15:08:36+07:00
- **Exit Code**: **1 (FAILURE)**
- **Hasil**: 26 passed, 1 failed.
  - **Uji yang Gagal**: `test_lesson_units_schema_and_grounding (TestTier1FeatureCoverage)`.
  - **Akar Masalah**: Berkas JSON yang dibuat oleh `worker_m1` di `internal/lessons/chapter-08/` tidak memuat 8 top-level keys (`point_id`, `title`, `importance`, `curriculum_alignment`, `grounding`, `theory`, `numerical_example`, `exam_pitfalls`), melainkan memuat keys `study-teach` (`textbook`, `chapter_id`, `chapter_title`, `section`, `mode`, `points`).
  - **Uji Tingkat Lain (Tier 2, 3, 4, 5)**: Seluruh perhitungan matematis (BVA, integrasi lintas fitur, rekonstruksi 9 soal riil UAS/Slide BPS, dan kepatuhan 0 dependensi remote offline) **LULUS 100%**.

---

## 5. Rencana Aksi Eksekusi Milestone M1 s.d. M7 (Structured Action Plan)

### Pola Standar Eksekusi Per Bab (Standard Chapter Workflow Protocol):
Setiap pengerjaan bab (M1 s.d. M6) wajib mengikuti siklus 6 langkah berikut:
1. **Penyalinan Teks Rujukan Bab**: Salin berkas ekstraksi dari `extracted/` ke `internal/textbook/chapter-XX.md`.
2. **Pembuatan Berkas Konsep JSON (Dual-Compatible Schema)**: Tulis seluruh poin konsep bab ke `internal/lessons/chapter-XX/<point-id>-<slug>.json` dengan menyertakan:
   - 8 top-level keys untuk kelulusan `test_e2e_modules.py`.
   - Objek `points[0]` lengkap untuk kompatibilitas `build_chapter_lecture.py` dan `audit_chapter.py`.
   - Grounding sitasi presisi format `[nama-file, slide/hal. N]`.
   - Penurunan rumus LaTeX rigor dan skrip Python verifikasi angka.
   - Minimal 1 jebakan dosen (*exam pitfalls*) dengan struktur (`trap_description`, `common_mistake`, `safe_strategy`).
3. **Kompilasi Bab**: Jalankan `uv run python .agents/skills/study-teach/scripts/build_chapter_lecture.py internal/lessons/chapter-XX/ --publish .` untuk memproduksi `internal/lessons/chapter-XX/chapter-XX.md`, `internal/lessons/chapter-XX/chapter-XX.html`, dan `open/chapters/chapter-XX.html`.
4. **Audit Mutu Bab**: Jalankan `uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter XX` dan pastikan status `pass` (exit code 0).
5. **Ingesti Bank Soal**: Jalankan `uv run python .agents/skills/study-quiz/scripts/bank.py . add-lecture internal/lessons/chapter-XX/<unit>.json` untuk seluruh unit konsep.
6. **Verifikasi E2E Parsial**: Jalankan `uv run python tests/test_e2e_modules.py` untuk memastikan kepatuhan skema dan kepatuhan offline berkas HTML baru.

---

### Rincian Target & Jadwal Eksekusi Milestones:

#### **Milestone M1 — Bab 8: Kemiskinan dan Ketimpangan (Selesaikan Sisa Pekerjaan)**
- **Cakupan**: 8 konsep (8.1.1 s.d. 8.3.2).
- **Langkah Kerja**:
  1. Perbarui 6 berkas JSON yang sudah ada (`8.1.1` s.d. `8.2.3`) agar memuat 8 top-level keys skema E2E.
  2. Buat 2 berkas JSON yang belum ada:
     - `8.3.1-kurva-lorenz-koefisien-gini.json` (formulasi trapesium diskrit BPS, $G = 1 - \sum (X_i - X_{i-1})(Y_i + Y_{i-1})$).
     - `8.3.2-kriteria-ketimpangan-bank-dunia.json` (distribusi 40% terbawah: $<12\%$ tinggi, $12-17\%$ sedang, $>17\%$ rendah).
  3. Kompilasi modul bab penuh ke `open/chapters/chapter-08.html` menggunakan `build_chapter_lecture.py`.
  4. Jalankan `audit_chapter.py . --chapter 8` (harus `pass`).
  5. Ingesti contoh soal Bab 8 ke `question-bank/question-bank.json` via `bank.py`.
  6. Perbarui status 8 konsep pada `knowledge.json` menjadi `"status": "已讲解"`, `"mastery": 4`.

#### **Milestone M2 — Bab 9: Ketenagakerjaan dan Pendidikan**
- **Cakupan**: 6 konsep silabus (9.1.1 s.d. 9.2.2) + 2 ekstensi (EXT-1: Formal vs Informal, EXT-2: AMH & RLS).
- **Langkah Kerja**:
  1. Salin `extracted/Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md` ke `internal/textbook/chapter-09.md`.
  2. Implementasikan 6 berkas JSON di `internal/lessons/chapter-09/`:
     - `9.1.1-bekerja-minimal-1-jam-angkatan-kerja.json`
     - `9.1.2-tingkat-partisipasi-angkatan-kerja-tpak.json`
     - `9.1.3-tingkat-pengangguran-terbuka-tpt.json`
     - `9.1.4-setengah-penganggur-pekerja-paruh-waktu.json`
     - `9.2.1-angka-partisipasi-murni-dan-kasar.json`
     - `9.2.2-angka-partisipasi-sekolah-aps.json`
  3. Integrasikan EXT-1 ke dalam 9.1.4 dan EXT-2 ke dalam 9.2.2.
  4. Kompilasi via `build_chapter_lecture.py internal/lessons/chapter-09/ --publish .`.
  5. Audit via `audit_chapter.py . --chapter 9`.
  6. Ingesti soal ke bank soal dan perbarui state `knowledge.json`.

#### **Milestone M3 — Bab 10: Indikator Kesehatan dan SDGs 3**
- **Cakupan**: 5 konsep silabus (10.1.1 s.d. 10.2.2) + 2 ekstensi (EXT-3: Stunting TB/U, EXT-4: Rumah Layak Huni).
- **Langkah Kerja**:
  1. Salin `extracted/Pertemuan_10_Indikator_Kesehatan.md` ke `internal/textbook/chapter-10.md`.
  2. Implementasikan 5 berkas JSON di `internal/lessons/chapter-10/`:
     - `10.1.1-angka-kematian-ibu-aki-mmr.json` (multiplier $100.000\text{ KH}$).
     - `10.1.2-angka-kematian-bayi-dan-balita.json` (multiplier $1.000\text{ KH}$).
     - `10.1.3-angka-kematian-neonatal-nmr.json` (usia $0-28$ hari).
     - `10.2.1-angka-kesakitan-morbiditas.json` (keluhan kesehatan & terganggu aktivitas).
     - `10.2.2-imunisasi-dasar-lengkap-idl.json` (HB0, BCG, DPT-HB-Hib, Polio, Campak).
  3. Integrasikan EXT-3 ke dalam 10.2.1 dan EXT-4 ke dalam 10.2.2.
  4. Kompilasi via `build_chapter_lecture.py internal/lessons/chapter-10/ --publish .`.
  5. Audit via `audit_chapter.py . --chapter 10`.
  6. Ingesti soal ke bank soal dan perbarui state `knowledge.json`.

#### **Milestone M4 — Bab 11: Statistik Produksi Pertanian dan Industri**
- **Cakupan**: 5 konsep silabus (11.1.1 s.d. 11.2.2) + 1 ekstensi (EXT-5: Nilai Pekerjaan Konstruksi).
- **Langkah Kerja**:
  1. Salin `extracted/Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md` ke `internal/textbook/chapter-11.md`.
  2. Implementasikan 5 berkas JSON di `internal/lessons/chapter-11/`:
     - `11.1.1-kerangka-sampel-area-ksa-padi.json` (segmen 300x300, subsegmen 100x100, fase amatan).
     - `11.1.2-metode-ubinan-produktivitas.json` (plot 2.5x2.5 m, multiplier 1600).
     - `11.1.3-survei-konversi-gabah-ke-beras-skgb.json` (GKP ke GKG 83.38%, GKG ke Beras 64.02%).
     - `11.2.1-survei-industri-besar-dan-sedang-ibs.json` (tenaga kerja $\ge 20$).
     - `11.2.2-survei-industri-mikro-dan-kecil-imk.json` (mikro 1-4, kecil 5-19).
  3. Integrasikan EXT-5 ($NK = (NP-NS) \times \%NR$) ke dalam 11.2.1.
  4. Kompilasi via `build_chapter_lecture.py internal/lessons/chapter-11/ --publish .`.
  5. Audit via `audit_chapter.py . --chapter 11`.
  6. Ingesti soal ke bank soal dan perbarui state `knowledge.json`.

#### **Milestone M5 — Bab 12: Perdagangan dan Indikator Harga**
- **Cakupan**: 8 konsep silabus (12.1.1 s.d. 12.3.3) + 1 ekstensi (EXT-6: IKK & Metode CPD).
- **Langkah Kerja**:
  1. Salin `extracted/Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md` ke `internal/textbook/chapter-12.md`.
  2. Implementasikan 8 berkas JSON di `internal/lessons/chapter-12/`:
     - `12.1.1-margin-perdagangan-dan-pengangkutan-mpp.json`
     - `12.1.2-survei-pola-distribusi-perdagangan-poldis.json`
     - `12.2.1-ihk-rumus-modified-laspeyres.json` (formula berantai dengan pembobot konsumsi $W_{t-1}$).
     - `12.2.2-tiga-laju-inflasi-bps-mtom-yony-ytd.json`
     - `12.2.3-disagregasi-inflasi-inti-bergejolak-administered.json`
     - `12.3.1-konsep-dan-rasio-ntp-it-per-ib.json`
     - `12.3.2-nilai-tukar-usaha-petani-ntup.json` (rasio terhadap BPPBM).
     - `12.3.3-lima-subsektor-penyusun-ntp.json`
  3. Integrasikan EXT-6 (IKK dan metode Country Product Dummy) ke dalam 12.2.1.
  4. Kompilasi via `build_chapter_lecture.py internal/lessons/chapter-12/ --publish .`.
  5. Audit via `audit_chapter.py . --chapter 12`.
  6. Ingesti soal ke bank soal dan perbarui state `knowledge.json`.

#### **Milestone M6 — Bab 13: Ekspor-Impor, Terms of Trade, dan Pariwisata**
- **Cakupan**: 7 konsep silabus (13.1.1 s.d. 13.2.3) + 2 ekstensi (EXT-7: ISP, EXT-8: RCA & Openness).
- **Langkah Kerja**:
  1. Salin `extracted/Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md` ke `internal/textbook/chapter-13.md`.
  2. Implementasikan 7 berkas JSON di `internal/lessons/chapter-13/`:
     - `13.1.1-valuasi-ekspor-impor-fob-vs-cif.json` (PEB, PIB, NDPBM).
     - `13.1.2-barang-dagangan-tanpa-masuk-pabean-merchanting.json` (SNA 2008).
     - `13.1.3-net-barter-terms-of-trade-nbtot.json` ($P_x / P_m \times 100$).
     - `13.1.4-gross-barter-dan-income-tot.json` ($Q_m/Q_x \times 100$ dan $\text{NBToT} \times Q_x/100$).
     - `13.2.1-definisi-wisman-dan-wisnus.json` (kriteria UNWTO $<1$ tahun, bukan mencari nafkah).
     - `13.2.2-tingkat-penghunian-kamar-tpk-hotel.json` (malam kamar terpakai / tersedia).
     - `13.2.3-rata-rata-lama-menginap-tamu-rlmt.json` (malam menginap / tamu datang).
  3. Integrasikan EXT-7 (ISP & Siklus Produk) dan EXT-8 (RCA & Openness) ke dalam 13.1.3.
  4. Kompilasi via `build_chapter_lecture.py internal/lessons/chapter-13/ --publish .`.
  5. Audit via `audit_chapter.py . --chapter 13`.
  6. Ingesti soal ke bank soal dan perbarui state `knowledge.json`.

#### **Milestone M7 — Integrasi Akhir E2E, Sinkronisasi Workspace & Verifikasi Menyeluruh**
- **Cakupan**: Seluruh artefak publik, state, mindmaps, dan test suites.
- **Langkah Kerja**:
  1. Sinkronkan seluruh 39 konsep pada `internal/state/knowledge.json` ke status `"status": "已讲解"`, `"mastery": 5`.
  2. Perbarui `internal/state/progress.json` untuk mencerminkan bahwa seluruh kurikulum pasca-UTS telah selesai dipelajari dan siap ujian.
  3. Rebuild dashboard: `uv run python .agents/skills/study-assistant/scripts/build_dashboard.py .`.
  4. Rebuild mindmaps: `uv run python .agents/skills/study-mindmap/scripts/build_mindmap.py internal/state/knowledge.json` dan `--book`.
  5. Validasi workspace: `uv run python .agents/skills/study-assistant/scripts/validate_workspace.py .` (harus `OK`).
  6. Verifikasi kepatuhan offline mandiri: `uv run python .agents/skills/exam-sprint-builder/scripts/verify_html.py` pada seluruh berkas di `open/` dan `open/chapters/`.
  7. Eksekusi rangkaian uji lengkap:
     - `uv run python tests/test_pipeline.py` (wajib 100% PASS).
     - `uv run python tests/test_e2e_modules.py` (wajib 27/27 PASS, 100% PASS).
