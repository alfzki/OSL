---
tags: [osl, formulas]
status: draft
---

# Rumus OSL

Kumpulan rumus seluruh bab OSL dalam format LaTeX/MathJax.
Dapat dirender langsung di Obsidian atau aplikasi Markdown dengan dukungan KaTeX/MathJax.

## Pertemuan 10: Indikator Kesehatan dan SDGs 3

### 10.1.1 Angka Kematian Ibu AKI MMR

$$\text{MMR} = \frac{\sum \text{Kematian Ibu Maternal}}{\sum \text{Kelahiran Hidup}} \times 100.000$$

Rujukan: [Pertemuan_10_Indikator_Kesehatan.md, slide/hal. 4-20] [Pertemuan_10_Indikator_Kesehatan.md, slide/hal. 33-36]

### 10.1.2 Angka Kematian Bayi AKB dan Balita AKABA

$$\text{AKB} = \frac{D_{0-<1\text{ th}}}{B} \times 1.000, \quad \text{AK Anak} = \frac{D_{1-4\text{ th}}}{P_{1-4}} \times 1.000, \quad \text{AKABA} = \frac{D_{0-4\text{ th}}}{P_{0-4}} \times 1.000$$

Rujukan: [Pertemuan_10_Indikator_Kesehatan.md, slide/hal. 18-35]

### 10.1.3 Angka Kematian Neo-Natal NMR

$$\text{NMR} = \frac{D_{0-<28\text{ hari}}}{B} \times 1.000, \quad \text{PNMR} = \frac{D_{1\text{ bln}-<1\text{ th}}}{B} \times 1.000, \quad \text{AKB} = \text{NMR} + \text{PNMR}$$

Rujukan: [Pertemuan_10_Indikator_Kesehatan.md, slide/hal. 24-35]

### 10.2.1 Angka Kesakitan Morbiditas

$$\text{Morbiditas} = \frac{\sum P_{\text{terganggu}}}{\sum P} \times 100\%, \quad Z = \frac{X - \text{Median}}{\text{SD}}, \quad \text{Stunting}(\%) = \frac{\sum \text{Balita}(Z_{\text{TB/U}} < -2\text{ SD})}{\sum \text{Balita Diukur}} \times 100\%$$

Rujukan: [Pertemuan_10_Indikator_Kesehatan.md, slide/hal. 36-65] [SUPLEMEN: suplemen]

### 10.2.2 Imunisasi Dasar Lengkap IDL

$$\text{Cakupan IDL} = \frac{\sum \text{Anak(IDL Lengkap)}}{\sum \text{Sasaran Anak}} \times 100\%, \quad \text{Skor Kumuh} = 0,15 D_{\text{air}} + 0,15 D_{\text{sanitasi}} + 0,35 D_{\text{luas}} + 0,35 D_{\text{durabilitas}}$$

Rujukan: [Pertemuan_10_Indikator_Kesehatan.md, slide/hal. 40-42, 62-91] [SUPLEMEN: suplemen]

## Pertemuan 11: Statistik Produksi Pertanian dan Industri

### 11.1.1 Kerangka Sampel Area KSA Padi

$$\hat{A}_{\text{panen}} = \sum_{h=1}^H A_h \cdot \hat{p}_{h,\text{panen}} = \sum_{h=1}^H A_h \left( \frac{\sum_{i=1}^{n_h} \sum_{j=1}^{9} y_{hij}}{9 \cdot n_h} \right)$$

Rujukan: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 4-18]

### 11.1.2 Metode Ubinan Produktivitas

$$\text{Produktivitas (kg/ha)} = \frac{b}{6,25} \times 10.000 = b \times 1.600, \quad \text{Produktivitas (ku/ha)} = b \times 16, \quad \text{Produktivitas (ton/ha)} = b \times 1,6$$

Rujukan: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 19-27]

### 11.1.3 Survei Konversi Gabah ke Beras SKGB

$$\text{Produksi GKG} = \text{Produksi GKP} \times 0,8338, \quad \text{Produksi Beras} = \text{Produksi GKG} \times 0,6402 = \text{Produksi GKP} \times 0,533799$$

Rujukan: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 20-24]

### 11.2.1 Survei Industri Besar dan Sedang IBS

$$\text{Efisiensi IBS} = \frac{\text{Biaya Input Antara}}{\text{Nilai Output}}, \quad \text{Nilai Tambah Bruto} = \text{Output} - \text{Input}, \quad NK = (NP - NS) \times \%NR$$

Rujukan: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 25-28, 50-51]

### 11.2.2 Survei Industri Mikro dan Kecil IMK

$$\text{Klasifikasi IMK} = \begin{cases} \text{Industri Mikro (IM)}, & 1 \le L \le 4 \\ \text{Industri Kecil (IK)}, & 5 \le L \le 19 \\ \text{Industri Sedang (IS)}, & 20 \le L \le 99 \\ \text{Industri Besar (IB)}, & L \ge 100 \end{cases}, \quad \text{Produktivitas} = \frac{\text{Nilai Tambah}}{L}$$

Rujukan: [SUPLEMEN: [SUPLEMEN] BPS Sensus Ekonomi 2016 & Publikasi Profil Industri Mikro dan Kecil 2024]

## Pertemuan 12: Perdagangan dan Indikator Harga

### 12.1.1 Margin Perdagangan dan Pengangkutan MPP

$$MPP_i = \frac{P_{\text{jual}, i} - P_{\text{beli}, i}}{P_{\text{beli}, i}} \times 100\%, \quad 1 + MPP_{\text{total}} = \prod_{i=1}^n (1 + MPP_i), \quad MPP_{\text{total}} = \frac{P_{\text{konsumen akhir}} - P_{\text{produsen}}}{P_{\text{produsen}}} \times 100\%$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 4-9]

### 12.1.2 Survei Pola Distribusi Perdagangan Poldis

$$\text{MPP}_{\text{rantai}} = \frac{P_{\text{konsumen akhir}} - P_{\text{produsen}}}{P_{\text{produsen}}} \times 100\%, \quad \Delta \text{Beban} = \text{MPP}_{\text{rantai panjang}} - \text{MPP}_{\text{rantai pendek}}$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 10-13]

### 12.2.1 IHK Rumus Modified Laspeyres

$$IHK_t = \frac{\sum_{i=1}^k \left( \frac{P_{ti}}{P_{(t-1)i}} \times P_{(t-1)i} Q_{0i} \right)}{\sum_{i=1}^k P_{0i} Q_{0i}} \times 100 = \sum_{i=1}^k \left( \frac{P_{ti}}{P_{(t-1)i}} \times W_{(t-1)i} \right)$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 14-20] [indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.md, slide/hal. 15-25]

### 12.2.2 Tiga Laju Inflasi BPS mtom yony ytd

$$\pi_{m\text{-to-}m} = \frac{IHK_{t, m} - IHK_{t, m-1}}{IHK_{t, m-1}} \times 100\%, \quad \pi_{y\text{-to-}d} = \frac{IHK_{t, m} - IHK_{t-1, 12}}{IHK_{t-1, 12}} \times 100\%, \quad \pi_{y\text{-on-}y} = \frac{IHK_{t, m} - IHK_{t-1, m}}{IHK_{t-1, m}} \times 100\%$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 21-26]

### 12.2.3 Disagregasi Inflasi Inti Bergejolak Administered

$$\pi_{\text{headline}} = \sum_{k \in \{\text{inti}, \text{bergejolak}, \text{diatur}\}} \left( \frac{w_k}{100} \times \pi_k \right), \quad \text{Andil}_k = \frac{w_k}{100} \times \pi_k$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 18-21]

### 12.3.1 Konsep dan Rasio NTP It per Ib

$$NTP = \frac{I_t}{I_b} \times 100, \quad I_b = w_{\text{IKRT}} \cdot IKRT + w_{\text{BPPBM}} \cdot BPPBM, \quad \text{Inflasi Perdesaan} = \frac{IKRT_t - IKRT_{t-1}}{IKRT_{t-1}} \times 100\%$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 33-36]

### 12.3.2 Nilai Tukar Usaha Petani NTUP

$$NTUP = \frac{I_t}{BPPBM} \times 100, \quad \text{Upah Riil Buruh Tani} = \frac{\text{Upah Nominal}}{IKRT} \times 100$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 37-38]

### 12.3.3 Lima Subsektor Penyusun NTP

$$NTP_{\text{gabungan}} = \sum_{s=1}^5 \left( w_s \times NTP_s \right), \quad \text{di mana } \sum_{s=1}^5 w_s = 1,0$$

Rujukan: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 36-40]

## Pertemuan 13: Ekspor-Impor, Terms of Trade, dan Pariwisata

### 13.1.1 Valuasi Ekspor Impor FOB vs CIF

$$\text{CIF} = \text{FOB} + \text{Freight} + \text{Insurance}, \quad X_{\text{IDR}} = X_{\text{USD}} \times \bar{K}_{\text{beli}}, \quad M_{\text{IDR}} = M_{\text{USD}} \times \bar{K}_{\text{jual}}$$

Rujukan: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 4-9]

### 13.1.2 Barang Dagangan Tanpa Masuk Pabean Merchanting

$$\text{Ekspor Neto Merchanting} = X_{\text{merchanting (penjualan)}} - M_{\text{merchanting (perolehan)}} = X_{\text{positif}} + X_{\text{negatif}}$$

Rujukan: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 5, 10-15]

### 13.1.3 Net Barter Terms of Trade NBToT

$$\text{NBToT} = \frac{P_x}{P_m} \times 100, \quad \text{ISP}_i = \frac{X_i - M_i}{X_i + M_i}, \quad \text{RCA}_{ij} = \frac{X_{ij} / X_j}{X_{iw} / X_w}, \quad \text{Openness} = \frac{X_t + M_t}{\text{PDB}_t} \times 100\%$$

Rujukan: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 10-16]

### 13.1.4 Gross Barter dan Income ToT

$$\text{Income ToT} = \text{KM} = \frac{\text{NBToT} \times Q_x}{100} = \frac{X_{\text{ADHB}}}{P_m} \times 100, \quad \text{GBToT [SUPLEMEN]} = \frac{Q_m}{Q_x} \times 100$$

Rujukan: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 15, 25-28] [SUPLEMEN: suplemen]

### 13.2.1 Definisi Wisman dan Wisnus

$$\text{Total Pengunjung Mancanegara (Visitors)} = \text{Wisatawan (Tourists)} + \text{Pelancong (Excursionists)}$$

Rujukan: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 32-38]

### 13.2.2 Tingkat Penghunian Kamar TPK Hotel

$$\text{TPK} = \frac{\text{Malam Kamar Terpakai}}{\text{Malam Kamar Tersedia}} \times 100\% = \frac{\sum_{t=1}^D K_{\text{terpakai}, t}}{\text{Jumlah Kamar} \times \text{Jumlah Hari Buka}} \times 100\%$$

Rujukan: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 36-41]

### 13.2.3 Rata-rata Lama Menginap Tamu RLMT

$$\text{RLMT} = \frac{\text{Total Malam Tamu Menginap}}{\text{Total Tamu yang Datang \& Menginap}} = \frac{\sum_{i=1}^N L_i}{N}, \quad \text{RLMT}_{\text{gabungan}} = \frac{M_{\text{asing}} + M_{\text{domestik}}}{T_{\text{asing}} + T_{\text{domestik}}}$$

Rujukan: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 40-43]

## Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan

### 8.1.1 Konsep Kemiskinan Absolut dan Relatif

$$z_{\text{abs}} = \text{konstan riil}, \quad z_{\text{rel}} = k \cdot \text{Median}(Y), \quad 0 < k < 1$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 4-13]

### 8.1.2 Garis Kemiskinan Makanan dan Non-Makanan

$$GK = GKM + GKNM = \sum_{k=1}^{52} P_k \cdot Q_k^* + \sum_{l=1}^m \alpha_l \cdot P_l \cdot Q_l$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 14-16, 27]

### 8.1.3 Metodologi Cost of Basic Needs BPS

$$GK = \sum_{k=1}^{52} P_k Q_k^* + \sum_{l=1}^m \alpha_l P_l Q_l, \quad Q_k^* = Q_k \cdot \left(\frac{2.100}{\sum_{j=1}^{52} c_j Q_j}\right)$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 14, 17-19, 42-43]

### 8.2.1 Headcount Index P0

$$P_0 = \frac{q}{n} = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^0$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 20-21, 24-28]

### 8.2.2 Poverty Gap Index P1

$$P_1 = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^1 = P_0 \cdot I_{\text{gap}}, \quad I_{\text{gap}} = \frac{1}{q} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 20, 22, 24-29]

### 8.2.3 Poverty Severity Index P2

$$P_2 = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^2$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 20, 23, 24, 26, 29]

### 8.3.1 Kurva Lorenz dan Koefisien Gini

$$G = 1 - \sum_{i=1}^k (p_i - p_{i-1})(y_i + y_{i-1}) = 1 - \sum_{i=1}^k f_i (Y_i + Y_{i-1})$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 33-40]

### 8.3.2 Kriteria Ketimpangan Bank Dunia

$$\text{Pangsa 40\% Terbawah} = p_1 + p_2 = Y_2 \times 100\%, \quad \text{Tingkat} = \begin{cases} \text{Tinggi}, & < 12\% \\ \text{Sedang}, & 12\% \le \text{Pangsa} \le 17\% \\ \text{Rendah}, & > 17\% \end{cases}$$

Rujukan: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 41-44]

## Pertemuan 9: Ketenagakerjaan dan Pendidikan

### 9.1.1 Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja

$$\text{Populasi} = \text{PUK} + \text{BUK}, \quad \text{PUK} = \text{AK} + \text{BAK}, \quad \text{AK} = \text{Bekerja} + \text{Penganggur}$$

Rujukan: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 4-20] [Kuesioner_SAK.AGS25-AK.md, slide/hal. 15-22]

### 9.1.2 Tingkat Partisipasi Angkatan Kerja TPAK

$$\text{TPAK} = \frac{\text{AK}}{\text{PUK}} \times 100\% = \frac{\text{Bekerja} + \text{Penganggur}}{\text{Penduduk Usia } \ge 15 \text{ Tahun}} \times 100\%$$

Rujukan: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 13-14] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 21-23]

### 9.1.3 Tingkat Pengangguran Terbuka TPT

$$\text{TPT} = \frac{\text{Penganggur}}{\text{AK}} \times 100\% = \frac{\text{Penganggur}}{\text{Bekerja} + \text{Penganggur}} \times 100\%$$

Rujukan: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 15-16] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 21-23]

### 9.1.4 Setengah Penganggur vs Pekerja Paruh Waktu

$$\text{TSP} = \frac{\text{PB}_{<35, \text{mencari}}}{\text{PB}} \times 100\%, \quad \text{TPPW} = \frac{\text{PB}_{<35, \text{sukarela}}}{\text{PB}} \times 100\%, \quad \text{Proporsi INF} = \frac{\text{PB}_{\text{INF}}}{\text{PB}} \times 100\%$$

Rujukan: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 17-20] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 24-28]

### 9.2.1 Angka Partisipasi Murni APM dan Kasar APK

$$\text{APM}_J = \frac{S_{J, \text{usia } J}}{P_{\text{usia } J}} \times 100\%, \quad \text{APK}_J = \frac{\sum_{\text{semua umur}} S_J}{P_{\text{usia } J}} \times 100\%$$

Rujukan: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 66-71] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 51-55]

### 9.2.2 Angka Partisipasi Sekolah APS

$$\text{APS}_{x-y} = \frac{\sum \text{Siswa Bersekolah Usia } x-y}{P_{x-y}} \times 100\%, \quad \text{AMH}_{15+} = \frac{\text{MH}_{15+}}{P_{15+}} \times 100\%$$

Rujukan: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 61-65] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 57-60] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 72-74]

---

[[_MOC|← Back to MOC]]
