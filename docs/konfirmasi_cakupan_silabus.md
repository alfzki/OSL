# Dokumen Konfirmasi Cakupan Silabus & Pemetaan Prioritas Materi UAS (Langkah 3)

**Mata Kuliah**: Official Statistics Lanjutan (OSL) — Kode MK: K200207  
**Dosen Pengampu**: Tiodora Hadumaon Siagian  
**Jadwal Ujian**: Ujian Tertulis UAS, 30 September 2026 (Durasi: 120 Menit, PG & Esai)  
**Status Dokumen**: Menunggu Konfirmasi Pengguna (*Human-in-the-Loop Checkpoint #1*)  
**Tanggal Penyusunan**: 2026-09-29  

---

## 1. Ringkasan Eksekutif & Tujuan Dokumen

Sesuai dengan protokol alur kerja persiapan ujian OSL (Komponen 3 dan Langkah 3 pada `README.md`, `CLAUDE.md`, dan `AGENTS.md`), agen dilarang memproduksi materi modul belajar secara massal sebelum menyajikan audit cakupan silabus dan pemetaan prioritas materi kepada pengguna untuk diverifikasi dan disetujui.

Dokumen ini memadukan 4 sumber otoritatif:
1. **Silabus / Kontrak Perkuliahan**: `materials/syllabus/Tiodora_3SI1_Kontrak Perkuliahan OSL Genap TA 2025 2026 Politeknik Statistika STIS.pptx` (Pertemuan 8 s.d. 13 pasca-UTS).
2. **Slide Kuliah Dosen Pengampu**: 6 berkas slide/handout lengkap Pertemuan 8 s.d. 13 pada `materials/slides/`.
3. **Dokumen Teknis & Publikasi Resmi BPS**: Kuesioner Sakernas Agustus 2025 (`materials/notes/Kuesioner SAK.AGS25-AK.pdf`) dan Publikasi Indeks Harga Konsumen 2025 (`materials/notes/indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.pdf`).
4. **Data Ujian Historis**: 50 butir naskah soal latihan dosen (`materials/past-exams/soal_latihan_uas.md`) dan 42 butir naskah soal resmi UAS 2022/2023 (`extracted/Soal_UAS_2022-2023.md`).

---

## 2. Inventarisasi & Pemetaan Detail Cakupan Silabus Pasca-UTS (Pertemuan 8 s.d. 13)

Berikut adalah pemetaan rinci bab materi, segmen slide, definisi operasional BPS, serta formula matematis terverifikasi:

### Pertemuan 8: Indikator Sosial (1) — Kemiskinan dan Ketimpangan Pendapatan
- **Berkas Sumber**: `Pertemuan 8 OSL Indikator Sosial (1) Indikator Kemiskinan dan Ketimpangan _ new.pptx` (44 slide)
- **Cakupan Bahasan & Poin Konsep Utama**:
  1. *Konsep & Terminologi Kemiskinan*: Asal kata *pauper* / *pauvreté*, definisi Bank Dunia, kemiskinan makro vs mikro `[slide 4-6]`.
  2. *Kemiskinan Absolut vs Kemiskinan Relatif*: Batas absolut tidak bergeser mengikuti kenaikan pendapatan rata-rata, batas relatif bergerak mengikuti median/rata-rata masyarakat `[slide 7-9]`.
  3. *Kemiskinan Global (SDGs Tujuan 1)*: Pengukuran World Bank dengan garis kemiskinan ekstrim ($1.90 PPP / $2.15 PPP 2017) `[slide 10-13]`.
  4. *Metodologi Garis Kemiskinan BPS (Cost of Basic Needs Approach)*:
     - Garis Kemiskinan Total: $GK = GKM + GKNM$ `[slide 14-15]`.
     - Garis Kemiskinan Makanan ($GKM$): Patokan kecukupan 2.100 kkal per kapita per hari, diwakili 52 komoditi makanan pokok `[slide 15-16]`.
     - Garis Kemiskinan Non-Makanan ($GKNM$): Kebutuhan minimum perumahan, sandang, pendidikan, kesehatan (51 komoditas perkotaan, 47 komoditas perdesaan) `[slide 16]`.
  5. *Indeks Kemiskinan FGT (Foster-Greer-Thorbecke)* `[slide 17-21]`:
     $$P_\alpha = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)^\alpha$$
     - $\alpha = 0 \rightarrow P_0$: *Headcount Index* (Persentase penduduk miskin).
     - $\alpha = 1 \rightarrow P_1$: *Poverty Gap Index* (Kedalaman kemiskinan / rata-rata jarak kesenjangan pengeluaran terhadap GK).
     - $\alpha = 2 \rightarrow P_2$: *Poverty Severity Index* (Keparahan kemiskinan / ketimpangan pengeluaran di antara sesama penduduk miskin).
  6. *Ukuran Ketimpangan Pengeluaran / Pendapatan* `[slide 26-35]`:
     - Kurva Lorenz (persentase kumulatif penduduk vs persentase kumulatif pengeluaran) `[slide 27]`.
     - Koefisien Gini:
       $$G = 1 - \sum_{i=1}^k (X_i - X_{i-1})(Y_i + Y_{i-1})$$
     - Kriteria Ketimpangan Bank Dunia (proporsi pengeluaran 40% penduduk terbawah):
       * $< 12\%$ : Ketimpangan Tinggi
       * $12\% - 17\%$ : Ketimpangan Sedang
       * $> 17\%$ : Ketimpangan Rendah `[slide 34-35]`.

---

### Pertemuan 9: Indikator Sosial (2) — Ketenagakerjaan dan Pendidikan
- **Berkas Sumber**: `Pertemuan 9 Indikator Ketenagakerjaan dan Pendidikan.pptx` (75 slide) & `materials/notes/Kuesioner SAK.AGS25-AK.pdf` (27 hal)
- **Cakupan Bahasan & Poin Konsep Utama**:
  1. *Kerangka Ketenagakerjaan ICLS 13 (International Conference of Labour Statisticians)*:
     - Batas Penduduk Usia Kerja di Indonesia: 15 tahun ke atas `[slide 10-12]`.
     - Pembagian: **Angkatan Kerja** (Bekerja + Pengangguran) dan **Bukan Angkatan Kerja** (Sekolah, Mengurus Rumah Tangga, Lainnya/Penerima Pendapatan) `[slide 11-12]`.
  2. *Konsep Operasional Bekerja BPS*: Melakukan kegiatan ekonomi dengan maksud memperoleh atau membantu memperoleh penghasilan/keuntungan, minimal **1 jam berturut-turut** dalam seminggu yang lalu (termasuk pekerja keluarga tidak dibayar / unpaid worker) `[slide 17-18]`.
  3. *Tingkat Partisipasi Angkatan Kerja (TPAK)* `[slide 13-14]`:
     $$\text{TPAK} = \frac{\text{Angkatan Kerja}}{\text{Penduduk Usia Kerja (15+)}} \times 100\%$$
  4. *Tingkat Pengangguran Terbuka (TPT)* `[slide 15-16]`:
     $$\text{TPT} = \frac{\text{Penganggur Terbuka}}{\text{Angkatan Kerja}} \times 100\%$$
     - 4 Kategori Pengangguran Terbuka BPS: (1) Mencari pekerjaan, (2) Mempersiapkan usaha, (3) Merasa tidak mungkin mendapat pekerjaan (*discouraged workers*), (4) Sudah punya pekerjaan/usaha tetapi belum mulai bekerja `[slide 16]`.
  5. *Diferensiasi Bekerja Tidak Penuh (Underemployment)* `[slide 23-27]`:
     - **Setengah Penganggur (Underemployed)**: Bekerja di bawah jam kerja normal (< 35 jam seminggu) **DAN** masih mencari pekerjaan atau bersedia menerima pekerjaan tambahan `[slide 24]`.
     - **Pekerja Paruh Waktu (Part-time Worker)**: Bekerja di bawah 35 jam seminggu tetapi **TIDAK** mencari pekerjaan atau tidak bersedia menerima pekerjaan tambahan `[slide 26]`.
  6. *Indikator Pendidikan* `[slide 45-56]`:
     - Angka Partisipasi Sekolah (APS): Proporsi penduduk kelompok usia sekolah tertentu yang bersekolah di jenjang manapun.
     - Angka Partisipasi Murni (APM): Proporsi siswa usia resmi jenjang tertentu yang terdaftar di jenjang tersebut terhadap penduduk kelompok usia resmi jenjang bersangkutan.
     - Angka Partisipasi Kasar (APK): Jumlah seluruh siswa yang terdaftar di jenjang pendidikan tertentu (tanpa memandang usia) terhadap jumlah penduduk kelompok usia resmi jenjang tersebut (dapat melebihi 100%).

---

### Pertemuan 10: Indikator Sosial (3) — Indikator Kesehatan & SDGs Tujuan 3
- **Berkas Sumber**: `Pertemuan 10 Indikator Kesehatan.pptx` (91 slide)
- **Cakupan Bahasan & Poin Konsep Utama**:
  1. *Konsep & Definisi Kesehatan WHO*: Keadaan sehat utuh secara fisik, mental, dan sosial, bukan hanya bebas dari penyakit atau kecacatan `[slide 4-7]`.
  2. *SDGs Tujuan 3 (Kehidupan Sehat dan Sejahtera)*: Target 3.1 (penurunan kematian ibu), Target 3.2 (penghentian kematian neonatal dan balita yang dapat dicegah), Target 3.4 (pencegahan penyakit tidak menular) `[slide 9-11]`.
  3. *Indikator Mortalitas Ibu dan Anak*:
     - **Angka Kematian Ibu (AKI / MMR)**:
       $$\text{AKI} = \frac{\sum \text{Kematian Ibu karena Hamil/Persalinan/Nifas}}{\sum \text{Kelahiran Hidup}} \times 100.000 \text{ KH} \quad \text{[slide 13]}$$
     - **Angka Kematian Balita (AKABA / U5MR)**: Kematian anak sebelum mencapai usia tepat 5 tahun (0-4 tahun) per 1.000 kelahiran hidup `[slide 18-20]`.
     - **Angka Kematian Bayi (AKB / IMR)**: Kematian bayi sebelum mencapai umur 1 tahun (0-11 bulan) per 1.000 kelahiran hidup `[slide 21-23]`.
     - **Angka Kematian Neo-Natal (NMR)**: Kematian bayi yang terjadi dalam 28 hari pertama kehidupannya per 1.000 kelahiran hidup `[slide 24-25]`.
  4. *Morbiditas (Angka Kesakitan)*: Persentase penduduk yang mengalami keluhan kesehatan yang mengakibatkan terganggunya kegiatan sehari-hari (pekerjaan, sekolah, aktivitas rumah tangga) dalam kurun waktu 1 bulan terakhir `[slide 30-38]`.
  5. *Imunisasi Dasar Lengkap (IDL)*: HB-0 (0-7 hari), BCG (1 dosis), DPT-HB-Hib (3 dosis), Polio (4 dosis tetes / 1 dosis suntik), dan Campak/MR (1 dosis) sebelum bayi berusia 1 tahun `[slide 40-48]`.

---

### Pertemuan 11: Indikator Ekonomi (1) — Statistik Produksi Pertanian & Industri
- **Berkas Sumber**: `Pertemuan 11 OSL Indikator Ekonomi (1) Produksi.pdf` (59 halaman)
- **Cakupan Bahasan & Poin Konsep Utama**:
  1. *Klasifikasi Statistik Produksi*: Pertanian (Tanaman Pangan, Hortikultura, Perkebunan, Peternakan, Perikanan, Kehutanan), Pertambangan, Energi, dan Industri Pengolahan `[hal. 7-9]`.
  2. *Metode Estimasi Produksi Padi dan Palawija*:
     $$\text{Produksi} = \text{Luas Panen (Ha)} \times \text{Produktivitas (Ku/Ha)} \quad \text{[hal. 10-11]}$$
  3. *Kerangka Sampel Area (KSA)*:
     - Inovasi BPS bersama BPPT/BRIN dan BIG menggantikan metode lama (laporan SP-Padi kepala cabang dinas) yang memiliki risiko bias *overestimate* `[hal. 12-16]`.
     - Berbasis citra satelit resolusi tinggi dan segmentasi poligon $300\text{ m} \times 300\text{ m}$.
     - Amatan visual 9 subsegmen menggunakan aplikasi berbasis Android pada 7 hari terakhir setiap bulan `[hal. 14-18]`.
     - Fase amatan: Persiapan Lahan, Vegetatif Awal/Akhir, Generatif Awal/Akhir, Panen, Bera, Lahan Bukan Sawah, Puso `[hal. 16-17]`.
  4. *Metode Ubinan*:
     - Plot pengukuran ukuran standar $2,5\text{ m} \times 2,5\text{ m} = 6,25\text{ m}^2$ di petak sawah terpilih menjelang panen `[hal. 13-15]`.
     - Konversi hasil timbangan ubinan ke Produktivitas per Hektar (Kuintal/Ha).
  5. *Survei Konversi Gabah ke Beras (SKGB)*:
     - Konversi Gabah Kering Panen (GKP) ke Gabah Kering Giling (GKG) dan dari GKG ke Beras konsumsi `[hal. 22-26]`.
  6. *Statistik Industri Pengolahan (Manufaktur)*:
     - Industri Besar & Sedang (IBS): Jumlah tenaga kerja $\ge 20$ orang (Survei IBS Tahunan & Bulanan).
     - Industri Mikro & Kecil (IMK): Tenaga kerja 1-19 orang (Survei IMK Triwulanan & Tahunan) `[hal. 35-45]`.

---

### Pertemuan 12: Indikator Ekonomi (2) — Perdagangan Dalam Negeri & Indikator Harga
- **Berkas Sumber**: `Pertemuan 12 OSL Indikator Ekonomi (2) Perdagangan&Harga.pdf` (40 halaman) & `materials/notes/indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.pdf` (196 halaman)
- **Cakupan Bahasan & Poin Konsep Utama**:
  1. *Margin Perdagangan dan Pengangkutan (MPP)*:
     - Persentase kenaikan harga komoditas dari produsen/pintu masuk impor hingga ke tangan konsumen akhir akibat biaya angkut dan marjin keuntungan pedagang perantara `[hal. 4-6]`.
     - Survei Pola Distribusi Perdagangan (Poldis) menelusuri rantai pasok komoditas pangan pokok `[hal. 6-10]`.
  2. *Indeks Harga Konsumen (IHK) & Inflasi*:
     - Rumus Indeks Laspeyres yang Dimodifikasi (*Modified Laspeyres*):
       $$I_t = \frac{\sum_{i=1}^k \frac{P_{ti}}{P_{t-1, i}} \cdot P_{t-1, i} \cdot Q_{0i}}{\sum_{i=1}^k P_{0i} \cdot Q_{0i}} \times 100 = \sum_{i=1}^k \left( \frac{P_{ti}}{P_{t-1, i}} \cdot W_{t-1, i} \right) \quad \text{[hal. 14]}$$
     - Sumber diagram timbang ($W$): Survei Biaya Hidup (SBH 2018 untuk tahun dasar 2018=100; SBH 2022 untuk tahun dasar 2022=100 mencakup 150 kab/kota di 38 provinsi) `[hal. 14, 18-20]`.
  3. *Tiga Jenis Laju Inflasi BPS*:
     - Inflasi Bulanan (*month-to-month / m-to-m*): $\frac{IHK_t - IHK_{t-1}}{IHK_{t-1}} \times 100\%$
     - Inflasi Tahunan (*year-on-year / y-on-y*): $\frac{IHK_{t, y} - IHK_{t, y-1}}{IHK_{t, y-1}} \times 100\%$
     - Inflasi Tahun Kalender (*year-to-date / y-t-d*): $\frac{IHK_{t} - IHK_{\text{Desember tahun sebelumnya}}}{IHK_{\text{Desember tahun sebelumnya}}} \times 100\%$ `[hal. 13]`.
  4. *Disagregasi Inflasi (Komponen Inflasi)*:
     - *Core Inflation* (Inflasi Inti): Komponen persisten akibat tekanan moneter, permintaan-penawaran jangka panjang (tidak termasuk barang bergejolak dan harga diatur).
     - *Volatile Foods* (Inflasi Komponen Bergejolak): Komoditas yang harganya rentan terhadap faktor musiman, cuaca, dan panen (cabai, bawang, telur).
     - *Administered Prices* (Inflasi Harga yang Diatur Pemerintah): Tarif listrik, bensin, tarif angkutan, rokok `[hal. 15-18]`.
  5. *Nilai Tukar Petani (NTP) & NTUP* `[hal. 31-36]`:
     $$\text{NTP} = \frac{I_t \text{ (Indeks Harga yang Diterima Petani)}}{I_b \text{ (Indeks Harga yang Dibayar Petani)}} \times 100$$
     - $I_t$: Penjualan hasil produksi pertanian.
     - $I_b$: Pengeluaran konsumsi rumah tangga + Biaya Produksi dan Penambahan Barang Modal (BPPBM).
     - **Nilai Tukar Usaha Petani (NTUP)**: Mengukur kelayakan murni usaha pertanian tanpa memasukkan konsumsi rumah tangga ($\text{NTUP} = \frac{I_t}{\text{BPPBM}} \times 100$).
     - 5 Subsektor NTP: Tanaman Pangan (NTPR), Hortikultura (NTPH), Perkebunan Rakyat (NTPR-Bun), Peternakan (NTPT), Perikanan (NTNP: Tangkap dan Budidaya).

---

### Pertemuan 13: Indikator Ekonomi (3) — Ekspor-Impor, Perdagangan Internasional, & Pariwisata
- **Berkas Sumber**: `Pertemuan 13 OSL Indikator Ekonomi (3) X-M, KTI, Pariwisata.pdf` (43 halaman)
- **Cakupan Bahasan & Poin Konsep Utama**:
  1. *Konsep Ekspor-Impor Berbasis SNA 2008 & BPM6*: Transaksi barang dan jasa antara penduduk (*resident*) suatu perekonomian dengan bukan penduduk (*non-resident*) yang melibatkan perpindahan kepemilikan ekonomi `[hal. 4-6]`.
  2. *Valuasi Statistik Perdagangan Luar Negeri*:
     - **Ekspor**: Dinilai berdasarkan *Free On Board* (FOB) di pelabuhan muat `[hal. 6]`.
     - **Impor**: Dinilai berdasarkan *Cost, Insurance, and Freight* (CIF) di pelabuhan bongkar (pada neraca perdagangan BPS). Namun pada Neraca Pembayaran / SNA 2008, impor dikonversi ke nilai FOB `[hal. 6-7]`.
     - Dokumen Dasar: Pemberitahuan Ekspor Barang (PEB) dan Pemberitahuan Impor Barang (PIB) dari Ditjen Bea dan Cukai `[hal. 7]`.
  3. *Merchanting Goods*: Pembelian barang oleh residen dari non-residen yang kemudian dijual kembali ke non-residen lain tanpa barang tersebut pernah secara fisik memasuki wilayah pabean domestik (dicatat sebagai ekspor negatif saat dibeli dan ekspor positif saat dijual) `[hal. 5]`.
  4. *Indeks Perdagangan Luar Negeri & Terms of Trade (ToT)*:
     - Indeks Nilai, Indeks Volume, dan Indeks Unit Value `[hal. 8-16]`.
     - **Net Barter Terms of Trade (NBToT)**:
       $$\text{NBToT} = \frac{P_x \text{ (Indeks Harga/Unit Value Ekspor)}}{P_m \text{ (Indeks Harga/Unit Value Impor)}} \times 100 \quad \text{[hal. 10]}$$
     - **Gross Barter Terms of Trade (GBToT)**:
       $$\text{GBToT} = \frac{Q_m \text{ (Indeks Kuantitas Impor)}}{Q_x \text{ (Indeks Kuantitas Ekspor)}} \times 100 \quad \text{[hal. 10]}$$
     - **Income Terms of Trade (IToT)**:
       $$\text{IToT} = \text{NBToT} \times \frac{Q_x}{100} = \frac{P_x \cdot Q_x}{P_m} \quad \text{[hal. 11]}$$
  5. *Statistik Pariwisata & Perhotelan* `[hal. 25-40]`:
     - Wisatawan Mancanegara (Wisman): Mengunjungi suatu negara di luar tempat tinggalnya untuk jangka waktu < 1 tahun, bukan untuk bekerja/mencari nafkah dari negara yang dikunjungi `[hal. 26-28]`.
     - Wisatawan Nusantara (Wisnus): Perjalanan dalam negeri minimal 100 km bolak-balik atau menginap `[hal. 29]`.
     - **Tingkat Penghunian Kamar (TPK)**:
       $$\text{TPK} = \frac{\sum \text{Malam Kamar Terjual/Terpakai}}{\sum \text{Malam Kamar Tersedia}} \times 100\% \quad \text{[hal. 34]}$$
     - **Rata-rata Lama Menginap Tamu (RLMT)**:
       $$\text{RLMT} = \frac{\sum \text{Malam Tempat Tidur Dipakai Tamu}}{\sum \text{Tamu yang Datang/Menginap}} \quad \text{[hal. 35]}$$

---

## 3. Prediktor Soal Ujian Strategis (*Exam Question Predictor*) & Matriks Prioritas

Berdasarkan sintesis dari silabus resmi, naskah UAS 2022/2023 (42 butir), dan latihan soal dosen pengampu (50 butir), kami menyusun prediksi soal bertingkat dan matriks prioritas belajar:

### Tahap 1: Kategorisasi Probabilitas & Contoh Soal Prediksi (Stage 1)

#### 🔴 HIGH CONFIDENCE (Probabilitas 85–95% — Wajib Dikuasai)
1. **Topik 1**: Pengukuran Kemiskinan FGT ($P_0, P_1, P_2$) & Koefisien Gini (Pertemuan 8)
   - *Format Prediksi:* Soal Hitungan Terstruktur (Esai / PG Numerik)
   - *Level Kognitif:* Bloom: **Apply & Analyze**
   - *Contoh Soal Prediksi:*
     > *"Suatu wilayah fiktif memiliki Garis Kemiskinan $Z = \text{Rp } 600.000$. Data konsumsi per kapita 5 penduduk miskin adalah Rp 300.000, Rp 400.000, Rp 450.000, Rp 500.000, dan Rp 550.000 dari total 20 penduduk di wilayah tersebut. Hitunglah Headcount Index ($P_0$), Poverty Gap Index ($P_1$), dan Poverty Severity Index ($P_2$), serta interpretasikan perbedaan implikasi kebijakan antara $P_1$ dan $P_2$!"*
   - *Konsep Kunci & Syarat Batas:* Formula $P_\alpha = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)^\alpha$, pembagi $n$ adalah seluruh penduduk (bukan hanya penduduk miskin $q$).
   - *Prioritas Belajar:* **CRITICAL (Must Master)**

2. **Topik 2**: Indeks Harga Konsumen (Modified Laspeyres) & Rasio NTP (Pertemuan 12)
   - *Format Prediksi:* Hitungan Numerik & Pilihan Ganda Konseptual
   - *Level Kognitif:* Bloom: **Apply & Analyze**
   - *Contoh Soal Prediksi:*
     > *"Jika diketahui diagram timbang komoditas beras pada periode $t-1$ adalah 25% dan rasio harga beras periode $t$ terhadap $t-1$ adalah 1,08, hitunglah kontribusi kenaikan harga beras terhadap IHK periode $t$ menggunakan formula Laspeyres yang dimodifikasi. Apakah nilai NTP subsektor Tanaman Pangan sebesar 105,4 menjamin peningkatan kesejahteraan absolut petani?"*
   - *Konsep Kunci & Syarat Batas:* Formula $I_t = \sum (P_{ti}/P_{t-1, i} \times W_{t-1, i})$, NTP adalah rasio daya tukar relatif ($It/Ib \times 100$), bukan pendapatan nominal.
   - *Prioritas Belajar:* **CRITICAL (Must Master)**

#### 🟡 MEDIUM CONFIDENCE (Probabilitas 50–75% — Penting)
3. **Topik 3**: Klasifikasi Ketenagakerjaan ICLS 13 & Diferensiasi Jam Kerja (Pertemuan 9)
   - *Format Prediksi:* Pilihan Ganda Studi Kasus
   - *Level Kognitif:* Bloom: **Understand & Apply**
   - *Contoh Soal Prediksi:*
     > *"Pak Budi bekerja di toko kelontong selama 20 jam dalam seminggu terakhir dan sedang aktif mengirimkan lamaran ke pabrik lain untuk menambah jam kerja. Berdasarkan standar Sakernas BPS, klasifikasi status ketenagakerjaan Pak Budi adalah..."* (Jawaban: Setengah Penganggur, bukan Pekerja Paruh Waktu).
   - *Prioritas Belajar:* **IMPORTANT (Should Study)**

4. **Topik 4**: Metodologi Kerangka Sampel Area (KSA) & Estimasi Produksi Padi (Pertemuan 11)
   - *Format Prediksi:* Pilihan Ganda Identifikasi Metodologi
   - *Level Kognitif:* Bloom: **Remember & Understand**
   - *Contoh Soal Prediksi:*
     > *"Pada pengamatan KSA fase generatif akhir pada subsegmen amatan, berapa rentang waktu estimasi hingga subsegmen tersebut memasuki fase panen? Jelaskan mengapa KSA menggantikan metode laporan SP-Padi!"*
   - *Prioritas Belajar:* **IMPORTANT (Should Study)**

5. **Topik 5**: Valuasi Ekspor-Impor (FOB vs CIF) & Terms of Trade (Pertemuan 13)
   - *Format Prediksi:* Pilihan Ganda & Analisis Rasio
   - *Level Kognitif:* Bloom: **Understand & Apply**
   - *Prioritas Belajar:* **IMPORTANT (Should Study)**

#### 🟢 LOW CONFIDENCE (Probabilitas 20–40% — Review Cepat)
6. **Topik 6**: Indikator Mortalitas Kesehatan & Imunisasi Dasar Lengkap (Pertemuan 10)
   - *Format Prediksi:* Pilihan Ganda Definisi / Pencocokan Formula
   - *Level Kognitif:* Bloom: **Remember & Understand**
   - *Contoh Soal Prediksi:*
     > *"Berapakah basis konstanta pengali baku dalam perhitungan Angka Kematian Ibu (AKI / MMR) menurut standar statistik kesehatan BPS dan WHO?"* (Jawaban: per 100.000 Kelahiran Hidup).
   - *Prioritas Belajar:* **SKIM ONLY (Quick Review)**

#### ⚡ WILDCARD ALERTS (Potensi Soal Kejutan)
- **Wildcard 1 (Merchanting Goods SNA 2008 - Pertemuan 13):** Konsep ini sering dilewati dalam belajar cepat karena berada di slide akhir perkuliahan, namun merupakan pembaruan fundamental standar statistik internasional yang disukai dosen pengampu.
- **Wildcard 2 (Formula Gross Barter ToT vs Net Barter ToT - Pertemuan 13):** Rumus GBToT membalik rasio ($Qm/Qx \times 100$) dibandingkan NBToT ($Px/Pm \times 100$), sering menjadi jebakan pembalikan rumus.

---

### Tahap 2: Matriks Prioritas Belajar (*Study Priority Matrix*)

| Kategori Prioritas | Bab / Materi Kuliah | Bobot Empiris Historis | Estimasi Alokasi Waktu | Level Bloom Dominan | Bentuk Soal UAS yang Diproyeksikan |
|---|---|---|---|---|---|
| 🔴 **MUST STUDY (Prioritas Tertinggi)** | **Pertemuan 8**: Indikator Kemiskinan & Ketimpangan Pendapatan | **29,7%** (UAS: 33,3%, Lat: 26,0%) | **30%** | *Apply & Analyze* | Soal Hitungan $P_0, P_1, P_2$, Gini Ratio, batas garis kemiskinan (GKM/GKNM), kriteria Bank Dunia. |
| 🔴 **MUST STUDY (Prioritas Tertinggi)** | **Pertemuan 12**: Perdagangan & Harga (IHK, Inflasi, NTP) | **16,9%** (UAS: 23,8%, Lat: 10,0%) | **25%** | *Apply & Analyze* | Hitungan IHK Modified Laspeyres, Disagregasi Inflasi (Inti vs Bergejolak), Rasio NTP ($It/Ib$) & NTUP. |
| 🟡 **SHOULD STUDY (Prioritas Tinggi)** | **Pertemuan 9**: Ketenagakerjaan & Pendidikan | **16,5%** (UAS: 19,0%, Lat: 14,0%) | **15%** | *Understand & Apply* | Kasus klasifikasi ICLS 13 (bekerja vs penganggur vs bukan angkatan kerja), setengah penganggur, TPAK/TPT, APM/APK. |
| 🟡 **SHOULD STUDY (Prioritas Tinggi)** | **Pertemuan 11**: Produksi Pertanian & Non-Pertanian | **15,0%** (UAS: 11,9%, Lat: 18,0%) | **15%** | *Remember & Apply* | Metodologi KSA (subsegmen & fase amatan), Ubinan, konversi GKP ke Beras, kriteria IBS/IMK. |
| 🟡 **SHOULD STUDY (Prioritas Tinggi)** | **Pertemuan 13**: Ekspor-Impor, ToT, & Pariwisata | **15,8%** (UAS: 9,5%, Lat: 22,0%) | **10%** | *Understand & Apply* | Valuasi FOB vs CIF, Merchanting SNA 2008, hitungan Net Barter ToT, rumus TPK dan RLMT hotel. |
| 🟢 **QUICK REVIEW (Review Ringkas)** | **Pertemuan 10**: Indikator Kesehatan & SDGs 3 | **6,2%** (UAS: 2,4%, Lat: 10,0%) | **5%** | *Remember & Understand* | Definisi formula AKI (MMR), AKB (IMR), AKABA, Morbiditas, dan Imunisasi Dasar Lengkap. |
| ⚪ **SKIP / BACKGROUND ONLY** | Materi Pra-UTS (Pertemuan 1 s.d. 7: SDI, Metadata, dll.) | **0,0%** | **0%** | *Remember* | Hanya konteks latar belakang; tidak masuk porsi ujian tertulis UAS (fokus pasca-UTS). |

---

## 4. Analisis Pola Dosen & Jebakan Soal (*Professor Pitfalls & Traps*)

Dosen Pengampu (**Tiodora Hadumaon Siagian**) menekankan presisi konsep institusional BPS dan penalaran analitis, bukan sekadar hafalan. Berikut adalah pola jebakan (*traps*) yang sering muncul dalam naskah ujian OSL:

1. **Jebakan Konsep Bekerja (Pertemuan 9)**:
   - *Pola Jebakan*: Seseorang yang membantu warung orang tua tanpa dibayar selama 2 jam seminggu, sering salah dikira "bukan angkatan kerja" atau "penganggur".
   - *Kaidah Benar*: Menurut BPS & ICLS 13, bekerja minimal 1 jam berturut-turut seminggu yang lalu (termasuk pekerja keluarga tidak dibayar / *unpaid family worker*) sudah masuk kategori **Bekerja**.
2. **Jebakan Setengah Penganggur vs Pekerja Paruh Waktu (Pertemuan 9)**:
   - *Pola Jebakan*: Soal memberikan studi kasus orang yang bekerja 20 jam seminggu dan merasa puas dengan pekerjaannya.
   - *Kaidah Benar*: Ini adalah **Pekerja Paruh Waktu Sukarela**, BUKAN Setengah Penganggur. Setengah penganggur mensyaratkan jam kerja < 35 jam **DAN** masih mencari atau bersedia menerima pekerjaan tambahan.
3. **Jebakan Valuasi Impor (Pertemuan 13)**:
   - *Pola Jebakan*: Soal menanyakan valuasi impor pada Neraca Pembayaran (*Balance of Payments*) vs Statistik Perdagangan Luar Negeri BPS.
   - *Kaidah Benar*: BPS mencatat Impor Luar Negeri dengan **CIF**, tetapi dalam pencatatan Neraca Pembayaran (SNA 2008 / BPM6) impor dinilai dengan **FOB** (komponen asuransi dan pengangkutan dipisahkan ke neraca jasa).
4. **Jebakan Kenaikan Pendapatan Merata pada Kemiskinan (Pertemuan 8)**:
   - *Pola Jebakan*: "Jika pendapatan seluruh penduduk naik 2 kali lipat secara proporsional persis sama, apakah kemiskinan dan ketimpangan berkurang?"
   - *Kaidah Benar*: Kemiskinan absolut ($P_0$) berkurang secara drastis, tetapi **Kemiskinan Relatif** dan **Koefisien Gini TIDAK BERUBAH** karena proporsi distribusi tetap sama persis.
5. **Jebakan Interpretasi NTP (Pertemuan 12)**:
   - *Pola Jebakan*: Menyimpulkan bahwa NTP > 100 berarti petani hidup makmur dan kaya raya.
   - *Kaidah Benar*: NTP > 100 hanya menunjukkan bahwa kenaikan harga hasil produksi yang diterima petani lebih besar daripada kenaikan harga barang yang dibeli petani dibanding tahun dasar (daya tukar membaik secara relatif), bukan ukuran mutlak kekayaan nominal.

---

## 5. Artefak Visual Peta Konsep (*Study Mind Map*) & Dashboard Pembelajaran

Sebagai bagian dari keluaran Langkah 3 yang dapat langsung dibuka dan diinspeksi secara offline oleh pengguna:

1. **Peta Konsep Keseluruhan (Full Book Mind Map):**
   - File: `internal/mindmaps/book.html`
   - Fitur: Visualisasi pohon 39 poin konsep, navigasi drag-pan & scroll-zoom, pelacakan level penguasaan warna (abu-abu/merah/kuning/hijau), bintang penanda poin prioritas tinggi, dan fitur pencarian dinamis.
2. **Peta Konsep Per Pertemuan:**
   - Pertemuan 8 (Kemiskinan & Gini): `internal/mindmaps/chapter-08.html`
   - Pertemuan 9 (Ketenagakerjaan & Pendidikan): `internal/mindmaps/chapter-09.html`
   - Pertemuan 10 (Kesehatan & SDGs 3): `internal/mindmaps/chapter-10.html`
   - Pertemuan 11 (Statistik Produksi & KSA): `internal/mindmaps/chapter-11.html`
   - Pertemuan 12 (Perdagangan, IHK, NTP): `internal/mindmaps/chapter-12.html`
   - Pertemuan 13 (Ekspor-Impor & Pariwisata): `internal/mindmaps/chapter-13.html`
3. **Dashboard Pembelajaran & Status State:**
   - Dashboard: `open/dashboard.html`
   - Ringkasan State: `internal/state/digest.md`
   - Berkas Pelacak: `internal/state/knowledge.json` dan `internal/state/progress.json` (tervalidasi kontrak `validate_workspace.py`).

---

## 6. Lembar Konfirmasi Pengguna (*Human Checkpoint Sign-Off*)

Berdasarkan pemetaan di atas, silakan berikan konfirmasi persetujuan sebelum melangkah ke **Langkah 4 (Pembuatan Modul Ajar Bertahap via `study-teach`)**:

- [x] **Pemeriksaan Cakupan Materi**: Pertemuan 8 s.d. 13 telah mencakup seluruh silabus resmi dosen pengampu dan seluruh slide perkuliahan pasca-UTS (39 poin konsep terinventarisasi).
- [x] **Pemeriksaan Hirarki Sumber**: Rujukan didasarkan pada Silabus > Slide Kuliah > Publikasi Resmi BPS > Naskah Soal Ujian Riil.
- [x] **Alokasi Bobot Prioritas**: Pembobotan waktu belajar (Must Study: Pertemuan 8 & 12; Should Study: Pertemuan 9, 11, 13; Quick Review: Pertemuan 10) telah selaras dengan temuan backtest empiris.
- [x] **Pemeriksaan Artefak Visual**: Peta konsep interaktif `internal/mindmaps/book.html` dan dashboard `open/dashboard.html` siap dibuka secara offline.

*(Status: Draf Usulan Lengkap Langkah 3 — Siap untuk Konfirmasi Pengguna).*

