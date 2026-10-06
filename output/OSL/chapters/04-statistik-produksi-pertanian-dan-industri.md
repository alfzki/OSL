---
tags: [osl, ppt-11, universitas]
chapter: 11
status: draft
points: 5
---

# Pertemuan 11: Statistik Produksi Pertanian dan Industri

> Modul ini diturunkan dari `internal/lessons/chapter-11/*.json`.
> `status: draft` karena belum ada sesi belajar yang tercatat pada `progress/tracker.json`.

## Konsep

### 11.1.1 Kerangka Sampel Area KSA Padi

- **Seksi**: 11.1 Estimasi Produksi Tanaman Pangan
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 4-18]
- **Cakupan**: COVERED

**Fokus ujian** — Prinsip dasar Kerangka Sampel Area (KSA), stratifikasi Lahan Baku Sawah (LBS), struktur hierarki segmen (300m x 300m) dan subsegmen (100m x 100m), 9 titik amatan koordinat GPS, klasifikasi fase pertumbuhan padi, serta peramalan luas panen 1-3 bulan ke depan.

**Intuisi** — Sebelum KSA diterapkan pada tahun 2018, BPS mengandalkan laporan eye-estimate (pandangan mata) dari ribuan Mantri Tani kecamatan yang rentan terhadap bias subjektif dan seringkali menghasilkan over-estimate luas panen hingga jutaan ton. KSA mengubah pendekatan menjadi pengukuran berbasis bukti spasial objektif. Setiap hamparan sawah dibagi menjadi petak-petak grid koordinat berukuran 300 m x 300 m (segmen). Pada minggu terakhir setiap bulan (tanggal 21-27), petugas memotret 9 titik tetap di dalam segmen menggunakan kamera ponsel Android berbasis GPS untuk mencatat fase tumbuh padi secara presisi dan diaudit secara digital oleh server pusat.

**Definisi BPS** — Kerangka Sampel Area (KSA) adalah metode survei berbasis area sampling frame yang membagi seluruh wilayah daratan berpotensi sawah menjadi grid segmen berukuran 300 m x 300 m (9 hektar), di mana setiap segmen dibagi menjadi 9 subsegmen berukuran 100 m x 100 m (1 hektar) dengan 9 titik pengamatan tetap setiap bulan untuk mengidentifikasi fase tumbuh tanaman padi secara objektif.

**Syarat & batas** — Pengamatan KSA dilakukan serentak pada minggu terakhir setiap bulan (tanggal 21 s.d. 27/28). Fase amatan mencakup: Vegetatif Awal (V1: 1-30 HST), Vegetatif Akhir (V2: 31-60 HST), Generatif Awal (G1: 61-90 HST), Generatif Akhir (G2: 91-105 HST), Panen (P), Persiapan Lahan (PL), Puso/Gagal Panen (PS), dan Bukan Sawah/Bukan Padi (BP/BS). Proyeksi panen dihitung berdasarkan masa tanam: V1 panen 3 bulan ke depan, V2/G1 panen 2 bulan ke depan, dan G2 panen 1 bulan ke depan.

**Rumus** — $$\hat{A}_{\text{panen}} = \sum_{h=1}^H A_h \cdot \hat{p}_{h,\text{panen}} = \sum_{h=1}^H A_h \left( \frac{\sum_{i=1}^{n_h} \sum_{j=1}^{9} y_{hij}}{9 \cdot n_h} \right)$$

### 11.1.2 Metode Ubinan Produktivitas

- **Seksi**: 11.1 Estimasi Produksi Tanaman Pangan
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 19-27]
- **Cakupan**: COVERED

**Fokus ujian** — Teknik survei ubinan objektif BPS, dimensi plot bujur sangkar 2,5 m x 2,5 m (6,25 m2), penimbangan Gabah Kering Panen (GKP), turunan matematis multiplier 1.600 (kg/ha), 16 (ku/ha), dan 1,6 (ton/ha), serta rekonstruksi soal UAS 2022/2023 Esai 2a Pak Sakri.

**Intuisi** — Bagaimana cara BPS mengetahui produktivitas panen padi tanpa harus menimbang seluruh hasil sawah berhektar-hektar? BPS menerapkan metode ubinan (crop-cutting survey). Petak cuplikan representatif berukuran bujur sangkar 2,5 m x 2,5 m (6,25 m2) dipasang secara acak di lahan sawah yang sedang dipanen. Seluruh rumpun padi di dalam petak dipotong, dirontokkan, dibersihkan dari hampa, lalu ditimbang dengan timbangan gantung terkalibrasi. Karena 1 hektar sama dengan 10.000 m2, maka 1 hektar memuat persis 10.000 / 6,25 = 1.600 petak ubinan, sehingga hasil timbangan dalam kilogram dapat langsung dikonversi menjadi produktivitas per hektar.

**Definisi BPS** — Metode Ubinan adalah teknik pengukuran objektif (crop cutting survey) yang dilaksanakan BPS bersama petugas Dinas Pertanian pada saat panen raya petani untuk mengestimasi produktivitas tanaman pangan per hektar. Plot standar ubinan padi adalah bujur sangkar berukuran 2,5 m x 2,5 m (luas 6,25 m2) dengan hasil panen ditimbang dalam wujud Gabah Kering Panen (GKP).

**Syarat & batas** — Plot ubinan padi berukuran baku 2,5 m x 2,5 m = 6,25 m2. Multiplier konversi: faktor pengali kg/ha adalah 1.600; faktor pengali kuintal/ha (ku/ha) adalah 16 (karena 1 ku = 100 kg); faktor pengali ton/ha adalah 1,6 (karena 1 ton = 1.000 kg). Rekonstruksi Soal UAS 2022/2023 Esai 2a Pak Sakri: timbangan 4,5 kg GKP menghasilkan produktivitas 72 ku/ha atau 7,2 ton/ha.

**Rumus** — $$\text{Produktivitas (kg/ha)} = \frac{b}{6,25} \times 10.000 = b \times 1.600, \quad \text{Produktivitas (ku/ha)} = b \times 16, \quad \text{Produktivitas (ton/ha)} = b \times 1,6$$

### 11.1.3 Survei Konversi Gabah ke Beras SKGB

- **Seksi**: 11.1 Estimasi Produksi Tanaman Pangan
- **Prioritas**: Sedang
- **Rujukan**: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 20-24]
- **Cakupan**: COVERED

**Fokus ujian** — Alur konversi gabah menjadi beras hasil SKGB 2018 BPS, parameter rendemen GKP ke GKG (83,38%), rendemen GKG ke Beras (64,02%), perhitungan produktivitas beras per hektar, serta dampaknya terhadap estimasi ketersediaan pangan nasional.

**Intuisi** — Mengapa angka konversi SKGB sangat krusial dalam statistik pangan nasional? Ketika survei ubinan dilakukan di sawah, hasil panen yang ditimbang adalah Gabah Kering Panen (GKP) yang masih basah dan belum dapat dikonsumsi. Masyarakat mengonsumsi beras, bukan gabah. Untuk menghitung neraca pangan beras nasional, BPS harus mengetahui secara persis berapa kilogram beras yang dihasilkan dari setiap kilogram gabah basah. Terdapat dua proses penyusutan fisik: penjemuran (pengurangan kadar air dari GKP ke GKG) dan penggilingan (pemisahan sekam dan dedak dari GKG ke beras).

**Definisi BPS** — Survei Konversi Gabah ke Beras (SKGB) adalah survei berkala BPS pada usaha penggilingan padi (Rice Milling Unit) dan produsen untuk memperbarui parameter rendemen gabah dan beras. Berdasarkan SKGB 2018 resmi BPS: (1) Angka konversi GKP ke GKG adalah 83,38% (0,8338); (2) Angka konversi GKG ke Beras adalah 64,02% (0,6402); (3) Angka konversi gabungan dari GKP langsung ke Beras adalah 83,38% x 64,02% = 53,38% (0,533799).

**Syarat & batas** — Angka konversi SKGB 2018 menggantikan angka konversi survei lama tahun 2005-2007. Standar kadar air: GKP berkadar air sekitar 20-25% dengan hampa/kotoran > 3%; GKG berkadar air maksimum 14% dengan hampa/kotoran maksimum 3%. Konversi ke beras tidak boleh langsung menerapkan 64,02% pada GKP tanpa memperhitungkan penyusutan jemur 83,38%.

**Rumus** — $$\text{Produksi GKG} = \text{Produksi GKP} \times 0,8338, \quad \text{Produksi Beras} = \text{Produksi GKG} \times 0,6402 = \text{Produksi GKP} \times 0,533799$$

### 11.2.1 Survei Industri Besar dan Sedang IBS

- **Seksi**: 11.2 Statistik Industri Pengolahan
- **Prioritas**: Sedang
- **Rujukan**: [Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md, slide/hal. 25-28, 50-51]
- **Cakupan**: COVERED

**Fokus ujian** — Definisi industri pengolahan/manufaktur BPS, batasan tenaga kerja IBS (20 orang atau lebih), indikator efisiensi rasio input terhadap output, indeks produksi manufaktur, serta integrasi ekstensi EXT-5 formula Nilai Pekerjaan Konstruksi NK = (NP - NS) x %NR.

**Intuisi** — Mengapa BPS menyurvei IBS secara lengkap (complete enumeration) terpisah dari industri kecil? Industri besar dan sedang (IBS) mencakup hanya sekitar 1-2% dari total jumlah entitas industri di Indonesia, namun mereka menyumbang lebih dari 80-85% total nilai tambah dan ekspor manufaktur nasional. Karakteristik IBS memiliki pembukuan formal terstandar, sehingga BPS dapat mengumpulkan data rinci komposisi input, output, tenaga kerja, upah, dan efisiensi. Selain manufaktur, sektor penyumbang output fisik besar lainnya adalah jasa konstruksi, di mana nilai realisasi output dihitung melalui formula Nilai Pekerjaan Konstruksi (NK) dengan mengurangkan pekerjaan yang disubkontrakkan agar tidak terjadi pencatatan ganda (double counting).

**Definisi BPS** — Survei Industri Besar dan Sedang (IBS) adalah kegiatan pengumpulan data tahunan dan bulanan BPS terhadap seluruh perusahaan industri manufaktur berstatus aktif dengan tenaga kerja 20 orang atau lebih (Sedang: 20-99 orang; Besar: 100 orang atau lebih). Indikator efisiensi IBS diukur dari rasio input terhadap output. Pada statistik konstruksi (EXT-5), Nilai Pekerjaan Konstruksi (NK) adalah besarnya nilai realisasi fisik proyek yang dikerjakan kontraktor utama setelah dikurangi nilai pekerjaan yang disubkontrakkan kepada pihak lain: NK = (NP - NS) * %NR.

**Syarat & batas** — Klasifikasi IBS mensyaratkan tenaga kerja minimal 20 orang. Pengurangan nilai subkontrak (NS) wajib dilakukan agar tidak terjadi double counting dalam penghitungan PDRB/PDB konstruksi, karena output subkontraktor akan dicatat pada laporan terpisah pihak subkontraktor tersebut.

**Rumus** — $$\text{Efisiensi IBS} = \frac{\text{Biaya Input Antara}}{\text{Nilai Output}}, \quad \text{Nilai Tambah Bruto} = \text{Output} - \text{Input}, \quad NK = (NP - NS) \times \%NR$$

### 11.2.2 Survei Industri Mikro dan Kecil IMK

- **Seksi**: 11.2 Statistik Industri Pengolahan
- **Prioritas**: Rendah
- **Rujukan**: [SUPLEMEN: [SUPLEMEN] BPS Sensus Ekonomi 2016 & Publikasi Profil Industri Mikro dan Kecil 2024]
- **Cakupan**: SUPPLEMENTED

**Fokus ujian** — [SUPLEMEN] Batasan operasional tenaga kerja industri mikro (1-4 orang) dan kecil (5-19 orang) BPS, karakteristik usaha informal manufaktur, metodologi survei sampel VIMK, serta penghitungan nilai tambah dan produktivitas per pekerja.

**Intuisi** — Sebagian besar unit usaha industri di Indonesia (>98%) berskala mikro dan kecil (seperti pengrajin tempe, konveksi rumahan, pandai besi, kerajinan anyaman). Walaupun skala per unit usahanya kecil, secara agregat mereka menyerap puluhan juta tenaga kerja informal dan menjaga ketahanan ekonomi rakyat dari guncangan krisis. Berbeda dengan IBS yang dicacah lengkap via direktori industri, IMK tersebar luas di lingkungan permukiman tanpa plang usaha resmi atau izin berbadan hukum, sehingga dicacah dengan pendekatan sampling rumah tangga/usaha berbasis blok sensus.

**Definisi BPS** — [SUPLEMEN] Survei Industri Mikro dan Kecil (VIMK) adalah survei berbasis sampel yang dilaksanakan BPS untuk menangkap profil, dinamika produksi, kendala usaha, dan nilai tambah dari usaha industri berskala kecil di Indonesia. Definisi operasional batas tenaga kerja BPS: (1) Industri Mikro (IM) adalah usaha industri pengolahan dengan 1 sampai 4 orang tenaga kerja; (2) Industri Kecil (IK) adalah usaha industri pengolahan dengan 5 sampai 19 orang tenaga kerja. Tenaga kerja mencakup pemilik usaha, pekerja keluarga tanpa bayaran (unpaid family workers), dan buruh/karyawan.

**Syarat & batas** — Konsep IMK merupakan materi pelengkap resmi [SUPLEMEN] karena slide perkuliahan Pertemuan 11 menitikberatkan pada IBS. Kriteria BPS secara operasional murni berbasis jumlah tenaga kerja aktif (1-4 mikro, 5-19 kecil), bukan kriteria omzet atau aset kekayaan bersih versi UU Koperasi & UMKM. Usaha dengan 20 tenaga kerja atau lebih masuk ke dalam populasi IBS.

**Rumus** — $$\text{Klasifikasi IMK} = \begin{cases} \text{Industri Mikro (IM)}, & 1 \le L \le 4 \\ \text{Industri Kecil (IK)}, & 5 \le L \le 19 \\ \text{Industri Sedang (IS)}, & 20 \le L \le 99 \\ \text{Industri Besar (IB)}, & L \ge 100 \end{cases}, \quad \text{Produktivitas} = \frac{\text{Nilai Tambah}}{L}$$

## Contoh Hitung

### 11.1.1 — Kerangka Sampel Area KSA Padi

Suatu kabupaten memiliki luas Lahan Baku Sawah (LBS) sebesar 45.000 hektar. Terpilih 200 segmen sampel KSA (masing-masing 9 titik amatan, total 1.800 titik amatan). Pada putaran amatan akhir Mei, tercatat 270 titik berada pada fase Panen (P), 360 titik pada fase Generatif Akhir (G2), dan 450 titik pada fase Vegetatif Akhir/Generatif Awal (V2/G1). Tentukan estimasi luas panen bulan Mei serta proyeksi luas panen bulan Juni dan Juli.

| Parameter Sampling KSA | Nilai Parameter |
|---|---|
| Luas Stratum Sawah Irigasi ($A_1$) | 45.000 ha |
| Jumlah Segmen Sampel ($n_1$) | 200 segmen |
| Jumlah Titik Amatan per Segmen | 9 titik |
| Total Titik Pengamatan ($N_{\text{titik}}$) | 1.800 titik |
| Titik Fase Panen Mei | 270 titik |
| Titik Fase G2 (Panen Juni) | 360 titik |
| Titik Fase V2/G1 (Panen Juli) | 450 titik |

**Penyelesaian**

1. Total titik amatan = 200 segmen * 9 titik = 1.800 titik amatan.
2. Luas Panen Bulan Mei: Proporsi titik panen = 270 / 1.800 = 0,15 (15%). Estimasi luas panen Mei = 0,15 * 45.000 ha = 6.750 ha.
3. Proyeksi Luas Panen Bulan Juni (fase G2): Proporsi titik G2 = 360 / 1.800 = 0,20 (20%). Proyeksi luas panen Juni = 0,20 * 45.000 ha = 9.000 ha.
4. Proyeksi Luas Panen Bulan Juli (fase V2/G1): Proporsi titik V2/G1 = 450 / 1.800 = 0,25 (25%). Proyeksi luas panen Juli = 0,25 * 45.000 ha = 11.250 ha.

**Hasil verifikasi** — `Mei=6750 ha, Juni=9000 ha, Juli=11250 ha`

### 11.1.2 — Metode Ubinan Produktivitas

Rekonstruksi Soal UAS OSL 2022/2023 Esai 2a: Pak Sakri adalah seorang petani padi di Kabupaten Sukoharjo yang memanen sawahnya seluas 2,5 hektar. Petugas BPS bersama petugas Dinas Pertanian setempat melakukan pengukuran produktivitas menggunakan alat ubinan berukuran 2,5 m x 2,5 m. Setelah seluruh tanaman padi dalam plot ubinan dipotong, dirontokkan, dan dibersihkan dari kotoran, jarum timbangan ubinan menunjukkan angka tepat 4,5 kg Gabah Kering Panen (GKP). Tentukan produktivitas sawah Pak Sakri dalam ku/ha dan ton/ha serta total estimasi produksi GKP dari seluruh sawah 2,5 hektar tersebut.

| Parameter Pengukuran | Simbol | Nilai | Satuan |
|---|---|---|---|
| Ukuran Sisi Plot Ubinan | $s$ | 2,5 | meter |
| Luas Plot Ubinan | $A_{\text{plot}}$ | 6,25 | $\text{m}^2$ |
| Luas 1 Hektar | $A_{\text{ha}}$ | 10.000 | $\text{m}^2$ |
| Berat Gabah Hasil Ubinan | $b$ | 4,5 | kg GKP |
| Luas Lahan Panen Pak Sakri | $L$ | 2,5 | hektar |

**Penyelesaian**

1. Luas plot ubinan = 2,5 m * 2,5 m = 6,25 m2. Multiplier konversi ke hektar: kg/ha = 10.000 / 6,25 = 1.600; ku/ha = 1.600 / 100 = 16; ton/ha = 1.600 / 1.000 = 1,6.
2. Produktivitas dalam kuintal per hektar: ku/ha = 4,5 * 16 = 72,0 ku/ha.
3. Produktivitas dalam ton per hektar: ton/ha = 4,5 * 1,6 = 7,2 ton/ha (atau 7.200 kg/ha).
4. Total estimasi produksi GKP sawah Pak Sakri seluas 2,5 ha: Total Produksi = 2,5 ha * 7,2 ton/ha = 18,0 ton GKP (atau 180 kuintal).

**Hasil verifikasi** — `ku/ha=72.0, ton/ha=7.2, total=18.0 ton`

### 11.1.3 — Survei Konversi Gabah ke Beras SKGB

Berdasarkan contoh resmi Slide 23 materi kuliah BPS: Suatu hamparan sawah ABCD seluas 1 hektar (125 m x 80 m = 10.000 m2) dilakukan ubinan 2,5 m x 2,5 m dan menghasilkan berat timbangan 3,1 kg Gabah Kering Panen (GKP). Menggunakan angka konversi SKGB 2018 (GKP ke GKG = 0,8338 dan GKG ke Beras = 0,6402), hitunglah: (1) Produktivitas GKP per ha dalam kuintal; (2) Produktivitas GKG per ha dalam kuintal; (3) Estimasi total produksi beras siap konsumsi untuk sawah 1 ha tersebut dalam kuintal beras dan kilogram beras.

| Parameter Konversi SKGB | Nilai | Satuan |
|---|---|---|
| Berat Timbangan Ubinan GKP | 3,1 | kg |
| Multiplier Ubinan ke Ku/ha | 16 | - |
| Angka Konversi GKP ke GKG ($K_1$) | 83,38% (0,8338) | rasio |
| Angka Konversi GKG ke Beras ($K_2$) | 64,02% (0,6402) | rasio |
| Luas Hamparan Sawah ABCD | 1 | hektar |

**Penyelesaian**

1. Produktivitas GKP per hektar: ku/ha (GKP) = 3,1 * 16 = 49,60 ku/ha.
2. Produktivitas GKG per hektar: ku/ha (GKG) = 49,60 * 0,8338 = 41,35648 ku/ha (dibulatkan 41,356 ku/ha).
3. Produksi Beras untuk sawah 1 ha ABCD: Produksi Beras = 41,35648 * 0,6402 = 26,47642 kuintal beras (dibulatkan 26,476 kuintal beras). Dalam kilogram: 26,47642 * 100 = 2.647,6 kg beras.

**Hasil verifikasi** — `GKP=49.60 ku/ha, GKG=41.356 ku/ha, Beras=26.476 ku (2647.6 kg)`

### 11.2.1 — Survei Industri Besar dan Sedang IBS

Rekonstruksi Soal Slide 50-51 & Uji E2E Skenario 9: PT Mahakarya Nusantara memenangkan kontrak proyek infrastruktur senilai total NP = Rp10.000.000.000,- (10 Miliar Rupiah). Untuk pekerjaan fondasi khusus, perusahaan mensubkontrakkannya kepada mitra dengan nilai NS = Rp2.000.000.000,- (2 Miliar Rupiah). Hingga akhir periode survei, persentase realisasi fisik yang diselesaikan adalah 80% (%NR = 0,80). Di samping itu, anak usaha manufaktur beton IBS milik perusahaan (memiliki 45 tenaga kerja) mencatat nilai output bruto Rp5.000.000.000,- dan input antara Rp3.000.000.000,-. Hitunglah: (1) Nilai Pekerjaan Konstruksi (NK) yang diselesaikan; (2) Rasio efisiensi dan Nilai Tambah Bruto (NTB) unit manufaktur beton IBS.

| Variabel Indikator | Nilai | Satuan |
|---|---|---|
| Nilai Kontrak Proyek ($NP$) | 10.000.000.000 | Rupiah (10 Miliar) |
| Nilai Subkontrak ($NS$) | 2.000.000.000 | Rupiah (2 Miliar) |
| Persentase Realisasi Fisik ($\BNR$) | 80% (0,80) | rasio |
| Output Manufaktur Beton IBS | 5.000.000.000 | Rupiah (5 Miliar) |
| Input Antara Manufaktur IBS | 3.000.000.000 | Rupiah (3 Miliar) |
| Tenaga Kerja Manufaktur | 45 | orang (Sedang) |

**Penyelesaian**

1. Nilai proyek bersih yang dikerjakan sendiri: NP - NS = 10.000.000.000 - 2.000.000.000 = 8.000.000.000 Rupiah (8 Miliar).
2. Nilai Pekerjaan Konstruksi: NK = (NP - NS) * %NR = 8.000.000.000 * 0,80 = 6.400.000.000 Rupiah (6,4 Miliar).
3. Efisiensi manufaktur IBS: Efisiensi = Input / Output = 3.000.000.000 / 5.000.000.000 = 0,60 (dibutuhkan Rp0,60 biaya input untuk menghasilkan Rp1,00 output).
4. Nilai Tambah Bruto (NTB) manufaktur: NTB = Output - Input = 5.000.000.000 - 3.000.000.000 = 2.000.000.000 Rupiah (2 Miliar).

**Hasil verifikasi** — `NK=6400000000.0 (Rp6.4 Miliar), Efisiensi=0.60, NTB=Rp2.0 Miliar`

### 11.2.2 — Survei Industri Mikro dan Kecil IMK

Dalam kegiatan pencacahan Survei Industri Mikro dan Kecil (VIMK) di sebuah kecamatan, tercatat data 4 unit usaha pengolahan makanan rakyat sebagai berikut: Usaha A (Pembuat Keripik Singkong, L=3 orang, output Rp15 juta, input Rp9 juta); Usaha B (Pabrik Tahu Rumahan, L=8 orang, output Rp60 juta, input Rp36 juta); Usaha C (Konveksi Daster, L=15 orang, output Rp120 juta, input Rp75 juta); Usaha D (Pabrik Roti Modern, L=25 orang, output Rp250 juta, input Rp150 juta). Tentukan klasifikasi masing-masing usaha menurut BPS, unit usaha yang masuk target survei IMK, serta produktivitas tenaga kerja per orang pada unit usaha IMK tersebut.

| Usaha | Tenaga Kerja ($L$) | Output (Juta Rp) | Input (Juta Rp) | Klasifikasi BPS | Masuk IMK? |
|---|---|---|---|---|---|
| Usaha A | 3 orang | 15,0 | 9,0 | Industri Mikro | Ya (Mikro) |
| Usaha B | 8 orang | 60,0 | 36,0 | Industri Kecil | Ya (Kecil) |
| Usaha C | 15 orang | 120,0 | 75,0 | Industri Kecil | Ya (Kecil) |
| Usaha D | 25 orang | 250,0 | 150,0 | Industri Sedang | Tidak (Masuk IBS) |

**Penyelesaian**

1. Klasifikasi Tenaga Kerja BPS:
   - Usaha A (L=3 orang) -> Industri Mikro (1-4 orang).
   - Usaha B (L=8 orang) -> Industri Kecil (5-19 orang).
   - Usaha C (L=15 orang) -> Industri Kecil (5-19 orang).
   - Usaha D (L=25 orang) -> Industri Sedang (20-99 orang, masuk IBS).
2. Target Populasi Survei IMK:
   - Usaha yang masuk cakupan survei IMK adalah Usaha A, B, dan C (total 3 usaha). Usaha D dicatat dalam Direktori IBS.
3. Nilai Tambah (NT) dan Produktivitas per Tenaga Kerja:
   - Usaha A: NT = 15 - 9 = 6 Juta Rp. Produktivitas = 6 / 3 = 2,0 Juta Rp/pekerja.
   - Usaha B: NT = 60 - 36 = 24 Juta Rp. Produktivitas = 24 / 8 = 3,0 Juta Rp/pekerja.
   - Usaha C: NT = 120 - 75 = 45 Juta Rp. Produktivitas = 45 / 15 = 3,0 Juta Rp/pekerja.

**Hasil verifikasi** — `IMK=3 usaha; A:NT=6jt,Prod=2.0jt, B:NT=24jt,Prod=3.0jt, C:NT=45jt,Prod=3.0jt`

## Jebakan Ujian

**11.1.1 — Hierarki Dimensi Segmen vs Subsegmen KSA**

- Jebakan: Mengira 1 segmen KSA berukuran 100m x 100m atau menganggap foto diambil hanya pada 1 titik per segmen.
- Strategi aman: Ingat bahwa 1 segmen berukuran 300m x 300m (9 ha), yang dibagi menjadi 9 subsegmen berukuran 100m x 100m (1 ha) dengan total 9 titik amatan GPS per segmen.

**11.1.1 — Proyeksi Waktu Panen Berdasarkan Fase**

- Jebakan: Menganggap fase vegetatif awal (V1) atau vegetatif akhir (V2) akan langsung dipanen pada bulan berikutnya (t+1).
- Strategi aman: Siklus tanam padi berlangsung 3,5 hingga 4 bulan: V1 panen 3 bulan ke depan, V2/G1 panen 2 bulan ke depan, dan hanya G2 yang diproyeksikan panen 1 bulan ke depan.

**11.1.2 — Tertukar Satuan Kuintal/ha dan Ton/ha**

- Jebakan: Mengalikan hasil timbangan dengan 16 tetapi menuliskan satuannya sebagai ton/ha (misal 4,5 x 16 = 72 ton/ha).
- Strategi aman: Perhatikan bahwa 1 kuintal = 100 kg sedangkan 1 ton = 1.000 kg. Multiplier untuk kuintal/ha adalah 16, sedangkan multiplier untuk ton/ha adalah 1,6 (hasilnya 7,2 ton/ha, bukan 72 ton/ha).

**11.1.2 — Asumsi Bentuk Gabah Hasil Ubinan**

- Jebakan: Menganggap hasil timbangan ubinan langsung berupa Gabah Kering Giling (GKG) atau beras siap konsumsi.
- Strategi aman: Hasil timbangan ubinan riil di sawah selalu berbentuk Gabah Kering Panen (GKP) berkadar air tinggi yang masih harus dikonversi dengan angka SKGB.

**11.1.3 — Mengalikan GKP Langsung dengan Rasio Giling 64,02%**

- Jebakan: Langsung mengalikan data GKP dengan 0,6402 untuk mendapatkan beras, mengabaikan tahap penjemuran menjadi GKG.
- Strategi aman: Alur konversi wajib bertahap: GKP disusutkan jemur (x 0,8338) menjadi GKG, lalu GKG digiling (x 0,6402) menjadi Beras, atau gunakan pengali gabungan langsung 0,533799.

**11.1.3 — Tertukar Nilai Konversi Jemur dan Giling**

- Jebakan: Menggunakan angka 64,02% untuk konversi jemur dan 83,38% untuk konversi giling.
- Strategi aman: Ingat bahwa rendemen penjemuran lebih tinggi (83,38% karena hanya susut air), sedangkan rendemen penggilingan lebih rendah (64,02% karena kulit sekam dan bekatul terbuang).

**11.2.1 — Lupa Mengurangkan Nilai Subkontrak (NS)**

- Jebakan: Mengalikan nilai proyek total langsung dengan persentase realisasi: NK = NP x %NR = 10 Miliar x 80% = 8 Miliar.
- Strategi aman: Wajib mengurangkan nilai pekerjaan yang disubkontrakkan terlebih dahulu agar tidak terjadi penghitungan ganda (double counting) dalam neraca output konstruksi.

**11.2.1 — Interpretasi Terbalik Nilai Rasio Efisiensi**

- Jebakan: Mengira bahwa angka rasio efisiensi yang semakin besar menunjukkan kinerja industri yang semakin baik.
- Strategi aman: Rasio efisiensi BPS dihitung sebagai Input/Output (biaya masukan per satu rupiah keluaran), sehingga semakin KECIL rasionya, semakin efisien perusahaan tersebut.

**11.2.2 — Menggunakan Kriteria Modal atau Omzet**

- Jebakan: Mengklasifikasikan industri mikro dan kecil berdasarkan batasan modal atau omzet penjualan versi UU UMKM.
- Strategi aman: Official Statistics BPS secara operasional murni menggunakan jumlah tenaga kerja yang bekerja (1-4 pekerja untuk mikro, 5-19 pekerja untuk kecil).

**11.2.2 — Mengabaikan Pekerja Keluarga Tak Dibayar**

- Jebakan: Hanya menghitung pekerja yang menerima gaji formal dan mengabaikan pemilik atau anggota keluarga yang ikut memproduksi.
- Strategi aman: Seluruh tenaga kerja yang terlibat aktif dalam proses produksi fisik (termasuk pekerja keluarga tanpa bayaran) wajib diperhitungkan.

## Navigasi

- [[03-indikator-kesehatan-dan-sdgs-3|← Pertemuan 10: Indikator Kesehatan dan SDGs 3]]
- [[05-perdagangan-dan-indikator-harga|→ Pertemuan 12: Perdagangan dan Indikator Harga]]
- [[_formulas|Rumus lengkap OSL]]
- [[_glossary|Glosarium istilah]]

---

[[_MOC|← Back to MOC]]
