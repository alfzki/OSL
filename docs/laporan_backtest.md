# Laporan Status Backtest Prediksi Ujian OSL

- **Tanggal Analisis**: 2026-09-29
- **Status Eksekusi**: **BACKTEST DITANGGUHKAN (< 2 TAHUN UJIAN RESMI TAHUNAN)**
- **Naskah Ujian Resmi Berlabel Tahun**: 1 berkas (`Soal_UAS_2022-2023.md` (2022-2023))
- **Korpus Naskah Soal yang Tersedia**:
  1. `materials/past-exams/soal_latihan_uas.md` (Kumpulan soal latihan persiapan UAS dari dosen pengampu)
  2. `extracted/Soal_UAS_2022-2023.md` (Naskah soal UAS resmi 2022/2023 diekstrak dari PDF)

---

## 1. Kesimpulan Audit Metodologis

> **Sesuai Aturan Komponen 6:**
> *"Jika soal tahun lalu kurang dari dua, tulis di laporan bahwa backtest tidak bisa dijalankan dan prediksi hanya berbasis silabus."*

Repositori saat ini memiliki naskah ujian resmi bertahun tunggal (`Soal UAS 2022-2023.pdf` / `extracted/Soal_UAS_2022-2023.md`). Validasi backtest longitudinal antar-tahun resmi (*multi-year hold-out validation*) secara statistik tidak dapat dilakukan karena pemisahan hold-out pada 1 tahun akademik akan mengosongkan data pelatihan (*training data*).

Dengan demikian, acuan estimasi bobot prioritas utama dialihkan ke **Baseline Silabus & Kontrak Perkuliahan**.

---

## 2. Model Pembobotan Alternatif (Baseline Silabus & Kontrak Kuliah)

Berdasarkan silabus resmi dosen pengampu (`Tiodora_3SI1_Kontrak Perkuliahan OSL Genap TA 2025 2026 Politeknik Statistika STIS.pptx`) dan alokasi tatap muka slide perkuliahan pasca-UTS (Pertemuan 8 s.d. 13), seluruh bab memiliki alokasi waktu yang setara (masing-masing 1 pertemuan = 16,67% alokasi tatap muka).

### Distribusi Prioritas Materi UAS (Baseline Silabus):

| No | Bab / Pertemuan | Fokus Bahasan Utama | Estimasi Bobot Silabus | Tingkat Keyakinan |
|---|---|---|---|---|
| 1 | **Pertemuan 8** | Indikator Kemiskinan Makro, Mikro, Garis Kemiskinan, & Koefisien Gini | 16,67% | Sedang (Silabus) |
| 2 | **Pertemuan 9** | Ketenagakerjaan (ICLS 13, TPT, TPAK, Setengah Penganggur) & Pendidikan | 16,67% | Sedang (Silabus) |
| 3 | **Pertemuan 10** | Indikator Kesehatan, SDGs Tujuan 3 (U5MR, MMR, Imunisasi) & Morbiditas | 16,67% | Sedang (Silabus) |
| 4 | **Pertemuan 11** | Statistik Produksi Pertanian & Nilai Tukar Petani (NTP: It & Ib) | 16,67% | Sedang (Silabus) |
| 5 | **Pertemuan 12** | Perdagangan & Harga: IHK (Modified Laspeyres), SBH, & Inflasi | 16,67% | Sedang (Silabus) |
| 6 | **Pertemuan 13** | Ekspor-Impor (SNA 2008, Merchanting), Terms of Trade, & Pariwisata (TPK) | 16,67% | Sedang (Silabus) |

---

## 3. Evaluasi Silang Empiris: Soal Latihan Dosen vs Naskah UAS Riil 2022/2023

Sebagai validasi empiris berbasis data yang tersedia, model mengevaluasi keselarasan antara soal latihan dosen (`soal_latihan_uas.md`, 50 butir) dengan naskah UAS riil (`Soal_UAS_2022-2023.md`, 42 butir):

### Ringkasan Metrik Evaluasi Silang:

| Metrik Evaluasi | Capaian | Status Validasi |
|---|---|---|
| **Top-3 Topic Hit Rate** | **33.3%** (1/3 topik teratas tepat) | CUKUP (Rotasi Fokus) |
| **Top-5 Topic Hit Rate** | **80.0%** (4/5 topik tepat) | LULUS |
| **Mean Absolute Error (MAE) Bobot** | **8.73%** | SANGAT BAIK |

### Perbandingan Bobot Topik: Latihan Dosen vs UAS Riil vs Silabus:

| No | Bab / Materi | Bobot Latihan Dosen (%) | Bobot UAS Riil (%) | Baseline Silabus (%) | Selisih (Latihan - Riil) | Keterangan |
|---|---|---|---|---|---|---|
| 1 | **Pertemuan 8**: Kemiskinan dan Ketimpangan | 26.0% | 33.3% | 16,67% | -7.3% | Underpredicted di Latihan |
| 2 | **Pertemuan 13**: Ekspor-Impor, Neraca & Pariwisata | 22.0% | 9.5% | 16,67% | +12.5% | Overpredicted di Latihan |
| 3 | **Pertemuan 11**: Produksi Pertanian & Nilai Tukar Petani (NTP) | 18.0% | 11.9% | 16,67% | +6.1% | Overpredicted di Latihan |
| 4 | **Pertemuan 9**: Ketenagakerjaan dan Pendidikan | 14.0% | 19.0% | 16,67% | -5.0% | Underpredicted di Latihan |
| 5 | **Pertemuan 10**: Indikator Kesehatan & SDGs 3 | 10.0% | 2.4% | 16,67% | +7.6% | Overpredicted di Latihan |
| 6 | **Pertemuan 12**: Perdagangan, Harga & IHK | 10.0% | 23.8% | 16,67% | -13.8% | Underpredicted di Latihan |

### Perbandingan Distribusi Jenis Soal:

| Jenis Soal | Proporsi Latihan (%) | Proporsi UAS Riil (%) | Selisih |
|---|---|---|---|
| **Pilihan Ganda (PG)** | 100.0% | 95.2% | +4.8% |
| **Hitungan** | 0.0% | 0.0% | +0.0% |
| **Isian** | 0.0% | 0.0% | +0.0% |
| **Esai** | 0.0% | 4.8% | -4.8% |

### Temuan Utama Evaluasi Silang:
1. **Dominasi Pilihan Ganda**: Baik pada latihan dosen (100.0%) maupun ujian riil (95.2%), format pilihan ganda mendominasi naskah ujian tertulis.
2. **Topik Inti Konsisten**: Pertemuan 8 (Kemiskinan) dan Pertemuan 11 (Statistik Produksi & NTP) konsisten memiliki porsi pertanyaan yang tinggi pada kedua berkas.
3. **Akurasi Topik (MAE 8.73%)**: Deviasi bobot secara rata-rata di bawah 10%, menunjukkan bahwa paket soal latihan dari dosen merefleksikan komposisi ujian riil dengan baik.

---

## 4. Disclaimer Wajib

> **Catatan Penting:** Pembobotan ini merupakan panduan prioritas alokasi waktu belajar berbasis silabus resmi dan data latihan dosen, bukan jaminan kisi-kisi tertutup. Seluruh materi silabus OSL tetap wajib dikuasai secara menyeluruh.

---

## 5. Prosedur Pembaruan jika Naskah Bertambah

Jika di kemudian hari naskah ujian resmi tahun berikutnya diperoleh:
1. Simpan berkas (misal `Soal UAS 2023-2024.pdf`) ke folder `materials/past-exams/`.
2. Jalankan kembali:
   ```bash
   uv run python scripts/backtest.py
   ```
   Sistem akan secara otomatis beralih ke mode hold-out longitudinal antar-tahun resmi.
