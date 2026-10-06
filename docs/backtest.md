# Metodologi & Prosedur Backtest Prediksi Ujian

Dokumen ini mendefinisikan prosedur formal untuk memvalidasi akurasi model peramalan/prediksi soal ujian (*exam forecast backtesting*) pada mata kuliah **Official Statistics Lanjutan (OSL)**.

---

## 1. Prinsip Dasar Backtesting (Hold-out Validation)

Tujuan backtesting adalah membuktikan secara empiris apakah metode prediksi topik berbasis tren historis benar-benar mampu memproyeksikan komposisi soal pada ujian yang belum pernah dilihat sebelumnya (*unseen exam*).

### Alur Prosedur Baku:
1. **Pemisahan Data (*Hold-out Split*)**:
   - Berkas soal ujian tahun terakhir (misal $T_n$) disembunyikan (*held out*) dari korpus analisis.
   - Hanya soal ujian dari tahun-tahun sebelumnya ($T_1, T_2, \dots, T_{n-1}$) yang digunakan sebagai masukan model prediksi pola (*training set*).
2. **Generasi Prediksi Tanpa Bocoran**:
   - Model peramalan (berbasis frekuensi Sub-CPMK, bobot jam kuliah, dan kemunculan tipe soal) menghasilkan:
     - Daftar *Top-K* topik prioritas tinggi.
     - Estimasi proporsi tipe soal (Pilihan Ganda, Esai, Hitungan).
     - Estimasi persentase bobot per bab.
3. **Komparasi dengan Ujian yang Disembunyikan**:
   - Hasil prediksi dicocokkan dengan soal ujian tahun $T_n$ yang di-hold-out.
4. **Metrik Evaluasi**:
   - **Top-3 & Top-5 Topic Hit Rate**: Berapa persentase topik prioritas yang benar-benar keluar di ujian hold-out.
   - **Akurasi Tipe Soal**: Kesesuaian distribusi tipe soal (selisih rasio PG vs Esai).
   - **Weight Divergence (Mean Absolute Error / MAE)**: Rata-rata deviasi absolut antara bobot prediksi topik dan bobot riil soal.

---

## 2. Status Dataset Saat Ini & Aturan Khusus (< 2 Tahun)

### Kondisi Korpus Eksisting:
Di dalam repositori, naskah soal yang tersedia secara definitif adalah:
1. `materials/past-exams/soal_latihan_uas.md`: Kumpulan 50 butir soal latihan resmi persiapan UAS dari dosen pengampu (Tiodora Hadumaon Siagian).
2. `extracted/Soal_UAS_2022-2023.md` (sumber: `materials/past-exams/Soal UAS 2022-2023.pdf`): Naskah 42 butir soal ujian resmi UAS 2022/2023 (40 Pilihan Ganda dan 2 Esai).

### Aturan Metodologi Wajib:
> **"Jika soal tahun lalu kurang dari dua tahun ujian resmi tahunan, backtest longitudinal multi-tahun TIDAK BISA dijalankan secara valid, dan estimasi utama wajib didasarkan secara penuh pada Silabus/RPS serta distribusi materi pertemuan slide."**

Karena jumlah naskah ujian historis tahunan bernilai $N = 1$ (< 2), backtesting longitudinal hold-out tahun-ke-tahun belum memenuhi syarat statistik untuk dijalankan.

### Pendekatan Komprehensif yang Diterapkan:
1. **Mode Proyeksi Utama (Baseline Silabus & SAP)**:
   Estimasi alokasi waktu belajar didasarkan pada bobot pertemuan setara pada RPS/Kontrak Kuliah Dosen (`Tiodora_3SI1_Kontrak Perkuliahan OSL Genap TA 2025 2026 Politeknik Statistika STIS.pptx`) dan sebaran slide Pertemuan 8 s.d. 13:
   - **Pertemuan 8**: Indikator Kemiskinan Makro, Mikro, dan Ketimpangan (~16,7%)
   - **Pertemuan 9**: Indikator Ketenagakerjaan (ICLS 13/19) dan Pendidikan (~16,7%)
   - **Pertemuan 10**: Indikator Kesehatan & SDGs Tujuan 3 (~16,7%)
   - **Pertemuan 11**: Indikator Ekonomi (1) - Statistik Produksi & NTP (~16,7%)
   - **Pertemuan 12**: Indikator Ekonomi (2) - Perdagangan, Harga, IHK & Inflasi (~16,7%)
   - **Pertemuan 13**: Indikator Ekonomi (3) - Ekspor-Impor, Merchanting & Pariwisata (~16,7%)
2. **Evaluasi Silang Empiris (Soal Latihan Dosen vs UAS Riil)**:
   Skrip `scripts/backtest.py` secara otomatis mengevaluasi keselarasan topik antara soal latihan dosen dan naskah UAS riil (menghasilkan Top-5 Hit Rate 80.0% dan MAE 8.73%), yang dilaporkan secara detail di `docs/laporan_backtest.md`.

---

## 3. Prosedur Aktivasi Backtest Setelah Penambahan Soal

Segera setelah pengguna menambahkan berkas ujian tahun kedua (misalnya `materials/past-exams/Soal UAS 2023-2024.pdf`), jalankan:
```bash
uv run python scripts/backtest.py
```
Skrip akan secara otomatis:
1. Mengidentifikasi naskah tertua (2022-2023) sebagai bahan latih dan naskah terbaru (2023-2024) sebagai hold-out set.
2. Mengekstrak dan memetakan frekuensi topik.
3. Mencetak tabel evaluasi akurasi metrik ke terminal dan menyimpan laporannya ke `docs/laporan_backtest.md`.
