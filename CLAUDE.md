# Pedoman Proyek & Konteks AI (Official Statistics Lanjutan)

Dokumen ini merupakan panduan instruksi utama untuk agen AI yang bekerja dalam proyek persiapan ujian **Official Statistics Lanjutan (OSL)**. Seluruh agen wajib mematuhi aturan grounding, hierarki sumber, dan titik kendali manusia yang tercantum di sini.

---

## 1. Konteks Ujian & Perkuliahan

- **Mata Kuliah**: Official Statistics Lanjutan (OSL)
- **Dosen Pengampu**: Tiodora Hadumaon Siagian
- **Jenis & Tanggal Ujian**: Ujian Tertulis, 30 September 2026
- **Format Ujian**: 120 menit, Pilihan Ganda (PG) dan Esai (jumlah soal dan bobot per butir belum ditentukan secara pasti).
- **Bahasa Keluaran Wajib**: **Bahasa Indonesia** (istilah teknis statistik resmi BPS / internasional seperti *SNA 2008*, *ICLS 13*, *IHK*, *NTP*, *TPK*, *trade openness*, *SDGs* tetap dipertahankan sesuai konvensi).
- **Lokasi Berkas Materi**:
  - Slide Kuliah Dosen: `materials/slides/` (format `.pdf` dan `.pptx`)
  - Catatan & Dokumen Resmi: `materials/notes/` (kuesioner BPS, publikasi IHK)
  - Soal Tahun Lalu & Latihan: `materials/past-exams/`
  - Silabus / Kontrak Kuliah / RPS: `materials/syllabus/`
  - Pengetahuan Tambahan / Web: `suplemen/`

---

## 2. Struktur Folder & Konvensi Penamaan

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
├── materials/                # Sumber primer asli (read-only, tidak boleh diubah)
│   ├── slides/               # Slide perkuliahan dosen
│   ├── notes/                # Kuesioner, publikasi, catatan resmi
│   ├── past-exams/           # Arsip soal ujian tahun lalu & latihan
│   └── syllabus/             # RPS, silabus, dan kontrak perkuliahan
├── extracted/                # Teks hasil ekstraksi per slide/halaman (Markdown)
│   ├── img/                  # Render PNG halaman bermasalah/rumus/gambar slide
│   └── _laporan.md           # Laporan audit ekstraksi, status OCR, dan inspeksi visual
├── index/                    # Indeks materi terstruktur
│   └── materi.json           # Pemetaan judul, ringkasan, kata kunci, dan rujukan slide
├── bank/                     # Bank soal terverifikasi
│   └── soal.json             # Kumpulan soal berformat JSON terstandar
├── progress/                 # Pelacakan hasil belajar
│   ├── tracker.json          # Riwayat akurasi, status repetisi berjarak, topik lemah
│   └── kesalahan.md          # Log analisis kesalahan (mistake book)
├── docs/                     # Dokumentasi prosedur & metodologi
│   ├── backtest.md           # Prosedur validasi & backtest prediksi soal
│   └── konfirmasi_cakupan_silabus.md # Deliverable Langkah 3 (silabus, prioritas & mindmap)
├── forecasts/                # Proyeksi ujian UAS standar exam-forecast
│   └── OSL/uas-forecast-2026.md # Proyeksi blueprint & bobot topik UAS OSL
├── scripts/                  # Skrip otomatisasi alur kerja
│   ├── extract.py            # Ekstraksi PDF/PPTX ke Markdown & PNG
│   ├── build_index.py        # Pembuatan indeks pencarian materi (materi.json)
│   ├── validate_bank.py      # Validator skema & integritas soal.json
│   ├── backtest.py           # Evaluasi akurasi prediksi longitudinal
│   ├── sample_check.py       # Sampling 10 butir soal untuk inspeksi manual
│   └── hooks/                # Git hook validasi bank soal
├── suplemen/                 # Berkas eksternal dari web (terisolasi ketat)
├── .claude/agents/           # Konfigurasi subagen mandiri (e.g. reviewer.md)
├── CLAUDE.md                 # Konteks proyek & aturan grounding (file ini)
├── AGENTS.md                 # Rujukan agen setara
└── README.md                 # Panduan cepat eksekusi skrip & workflow
```

---

## 3. Hierarki Sumber (Source Hierarchy)

Saat terjadi pertentangan atau perbedaan istilah/angka, urutan otoritas sumber adalah:

1. **Silabus / RPS / Kontrak Perkuliahan Dosen** (`materials/syllabus/`) — *Otoritas cakupan tertinggi*.
2. **Slide Resmi Dosen Pengampu** (`materials/slides/`) — *Acuan utama definisi & rumus yang diajarkan*.
3. **Handout Resmi & Publikasi Metodologi BPS** (`materials/notes/`) — *Acuan data teknis dan konsep institusional*.
4. **Soal Ujian Tahun Lalu** (`materials/past-exams/`) — *Acuan gaya penulisan soal dan tipe pertanyaan*.
5. **Catatan Pribadi Mahasiswa** — *Acuan penjelasan tambahan*.
6. **Catatan / Rangkuman Senior** — *Acuan sekunder (perlu verifikasi ulang)*.
7. **Suplemen Luar / Web** (`suplemen/`) — *Hanya pelengkap berlabel khusus; tidak boleh menggantikan sumber resmi*.

---

## 4. Aturan Wajib Grounding & Sitasi

1. **Format Sitasi Ketat**:
   Setiap definisi, rumus, interpretasi data, fakta statistik, dan kunci jawaban **wajib mencantumkan sumber sitasi spesifik**:
   `[nama-file, slide/hal. N]` (Contoh: `[Pertemuan 8 OSL Indikator Sosial (1)...pptx, slide 14]`).
2. **Larangan Mengarang (Zero Hallucination)**:
   Jika suatu informasi atau jawaban tidak termuat dalam berkas materi resmi, tulis secara eksplisit:
   `"TIDAK ADA DI MATERI"`. Jangan berasumsi atau membuat-buat data.
3. **Isolasi Pengetahuan Luar**:
   Pengetahuan dari luar slide kuliah hanya boleh digunakan sebagai suplemen penjelas, wajib diberi label `[SUPLEMEN]`, dan diletakkan terpisah dari penjelasan materi utama.
4. **Verifikasi Hitungan dengan Kode**:
   Semua angka, formula matematis (misal IHK Laspeyres modifikasi, koefisien Gini, formula FGT kemiskinan, NTP, TPK), dan hasil kalkulasi numerik **wajib dihitung ulang secara programatik (eksekusi kode Python)**, bukan dihitung secara manual atau ditebak.

---

## 5. Aturan Indeks & Penggunaan Konteks (Poin 8)

- **Cari di Indeks Terlebih Dahulu**:
  Jangan memuat seluruh isi berkas materi secara masif ke dalam prompt/konteks.
- Gunakan `scripts/build_index.py --search "<kata-kunci>"` atau baca berkas `index/materi.json` untuk menemukan slide/halaman yang relevan.
- Setelah menemukan lokasinya, baca **hanya potongan bab/slide yang bersangkutan** dari direktori `extracted/`.

---

## 6. Aturan Pelacakan Kemajuan & Repetisi Berjarak (Poin 7)

- Sebelum memulai sesi latihan soal:
  1. Baca `progress/tracker.json`.
  2. Prioritaskan butir soal dari topik-topik lemah (`topik_lemah: true` pada `ringkasan_topik`) dan butir soal yang telah jatuh tempo (`status: "perlu_latihan"`, dengan `tahap_interval` 0-3 memetakan interval *Spaced Repetition* 1, 3, 7, 14 hari).
- Setelah sesi latihan:
  1. Perbarui riwayat jawaban benar/salah pada `progress/tracker.json`.
  2. Catat butir yang salah ke dalam `progress/kesalahan.md` lengkap dengan analisis jenis kesalahan (konsep / rumus / ketelitian / hafalan) dan tindakan remedial.

---

## 7. Titik Kendali Manusia (Human-in-the-Loop)

Agen **TIDAK BOLEH** melangkahi titik kendali berikut tanpa persetujuan eksplisit dari pengguna:

1. **Konfirmasi Cakupan Silabus & Indeks**:
   Setelah ekstraksi dan pembuatan `index/materi.json` selesai, sajikan ringkasan cakupan bab/topik kepada pengguna dan **minta konfirmasi** sebelum membuat modul materi massal.
2. **Konfirmasi Sampel Bank Soal**:
   Sebelum membuat seluruh bank soal, buat terlebih dahulu **sampel 5–10 soal representatif**, jalankan validasi, dan mintakan persetujuan pengguna.
3. **Pemberhentian Saat Validasi / Review Gagal**:
   Jika validator (`scripts/validate_bank.py`) atau subagen `reviewer` mendeteksi status `GAGAL`, perbaiki masalah tersebut terlebih dahulu hingga tuntas (`LULUS`). Jangan melanjutkan ke pembuatan paket belajar sebelum status hijau.

---

## 8. Pengaman Tambahan (Safeguards)

1. **Folder `suplemen/`**:
   Semua data sekunder, rangkuman web, atau literatur eksternal harus disimpan di direktori `suplemen/` dan tidak boleh dicampurkan ke direktori materi primer.
2. **Disclaimer Prediksi Ujian**:
   Setiap analisis pola soal, proyeksi materi ujian, atau prediksi probabilitas keluarnya topik wajib mencantumkan tingkat keyakinan (`tinggi` / `sedang` / `rendah`) dan pernyataan penafian wajib:
   > *"Catatan Penting: Prediksi ini merupakan pembobotan prioritas waktu belajar berbasis frekuensi materi historis, bukan jaminan soal resmi. Seluruh materi dalam silabus RPS tetap wajib dipelajari secara menyeluruh."*
3. **Inspeksi Sampel Manual**:
   Gunakan `python scripts/sample_check.py` untuk menginspeksi 10 butir soal acak (terutama soal hitungan dan formula) sebelum dipakai dalam simulasi ujian.

---

## 9. Integrasi 9 Skills Spesialis (.agents/skills/)

Untuk memaksimalkan efektivitas dan kualitas persiapan ujian, sistem mengintegrasikan 9 skills spesialis:

| No | Skill | Sumber | Fungsi Utama & Kapan Digunakan | Tahap Terintegrasi |
|---|---|---|---|---|
| 1 | **`study-assistant`** | [GitHub Repo](https://github.com/2362094903-ops/study-assistant-skills) | **Orchestrator Utama**: Mengatur kurikulum belajar per bab, melacak progres belajar lintas sesi (*session state*), dan mengelola alur belajar terstruktur. | Pengatur alur utama (Langkah 2, 3, 4, 8, 9) |
| 2 | **`study-teach`** | *Study Assistant Suite* | Menghasilkan modul ajar/catatan kuliah per poin konsep dengan penjelasan mendalam, penurunan rumus LaTeX, tabel, dan contoh soal teruji. | Langkah 4 (Pembuatan Materi Belajar) |
| 3 | **`study-quiz`** | *Study Assistant Suite* | Generator kuis interaktif HTML MathJax dengan koreksi instan, bank soal global, dan buku catatan evaluasi salah (*mistake book*). | Langkah 6 (Bank Soal) & Langkah 8 (Latihan Kuis) |
| 4 | **`study-mindmap`** | *Study Assistant Suite* | Membuat visualisasi peta konsep (mind map) interaktif berbasis HTML mandiri dengan pewarnaan berdasarkan tingkat penguasaan materi. | Langkah 3 (Pemetaan Konsep) & Langkah 4 |
| 5 | **`study-feynman`** | *Study Assistant Suite* | Penguji pemahaman berbasis Teknik Feynman — AI bertindak sebagai pemula kritis yang menguji apakah Anda benar-benar paham suatu konsep tanpa menghafal. | Langkah 8 (Uji Pemahaman Mendalam / Sign-off) |
| 6 | **`study-img`** | *Study Assistant Suite* | Ekstraksi visual, OCR soal, transkripsi tulisan tangan, dan interpretasi diagram/grafik dari foto lembar ujian atau slide kuliah. | Langkah 1 (Ekstraksi & OCR Visual) |
| 7 | **`exam-forecast`** | [Anthropic MCP](https://mcpservers.org/agent-skills/anthropic/exam-forecast) | Analisis longitudinal soal UAS tahun-tahun sebelumnya untuk mendeteksi bobot materi, tipe soal favorit dosen, pola jebakan, dan memproyeksikan struktur soal UAS mendatang. | Langkah 5 (Analisis Pola & Backtest) |
| 8 | **`exam-question-predictor`** | [FindSkill.ai](https://findskill.ai/skills/education-learning/exam-question-predictor/) | Prediktor soal berbasis *Bloom's Taxonomy* & sinyal perkuliahan dosen untuk menyusun *Study Priority Matrix* (Must Study, Should Study, Quick Review, Skip). | Langkah 3 (Pemetaan Prioritas) & Langkah 5 |
| 9 | **`exam-sprint-builder`** | [GitHub Repo](https://github.com/dentar142/exam-sprint-builder) | Membuat paket belajar kilat *offline-first* (buka langsung via browser tanpa server): aplikasi kuis HTML instan, *one-page cheat sheet* A4, Obsidian study vault, dan simulasi UAS. | Langkah 8 (Paket Sprint UAS Final) |

### Protokol Operasional Skills:
1. **Fidelity Sumber**: Tidak ada materi atau soal yang dihasilkan di luar korpus resmi tanpa label `[SUPLEMEN]`.
2. **Offline-First Delivery**: Seluruh artefak visual, modul HTML, kuis, dan mind map yang dibuat oleh `exam-sprint-builder`, `study-quiz`, dan `study-mindmap` wajib bersifat mandiri (*zero-dependency*, dapat dibuka langsung melalui protokol `file://` tanpa server lokal).
3. **Sinkronisasi Status**: Perubahan penguasaan materi dari kuis (`study-quiz`) atau uji Feynman (`study-feynman`) wajib disinkronkan ke `progress/tracker.json` dan `progress/kesalahan.md`.
