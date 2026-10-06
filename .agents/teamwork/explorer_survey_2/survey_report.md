# Laporan Survei Kode & Pipeline Infrastruktur OSL (Codebase & Pipeline Survey Report)

**Penyusun**: Survey Agent 2 (Codebase & Pipeline Explorer)  
**Tanggal**: 2026-09-29  
**Repositori**: `/home/alfzki/Documents/OSL`  
**Tujuan**: Pemetaan komprehensif struktur workspace, kontrak state schema, runner pengujian integritas (`tests/test_pipeline.py`), mekanisme kompilasi modul ajar Markdown & HTML interaktif mandiri, serta status `knowledge.json` dan `progress.json` untuk 39 poin konsep pasca-UTS (Pertemuan 8 s.d. 13).

---

## 1. Arsitektur Workspace & Inventarisasi Komponen Eksisting

Workspace OSL mengadopsi standar modern *study workspace* yang memisahkan secara ketat artefak publik (*user-facing*) dan state internal (*model & state files*):

```text
/home/alfzki/Documents/OSL/
├── open/                         # Artefak publik / user-facing
│   ├── dashboard.html            # Dashboard belajar interaktif (mastery & progress overview)
│   ├── update_dashboard.command  # Script penyegaran dashboard lokal (chmod +x)
│   ├── chapters/                 # Direktori kompilasi HTML kuliah per bab (SAAT INI KOSONG)
│   └── quizzes/                  # Direktori kuis interaktif HTML mandiri (SAAT INI KOSONG)
├── internal/                     # State internal model, pelacakan, dan draft materi
│   ├── state/
│   │   ├── knowledge.json        # Single source of truth 39 poin konsep (Chapters 8-13)
│   │   ├── progress.json         # State sesi, current_chapter, current_point, log aktivitas
│   │   ├── digest.md             # Ringkasan ringkas status belajar (dihasilkan build_dashboard.py)
│   │   └── exam-style.md         # Profil format ujian, karakteristik dosen & aturan penilaian
│   ├── mindmaps/                 # Peta konsep interaktif SVG/HTML (zero-dependency)
│   │   ├── book.html             # Peta konsep terpadu seluruh buku (Pertemuan 8 s.d. 13)
│   │   └── chapter-08.html s.d. chapter-13.html # Peta konsep per pertemuan
│   ├── lessons/                  # Direktori unit JSON/MD/HTML kuliah per bab (SAAT INI KOSONG)
│   ├── reports/                  # Laporan audit bab (chapter-XX-audit.json & .md) (SAAT INI KOSONG)
│   ├── textbook/                 # Bahan ajar acuan audit (chapter-XX.md) (SAAT INI KOSONG)
│   └── assets/                   # Aset grafis internal
├── materials/                    # Sumber primer asli (READ-ONLY)
│   ├── slides/                   # Slide kuliah resmi Pertemuan 8 s.d. 13 (.pptx & .pdf)
│   ├── notes/                    # Kuesioner Sakernas Ags 2025 & Publikasi IHK 2025 BPS
│   ├── past-exams/               # Soal UAS 2022/2023 (.pdf) & soal_latihan_uas.md (50 soal)
│   └── syllabus/                 # Kontrak perkuliahan & RPS OSL Genap TA 2025/2026 (.pptx)
├── extracted/                    # Teks hasil ekstraksi materi primer (Markdown & Gambar)
│   ├── Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md
│   ├── Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md
│   ├── Pertemuan_10_Indikator_Kesehatan.md
│   ├── Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md
│   ├── Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md
│   ├── Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md
│   ├── Kuesioner_SAK.AGS25-AK.md
│   ├── indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.md
│   ├── Soal_UAS_2022-2023.md (42 butir soal ter-OCR & terekstraksi)
│   ├── Tiodora_3SI1_Kontrak_Perkuliahan_OSL_Genap_TA_2025_2026_Politeknik_Statistika_STIS.md
│   ├── img/                      # Gambar/tabel/diagram slide hasil ekstraksi visual
│   └── _laporan.md               # Laporan status OCR dan inspeksi visual ekstraksi
├── question-bank/
│   └── question-bank.json        # Bank soal terstruktur modular (saat ini memuat 10 butir terindeks)
├── bank/
│   └── soal.json                 # Bank soal resmi terverifikasi validator (10 butir terverifikasi)
├── progress/
│   ├── tracker.json              # Riwayat repetisi berjarak (interval 1, 3, 7, 14 hari)
│   └── kesalahan.md              # Buku catatan evaluasi kesalahan (mistake book)
├── index/
│   └── materi.json               # Indeks pencarian materi (610 segmen slide/dokumen)
├── forecasts/
│   └── OSL/uas-forecast-2026.md  # Blueprint proyeksi bobot materi & tipe soal UAS 2026
├── docs/
│   ├── konfirmasi_cakupan_silabus.md # Deliverable Langkah 3: Matriks prioritas & silabus
│   └── laporan_backtest.md       # Laporan analisis empiris silang latihan vs UAS
├── tests/
│   └── test_pipeline.py          # Test suite integritas pipeline end-to-end (8 test suites)
└── .agents/skills/               # 9 skills spesialis terpasang
    ├── study-assistant/          # Orchestrator alur belajar, kurikulum & state validator
    ├── study-teach/              # Generator modul ajar per poin konsep & kompilator bab
    ├── study-quiz/               # Generator kuis interaktif HTML & manager bank soal
    ├── study-mindmap/            # Visualisasi peta konsep interaktif SVG/HTML
    ├── study-feynman/            # Penguji pemahaman berbasis Teknik Feynman
    ├── study-img/                # Ekstraksi visual & OCR naskah soal/slide
    ├── exam-forecast/            # Analisis longitudinal bobot & pola soal ujian
    ├── exam-question-predictor/  # Prediktor soal Bloom's Taxonomy & Study Priority Matrix
    └── exam-sprint-builder/      # Pembuat paket sprint UAS offline-first & verifikator HTML
```

---

## 2. Syarat Mutlak Validator State (`validate_workspace.py`)

Perintah validasi:
```bash
uv run python .agents/skills/study-assistant/scripts/validate_workspace.py .
```

Agar perintah tersebut mengembalikan exit code **0 (`OK`)**, seluruh persyaratan berikut wajib terpenuhi tanpa pelanggaran:

### A. Integritas Struktur Direktori (*Layout Check*)
Apabila folder `internal/` ada, skrip memeriksa keberadaan **9 direktori wajib**:
1. `open/`
2. `open/chapters/`
3. `open/quizzes/`
4. `internal/state/`
5. `internal/textbook/`
6. `internal/lessons/`
7. `internal/mindmaps/`
8. `internal/reports/`
9. `question-bank/`

*Status saat ini*: Seluruh 9 direktori telah ada dan valid.

### B. Kontrak Schema `knowledge.json` (`internal/state/knowledge.json`)
1. **Field Tingkat Atas (Top-Level Keys)**: Wajib memuat `"textbook"`, `"subject_type"`, `"updated"`, dan `"chapters"`.
2. **Struktur Bab (`chapters[]`)**:
   - `id`: Wajib bertipe `int` (misal 8, 9, 10, 11, 12, 13).
   - `title`: Wajib berupa *string* tidak kosong.
   - `sections`: Wajib berupa *list* dan tidak boleh kosong.
3. **Struktur Subbab (`sections[]`)**:
   - `title`: Wajib berupa *string* tidak kosong.
   - `points`: Wajib berupa *list* poin konsep.
4. **Struktur Poin Konsep (`points[]`)**:
   - `id`: Wajib mencocokkan ekspresi reguler `r"^\d+(\.\d+)+$"` (contoh: `"8.1.1"`).
   - **Keunikan ID**: Setiap `id` wajib unik secara global di seluruh berkas.
   - `name`: Wajib berupa *string* tidak kosong (judul ringkas poin konsep).
   - `importance`: Wajib bernilai salah satu dari enum `["高", "中", "低"]` (Tinggi, Sedang, Rendah).
   - `status`: Wajib bernilai salah satu dari enum `["未学", "已讲解", "已测验", "已检验"]`.
   - `mastery`: Wajib berupa angka (`int` atau `float`) dalam rentang batas $[0, 5]$.
   - `note`: Wajib ada dalam dictionary poin (boleh berupa string kosong `""`).

### C. Kontrak Schema `progress.json` (`internal/state/progress.json`)
1. **Field Wajib Tingkat Atas**: `"current_chapter"`, `"current_point"`, `"next_action"`, `"exam_style_ready"`, `"log"`.
2. **Validitas `current_point`**: Nilai `current_point` (jika tidak kosong) **wajib terdaftar** dalam daftar ID poin konsep yang ada di `knowledge.json`.
3. **Field `log`**: Wajib bertipe `list`, dan setiap entri berupa objek `{"date": "...", "event": "..."}` dengan kedua nilai tidak kosong.
4. **Atribut Opsional Terikat**:
   - `lecture_format` (jika ada): Wajib salah satu dari `"obsidian"`, `"html"`, `"both"`.
   - `study_mode` (jika ada): Wajib salah satu dari `"deep"`, `"speedrun"`.

---

## 3. Rincian Pengujian Integrasi Pipeline (`tests/test_pipeline.py`)

Test suite dijalankan dengan:
```bash
uv run python tests/test_pipeline.py
```
Test suite memuat 8 unit/integration test function yang memeriksa seluruh ekosistem persiapan ujian:

| No | Nama Uji | Sasaran Pemeriksaan & Verifikasi | Syarat Lulus & Nilai Ambang Batas |
|---|---|---|---|
| **1** | `test_validator_on_real_bank` | Integritas `bank/soal.json` via `validate_bank` | - Jumlah soal tepat 10 butir.<br>- `jenis` mencakup `pg`, `isian`, `esai`, `hitungan`.<br>- `asal` mencakup `materi`, `soal-lama`, `suplemen`. |
| **2** | `test_validator_edge_cases` | Robustness validator semantik & aturan eliminasi | - Menolak field wajib yang hilang.<br>- Menolak sumber kosong atau tanpa nomor slide/halaman.<br>- Menolak opsi PG yang tidak cocok dengan kunci.<br>- Menolak soal suplemen tanpa label `[SUPLEMEN]`.<br>- Menolak duplikat (leksikal >85%) tetapi mencegah false-collision pada indikator FGT ($P_0$ vs $P_1$). |
| **3** | `test_index_quality` | Kualitas segmentasi pencarian materi `index/materi.json` | - Berkas ada dan memuat $\ge 600$ segmen (saat ini 610 segmen).<br>- Tidak ada judul segmen yang berupa angka polos, `---`, kosong, atau karakter pipa tabel `\|`.<br>- Fungsi `extract_title` lolos uji parsing. |
| **4** | `test_backtest_pipeline` | Pipeline evaluasi longitudinal backtest prediksi | - Mendeteksi naskah ujian resmi historis.<br>- Mengaktifkan cabang fallback jika naskah $< 2$ (proporsi 16,67% per bab).<br>- Menguji kalkulasi simulasi multi-tahun (Top-3 hit rate & MAE). |
| **5** | `test_tracker_integrity` | Keselarasan `progress/tracker.json` dengan bank soal | - ID pada `bank/soal.json` identik 100% dengan `tracker["riwayat_soal"]`.<br>- Interval spaced repetition baku: `[1, 3, 7, 14]` hari. |
| **6** | `test_ocr_engine_integration` | Ketersediaan binary Tesseract dan modul `pytesseract` | - Binary `tesseract` terdeteksi pada PATH OS.<br>- Flag `CAN_OCR == True`.<br>- Bahasa `eng` dan `ind` aktif.<br>- Berkas `extracted/_laporan.md` mencantumkan status 'Tersedia'. |
| **7** | `test_exam_corpora_and_cross_evaluation` | Parsing korpus soal latihan vs naskah UAS riil | - `materials/past-exams/soal_latihan_uas.md` tepat memuat 50 butir PG.<br>- `extracted/Soal_UAS_2022-2023.md` tepat memuat 42 butir (40 PG, 2 Esai).<br>- Robustness parser pada edge text (heading H5, nomor rapat, dsb).<br>- Evaluasi silang empiris: Top-5 Hit Rate $\ge 60,0\%$ (aktual: $80,0\%$) dan MAE $\le 12,0\%$ (aktual: $8,73\%$).<br>- Berkas `docs/laporan_backtest.md` ada dan memuat metrik terkait. |
| **8** | `test_skills_integration_and_step3_deliverables` | Kepatuhan 9 skills & deliverable Langkah 3 | - 9 direktori skill ada dan memuat `SKILL.md` dengan frontmatter YAML `name:` dan `description:`.<br>- 9 skills terdokumentasi di `README.md`, `CLAUDE.md`, dan `AGENTS.md`.<br>- `docs/konfirmasi_cakupan_silabus.md` memuat Pertemuan 8 s.d. 13, Matriks Prioritas, Human Checkpoint, HIGH CONFIDENCE, dan Contoh Soal Prediksi.<br>- `forecasts/OSL/uas-forecast-2026.md` memuat Topic Weighting Matrix & Blueprint.<br>- `validate_workspace.py` dieksekusi dengan return code 0.<br>- `internal/mindmaps/book.html` memuat Pertemuan 8 s.d. 13; `chapter-{08..13}.html` lengkap.<br>- `open/dashboard.html` ada; `internal/state/digest.md` memuat "39".<br>- `internal/state/exam-style.md` ada; `question-bank/question-bank.json` memuat $\ge 10$ entri. |

*Hasil eksekusi*: Seluruh 8 pengujian saat ini **LULUS 100% (PASS)** tanpa error atau kegagalan.

---

## 4. Mekanisme Kompilasi Modul Ajar (Markdown & HTML Interaktif)

Alur produksi materi pembelajaran dari poin konsep hingga menjadi paket modul ajar terpadu diatur melalui skrip spesialis berikut:

### Alur 1: Pembentukan Unit JSON Poin Konsep (`study-teach`)
Setiap poin konsep disusun menjadi berkas JSON tersendiri di dalam direktori `internal/lessons/chapter-XX/<point-id>-<nama-sanitasi>.json`.
Struktur JSON mematuhi schema `build_lecture.py`:
- `textbook`: `"Official Statistics Lanjutan (OSL)"`
- `chapter_id`: integer bab (8 s.d. 13)
- `chapter_title`: nama lengkap bab
- `section`: nomor dan nama subbab (misal `"8.1 Konsep dan Metodologi Garis Kemiskinan BPS"`)
- `mode`: `"deep"` (sesuai kontrak perkuliahan dan `progress.json`)
- `points`: array berisi 1 objek poin konsep:
  - `id`: contoh `"8.1.1"`
  - `name`: contoh `"Konsep Kemiskinan Absolut dan Relatif"`
  - `importance`: `"高"`, `"中"`, atau `"低"`
  - `source_ref`: rujukan sitasi presisi `[nama-file, slide/hal. N]`
  - `exam_focus`: orientasi tipe soal dan jebakan ujian
  - `textbook_excerpt`: kutipan materi primer BPS
  - `intuition`: penjelasan intuitif dan analogi batas
  - `formal`: penurunan rumus LaTeX rigor dan definisi operasional BPS (wajib pada mode deep)
  - `pitfalls`: pembahasan jebakan dosen (*common pitfalls*)
  - `memory_hook`: jembatan keledai / pengingat cepat
  - `figures`: array gambar/diagram (path, caption, source, alt) jika relevan
  - `examples`: latihan soal interaktif berformat:
    - `type`: `"single"`, `"multi"`, `"judge"`, atau `"text"` (hitungan/esai)
    - `problem`: narasi soal dan tabel angka
    - `options`: opsi pilihan ganda (jika single/multi)
    - `answer`: indeks kunci jawaban atau teks solusi angka
    - `solution`: langkah kalkulasi matematis bertahap dan pembahasan lengkap
    - `source_ref`: rujukan sumber soal
  - `links`: array relasi ke ID poin konsep lain

Kompilasi unit individu:
```bash
uv run python .agents/skills/study-teach/scripts/build_lecture.py \
  internal/lessons/chapter-08/8.1.1-konsep-kemiskinan-absolut-dan-relatif.json --format both
```

### Alur 2: Penggabungan dan Penerbitan Kuliah Bab (`build_chapter_lecture.py`)
Setelah seluruh unit poin konsep dalam satu bab selesai ditulis, modul digabungkan menjadi satu modul utuh per bab:
```bash
uv run python .agents/skills/study-teach/scripts/build_chapter_lecture.py \
  internal/lessons/chapter-08/ --format both --publish .
```
Efek eksekusi dengan argumen `--publish .`:
1. Membaca seluruh `*.json` di `internal/lessons/chapter-08/`, memvalidasi konsistensi metadata dan mencegah ID duplikat.
2. Menghasilkan modul Markdown bab terpadu: `internal/lessons/chapter-08/chapter-08.md`.
3. Menghasilkan modul HTML interaktif mandiri: `internal/lessons/chapter-08/chapter-08.html`.
4. Menerbitkan berkas HTML publik siap pakai ke `open/chapters/chapter-08.html` dan menyalin seluruh aset grafis terkait ke `open/chapters/assets/chapter-08/`.
5. HTML yang dihasilkan memuat:
   - TOC dinamis sticky di sisi kiri dengan indikator kelulusan (*checkmarks*), bobot bintang `⭐`, dan label mode.
   - Script interaktif untuk tombol status belajar (`标记为已学` / `✓ 已学完`) yang tersinkron ke `localStorage`.
   - Engine evaluasi interaktif untuk soal latihan (single choice, multi choice, boolean judge, dan input perhitungan numerik) yang memvalidasi jawaban sebelum membuka pembahasan lengkap.

### Alur 3: Audit Kualitas Bab (*Quality Gate Audit* — `audit_chapter.py`)
Sebelum bab dinyatakan selesai, jalankan audit terhadap materi sumber:
```bash
uv run python .agents/skills/study-assistant/scripts/audit_chapter.py . --chapter 8
```
Pemeriksaan audit mencakup:
1. **Kelengkapan Poin**: Seluruh poin konsep bab terkait di `knowledge.json` wajib ada di `internal/lessons/chapter-XX/*.json`. Jika ada poin yang tertinggal $\rightarrow$ status `blocked` (exit code 1).
2. **Keterbawaan Visual & Tabel**: Jika teks acuan (`internal/textbook/chapter-XX.md` atau `extracted/`) memuat diagram/grafik/tabel, modul ajar wajib menyertakan `figures` atau tabel Markdown.
3. **Keterbawaan Contoh Soal**: Jika materi primer memuat contoh soal, modul ajar wajib memuat `examples`.
4. **Keterbawaan Formula**: Jika materi primer memuat rumus, modul wajib menyertakan ekspresi matematis LaTeX.
5. **Sitasi Rujukan**: Seluruh gambar dan soal wajib memiliki `source_ref`.
6. **Keluaran**: Menghasilkan `internal/reports/chapter-XX-audit.json` dan `chapter-XX-audit.md`. Jika status `pass`, dashboard akan menampilkan label status hijau `已完成` (Selesai).

### Alur 4: Verifikasi Mandiri Offline (*Offline-First Verification* — `verify_html.py`)
Setiap berkas HTML yang diterbitkan diuji dengan:
```bash
uv run python .agents/skills/exam-sprint-builder/scripts/verify_html.py open/chapters/chapter-08.html
```
Kriteria verifikasi:
- **Zero External URLs**: Tidak ada URL `http://` / `https://` atau hostname CDN eksternal (MathJax dan styling beroperasi mandiri).
- **Zero Placeholder Residue**: Bebas dari token placeholder generator (`__BANK__`, `__CONTENT__`, `INSERT_HERE`, dsb).
- **Tema & Responsivitas**: Penanda `data-theme` dan tombol toggle tema berfungsi.
- **Batas Ukuran**: Ukuran berkas $< 5\text{ MB}$.

### Alur 5: Sinkronisasi Dashboard & Peta Konsep
Setelah modul atau kuis diperbarui:
1. Jalankan pembangun dashboard:
   ```bash
   uv run python .agents/skills/study-assistant/scripts/build_dashboard.py .
   ```
   Menghasilkan `internal/state/digest.md` dan `open/dashboard.html` dengan tautan aktif ke `open/chapters/chapter-XX.html`.
2. Jalankan pembangun peta konsep:
   ```bash
   uv run python .agents/skills/study-mindmap/scripts/build_mindmap.py internal/state/knowledge.json
   uv run python .agents/skills/study-mindmap/scripts/build_mindmap.py internal/state/knowledge.json --book
   ```

---

## 5. Status Eksisting & Rencana Pembaruan 39 Konsep (`knowledge.json` & `progress.json`)

### A. Inventarisasi 39 Konsep pada `knowledge.json`

| Bab / Pertemuan | Kode Poin | Nama Poin Konsep | Tingkat Kepentingan | Status Saat Ini | Skor Mastery |
|---|---|---|---|---|---|
| **Bab 8: Kemiskinan & Gini** | 8.1.1 | Konsep Kemiskinan Absolut dan Relatif | 高 (Tinggi) | 未学 (Belum Belajar) | 0 / 5 |
| | 8.1.2 | Garis Kemiskinan Makanan dan Non-Makanan | 高 (Tinggi) | 未学 | 0 / 5 |
| | 8.1.3 | Metodologi Cost of Basic Needs BPS | 高 (Tinggi) | 未学 | 0 / 5 |
| | 8.2.1 | Headcount Index P0 | 高 (Tinggi) | 未学 | 0 / 5 |
| | 8.2.2 | Poverty Gap Index P1 | 高 (Tinggi) | 未学 | 0 / 5 |
| | 8.2.3 | Poverty Severity Index P2 | 高 (Tinggi) | 未学 | 0 / 5 |
| | 8.3.1 | Kurva Lorenz dan Koefisien Gini | 高 (Tinggi) | 未学 | 0 / 5 |
| | 8.3.2 | Kriteria Ketimpangan Bank Dunia | 高 (Tinggi) | 未学 | 0 / 5 |
| **Bab 9: Ketenagakerjaan & Pendidikan** | 9.1.1 | Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja | 高 (Tinggi) | 未学 | 0 / 5 |
| | 9.1.2 | Tingkat Partisipasi Angkatan Kerja TPAK | 中 (Sedang) | 未学 | 0 / 5 |
| | 9.1.3 | Tingkat Pengangguran Terbuka TPT | 高 (Tinggi) | 未学 | 0 / 5 |
| | 9.1.4 | Setengah Penganggur vs Pekerja Paruh Waktu | 高 (Tinggi) | 未学 | 0 / 5 |
| | 9.2.1 | Angka Partisipasi Murni APM dan Kasar APK | 中 (Sedang) | 未学 | 0 / 5 |
| | 9.2.2 | Angka Partisipasi Sekolah APS | 中 (Sedang) | 未学 | 0 / 5 |
| **Bab 10: Kesehatan & SDGs 3** | 10.1.1 | Angka Kematian Ibu AKI MMR | 中 (Sedang) | 未学 | 0 / 5 |
| | 10.1.2 | Angka Kematian Bayi AKB dan Balita AKABA | 中 (Sedang) | 未学 | 0 / 5 |
| | 10.1.3 | Angka Kematian Neo-Natal NMR | 低 (Rendah) | 未学 | 0 / 5 |
| | 10.2.1 | Angka Kesakitan Morbiditas | 低 (Rendah) | 未学 | 0 / 5 |
| | 10.2.2 | Imunisasi Dasar Lengkap IDL | 低 (Rendah) | 未学 | 0 / 5 |
| **Bab 11: Statistik Produksi** | 11.1.1 | Kerangka Sampel Area KSA Padi | 高 (Tinggi) | 未学 | 0 / 5 |
| | 11.1.2 | Metode Ubinan Produktivitas | 高 (Tinggi) | 未学 | 0 / 5 |
| | 11.1.3 | Survei Konversi Gabah ke Beras SKGB | 中 (Sedang) | 未学 | 0 / 5 |
| | 11.2.1 | Survei Industri Besar dan Sedang IBS | 中 (Sedang) | 未学 | 0 / 5 |
| | 11.2.2 | Survei Industri Mikro dan Kecil IMK | 低 (Rendah) | 未学 | 0 / 5 |
| **Bab 12: Perdagangan, IHK & NTP** | 12.1.1 | Margin Perdagangan dan Pengangkutan MPP | 中 (Sedang) | 未学 | 0 / 5 |
| | 12.1.2 | Survei Pola Distribusi Perdagangan Poldis | 中 (Sedang) | 未学 | 0 / 5 |
| | 12.2.1 | IHK Rumus Modified Laspeyres | 高 (Tinggi) | 未学 | 0 / 5 |
| | 12.2.2 | Tiga Laju Inflasi BPS mtom yony ytd | 高 (Tinggi) | 未学 | 0 / 5 |
| | 12.2.3 | Disagregasi Inflasi Inti Bergejolak Administered | 高 (Tinggi) | 未学 | 0 / 5 |
| | 12.3.1 | Konsep dan Rasio NTP It per Ib | 高 (Tinggi) | 未学 | 0 / 5 |
| | 12.3.2 | Nilai Tukar Usaha Petani NTUP | 高 (Tinggi) | 未学 | 0 / 5 |
| | 12.3.3 | Lima Subsektor Penyusun NTP | 中 (Sedang) | 未学 | 0 / 5 |
| **Bab 13: Ekspor-Impor & Pariwisata** | 13.1.1 | Valuasi Ekspor Impor FOB vs CIF | 高 (Tinggi) | 未学 | 0 / 5 |
| | 13.1.2 | Barang Dagangan Tanpa Masuk Pabean Merchanting | 中 (Sedang) | 未学 | 0 / 5 |
| | 13.1.3 | Net Barter Terms of Trade NBToT | 高 (Tinggi) | 未学 | 0 / 5 |
| | 13.1.4 | Gross Barter dan Income ToT | 中 (Sedang) | 未学 | 0 / 5 |
| | 13.2.1 | Definisi Wisman dan Wisnus | 中 (Sedang) | 未学 | 0 / 5 |
| | 13.2.2 | Tingkat Penghunian Kamar TPK Hotel | 高 (Tinggi) | 未学 | 0 / 5 |
| | 13.2.3 | Rata-rata Lama Menginap Tamu RLMT | 中 (Sedang) | 未学 | 0 / 5 |

**Distribusi Tingkat Kepentingan**:
- **Tinggi (高)**: 19 poin (48,7%)
- **Sedang (中)**: 16 poin (41,0%)
- **Rendah (低)**: 4 poin (10,3%)
- **Total**: 39 poin konsep

### B. Status Eksisting `progress.json`
```json
{
  "current_chapter": 8,
  "current_point": "8.1.1",
  "next_action": "Konfirmasi Cakupan Silabus & Peta Konsep (Langkah 3)",
  "exam_style_ready": true,
  "lecture_format": "both",
  "study_mode": "deep",
  "log": [
    {
      "date": "2026-09-29",
      "event": "Inisialisasi kurikulum dan pemetaan 40 poin konsep silabus pasca-UTS (Langkah 3)"
    }
  ]
}
```

### C. Kebutuhan Pembaruan State Berkelanjutan
1. **Transisi Status & Mastery Poin Konsep di `knowledge.json`**:
   - Saat modul dibuat: status bertransisi dari `"未学"` $\rightarrow$ `"已讲解"`, mastery naik menjadi $1 - 3$.
   - Saat kuis diselesaikan: status bertransisi $\rightarrow$ `"已测验"`, mastery naik menjadi $3 - 4$.
   - Saat uji pemahaman (Feynman) disahkan: status $\rightarrow$ `"已检验"`, mastery mencapai $5$.
   - Catatan kelemahan/jebakan dimasukkan pada kolom `"note"`.
2. **Pembaruan Berkelanjutan pada `progress.json`**:
   - `current_chapter` bergulir dari bab $8 \rightarrow 9 \rightarrow 10 \rightarrow 11 \rightarrow 12 \rightarrow 13$.
   - `current_point` bergulir mengikuti poin konsep aktif.
   - `next_action` bergeser dari "Konfirmasi Cakupan Silabus" menjadi "Pembuatan Modul Ajar Pertemuan 8 s.d. 13", "Kompilasi Modul Bab & Audit", dan "Simulasi UAS & Uji Feynman".
   - `log` ditambahkan entri aktivitas bertanggal untuk setiap penyelesaian modul bab dan audit.
3. **Penyelarasan Artefak Turunan**:
   - Menghubungkan teks acuan silabus ke `internal/textbook/chapter-XX.md` (atau membuat symlink/copy dari berkas di `extracted/`) agar fungsi `audit_chapter.py` dapat memverifikasi keterbawaan rumus, tabel, dan contoh soal secara otomatis.
   - Menjalankan kembali `build_mindmap.py` agar pewarnaan node mindmap mencerminkan peningkatan mastery.
   - Menjalankan kembali `build_dashboard.py` agar ringkasan `digest.md` dan tabel kemajuan bab pada `open/dashboard.html` memuat status kelulusan audit hijau (`已完成`).

---

## 6. Ringkasan Kesiapan Eksekusi

Infrastruktur pengujian, validator state, generator mindmap, generator kuis, dan engine kompilasi modul berada dalam status **100% prima dan siap digunakan**:
- `test_pipeline.py`: **8/8 PASS (100%)**
- `validate_workspace.py`: **Exit code 0 (OK)**
- Skrip kompilasi dan audit (`build_lecture.py`, `build_chapter_lecture.py`, `audit_chapter.py`, `build_quiz.py`, `build_mindmap.py`, `build_dashboard.py`) siap dieksekusi secara terotomasi via `uv run`.
