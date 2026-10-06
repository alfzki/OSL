# Laporan Survei Investigasi Ujian & Verifikasi Numerik OSL (Pertemuan 8 s.d. 13)

**Penyusun**: Survey Agent 3 (Exam & Numerical Verification Explorer)  
**Tanggal**: 2026-09-29  
**Status**: Final Survey Report  
**Ruang Lingkup**: Evaluasi Naskah Ujian Resmi (`Soal_UAS_2022-2023.md`), Soal Latihan Dosen (`soal_latihan_uas.md`), Bahan Slide Kuliah Pertemuan 8 s.d. 13, Publikasi Resmi BPS (IHK 2025, Sakernas 2025), Formula Kuantitatif, Tabel Data Riil, Jebakan Dosen (*Lecturer Pitfalls*), dan Kode Verifikasi Komputasional Python.

---

## 1. Ringkasan Eksekutif & Batasan Masalah

Penyusunan modul ajar komprehensif dan bank soal teruji untuk mata kuliah **Official Statistics Lanjutan (OSL)** menuntut ketepatan matematis absolut dan grounding institusional berstandar Badan Pusat Statistik (BPS). Sesuai arahan pada `ORIGINAL_REQUEST.md` (R2 dan R3), tidak boleh ada formula atau angka perhitungan yang disajikan tanpa verifikasi komputasional independen melalui eksekusi kode Python.

Laporan ini menyajikan:
1. **Katalog Lengkap Formula Kuantitatif**: Seluruh indikator dari Pertemuan 8 s.d. 13 dirinci dengan notasi matematis baku, definisi variabel operasional BPS, dan kondisi batasnya.
2. **Kompilasi Dataset & Soal Hitungan Riil**: Rekonstruksi eksak terhadap soal hitungan dari naskah ujian resmi UAS 2022/2023 (baik soal esai maupun pilihan ganda numerik) serta contoh soal pada slide dosen pengampu.
3. **Analisis Jebakan Dosen (*Professor Pitfalls & Traps*)**: Pengelupasan 10 pola jebakan khas dosen pengampu (**Dr. Tiodora Hadumaon Siagian**) yang sering mengecoh mahasiswa pada ujian OSL.
4. **Skrip Verifikasi Python Mandiri**: Implementasi dan eksekusi skrip Python murni (standar pustaka tanpa dependensi eksternal, patuh *Zero Host Mutation*) yang memvalidasi seluruh dataset numerik dengan akurasi 100%.

---

## 2. Inventarisasi Formula & Indikator Kuantitatif (Pertemuan 8 s.d. 13)

### A. Pertemuan 8: Indikator Kemiskinan dan Ketimpangan Pendapatan
*Rujukan Slide: `Pertemuan 8 OSL Indikator Sosial (1) Indikator Kemiskinan dan Ketimpangan _ new.pptx` [slide 14-39]*

1. **Garis Kemiskinan BPS (Cost of Basic Needs Approach)** `[slide 14-16]`:
   $$GK = GKM + GKNM$$
   - $GKM$ (Garis Kemiskinan Makanan): Nilai pengeluaran kebutuhan minimum makanan yang disetarakan dengan $2.100\text{ kkal per kapita per hari}$ berdasarkan rekomendasi WNPG 1978, diwakili oleh 52 komoditi makanan pokok pada populasi rujukan (*reference population*).
   - $GKNM$ (Garis Kemiskinan Bukan Makanan): Nilai pengeluaran minimum kebutuhan non-makanan dasar (perumahan, sandang, pendidikan, kesehatan) yang mencakup 51 komoditas di perkotaan dan 47 komoditas di perdesaan.
   - Status Kemiskinan: Penduduk dengan pengeluaran per kapita sebulan $y_i < GK$ dikategorikan sebagai **Miskin**.

2. **Indeks Kemiskinan Foster-Greer-Thorbecke (FGT)** `[slide 20-23]`:
   $$P_\alpha = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)^\alpha$$
   - $z$: Garis Kemiskinan ($GK$).
   - $y_i$: Rata-rata pengeluaran per kapita sebulan penduduk miskin ke-$i$ ($y_i < z$).
   - $q$: Jumlah penduduk yang berada di bawah garis kemiskinan.
   - $n$: Jumlah seluruh penduduk wilayah (bukan hanya penduduk miskin).
   - **Tiga Varian FGT**:
     - $\alpha = 0 \rightarrow P_0$: *Headcount Index* (Persentase Penduduk Miskin):
       $$P_0 = \frac{q}{n}$$
     - $\alpha = 1 \rightarrow P_1$: *Poverty Gap Index* (Indeks Kedalaman Kemiskinan):
       $$P_1 = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right) = P_0 \cdot \left(\frac{z - \bar{y}_q}{z}\right)$$
       Mengukur rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan.
     - $\alpha = 2 \rightarrow P_2$: *Poverty Severity Index* (Indeks Keparahan Kemiskinan):
       $$P_2 = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)^2$$
       Mengukur ketimpangan pengeluaran di antara sesama penduduk miskin (memberikan bobot lebih besar bagi penduduk yang sangat miskin).

3. **Koefisien Gini (Gini Ratio)** `[slide 38-39]`:
   $$G = 1 - \sum_{i=1}^k f_i (Y_i + Y_{i-1})$$
   - $k$: Jumlah kelas pengeluaran/pendapatan (misal kuintil $k=5$ atau desil $k=10$).
   - $f_i$: Proporsi/persentase penduduk pada kelas ke-$i$.
   - $Y_i$: Kumulatif proporsi/persentase pengeluaran hingga kelas ke-$i$ (dengan $Y_0 = 0$).
   - Hubungan Kurva Lorenz: $G = \frac{A}{A + B} = 2A = 1 - 2B$. Rentang nilai $0 \le G \le 1$.
   - Kategori BPS/Dunia:
     - $G < 0,3$ : Ketimpangan Rendah
     - $0,3 \le G \le 0,5$ : Ketimpangan Sedang
     - $G > 0,5$ : Ketimpangan Tinggi

4. **Kriteria Ketimpangan Distribusi Bank Dunia** `[slide 37]`:
   Berdasarkan pangsa pengeluaran kumulatif dari kelompok 40% penduduk terbawah ($Q_1 + Q_2$):
   - $< 12\%$ : Ketimpangan Tinggi
   - $12\% - 17\%$ : Ketimpangan Sedang
   - $> 17\%$ : Ketimpangan Rendah

---

### B. Pertemuan 9: Indikator Ketenagakerjaan dan Pendidikan
*Rujukan Slide: `Pertemuan 9 Indikator Ketenagakerjaan dan Pendidikan.pptx` [slide 11-70] & `materials/notes/Kuesioner SAK.AGS25-AK.pdf`*

1. **Kerangka Ketenagakerjaan ICLS 13**:
   - Penduduk Total = Penduduk Usia Kerja (PUK $\ge 15$ tahun) + Penduduk Bukan Usia Kerja (< 15 tahun).
   - $\text{PUK} = \text{Angkatan Kerja (AK)} + \text{Bukan Angkatan Kerja (BAK)}$.
   - $\text{Angkatan Kerja} = \text{Bekerja (PB)} + \text{Pengangguran Terbuka (PTP)}$.
   - $\text{Bukan Angkatan Kerja} = \text{Sekolah} + \text{Mengurus Rumah Tangga} + \text{Lainnya/Penerima Pendapatan/Manula}$.

2. **Tingkat Partisipasi Angkatan Kerja (TPAK)** `[slide 13]`:
   $$\text{TPAK} = \frac{\text{Jumlah Angkatan Kerja (AK)}}{\text{Penduduk Usia Kerja } (15+)} \times 100\%$$

3. **Tingkat Pengangguran Terbuka (TPT)** `[slide 15]`:
   $$\text{TPT} = \frac{\text{Jumlah Pengangguran Terbuka}}{\text{Jumlah Angkatan Kerja (AK)}} \times 100\%$$
   - 4 Kategori Pengangguran BPS: (1) Mencari pekerjaan, (2) Mempersiapkan usaha, (3) Merasa putus asa/tidak mungkin mendapat kerja (*discouraged worker*), (4) Sudah punya pekerjaan/diterima tetapi belum mulai bekerja.

4. **Tingkat Setengah Penganggur (TSP)** `[slide 17-18]`:
   $$\text{TSP} = \frac{\text{Jumlah Setengah Penganggur (jam kerja } < 35\text{ jam & mencari/bersedia kerja tambahan)}}{\text{Jumlah Penduduk yang Bekerja (PB)}} \times 100\%$$

5. **Tingkat Pekerja Paruh Waktu (TPPW)** `[slide 19-20]`:
   $$\text{TPPW} = \frac{\text{Jumlah Pekerja Paruh Waktu (jam kerja } < 35\text{ jam & sukarela/tidak mencari kerja)}}{\text{Jumlah Penduduk yang Bekerja (PB)}} \times 100\%$$

6. **Proporsi Lapangan Kerja Informal** `[slide 26-28]`:
   $$\text{Pr PB INF} = \frac{\text{Jumlah Pekerja Berstatus Informal}}{\text{Jumlah Penduduk yang Bekerja (PB)}} \times 100\%$$
   - Status Informal BPS: Berusaha Sendiri, Berusaha dibantu buruh tidak tetap/tak dibayar, Pekerja bebas pertanian, Pekerja bebas nonpertanian, Pekerja keluarga/tidak dibayar.
   - Status Formal BPS: Berusaha dibantu buruh tetap/dibayar, Buruh/Karyawan/Pegawai.

7. **Indikator Partisipasi Pendidikan** `[slide 58-70]`:
   - **Angka Partisipasi Sekolah (APS)** `[slide 63-64]`:
     $$\text{APS}_a = \frac{\text{Jumlah penduduk kelompok usia } a \text{ yang bersekolah (jenjang apapun)}}{\text{Jumlah seluruh penduduk kelompok usia } a} \times 100\%$$
     Kelompok usia baku BPS: 7–12 tahun (SD), 13–15 tahun (SMP), 16–18 tahun (SMA), 19–24 tahun (PT).
   - **Angka Partisipasi Kasar (APK)** `[slide 66-67]`:
     $$\text{APK}_j = \frac{\text{Jumlah seluruh murid terdaftar di jenjang } j \text{ (usia berapapun)}}{\text{Jumlah penduduk kelompok usia resmi jenjang } j} \times 100\%$$
     *(Nilai dapat melebihi 100% karena pendaftaran usia dini, terlambat sekolah, atau tinggal kelas).*
   - **Angka Partisipasi Murni (APM)** `[slide 69-70]`:
     $$\text{APM}_j = \frac{\text{Jumlah murid terdaftar di jenjang } j \text{ yang berusia resmi jenjang } j}{\text{Jumlah penduduk kelompok usia resmi jenjang } j} \times 100\%$$
     *($\text{APM} \le \text{APK}$, nilai maksimum 100%).*
   - **Angka Melek Huruf (AMH 15+)** `[slide 58-59]`:
     $$\text{AMH}_{15+} = \frac{\text{Jumlah penduduk usia } 15+ \text{ yang dapat membaca & menulis}}{\text{Jumlah seluruh penduduk usia } 15+} \times 100\%$$

---

### C. Pertemuan 10: Indikator Kesehatan & SDGs Tujuan 3
*Rujukan Slide: `Pertemuan 10 Indikator Kesehatan.pptx` [slide 9-48]*

1. **Angka Kematian Ibu (AKI / Maternal Mortality Ratio - MMR)** `[slide 13]`:
   $$\text{AKI} = \frac{\sum \text{Kematian Ibu karena Hamil, Persalinan, atau Nifas (hingga 42 hari)}}{\sum \text{Kelahiran Hidup}} \times 100.000$$
   *Konstanta baku: $K = 100.000$ Kelahiran Hidup.* Target SDG 3.1: $< 70$ per $100.000\text{ KH}$.

2. **Angka Kematian Balita (AKABA / Under-5 Mortality Rate - U5MR)** `[slide 18-19]`:
   $$\text{AKABA} = \frac{D_{0-4 \text{ tahun}}}{P_{0-4 \text{ tahun pada pertengahan tahun}}} \times 1.000$$
   Target SDG 3.2: $\le 25$ per $1.000\text{ KH}$.

3. **Angka Kematian Anak (CMR 1–4 tahun)** `[slide 20-21]`:
   $$\text{AK Anak} = \frac{D_{1-4 \text{ tahun}}}{P_{1-4 \text{ tahun pertengahan tahun}}} \times 1.000$$

4. **Angka Kematian Bayi (AKB / Infant Mortality Rate - IMR)** `[slide 22-23]`:
   $$\text{AKB} = \frac{D_{0 \text{ tahun (0-11 bulan)}}}{\sum \text{Kelahiran Hidup}} \times 1.000$$

5. **Angka Kematian Neonatal (NMR)**:
   Kematian bayi pada 28 hari pertama per $1.000$ Kelahiran Hidup. Target SDG 3.2: $\le 12$ per $1.000\text{ KH}$.

6. **Angka Kesakitan (Morbiditas)**:
   Persentase penduduk yang mengalami keluhan kesehatan yang mengganggu aktivitas sehari-hari (pekerjaan, sekolah, aktivitas rumah tangga) dalam kurun waktu 1 bulan terakhir terhadap total populasi.

---

### D. Pertemuan 11: Indikator Statistik Produksi & Pertanian
*Rujukan Slide: `Pertemuan 11 OSL Indikator Ekonomi (1) Produksi.pdf` [hal. 9-45]*

1. **Produksi Tanaman Pangan (Padi/Palawija)** `[hal. 9-11]`:
   $$\text{Produksi (Ton)} = \text{Luas Panen (Ha)} \times \text{Produktivitas (Ton/Ha)}$$

2. **Produktivitas Rata-rata Wilayah Agregat (Provinsi/Nasional)** `[hal. 11-12]`:
   $$\text{Produktivitas Provinsi} = \frac{\sum_{i=1}^k \text{Luas Panen}_i \times \text{Produktivitas}_i}{\sum_{i=1}^k \text{Luas Panen}_i} = \frac{\text{Total Produksi (Ton)}}{\text{Total Luas Panen (Ha)}}$$
   *(Merupakan hasil BAGI total produksi terhadap total luas panen, bukan hasil kali).*

3. **Formula Survei Ubinan Padi BPS** `[hal. 18-20]`:
   - Ukuran plot ubinan standar: $2,5\text{ m} \times 2,5\text{ m} = 6,25\text{ m}^2$.
   - Luas $1\text{ hektar} = 10.000\text{ m}^2$.
   - Faktor konversi per hektar:
     $$\text{Faktor} = \frac{10.000\text{ m}^2}{6,25\text{ m}^2} = 1.600$$
   - Konversi Hasil Timbangan Ubinan ($B$ dalam kg):
     - $\text{Produktivitas (kg/ha)} = B \times 1.600$
     - $\text{Produktivitas (ku/ha)} = \frac{B \times 1.600}{100} = B \times 16$
     - $\text{Produktivitas (ton/ha)} = \frac{B \times 1.600}{1.000} = B \times 1,6$

4. **Keseimbangan Pasokan Neraca Energi (UU No. 30/2007)** `[hal. 42-45]`:
   $$\text{Pasokan Energi Primer} = \text{Produksi} + \text{Impor} - \text{Ekspor} \pm \text{Perubahan Stok}$$
   *(Impor energi menambah pasokan dalam negeri sehingga bertanda POSITIF).*

5. **Klasifikasi Industri Pengolahan**:
   - Industri Besar & Sedang (IBS): Jumlah tenaga kerja $\ge 20$ orang.
   - Industri Mikro & Kecil (IMK): Jumlah tenaga kerja $1 - 19$ orang.

---

### E. Pertemuan 12: Perdagangan Dalam Negeri & Indikator Harga
*Rujukan Slide: `Pertemuan 12 OSL Indikator Ekonomi (2) Perdagangan&Harga.pdf` [hal. 4-38] & Publikasi IHK BPS 2025*

1. **Margin Perdagangan dan Pengangkutan (MPP)** `[hal. 4-6]`:
   - Tingkat Pelaku Usaha ke-$i$:
     $$\text{MPP}_i = \frac{\text{Nilai Penjualan}_i - \text{Nilai Pembelian}_i}{\text{Nilai Pembelian}_i} \times 100\%$$
   - MPP Total Rantai Distribusi:
     $$\text{MPP Total} = \frac{\text{Harga Jual Konsumen Akhir} - \text{Harga Beli Produsen}}{\text{Harga Beli Produsen}} \times 100\%$$

2. **Indeks Harga Konsumen (Formula Modified Laspeyres)** `[hal. 14]`:
   $$I_n = \frac{\sum_{i=1}^k \left(\frac{P_{ni}}{P_{(n-1)i}}\right) \cdot P_{(n-1)i} Q_{0i}}{\sum_{i=1}^k P_{0i} Q_{0i}} \times 100 = \sum_{i=1}^k \left[ \left(\frac{P_{ni}}{P_{(n-1)i}}\right) \cdot W_{(n-1)i} \right]$$
   di mana:
   - $\frac{P_{ni}}{P_{(n-1)i}}$: Relatif Harga ($RH$) komoditas $i$ pada bulan ke-$n$ terhadap bulan $(n-1)$.
   - $P_{(n-1)i} Q_{0i}$: Nilai Konsumsi ($NK$) komoditas $i$ pada bulan $(n-1)$.
   - $P_{0i} Q_{0i}$: Nilai Konsumsi tahun dasar hasil Survei Biaya Hidup (SBH).
   - Pembaruan Nilai Konsumsi: $NK_{ni} = RH_{ni} \times NK_{(n-1)i}$.

3. **Laju Inflasi Publikasi BPS** `[hal. 19-20]`:
   - Inflasi Bulanan (*month-to-month / m-to-m*):
     $$\text{Inflasi}_{m-to-m} = \frac{IHK_t - IHK_{t-1}}{IHK_{t-1}} \times 100\%$$
   - Inflasi Tahun Kalender (*year-to-date / y-to-d*):
     $$\text{Inflasi}_{y-to-d} = \frac{IHK_t - IHK_{\text{Desember tahun sebelumnya}}}{IHK_{\text{Desember tahun sebelumnya}}} \times 100\%$$
   - Inflasi Tahunan (*year-on-year / y-on-y*):
     $$\text{Inflasi}_{y-on-y} = \frac{IHK_{t, y} - IHK_{t, y-1}}{IHK_{t, y-1}} \times 100\%$$

4. **Nilai Tukar Petani (NTP) & Nilai Tukar Usaha Petani (NTUP)** `[hal. 31-38]`:
   - **NTP**:
     $$\text{NTP} = \frac{I_t \text{ (Indeks Harga yang Diterima Petani)}}{I_b \text{ (Indeks Harga yang Dibayar Petani)}} \times 100$$
     di mana $I_b$ mencakup Indeks Konsumsi Rumah Tangga ($IKRT$) dan Indeks Biaya Produksi & Penambahan Barang Modal ($BPPBM$).
   - **NTUP**:
     $$\text{NTUP} = \frac{I_t}{\text{BPPBM}} \times 100$$
     *(Hanya membandingkan harga hasil produksi dengan biaya sarana produksi/usaha tani).*
   - **Inflasi Perdesaan**:
     $$\text{Inflasi Perdesaan} = \frac{IKRT_t - IKRT_{t-1}}{IKRT_{t-1}} \times 100\%$$

---

### F. Pertemuan 13: Ekspor-Impor, Terms of Trade, & Pariwisata
*Rujukan Slide: `Pertemuan 13 OSL Indikator Ekonomi (3) X-M, KTI, Pariwisata.pdf` [hal. 8-41]*

1. **Neraca Perdagangan & Keterbukaan Ekonomi** `[hal. 8-9]`:
   - Neraca Perdagangan: $\text{Trade Balance} = X - M$
   - Derajat Keterbukaan (*Trade Openness*): $\text{Trade Openness} = \frac{X + M}{\text{PDB}}$

2. **Indeks Spesialisasi Perdagangan (ISP) / Trade Specialisation Ratio (TSR)** `[hal. 10-11]`:
   $$\text{ISP} = \frac{X_i - M_i}{X_i + M_i}$$
   Rentang nilai $-1 \le \text{ISP} \le +1$. Tahapan Siklus Produk:
   - $-1,00 \le \text{ISP} \le -0,50$ : Tahap Pengenalan
   - $-0,50 < \text{ISP} \le 0,00$ : Tahap Substitusi Impor
   - $0,00 < \text{ISP} \le 0,80$ : Tahap Perluasan Ekspor
   - $0,80 < \text{ISP} \le 1,00$ : Tahap Pematangan (Eksportir Murni)

3. **Revealed Comparative Advantage (RCA)** `[hal. 12]`:
   $$\text{RCA} = \frac{X_{ij} / X_j}{X_{iw} / X_w}$$
   - $X_{ij}$: Nilai ekspor komoditi $i$ negara $j$.
   - $X_j$: Total ekspor negara $j$.
   - $X_{iw}$: Nilai ekspor komoditi $i$ dunia.
   - $X_w$: Total ekspor seluruh dunia.
   - $\text{RCA} \ge 1$: Memiliki keunggulan komparatif kuat (di atas rata-rata dunia).
   - $\text{RCA} < 1$: Keunggulan komparatif lemah.

4. **Terms of Trade (ToT)** `[hal. 13-15]`:
   - **Net Barter Terms of Trade (NBToT)**:
     $$\text{NBToT} = \frac{P_x \text{ (Indeks Harga/Unit Value Ekspor)}}{P_m \text{ (Indeks Harga/Unit Value Impor)}} \times 100$$
   - **Gross Barter Terms of Trade (GBToT)**:
     $$\text{GBToT} = \frac{Q_m \text{ (Indeks Kuantitas Impor)}}{Q_x \text{ (Indeks Kuantitas Ekspor)}} \times 100$$
   - **Income Terms of Trade (IToT)** / Kapasitas Impor:
     $$\text{IToT} = \text{NBToT} \times \frac{Q_x}{100} = \frac{P_x \cdot Q_x}{P_m}$$

5. **Statistik Perhotelan & Pariwisata** `[hal. 39-41]`:
   - **Tingkat Penghunian Kamar (TPK)**:
     $$\text{TPK} = \frac{\sum \text{Malam Kamar Terpakai}}{\sum \text{Malam Kamar Tersedia}} \times 100\%$$
   - **Tingkat Pemakaian Tempat Tidur (TPTT)**:
     $$\text{TPTT} = \frac{\sum \text{Malam Tamu}}{\sum \text{Tempat Tidur Tersedia}} \times 100\%$$
   - **Rata-rata Lama Menginap Tamu (RLMT)**:
     $$\text{RLMT} = \frac{\sum \text{Malam Tamu}}{\sum \text{Tamu yang Datang dan Menginap}} \quad (\text{satuan: malam})$$
   - **Rata-rata Tamu per Kamar (RTK)**:
     $$\text{RTK} = \frac{\sum \text{Malam Tamu}}{\sum \text{Malam Kamar Terjual}}$$

---

## 3. Kompilasi Masalah Numerik & Rekonstruksi Ujian Historis

### Kasus 1: Perhitungan Gini Ratio & Kriteria Bank Dunia (Slide 39 Pertemuan 8)
**Tabel Data Slide**:
| Kuintil | Konsumsi (Rp) | Persentase Konsumsi ($p_i$) | Kumulatif Penduduk ($f_i$) | Kumulatif Konsumsi ($Y_i$) | $Y_i + Y_{i-1}$ | $f_i \cdot (Y_i + Y_{i-1})$ |
|---|---|---|---|---|---|---|
| 1 | 50.000 | 0,0719 | 0,2000 | 0,0719 | 0,0719 | 0,0144 |
| 2 | 70.000 | 0,1007 | 0,2000 | 0,1727 | 0,2446 | 0,0489 |
| 3 | 100.000 | 0,1439 | 0,2000 | 0,3165 | 0,4892 | 0,0978 |
| 4 | 125.000 | 0,1799 | 0,2000 | 0,4964 | 0,8129 | 0,1626 |
| 5 | 350.000 | 0,5036 | 0,2000 | 1,0000 | 1,4964 | 0,2993 |
| **Total** | **695.000** | **1,0000** | **1,0000** | - | - | **0,6230** |

- **Kalkulasi Gini**:
  $$G = 1 - \sum f_i (Y_i + Y_{i-1}) = 1 - 0,6230 = \mathbf{0,3770}$$
- **Evaluasi Kriteria Bank Dunia**:
  Pangsa 40% penduduk terbawah ($Q_1 + Q_2$) $= 7,19\% + 10,07\% = \mathbf{17,27\%}$. Karena $17,27\% > 17\%$, maka ketimpangan tergolong **Rendah**.

---

### Kasus 2: Soal Esai 1 Ketenagakerjaan UAS 2022/2023 (Skor 30)
*Rujukan Naskah: `extracted/Soal_UAS_2022-2023.md` [hal. 6-7]*

**Deskripsi Kasus**:
Negara A memiliki 18 juta penduduk (14 juta berusia 15+ tahun, 4 juta berusia < 15 tahun). Dari 14 juta PUK:
- 9 juta Angkatan Kerja
- Bukan Angkatan Kerja: 2 juta sekolah, 2 juta mengurus rumah tangga, 1 juta manula/tanpa kegiatan (Total BAK = 5 juta).
Dari 9 juta Angkatan Kerja:
- Bekerja: 6 juta orang $\ge 35$ jam/minggu, 1 juta orang $< 35$ jam/minggu (Total Bekerja = 7 juta).
- Pengangguran: 1 juta terkena PHK sedang mencari kerja, 500 ribu menyiapkan usaha baru, 500 ribu lulus tes menunggu panggilan kerja (Total Penganggur = 2 juta).

**Pertanyaan & Jawaban Terverifikasi**:
1. Penduduk Usia Kerja (PUK) $= \mathbf{14\text{ juta orang}}$.
2. Jumlah Angkatan Kerja (AK) $= \mathbf{9\text{ juta orang}}$.
3. Jumlah Bukan Angkatan Kerja (BAK) $= 2 + 2 + 1 = \mathbf{5\text{ juta orang}}$.
4. Tingkat Partisipasi Angkatan Kerja (TPAK):
   $$\text{TPAK} = \frac{9}{14} \times 100\% = \mathbf{64,29\%} \quad (64,2857\%)$$
5. Tingkat Pengangguran Terbuka (TPT):
   $$\text{TPT} = \frac{2}{9} \times 100\% = \mathbf{22,22\%} \quad (22,2222\%)$$
6. Jumlah Setengah Penganggur $= \mathbf{1\text{ juta orang}}$ (Tingkat TSP BPS $= \frac{1}{7} \times 100\% = 14,29\%$).

---

### Kasus 3: Soal Esai 2a Ubinan Padi UAS 2022/2023
*Rujukan Naskah: `extracted/Soal_UAS_2022-2023.md` [hal. 7]*

**Deskripsi Kasus**:
Pak Sakri menjadi responden ubinan dengan petak plot standar $2,5\text{ m} \times 2,5\text{ m}$. Hasil timbangan ubinan adalah $4,5\text{ kg}$ Gabah Kering Panen (GKP).

**Kalkulasi Bertahap**:
1. Luas plot ubinan $= 2,5\text{ m} \times 2,5\text{ m} = 6,25\text{ m}^2$.
2. Faktor pengali per hektar $= \frac{10.000\text{ m}^2}{6,25\text{ m}^2} = 1.600$.
3. Produktivitas per hektar:
   $$\text{Produktivitas} = 4,5\text{ kg} \times 1.600 = \mathbf{7.200\text{ kg/ha}} = \mathbf{72\text{ ku/ha}} = \mathbf{7,2\text{ ton/ha}}$$

---

### Kasus 4: Soal Esai 2b.1 Rekonstruksi Tabel Inflasi UAS 2022/2023
*Rujukan Naskah: Gambar Halaman 7 `extracted/img/Soal_UAS_2022-2023_hal_7.png`*

**Tabel Asli Ujian**:
| Uraian | Indikator |
|---|---|
| IHK April 2022 | 109,98 |
| IHK Mei 2022 | 110,42 |
| IHK Desember 2022 | 113,59 |
| IHK April 2023 | 114,74 |
| IHK Mei 2023 | **... (A)** |
| Inflasi *month to month* Mei 2023 (%) | 0,09 |
| Inflasi *year to date* Mei 2023 (%) | **... (B)** |
| Inflasi *year on year* Mei 2023 (%) | **... (C)** |

**Kalkulasi Rekonstruksi**:
1. **Mencari IHK Mei 2023 (A)**:
   $$\text{Inflasi m-to-m} = \frac{\text{IHK Mei 2023} - \text{IHK April 2023}}{\text{IHK April 2023}} \times 100\% = 0,09\%$$
   $$\text{IHK Mei 2023} = 114,74 \times \left(1 + \frac{0,09}{100}\right) = 114,74 \times 1,0009 = \mathbf{114,843266} \approx \mathbf{114,84}$$
2. **Mencari Inflasi *year to date* Mei 2023 (B)**:
   $$\text{Inflasi y-to-d} = \frac{\text{IHK Mei 2023} - \text{IHK Des 2022}}{\text{IHK Des 2022}} \times 100\% = \frac{114,843266 - 113,59}{113,59} \times 100\% = \frac{1,253266}{113,59} \times 100\% = \mathbf{1,10\%}$$
3. **Mencari Inflasi *year on year* Mei 2023 (C)**:
   $$\text{Inflasi y-on-y} = \frac{\text{IHK Mei 2023} - \text{IHK Mei 2022}}{\text{IHK Mei 2022}} \times 100\% = \frac{114,843266 - 110,42}{110,42} \times 100\% = \frac{4,423266}{110,42} \times 100\% = \mathbf{4,01\%}$$
   *(Catatan: IHK April 2022 sebesar 109,98 adalah **distraktor** murni yang tidak digunakan dalam perhitungan).*

---

### Kasus 5: Soal Esai 2b.3 Rekonstruksi Tabel Nilai Tukar Petani UAS 2022/2023
*Rujukan Naskah: Gambar Halaman 7 & 8 `extracted/img/Soal_UAS_2022-2023_hal_7.png` & `hal_8.png`*

**Tabel Asli Ujian**:
| Uraian | April 2023 | Mei 2023 |
|---|---|---|
| NTP | **... (1)** | **... (4)** |
| NTUP | **... (2)** | 110,75 |
| Indeks yang diterima petani ($I_t$) | 128,64 | **... (3)** |
| Indeks yang dibayar petani ($I_b$) | 116,33 | 116,71 |
| IKRT | 116,71 | 117,18 |
| Indeks BPPBM | 115,98 | 116,13 |
| Inflasi perdesaan (%) | 0,14 | **... (5)** |

**Kalkulasi Rekonstruksi**:
1. **NTP April 2023 (1)**:
   $$\text{NTP}_{\text{Apr}} = \frac{I_t}{I_b} \times 100 = \frac{128,64}{116,33} \times 100 = \mathbf{110,58}$$
2. **NTUP April 2023 (2)**:
   $$\text{NTUP}_{\text{Apr}} = \frac{I_t}{\text{BPPBM}} \times 100 = \frac{128,64}{115,98} \times 100 = \mathbf{110,92}$$
3. **$I_t$ Mei 2023 (3)**:
   $$\text{NTUP}_{\text{Mei}} = \frac{I_{t, \text{Mei}}}{\text{BPPBM}_{\text{Mei}}} \times 100 \implies I_{t, \text{Mei}} = \frac{110,75 \times 116,13}{100} = \mathbf{128,613975} \approx \mathbf{128,61}$$
4. **NTP Mei 2023 (4)**:
   $$\text{NTP}_{\text{Mei}} = \frac{128,613975}{116,71} \times 100 = \mathbf{110,20}$$
5. **Inflasi Perdesaan Mei 2023 (5)**:
   Dihitung dari perubahan bulanan Indeks Konsumsi Rumah Tangga ($IKRT$):
   $$\text{Inflasi Perdesaan} = \frac{\text{IKRT}_{\text{Mei}} - \text{IKRT}_{\text{Apr}}}{\text{IKRT}_{\text{Apr}}} \times 100\% = \frac{117,18 - 116,71}{116,71} \times 100\% = \frac{0,47}{116,71} \times 100\% = \mathbf{0,40\%}$$

---

### Kasus 6: Soal Pilihan Ganda Ekspor-Impor UAS 2022/2023 (Nomor 24, 25, 26)
*Rujukan Naskah: `extracted/Soal_UAS_2022-2023.md` [hal. 4]*

1. **Soal 24 (Hitungan Indeks Spesialisasi Perdagangan)**:
   Ekspor karet $X = 350\text{ juta USD}$, impor karet $M = 164\text{ juta USD}$.
   $$\text{ISP} = \frac{X - M}{X + M} = \frac{350 - 164}{350 + 164} = \frac{186}{514} = \mathbf{0,3619} \approx \mathbf{0,36} \quad (\text{Pilihan A})$$
2. **Soal 25 (Tahap Siklus Produk dari Nilai ISP)**:
   Nilai $\text{ISP} = -0,36$. Karena berada dalam rentang $-0,50 \le \text{ISP} \le 0,00$, maka komoditas berada pada **Tahap Substitusi Impor** (Pilihan B).
3. **Soal 26 (Hitungan Terms of Trade)**:
   Indeks harga ekspor $P_x = 105$, indeks harga impor $P_m = 100$.
   $$\text{ToT} = \frac{105}{100} \times 100 = \mathbf{105} \quad (\text{Pilihan C})$$

---

## 4. Analisis Jebakan Dosen (*Professor Pitfalls & Traps*)

Berdasarkan telaah mendalam terhadap karakter soal dosen pengampu (**Dr. Tiodora Hadumaon Siagian**), kami memetakan 10 pola jebakan konseptual dan kalkulasi:

| No | Nama Jebakan | Pola Kesalahan Umum Mahasiswa | Kaidah Statistik BPS yang Benar |
|---|---|---|---|
| 1 | **Pembagi Formula FGT $P_1$ dan $P_2$** | Mahasiswa sering membagi jumlah deviasi kemiskinan dengan $q$ (jumlah orang miskin saja). | Pembagi pada rumus resmi FGT adalah **$n$ (total seluruh penduduk wilayah)**, bukan $q$. Membagi dengan $q$ hanya menghasilkan *income gap ratio* ($I_{gap}$), bukan $P_1$. |
| 2 | **Pembagi Indikator Setengah Penganggur (TSP)** | Mahasiswa membagi jumlah setengah penganggur dengan Angkatan Kerja ($PAK$). | Menurut slide BPS (Pertemuan 9 Slide 17), penyebut untuk Tingkat Setengah Pengangguran (TSP) dan Pekerja Paruh Waktu (TPPW) adalah **$PB$ (Jumlah Penduduk yang Bekerja)**. |
| 3 | **Kriteria Pekerja Paruh Waktu vs Setengah Penganggur** | Mengira semua orang yang bekerja $< 35\text{ jam/minggu}$ otomatis adalah penganggur atau setengah penganggur. | Harus diuji niatnya: Jika bekerja $< 35$ jam dan **tidak mencari pekerjaan tambahan**, statusnya adalah **Pekerja Paruh Waktu (sukarela)**, BUKAN setengah penganggur. |
| 4 | **Definisi Bekerja 1 Jam BPS** | Menganggap orang yang membantu toko orang tua tanpa dibayar selama 2 jam seminggu sebagai "pengangguran" atau "bukan angkatan kerja". | Berdasarkan ICLS 13 & BPS, bekerja **minimal 1 jam berturut-turut** dalam seminggu terakhir (termasuk pekerja keluarga tidak dibayar / *unpaid worker*) sudah resmi berstatus **Bekerja**. |
| 5 | **Sumber Data Inflasi Perdesaan** | Menghitung inflasi perdesaan dari perubahan $I_b$ (Indeks yang Dibayar Petani) atau IHK. | Inflasi perdesaan resmi BPS dihitung secara eksklusif dari perubahan **IKRT (Indeks Konsumsi Rumah Tangga)** petani, karena IKRT mencerminkan biaya hidup harian di perdesaan. |
| 6 | **Distraktor Tabel IHK** | Menggunakan data IHK bulan/tahun yang tidak relevan saat menghitung inflasi tahunan (*year on year*). | Pada tabel soal UAS 2022/2023, dosen menyertakan `IHK April 2022 (109.98)` sebagai pengalih. Inflasi y-on-y Mei 2023 wajib menggunakan **`IHK Mei 2022 (110.42)`**. |
| 7 | **Pembalikan Rumus Gross Barter ToT** | Mengira rumus Gross Barter ToT sama posisinya dengan Net Barter ToT ($\frac{Q_x}{Q_m}$). | Pada Gross Barter ToT, kuantitas impor berada di pembilang: **$\text{GBToT} = \frac{Q_m}{Q_x} \times 100$**. Ini sering dijadikan jebakan pilihan ganda. |
| 8 | **Valuasi Impor: BPS vs SNA 2008 / BPM6** | Mengira impor selalu dinilai dengan CIF di semua neraca ekonomi. | Dalam Statistik Perdagangan Luar Negeri BPS, impor dicatat dengan **CIF**. Namun dalam Neraca Pembayaran (SNA 2008 / BPM6), impor wajib dinilai dengan **FOB** (ongkos angkut dan asuransi dikeluarkan ke neraca jasa). |
| 9 | **Produktivitas Agregat Provinsi** | Mengalikan total produksi dengan total luas panen atau merata-ratakan langsung produktivitas kabupaten tanpa bobot luas panen. | Produktivitas provinsi adalah **hasil BAGI total produksi seluruh kabupaten terhadap total luas panen**, atau rata-rata tertimbang produktivitas berbobot luas panen. |
| 10 | **Basis Konstanta Indikator Mortalitas** | Menghitung Angka Kematian Ibu (AKI) dengan pengali per $1.000$ atau per $10.000$. | AKI wajib menggunakan pengali **$100.000$ Kelahiran Hidup**, sedangkan AKB dan AKABA menggunakan pengali **$1.000$**. |

---

## 5. Arsitektur Verifikasi Python Mandiri & Hasil Uji

Untuk menjamin kepatuhan *Zero Host Mutation* dan integritas *offline*, kami menyusun modul verifikasi komputasional mandiri berbasis standar pustaka Python di:
`/home/alfzki/Documents/OSL/.agents/teamwork/explorer_survey_3/verify_numerical.py`

### Ringkasan Eksekusi Uji Komputasional:
Perintah: `uv run python .agents/teamwork/explorer_survey_3/verify_numerical.py`  
Hasil: **Exit Code 0 (`OK`) — 7 Suite Lulus 100%**

```text
=== 1. VERIFIKASI GINI RATIO (Pertemuan 8 Slide 39) ===
Total Konsumsi: 695,000.00
Persentase Konsumsi: [0.0719, 0.1007, 0.1439, 0.1799, 0.5036]
Kumulatif Pengeluaran (Yi): [0.0719, 0.1727, 0.3165, 0.4964, 1.0]
fi * (Yi + Yi-1): [0.0144, 0.0489, 0.0978, 0.1626, 0.2993]
Sum fi*(Yi + Yi-1): 0.6230
Koefisien Gini: 0.3770
Proporsi 40% Terbawah: 17.27%
Ketimpangan Bank Dunia: Rendah
-> Verifikasi Gini: LULUS

=== 2. VERIFIKASI INDEKS FGT (P0, P1, P2) ===
Garis Kemiskinan (z): 600000.0
Total Populasi (n): 20, Jumlah Penduduk Miskin (q): 5
Poverty Gaps ((z-y)/z): [0.5, 0.3333, 0.25, 0.1667, 0.0833]
P0 (Headcount Index): 0.2500 (25.00%)
P1 (Poverty Gap Index): 0.0667 (6.67%)
P2 (Poverty Severity Index): 0.0229 (2.29%)
-> Verifikasi FGT: LULUS

=== 3. VERIFIKASI ESSAY KETENAGAKERJAAN UAS 2022/2023 ===
Penduduk Usia Kerja (PUK): 14.0 juta
Angkatan Kerja (AK): 9.0 juta
Bukan Angkatan Kerja (BAK): 5.0 juta
Penduduk Bekerja: 7.0 juta
Pengangguran Terbuka: 2.0 juta
TPAK: 64.2857% (64.29%)
TPT: 22.2222% (22.22%)
Jumlah Setengah Pengangguran: 1.0 juta
Tingkat Setengah Penganggur (TSP BPS): 14.2857% (14.29%)
-> Verifikasi Ketenagakerjaan: LULUS

=== 4. VERIFIKASI SURVEI UBINAN PADI ===
Kasus PG 33 (4.0 kg): 6400.0 kg/ha = 64.0 ku/ha
Kasus UAS 2022/2023 Essay 2a (4.5 kg): 7200.0 kg/ha = 72.0 ku/ha = 7.2 ton/ha
-> Verifikasi Ubinan: LULUS

=== 5. VERIFIKASI TABEL INFLASI UAS 2022/2023 ESSAY 2b.1 ===
IHK Mei 2023: 114.843266 (dibulatkan: 114.84)
Inflasi y-to-d Mei 2023: 1.1033% (1.10%)
Inflasi y-on-y Mei 2023: 4.0059% (4.01%)
-> Verifikasi Tabel Inflasi: LULUS

=== 6. VERIFIKASI TABEL NTP UAS 2022/2023 ESSAY 2b.3 ===
April 2023:
  NTP: 110.5820 (110.58)
  NTUP: 110.9157 (110.92)
Mei 2023:
  It (dihitung dari NTUP & BPPBM): 128.613975 (128.61)
  NTP: 110.1996 (110.20)
  Inflasi Perdesaan (dari IKRT): 0.4027% (0.40%)
-> Verifikasi Tabel NTP: LULUS

=== 7. VERIFIKASI PERDAGANGAN LUAR NEGERI & PARIWISATA ===
ISP Karet: 0.3619 (0.36)
ToT: 105.00
TPK Hotel: 60.00%
RLMT Hotel: 2.50 malam
-> Verifikasi Perdagangan & Pariwisata: LULUS

ALL 7 VERIFICATION SUITES PASSED SUCCESSFULLY!
```

---

## 6. Rekomendasi untuk Pembuatan Modul Belajar (Langkah 4) & Bank Soal (Langkah 6)

1. **Format Modul Belajar (`study-teach`)**:
   - Selalu sertakan box peringatan "⚠️ Perhatian / Jebakan Dosen" di setiap sub-bab yang memuat 10 poin jebakan di atas.
   - Cantumkan penurunan rumus matematis lengkap dalam format LaTeX dengan menyertakan interpretasi praktis BPS (contoh: mengapa $P_2$ lebih sensitif terhadap transfer bantuan sosial dibanding $P_1$).
   - Sertakan contoh soal bertahap yang telah diverifikasi dengan skrip Python di atas.
2. **Format Soal Bank Soal (`study-quiz`)**:
   - Sediakan soal rekonstruksi tabel serupa soal UAS 2022/2023 (Tabel IHK dan Tabel NTP) karena terbukti menjadi format soal esai favorit dosen.
   - Masukkan opsi distraktor pada soal pilihan ganda yang secara presisi merefleksikan salah kaprah mahasiswa (misal: membagi TSP dengan Angkatan Kerja, atau menghitung inflasi perdesaan dari $I_b$).
   - Gunakan angka-angka realistis dari data BPS Indonesia (misal PUK ratusan juta, nilai konsumsi ratusan ribu rupiah, IHK dengan tahun dasar 2018=100 atau 2022=100).
