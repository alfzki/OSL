---
textbook: Official Statistics Lanjutan (OSL)
chapter: 11
chapter_title: "Pertemuan 11: Statistik Produksi Pertanian dan Industri"
sections: ["11.1 Estimasi Produksi Tanaman Pangan", "11.2 Statistik Industri Pengolahan"]
points: 5
generated: 2026-09-29
---

# Pertemuan 11: Statistik Produksi Pertanian dan Industri

> 《Official Statistics Lanjutan (OSL)》 ｜ 2 Bagian ｜ 5 Poin Konsep ｜ Dibuat: 2026-09-29

## 11.1 Estimasi Produksi Tanaman Pangan `[Pembahasan Mendalam]`

### 11.1.1 Kerangka Sampel Area KSA Padi ⭐

> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 4-18]

> [!info]
> Prinsip dasar Kerangka Sampel Area (KSA), stratifikasi Lahan Baku Sawah (LBS), struktur hierarki segmen (300m x 300m) dan subsegmen (100m x 100m), 9 titik amatan koordinat GPS, klasifikasi fase pertumbuhan padi, serta peramalan luas panen 1-3 bulan ke depan.

> [!quote]
> **Teks Materi Kuliah**
> Metode Pengumpulan Data 'Eye Estimate' bersifat Subjective Measurement digantikan dengan Pengukuran Objective Measurement yaitu Kerangka Sampel Area (KSA). KSA merupakan kumpulan sampel area (segmen) dengan ukuran tertentu dalam suatu wilayah administrasi yang mewakili suatu populasi (area pertanian/sawah). Merupakan kombinasi sistem informasi geografis, penginderaan jauh, teknologi informasi, dan statistika menjadi satu kolaborasi harmonis [slide 10, 13]. Fase pertumbuhan padi hasil pengamatan KSA untuk kerangka sampel subsegmen mencakup Vegetatif awal (V1), Vegetatif akhir (V2), Generatif awal (G1), Generatif akhir (G2), dan Panen [slide 15].

**Intuisi Konsep**　Sebelum KSA diterapkan pada tahun 2018, BPS mengandalkan laporan eye-estimate (pandangan mata) dari ribuan Mantri Tani di tingkat kecamatan. Metode ini rentan terhadap bias subjektif, kepentingan birokrasi, dan seringkali menghasilkan over-estimate luas panen beras nasional hingga jutaan ton. KSA mengubah pendekatan dari 'menilai menurut perkiraan manusia' menjadi 'pengukuran berbasis bukti spasial objektif'. Setiap hamparan sawah dibagi menjadi petak-petak grid koordinat berukuran 300 m x 300 m (segmen). Pada minggu terakhir setiap bulan (tanggal 21-27), petugas lapangan memotret 9 titik tetap di dalam segmen menggunakan smartphone berbasis GPS. Dari foto-foto ini, fase tumbuh padi (vegetatif, generatif, panen, persiapan lahan, atau puso) dicatat secara presisi dan diaudit secara digital oleh server pusat.

**Definisi & Penjelasan Rigor**　### 1. Landasan Metodologis dan Arsitektur Sampling KSA

Kerangka Sampel Area (KSA) dikembangkan melalui kerja sama BPS, BPPT (sekarang BRIN), Kementerian ATR/BPN, Badan Informasi Geospasial (BIG), dan LAPAN (BRIN) untuk memperbaiki estimasi luas panen padi nasional [slide 10, 13].

#### A. Stratifikasi Populasi Lahan Baku Sawah (LBS)
Populasi sampling dibangun menggunakan peta spasial Lahan Baku Sawah (LBS) termutakhir hasil integrasi citra satelit resolusi tinggi. Populasi dikelompokkan ke dalam beberapa stratum berdasarkan intensitas pertanaman dan potensi sawah:
- **Stratum Sawah Irigasi**: Intensitas tanam tinggi (IP 200–300).
- **Stratum Sawah Non-Irigasi / Tadah Hujan**: Intensitas tanam sedang (IP 100–150).
- **Stratum Lahan Bukan Sawah Berpotensi / Lahan Kering**.

#### B. Hierarki Satuan Sampling
1. **Segmen (Sampling Unit)**:
   - Berukuran bujur sangkar $300\text{ m} \times 300\text{ m}$ (luas $90.000\text{ m}^2 = 9\text{ hektar}$) [slide 14].
   - Dipilih secara acak terstratifikasi (*Stratified Systematic Sampling*) dari grid LBS pada masing-masing kabupaten/kota.
2. **Subsegmen (Observation Unit / Grid Amatan)**:
   - Setiap segmen dibagi secara teratur menjadi 9 subsegmen berukuran $100\text{ m} \times 100\text{ m}$ ($10.000\text{ m}^2 = 1\text{ hektar}$) [slide 15, 21].
   - Diberi kode indeks posisi $A_1, A_2, A_3, B_1, B_2, B_3, C_1, C_2, C_3$.
3. **Titik Pengamatan (Sample Point Coordinates)**:
   - Di setiap subsegmen terdapat 1 titik koordinat pengamatan tetap (total 9 titik per segmen).
   - Petugas mengambil foto lapangan dengan kamera ponsel Android ber-GPS pada sudut pandang tertentu dengan batas toleransi radius maksimum 10–15 meter dari titik koordinat nominal [slide 15].

### 2. Klasifikasi Fase Pertumbuhan Padi dan Horison Proyeksi Panen

Setiap titik amatan pada minggu terakhir tiap bulan diklasifikasikan ke dalam salah satu fase biologis [slide 15, 16]:

| Kode Fase | Deskripsi Fase Biologis | Karakteristik Visual Lapangan | Horison Waktu Menuju Panen |
|---|---|---|---|
| **V1** | Vegetatif Awal (1–30 HST) | Semai, pindah tanam, daun muda, rumpun kecil, air sawah terlihat dominan | Panen 3 bulan berikutnya ($t+3$) |
| **V2** | Vegetatif Akhir (31–60 HST) | Anakan maksimal, kanopi daun rimbun hijau pekat menutup permukaan air | Panen 2 bulan berikutnya ($t+2$) |
| **G1** | Generatif Awal (61–90 HST) | Bunting, keluar malai (flowering), tanaman berwarna hijau kekuningan | Panen 2 bulan berikutnya ($t+2$) |
| **G2** | Generatif Akhir (91–105 HST) | Pengisian bulir, malai merunduk, bulir menguning matang fisiologis | Panen 1 bulan berikutnya ($t+1$) |
| **P** | Panen (Harvesting) | Sedang dilakukan pemotongan padi, tumpukan jerami, perontokan | **Panen bulan berjalan ($t$)** |
| **PL** | Persiapan Lahan | Olah tanah, pembajakan, pelumpuran, sawah tergenang tanpa tanaman | Panen 4 bulan berikutnya ($t+4$) |
| **PS** | Puso / Gagal Panen | Tanaman kering/rusak total akibat banjir, kekeringan, atau hama | Tidak menghasilkan panen |
| **BP / BS** | Bukan Padi / Bukan Sawah | Lahan ditanami palawija/tebu atau beralih fungsi bangunan/kolam | Dikeluarkan dari estimasi padi |

### 3. Formulasi Estimasi Luas Panen BPS

Misalkan suatu wilayah administratif (kabupaten/provinsi) memiliki $H$ stratum tutupan lahan sawah. Untuk stratum ke-$h$:
- $A_h$ : Total luas Lahan Baku Sawah (LBS) pada stratum $h$ (hektar).
- $n_h$ : Jumlah segmen sampel terpilih pada stratum $h$.
- $M_i = 9$ : Jumlah titik amatan pada segmen ke-$i$.
- $y_{hij} \in \{0, 1\}$ : Nilai biner indikator apakah titik amatan ke-$j$ pada segmen ke-$i$ stratum $h$ berada pada fase panen (1 jika panen, 0 jika lainnya).

Proporsi titik panen pada stratum $h$ dihitung sebagai:
$$\hat{p}_{h,\text{panen}} = \frac{\sum_{i=1}^{n_h} \sum_{j=1}^{9} y_{hij}}{9 \cdot n_h}$$

Total estimasi luas panen pada periode bulan amatan berjalan ($t$) adalah:
$$\hat{A}_{\text{panen}} = \sum_{h=1}^H A_h \cdot \hat{p}_{h,\text{panen}}$$

Untuk peramalan potensi luas panen 1 bulan ke depan ($t+1$), proporsi dihitung dari titik-titik yang berada pada fase Generatif Akhir (G2):
$$\hat{A}_{\text{panen}}^{(t+1)} = \sum_{h=1}^H A_h \cdot \hat{p}_{h,G2}$$

**Contoh Soal 1 (Pilihan Ganda)**　Dalam pelaksanaan Kerangka Sampel Area (KSA) oleh BPS, pengamatan fase pertumbuhan padi dilakukan pada akhir bulan berjalan. Jika pada akhir bulan Maret seorang pencacah KSA mencatat suatu titik amatan berada pada fase Generatif Akhir (G2: pengisian bulir dan malai menguning), pada bulan apakah titik tersebut diproyeksikan akan memasuki fase Panen (P)?
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 13-16]

- A. Bulan Maret (bulan berjalan)
- B. Bulan April (1 bulan berikutnya)
- C. Bulan Mei (2 bulan berikutnya)
- D. Bulan Juni (3 bulan berikutnya)

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan Bertahap**:
> 1. Berdasarkan siklus biologis padi pada KSA BPS [Slide 15, 16], fase Generatif Akhir (G2) terjadi pada umur 91–105 hari setelah tanam, yaitu masa pematangan bulir gabah.
> 2. Titik amatan yang berada pada fase G2 pada akhir bulan Maret diproyeksikan akan dipanen pada 1 bulan berikutnya, yaitu bulan **April**.
> 3. Sebagai perbandingan:
>    - Fase V1 (Maret) diproyeksikan panen bulan Juni (3 bulan berikutnya).
>    - Fase V2/G1 (Maret) diproyeksikan panen bulan Mei (2 bulan berikutnya).
>    - Fase G2 (Maret) diproyeksikan panen bulan April (1 bulan berikutnya).

**Contoh Soal 2 (Isian/Esai)**　Suatu kabupaten memiliki luas Lahan Baku Sawah (LBS) sebesar 45.000 hektar. Terpilih 200 segmen sampel KSA (masing-masing 9 titik amatan, total 1.800 titik amatan). Pada putaran amatan akhir Mei, tercatat 270 titik berada pada fase Panen (P), 360 titik pada fase Generatif Akhir (G2), dan 450 titik pada fase Vegetatif Akhir/Generatif Awal (V2/G1). Tentukan estimasi luas panen bulan Mei serta proyeksi luas panen bulan Juni dan Juli dalam format: `Mei=X ha, Juni=Y ha, Juli=Z ha`.
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 10-16]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. Total titik amatan = $200 \times 9 = 1.800\text{ titik}$.
> 2. **Luas Panen Bulan Mei**:
>    - Titik panen = 270 titik.
>    - Proporsi panen Mei = $270 / 1.800 = 0,15$ (15%).
>    - Luas Panen Mei = $0,15 \times 45.000\text{ ha} = 6.750\text{ ha}$.
> 3. **Proyeksi Luas Panen Bulan Juni (dari fase G2)**:
>    - Titik G2 = 360 titik.
>    - Proporsi panen Juni = $360 / 1.800 = 0,20$ (20%).
>    - Luas Panen Juni = $0,20 \times 45.000\text{ ha} = 9.000\text{ ha}$.
> 4. **Proyeksi Luas Panen Bulan Juli (dari fase V2/G1)**:
>    - Titik V2/G1 = 450 titik.
>    - Proporsi panen Juli = $450 / 1.800 = 0,25$ (25%).
>    - Luas Panen Juli = $0,25 \times 45.000\text{ ha} = 11.250\text{ ha}$.
> 
> **Verifikasi Kode Python**:
> ```python
> A_1 = 45000
> total_pts = 200 * 9
> p_mei = 270 / total_pts
> luas_mei = p_mei * A_1
> p_jun = 360 / total_pts
> luas_jun = p_jun * A_1
> p_jul = 450 / total_pts
> luas_jul = p_jul * A_1
> print(f'Mei={luas_mei:.0f} ha, Juni={luas_jun:.0f} ha, Juli={luas_jul:.0f} ha')
> # Output: Mei=6750 ha, Juni=9000 ha, Juli=11250 ha
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Hirarki Dimensi Segmen vs Subsegmen**: Sering tertukar antara luas segmen (9 ha / 300m x 300m) dan subsegmen (1 ha / 100m x 100m). Pengamatan fase padi dilakukan di tingkat subsegmen (9 titik amatan per segmen).
> 2. **Jebakan Proyeksi Waktu Panen**: Menjawab bahwa fase vegetatif awal (V1) akan panen 1 bulan kemudian. Siklus hidup padi normal adalah 110–120 hari (~3,5 s.d. 4 bulan). V1 panen 3 bulan ke depan, V2/G1 panen 2 bulan ke depan, dan hanya G2 yang diproyeksikan panen pada bulan berikutnya ($t+1$).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Segmen 300x300m (9 ha), Subsegmen 100x100m (1 ha), 9 titik foto GPS akhir bulan: V1 panen 3 bln, V2/G1 panen 2 bln, G2 panen 1 bln.

*Keterkaitan Konsep: 11.1.2, 11.1.3*

### 11.1.2 Metode Ubinan Produktivitas ⭐

> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 19-27]

> [!info]
> Teknik survei ubinan objektif BPS, dimensi plot bujur sangkar 2,5 m x 2,5 m (6,25 m2), penimbangan Gabah Kering Panen (GKP), turunan matematis multiplier 1.600 (kg/ha), 16 (ku/ha), dan 1,6 (ton/ha), serta rekonstruksi soal UAS 2022/2023 Esai 2a Pak Sakri.

> [!quote]
> **Teks Materi Kuliah**
> Pengukuran dilakukan oleh Petugas BPS Kab/Kota (KSK) dan petugas Dinas Pertanian Kab/Kota (Mantri Tani/KCD/PPL). Frekuensi pengumpulan data: caturwulan/subround. Pengukuran produksi tanaman pangan menggunakan alat ubinan. Untuk satu plot berukuran 2,5 m x 2,5 m. Hasilnya untuk estimasi produksi per hektar [slide 10]. Pelaksanaan Survei Ubinan di lapangan: Alat Ubinan, Memasang Alat, Memanen Plot Ubinan 2,5m x 2,5m, Merontok, Membersihkan, Menimbang [slide 20]. Plot Ubinan: Luas Plot = 6,25 m2. Produktivitas kuintal per ha (GKP) = (3,1 / 100) : (6,25 / 10000) = (3,1 / 100) x (10000 / 6,25) = 3,1 x 16 = 49,60 ku/ha [slide 23].

**Intuisi Konsep**　Bagaimana cara BPS mengetahui produktivitas panen padi tanpa harus menimbang seluruh hasil sawah berhektar-hektar? BPS menerapkan metode ubinan (crop-cutting survey). Petak cuplikan representatif berukuran bujur sangkar 2,5 m x 2,5 m (6,25 m2) dipasang secara acak di lahan sawah yang sedang dipanen. Seluruh rumpun padi di dalam petak dipotong, dirontokkan, dibersihkan dari hampa, lalu ditimbang dengan timbangan gantung terkalibrasi. Karena 1 hektar sama dengan 10.000 m2, maka 1 hektar memuat persis 10.000 / 6,25 = 1.600 petak ubinan, sehingga hasil timbangan dalam kilogram dapat langsung dikonversi menjadi produktivitas per hektar.

**Definisi & Penjelasan Rigor**　### 1. Metodologi Survei Ubinan BPS

Survei Ubinan Padi adalah survei berbasis rumah tangga dan petak sawah yang bertujuan untuk mengukur produktivitas per hektar tanaman pangan secara objektif pada saat panen raya [slide 10, 20].

#### A. Unit Sampling dan Unit Observasi
- **Kerangka Sampel**: Menggunakan subsegmen terpilih hasil amatan Kerangka Sampel Area (KSA) yang berada pada fase siap panen [slide 21].
- **Unit Sampling**: Subsegmen KSA berukuran $100\text{ m} \times 100\text{ m}$ [slide 21].
- **Unit Observasi**: Plot ubinan yang dipasang di petak sawah petani terpilih [slide 21].

#### B. Standar Operasional Prosedur (SOP) Ubinan
Pelaksanaan ubinan di lapangan mengikuti 6 tahapan baku [slide 20]:
1. **Memasang Alat Ubinan**: Alat ubinan berbahan pipa besi/paralon berukuran bujur sangkar $2,5\text{ m} \times 2,5\text{ m}$ dibentangkan di petak sawah. Sudut penempatan ditentukan secara acak menggunakan tabel angka acak (berdasarkan panjang pematang barat dan utara).
2. **Memotong/Memanen**: Seluruh rumpun tanaman padi yang pangkal batangnya berada di dalam batas tali alat ubinan dipotong.
3. **Merontok**: Gabah dirontokkan dari malainya menggunakan perontok manual atau mekanis (*thresher*).
4. **Membersihkan**: Gabah diayak untuk memisahkan kotoran, daun, dan bulir hampa.
5. **Menimbang**: Gabah bersih ditimbang dengan timbangan gantung berskala ketelitian 0,05 kg atau 0,1 kg dalam wujud **Gabah Kering Panen (GKP)**.

### 2. Penurunan Matematis Faktor Pengali (Multiplier) Ubinan

Misalkan:
- Ukuran plot ubinan: sisi bujur sangkar $s = 2,5\text{ meter}$.
- Luas plot ubinan: $A_{\text{plot}} = 2,5\text{ m} \times 2,5\text{ m} = 6,25\text{ m}^2$ [slide 23].
- Luas standar satu hektar: $A_{\text{ha}} = 10.000\text{ m}^2$.
- Hasil timbangan plot ubinan: $b\text{ kg GKP}$.

#### A. Konversi ke Satuan Kilogram per Hektar (kg/ha)
$$\text{Produktivitas (kg/ha)} = \frac{b}{A_{\text{plot}}} \times A_{\text{ha}} = \frac{b}{6,25} \times 10.000 = b \times 1.600$$
Faktor pengali ke kg/ha adalah **1.600** [slide 23].

#### B. Konversi ke Satuan Kuintal per Hektar (ku/ha)
Karena $1\text{ kuintal (ku)} = 100\text{ kg}$:
$$\text{Produktivitas (ku/ha)} = \frac{b \times 1.600}{100} = b \times 16$$
Faktor pengali ke ku/ha adalah **16** [slide 23].

#### C. Konversi ke Satuan Ton per Hektar (ton/ha)
Karena $1\text{ ton} = 1.000\text{ kg}$:
$$\text{Produktivitas (ton/ha)} = \frac{b \times 1.600}{1.000} = b \times 1,6$$
Faktor pengali ke ton/ha adalah **1,6** [slide 11, 23].

| Satuan Target Produktivitas | Formulasi Lengkap | Faktor Pengali ($b = \text{berat kg}$)| Nilai untuk $b = 4,5\text{ kg}$ |
|---|---|---|---|
| **Kilogram per Hektar (kg/ha)** | $\frac{b}{6,25} \times 10.000$ | $b \times 1.600$ | $7.200\text{ kg/ha}$ |
| **Kuintal per Hektar (ku/ha)** | $\frac{b / 100}{6,25 / 10.000}$ | $b \times 16$ | $72,0\text{ ku/ha}$ |
| **Ton per Hektar (ton/ha)** | $\frac{b / 1.000}{6,25 / 10.000}$ | $b \times 1,6$ | $7,2\text{ ton/ha}$ |

### 3. Estimasi Produksi Agregat Tingkat Wilayah

Produksi gabah tingkat kabupaten/kota dihitung sebagai hasil kali estimasi luas panen KSA dengan produktivitas ubinan [slide 11, 12]:
$$P_k = L_k \times Y_k$$
di mana $L_k$ adalah luas panen kabupaten $k$ (ha) dan $Y_k$ adalah produktivitas kabupaten $k$ (ton/ha).

Untuk tingkat provinsi dan nasional, angka produktivitas **bukan rata-rata sederhana**, melainkan rata-rata tertimbang (*weighted average*) [slide 11, 12]:
$$Y_{\text{prov}} = \frac{\sum_{k=1}^K P_k}{\sum_{k=1}^K L_k} = \frac{\sum_{k=1}^K L_k \cdot Y_k}{\sum_{k=1}^K L_k}$$

**Contoh Soal 1 (Pilihan Ganda)**　Dalam suatu survei ubinan komoditas padi dengan plot baku berukuran 2,5 m x 2,5 m, timbangan Gabah Kering Panen (GKP) menunjukkan angka 3,5 kg. Berapakah produktivitas lahan sawah tersebut dalam satuan kuintal per hektar (ku/ha) dan ton per hektar (ton/ha)?
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 23]

- A. 56,0 ku/ha dan 5,6 ton/ha
- B. 56,0 ku/ha dan 0,56 ton/ha
- C. 35,0 ku/ha dan 3,5 ton/ha
- D. 5.600 ku/ha dan 56 ton/ha

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: A**
> Jawaban: **A**.
> 
> **Pembahasan Bertahap**:
> 1. Luas plot ubinan = $2,5\text{ m} \times 2,5\text{ m} = 6,25\text{ m}^2$.
> 2. Multiplier ke 1 hektar ($10.000\text{ m}^2$):
>    - Ke kg/ha: $10.000 / 6,25 = 1.600$.
>    - Ke ku/ha: $1.600 / 100 = 16$.
>    - Ke ton/ha: $1.600 / 1.000 = 1,6$.
> 3. Produktivitas ku/ha = $3,5 \times 16 = 56,0\text{ ku/ha}$.
> 4. Produktivitas ton/ha = $3,5 \times 1,6 = 5,6\text{ ton/ha}$.

**Contoh Soal 2 (Isian/Esai)**　Rekonstruksi UAS OSL 2022/2023 Esai 2a: Pak Sakri memanen sawahnya seluas 2,5 hektar di Sukoharjo. Petugas memasang alat ubinan 2,5 m x 2,5 m secara acak dan memperoleh berat timbangan gabah (GKP) sebesar 4,5 kg. Hitunglah produktivitas sawah dalam ku/ha, ton/ha, dan total produksi gabah (GKP) yang dipanen dari lahan seluas 2,5 ha tersebut. Tuliskan jawaban dalam format: `ku/ha=X, ton/ha=Y, total=Z ton`.
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 20-23]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. Luas plot ubinan = $2,5 \times 2,5 = 6,25\text{ m}^2$.
> 2. Faktor pengali (multiplier):
>    - Multiplier kg/ha = $10.000 / 6,25 = 1.600$.
>    - Multiplier ku/ha = $1.600 / 100 = 16$.
>    - Multiplier ton/ha = $1.600 / 1.000 = 1,6$.
> 3. Produktivitas ku/ha = $4,5 \times 16 = 72,0\text{ ku/ha}$.
> 4. Produktivitas ton/ha = $4,5 \times 1,6 = 7,2\text{ ton/ha}$.
> 5. Total estimasi produksi gabah (GKP) untuk lahan seluas 2,5 ha:
>    $$\text{Total Produksi} = 2,5\text{ ha} \times 7,2\text{ ton/ha} = 18,0\text{ ton}$$
> 
> **Verifikasi Kode Python**:
> ```python
> b = 4.5
> luas_plot = 2.5 * 2.5
> mult_kg = 10000.0 / luas_plot
> kg_ha = b * mult_kg
> ku_ha = kg_ha / 100.0
> ton_ha = kg_ha / 1000.0
> total_prod = ton_ha * 2.5
> print(f'ku/ha={ku_ha:.1f}, ton/ha={ton_ha:.1f}, total={total_prod:.1f} ton')
> # Output: ku/ha=72.0, ton/ha=7.2, total=18.0 ton
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Satuan Kuintal vs Ton**: Sering terjadi kesalahan fatal di mana mahasiswa menghitung $b \times 16 = 72$ kemudian memberi label 72 ton/ha. Ingat: 16 adalah pengali kuintal/ha (ku/ha), sedangkan pengali ton/ha adalah 1,6 (hasilnya 7,2 ton/ha).
> 2. **Rata-rata Produktivitas Provinsi**: Menghitung produktivitas provinsi dengan menjumlahkan produktivitas kabupaten lalu membaginya dengan jumlah kabupaten. Hal ini salah; produktivitas provinsi wajib dihitung sebagai total produksi provinsi dibagi total luas panen provinsi.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Plot ubinan 2,5 x 2,5 m (6,25 m2): kali 1.600 jadi kg/ha, kali 16 jadi ku/ha, kali 1,6 jadi ton/ha.

*Keterkaitan Konsep: 11.1.1, 11.1.3*

### 11.1.3 Survei Konversi Gabah ke Beras SKGB

> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 20-24]

> [!info]
> Alur konversi gabah menjadi beras hasil SKGB 2018 BPS, parameter rendemen GKP ke GKG (83,38%), rendemen GKG ke Beras (64,02%), perhitungan produktivitas beras per hektar, serta dampaknya terhadap estimasi ketersediaan pangan nasional.

> [!quote]
> **Teks Materi Kuliah**
> Hasil ubinan berbentuk GKP dikonversi menjadi GKG dengan angka konversi hasil survei tahun 2005-2007. Sedang dikembangkan metode ubinan untuk pola tanam Jajar Legowo. Dilakukan Survei Konversi Gabah ke Beras (SKGB) pada tahun 2018 [slide 10]. Alur Konversi Gabah Menjadi Beras: 83,38% (GKP ke GKG) dan 64,02% (GKG ke Beras) [slide 22]. Produktivitas kuintal per ha (GKG) = 49,60 x 0,8338 = 41,356 ku/ha dalam bentuk GKG. Konversi GKP ke GKG = 0,8338; Konversi GKG ke beras = 0,6402. Produksi Beras (ku) untuk sawah seluas 1 ha ABCD = (41,356 x 1) x 0,6402 = 26,476 kuintal beras [slide 23].

**Intuisi Konsep**　Mengapa angka konversi SKGB sangat krusial dalam statistik pangan nasional? Ketika survei ubinan dilakukan di sawah, hasil panen yang ditimbang adalah Gabah Kering Panen (GKP) yang masih basah dan belum dapat dikonsumsi. Masyarakat mengonsumsi beras, bukan gabah. Untuk menghitung neraca pangan beras nasional, BPS harus mengetahui secara persis berapa kilogram beras yang dihasilkan dari setiap kilogram gabah basah. Terdapat dua proses penyusutan fisik: penjemuran (pengurangan kadar air dari GKP ke GKG) dan penggilingan (pemisahan sekam dan dedak dari GKG ke beras).

**Definisi & Penjelasan Rigor**　### 1. Definisi dan Latar Belakang SKGB 2018

Untuk menyelaraskan data produksi beras nasional dengan data konsumsi Susenas, BPS bersama Kementerian Pertanian dan instansi terkait memperbarui angka konversi produksi beras melalui **Survei Konversi Gabah ke Beras (SKGB) 2018** [slide 10, 22]. Angka ini menggantikan angka konversi lama hasil survei tahun 2005–2007 yang dinilai sudah tidak mencerminkan efisiensi mesin penggilingan modern (*Rice Milling Unit* / RMU) dan varietas benih padi unggul mutakhir [slide 10].

### 2. Tahapan Rantai Pasok Konversi Gabah ke Beras

Rantai transformasi fisik gabah menuju beras siap konsumsi terdiri atas dua tahapan utama [slide 22, 23]:

```
[Gabah Kering Panen / GKP]
        │
        ▼  (Proses Penjemuran / Pengeringan: Susut Air 16,62%)
[Gabah Kering Giling / GKG]  ── Rendemen: 83,38% (0,8338)
        │
        ▼  (Proses Penggilingan / RMU: Sekam & Dedak 35,98%)
[Beras Siap Konsumsi]       ── Rendemen: 64,02% (0,6402)
```

#### A. Gabah Kering Panen (GKP) ke Gabah Kering Giling (GKG)
- **Definisi Mutu**: GKP memiliki kadar air sekitar $20\% - 25\%$ dan kotoran $>3\%$. Melalui penjemuran alami atau mesin pengering (*dryer*), gabah dikeringkan hingga mencapai kadar air maksimum $14\%$ dan kotoran maksimum $3\%$, yang disebut GKG.
- **Angka Konversi Resmi BPS ($K_{\text{GKP}\to\text{GKG}}$)**: **$83,38\%$** ($0,8338$) [slide 22, 23].
- **Tingkat Susut Bobot**: $100\% - 83,38\% = 16,62\%$ (penguapan air dan pembersihan kotoran ringan).

#### B. Gabah Kering Giling (GKG) ke Beras Giling
- **Definisi Mutu**: GKG dimasukkan ke dalam mesin penggilingan (*huller* dan *polisher*) untuk mengupas kulit luar (sekam $20\% - 22\%$) dan lapisan aleuron (bekatul/dedak $8\% - 10\%$) menghasilkan butir beras sosoh siap masak.
- **Angka Konversi Resmi BPS ($K_{\text{GKG}\to\text{Beras}}$)**: **$64,02\%$** ($0,6402$) [slide 22, 23].
- **Tingkat Susut Penggilingan**: $100\% - 64,02\% = 35,98\%$.

#### C. Angka Konversi Gabungan (Direct Multiplier GKP ke Beras)
$$\begin{aligned}
K_{\text{GKP}\to\text{Beras}} &= K_{\text{GKP}\to\text{GKG}} \times K_{\text{GKG}\to\text{Beras}} \\
&= 0,8338 \times 0,6402 \\
&= 0,53379876 \approx 53,38\%
\end{aligned}$$
Setiap $100\text{ kg}$ gabah basah yang baru dipotong di sawah rata-rata menghasilkan sekitar $53,38\text{ kg}$ beras siap konsumsi.

### 3. Matriks Perbandingan Parameter Konversi

| Bentuk Komoditas | Kadar Air Rata-rata | Rendemen terhadap Tahap Sebelumnya | Rendemen Kumulatif dari GKP | Kegunaan dalam Statistik BPS |
|---|---|---|---|---|
| **Gabah Kering Panen (GKP)** | 20% – 25% | 100% (Titik Awal) | 100% | Satuan hasil timbangan survei ubinan lapangan |
| **Gabah Kering Giling (GKG)** | Maksimal 14% | 83,38% | 83,38% | Standar resmi rilis 'Angka Produksi Padi BPS' |
| **Beras Siap Konsumsi** | Standar Sosoh | 64,02% | 53,38% | Penyusunan Neraca Bahan Makanan (NBM) & stok pangan |

**Contoh Soal 1 (Pilihan Ganda)**　Berdasarkan Survei Konversi Gabah ke Beras (SKGB) 2018 resmi BPS, jika suatu wilayah menghasilkan total 10.000 ton Gabah Kering Giling (GKG), berapakah estimasi total produksi beras siap konsumsi yang dihasilkan dari wilayah tersebut?
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 22, 23]

- A. 8.338 ton beras
- B. 6.402 ton beras
- C. 5.338 ton beras
- D. 7.200 ton beras

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan Bertahap**:
> 1. Data yang diberikan adalah produksi dalam bentuk **Gabah Kering Giling (GKG)** sebesar 10.000 ton.
> 2. Berdasarkan hasil SKGB 2018 [Slide 22], angka konversi dari GKG ke Beras adalah **64,02%** ($0,6402$).
> 3. Maka estimasi produksi beras = $10.000\text{ ton} \times 0,6402 = 6.402\text{ ton beras}$.
> 4. Catatan evaluasi pengecoh:
>    - 8.338 ton adalah jika dikalikan 83,38% (angka konversi GKP ke GKG).
>    - 5.338 ton adalah jika yang diketahui adalah 10.000 ton GKP (dikalikan 53,38%).

**Contoh Soal 2 (Isian/Esai)**　Mengacu pada contoh Slide 23 materi kuliah: Sawah 1 hektar menghasilkan ubinan 2,5 m x 2,5 m sebesar 3,1 kg GKP. Menggunakan angka konversi SKGB 2018 (0,8338 dan 0,6402), hitung produktivitas GKP (ku/ha), produktivitas GKG (ku/ha), dan produksi beras (ku dan kg). Tuliskan jawaban dalam format: `GKP=X ku/ha, GKG=Y ku/ha, Beras=Z ku (W kg)`.
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 22, 23]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. **Produktivitas GKP**:
>    $$\text{ku/ha (GKP)} = 3,1 \times 16 = 49,60\text{ ku/ha}$$
> 2. **Produktivitas GKG** (angka konversi $0,8338$):
>    $$\text{ku/ha (GKG)} = 49,60 \times 0,8338 = 41,35648 \approx 41,356\text{ ku/ha}$$
> 3. **Produksi Beras** untuk 1 hektar (angka konversi $0,6402$):
>    $$\text{Produksi Beras} = 41,35648 \times 0,6402 = 26,47642 \approx 26,476\text{ kuintal beras}$$
>    Dalam satuan kilogram: $26,47642 \times 100 = 2.647,6\text{ kg beras}$.
> 
> **Verifikasi Kode Python**:
> ```python
> b = 3.1
> gkp_ku = b * 16.0
> gkg_ku = gkp_ku * 0.8338
> beras_ku = gkg_ku * 0.6402
> beras_kg = beras_ku * 100.0
> print(f'GKP={gkp_ku:.2f} ku/ha, GKG={gkg_ku:.3f} ku/ha, Beras={beras_ku:.3f} ku ({beras_kg:.1f} kg)')
> # Output: GKP=49.60 ku/ha, GKG=41.356 ku/ha, Beras=26.476 ku (2647.6 kg)
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Mengalikan GKP Langsung dengan 64,02%**: Banyak mahasiswa mengalikan produktivitas ubinan GKP langsung dengan 0,6402. Ini salah fatal karena mengabaikan penyusutan jemur sebesar 16,62%, yang mengakibatkan estimasi beras menjadi overestimate sekitar 20%.
> 2. **Tertukar Rendemen Jemur vs Rendemen Giling**: Menukar angka 83,38% sebagai konversi beras dan 64,02% sebagai konversi gabah. Ingat bahwa rendemen jemur selalu lebih besar (83,38%) karena hanya menghilangkan kadar air, sedangkan penggilingan membuang sekam dan dedak dalam jumlah besar (sehingga rendemennya 64,02%).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　GKP jemur jadi GKG (83,38%), GKG giling jadi Beras (64,02%). Langsung GKP ke Beras = 53,38%.

*Keterkaitan Konsep: 11.1.1, 11.1.2*

## 11.2 Statistik Industri Pengolahan `[Pembahasan Mendalam]`

### 11.2.1 Survei Industri Besar dan Sedang IBS

> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 25-28, 50-51]

> [!info]
> Definisi industri pengolahan/manufaktur BPS, batasan tenaga kerja IBS (20 orang atau lebih), indikator efisiensi rasio input terhadap output, indeks produksi manufaktur, serta integrasi ekstensi EXT-5 formula Nilai Pekerjaan Konstruksi NK = (NP - NS) x %NR.

> [!quote]
> **Teks Materi Kuliah**
> Indeks Produksi Industri Manufaktur Besar Sedang. Industri Pengolahan/Manufaktur adalah usaha yang melakukan kegiatan ekonomi yang mengubah suatu barang dasar secara mekanis, kimia, atau dengan tangan sehingga menjadi barang jadi atau setengah jadi, dan atau barang yang kurang nilainya menjadi barang yang lebih tinggi nilainya [slide 25]. Efisiensi Industri Besar dan Sedang adalah suatu nilai yang menunjukkan perbandingan masukan dan keluaran yang diterima pada industri besar dan sedang yang menunjukkan tingkat penggunaan sumber daya secara minimum guna mencapai hasil yang maksimum. Nilai ini diperoleh dari rasio input terhadap output [slide 26]. Variabel Nilai Pekerjaan Konstruksi: NK = (NP - NS) x %NR. Dimana: NK = Nilai pekerjaan konstruksi, NP = Nilai proyek, NS = Nilai pekerjaan yang disubkontrakkan, %NR = persentase realisasi fisik pekerjaan yang diselesaikan [slide 50].

**Intuisi Konsep**　Mengapa BPS menyurvei IBS secara lengkap (complete enumeration) terpisah dari industri kecil? Industri besar dan sedang (IBS) mencakup hanya sekitar 1-2% dari total jumlah entitas industri di Indonesia, namun mereka menyumbang lebih dari 80-85% total nilai tambah dan ekspor manufaktur nasional. Karakteristik IBS memiliki pembukuan formal terstandar, sehingga BPS dapat mengumpulkan data rinci komposisi input, output, tenaga kerja, upah, dan efisiensi. Selain manufaktur, sektor penyumbang output fisik besar lainnya adalah jasa konstruksi, di mana nilai realisasi output dihitung melalui formula Nilai Pekerjaan Konstruksi (NK) dengan mengurangkan pekerjaan yang disubkontrakkan agar tidak terjadi pencatatan ganda (double counting).

**Definisi & Penjelasan Rigor**　### 1. Landasan Konseptual Statistik Industri Manufaktur BPS

Berdasarkan materi resmi perkuliahan [slide 25–28]:
- **Definisi Industri Pengolahan**: Kegiatan ekonomi yang mentransformasikan barang dasar secara mekanis, kimia, atau tangan menjadi barang baru dengan nilai ekonomis lebih tinggi, termasuk jasa industri (maklun di mana bahan baku disediakan pihak pemesan) dan perakitan (*assembling*) [slide 25].
- **Indikator Penting Industri Manufaktur**: Jumlah perusahaan, jumlah tenaga kerja, produktivitas tenaga kerja, komposisi input, komposisi output, nilai tambah, efisiensi, dan indeks produksi [slide 25].

#### A. Klasifikasi Skala Tenaga Kerja Industri BPS
BPS membagi sektor industri pengolahan ke dalam empat strata tenaga kerja:

| Skala Usaha Industri | Batasan Tenaga Kerja ($L$) | Pendekatan Pencacahan BPS | Sifat Karakteristik Usaha |
|---|---|---|---|
| **Industri Mikro (IM)** | 1 – 4 orang | Survei Sampel (VIMK) | Informal, tanpa badan hukum, padat karya |
| **Industri Kecil (IK)** | 5 – 19 orang | Survei Sampel (VIMK) | Campuran formal-informal, modal terbatas |
| **Industri Sedang (IS)** | 20 – 99 orang | Sensus Lengkap / Direktori IBS | Formal, memiliki izin usaha, pembukuan teratur |
| **Industri Besar (IB)** | 100 orang atau lebih | Sensus Lengkap / Direktori IBS | Korporasi besar, padat modal, teknologi canggih |

Gabungan Industri Besar dan Sedang (**IBS**) didefinisikan sebagai usaha industri dengan tenaga kerja **$\ge 20\text{ orang}$** [slide 25, 27].

### 2. Indikator Kinerja dan Efisiensi IBS

- **Efisiensi Industri**: Suatu nilai yang menunjukkan perbandingan masukan (input antara) dan keluaran (output bruto) [slide 26]:
$$\text{Efisiensi} = \frac{\text{Nilai Input Antara}}{\text{Nilai Output Bruto}}$$
Interpretasi: Jika efisiensi adalah 0,60, maka besarnya biaya input antara yang diperlukan oleh industri untuk menghasilkan setiap satu rupiah output adalah Rp0,60 [slide 27]. Semakin rendah rasio ini, semakin tinggi tingkat efisiensi penggunaan bahan baku dalam proses produksi.
- **Nilai Tambah Bruto (NTB)**: Kontribusi bersih industri terhadap PDB/PDRB:
$$\text{NTB} = \text{Nilai Output} - \text{Biaya Input Antara}$$

### 3. Ekstensi EXT-5: Statistik Konstruksi dan Nilai Pekerjaan Konstruksi (NK)

Sektor konstruksi memiliki karakteristik proyek berbasis kontrak multi-tahun (*multi-year contract*). Untuk mengukur produktivitas dan realisasi pembangunan infrastruktur tanpa terjadi penghitungan ganda (*double counting*), BPS menetapkan formula **Nilai Pekerjaan Konstruksi (NK)** [slide 50]:

$$NK = (NP - NS) \times \%NR$$

di mana:
- $NK$ : Nilai pekerjaan konstruksi yang diselesaikan (Rupiah).
- $NP$ : Nilai kontrak proyek total (*contract value*).
- $NS$ : Nilai pekerjaan yang disubkontrakkan kepada kontraktor spesialis lain (*subcontracted value*).
- $\%NR$ : Persentase realisasi fisik pekerjaan yang diselesaikan dalam periode survei berjalan, dihitung dari:
$$\%NR = \%NR_{\text{akhir periode}} - \%NR_{\text{awal periode}}$$

Pengurangan $NS$ adalah mutlak secara metodologis karena nilai pekerjaan yang disubkontrakkan akan dilaporkan secara mandiri oleh perusahaan subkontraktor yang bersangkutan dalam survei BPS [slide 50].

**Contoh Soal 1 (Pilihan Ganda)**　BPS mempublikasikan indikator efisiensi industri manufaktur besar dan sedang pada suatu provinsi sebesar 0,65. Bagaimanakah interpretasi ekonomi yang tepat dari angka rasio efisiensi 0,65 tersebut menurut standar BPS?
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 25-27]

- A. Perusahaan memperoleh keuntungan bersih sebesar 65% dari total penjualan produk.
- B. Untuk menghasilkan setiap satu rupiah output, industri memerlukan biaya input antara sebesar 0,65 rupiah.
- C. Nilai tambah bruto yang diciptakan perusahaan adalah sebesar 65% dari total input antara.
- D. Produksi industri manufaktur periode berjalan mengalami peningkatan sebesar 65% dibanding tahun dasar.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan Bertahap**:
> 1. Berdasarkan konsep resmi BPS [Slide 26, 27], efisiensi industri manufaktur dihitung dari perbandingan antara input antara terhadap output (rasio Input/Output).
> 2. Nilai efisiensi sebesar 0,65 berarti bahwa untuk menghasilkan setiap satu rupiah nilai keluaran (output), industri tersebut memerlukan masukan (biaya bahan baku dan penolong) sebesar Rp0,65.
> 3. Sisanya, yaitu $1,00 - 0,65 = 0,35$ rupiah (35%), merupakan porsi Nilai Tambah Bruto (NTB) yang menjadi balas jasa faktor produksi (upah tenaga kerja, penyusutan, sewa, dan keuntungan usaha).

**Contoh Soal 2 (Isian/Esai)**　Rekonstruksi Soal Slide 50-51 & EXT-5 Uji E2E Skenario 9: PT Mahakarya memenangkan proyek bernilai kontrak total NP = 10 Miliar Rupiah (Rp10.000.000.000,-). Bagian fondasi disubkontrakkan dengan nilai NS = 2 Miliar Rupiah (Rp2.000.000.000,-). Realisasi fisik yang diselesaikan adalah 80% (%NR = 0,80). Divisi manufaktur IBS milik perusahaan mencatat output Rp5.000.000.000,- dan input Rp3.000.000.000,-. Hitunglah Nilai Pekerjaan Konstruksi (NK), efisiensi IBS, dan Nilai Tambah Bruto (NTB). Tuliskan jawaban dalam format: `NK=X (RpY Miliar), Efisiensi=A, NTB=RpB Miliar`.
> 📎 [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide 50-51]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. **Nilai Pekerjaan Konstruksi (NK)**:
>    $$\begin{aligned}
>    NK &= (NP - NS) \times \%NR \\
>    &= (10.000.000.000 - 2.000.000.000) \times 0,80 \\
>    &= 8.000.000.000 \times 0,80 = 6.400.000.000\text{ Rupiah (6,4 Miliar)}
>    \end{aligned}$$
> 2. **Efisiensi Manufaktur IBS**:
>    $$\text{Efisiensi} = \frac{\text{Input}}{\text{Output}} = \frac{3.000.000.000}{5.000.000.000} = 0,60$$
> 3. **Nilai Tambah Bruto (NTB) Manufaktur IBS**:
>    $$\text{NTB} = \text{Output} - \text{Input} = 5.000.000.000 - 3.000.000.000 = 2.000.000.000\text{ Rupiah (2,0 Miliar)}$$
> 
> **Verifikasi Kode Python**:
> ```python
> np = 10000000000.0
> ns = 2000000000.0
> nr_percent = 0.80
> nk = (np - ns) * nr_percent
> out_man = 5000000000.0
> in_man = 3000000000.0
> eff = in_man / out_man
> ntb = out_man - in_man
> print(f'NK={nk:.1f} (Rp{nk/1e9:.1f} Miliar), Efisiensi={eff:.2f}, NTB=Rp{ntb/1e9:.1f} Miliar')
> # Output: NK=6400000000.0 (Rp6.4 Miliar), Efisiensi=0.60, NTB=Rp2.0 Miliar
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Nilai Subkontrak (NS)**: Seringkali mahasiswa menghitung $NK = NP \times \%NR$ tanpa mengurangkan $NS$. Hal ini salah karena menyebabkan pencatatan ganda atas output pekerjaan yang didelegasikan ke subkontraktor.
> 2. **Jebakan Rasio Efisiensi**: Mengasumsikan rasio efisiensi 0,7 lebih baik daripada 0,5. Rasio efisiensi BPS adalah Input/Output, sehingga angka 0,5 (biaya input 50%) jauh lebih efisien daripada 0,7 (biaya input 70%).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　IBS tenaga kerja >= 20 orang. Efisiensi = Input / Output (makin kecil makin bagus). Konstruksi NK = (NP - NS) x %NR.

*Keterkaitan Konsep: 11.2.2*

### 11.2.2 Survei Industri Mikro dan Kecil IMK

> 📎 [SUPLEMEN] BPS Sensus Ekonomi 2016 & Publikasi Profil IMK BPS

> [!info]
> [SUPLEMEN] Batasan operasional tenaga kerja industri mikro (1-4 orang) dan kecil (5-19 orang) BPS, karakteristik usaha informal manufaktur, metodologi survei sampel VIMK, serta penghitungan nilai tambah dan produktivitas per pekerja.

> [!quote]
> **Teks Materi Kuliah**
> [SUPLEMEN] Berdasarkan Sensus Ekonomi dan Survei Industri Mikro dan Kecil BPS, industri pengolahan dikelompokkan menurut banyaknya tenaga kerja: Industri Mikro memiliki tenaga kerja 1-4 orang, Industri Kecil memiliki tenaga kerja 5-19 orang, Industri Sedang memiliki tenaga kerja 20-99 orang, dan Industri Besar memiliki tenaga kerja 100 orang atau lebih. Survei Industri Mikro dan Kecil (VIMK) dilakukan secara triwulanan dan tahunan dengan metode penarikan sampel berbasis blok sensus.

**Intuisi Konsep**　Sebagian besar unit usaha industri di Indonesia (>98%) berskala mikro dan kecil (seperti pengrajin tempe, konveksi rumahan, pandai besi, kerajinan anyaman). Walaupun skala per unit usahanya kecil, secara agregat mereka menyerap puluhan juta tenaga kerja informal dan menjaga ketahanan ekonomi rakyat dari guncangan krisis. Berbeda dengan IBS yang dicacah lengkap via direktori industri, IMK tersebar luas di lingkungan permukiman tanpa plang usaha resmi atau izin berbadan hukum, sehingga dicacah dengan pendekatan sampling rumah tangga/usaha berbasis blok sensus.

**Definisi & Penjelasan Rigor**　### 1. Landasan Konseptual Industri Mikro dan Kecil (IMK) BPS [SUPLEMEN]

Dalam statistik ekonomi BPS, pembagian industri manufaktur menurut skala usaha berpedoman pada rekomendasi *International Recommendations for Industrial Statistics* (IRIS) PBB dengan penyesuaian kondisi ketenagakerjaan nasional:

```
Sektor Industri Pengolahan (KBLI Golongan Pokok C / 10-33)
├── Industri Mikro (IM)  : 1 s.d. 4 tenaga kerja   (Target Survei VIMK)
├── Industri Kecil (IK)  : 5 s.d. 19 tenaga kerja  (Target Survei VIMK)
├── Industri Sedang (IS) : 20 s.d. 99 tenaga kerja (Target Sensus/Direktori IBS)
└── Industri Besar (IB)  : >= 100 tenaga kerja     (Target Sensus/Direktori IBS)
```

#### A. Batasan Operasional Tenaga Kerja
- **Tenaga Kerja ($L$)**: Seluruh orang yang terlibat secara aktif dalam aktivitas produksi fisik barang, terdiri atas:
  1. Pekerja yang dibayar (buruh tetap, pekerja harian lepas, pekerja borongan).
  2. Pekerja yang tidak dibayar (pemilik usaha yang aktif bekerja, pekerja keluarga tidak dibayar / *unpaid family workers*).
- **Klasifikasi Formal vs Informal**:
  - Usaha mikro hampir seluruhnya berada pada ranah **informal** (tidak berbadan hukum PT/CV/Koperasi, tidak memiliki perizinan formal seperti NIB terverifikasi, dan tidak memisahkan keuangan rumah tangga dengan keuangan usaha).
  - Usaha kecil sebagian telah berizin mikro (NIB perseorangan) atau bermitra sebagai pemasok rantai pasok lokal.

### 2. Matriks Perbandingan IBS vs IMK

| Dimensi Karakteristik | Industri Besar & Sedang (IBS) | Industri Mikro & Kecil (IMK) |
|---|---|---|
| **Batasan Tenaga Kerja** | $\ge 20\text{ orang}$ | $1 - 19\text{ orang}$ (Mikro: 1-4, Kecil: 5-19) |
| **Metode Pendataan BPS** | Sensus / Direktori Lengkap (*Complete Enumeration*) | Survei Sampel Dua Tahap (*Two-stage Sampling*) |
| **Kerangka Sampel** | Direktori Perusahaan IBS BPS (diperbarui berkala) | Blok Sensus dari Sensus Ekonomi (SE) |
| **Pencatatan Keuangan** | Laporan Neraca & Laba Rugi standar akuntansi | Catatan kas sederhana atau ingatan (*recall*) pemilik |
| **Pangsa Jumlah Usaha** | Sekitar $1,0\% - 1,5\%$ dari total usaha industri | Sekitar $98,5\% - 99,0\%$ dari total usaha industri |
| **Pangsa Penyerapan Kerja** | Sekitar $30\% - 35\%$ tenaga kerja industri | Sekitar $65\% - 70\%$ tenaga kerja industri |
| **Pangsa Output & Nilai Tambah** | Dominan ($>80\%$ total nilai tambah industri) | Minoritas ($<20\%$ total nilai tambah industri) |

### 3. Indikator Produktivitas Tenaga Kerja IMK

Produktivitas tenaga kerja menggambarkan kontribusi nilai tambah bruto rata-rata yang diciptakan oleh setiap orang pekerja dalam satuan waktu tertentu:
$$\text{Produktivitas Tenaga Kerja} = \frac{\text{Nilai Tambah Bruto (NTB)}}{L} = \frac{\text{Output Bruto} - \text{Biaya Input Antara}}{L}$$

Karena modal kapital per pekerja (*capital-labor ratio*) pada industri mikro sangat kecil, produktivitas tenaga kerja IMK umumnya jauh lebih rendah dibandingkan pekerja IBS yang didukung mesin-mesin otomatis modern.

**Contoh Soal 1 (Pilihan Ganda)**　Sebuah usaha pengolahan emping melinjo di perdesaan dikelola oleh seorang pemilik, dibantu oleh 2 orang anggota keluarganya tanpa upah, serta 3 orang tetangga yang dipekerjakan sebagai buruh harian kupas melinjo dengan upah harian. Berdasarkan batasan resmi Badan Pusat Statistik (BPS), usaha pengolahan emping tersebut diklasifikasikan ke dalam kategori:
> 📎 [SUPLEMEN] BPS Sensus Ekonomi 2016 & Profil IMK

- A. Industri Mikro, karena buruh berupah hanya ada 3 orang.
- B. Industri Kecil, karena total tenaga kerja yang aktif terlibat adalah 6 orang.
- C. Industri Rumah Tangga Tanpa Badan Usaha, karena melibatkan anggota keluarga.
- D. Industri Sedang, karena mempekerjakan buruh dari luar keluarga.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan Bertahap**:
> 1. Menurut konsep statistik BPS, jumlah tenaga kerja dihitung dari **seluruh orang yang terlibat aktif** dalam kegiatan proses produksi, baik pekerja yang dibayar maupun pekerja keluarga yang tidak dibayar (*unpaid family worker*).
> 2. Total tenaga kerja pada usaha emping melinjo tersebut adalah:
>    $$L = 1\text{ (pemilik)} + 2\text{ (keluarga tanpa upah)} + 3\text{ (buruh berupah)} = 6\text{ orang}$$
> 3. Berdasarkan kriteria skala tenaga kerja BPS:
>    - Industri Mikro: $1 - 4\text{ orang}$.
>    - Industri Kecil: $5 - 19\text{ orang}$.
> 4. Karena $L = 6\text{ orang}$ berada dalam rentang $5 - 19\text{ orang}$, maka usaha tersebut diklasifikasikan sebagai **Industri Kecil**.

**Contoh Soal 2 (Isian/Esai)**　Pencacahan VIMK mencatat data 4 usaha pengolahan: Usaha A (L=3, Out=15jt, In=9jt); Usaha B (L=8, Out=60jt, In=36jt); Usaha C (L=15, Out=120jt, In=75jt); Usaha D (L=25, Out=250jt, In=150jt). Tentukan jumlah usaha yang masuk cakupan target IMK serta nilai tambah dan produktivitas per pekerja untuk masing-masing usaha IMK tersebut. Format jawaban: `IMK=X usaha; A:NT=Yjt,Prod=Zjt, B:NT=Ujt,Prod=Vjt, C:NT=Wjt,Prod=Kjt`.
> 📎 [SUPLEMEN] BPS Profil IMK 2024

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah analisis:
> 1. **Klasifikasi Tenaga Kerja BPS**:
>    - Usaha A ($L=3$): Industri Mikro ($1 - 4$ orang) $\implies$ Masuk IMK.
>    - Usaha B ($L=8$): Industri Kecil ($5 - 19$ orang) $\implies$ Masuk IMK.
>    - Usaha C ($L=15$): Industri Kecil ($5 - 19$ orang) $\implies$ Masuk IMK.
>    - Usaha D ($L=25$): Industri Sedang ($20 - 99$ orang) $\implies$ Tidak masuk IMK (masuk Direktori IBS).
>    Total usaha masuk target IMK = **3 usaha**.
> 
> 2. **Nilai Tambah (NT) dan Produktivitas Tenaga Kerja**:
>    - **Usaha A**:
>      $$NT_A = 15 - 9 = 6\text{ Juta Rp}$$
>      $$\text{Produktivitas}_A = \frac{6\text{ Juta}}{3\text{ orang}} = 2,0\text{ Juta Rp/pekerja}$$
>    - **Usaha B**:
>      $$NT_B = 60 - 36 = 24\text{ Juta Rp}$$
>      $$\text{Produktivitas}_B = \frac{24\text{ Juta}}{8\text{ orang}} = 3,0\text{ Juta Rp/pekerja}$$
>    - **Usaha C**:
>      $$NT_C = 120 - 75 = 45\text{ Juta Rp}$$
>      $$\text{Produktivitas}_C = \frac{45\text{ Juta}}{15\text{ orang}} = 3,0\text{ Juta Rp/pekerja}$$
> 
> **Verifikasi Kode Python**:
> ```python
> data = [{'u':'A', 'L':3, 'out':15, 'in':9}, {'u':'B', 'L':8, 'out':60, 'in':36}, {'u':'C', 'L':15, 'out':120, 'in':75}, {'u':'D', 'L':25, 'out':250, 'in':150}]
> imk = [d for d in data if d['L'] < 20]
> res = [f"{d['u']}:NT={d['out']-d['in']}jt,Prod={(d['out']-d['in'])/d['L']:.1f}jt" for d in imk]
> print(f"IMK={len(imk)} usaha; " + ", ".join(res))
> # Output: IMK=3 usaha; A:NT=6jt,Prod=2.0jt, B:NT=24jt,Prod=3.0jt, C:NT=45jt,Prod=3.0jt
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Batasan Omzet UU UMKM**: Seringkali mahasiswa menjawab bahwa industri mikro adalah usaha dengan kekayaan bersih maksimal Rp50 juta atau omzet Rp300 juta sesuai UU No. 20 Tahun 2008. Dalam statistik BPS, kriteria operasional murni berbasis jumlah tenaga kerja (1-4 pekerja untuk mikro, 5-19 pekerja untuk kecil).
> 2. **Jebakan Pekerja Keluarga Tak Dibayar**: Seringkali pekerja keluarga tidak dihitung sehingga usaha keluarga dengan 1 pemilik dan 4 anak/istri yang membantu dihitung hanya 1 orang (mikro), padahal total 5 orang (masuk industri kecil).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Mikro: 1-4 orang. Kecil: 5-19 orang. Sedang: 20-99 orang. Besar: >= 100 orang. Murni hitung kepala tenaga kerja aktif!

*Keterkaitan Konsep: 11.2.1*
