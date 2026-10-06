# Instruksi & Konteks Agen (Official Statistics Lanjutan)

Dokumen ini ditujukan untuk seluruh agen otomasi dan asisten AI pada repositori persiapan ujian **Official Statistics Lanjutan (OSL)**. Berkas ini memiliki spesifikasi teknis dan aturan yang selaras dengan [CLAUDE.md](file:///home/alfzki/Documents/OSL/CLAUDE.md).

---

## 1. Parameter Utama Proyek

- **Mata Kuliah**: Official Statistics Lanjutan (OSL)
- **Dosen Pengampu**: Tiodora Hadumaon Siagian
- **Jadwal Ujian**: Ujian Tertulis, 30 September 2026 (Durasi 120 Menit, Pilihan Ganda & Esai)
- **Bahasa Keluaran**: Bahasa Indonesia Baku (terminologi standar statistik BPS dipertahankan)
- **Materi Sumber**:
  - `materials/slides/`: Pertemuan 8 s.d. 13 (Kemiskinan, Ketenagakerjaan, Kesehatan, Produksi, Perdagangan & Harga, Pariwisata & Ekspor-Impor).
  - `materials/notes/`: Kuesioner Sakernas, Publikasi IHK BPS 2025.
  - `materials/past-exams/`: Soal UAS 2022-2023, Soal Latihan UAS.
  - `materials/syllabus/`: Kontrak Perkuliahan & RPS OSL Genap TA 2025/2026.
  - `suplemen/`: Materi eksternal terpisah.

---

## 2. Rantai Otoritas Sumber (Source Hierarchy)

Setiap klaim materi harus mematuhi hierarki otoritas berikut:
`Silabus / RPS > Slide Dosen > Handout Resmi BPS > Soal Tahun Lalu > Catatan Pribadi > Catatan Senior > Suplemen Luar`

---

## 3. Protokol Grounding & Kredibilitas

1. **Sitasi Presisi**: Wajib menyertakan label rujukan dalam format:
   `[nama-file, slide/hal. N]`
2. **Ketiadaan Data**: Apabila konsep tidak dibahas dalam materi kuliah, agen wajib menuliskan:
   `TIDAK ADA DI MATERI` (tanpa membuat asumsi atau berhalusinasi).
3. **Pelabelan Suplemen**: Konsep yang diambil dari luar materi wajib didahului tanda:
   `[SUPLEMEN]`
4. **Validasi Numerik**: Hitungan formula statistik (kemiskinan FGT, Gini, IHK Laspeyres modifikasi, NTP, TPK) wajib diverifikasi melalui eksekusi skrip kode Python.

---

## 4. Integrasi 9 Skills Spesialis (.agents/skills/)

Agen wajib memanfaatkan 9 skills terpasang pada direktori `.agents/skills/` sesuai peran dan tahapannya:

| Skill | Sumber | Fungsi Utama & Kapan Digunakan | Integrasi Alur Kerja |
|---|---|---|---|
| **`study-assistant`** | [GitHub Repo](https://github.com/2362094903-ops/study-assistant-skills) | **Orchestrator Utama**: Mengatur kurikulum belajar per bab, melacak progres belajar lintas sesi (*session state*), dan mengelola alur belajar terstruktur. | Pengatur alur utama (Langkah 2, 3, 4, 8, 9) |
| **`study-teach`** | *Study Assistant Suite* | Menghasilkan modul ajar/catatan kuliah per poin konsep dengan penjelasan mendalam, penurunan rumus LaTeX, tabel, dan contoh soal teruji. | Langkah 4 (Pembuatan Modul Belajar) |
| **`study-quiz`** | *Study Assistant Suite* | Generator kuis interaktif HTML MathJax dengan koreksi instan, bank soal global, dan buku catatan evaluasi salah (*mistake book*). | Langkah 6 (Bank Soal) & Langkah 8 (Kuis Interaktif) |
| **`study-mindmap`** | *Study Assistant Suite* | Membuat visualisasi peta konsep (mind map) interaktif berbasis HTML mandiri dengan pewarnaan berdasarkan tingkat penguasaan materi. | Langkah 3 & 4 (Pemetaan & Visualisasi Konsep) |
| **`study-feynman`** | *Study Assistant Suite* | Penguji pemahaman berbasis Teknik Feynman — AI bertindak sebagai pemula kritis yang menguji apakah Anda benar-benar paham suatu konsep tanpa menghafal. | Langkah 8 (Uji Pemahaman Mendalam / Sign-off) |
| **`study-img`** | *Study Assistant Suite* | Ekstraksi visual, OCR soal, transkripsi tulisan tangan, dan interpretasi diagram/grafik dari foto lembar ujian atau slide kuliah. | Langkah 1 (Ekstraksi & Audit Visual) |
| **`exam-forecast`** | [Anthropic MCP](https://mcpservers.org/agent-skills/anthropic/exam-forecast) | Analisis longitudinal soal UAS tahun-tahun sebelumnya untuk mendeteksi bobot materi, tipe soal favorit dosen, pola jebakan, dan memproyeksikan struktur soal UAS mendatang. | Langkah 5 (Analisis Pola & Backtest Prediksi) |
| **`exam-question-predictor`** | [FindSkill.ai](https://findskill.ai/skills/education-learning/exam-question-predictor/) | Prediktor soal berbasis *Bloom's Taxonomy* & sinyal perkuliahan dosen untuk menyusun *Study Priority Matrix* (Must Study, Should Study, Quick Review, Skip). | Langkah 3 (Pemetaan Prioritas) & Langkah 5 |
| **`exam-sprint-builder`** | [GitHub Repo](https://github.com/dentar142/exam-sprint-builder) | Membuat paket belajar kilat *offline-first* (buka langsung via browser tanpa server): aplikasi kuis HTML instan, *one-page cheat sheet* A4, Obsidian study vault, dan simulasi UAS. | Langkah 8 (Paket Sprint UAS Final) |

---

## 5. Alur Kerja & Titik Kendali Manusia

1. **Ekstraksi & Audit Visual (Langkah 1)**:
   - Gunakan `study-img` untuk OCR dan interpretasi diagram visual pada slide/naskah soal.
   - Jalankan `uv run python scripts/extract.py`. Periksa berkas `extracted/_laporan.md`.
2. **Pengindeksan & Pemetaan Kurikulum (Langkah 2)**:
   - Jalankan `uv run python scripts/build_index.py`. Cari bagian yang relevan sebelum membaca materi penuh.
   - `study-assistant` mengorganisasi hierarki konsep dan modul per pertemuan.
3. **Konfirmasi Cakupan & Prioritas (Titik Konfirmasi 1 - Langkah 3)**:
   - Gunakan `exam-question-predictor` untuk menyusun *Study Priority Matrix* (Must Study, Should Study, Quick Review, Skip).
   - Gunakan `study-mindmap` untuk merender peta konsep materi pasca-UTS.
   - Tampilkan ringkasan cakupan materi dan matriks prioritas kepada pengguna sebelum memproduksi bahan ajar.
4. **Pembuatan Modul Materi Belajar (Langkah 4)**:
   - Gunakan `study-teach` untuk menghasilkan catatan ajar per poin materi secara bertahap (*intuisi -> kondisi -> penurunan rumus rigor -> aplikasi ujian*).
   - Pastikan grounding ketat `[nama-file, slide/hal. N]` dan tandai suplemen dengan `[SUPLEMEN]`.
5. **Analisis Pola & Prediksi Ujian (Langkah 5)**:
   - Gunakan `exam-forecast` dan `scripts/backtest.py` untuk mengevaluasi data historis ujian dan memetakan pola soal serta jebakan dosen.
6. **Penyusunan Bank Soal (Titik Konfirmasi 2 - Langkah 6)**:
   - Gunakan `study-quiz` untuk menyusun butir soal berformat MathJax terstandar.
   - Buat sampel 5–10 soal terlebih dahulu dan minta persetujuan pengguna.
   - Semua soal harus divalidasi dengan `uv run python scripts/validate_bank.py` dan `scripts/sample_check.py`.
7. **Review Butir Soal (Langkah 7)**:
   - Lakukan peninjauan butir soal dengan subagen reviewer (`.claude/agents/reviewer.md`) dalam konteks terisolasi hingga status `LULUS`.
8. **Simulasi, Uji Feynman & Sprint UAS (Langkah 8)**:
   - Gunakan `study-quiz` untuk latihan interaktif HTML.
   - Gunakan `study-feynman` untuk menguji pemahaman konsep mahasiswa tanpa hafalan.
   - Gunakan `exam-sprint-builder` untuk menghasilkan paket belajar kilat *offline-first* (*cheat sheet* A4 rumus resmi, aplikasi kuis mandiri, dan simulasi UAS).
9. **Pelacakan & Remediasi (Langkah 9)**:
   - `study-assistant` menyinkronkan status penguasaan materi (*mastery 0-5*).
   - Baca `progress/tracker.json` sebelum latihan untuk memprioritaskan topik berakurasi rendah dan jadwal *spaced repetition*.
   - Perbarui data pelacakan dan catat kesalahan pada `progress/kesalahan.md`.
