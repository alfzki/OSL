# Official Statistics Lanjutan (OSL) — One-Page A4 Cheat Sheet Rumus & Definisi Resmi

> **Mata Kuliah**: Official Statistics Lanjutan (OSL) — Kode MK: K200207  
> **Dosen Pengampu**: Dr. Tiodora Hadumaon Siagian  
> **Jadwal Ujian**: Ujian Tertulis UAS, 30 September 2026 (Durasi: 120 Menit, PG & Esai)  
> **Prinsip Grounding**: 100% Bersumber dari Silabus Resmi, Slide Kuliah Pertemuan 8 s.d. 13, & Publikasi BPS.

---

## 1. Pertemuan 8: Kemiskinan FGT, Garis Kemiskinan, & Ketimpangan Pendapatan

### A. Indeks Kemiskinan FGT (Foster-Greer-Thorbecke)
$$\text{Formula Umum: } P_\alpha = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^\alpha$$
- **Headcount Index ($P_0$, $\alpha=0$)**: $P_0 = \frac{q}{n}$ (Persentase penduduk miskin).
- **Poverty Gap Index ($P_1$, $\alpha=1$)**: $P_1 = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)$ (Kedalaman kemiskinan / rata-rata kesenjangan terhadap Garis Kemiskinan).
- **Poverty Severity Index ($P_2$, $\alpha=2$)**: $P_2 = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^2$ (Keparahan kemiskinan / ketimpangan pengeluaran di antara penduduk miskin).
- **[KRITIS] Syarat Batas**: Pembagi selalu total populasi **$n$**, bukan hanya jumlah penduduk miskin $q$!

### B. Metodologi Garis Kemiskinan BPS (Cost of Basic Needs / CBN)
$$GK = GKM + GKNM$$
- **GKM (Garis Kemiskinan Makanan)**: Patokan kecukupan energi **2.100 kkal** per kapita per hari, diwakili oleh 52 komoditi makanan pokok.
- **GKNM (Garis Kemiskinan Non-Makanan)**: Nilai minimum kebutuhan perumahan, sandang, pendidikan, dan kesehatan (51 komoditas perkotaan, 47 komoditas perdesaan).

### C. Kurva Lorenz & Koefisien Gini
$$G = 1 - \sum_{i=1}^k (X_i - X_{i-1})(Y_i + Y_{i-1})$$
- $X_i$: Persentase kumulatif penduduk, $Y_i$: Persentase kumulatif pengeluaran/pendapatan.
- **Kriteria Ketimpangan Bank Dunia (Proporsi Pengeluaran 40% Terbawah)**:
  - $< 12\%$ : Ketimpangan **Tinggi**
  - $12\% - 17\%$ : Ketimpangan **Sedang**
  - $> 17\%$ : Ketimpangan **Rendah**
- **[JEBAKAN]**: Kenaikan pendapatan merata berkelipatan sama ($2 \times$) menurunkan $P_0$, tetapi **Gini dan kemiskinan relatif tidak berubah**.

---

## 2. Pertemuan 9: Ketenagakerjaan (ICLS 13) & Indikator Pendidikan

### A. Kerangka Ketenagakerjaan BPS & ICLS 13
- **Penduduk Usia Kerja (PUK)**: Penduduk usia **15 tahun ke atas**.
- **Bekerja**: Melakukan kegiatan ekonomi dengan maksud memperoleh penghasilan/keuntungan minimal **1 jam berturut-turut** dalam seminggu terakhir (termasuk pekerja keluarga tidak dibayar / *unpaid family worker*).
- **Angkatan Kerja (AK)** = Bekerja + Pengangguran Terbuka.
- **Bukan Angkatan Kerja (BAK)** = Sekolah + Mengurus Rumah Tangga + Lainnya (Pensiunan/Lansia).

$$\text{TPAK} = \frac{\text{Angkatan Kerja}}{\text{Penduduk Usia Kerja (15+)}} \times 100\%$$
$$\text{TPT} = \frac{\text{Pengangguran Terbuka}}{\text{Angkatan Kerja}} \times 100\%$$

### B. Batasan Bekerja Tidak Penuh (Underemployment Cutoff: 35 Jam)
- **Setengah Penganggur (*Underemployed*)**: Bekerja $< 35$ jam seminggu **DAN** masih mencari atau bersedia menerima pekerjaan tambahan.
- **Pekerja Paruh Waktu (*Part-time*)**: Bekerja $< 35$ jam seminggu tetapi **TIDAK** mencari dan tidak bersedia menerima pekerjaan tambahan.

### C. Indikator Partisipasi Pendidikan
$$\text{APM} = \frac{\text{Siswa Usia Resmi di Jenjang X}}{\text{Penduduk Usia Resmi Jenjang X}} \times 100\% \quad (\text{Selalu } \le 100\%)$$
$$\text{APK} = \frac{\text{Seluruh Siswa Terdaftar di Jenjang X}}{\text{Penduduk Usia Resmi Jenjang X}} \times 100\% \quad (\text{Bisa } > 100\%)$$
$$\text{APS} = \frac{\text{Penduduk Usia X yang Masih Bersekolah}}{\text{Total Penduduk Usia X}} \times 100\%$$

---

## 3. Pertemuan 10: Indikator Kesehatan & SDGs Tujuan 3

### A. Indikator Mortalitas & Pengali Baku
$$\text{Angka Kematian Ibu (AKI / MMR)} = \frac{\sum \text{Kematian Ibu Hamil/Persalinan/Nifas}}{\sum \text{Kelahiran Hidup}} \times 100.000 \text{ KH}$$
$$\text{Angka Kematian Bayi (AKB / IMR)} = \frac{\sum \text{Kematian Bayi } (< 1 \text{ th})}{\sum \text{Kelahiran Hidup}} \times 1.000 \text{ KH}$$
$$\text{Angka Kematian Balita (AKABA / U5MR)} = \frac{\sum \text{Kematian Anak } (< 5 \text{ th})}{\sum \text{Kelahiran Hidup}} \times 1.000 \text{ KH}$$
$$\text{Angka Kematian Neonatal (NMR)} = \frac{\sum \text{Kematian Bayi } (< 28 \text{ hari})}{\sum \text{Kelahiran Hidup}} \times 1.000 \text{ KH}$$

### B. Morbiditas & Imunisasi
- **Morbiditas (Angka Kesakitan)**: Persentase penduduk yang mengalami keluhan kesehatan yang mengganggu aktivitas sehari-hari dalam kurun waktu **1 bulan terakhir**.
- **Imunisasi Dasar Lengkap (IDL)**: HB-0 (0-7 hari), BCG (1 dosis), DPT-HB-Hib (3 dosis), Polio (4 dosis tetes / 1 suntik), Campak/MR (1 dosis) sebelum bayi genap berusia 1 tahun.

---

## 4. Pertemuan 11: Statistik Produksi Pertanian & Industri

### A. Estimasi Produksi Padi & Kerangka Sampel Area (KSA)
$$\text{Produksi Padi (Ku)} = \text{Luas Panen (Ha)} \times \text{Produktivitas (Ku/Ha)}$$
- **KSA (Kerangka Sampel Area)**: Segmen berukuran **$300\text{ m} \times 300\text{ m}$** dibagi menjadi **9 subsegmen** ($100\text{ m} \times 100\text{ m}$). Diamati visual via aplikasi Android pada **7 hari terakhir setiap bulan**.
- **Metode Ubinan**: Plot petak sawah ukuran standar **$2,5\text{ m} \times 2,5\text{ m} = 6,25\text{ m}^2$**.
  $$\text{Pengali ke Hektar} = \frac{10.000\text{ m}^2}{6,25\text{ m}^2} = 1.600$$
  $$\text{Produktivitas (Ku/Ha)} = \text{Hasil Ubinan (kg)} \times 16$$
- **SKGB**: Konversi Gabah Kering Panen (GKP) $\rightarrow$ Gabah Kering Giling (GKG) $\rightarrow$ Beras.

### B. Klasifikasi Industri Pengolahan (Manufaktur)
- **Industri Besar dan Sedang (IBS)**: Tenaga kerja **$\ge 20$ orang** (Survei Tahunan & Bulanan IBS).
- **Industri Mikro dan Kecil (IMK)**: Tenaga kerja **$1 - 19$ orang** (Survei Triwulanan & Tahunan IMK).

---

## 5. Pertemuan 12: Perdagangan Dalam Negeri, IHK & Nilai Tukar Petani

### A. Indeks Harga Konsumen (Modified Laspeyres)
$$I_t = \sum_{i=1}^k \left( \frac{P_{ti}}{P_{t-1, i}} \times W_{t-1, i} \right) \quad \text{di mana } W \text{ bersumber dari Survei Biaya Hidup (SBH)}$$

### B. Tiga Jenis Laju Inflasi BPS
$$\text{Inflasi } m\text{-to-}m = \frac{IHK_t - IHK_{t-1}}{IHK_{t-1}} \times 100\%$$
$$\text{Inflasi } y\text{-on-}y = \frac{IHK_{t, y} - IHK_{t, y-1}}{IHK_{t, y-1}} \times 100\%$$
$$\text{Inflasi } y\text{-t-}d = \frac{IHK_t - IHK_{\text{Des } y-1}}{IHK_{\text{Des } y-1}} \times 100\%$$
- **Disagregasi**: (1) Inflasi Inti (*Core* / persisten), (2) *Volatile Foods* (gejolak musiman/panen), (3) *Administered Prices* (kebijakan harga pemerintah).

### C. Nilai Tukar Petani (NTP) & NTUP
$$\text{NTP} = \frac{I_t}{I_b} \times 100 \quad \text{dan} \quad \text{NTUP} = \frac{I_t}{\text{BPPBM}} \times 100$$
- $I_t$: Indeks harga yang diterima petani (penjualan hasil produksi).
- $I_b$: Indeks harga yang dibayar petani = **IKRT** (konsumsi rumah tangga) + **BPPBM** (biaya produksi dan modal).
- **5 Subsektor NTP**: NTPR (Tanaman Pangan), NTPH (Hortikultura), NTPR-Bun (Perkebunan Rakyat), NTPT (Peternakan), NTNP (Perikanan: Tangkap & Budidaya).

---

## 6. Pertemuan 13: Ekspor-Impor, Terms of Trade & Pariwisata

### A. Valuasi Perdagangan Luar Negeri & SNA 2008
- **Ekspor BPS**: Dinilai berdasarkan **FOB** (*Free On Board*) di pelabuhan muat.
- **Impor BPS**: Dinilai berdasarkan **CIF** (*Cost, Insurance, and Freight*) di pelabuhan bongkar.
- **Impor Neraca Pembayaran / SNA 2008**: Dikonversi ke **FOB** (biaya asuransi dan pengangkutan dipisahkan ke neraca jasa).
- **Merchanting Goods (SNA 2008)**: Pembelian barang oleh residen dari non-residen yang dijual kembali ke non-residen tanpa fisik barang masuk ke wilayah pabean domestik (dicatat sebagai ekspor neto).

### B. Formula Terms of Trade (ToT)
$$\text{Net Barter ToT (NBToT)} = \frac{P_x}{P_m} \times 100 \quad (P_x=\text{Harga Ekspor}, P_m=\text{Harga Impor})$$
$$\text{Gross Barter ToT (GBToT)} = \frac{Q_m}{Q_x} \times 100 \quad (\text{[PEMBALIKAN] } Q_m=\text{Volume Impor}, Q_x=\text{Volume Ekspor})$$
$$\text{Income ToT (IToT)} = \text{NBToT} \times \frac{Q_x}{100} = \frac{P_x \cdot Q_x}{P_m}$$

### C. Statistik Perhotelan & Pariwisata
$$\text{Tingkat Penghunian Kamar (TPK)} = \frac{\sum \text{Malam Kamar Terpakai}}{\sum \text{Malam Kamar Tersedia}} \times 100\%$$
$$\text{Rata-rata Lama Menginap Tamu (RLMT)} = \frac{\sum \text{Malam Tempat Tidur Terpakai}}{\sum \text{Tamu yang Datang}}$$
- **Wisman**: Berkunjung $< 1$ tahun, bukan untuk bekerja/mencari nafkah dari negara yang dikunjungi.
- **Wisnus**: Perjalanan dalam negeri minimal 100 km bolak-balik atau menginap.
