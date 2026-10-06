# Workflow Persiapan Ujian Official Statistics Lanjutan (OSL)

Repositori ini telah disiapkan sebagai infrastruktur terverifikasi dan berlandaskan bukti (*grounded*) untuk persiapan ujian **Official Statistics Lanjutan (OSL)**. Seluruh komponen dirancang untuk mencegah halusinasi, memisahkan materi suplemen, memvalidasi perhitungan matematika dengan kode, dan menyertakan titik kendali manusia (*human-in-the-loop*).

---

## 1. Parameter Ujian

- **Mata Kuliah**: Official Statistics Lanjutan (OSL)
- **Dosen Pengampu**: Tiodora Hadumaon Siagian
- **Jadwal Ujian**: Ujian Tertulis, 30 September 2026
- **Format**: 120 Menit, Pilihan Ganda (PG) dan Esai
- **Bahasa Keluaran**: Bahasa Indonesia (istilah resmi BPS / standar internasional tetap dipertahankan)
- **Hierarki Sumber**: `Silabus/RPS > Slide Dosen > Handout BPS/Publikasi > Soal Ujian Tahun Lalu > Catatan > Suplemen Luar`

---

## 2. Struktur Direktori Proyek

```text
.
├── .agents/skills/           # 9 skills spesialis terpasang untuk alur belajar & ujian
│   ├── study-assistant/      # Orchestrator alur belajar, kurikulum & state
│   ├── study-teach/          # Modul kuliah per poin konsep & penurunan rumus
│   ├── study-quiz/           # Kuis interaktif HTML & bank soal terpusat
│   ├── study-mindmap/        # Visualisasi peta konsep interaktif
│   ├── study-feynman/        # Penguji pemahaman berbasis Teknik Feynman
│   ├── study-img/            # Ekstraksi visual & OCR naskah soal/slide
│   ├── exam-forecast/        # Analisis longitudinal bobot & jebakan soal UAS
│   ├── exam-question-predictor/ # Prediktor soal Bloom's Taxonomy & Priority Matrix
│   └── exam-sprint-builder/  # Pembuat paket belajar kilat offline-first & cheat sheet
├── open/                     # Artefak user-facing (dashboard.html, update_dashboard.command)
├── internal/                 # State internal model (state/knowledge.json, state/progress.json, mindmaps/)
├── question-bank/            # Bank soal modular skill study-quiz (question-bank.json)
├── materials/                # Sumber primer asli (read-only)
│   ├── slides/               # Slide perkuliahan dosen (Pertemuan 8 s.d. 13)
│   ├── notes/                # Kuesioner Sakernas, Publikasi IHK BPS
│   ├── past-exams/           # Soal UAS 2022-2023, Kompilasi Latihan Soal
│   └── syllabus/             # Kontrak Perkuliahan & RPS OSL
├── extracted/                # Teks terekstrak per slide/halaman (Markdown)
│   ├── img/                  # Render PNG halaman bermasalah, tabel, & gambar
│   └── _laporan.md           # Laporan audit kuantitas halaman & kebutuhan visual
├── index/                    # Indeks pencarian materi
│   └── materi.json           # Pemetaan judul, ringkasan, kata kunci, & rujukan sitasi
├── bank/                     # Bank soal terverifikasi
│   └── soal.json             # Kumpulan soal terstruktur (PG, esai, hitungan)
├── progress/                 # Pelacakan progres belajar
│   ├── tracker.json          # Riwayat akurasi, status repetisi berjarak (1, 3, 7, 14 hari)
│   └── kesalahan.md          # Log analisis kesalahan (mistake book)
├── docs/                     # Dokumentasi metodologi
│   ├── backtest.md           # Prosedur validasi & hold-out prediksi ujian
│   ├── laporan_backtest.md   # Laporan audit dataset & baseline pembobotan silabus
│   └── konfirmasi_cakupan_silabus.md # Deliverable Langkah 3 (silabus, prioritas & mindmap)
├── forecasts/                # Proyeksi ujian UAS standar exam-forecast
│   └── OSL/uas-forecast-2026.md # Proyeksi blueprint & bobot topik UAS OSL
├── scripts/                  # Skrip otomatisasi alur kerja
│   ├── extract.py            # Ekstraksi PDF/PPTX ke Markdown & PNG
│   ├── build_index.py        # Pembuatan indeks pencarian & CLI search
│   ├── validate_bank.py      # Validator skema ketat & integritas bank/soal.json
│   ├── backtest.py           # Evaluasi akurasi prediksi longitudinal / silabus
│   ├── sample_check.py       # Sampling 10 butir soal untuk inspeksi manual
│   └── hooks/pre-commit      # Git pre-commit hook validator bank soal
├── suplemen/                 # Folder terisolasi untuk data sekunder dari web
│   └── README.md             # Panduan isolasi dan pelabelan [SUPLEMEN]
├── .claude/agents/reviewer.md# Definisi subagen reviewer independen
├── CLAUDE.md                 # Konteks proyek, aturan grounding, & titik kendali
├── AGENTS.md                 # Referensi instruksi agen setara
└── README.md                 # Panduan eksekusi skrip & workflow (file ini)
```

---

## 3. Integrasi 9 Skills Spesialis (.agents/skills/)

Untuk memaksimalkan kesiapan menghadapi UAS, repositori mengintegrasikan 9 *agent skills* modular yang terpasang pada direktori `.agents/skills/`:

| Skill | Sumber | Fungsi Utama & Kapan Digunakan | Tahap Alur Kerja |
|---|---|---|---|
| **`exam-sprint-builder`** | [GitHub Repo](https://github.com/dentar142/exam-sprint-builder) | Membuat paket belajar kilat *offline-first* (buka langsung via browser tanpa server): aplikasi kuis HTML instan, *one-page cheat sheet* A4, Obsidian study vault, dan simulasi UAS. | Langkah 8 (Paket Belajar Kilat / Sprint UAS) |
| **`exam-forecast`** | [Anthropic MCP](https://mcpservers.org/agent-skills/anthropic/exam-forecast) | Analisis longitudinal soal UAS tahun-tahun sebelumnya untuk mendeteksi bobot materi, tipe soal favorit dosen, pola jebakan, dan memproyeksikan struktur soal UAS mendatang. | Langkah 5 (Analisis Pola & Proyeksi UAS) |
| **`exam-question-predictor`** | [FindSkill.ai](https://findskill.ai/skills/education-learning/exam-question-predictor/) | Prediktor soal berbasis *Bloom's Taxonomy* & sinyal perkuliahan dosen untuk menyusun *Study Priority Matrix* (Must Study, Should Study, Quick Review, Skip). | Langkah 3 (Prioritas Silabus) & Langkah 5 |
| **`study-assistant`** | [GitHub Repo](https://github.com/2362094903-ops/study-assistant-skills) | **Orchestrator Utama**: Mengatur kurikulum belajar per bab, melacak progres belajar lintas sesi (*session state*), dan mengelola alur belajar terstruktur. | Orchestrator Seluruh Alur (Langkah 2, 3, 4, 8, 9) |
| **`study-teach`** | *Study Assistant Suite* | Menghasilkan modul ajar/catatan kuliah per poin konsep dengan penjelasan mendalam, penurunan rumus LaTeX, tabel, dan contoh soal teruji. | Langkah 4 (Pembuatan Modul Ajar) |
| **`study-quiz`** | *Study Assistant Suite* | Generator kuis interaktif HTML MathJax dengan koreksi instan, bank soal global, dan buku catatan evaluasi salah (*mistake book*). | Langkah 6 (Bank Soal) & Langkah 8 (Kuis Mandiri) |
| **`study-mindmap`** | *Study Assistant Suite* | Membuat visualisasi peta konsep (mind map) interaktif berbasis HTML mandiri dengan pewarnaan berdasarkan tingkat penguasaan materi. | Langkah 3 (Peta Konsep) & Langkah 4 |
| **`study-feynman`** | *Study Assistant Suite* | Penguji pemahaman berbasis Teknik Feynman — AI bertindak sebagai pemula kritis yang menguji apakah Anda benar-benar paham suatu konsep tanpa menghafal. | Langkah 8 (Uji Pemahaman Mendalam / Mastery) |
| **`study-img`** | *Study Assistant Suite* | Ekstraksi visual, OCR soal, transkripsi tulisan tangan, dan interpretasi diagram/grafik dari foto lembar ujian atau slide kuliah. | Langkah 1 (Ekstraksi & OCR Visual) |

---

## 4. Urutan Alur Kerja Standar (End-to-End Workflow)

Untuk mempersiapkan materi dan latihan soal secara bertahap dan terverifikasi, ikuti 9 tahap alur kerja berikut:

```text
[1. Ekstrak & OCR] ──> [2. Indeks & Kurikulum] ──> [3. Konfirmasi & Prioritas] ──> [4. Modul Ajar & Mindmap]
   (study-img)           (study-assistant)           (exam-question-predictor)       (study-teach & mindmap)
                                                               │
  ┌────────────────────────────────────────────────────────────┘
  ▼
[5. Pola & Forecast] ──> [6. Bank Soal Terstandar] ──> [7. Review Independen]
  (exam-forecast)          (study-quiz & validator)      (subagent reviewer)
                                                               │
  ┌────────────────────────────────────────────────────────────┘
  ▼
[8. Simulasi, Feynman & Sprint] ──> [9. Pelacakan Kemajuan]
  (study-feynman & sprint-builder)    (study-assistant & tracker)
```

### Langkah 1: Ekstraksi Materi & OCR Visual (`extract` / `study-img`)
- Ekstraksi teks seluruh slide kuliah PDF/PPTX dan naskah ujian ke Markdown.
- Pemanfaatan `study-img` bersama Tesseract OCR (`pytesseract`) untuk membedah slide bergambar, diagram alir BPS, dan naskah soal foto/pindaian.
```bash
uv run python scripts/extract.py
```
*Hasil:* Berkas `.md` di `extracted/`, gambar di `extracted/img/`, dan laporan status OCR di `extracted/_laporan.md`.

### Langkah 2: Pembangunan Indeks & Struktur Kurikulum (`indeks` / `study-assistant`)
- Membangun indeks pencarian instan materi terstruktur untuk mencegah kelebihan konteks model.
- `study-assistant` menginisialisasi hierarki kompetensi per pertemuan (bab, seksi, poin konsep).
```bash
uv run python scripts/build_index.py
```
*Pencarian Cepat:*
```bash
uv run python scripts/build_index.py --search "kemiskinan FGT"
uv run python scripts/build_index.py --search "IHK Laspeyres"
```

### Langkah 3: Konfirmasi Cakupan Silabus & Matriks Prioritas (Titik Kendali Manusia #1 / `exam-question-predictor` / `study-mindmap`)
- Memetakan cakupan materi pasca-UTS (Pertemuan 8 s.d. 13) berdasarkan RPS dan slide kuliah dosen pengampu (Tiodora Hadumaon Siagian).
- `exam-question-predictor` menyusun *Study Priority Matrix* (Must Study, Should Study, Quick Review, Skip) berbasis taksonomi Bloom dan sinyal penekanan materi.
- `study-mindmap` memvisualisasikan keterkaitan antarkonsep.
- **Tunggu persetujuan pengguna** sebelum memproduksi modul materi belajar massal.

### Langkah 4: Pembuatan Modul Materi Belajar Bertahap (`study-teach` / `study-mindmap`)
- `study-teach` menyusun catatan ajar terstruktur per poin konsep: *Intuisi Pemula -> Kondisi Syarat Batas -> Penurunan Rumus Rigor -> Pengenalan Tipe Soal Ujian*.
- Grounding ketat dengan sitasi wajib `[nama-file, slide/hal. N]` dan pengetahuan luar bertanda `[SUPLEMEN]`.
- Sinkronisasi status penguasaan konsep ke peta mind map.

### Langkah 5: Analisis Pola Soal & Backtest Prediksi (`exam-forecast` / `scripts/backtest.py`)
- `exam-forecast` mengevaluasi naskah soal UAS historis dan soal latihan dosen untuk mendeteksi bobot materi, tipe soal favorit dosen, pola jebakan, dan proyeksi struktur UAS.
- Evaluasi empiris dijalankan melalui:
```bash
uv run python scripts/backtest.py
```
*Laporan:* Tersimpan di `docs/laporan_backtest.md` dan `forecasts/`.

### Langkah 6: Pembuatan Sampel & Bank Soal (Titik Kendali Manusia #2 / `study-quiz`)
- `study-quiz` mengelola bank soal MathJax terpusat (`bank/soal.json`).
- Buat sampel 5–10 soal terlebih dahulu dan minta persetujuan pengguna.
- Validasi integritas skema, kunci jawaban, dan pencegahan tabrakan semantik (*false collision*):
```bash
uv run python scripts/validate_bank.py
```
- Lakukan inspeksi manual 10 butir soal hitungan:
```bash
uv run python scripts/sample_check.py
```

### Langkah 7: Review Independen Subagen (`review`)
- Kirimkan setiap butir soal ke subagen reviewer (`.claude/agents/reviewer.md`) dalam konteks terisolasi (*isolated context*) untuk validasi independen keterlandasan dan kebenaran kunci/formula. Soal hanya boleh dipakai jika berstatus `LULUS`.

### Langkah 8: Sesi Latihan, Uji Pemahaman Feynman & Paket Sprint UAS (`study-quiz` / `study-feynman` / `exam-sprint-builder`)
- `study-quiz`: Simulasi latihan soal interaktif berformat HTML dengan feedback dan skor seketika.
- `study-feynman`: Uji penguasaan konsep mendalam di mana AI bertindak sebagai pemula kritis yang menguji mahasiswa menjelaskan konsep tanpa menghafal istilah.
- `exam-sprint-builder`: Menghasilkan paket belajar kilat *offline-first* mandiri (aplikasi kuis HTML interaktif, *one-page cheat sheet* A4 resmi ringkasan rumus statistik BPS, dan Obsidian study vault).

### Langkah 9: Pelacakan Kemajuan & Repetisi Berjarak (`study-assistant`)
- `study-assistant` melacak perkembangan *mastery level* (0 s.d. 5) lintas sesi.
- Baca `progress/tracker.json` sebelum latihan untuk mengidentifikasi topik lemah (`topik_lemah: true` pada `ringkasan_topik`) dan soal yang jatuh tempo (`status: "perlu_latihan"` pada `riwayat_soal`, dengan `tahap_interval` 0-3 memetakan interval *spaced repetition: 1, 3, 7, 14 hari*).
- Perbarui `progress/tracker.json` setelah latihan dan catat analisis kesalahan ke `progress/kesalahan.md` (mistake book).

---

## 5. Panduan Eksekusi Skrip Proyek

| Skrip | Perintah Eksekusi | Deskripsi & Fungsi |
|---|---|---|
| **Ekstraksi Materi** | `uv run python scripts/extract.py` | Mengekstrak teks PDF/PPTX, render visual, buat laporan `_laporan.md`. |
| **Pembangun Indeks** | `uv run python scripts/build_index.py` | Membangun `index/materi.json` dari berkas `extracted/`. |
| **Pencarian Indeks** | `uv run python scripts/build_index.py --search "<kata kunci>"` | Menemukan slide/halaman dan rujukan sitasi secara presisi. |
| **Validator Bank Soal**| `uv run python scripts/validate_bank.py` | Memeriksa integritas field, kunci PG, duplikasi, dan label suplemen. |
| **Backtest Prediksi** | `uv run python scripts/backtest.py [--simulate-multi-year]` | Mengevaluasi akurasi prediksi longitudinal atau fallback ke silabus. |
| **Inspeksi Sampel** | `uv run python scripts/sample_check.py [--n 10] [--jenis hitungan]` | Menampilkan kartu checklist inspeksi manual untuk 10 butir soal acak. |
| **Pengujian Otomatis** | `uv run python tests/test_pipeline.py` | Menjalankan seluruh test suite integritas pipeline dan skema. |

---

## 6. Status Kendala Eksternal & Korpus Soal Ujian (Status Terkini)

Berdasarkan perkembangan terbaru di lingkungan sistem dan audit materi:

1. **Tool OCR Mesin (Tesseract)**:
   - **Status**: **TERPASANG & AKTIF** (`/usr/bin/tesseract` v5.5.3, paket bahasa: `ind` dan `eng`).
   - **Integrasi**: Pustaka `pytesseract` telah ditambahkan ke virtual environment (`.venv`). Skrip `scripts/extract.py` secara otomatis menjalankan OCR pada halaman/slide berteks minim yang berisi gambar/diagram (PDF dan PPTX) serta menyimpannya ke berkas Markdown terekstrak (`extracted/`).
   - **Audit**: Rincian status OCR terdokumentasi lengkap di `extracted/_laporan.md`.
2. **Ketersediaan Naskah Soal Ujian (Past Exams)**:
   - **Status**: **TERVERIFIKASI & DIPETAKAN LENGKAP**. Korpus soal ujian yang tersedia secara definitif adalah:
     1. `materials/past-exams/soal_latihan_uas.md`: 50 butir soal latihan resmi persiapan UAS dari dosen pengampu (Tiodora Hadumaon Siagian, 100% Pilihan Ganda).
     2. `extracted/Soal_UAS_2022-2023.md` (sumber: `materials/past-exams/Soal UAS 2022-2023.pdf`): 42 butir soal naskah ujian resmi UAS 2022/2023 (40 Pilihan Ganda dan 2 Esai).
   - **Metodologi Backtest**:
     - *Longitudinal Antar-Tahun Resmi*: Karena naskah resmi tahunan baru tersedia 1 tahun (2022/2023), backtest longitudinal tahun-ke-tahun dialihkan ke **Baseline Silabus/RPS (16,67% per pertemuan)** untuk mencegah overfitting pada satu titik historis.
     - *Evaluasi Silang Empiris (Cross-Material)*: Skrip `scripts/backtest.py` secara langsung mengevaluasi keselarasan antara paket latihan dosen terhadap soal ujian riil, menghasilkan **Top-5 Hit Rate 80.0%** dan deviasi bobot rata-rata (**MAE**) yang sangat rendah yaitu **8.73%**. Laporan lengkap tersedia di `docs/laporan_backtest.md`.
