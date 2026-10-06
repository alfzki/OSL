---
tags: [osl, ppt-8, universitas]
chapter: 8
status: draft
points: 8
---

# Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan

> Modul ini diturunkan dari `internal/lessons/chapter-08/*.json`.
> `status: draft` karena belum ada sesi belajar yang tercatat pada `progress/tracker.json`.

## Konsep

### 8.1.1 Konsep Kemiskinan Absolut dan Relatif

- **Seksi**: 8.1 Konsep dan Metodologi Garis Kemiskinan BPS
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 4-13]
- **Cakupan**: COVERED

**Fokus ujian** — Mengidentifikasi perbedaan esensial kemiskinan absolut vs relatif, perilaku garis kemiskinan pasca-pembangunan ekonomi, interpretasi Purchasing Power Parity (\$ PPP) pada SDGs, dan respons indikator terhadap transformasi skala pendapatan.

**Intuisi** — Kemiskinan absolut mengukur batas fisik biologis kelangsungan hidup (garis statis riil), sedangkan kemiskinan relatif mengukur ketertinggalan ekonomi seseorang terhadap standar hidup rata-rata atau median masyarakat sekitarnya (garis dinamis mengikuti proporsi median).

**Definisi BPS** — Kemiskinan absolut adalah ketidakmampuan dari sisi ekonomi untuk memenuhi kebutuhan dasar makanan dan bukan makanan yang diukur dari sisi pengeluaran. Kemiskinan relatif diukur berdasarkan persentase penduduk dengan pendapatan/pengeluaran kurang dari proporsi tertentu (misal 50% atau 60%) terhadap median pendapatan masyarakat.

**Syarat & batas** — Kemiskinan absolut berkurang jika kue ekonomi tumbuh dan dinikmati kelompok di bawah garis kemiskinan riil. Kemiskinan relatif bersifat homogen berderajat nol (scale invariant): jika seluruh pengeluaran/pendapatan dikalikan konstanta positif c, persentase penduduk miskin relatif tidak berubah.

**Rumus** — $$z_{\text{abs}} = \text{konstan riil}, \quad z_{\text{rel}} = k \cdot \text{Median}(Y), \quad 0 < k < 1$$

### 8.1.2 Garis Kemiskinan Makanan dan Non-Makanan

- **Seksi**: 8.1 Konsep dan Metodologi Garis Kemiskinan BPS
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 14-16, 27]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai pembentukan Garis Kemiskinan Total BPS ($GK = GKM + GKNM$), standar kecukupan energi 2.100 kkal (WNPG 1978), paket komoditas perkotaan vs perdesaan, alasan penggunaan pengeluaran sebagai proksi pendapatan, dan disparitas nilai GK antar-wilayah.

**Intuisi** — Garis Kemiskinan (GK) BPS adalah jumlah rupiah pengeluaran minimum per kapita per bulan untuk memenuhi kebutuhan makanan (setara 2.100 kkal per kapita per hari) ditambah kebutuhan dasar bukan makanan minimum esensial seperti perumahan, sandang, pendidikan, dan kesehatan.

**Definisi BPS** — Garis Kemiskinan (GK) merupakan penjumlahan dari Garis Kemiskinan Makanan (GKM) dan Garis Kemiskinan Bukan Makanan (GKNM). Penduduk dengan pengeluaran per kapita bulanan di bawah GK dikategorikan sebagai penduduk miskin.

**Syarat & batas** — GK = GKM + GKNM. GKM berpatokan pada 2.100 kkal dari 52 komoditas makanan rujukan. GKNM mencakup 51 komoditas di perkotaan dan 47 komoditas di perdesaan. Pangsa GKM mendominasi sekitar 73-75% dari total GK.

**Rumus** — $$GK = GKM + GKNM = \sum_{k=1}^{52} P_k \cdot Q_k^* + \sum_{l=1}^m \alpha_l \cdot P_l \cdot Q_l$$

### 8.1.3 Metodologi Cost of Basic Needs BPS

- **Seksi**: 8.1 Konsep dan Metodologi Garis Kemiskinan BPS
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 14, 17-19, 42-43]
- **Cakupan**: COVERED

**Fokus ujian** — Membedakan metodologi Kemiskinan Makro (Susenas, sampel, agregat wilayah) vs Kemiskinan Mikro (PMT/Sensus, 14 kriteria, by name by address), mekanisme targeting bansos, serta kerentanan kelompok Near Poor terhadap guncangan harga.

**Intuisi** — Metodologi Cost of Basic Needs (CBN) menghitung rupiah yang secara riil dibutuhkan oleh kelompok masyarakat yang hidup sedikit di atas garis kemiskinan sementara (populasi rujukan) untuk memenuhi kebutuhan makanan pokok dan bukan makanan esensial.

**Definisi BPS** — Pendekatan Kebutuhan Dasar (Cost of Basic Needs Approach) adalah metode pengukuran kemiskinan dengan menghitung besarnya rupiah yang harus dikeluarkan untuk memenuhi kebutuhan minimum makanan setara 2.100 kkal per hari serta kebutuhan minimum bukan makanan dari populasi rujukan.

**Syarat & batas** — Populasi rujukan didefinisikan sebagai kelompok penduduk yang berada di kelas pengeluaran marjinal (sedikit di atas garis kemiskinan sementara). Susenas menghasilkan estimasi kemiskinan tingkat makro (kabupaten/kota ke atas), bukan basis data sasaran bansos by name by address.

**Rumus** — $$GK = \sum_{k=1}^{52} P_k Q_k^* + \sum_{l=1}^m \alpha_l P_l Q_l, \quad Q_k^* = Q_k \cdot \left(\frac{2.100}{\sum_{j=1}^{52} c_j Q_j}\right)$$

### 8.2.1 Headcount Index P0

- **Seksi**: 8.2 Ukuran Kemiskinan FGT (Foster-Greer-Thorbecke)
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 20-21, 24-28]
- **Cakupan**: COVERED

**Fokus ujian** — Menghitung persentase penduduk miskin ($P_0$), memahami derivasi formal dari kerangka umum FGT ($\alpha=0$), menganalisis disparitas spasial (perkotaan vs perdesaan), dan mengevaluasi kelemahan kritis $P_0$ terhadap aksioma Amartya Sen.

**Intuisi** — Headcount Index P0 mengukur prevalensi atau proporsi penduduk yang hidup di bawah garis kemiskinan terhadap seluruh total populasi.

**Definisi BPS** — Persentase penduduk miskin (Headcount Index / P0) mengukur proporsi penduduk yang memiliki pengeluaran per kapita sebulan di bawah garis kemiskinan.

**Syarat & batas** — 0 <= P0 <= 1 (atau 0% s.d. 100%). P0 mengukur insidensi kemiskinan tetapi tidak sensitif terhadap seberapa jauh pengeluaran orang miskin di bawah GK (insensitif terhadap kedalaman dan keparahan kemiskinan).

**Rumus** — $$P_0 = \frac{q}{n} = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^0$$

### 8.2.2 Poverty Gap Index P1

- **Seksi**: 8.2 Ukuran Kemiskinan FGT (Foster-Greer-Thorbecke)
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 20, 22, 24-29]
- **Cakupan**: COVERED

**Fokus ujian** — Menghitung Poverty Gap Index ($P_1$), dekomposisi $P_1 = P_0 \cdot I_{\text{gap}}$, perhitungan kebutuhan dana fiskal pengentasan kemiskinan ($n \cdot z \cdot P_1$), dan kewaspadaan terhadap kesalahan pembagi $q$ vs $n$.

**Intuisi** — Poverty Gap Index P1 mengukur rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan, dirata-ratakan terhadap seluruh populasi penduduk.

**Definisi BPS** — Indeks Kedalaman Kemiskinan (Poverty Gap Index / P1) adalah ukuran rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan.

**Syarat & batas** — 0 <= P1 <= P0 <= 1. Pembagi rumus adalah n (seluruh populasi), bukan q (jumlah orang miskin). P1 memenuhi Monotonicity Axiom namun melanggar Transfer Axiom.

**Rumus** — $$P_1 = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^1 = P_0 \cdot I_{\text{gap}}, \quad I_{\text{gap}} = \frac{1}{q} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)$$

### 8.2.3 Poverty Severity Index P2

- **Seksi**: 8.2 Ukuran Kemiskinan FGT (Foster-Greer-Thorbecke)
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 20, 23, 24, 26, 29]
- **Cakupan**: COVERED

**Fokus ujian** — Menghitung Poverty Severity Index ($P_2$), memahami mekanisme pembobotan kuadratik terhadap keparahan deprivasi, membuktikan pemenuhan Transfer Axiom dari Amartya Sen, dan menjelaskan hubungan komplementer antara $P_0, P_1,$ dan $P_2$.

**Intuisi** — Poverty Severity Index P2 memberikan bobot lebih berat pada penduduk yang jurang kemiskinannya semakin dalam melalui pengkuadratan rasio gap, sehingga mampu menangkap ketimpangan pengeluaran di antara sesama penduduk miskin.

**Definisi BPS** — Indeks Keparahan Kemiskinan (Poverty Severity Index / P2) memberikan gambaran mengenai penyebaran pengeluaran di antara penduduk miskin.

**Syarat & batas** — 0 <= P2 <= P1 <= P0 <= 1. Memenuhi Monotonicity Axiom dan Transfer Axiom. Pembagi adalah seluruh populasi n.

**Rumus** — $$P_2 = \frac{1}{n} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^2$$

### 8.3.1 Kurva Lorenz dan Koefisien Gini

- **Seksi**: 8.3 Ukuran Ketimpangan Pendapatan dan Pengeluaran
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 33-40]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai pembentukan kurva Lorenz, penghitungan Koefisien Gini metode trapesium diskrit BPS, interpretasi nilai Gini, dan sifat invariansi skala.

**Intuisi** — Kurva Lorenz menggambarkan hubungan kumulatif antara persentase penduduk (sumbu horizontal) dan persentase pengeluaran/pendapatan kumulatif (sumbu vertikal). Garis diagonal 45 derajat adalah line of perfect equality. Semakin melengkung kurva menjauhi diagonal, semakin tinggi ketimpangan. Koefisien Gini adalah rasio area antara diagonal dan kurva Lorenz terhadap seluruh segitiga di bawah diagonal (A / (A+B)).

**Definisi BPS** — Koefisien Gini (Gini Ratio) adalah ukuran kemerataan distribusi pendapatan atau pengeluaran yang dihitung berdasarkan luas wilayah antara garis pemerataan sempurna dan kurva Lorenz riil. Nilai Gini berkisar antara 0 (pemerataan sempurna) hingga 1 (ketimpangan sempurna). BPS menggunakan pengeluaran konsumsi Susenas sebagai proksi pendapatan.

**Syarat & batas** — 0 <= G <= 1. G = 0 berarti pemerataan sempurna (semua orang menikmati pengeluaran yang sama persis). G = 1 berarti satu orang menguasai seluruh pengeluaran. Koefisien Gini bersifat scale invariant (tidak berubah jika seluruh pengeluaran dikalikan konstanta c > 0).

**Rumus** — $$G = 1 - \sum_{i=1}^k (p_i - p_{i-1})(y_i + y_{i-1}) = 1 - \sum_{i=1}^k f_i (Y_i + Y_{i-1})$$

### 8.3.2 Kriteria Ketimpangan Bank Dunia

- **Seksi**: 8.3 Ukuran Ketimpangan Pendapatan dan Pengeluaran
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide/hal. 41-44]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai pembagian distribusi 40-40-20 Bank Dunia, ambang batas 12% dan 17% untuk kelompok 40% terbawah, interpretasi tingkat ketimpangan, dan perbandingannya dengan Koefisien Gini.

**Intuisi** — Bank Dunia membagi penduduk menjadi tiga lapisan: 40% terbawah (kelompok pendapatan rendah), 40% menengah, dan 20% teratas (kelompok pendapatan tinggi). Ukuran ketimpangan difokuskan secara spesifik pada kue ekonomi yang dinikmati oleh 40% kelompok terbawah. Jika kelompok 40% terbawah hanya memperoleh bagian sangat kecil (<12%), ketimpangan dinilai tinggi.

**Definisi BPS** — Kriteria Ketimpangan Bank Dunia mengklasifikasikan tingkat ketimpangan pengeluaran/pendapatan berdasarkan persentase total pengeluaran yang dinikmati oleh 40 persen penduduk berpendapatan terendah: (1) Ketimpangan Tinggi jika pangsa 40% terbawah < 12%; (2) Ketimpangan Sedang jika pangsa 40% terbawah antara 12% dan 17%; (3) Ketimpangan Rendah jika pangsa 40% terbawah > 17%.

**Syarat & batas** — Ambang batas Bank Dunia dihitung dari kuintil 1 + kuintil 2 (Q1 + Q2) atau desil 1 s.d. 4 (D1 + D2 + D3 + D4). Nilai batas pemisah kritis adalah 12% dan 17%.

**Rumus** — $$\text{Pangsa 40\% Terbawah} = p_1 + p_2 = Y_2 \times 100\%, \quad \text{Tingkat} = \begin{cases} \text{Tinggi}, & < 12\% \\ \text{Sedang}, & 12\% \le \text{Pangsa} \le 17\% \\ \text{Rendah}, & > 17\% \end{cases}$$

## Contoh Hitung

### 8.1.1 — Konsep Kemiskinan Absolut dan Relatif

Terdapat data pengeluaran per kapita bulanan untuk 10 orang penduduk (dalam ribuan rupiah): [200, 250, 300, 350, 400, 500, 600, 700, 800, 1000]. Jika Garis Kemiskinan Absolut z_abs = 380 ribu rupiah dan Garis Kemiskinan Relatif z_rel = 70% dari median pengeluaran, tentukan jumlah dan persentase penduduk miskin absolut dan relatif.

| Individu | Pengeluaran (ribu Rp) |
|---|---|
| 1 | 200 |
| 2 | 250 |
| 3 | 300 |
| 4 | 350 |
| 5 | 400 |
| 6 | 500 |
| 7 | 600 |
| 8 | 700 |
| 9 | 800 |
| 10 | 1000 |

**Penyelesaian**

1. Kemiskinan Absolut (z_abs = 380): Penduduk dengan pengeluaran < 380 adalah individu 1, 2, 3, 4 (q = 4 orang). Prevalensi P0_abs = (4 / 10) * 100% = 40%.
2. Median data genap (n=10): Median = (400 + 500) / 2 = 450 ribu rupiah.
3. Garis Kemiskinan Relatif: z_rel = 0.70 * 450 = 315 ribu rupiah.
4. Kemiskinan Relatif (z_rel = 315): Penduduk dengan pengeluaran < 315 adalah individu 1, 2, 3 (q = 3 orang). Prevalensi P0_rel = (3 / 10) * 100% = 30%.

**Hasil verifikasi** — `Absolut=4 (40%), Relatif=3 (30%)`

### 8.1.2 — Garis Kemiskinan Makanan dan Non-Makanan

Di suatu kabupaten pada September 2021, Garis Kemiskinan Makanan dihitung sebesar Rp367.000 per kapita per bulan dan Garis Kemiskinan Bukan Makanan sebesar Rp133.000 per kapita per bulan. Sebuah keluarga dengan 5 anggota rumah tangga memiliki total pengeluaran konsumsi bulanan Rp2.300.000. Tentukan GK total, pangsa GKM, pengeluaran per kapita sebulan, dan status kemiskinan keluarga tersebut.

| Komponen | Nilai (Rp) |
|---|---|
| GKM | 367.000 |
| GKNM | 133.000 |
| Anggota Rumah Tangga (ART) | 5 orang |
| Total Pengeluaran RT | 2.300.000 |

**Penyelesaian**

1. GK Total = GKM + GKNM = 367.000 + 133.000 = Rp500.000 per kapita per bulan.
2. Pangsa GKM = (367.000 / 500.000) * 100% = 73,4%.
3. Pengeluaran per kapita sebulan = 2.300.000 / 5 = Rp460.000.
4. Karena pengeluaran per kapita Rp460.000 < GK Rp500.000, maka keluarga tersebut berstatus Miskin.

**Hasil verifikasi** — `GK=Rp500,000, Pangsa GKM=73.4%, Pengeluaran/kapita=Rp460,000, Status=Miskin`

### 8.1.3 — Metodologi Cost of Basic Needs BPS

Suatu survei verifikasi keluarga pra-sejahtera menguji rumah tangga Bapak Joko berdasarkan kriteria kemiskinan mikro BPS. Dari hasil observasi diperoleh 13 dari 14 indikator kekurangan terpenuhi (ambang batas miskin mikro adalah minimal 9 kriteria). Tentukan status kemiskinan mikro keluarga tersebut.

| Indikator Mikro | Standar Miskin | Hasil Observasi | Terpenuhi? |
|---|---|---|---|
| Luas Lantai | < 8 m2/kapita | 6 m2/kapita | Ya |
| Jenis Lantai | Tanah/Bambu murah | Tanah | Ya |
| Bahan Bakar | Kayu/Arang/Minyak | Kayu bakar | Ya |
| Fasilitas BAB | Bersama/Tidak ada | Bersama | Ya |
| Sumber Air | Tak terlindung | Sumur terbuka | Ya |
| Total Terpenuhi | - | 13 dari 14 | 13 (>= 9) |

**Penyelesaian**

1. Evaluasi kriteria mikro: Sebanyak 13 dari 14 kriteria terpenuhi.
2. Berdasarkan standar perlindungan sosial BPS, rumah tangga dengan minimal 9 kriteria terpenuhi dikategorikan miskin.
3. Karena 13 >= 9, maka keluarga Bapak Joko diklasifikasikan sebagai Miskin (Layak Menerima Bansos).

**Hasil verifikasi** — `13 kriteria, Status=Miskin (Layak Menerima Bansos)`

### 8.2.1 — Headcount Index P0

Dalam suatu survei sampel di sebuah desa berpopulasi n = 20 orang, tercatat data pengeluaran per kapita bulanan (dalam ribuan rupiah): [280, 310, 350, 420, 480, 520, 550, 580, 600, 620, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200]. Jika Garis Kemiskinan ditetapkan z = 500 ribu rupiah, hitunglah jumlah orang miskin (q) dan nilai Headcount Index (P0).

| Kelompok | Pengeluaran (ribu Rp) | Jumlah Penduduk |
|---|---|---|
| y_i < 500 | 280, 310, 350, 420, 480 | 5 orang |
| y_i >= 500 | 520, 550, ..., 1200 | 15 orang |
| Total | - | 20 orang |

**Penyelesaian**

1. Garis kemiskinan z = 500 ribu rupiah.
2. Identifikasi penduduk dengan y_i < 500: 280, 310, 350, 420, 480. Diperoleh q = 5 orang miskin.
3. Total populasi n = 20 orang.
4. Headcount Index P0 = q / n = 5 / 20 = 0,25 (atau 25%).

**Hasil verifikasi** — `q=5 orang, P0=0.25 (atau 25%)`

### 8.2.2 — Poverty Gap Index P1

Sebuah komunitas terdiri dari n = 5 orang dengan pengeluaran per kapita sebulan masing-masing (dalam ribuan rupiah): Y = [300, 400, 450, 700, 900]. Jika Garis Kemiskinan ditetapkan z = 600 ribu rupiah, hitunglah: 1) Nilai Poverty Gap Index (P1), 2) Total dana minimum per bulan yang dibutuhkan untuk mengentaskan seluruh penduduk miskin tersebut tepat ke garis kemiskinan.

| Individu | Pengeluaran (ribu Rp) | Miskin? | Shortfall (z - y_i) | Normalized Gap (z - y_i)/z |
|---|---|---|---|---|
| 1 | 300 | Ya | 300 | 0,500 |
| 2 | 400 | Ya | 200 | 0,333 |
| 3 | 450 | Ya | 150 | 0,250 |
| 4 | 700 | Tidak | 0 | 0 |
| 5 | 900 | Tidak | 0 | 0 |
| Total | - | q=3 | Rp650.000 | 1,0833 |

**Penyelesaian**

1. Garis kemiskinan z = 600 ribu rupiah. Penduduk miskin adalah individu 1, 2, 3 (q = 3 orang, n = 5 orang).
2. Rasio kesenjangan (normalized poverty gap):
   - Individu 1: (600 - 300)/600 = 0,5000
   - Individu 2: (600 - 400)/600 = 0,3333
   - Individu 3: (600 - 450)/600 = 0,2500
3. Jumlah rasio gap = 0,5000 + 0,3333 + 0,2500 = 1,0833.
4. Poverty Gap Index P1 = (1 / n) * 1,0833 = 1,0833 / 5 = 0,2167 (atau 21,67%).
5. Total shortfall dana = (300 + 200 + 150) ribu rupiah = Rp650.000.

**Hasil verifikasi** — `P1=0.2167; Total Transfer=Rp650,000`

### 8.2.3 — Poverty Severity Index P2

Suatu wilayah berpopulasi n = 5 orang memiliki garis kemiskinan z = Rp600.000. Data pengeluaran per kapita sebulan 5 orang tersebut adalah: Y = [300.000, 400.000, 450.000, 750.000, 900.000]. Hitunglah: 1) Kuadrat rasio kesenjangan masing-masing penduduk miskin, 2) Nilai Poverty Severity Index (P2).

| Individu | Pengeluaran (Rp) | Miskin? | Gap (z - y_i)/z | Kuadrat Gap ((z - y_i)/z)^2 |
|---|---|---|---|---|
| 1 | 300.000 | Ya | 300.000/600.000 = 0,5000 | (0,5000)^2 = 0,2500 |
| 2 | 400.000 | Ya | 200.000/600.000 = 0,3333 | (0,3333)^2 = 0,1111 |
| 3 | 450.000 | Ya | 150.000/600.000 = 0,2500 | (0,2500)^2 = 0,0625 |
| 4 | 750.000 | Tidak | 0 | 0 |
| 5 | 900.000 | Tidak | 0 | 0 |
| Total | - | q=3 | 1,0833 | 0,4236 |

**Penyelesaian**

1. Garis kemiskinan z = Rp600.000. Penduduk miskin adalah individu 1, 2, 3 (q = 3 orang, n = 5 orang).
2. Menghitung kuadrat normalized gap:
   - Individu 1: ((600.000 - 300.000)/600.000)^2 = (0,5000)^2 = 0,2500
   - Individu 2: ((600.000 - 400.000)/600.000)^2 = (0,3333)^2 = 0,1111
   - Individu 3: ((600.000 - 450.000)/600.000)^2 = (0,2500)^2 = 0,0625
3. Jumlah kuadrat gap = 0,2500 + 0,1111 + 0,0625 = 0,4236.
4. Nilai Poverty Severity Index P2 = (1 / n) * 0,4236 = 0,4236 / 5 = 0,0847.

**Hasil verifikasi** — `P2=0.0847`

### 8.3.1 — Kurva Lorenz dan Koefisien Gini

Diberikan data konsumsi menurut 5 kelompok kuintil penduduk (masing-masing 20% penduduk): Kuintil 1 = 50.000, Kuintil 2 = 70.000, Kuintil 3 = 100.000, Kuintil 4 = 125.000, Kuintil 5 = 350.000. Hitunglah total konsumsi, proporsi konsumsi per kuintil, kumulatif konsumsi (Y_i), luas trapesium masing-masing kelas, dan Koefisien Gini BPS menggunakan formula pendekatan trapesium diskrit.

| Kuintil | Konsumsi (Rp) | Persentase Konsumsi (p_i) | Persentase Penduduk (f_i) | Kumulatif Konsumsi (Y_i) | Kumulatif Penduduk | Y_i + Y_{i-1} | f_i * (Y_i + Y_{i-1}) |
|---|---|---|---|---|---|---|---|
| 1 | 50.000 | 0,0719 | 0,2000 | 0,0719 | 0,2000 | 0,0719 | 0,0144 |
| 2 | 70.000 | 0,1007 | 0,2000 | 0,1727 | 0,4000 | 0,2446 | 0,0489 |
| 3 | 100.000 | 0,1439 | 0,2000 | 0,3165 | 0,6000 | 0,4892 | 0,0978 |
| 4 | 125.000 | 0,1799 | 0,2000 | 0,4964 | 0,8000 | 0,8129 | 0,1626 |
| 5 | 350.000 | 0,5036 | 0,2000 | 1,0000 | 1,0000 | 1,4964 | 0,2993 |
| Total | 695.000 | 1,0000 | 1,0000 | - | - | - | 0,6230 |

**Penyelesaian**

1. Total konsumsi = 50.000 + 70.000 + 100.000 + 125.000 + 350.000 = 695.000.
2. Hitung persentase konsumsi p_i:
   - p_1 = 50.000 / 695.000 = 0,0719
   - p_2 = 70.000 / 695.000 = 0,1007
   - p_3 = 100.000 / 695.000 = 0,1439
   - p_4 = 125.000 / 695.000 = 0,1799
   - p_5 = 350.000 / 695.000 = 0,5036
3. Hitung kumulatif konsumsi Y_i:
   - Y_1 = 0,0719
   - Y_2 = 0,0719 + 0,1007 = 0,1727
   - Y_3 = 0,1727 + 0,1439 = 0,3165
   - Y_4 = 0,3165 + 0,1799 = 0,4964
   - Y_5 = 0,4964 + 0,5036 = 1,0000
4. Hitung suku trapesium f_i * (Y_i + Y_{i-1}) dengan f_i = 0,2000:
   - Kelas 1: 0,2000 * (0,0719 + 0) = 0,0144
   - Kelas 2: 0,2000 * (0,1727 + 0,0719) = 0,2000 * 0,2446 = 0,0489
   - Kelas 3: 0,2000 * (0,3165 + 0,1727) = 0,2000 * 0,4892 = 0,0978
   - Kelas 4: 0,2000 * (0,4964 + 0,3165) = 0,2000 * 0,8129 = 0,1626
   - Kelas 5: 0,2000 * (1,0000 + 0,4964) = 0,2000 * 1,4964 = 0,2993
5. Jumlah luas area di bawah kurva Lorenz = 0,0144 + 0,0489 + 0,0978 + 0,1626 + 0,2993 = 0,6230.
6. Koefisien Gini: G = 1 - 0,6230 = 0,3770.

**Hasil verifikasi** — `Total=695000, SumTrapezoid=0.6230, Gini=0.3770`

### 8.3.2 — Kriteria Ketimpangan Bank Dunia

Berdasarkan data kuintil konsumsi pada Slide 39 (Q1 = 50.000, Q2 = 70.000, Q3 = 100.000, Q4 = 125.000, Q5 = 350.000; total = 695.000), hitunglah persentase pengeluaran yang dinikmati oleh 40% penduduk terbawah, 40% penduduk menengah, dan 20% penduduk teratas, lalu klasifikasikan tingkat ketimpangan menurut kriteria Bank Dunia.

| Kelompok Penduduk | Kuintil Termasuk | Total Konsumsi (Rp) | Persentase Konsumsi (%) | Kriteria Bank Dunia |
|---|---|---|---|---|
| 40% Terbawah | Q1 + Q2 | 120.000 | 17,27% | > 17% -> Rendah |
| 40% Menengah | Q3 + Q4 | 225.000 | 32,37% | - |
| 20% Teratas | Q5 | 350.000 | 50,36% | - |
| Total | Q1 s.d. Q5 | 695.000 | 100,00% | - |

**Penyelesaian**

1. Total konsumsi populasi = 50.000 + 70.000 + 100.000 + 125.000 + 350.000 = 695.000.
2. Konsumsi 40% penduduk terbawah (Q1 + Q2) = 50.000 + 70.000 = 120.000.
3. Pangsa pengeluaran 40% terbawah = (120.000 / 695.000) * 100% = 17,266...% ≈ 17,27%.
4. Evaluasi kriteria Bank Dunia:
   - < 12% : Ketimpangan Tinggi
   - 12% s.d. 17% : Ketimpangan Sedang
   - > 17% : Ketimpangan Rendah
5. Karena 17,27% > 17,0%, maka distribusi pengeluaran berada pada kategori Ketimpangan Rendah.

**Hasil verifikasi** — `Bottom40_Pct=17.27%, Category=Rendah`

## Jebakan Ujian

**8.1.1 — Transformasi skala seragam terhadap kemiskinan relatif**

- Jebakan: Menganggap kenaikan pendapatan 20% seragam untuk semua warga menurunkan tingkat kemiskinan relatif.
- Strategi aman: Ingat bahwa median ikut naik 20% sehingga garis relatif naik proporsional; persentase kemiskinan relatif tetap tidak berubah.

**8.1.1 — Tertukar Konversi Nominal vs Purchasing Power Parity (PPP)**

- Jebakan: Mengalikan garis kemiskinan global \$2.15 per hari langsung dengan kurs pasar valuta asing dolar AS.
- Strategi aman: Konversi wajib menggunakan faktor konversi PPP yang dihitung Bank Dunia/ICP untuk menstandarkan daya beli sekeranjang barang pokok.

**8.1.2 — Memasukkan atau tidaknya rokok ke dalam GKM BPS**

- Jebakan: Mengira rokok kretek filter dikeluarkan dari GKM karena bukan makanan sehat.
- Strategi aman: Rokok kretek filter secara faktual masuk ke dalam GKM dan menjadi komoditas penyumbang terbesar kedua setelah beras di perkotaan dan perdesaan.

**8.1.2 — Menilai kemiskinan berdasarkan total pengeluaran RT, bukan per kapita**

- Jebakan: Membandingkan total pengeluaran keluarga langsung dengan nilai Garis Kemiskinan.
- Strategi aman: Total pengeluaran rumah tangga wajib dibagi dengan jumlah anggota rumah tangga (ART) terlebih dahulu untuk memperoleh pengeluaran per kapita sebelum dibandingkan dengan GK.

**8.1.3 — Kesalahan Kebijakan Penyaluran Bansos berbasis data makro Susenas**

- Jebakan: Menggunakan angka atau sampel data Susenas BPS untuk membagikan paket sembako kepada penduduk miskin by name by address.
- Strategi aman: Susenas adalah survei sampel untuk estimasi makro dan tidak menyimpan by name by address lengkap; untuk penyaluran bansos mikro wajib digunakan basis data sensus/registrasi (Regsosek/DTKS).

**8.1.3 — Mengabaikan Karakteristik Penduduk Near Poor**

- Jebakan: Menganggap penurunan P0 secara otomatis menyelesaikan kerentanan kemiskinan secara permanen.
- Strategi aman: Perhatikan bahwa banyak penduduk keluar dari kemiskinan hanya berada tipis di atas GK (kelompok rentan/near poor) yang dapat kembali jatuh miskin akibat sedikit kenaikan inflasi pangan.

**8.2.1 — Kesalahan Pembagi Populasi (n vs q atau angkatan kerja)**

- Jebakan: Membagi jumlah orang miskin q dengan jumlah kepala keluarga atau angkatan kerja.
- Strategi aman: Pembagi wajib seluruh populasi individu (n), baik tua, muda, bekerja, maupun tidak bekerja.

**8.2.1 — Kelemahan Kebijakan Mentas Sesaat (Cream-Skimming Policy)**

- Jebakan: Mengasumsikan bahwa penurunan P0 selalu berarti intervensi sosial berjalan adil bagi yang paling menderita.
- Strategi aman: P0 hanya menghitung orang yang melintasi garis kemiskinan, sehingga rawan dieksploitasi dengan hanya membantu orang yang sedikit di bawah GK (near poor) dan mengabaikan orang yang miskin ekstrem.

**8.2.2 — Jebakan Pembagi q vs n pada formula P1**

- Jebakan: Membagi total normalized poverty gap dengan q (jumlah orang miskin saja).
- Strategi aman: Formula resmi FGT dan BPS mewajibkan pembagian dengan seluruh populasi n. Membagi dengan q hanya menghasilkan Income Gap Ratio (I_gap), bukan Poverty Gap Index (P1).

**8.2.2 — Keterbatasan Aksioma Transfer pada P1**

- Jebakan: Menganggap P1 sensitif terhadap transfer uang antar-penduduk miskin.
- Strategi aman: P1 melanggar Transfer Axiom: jika uang ditransfer dari orang miskin ekstrem ke orang miskin lain (keduanya tetap di bawah GK), total kesenjangan tidak berubah sehingga P1 tetap konstan.

**8.2.3 — Lupa Menguadratkan Rasio Kesenjangan pada perhitungan P2**

- Jebakan: Menjumlahkan deviasi tanpa dikuadratkan terlebih dahulu sehingga malah menghitung P1.
- Strategi aman: Pastikan setiap suku rasio (z - y_i)/z dikuadratkan terlebih dahulu sebelum dijumlahkan dan dibagi total populasi n.

**8.2.3 — Kesesatan Logika 'P0 Turun Berarti Keparahan Kemiskinan Berkurang'**

- Jebakan: Mengira jika angka persentase penduduk miskin P0 berkurang, kondisi kelompok miskin yang tersisa pasti membaik.
- Strategi aman: Jika bantuan pemerintah hanya mentaskan orang yang berada di ambang batas garis kemiskinan, P0 turun tetapi P2 dapat tetap tinggi atau bahkan memperlihatkan ketimpangan yang lebih tajam di antara penduduk miskin ekstrem yang tertinggal.

**8.3.1 — Tertukar antara formula diskrit trapesium BPS dengan luas segitiga**

- Jebakan: Lupa mengurangkan jumlah suku trapesium dari angka 1, atau lupa mengalikan suku trapesium dengan f_i.
- Strategi aman: Ingat bahwa sum f_i * (Y_i + Y_{i-1}) adalah dua kali luas area B di bawah kurva Lorenz; rumus Gini BPS adalah G = 1 - sum f_i * (Y_i + Y_{i-1}).

**8.3.1 — Invariansi Skala Koefisien Gini**

- Jebakan: Mengira jika setiap orang mendapatkan kenaikan pendapatan 20% serempak, koefisien Gini akan berubah.
- Strategi aman: Gini bersifat scale-invariant: jika seluruh pendapatan dikalikan skalar positif c, proporsi konsumsi p_i dan Gini tetap konstan.

**8.3.1 — Keterbatasan Persilangan Kurva Lorenz (Lorenz Crossing)**

- Jebakan: Menyimpulkan distribusi A lebih merata daripada B hanya dari angka Gini ketika kedua kurva Lorenz saling bersilangan.
- Strategi aman: Jika kurva Lorenz saling bersilangan, perbandingan Gini dapat menyesatkan karena distribusi ketimpangan di kelompok bawah dan atas berbeda secara struktural.

**8.3.2 — Terbalik menafsirkan arah persentase Bank Dunia**

- Jebakan: Mengira jika pangsa 40% terbawah < 12%, maka ketimpangannya rendah karena angkanya kecil.
- Strategi aman: Ingat bahwa semakin KECIL pangsa yang dinikmati kelompok terbawah, semakin TINGGI ketimpangannya (< 12% adalah Ketimpangan Tinggi, sedangkan > 17% adalah Ketimpangan Rendah).

**8.3.2 — Tertukar cakupan kuintil pada kelompok 40-40-20**

- Jebakan: Mengambil hanya Kuintil 1 untuk mewakili 40% terbawah.
- Strategi aman: Setiap kuintil mewakili 20% penduduk; 40% terbawah adalah penjumlahan Kuintil 1 dan Kuintil 2 (Q1 + Q2).

## Navigasi

- ← (bab pertama)
- [[02-ketenagakerjaan-dan-pendidikan|→ Pertemuan 9: Ketenagakerjaan dan Pendidikan]]
- [[_formulas|Rumus lengkap OSL]]
- [[_glossary|Glosarium istilah]]

---

[[_MOC|← Back to MOC]]
