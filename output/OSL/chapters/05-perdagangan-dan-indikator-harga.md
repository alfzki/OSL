---
tags: [osl, ppt-12, universitas]
chapter: 12
status: draft
points: 8
---

# Pertemuan 12: Perdagangan dan Indikator Harga

> Modul ini diturunkan dari `internal/lessons/chapter-12/*.json`.
> `status: draft` karena belum ada sesi belajar yang tercatat pada `progress/tracker.json`.

## Konsep

### 12.1.1 Margin Perdagangan dan Pengangkutan MPP

- **Seksi**: 12.1 Margin Perdagangan dan Distribusi
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 4-9]
- **Cakupan**: COVERED

**Fokus ujian** — Definisi operasional MPP menurut SNA 15.28, perhitungan margin per simpul perantara, formula akumulasi multiplikatif MPP Total, dan interpretasi efisiensi distribusi barang strategis.

**Intuisi** — Margin Perdagangan dan Pengangkutan (MPP) mencerminkan kompensasi atau imbalan jasa yang diterima oleh para pelaku pedagang perantara (distributor, agen, pedagang besar/grosir, dan pedagang eceran) yang mengalirkan barang dari produsen hingga sampai ke tangan konsumen akhir. Semakin banyak perantara dalam saluran distribusi atau semakin tinggi biaya logistik dan laba pedagang, semakin besar disparitas antara harga yang diterima produsen dan harga yang dibayar konsumen.

**Definisi BPS** — Selisih antara nilai penjualan dengan nilai pembelian yang mengikutsertakan biaya pengangkutan (SNA 15.28). MPP merupakan ukuran nilai output dari kegiatan distribusi perdagangan. Mulai tahun 2017, BPS menyajikan data MPP Total, yaitu akumulasi margin perdagangan dari pedagang besar pertama hingga pedagang eceran ke konsumen akhir.

**Syarat & batas** — MPP tidak diberlakukan untuk penjualan langsung oleh produsen ke konsumen akhir (karena tidak ada jasa distribusi perantara). MPP tiap pelaku usaha i dihitung berdasarkan harga beli pelaku tersebut: MPP_i = (P_jual,i - P_beli,i) / P_beli,i * 100%. Akumulasi margin bersifat multiplikatif terhadap harga produsen: 1 + MPP_total = prod(1 + MPP_i).

**Rumus** — $$MPP_i = \frac{P_{\text{jual}, i} - P_{\text{beli}, i}}{P_{\text{beli}, i}} \times 100\%, \quad 1 + MPP_{\text{total}} = \prod_{i=1}^n (1 + MPP_i), \quad MPP_{\text{total}} = \frac{P_{\text{konsumen akhir}} - P_{\text{produsen}}}{P_{\text{produsen}}} \times 100\%$$

### 12.1.2 Survei Pola Distribusi Perdagangan Poldis

- **Seksi**: 12.1 Margin Perdagangan dan Distribusi
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 10-13]
- **Cakupan**: COVERED

**Fokus ujian** — Tujuan dan metodologi Survei Poldis, pemetaan rantai saluran distribusi komoditas strategis, konsep marketed surplus produsen, dan analisis efisiensi perdagangan antarpelaku.

**Intuisi** — Komoditas pangan strategis seperti cabai merah, bawang merah, dan daging sapi sering mengalami lonjakan harga tajam di pasar kota meskipun harga di tingkat petani sedang jatuh. Mengapa disparitas harga ini terjadi? Survei Poldis menelusuri secara empiris jejak perjalanan fisik komoditas: siapa saja pedagang perantara yang terlibat, rute antarpulau yang dilewati, dan di titik simpul mana penumpukan margin keuntungan serta biaya logistik terjadi. Rantai yang ramping mencerminkan sistem distribusi yang efisien.

**Definisi BPS** — Survei terstruktur yang diselenggarakan BPS untuk memetakan alur distribusi perdagangan komoditas barang strategis mulai dari produsen sampai konsumen akhir, mengidentifikasi pola rantai utama per komoditas, dan menghitung Margin Perdagangan dan Pengangkutan (MPP) di setiap pelaku usaha perdagangan serta antarwilayah.

**Syarat & batas** — Saluran distribusi perdagangan membedakan pelaku menjadi 4 tingkatan: Produsen, Pedagang Besar (Grosir/Distributor I & II), Pedagang Eceran (Pasar tradisional/modern), dan Konsumen Akhir (Rumah Tangga dan Non-Rumah Tangga). Rantai distribusi yang pendek menunjukkan distribusi yang efisien, sedangkan rantai yang panjang meningkatkan beban biaya pada konsumen akhir.

**Rumus** — $$\text{MPP}_{\text{rantai}} = \frac{P_{\text{konsumen akhir}} - P_{\text{produsen}}}{P_{\text{produsen}}} \times 100\%, \quad \Delta \text{Beban} = \text{MPP}_{\text{rantai panjang}} - \text{MPP}_{\text{rantai pendek}}$$

### 12.2.1 IHK Rumus Modified Laspeyres

- **Seksi**: 12.2 Indeks Harga Konsumen dan Inflasi
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 14-20] [indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.md, slide/hal. 15-25]
- **Cakupan**: COVERED

**Fokus ujian** — Penurunan rumus Modified Laspeyres berantai BPS, pembaruan bobot diagram timbang dari SBH, 11 kelompok pengeluaran COICOP 2018, dan rekonstruksi tabel hitungan UAS 2022/2023 Esai 2b.1.

**Intuisi** — Indeks Laspeyres klasik membutuhkan data kuantitas barang tahun dasar (Q0) dan harga periode berjalan (Pt). Namun di lapangan, mengumpulkan data konsumsi fisik seluruh rumah tangga setiap bulan tidak mungkin dilakukan. Oleh karena itu, BPS menggunakan formula Modified Laspeyres: indeks dihitung berantai dengan mengalikan Relatif Harga bulan berjalan terhadap bulan sebelumnya (Pt / P_{t-1}) dengan Nilai Konsumsi bulan sebelumnya (P_{t-1} Q0). Cara ini sangat praktis, konsisten matematis, dan memungkinkan pemutakhiran harga bulanan secara cepat tanpa harus mengubah kuantitas dasar.

**Definisi BPS** — Indeks harga yang mengukur perubahan rata-rata harga sekeranjang tetap barang dan jasa yang dikonsumsi oleh rumah tangga di wilayah perkotaan antarwaktu, dihitung menggunakan formula Laspeyres yang Dimodifikasi (Modified Laspeyres) dengan bobot diagram timbang dari Survei Biaya Hidup (SBH).

**Syarat & batas** — Jika harga seluruh komoditas tetap sama persis (Pt = P_{t-1}), relatif harga RH = 1,0 untuk setiap komoditas, sehingga IHK_t = IHK_{t-1}. Pembaruan diagram timbang dilakukan secara periodik melalui SBH (SBH 2012 -> SBH 2018 mencakup 90 kota -> SBH 2022 mencakup 150 kabupaten/kota di 38 provinsi). Klasifikasi komoditas mengikuti COICOP 2018 dengan 11 kelompok pengeluaran.

**Rumus** — $$IHK_t = \frac{\sum_{i=1}^k \left( \frac{P_{ti}}{P_{(t-1)i}} \times P_{(t-1)i} Q_{0i} \right)}{\sum_{i=1}^k P_{0i} Q_{0i}} \times 100 = \sum_{i=1}^k \left( \frac{P_{ti}}{P_{(t-1)i}} \times W_{(t-1)i} \right)$$

### 12.2.2 Tiga Laju Inflasi BPS mtom yony ytd

- **Seksi**: 12.2 Indeks Harga Konsumen dan Inflasi
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 21-26]
- **Cakupan**: COVERED

**Fokus ujian** — Formula tiga laju inflasi BPS, penentuan penyebut rujukan periode dasar, sifat ekuivalensi bulan Januari dan Desember, serta interpretasi ekonomi makro.

**Intuisi** — Tiga laju inflasi BPS memberikan lensa waktu berbeda untuk mendiagnosis dinamika kenaikan harga. Inflasi bulanan (m-to-m) memotret kejutan harga sesaat (misalnya lonjakan harga tiket pesawat saat libur Lebaran). Inflasi tahun kalender (y-to-d) merekam akumulasi kenaikan harga sejak awal tahun anggaran (Januari hingga bulan berjalan). Inflasi tahunan (y-on-y) membandingkan harga terhadap bulan yang sama di tahun sebelumnya, sehingga menyingkirkan faktor musiman tahunan dan digunakan sebagai sasaran resmi stabilitas moneter Bank Indonesia.

**Definisi BPS** — Tiga ukuran perubahan persentase IHK yang dirilis resmi oleh BPS: 1) Inflasi m-to-m: perubahan IHK bulan berjalan terhadap bulan sebelumnya; 2) Inflasi y-to-d: perubahan IHK bulan berjalan terhadap bulan Desember tahun sebelumnya; 3) Inflasi y-on-y: perubahan IHK bulan berjalan terhadap bulan yang sama pada tahun sebelumnya.

**Syarat & batas** — Sifat batas matematis unik pada kalender inflasi: 1) Pada bulan Januari: laju inflasi m-to-m selalu identik dengan inflasi y-to-d karena keduanya menggunakan dasar IHK Desember (t-1); 2) Pada bulan Desember: laju inflasi y-to-d selalu identik dengan inflasi y-on-y karena keduanya membandingkan IHK Desember tahun t terhadap IHK Desember tahun t-1 (terbukti pada Slide 21).

**Rumus** — $$\pi_{m\text{-to-}m} = \frac{IHK_{t, m} - IHK_{t, m-1}}{IHK_{t, m-1}} \times 100\%, \quad \pi_{y\text{-to-}d} = \frac{IHK_{t, m} - IHK_{t-1, 12}}{IHK_{t-1, 12}} \times 100\%, \quad \pi_{y\text{-on-}y} = \frac{IHK_{t, m} - IHK_{t-1, m}}{IHK_{t-1, m}} \times 100\%$$

### 12.2.3 Disagregasi Inflasi Inti Bergejolak Administered

- **Seksi**: 12.2 Indeks Harga Konsumen dan Inflasi
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 18-21]
- **Cakupan**: COVERED

**Fokus ujian** — Definisi tiga komponen disagregasi inflasi BPS, formula andil inflasi tertimbang, pembagian kewenangan pengendalian inflasi antara BI (Moneter) dan Pemerintah (Fiskal/Pangan/TPID).

**Intuisi** — Jika harga cabai rawit melonjak akibat curah hujan tinggi, apakah Bank Indonesia harus menaikkan suku bunga acuan? Tentu tidak! Kenaikan suku bunga tidak akan menghentikan hujan atau mempercepat panen cabai. Sebaliknya, jika seluruh harga barang industri dan jasa naik karena peredaran uang yang berlebihan dan ekspektasi inflasi masyarakat yang memburuk, barulah bank sentral perlu memperketat moneter. Untuk membedakan sumber pemicu kenaikan harga ini, BPS mendisagregasikan inflasi umum (headline) ke dalam tiga komponen: Inti, Bergejolak, dan Diatur Pemerintah.

**Definisi BPS** — Disagregasi IHK BPS yang mengelompokkan komoditas ke dalam tiga komponen pembentuk inflasi berdasarkan karakteristik pemicu pergerakan harga: 1) Inflasi Inti (Core Inflation): komponen yang pergerakan harganya cenderung persisten dan dipengaruhi faktor fundamental makro; 2) Komponen Bergejolak (Volatile Foods): komponen yang pergerakan harganya dipengaruhi oleh guncangan pasokan jangka pendek seperti cuaca dan musim panen; 3) Komponen Harga Diatur Pemerintah (Administered Prices): komponen yang harganya ditentukan atau dikendalikan oleh kebijakan harga pemerintah.

**Syarat & batas** — Penjumlahan andil dari ketiga komponen pembentuk inflasi sama persis dengan laju inflasi umum (headline): pi_headline = Andil_inti + Andil_bergejolak + Andil_administered, di mana Andil_k = (w_k / 100) * pi_k dan sum(w_k) = 100%.

**Rumus** — $$\pi_{\text{headline}} = \sum_{k \in \{\text{inti}, \text{bergejolak}, \text{diatur}\}} \left( \frac{w_k}{100} \times \pi_k \right), \quad \text{Andil}_k = \frac{w_k}{100} \times \pi_k$$

### 12.3.1 Konsep dan Rasio NTP It per Ib

- **Seksi**: 12.3 Nilai Tukar Petani NTP
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 33-36]
- **Cakupan**: COVERED

**Fokus ujian** — Konsep dasar dan formulasi rasio NTP, dekomposisi komponen pembayar petani (IKRT dan BPPBM), perhitungan inflasi perdesaan, dan rekonstruksi soal esai UAS 2022/2023 Esai 2b.3.

**Intuisi** — Petani memproduksi komoditas pangan untuk dijual ke pasar, tetapi pada saat yang sama petani dan keluarganya juga merupakan konsumen yang harus membeli beras, minyak goreng, pakaian, serta membayar biaya pupuk dan sewa traktor. Apakah petani semakin sejahtera atau justru semakin tertekan? Jawaban atas pertanyaan ini tidak cukup dilihat dari harga gabah semata. Jika harga gabah naik 5% tetapi harga kebutuhan pokok dan pupuk naik 10%, petani sejatinya merugi. Nilai Tukar Petani (NTP) adalah pengukur daya tukar riil (terms of trade) antara apa yang dijual petani dan apa yang dibeli petani.

**Definisi BPS** — Perbandingan antara Indeks Harga yang Diterima Petani (It) dengan Indeks Harga yang Dibayar Petani (Ib) yang dinyatakan dalam persentase. Indeks Ib terdiri dari dua kelompok besar: Indeks Konsumsi Rumah Tangga (IKRT) yang menjadi proksi inflasi perdesaan, serta Indeks Biaya Produksi dan Penambahan Barang Modal (BPPBM).

**Syarat & batas** — 1) NTP > 100: Petani mengalami surplus perdagangan (daya beli produk pertanian naik dibanding tahun dasar); 2) NTP = 100: Petani mengalami kondisi impas (daya beli tetap stabil); 3) NTP < 100: Petani mengalami defisit perdagangan (daya beli produk pertanian tergerus dibanding tahun dasar).

**Rumus** — $$NTP = \frac{I_t}{I_b} \times 100, \quad I_b = w_{\text{IKRT}} \cdot IKRT + w_{\text{BPPBM}} \cdot BPPBM, \quad \text{Inflasi Perdesaan} = \frac{IKRT_t - IKRT_{t-1}}{IKRT_{t-1}} \times 100\%$$

### 12.3.2 Nilai Tukar Usaha Petani NTUP

- **Seksi**: 12.3 Nilai Tukar Petani NTP
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 37-38]
- **Cakupan**: COVERED

**Fokus ujian** — Perbedaan fundamental antara NTP dan NTUP, formula NTUP = It / BPPBM * 100, analisis divergensi akibat inflasi perdesaan IKRT, dan konsep upah riil buruh tani.

**Intuisi** — Mengapa BPS mempublikasikan NTUP berdampingan dengan NTP? Karena sering kali terjadi paradoks di lapangan: teknologi pertanian berhasil meningkatkan efisiensi dan harga jual panen melampaui biaya pupuk/traktor (usaha tani sangat menguntungkan), tetapi angka NTP petani justru anjlok. Hal itu terjadi karena harga minyak goreng, gula, atau biaya sekolah di desa melonjak tajam. NTUP sengaja memisahkan urusan 'kegiatan berusahatani' dari urusan 'konsumsi rumah tangga' guna mengevaluasi kelayakan ekonomi dan daya saing murni dari sektor produksi pertanian.

**Definisi BPS** — Perbandingan antara Indeks Harga yang Diterima Petani (It) dengan Indeks Biaya Produksi dan Penambahan Barang Modal (BPPBM) yang dinyatakan dalam persentase. NTUP mengeluarkan komponen Indeks Konsumsi Rumah Tangga (IKRT) dari indeks yang dibayar petani (Ib), sehingga lebih mencerminkan kemampuan produksi riil usahatani.

**Syarat & batas** — 1) NTUP > 100: Usaha tani menghasilkan margin keuntungan di atas biaya input sarana produksi; 2) NTUP = 100: Usaha tani berada pada titik impas biaya operasional produksi; 3) Hubungan terhadap NTP: Jika laju kenaikan IKRT lebih besar daripada laju kenaikan BPPBM, maka NTP akan bergerak lebih rendah daripada NTUP (NTP < NTUP).

**Rumus** — $$NTUP = \frac{I_t}{BPPBM} \times 100, \quad \text{Upah Riil Buruh Tani} = \frac{\text{Upah Nominal}}{IKRT} \times 100$$

### 12.3.3 Lima Subsektor Penyusun NTP

- **Seksi**: 12.3 Nilai Tukar Petani NTP
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md, slide/hal. 36-40]
- **Cakupan**: COVERED

**Fokus ujian** — Klasifikasi komoditas 5 subsektor pertanian BPS, formula agregasi rata-rata tertimbang NTP gabungan, serta keterkaitan indeks spasial IKK dalam alokasi fiskal DAU.

**Intuisi** — Petani di Indonesia tidak homogen: petani padi di Karawang memiliki siklus panen dan pasar yang sangat berbeda dengan pekebun kelapa sawit di Riau, peternak ayam broiler di Blitar, atau nelayan tangkap cumi di Maluku. Jika BPS hanya merilis satu angka NTP nasional, kesejahteraan nelayan yang anjlok akibat cuaca buruk bisa tertutupi oleh rezeki nomplok pekebun sawit saat harga CPO dunia melonjak. Oleh karena itu, BPS menyusun NTP secara independen untuk 5 subsektor pertanian.

**Definisi BPS** — Disagregasi Nilai Tukar Petani menurut lima subsektor pertanian resmi BPS: 1) NTP Subsektor Tanaman Pangan (NTPR); 2) NTP Subsektor Hortikultura (NTPH); 3) NTP Subsektor Tanaman Perkebunan Rakyat (NTPR/BUN); 4) NTP Subsektor Peternakan (NTPT); 5) NTP Subsektor Perikanan (NTNP, mencakup Perikanan Tangkap dan Perikanan Budidaya).

**Syarat & batas** — 1) Setiap subsektor memiliki paket komoditas, harga produsen (It), dan struktur biaya produksi (BPPBM) yang spesifik hasil SPDT-NTP; 2) NTP gabungan provinsi/nasional merupakan rata-rata tertimbang dari kelima subsektor: NTP_gabungan = sum(w_s * NTP_s) dengan sum(w_s) = 1,0; 3) Ekstensi IKK: mengukur disparitas harga konstruksi spasial antarwilayah untuk Dana Alokasi Umum (DAU).

**Rumus** — $$NTP_{\text{gabungan}} = \sum_{s=1}^5 \left( w_s \times NTP_s \right), \quad \text{di mana } \sum_{s=1}^5 w_s = 1,0$$

## Contoh Hitung

### 12.1.1 — Margin Perdagangan dan Pengangkutan MPP

Berdasarkan Survei Pola Distribusi Perdagangan beras BPS, produsen menjual beras seharga Rp10.000,-/kg kepada distributor. Distributor menjual beras tersebut kepada Pedagang Eceran (PE) dengan harga Rp11.500,-/kg. Selanjutnya, pedagang eceran menjual beras kepada konsumen akhir dengan harga Rp13.800,-/kg. Hitunglah MPP Distributor ke PE, MPP PE ke Konsumen Akhir, dan MPP Total rantai distribusi beras tersebut.

| Pelaku Perdagangan | Harga Pembelian (Rp/kg) | Harga Penjualan (Rp/kg) | Peran Distribusi |
|---|---|---|---|
| Produsen | - | 10.000 | Petani / Penggilingan Padi |
| Distributor | 10.000 | 11.500 | Pedagang Besar / Grosir |
| Pedagang Eceran (PE) | 11.500 | 13.800 | Toko / Warung / Swalayan |
| Konsumen Akhir | 13.800 | - | Rumah Tangga Pembeli |

**Penyelesaian**

1. Menghitung MPP Distributor ke Pedagang Eceran:
   MPP_Dist = ((11.500 - 10.000) / 10.000) * 100% = (1.500 / 10.000) * 100% = 15,00%.
2. Menghitung MPP Pedagang Eceran ke Konsumen Akhir:
   MPP_Ecer = ((13.800 - 11.500) / 11.500) * 100% = (2.300 / 11.500) * 100% = 20,00%.
3. Menghitung MPP Total Rantai Distribusi:
   Cara langsung (rasio kenaikan dari produsen ke konsumen akhir):
   MPP_Total = ((13.800 - 10.000) / 10.000) * 100% = (3.800 / 10.000) * 100% = 38,00%.
   Cara multiplikatif rantai:
   1 + MPP_Total = (1 + 0,15) * (1 + 0,20) = 1,15 * 1,20 = 1,38 -> MPP_Total = 38,00%.

**Hasil verifikasi** — `MPP_Dist=15.00%, MPP_Ecer=20.00%, MPP_Total=38.00%`

### 12.1.2 — Survei Pola Distribusi Perdagangan Poldis

Dalam kajian Survei Poldis komoditas cabai merah di suatu provinsi, BPS mengidentifikasi dua pola distribusi perdagangan alternatif:
- Rantai A (Pola Distribusi Pendek): Petani Produsen -> Pedagang Eceran / Pasar Tani -> Konsumen Akhir. Harga di tingkat petani adalah Rp25.000,-/kg dan harga beli konsumen akhir adalah Rp32.000,-/kg.
- Rantai B (Pola Distribusi Panjang): Petani Produsen -> Tengkulak Desa -> Pedagang Besar Pasar Induk -> Pedagang Eceran -> Konsumen Akhir. Harga di tingkat petani adalah Rp25.000,-/kg dan harga beli konsumen akhir adalah Rp40.000,-/kg.
Hitunglah persentase MPP Total untuk Rantai A dan Rantai B, serta hitung selisih beban harga yang ditanggung oleh konsumen akibat rantai distribusi yang panjang.

| Pola Rantai | Rute Pelaku Perdagangan | Harga Produsen (Rp/kg) | Harga Konsumen Akhir (Rp/kg) |
|---|---|---|---|
| Rantai A | Petani -> Pedagang Eceran -> Konsumen | 25.000 | 32.000 |
| Rantai B | Petani -> Tengkulak -> Pedagang Besar -> Pengecer -> Konsumen | 25.000 | 40.000 |

**Penyelesaian**

1. Menghitung MPP Total Rantai A (Pola Pendek):
   MPP_A = ((32.000 - 25.000) / 25.000) * 100% = (7.000 / 25.000) * 100% = 28,00%.
2. Menghitung MPP Total Rantai B (Pola Panjang):
   MPP_B = ((40.000 - 25.000) / 25.000) * 100% = (15.000 / 25.000) * 100% = 60,00%.
3. Menghitung Selisih Beban Kenaikan Harga bagi Konsumen:
   Selisih_Beban = MPP_B - MPP_A = 60,00% - 28,00% = 32,00%.
   Konsumen pada Rantai B menanggung tambahan beban harga sebesar 32,00% poin lebih tinggi dibandingkan Rantai A.

**Hasil verifikasi** — `MPP_Rantai_A=28.00%, MPP_Rantai_B=60.00%, Selisih_Beban=32.00%`

### 12.2.1 — IHK Rumus Modified Laspeyres

Rekonstruksi Tabel Ujian Akhir Semester (UAS) OSL 2022/2023 Esai 2b.1:
Diberikan data series IHK Gabungan Kota di Indonesia sebagai berikut:
- IHK April 2022 = 109,98
- IHK Mei 2022 = 110,42
- IHK Desember 2022 = 113,59
- IHK April 2023 = 114,74
- Tingkat Inflasi m-to-m Mei 2023 = 0,09%
Berdasarkan data tersebut, hitunglah:
1. Nilai IHK Mei 2023 (Cell A)
2. Tingkat Inflasi Year to Date (y-to-d) Mei 2023 (Cell B)
3. Tingkat Inflasi Year on Year (y-on-y) Mei 2023 (Cell C)

| Periode Data | Nilai IHK | Catatan Pembanding Inflasi |
|---|---|---||
| April 2022 | 109,98 | Distractor ujian |
| Mei 2022 | 110,42 | Basis pembanding y-on-y Mei 2023 |
| Desember 2022 | 113,59 | Basis pembanding y-to-d Mei 2023 |
| April 2023 | 114,74 | Basis pembanding m-to-m Mei 2023 |
| Mei 2023 | [Cell A] | Inflasi m-to-m diketahui = 0,09% |

**Penyelesaian**

1. Menghitung IHK Mei 2023 (Cell A):
   IHK_Mei_2023 = IHK_Apr_2023 * (1 + Inflasi_mtom / 100)
   IHK_Mei_2023 = 114,74 * (1 + 0,09 / 100) = 114,74 * 1,0009 = 114,843266 -> dibulatkan 114,84.
2. Menghitung Inflasi Year to Date (y-to-d) Mei 2023 (Cell B):
   Inflasi_ytd = ((IHK_Mei_2023 - IHK_Des_2022) / IHK_Des_2022) * 100%
   Inflasi_ytd = ((114,843266 - 113,59) / 113,59) * 100% = (1,253266 / 113,59) * 100% = 1,103324% -> dibulatkan 1,10%.
3. Menghitung Inflasi Year on Year (y-on-y) Mei 2023 (Cell C):
   Inflasi_yoy = ((IHK_Mei_2023 - IHK_Mei_2022) / IHK_Mei_2022) * 100%
   Inflasi_yoy = ((114,843266 - 110,42) / 110,42) * 100% = (4,423266 / 110,42) * 100% = 4,005856% -> dibulatkan 4,01%.
   (Peringatan: jangan menggunakan IHK April 2022 sebagai pembagi yoy Mei 2023!).

**Hasil verifikasi** — `IHK_Mei_2023=114.84, Inflasi_ytd=1.10%, Inflasi_yoy=4.01%`

### 12.2.2 — Tiga Laju Inflasi BPS mtom yony ytd

Berdasarkan Berita Resmi Statistik (BRS) BPS Gabungan 90 Kota (2018=100) pada Slide 20, tercatat data IHK sebagai berikut:
- IHK Maret 2021 = 106,15
- IHK Desember 2021 = 107,66
- IHK Februari 2022 = 108,24
- IHK Maret 2022 = 108,95
Hitunglah ketiga jenis laju inflasi untuk bulan Maret 2022:
1. Tingkat Inflasi month-to-month (m-to-m)
2. Tingkat Inflasi year-to-date (y-to-d)
3. Tingkat Inflasi year-on-year (y-on-y)

| Periode Rujukan | Nilai IHK | Kegunaan dalam Perhitungan Maret 2022 |
|---|---|---|
| Maret 2021 | 106,15 | Penyebut formula year-on-year (y-on-y) |
| Desember 2021 | 107,66 | Penyebut formula year-to-date (y-to-d) |
| Februari 2022 | 108,24 | Penyebut formula month-to-month (m-to-m) |
| Maret 2022 | 108,95 | Pembilang IHK bulan berjalan ($IHK_t$) |

**Penyelesaian**

1. Menghitung Inflasi month-to-month (m-to-m) Maret 2022:
   pi_mtom = ((108,95 - 108,24) / 108,24) * 100% = (0,71 / 108,24) * 100% = 0,655931% -> 0,66%.
2. Menghitung Inflasi year-to-date (y-to-d) Maret 2022:
   pi_ytd = ((108,95 - 107,66) / 107,66) * 100% = (1,29 / 107,66) * 100% = 1,198217% -> 1,20%.
3. Menghitung Inflasi year-on-year (y-on-y) Maret 2022:
   pi_yony = ((108,95 - 106,15) / 106,15) * 100% = (2,80 / 106,15) * 100% = 2,637777% -> 2,64%.

**Hasil verifikasi** — `m-to-m=0.66%, y-to-d=1.20%, y-on-y=2.64%`

### 12.2.3 — Disagregasi Inflasi Inti Bergejolak Administered

Dalam suatu rilis BRS IHK bulanan, diagram timbang dan tingkat inflasi bulanan (m-to-m) menurut komponen disagregasi tercatat sebagai berikut:
- Komponen Inti: bobot w = 60,00%, laju inflasi m-to-m = 0,20%
- Komponen Bergejolak (Volatile Foods): bobot w = 20,00%, laju inflasi m-to-m = 1,50%
- Komponen Diatur Pemerintah (Administered Prices): bobot w = 20,00%, laju inflasi m-to-m = 0,50%
Hitunglah andil inflasi masing-masing komponen terhadap pembentukan inflasi umum, serta tentukan laju inflasi umum (headline inflation) bulan tersebut!

| Komponen Pembentuk Inflasi | Bobot Diagram Timbang ($w_k$) | Laju Inflasi m-to-m ($\pi_k$) | Pemicu Utama Pergerakan |
|---|---|---|---|
| **Komponen Inti (Core)** | 60,00% | 0,20% | Interaksi permintaan-penawaran uang |
| **Komponen Bergejolak (Volatile)** | 20,00% | 1,50% | Gagal panen cabai dan cuaca ekstrem |
| **Diatur Pemerintah (Administered)** | 20,00% | 0,50% | Penyesuaian tarif angkutan lokal |

**Penyelesaian**

1. Menghitung Andil Inflasi Komponen Inti:
   Andil_Inti = (w_Inti / 100) * pi_Inti = (60,00 / 100) * 0,20% = 0,60 * 0,20% = 0,12%.
2. Menghitung Andil Inflasi Komponen Bergejolak:
   Andil_Berg = (w_Berg / 100) * pi_Berg = (20,00 / 100) * 1,50% = 0,20 * 1,50% = 0,30%.
3. Menghitung Andil Inflasi Komponen Diatur Pemerintah:
   Andil_Adm = (w_Adm / 100) * pi_Adm = (20,00 / 100) * 0,50% = 0,20 * 0,50% = 0,10%.
4. Menghitung Laju Inflasi Umum (Headline Inflation):
   pi_Headline = Andil_Inti + Andil_Berg + Andil_Adm = 0,12% + 0,30% + 0,10% = 0,52%.
   Komponen bergejolak menjadi penyumbang terbesar andil inflasi (0,30% dari total 0,52%).

**Hasil verifikasi** — `Andil_Inti=0.12%, Andil_Bergejolak=0.30%, Andil_Administered=0.10%, Headline=0.52%`

### 12.3.1 — Konsep dan Rasio NTP It per Ib

Rekonstruksi Tabel Ujian Akhir Semester (UAS) OSL 2022/2023 Esai 2b.3:
Diberikan data indikator harga perdesaan BPS bulan April dan Mei 2023 sebagai berikut:
- Bulan April 2023: It = 128,64; Ib = 116,33; IKRT = 116,71; BPPBM = 115,98.
- Bulan Mei 2023: NTUP = 110,75; Ib = 116,71; IKRT = 117,18; BPPBM = 116,13.
Berdasarkan data di atas, hitunglah:
1. Nilai NTP bulan April 2023 (Cell 1)
2. Nilai NTUP bulan April 2023 (Cell 2)
3. Nilai Indeks yang Diterima Petani (It) bulan Mei 2023 (Cell 3)
4. Nilai NTP bulan Mei 2023 (Cell 4)
5. Laju Inflasi Perdesaan bulan Mei 2023 (Cell 5)

| Indikator Statistik | April 2023 | Mei 2023 | Keterangan Hubungan Antar-Variabel |
|---|---|---|---|
| **Indeks Diterima Petani ($I_t$)** | 128,64 | [Cell 3] | Dihitung dari NTUP Mei dan BPPBM Mei |
| **Indeks Dibayar Petani ($I_b$)** | 116,33 | 116,71 | Pembagi untuk menghitung NTP |
| - Indeks Konsumsi RT ($IKRT$) | 116,71 | 117,18 | Basis penghitungan inflasi perdesaan |
| - Biaya Produksi ($BPPBM$) | 115,98 | 116,13 | Pembagi untuk menghitung NTUP |
| **Nilai Tukar Petani ($NTP$)** | [Cell 1] | [Cell 4] | Rasio ($I_t / I_b \times 100$) |
| **Nilai Tukar Usaha ($NTUP$)** | [Cell 2] | 110,75 | Rasio ($I_t / BPPBM \times 100$) |

**Penyelesaian**

1. Menghitung NTP April 2023 (Cell 1):
   NTP_Apr = (It_Apr / Ib_Apr) * 100 = (128,64 / 116,33) * 100 = 110,5820% -> 110,58.
2. Menghitung NTUP April 2023 (Cell 2):
   NTUP_Apr = (It_Apr / BPPBM_Apr) * 100 = (128,64 / 115,98) * 100 = 110,9157% -> 110,92.
3. Menghitung It Mei 2023 (Cell 3):
   Karena NTUP_Mei = (It_Mei / BPPBM_Mei) * 100 = 110,75, maka:
   It_Mei = (NTUP_Mei * BPPBM_Mei) / 100 = (110,75 * 116,13) / 100 = 128,613975 -> 128,61.
4. Menghitung NTP Mei 2023 (Cell 4):
   NTP_Mei = (It_Mei / Ib_Mei) * 100 = (128,613975 / 116,71) * 100 = 110,1996% -> 110,20.
5. Menghitung Laju Inflasi Perdesaan Mei 2023 (Cell 5):
   Inflasi dihitung khusus dari perubahan IKRT:
   Inflasi_Desa = ((IKRT_Mei - IKRT_Apr) / IKRT_Apr) * 100%
   Inflasi_Desa = ((117,18 - 116,71) / 116,71) * 100% = (0,47 / 116,71) * 100% = 0,402708% -> 0,40%.

**Hasil verifikasi** — `NTP_Apr=110.58, NTUP_Apr=110.92, It_Mei=128.61, NTP_Mei=110.20, Inflasi_Desa=0.40%`

### 12.3.2 — Nilai Tukar Usaha Petani NTUP

Dalam analisis kebijakan pertanian daerah, diketahui kondisi harga usahatani pada dua periode berturut-turut:
- Bulan ke-1: Indeks Diterima Petani It = 120,0; Indeks Konsumsi RT IKRT = 110,0; Indeks Biaya Produksi BPPBM = 100,0. Bobot diagram timbang Ib adalah 60% IKRT dan 40% BPPBM.
- Bulan ke-2: Terjadi guncangan pasokan pangan di perdesaan sehingga IKRT melonjak 10% menjadi 121,0. Sementara itu, harga hasil panen (It) tetap 120,0 dan biaya sarana produksi (BPPBM) tetap stabil di angka 100,0.
Hitunglah nilai NTP dan NTUP untuk bulan ke-1 dan bulan ke-2, serta simpulkan perbedaan indikasi antara kesejahteraan rumah tangga versus profitabilitas usahatani!

| Periode | $I_t$ | $IKRT$ (Bobot 60%) | $BPPBM$ (Bobot 40%) | $I_b$ Gabungan |
|---|---|---|---|---|
| Bulan 1 | 120,0 | 110,0 | 100,0 | $0,6(110) + 0,4(100) = 106,0$ |
| Bulan 2 | 120,0 | 121,0 | 100,0 | $0,6(121) + 0,4(100) = 112,6$ |

**Penyelesaian**

1. Menghitung NTP dan NTUP Bulan ke-1:
   Ib1 = (0,6 * 110,0) + (0,4 * 100,0) = 66,0 + 40,0 = 106,0.
   NTP1 = (It / Ib1) * 100 = (120,0 / 106,0) * 100 = 113,2075% -> 113,21.
   NTUP1 = (It / BPPBM) * 100 = (120,0 / 100,0) * 100 = 120,00% -> 120,00.
2. Menghitung NTP dan NTUP Bulan ke-2:
   Ib2 = (0,6 * 121,0) + (0,4 * 100,0) = 72,6 + 40,0 = 112,6.
   NTP2 = (It / Ib2) * 100 = (120,0 / 112,6) * 100 = 106,5719% -> 106,57.
   NTUP2 = (It / BPPBM) * 100 = (120,0 / 100,0) * 100 = 120,00% -> 120,00.
3. Kesimpulan Analitis:
   Nilai NTUP tetap konstan pada 120,00 (profitabilitas usaha tani stabil), namun NTP tergerus dari 113,21 menjadi 106,57 akibat lonjakan inflasi biaya hidup keluarga petani (IKRT naik 10%).

**Hasil verifikasi** — `NTP1=113.21, NTP2=106.57, NTUP1=120.00, NTUP2=120.00`

### 12.3.3 — Lima Subsektor Penyusun NTP

Sebuah provinsi agraris di luar Jawa memiliki struktur ekonomi pertanian yang ditopang oleh 5 subsektor. Berdasarkan hasil SPDT-NTP dan Survei Harga Perdesaan, tercatat bobot diagram timbang serta nilai NTP masing-masing subsektor sebagai berikut:
- Subsektor Tanaman Pangan (NTPR): bobot w = 0,35, nilai NTP = 102,50
- Subsektor Hortikultura (NTPH): bobot w = 0,20, nilai NTP = 115,00
- Subsektor Tanaman Perkebunan Rakyat (TPR): bobot w = 0,25, nilai NTP = 120,00
- Subsektor Peternakan (NTPT): bobot w = 0,10, nilai NTP = 108,00
- Subsektor Perikanan (NTNP): bobot w = 0,10, nilai NTP = 104,00
Hitunglah nilai NTP gabungan provinsi tersebut!

| No | Subsektor Pertanian | Bobot Timbang ($w_s$) | Nilai NTP Subsektor ($NTP_s$) | Kontribusi Tertimbang |
|---|---|---|---|---|
| 1 | Tanaman Pangan (NTPR) | 0,35 | 102,50 | $0,35 \times 102,50 = 35,875$ |
| 2 | Hortikultura (NTPH) | 0,20 | 115,00 | $0,20 \times 115,00 = 23,000$ |
| 3 | Perkebunan Rakyat (TPR) | 0,25 | 120,00 | $0,25 \times 120,00 = 30,000$ |
| 4 | Peternakan (NTPT) | 0,10 | 108,00 | $0,10 \times 108,00 = 10,800$ |
| 5 | Perikanan (NTNP) | 0,10 | 104,00 | $0,10 \times 104,00 = 10,400$ |

**Penyelesaian**

1. Menghitung kontribusi tertimbang masing-masing subsektor:
   - Tanaman Pangan = 0,35 * 102,50 = 35,875
   - Hortikultura = 0,20 * 115,00 = 23,000
   - Perkebunan Rakyat = 0,25 * 120,00 = 30,000
   - Peternakan = 0,10 * 108,00 = 10,800
   - Perikanan = 0,10 * 104,00 = 10,400
2. Menjumlahkan seluruh kontribusi tertimbang:
   NTP_Gabungan = 35,875 + 23,000 + 30,000 + 10,800 + 10,400 = 110,075 -> dibulatkan 110,08.
3. Interpretasi Hasil:
   NTP gabungan provinsi sebesar 110,08 (> 100) mengindikasikan sektor pertanian provinsi secara agregat mengalami surplus daya tukar riil, ditopang paling kuat oleh performa subsektor perkebunan rakyat (120,00) dan hortikultura (115,00).

**Hasil verifikasi** — `NTP_Gabungan=110.08`

## Jebakan Ujian

**12.1.1 — Menjumlahkan persentase margin secara aditif sederhana**

- Jebakan: Menghitung MPP Total dengan menjumlahkan margin pelaku usaha: 15% + 20% = 35%.
- Strategi aman: Gunakan formula multiplikatif BPS: (1 + 0,15) * (1 + 0,20) - 1 = 38%, atau hitung langsung selisih harga konsumen akhir terhadap harga produsen dibagi harga produsen.

**12.1.1 — Memasukkan transaksi penjualan langsung produsen ke konsumen ke dalam MPP**

- Jebakan: Menganggap penjualan beras langsung dari petani penggilingan ke rumah tangga memiliki margin perdagangan.
- Strategi aman: Ingat prinsip SNA 15.28: margin perdagangan hanya muncul jika ada jasa distribusi melalui pembelian dan penjualan kembali produk oleh pedagang perantara.

**12.1.2 — Mengabaikan konsumen non-rumah tangga dalam analisis saluran akhir Poldis**

- Jebakan: Mengasumsikan seluruh komoditas yang didistribusikan pasti berakhir di konsumen rumah tangga.
- Strategi aman: SNA dan BPS secara tegas membagi konsumen akhir menjadi dua: konsumen rumah tangga (household) dan konsumen non-rumah tangga (seperti industri pengolahan makanan, hotel, restoran, dan katering).

**12.1.2 — Mengira panjang rantai selalu menandakan mutu produk yang lebih baik**

- Jebakan: Menganggap semakin banyak tahapan perantara, kualitas barang semakin terjamin.
- Strategi aman: Dalam statistik distribusi pangan, rantai yang terlalu panjang sering kali mengindikasikan inefisiensi pasar, monopsoni lokal oleh tengkulak, dan memperbesar risiko penyusutan fisik komoditas pangan.

**12.2.1 — Salah memilih tahun dasar pembanding pada inflasi year-on-year**

- Jebakan: Menggunakan IHK April 2022 (109,98) alih-alih IHK Mei 2022 (110,42) untuk menghitung inflasi tahunan Mei 2023.
- Strategi aman: Inflasi year-on-year (y-on-y) wajib membandingkan bulan yang persis sama pada tahun sebelumnya: Mei 2023 terhadap Mei 2022. Nilai IHK April 2022 hanyalah pengecoh (distractor).

**12.2.1 — Membagi inflasi year-to-date (y-to-d) terhadap IHK Januari tahun berjalan**

- Jebakan: Menghitung inflasi tahun berjalan dengan membagi terhadap IHK Januari 2023.
- Strategi aman: Formula resmi BPS untuk inflasi year-to-date (tahun kalender) selalu membandingkan IHK bulan berjalan terhadap IHK bulan Desember tahun sebelumnya (t-1).

**12.2.2 — Mengabaikan kesamaan nilai ytd dan yoy pada bulan Desember**

- Jebakan: Menganggap inflasi y-to-d dan y-on-y pada bulan Desember harus memiliki angka yang berbeda.
- Strategi aman: Ingat dalil BPS Slide 21: pada bulan Desember, kedua ukuran sama persis secara definisi dan matematis karena sama-sama membandingkan IHK Desember tahun berjalan terhadap IHK Desember tahun sebelumnya.

**12.2.2 — Menjumlahkan inflasi bulanan m-to-m secara linier untuk mencari inflasi tahunan**

- Jebakan: Menjumlahkan 12 angka inflasi m-to-m dalam setahun secara langsung untuk mengklaim angka inflasi tahunan.
- Strategi aman: Inflasi adalah angka indeks dengan pertumbuhan multiplikatif geometrik: (1 + r_t) = prod(1 + r_m). Menjumlahkan langsung mengabaikan efek pertumbuhan majemuk (compounding effect).

**12.2.3 — Menyamakan laju inflasi komponen dengan andil inflasi**

- Jebakan: Menyimpulkan bahwa komponen bergejolak memiliki pengaruh paling dominan hanya karena laju inflasinya paling tinggi (1,50% vs 0,20%).
- Strategi aman: Pengaruh terhadap inflasi umum diukur oleh ANDIL inflasi (perkalian laju dengan bobot). Komponen inti dengan bobot 60% menyumbang andil stabil yang menjadi target utama moneter.

**12.2.3 — Salah menempatkan komoditas rokok dan elpiji ke dalam komponen bergejolak**

- Jebakan: Menggolongkan rokok kretek filter atau gas elpiji 3 kg ke dalam volatile foods karena sering dibeli sehari-hari.
- Strategi aman: Rokok (kenaikan cukai) dan elpiji subsidi merupakan komponen Administered Prices karena harga dan regulasinya ditetapkan pemerintah.

**12.3.1 — Menghitung inflasi perdesaan menggunakan indeks Ib**

- Jebakan: Menggunakan persentase perubahan indeks Ib total untuk menjawab inflasi perdesaan: ((116,71 - 116,33) / 116,33) * 100% = 0,33%.
- Strategi aman: Sesuai pedoman resmi BPS Slide 37-38, inflasi perdesaan secara khusus hanya diturunkan dari Indeks Konsumsi Rumah Tangga (IKRT), menghasilkan angka 0,40%.

**12.3.1 — Terbalik menempatkan pembilang dan penyebut pada rasio NTP**

- Jebakan: Membagi harga yang dibayar petani dengan harga yang diterima (Ib / It).
- Strategi aman: Ingat prinsip terms of trade: harga yang diterima di atas (pembilang), harga yang dibayar di bawah (penyebut). NTP = (It / Ib) * 100.

**12.3.2 — Mengasumsikan NTP dan NTUP selalu bergerak searah**

- Jebakan: Menyimpulkan bahwa ketika NTUP meningkat, kesejahteraan keluarga petani (NTP) dipastikan ikut membaik.
- Strategi aman: Dekomposisi menunjukkan jika laju inflasi bahan makanan (IKRT) melonjak drastis, NTP dapat turun drastis meskipun NTUP meningkat.

**12.3.2 — Memasukkan upah buruh tani ke dalam indeks konsumsi rumah tangga**

- Jebakan: Menggolongkan upah buruh tani ke dalam IKRT keluarga petani.
- Strategi aman: Upah buruh tani yang dikeluarkan oleh petani pemilik usaha tani merupakan biaya input tenaga kerja langsung dalam proses produksi sehingga masuk ke kelompok BPPBM.

**12.3.3 — Mengelompokkan komoditas sayuran dan cabai ke dalam subsektor tanaman pangan**

- Jebakan: Menganggap cabai merah, bawang merah, dan tomat masuk ke dalam subsektor Tanaman Pangan (NTPR).
- Strategi aman: Sesuai klasifikasi BPS Slide 36: Tanaman Pangan HANYA mencakup Padi dan Palawija (jagung, kedelai, dsb). Sayur-sayuran, buah-buahan, dan tanaman biofarmaka/obat masuk ke subsektor Hortikultura (NTPH).

**12.3.3 — Menghitung rata-rata aritmetika sederhana dari kelima subsektor**

- Jebakan: Menjumlahkan NTP kelima subsektor lalu membaginya langsung dengan 5: (102,5 + 115 + 120 + 108 + 104) / 5 = 109,90.
- Strategi aman: NTP gabungan wajib dihitung menggunakan rata-rata tertimbang (weighted average) berdasarkan bobot diagram timbang SPDT-NTP, bukan rata-rata sederhana.

## Navigasi

- [[04-statistik-produksi-pertanian-dan-industri|← Pertemuan 11: Statistik Produksi Pertanian dan Industri]]
- [[06-ekspor-impor-dan-pariwisata|→ Pertemuan 13: Ekspor-Impor dan Pariwisata]]
- [[_formulas|Rumus lengkap OSL]]
- [[_glossary|Glosarium istilah]]

---

[[_MOC|← Back to MOC]]
