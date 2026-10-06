---
tags: [osl, ppt-9, universitas]
chapter: 9
status: draft
points: 6
---

# Pertemuan 9: Ketenagakerjaan dan Pendidikan

> Modul ini diturunkan dari `internal/lessons/chapter-09/*.json`.
> `status: draft` karena belum ada sesi belajar yang tercatat pada `progress/tracker.json`.

## Konsep

### 9.1.1 Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja

- **Seksi**: 9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 4-20] [Kuesioner_SAK.AGS25-AK.md, slide/hal. 15-22]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai dekomposisi piramida ketenagakerjaan ICLS 13, definisi bekerja minimal 1 jam, pemilahan AK vs BAK, dan penerapan aturan prioritas ketenagakerjaan pada Sakernas BPS.

**Intuisi** — Kerangka ketenagakerjaan membagi seluruh penduduk ke dalam piramida aktivitas ekonomi. Ambang batas 'bekerja minimal 1 jam tanpa putus dalam seminggu terakhir' diadopsi dari standar internasional ILO (ICLS 13) dengan filosofi inklusivitas: menangkap setiap sumbangan marginal terhadap produksi nasional barang dan jasa, sekecil apa pun jam kerjanya. Aturan prioritas menetapkan bahwa kegiatan ekonomi (bekerja atau mencari kerja) mengalahkan kegiatan non-ekonomi (sekolah atau mengurus rumah tangga).

**Definisi BPS** — Penduduk Usia Kerja (PUK) adalah seluruh penduduk berumur 15 tahun ke atas. PUK terbagi menjadi Angkatan Kerja (AK) dan Bukan Angkatan Kerja (BAK). Bekerja adalah kegiatan ekonomi yang dilakukan seseorang dengan maksud memperoleh atau membantu memperoleh pendapatan/keuntungan, paling sedikit 1 jam secara tidak terputus dalam seminggu terakhir. Bekerja juga mencakup pekerja keluarga tak dibayar (unpaid worker) dan mereka yang sementara tidak bekerja karena sakit, cuti, atau mogok.

**Syarat & batas** — 1. Batas umur PUK di Indonesia sejak 1998 adalah >= 15 tahun (sebelumnya >= 10 tahun). Pekerja anak (< 15 tahun) tidak dimasukkan dalam statistik resmi PUK/AK.
2. Bekerja minimal 1 jam harus dalam kurun waktu 7 hari terakhir (reference period).
3. Pekerja yang sementara tidak bekerja (cuti sakit, cuti melahirkan, menunggu panen) tetap diklasifikasikan sebagai Bekerja, bukan Pengangguran.
4. Persamaan identitas demografi ketenagakerjaan: PUK = AK + BAK = (Bekerja + Penganggur) + (Sekolah + Mengurus Rumah Tangga + Lainnya).

**Rumus** — $$\text{Populasi} = \text{PUK} + \text{BUK}, \quad \text{PUK} = \text{AK} + \text{BAK}, \quad \text{AK} = \text{Bekerja} + \text{Penganggur}$$

### 9.1.2 Tingkat Partisipasi Angkatan Kerja TPAK

- **Seksi**: 9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 13-14] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 21-23]
- **Cakupan**: COVERED

**Fokus ujian** — Formula resmi TPAK, perhitungan bobot disagregasi wilayah/gender, analisis dinamika penawaran tenaga kerja (labor supply), dan interpretasi tren TPAK BPS.

**Intuisi** — TPAK mengukur proporsi penduduk usia kerja yang benar-benar terjun ke gelanggang pasar kerja, baik yang sudah berhasil mendapatkan pekerjaan maupun yang masih aktif mencari kerja. TPAK merupakan indikator utama dari sisi penawaran tenaga kerja (labor supply side). Jika TPAK naik, ekonomi memiliki lebih banyak tangan produktif; namun jika tidak diimbangi penciptaan lapangan kerja, kenaikan TPAK dapat memicu lonjakan angka pengangguran.

**Definisi BPS** — Tingkat Partisipasi Angkatan Kerja (TPAK) adalah persentase penduduk usia 15 tahun ke atas yang merupakan angkatan kerja terhadap seluruh penduduk usia 15 tahun ke atas. Sumber data resmi diperoleh dari Survei Angkatan Kerja Nasional (SAKERNAS).

**Syarat & batas** — 1. Rentang matematis: $0\% \le \text{TPAK} \le 100\%$. Pada praktiknya di Indonesia, TPAK berkisar antara 67% hingga 70%.
2. Pembagi mutlak: Penduduk Usia Kerja (PUK, 15+ tahun). Pembagian dengan total populasi (0+ tahun) adalah kekeliruan fatal.
3. Disagregasi gender: TPAK laki-laki konsisten jauh lebih tinggi (~83%) dibanding perempuan (~54%), karena sebagian besar perempuan yang tidak bekerja berada di kelompok mengurus rumah tangga (BAK).
4. Disagregasi wilayah: TPAK perdesaan umumnya lebih tinggi dibanding perkotaan karena dominasi sektor pertanian keluarga.

**Rumus** — $$\text{TPAK} = \frac{\text{AK}}{\text{PUK}} \times 100\% = \frac{\text{Bekerja} + \text{Penganggur}}{\text{Penduduk Usia } \ge 15 \text{ Tahun}} \times 100\%$$

### 9.1.3 Tingkat Pengangguran Terbuka TPT

- **Seksi**: 9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 15-16] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 21-23]
- **Cakupan**: COVERED

**Fokus ujian** — Definisi 4 kategori penganggur BPS, rekonstruksi soal hitungan esai UAS, rumus TPT terhadap AK, dan analisis dampak ekonomi makro (Okun's law context).

**Intuisi** — TPT mengukur sejauh mana pasokan tenaga kerja yang telah aktif di bursa kerja gagal diserap oleh aktivitas ekonomi. TPT bukan cerminan dari seluruh orang yang tidak bekerja, melainkan hanya mereka yang 'siap dan berupaya' bekerja tetapi belum memperoleh pekerjaan. Oleh sebab itu, pembagi TPT adalah Angkatan Kerja (AK), bukan total penduduk usia kerja.

**Definisi BPS** — Tingkat Pengangguran Terbuka (TPT) adalah persentase jumlah pengangguran terhadap jumlah angkatan kerja. Pengangguran Terbuka BPS terdiri atas 4 kategori: (1) Penduduk yang aktif mencari pekerjaan, (2) Penduduk yang sedang mempersiapkan usaha/pekerjaan baru, (3) Penduduk yang tidak mencari kerja karena merasa tidak mungkin mendapat pekerjaan (discouraged workers / putus asa), dan (4) Penduduk yang sudah memiliki pekerjaan/diterima kerja tetapi belum mulai bekerja (future starts).

**Syarat & batas** — 1. Pembagi resmi: Angkatan Kerja (AK = Bekerja + Pengangguran). Bukan PUK, bukan total penduduk, dan bukan penduduk bekerja.
2. Batasan kategori: Seseorang yang tidak bekerja tetapi tidak mencari pekerjaan karena sedang sekolah atau mengurus rumah tangga TIDAK boleh dimasukkan sebagai pengangguran terbuka (mereka adalah BAK).
3. Kategori 'putus asa' dan 'mempersiapkan usaha' secara eksplisit dihitung sebagai pengangguran terbuka di Indonesia, berbeda dengan definisi ILO murni yang mensyaratkan pencarian kerja aktif.

**Rumus** — $$\text{TPT} = \frac{\text{Penganggur}}{\text{AK}} \times 100\% = \frac{\text{Penganggur}}{\text{Bekerja} + \text{Penganggur}} \times 100\%$$

### 9.1.4 Setengah Penganggur vs Pekerja Paruh Waktu

- **Seksi**: 9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 17-20] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 24-28]
- **Cakupan**: COVERED

**Fokus ujian** — Batas 35 jam kerja normal, perbedaan esensial voluntary vs involuntary part-time, pembagi resmi PB, dan penentuan klasifikasi formal vs informal BPS (EXT-1).

**Intuisi** — Mempunyai pekerjaan tidak serta-merta berarti terhindar dari pemborosan kapasitas tenaga kerja. BPS menetapkan standar jam kerja normal adalah 35 jam per minggu. Pekerja dengan jam kerja < 35 jam dipilah berdasarkan kesukarelaannya: mereka yang masih ingin bekerja lebih banyak jam adalah Setengah Penganggur (involuntary underemployment), sedangkan mereka yang memang puas dengan jam kerja pendek adalah Pekerja Paruh Waktu (voluntary part-time). Selain kuantitas jam, kualitas kerja diukur melalui sektor Formal vs Informal.

**Definisi BPS** — Pekerja Setengah Pengangguran adalah mereka yang bekerja di bawah jam kerja normal (< 35 jam seminggu) dan masih mencari pekerjaan atau masih bersedia menerima pekerjaan tambahan. Pekerja Paruh Waktu adalah mereka yang bekerja < 35 jam seminggu tetapi tidak mencari atau tidak bersedia menerima pekerjaan lain. Sektor informal didefinisikan berdasarkan status pekerjaan berusaha sendiri, berusaha dibantu buruh tidak tetap, pekerja bebas, dan pekerja keluarga tak dibayar.

**Syarat & batas** — 1. Pembagi resmi TSP dan TPPW adalah Penduduk Bekerja (PB), BUKAN Angkatan Kerja (AK) dan BUKAN PUK.
2. Cut-off jam kerja: persis < 35 jam seminggu. Bekerja tepat 35 jam seminggu tergolong jam kerja normal (bekerja penuh).
3. Klasifikasi Formal BPS: Berusaha dibantu buruh tetap dan Buruh/Karyawan/Pegawai selalu formal; Pekerja bebas dan Pekerja keluarga selalu informal; Berusaha sendiri dipilah menurut keahlian jabatan.

**Rumus** — $$\text{TSP} = \frac{\text{PB}_{<35, \text{mencari}}}{\text{PB}} \times 100\%, \quad \text{TPPW} = \frac{\text{PB}_{<35, \text{sukarela}}}{\text{PB}} \times 100\%, \quad \text{Proporsi INF} = \frac{\text{PB}_{\text{INF}}}{\text{PB}} \times 100\%$$

### 9.2.1 Angka Partisipasi Murni APM dan Kasar APK

- **Seksi**: 9.2 Indikator Pendidikan
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 66-71] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 51-55]
- **Cakupan**: COVERED

**Fokus ujian** — Definisi perbedaan pembilang APM vs APK, rentang usia resmi 4 jenjang sekolah, pembuktian ketidaksamaan APM <= APK dan batas APK > 100%, serta aplikasi pada neraca pendidikan BPS.

**Intuisi** — APM mengukur ketepatan usia siswa pada jenjang pendidikannya (apakah anak usia SD bersekolah tepat di SD). Sebaliknya, APK mengukur daya tampung atau kapasitas fisik sistem pendidikan pada jenjang tertentu tanpa memedulikan umur siswa (berapa total kursi siswa yang terisi di SD dibandingkan jumlah anak usia SD). Oleh karena itu, jika ada murid yang masuk sekolah lebih awal (usia dini) atau terlambat/mengulang kelas, pembilang APK akan membengkak sehingga nilai APK dapat melampaui 100%, sementara APM tidak pernah bisa melebihi 100%.

**Definisi BPS** — Angka Partisipasi Murni (APM) adalah proporsi anak kelompok usia sekolah tertentu yang sedang bersekolah tepat di jenjang pendidikan yang seharusnya terhadap penduduk kelompok usia sekolah yang bersangkutan. Angka Partisipasi Kasar (APK) adalah rasio antara jumlah siswa yang bersekolah di suatu jenjang pendidikan tertentu (tanpa memandang usia) terhadap jumlah penduduk kelompok usia sekolah resmi pada jenjang yang sama. Sejak 2007, Susenas turut memperhitungkan Pendidikan Non-Formal (Paket A, Paket B, dan Paket C).

**Syarat & batas** — 1. Kondisi Batas Matematika Kritis:
   - $\text{APM} \le \text{APK}$ (selalu berlaku karena pembilang APM adalah bagian himpunan bagian dari pembilang APK).
   - $\text{APM} \le 100\%$ (mutlak secara teoritis).
   - $\text{APK}$ dapat $> 100\%$ jika terdapat pendaftaran usia dini, terlambat masuk, atau pengulangan kelas.
2. Kelompok umur resmi jenjang BPS: SD (7-12 tahun), SMP (13-15 tahun), SMA/SMK (16-18 tahun), Perguruan Tinggi (19-24 tahun).

**Rumus** — $$\text{APM}_J = \frac{S_{J, \text{usia } J}}{P_{\text{usia } J}} \times 100\%, \quad \text{APK}_J = \frac{\sum_{\text{semua umur}} S_J}{P_{\text{usia } J}} \times 100\%$$

### 9.2.2 Angka Partisipasi Sekolah APS

- **Seksi**: 9.2 Indikator Pendidikan
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 61-65] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 57-60] [Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide/hal. 72-74]
- **Cakupan**: COVERED

**Fokus ujian** — Formula 4 kelompok usia APS, komparasi analitis APM vs APK vs APS, integrasi indikator pendidikan IPM (AMH 15+ dan RLS/MYS) (EXT-2).

**Intuisi** — Jika APM bertanya 'apakah kamu sekolah di jenjang yang benar?', maka APS bertanya lebih mendasar: 'apakah kamu sekolah atau tidak, di jenjang mana pun itu?'. APS memantau hak asasi anak untuk menikmati fasilitas pendidikan formal/kesetaraan pada kelompok umurnya tanpa menghakimi apakah anak tersebut tertinggal kelas atau mengalami percepatan belajar. Indikator outcome pendidikan dalam IPM melengkapinya melalui Angka Melek Huruf (AMH 15+) dan Rata-rata Lama Sekolah (RLS).

**Definisi BPS** — Angka Partisipasi Sekolah (APS) adalah proporsi dari semua anak yang masih bersekolah pada suatu kelompok umur tertentu terhadap jumlah penduduk dengan kelompok umur yang sesuai, tanpa memandang jenjang pendidikan yang sedang ditempuh. Angka Melek Huruf (AMH 15+) adalah persentase penduduk usia 15 tahun ke atas yang dapat membaca dan menulis kalimat sederhana. Rata-rata Lama Sekolah (RLS) adalah jumlah tahun belajar penduduk usia 15 tahun ke atas yang telah diselesaikan dalam pendidikan formal tanpa mengulang.

**Syarat & batas** — 1. Pada APS, jenjang pendidikan tidak dipedulikan: murid usia 13-15 tahun yang masih duduk di bangku SD tetap dihitung dalam pembilang APS 13-15 tahun.
2. Hubungan hirarkis indikator partisipasi: $\text{APM}_J \le \text{APS}_{\text{Usia}(J)} \le 100\%$.
3. Aturan RLS: Tahun mengulang kelas (tinggal kelas) TIDAK dihitung sebagai penambah tahun belajar formal.

**Rumus** — $$\text{APS}_{x-y} = \frac{\sum \text{Siswa Bersekolah Usia } x-y}{P_{x-y}} \times 100\%, \quad \text{AMH}_{15+} = \frac{\text{MH}_{15+}}{P_{15+}} \times 100\%$$

## Contoh Hitung

### 9.1.1 — Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja

Dalam suatu wilayah sensus terdapat total populasi 20.000.000 jiwa. Dari jumlah tersebut, penduduk berusia 0-14 tahun berjumlah 5.000.000 jiwa. Di antara penduduk usia 15 tahun ke atas, tercatat 9.500.000 orang aktif bekerja (termasuk 200.000 pekerja yang sedang cuti/sementara tidak bekerja), 500.000 orang sedang mencari pekerjaan secara aktif, 2.000.000 orang bersekolah penuh waktu, 2.500.000 orang mengurus rumah tangga tanpa kegiatan komersial, dan 500.000 orang lansia/penerima pensiun (lainnya). Hitunglah nilai PUK, AK, BAK, dan buktikan persamaan PUK = AK + BAK.

| Komponen Ketenagakerjaan | Jumlah Jiwa |
|---|---|
| Penduduk Berumur 0-14 Tahun (BUK) | 5.000.000 |
| Penduduk Bekerja (termasuk cuti sementara) | 9.500.000 |
| Pengangguran Terbuka (mencari kerja) | 500.000 |
| Sekolah Penuh Waktu | 2.000.000 |
| Mengurus Rumah Tangga | 2.500.000 |
| Lainnya (Pensiunan/Lansia/Disabilitas) | 500.000 |

**Penyelesaian**

1. Menghitung Penduduk Usia Kerja (PUK):
   $$\text{PUK} = \text{Total Populasi} - \text{BUK} = 20.000.000 - 5.000.000 = 15.000.000$$
2. Menghitung Angkatan Kerja (AK):
   $$\text{AK} = \text{Bekerja} + \text{Pengangguran} = 9.500.000 + 500.000 = 10.000.000$$
3. Menghitung Bukan Angkatan Kerja (BAK):
   $$\text{BAK} = \text{Sekolah} + \text{Mengurus RT} + \text{Lainnya} = 2.000.000 + 2.500.000 + 500.000 = 5.000.000$$
4. Verifikasi Identitas Neraca Tenaga Kerja:
   $$\text{AK} + \text{BAK} = 10.000.000 + 5.000.000 = 15.000.000 = \text{PUK} \quad (\text{Terbukti Identik})$$

**Hasil verifikasi** — `PUK=15000000, AK=10000000, BAK=5000000, Valid=True`

### 9.1.2 — Tingkat Partisipasi Angkatan Kerja TPAK

Dalam publikasi profil ketenagakerjaan Provinsi Harmoni, tercatat data demografi penduduk usia 15 tahun ke atas sbb: Penduduk usia kerja laki-laki berjumlah 5.000.000 jiwa dengan 4.150.000 jiwa di antaranya tergolong angkatan kerja. Penduduk usia kerja perempuan berjumlah 5.000.000 jiwa dengan 2.700.000 jiwa di antaranya tergolong angkatan kerja. Hitunglah: (1) TPAK Laki-laki, (2) TPAK Perempuan, (3) TPAK Total Provinsi, dan (4) Kesenjangan Partisipasi Gender (Gender Gap).

| Kelompok Gender | PUK (15+ Tahun) | Angkatan Kerja (AK) |
|---|---|---|
| Laki-laki | 5.000.000 | 4.150.000 |
| Perempuan | 5.000.000 | 2.700.000 |
| Total Provinsi | 10.000.000 | 6.850.000 |

**Penyelesaian**

1. TPAK Laki-laki:
   $$\text{TPAK}_L = \frac{4.150.000}{5.000.000} \times 100\% = 83,00\%$$
2. TPAK Perempuan:
   $$\text{TPAK}_P = \frac{2.700.000}{5.000.000} \times 100\% = 54,00\%$$
3. TPAK Total Provinsi:
   $$\text{TPAK}_{\text{Total}} = \frac{4.150.000 + 2.700.000}{5.000.000 + 5.000.000} \times 100\% = \frac{6.850.000}{10.000.000} \times 100\% = 68,50\%$$
4. Gender Gap TPAK:
   $$\Delta \text{TPAK} = \text{TPAK}_L - \text{TPAK}_P = 83,00\% - 54,00\% = 29,00\%$$

**Hasil verifikasi** — `TPAK L=83.00%, TPAK P=54.00%, TPAK Total=68.50%, Gap=29.00%`

### 9.1.3 — Tingkat Pengangguran Terbuka TPT

Rekonstruksi Soal UAS 2022/2023 Esai 1 Ketenagakerjaan: Suatu negara berpenduduk 18,0 juta jiwa dengan 4,0 juta jiwa di antaranya belum mencapai usia 15 tahun (BUK). Dari penduduk usia kerja (PUK), 5,0 juta jiwa tergolong bukan angkatan kerja (2,0 juta bersekolah, 2,0 juta mengurus rumah tangga, dan 1,0 juta lainnya). Penduduk yang bekerja berjumlah 7,0 juta orang (6,0 juta bekerja penuh dan 1,0 juta bekerja paruh waktu). Terdapat 1,0 juta orang yang terkena PHK dan sedang aktif mencari kerja, 0,5 juta orang sedang mempersiapkan usaha kedai kopi, serta 0,5 juta orang telah dinyatakan lulus seleksi kerja tetapi baru akan mulai bertugas bulan depan. Hitunglah nilai TPAK dan TPT negara tersebut!

| Komponen Ketenagakerjaan | Jumlah Jiwa (Juta) |
|---|---|
| Total Populasi | 18,0 |
| Bukan Usia Kerja (< 15 Tahun) | 4,0 |
| Penduduk Usia Kerja (PUK >= 15 Tahun) | 14,0 |
| Bukan Angkatan Kerja (Sekolah, IRT, Lainnya) | 5,0 |
| Penduduk Bekerja Penuh (>= 35 jam) | 6,0 |
| Penduduk Bekerja Kurang Jam Kerja (< 35 jam) | 1,0 |
| Penganggur: Terkena PHK mencari kerja | 1,0 |
| Penganggur: Sedang mempersiapkan usaha | 0,5 |
| Penganggur: Sudah diterima kerja belum mulai | 0,5 |

**Penyelesaian**

1. Identifikasi PUK dan Angkatan Kerja (AK):
   $$\text{PUK} = 18,0 - 4,0 = 14,0 \text{ juta jiwa}$$
   $$\text{Total Bekerja (PB)} = 6,0 + 1,0 = 7,0 \text{ juta jiwa}$$
   $$\text{Total Penganggur} = 1,0 + 0,5 + 0,5 = 2,0 \text{ juta jiwa}$$
   $$\text{Angkatan Kerja (AK)} = \text{PB} + \text{Penganggur} = 7,0 + 2,0 = 9,0 \text{ juta jiwa}$$
2. Perhitungan TPAK:
   $$\text{TPAK} = \frac{\text{AK}}{\text{PUK}} \times 100\% = \frac{9,0}{14,0} \times 100\% = 64,2857\% \approx 64,29\%$$
3. Perhitungan TPT:
   $$\text{TPT} = \frac{\text{Penganggur}}{\text{AK}} \times 100\% = \frac{2,0}{9,0} \times 100\% = 22,2222\% \approx 22,22\%$$

**Hasil verifikasi** — `TPAK=64.29%, TPT=22.22%`

### 9.1.4 — Setengah Penganggur vs Pekerja Paruh Waktu

Melanjutkan Soal UAS 2022/2023 Esai 1 dan integrasi EXT-1: Dari 7,0 juta penduduk yang bekerja, terdapat 5,0 juta orang bekerja penuh (>= 35 jam). Dari 2,0 juta orang yang bekerja < 35 jam seminggu, 1,0 juta orang masih aktif mencari pekerjaan tambahan (setengah penganggur), sedangkan 1,0 juta orang lainnya puas dengan jam kerjanya (pekerja paruh waktu sukarela). Di samping itu, berdasarkan audit status pekerjaan, terdapat 3,5 juta pekerja berstatus informal (pekerja bebas, pekerja keluarga, dan pedagang keliling mandiri) dan 3,5 juta pekerja formal. Hitunglah: (1) Tingkat Setengah Pengangguran (TSP), (2) Tingkat Pekerja Paruh Waktu (TPPW), dan (3) Proporsi Tenaga Kerja Informal.

| Klasifikasi Pekerja | Jumlah (Juta Jiwa) | Pembagi Resmi BPS |
|---|---|---|
| Bekerja Penuh (>= 35 Jam) | 5,0 | Penduduk Bekerja (PB = 7,0) |
| Setengah Penganggur (< 35 Jam, Masih Mencari) | 1,0 | Penduduk Bekerja (PB = 7,0) |
| Pekerja Paruh Waktu (< 35 Jam, Sukarela) | 1,0 | Penduduk Bekerja (PB = 7,0) |
| Pekerja Sektor Informal | 3,5 | Penduduk Bekerja (PB = 7,0) |
| Total Penduduk Bekerja (PB) | 7,0 | - |

**Penyelesaian**

1. Menghitung Tingkat Setengah Pengangguran (TSP):
   $$\text{TSP} = \frac{1,0}{7,0} \times 100\% = 14,2857\% \approx 14,29\%$$
2. Menghitung Tingkat Pekerja Paruh Waktu (TPPW):
   $$\text{TPPW} = \frac{1,0}{7,0} \times 100\% = 14,2857\% \approx 14,29\%$$
3. Menghitung Proporsi Tenaga Kerja Informal:
   $$\text{Proporsi INF} = \frac{3,5}{7,0} \times 100\% = 50,00\%$$

**Hasil verifikasi** — `TSP=14.29%, TPPW=14.29%, Proporsi Informal=50.00%`

### 9.2.1 — Angka Partisipasi Murni APM dan Kasar APK

Verifikasi Batas Kritis BVA Pendidikan (test_bva_06): Di suatu distrik pendidikan, populasi anak usia resmi sekolah dasar (7-12 tahun) berjumlah 1.000 orang. Data dinas pendidikan mencatat total siswa yang terdaftar di jenjang SD adalah 1.060 anak, yang terdiri atas 40 anak berusia di bawah 7 tahun (masuk dini), 920 anak berusia 7-12 tahun (usia tepat jenjang), dan 100 anak berusia di atas 12 tahun (tinggal kelas/terlambat). Hitunglah nilai APM SD dan APK SD distrik tersebut, serta buktikan kondisi batas APM <= 100%, APM <= APK, dan APK > 100%!

| Komponen Siswa / Penduduk | Jumlah Anak |
|---|---|
| Penduduk Usia Resmi SD (7-12 Tahun) | 1.000 |
| Siswa SD Berusia Tepat (7-12 Tahun) | 920 |
| Siswa SD Berusia Dini (< 7 Tahun) | 40 |
| Siswa SD Berusia Lebih (> 12 Tahun) | 100 |
| Total Seluruh Siswa Terdaftar di SD | 1.060 |

**Penyelesaian**

1. Menghitung Angka Partisipasi Murni (APM) SD:
   $$\text{APM}_{\text{SD}} = \frac{\text{Siswa SD Usia 7-12}}{\text{Penduduk Usia 7-12}} \times 100\% = \frac{920}{1.000} \times 100\% = 92,00\%$$
2. Menghitung Angka Partisipasi Kasar (APK) SD:
   $$\text{APK}_{\text{SD}} = \frac{\text{Total Siswa Terdaftar di SD}}{\text{Penduduk Usia 7-12}} \times 100\% = \frac{1.060}{1.000} \times 100\% = 106,00\%$$
3. Verifikasi Kondisi Batas Matematika BPS:
   - $\text{APM} = 92,00\% \le 100\%$ (Terpenuhi)
   - $\text{APM} (92,00\%) \le \text{APK} (106,00\%)$ (Terpenuhi)
   - $\text{APK} = 106,00\% > 100\%$ (Menunjukkan kapasitas sistem menampung siswa di luar usia standar)

**Hasil verifikasi** — `APM=92.00%, APK=106.00%, APM<=APK=True, APK>100=True`

### 9.2.2 — Angka Partisipasi Sekolah APS

Di sebuah perdesaan terpencil terdapat 500 orang penduduk berusia 13-15 tahun (usia kelompok SMP). Berdasarkan pencacahan Susenas: 380 anak bersekolah tepat di jenjang SMP/MTs, 40 anak masih duduk di bangku SD karena terlambat masuk, 10 anak bersekolah akselerasi di jenjang SMA, dan 70 anak sudah putus sekolah. Di samping itu, dari 2.000 penduduk usia 15 tahun ke atas, terdapat 1.900 orang yang melek huruf. Hitunglah: (1) Total anak usia 13-15 tahun yang masih bersekolah, (2) APS 13-15 tahun, (3) APM SMP, dan (4) AMH 15+ desa tersebut!

| Kelompok Penduduk / Siswa | Jumlah Jiwa |
|---|---|
| Penduduk Usia 13-15 Tahun | 500 |
| Siswa Usia 13-15 di Jenjang SMP/MTs | 380 |
| Siswa Usia 13-15 di Jenjang SD | 40 |
| Siswa Usia 13-15 di Jenjang SMA | 10 |
| Anak Usia 13-15 Tidak Bersekolah Lagi | 70 |
| Penduduk Usia 15 Tahun ke Atas (P15+) | 2.000 |
| Penduduk Usia 15+ yang Melek Huruf (MH15+) | 1.900 |

**Penyelesaian**

1. Menghitung Total Penduduk 13-15 Tahun yang Masih Bersekolah:
   $$\text{Total Siswa}_{13-15} = 380 (\text{SMP}) + 40 (\text{SD}) + 10 (\text{SMA}) = 430 \text{ anak}$$
2. Menghitung Angka Partisipasi Sekolah (APS 13-15):
   $$\text{APS}_{13-15} = \frac{430}{500} \times 100\% = 86,00\%$$
3. Menghitung Angka Partisipasi Murni (APM SMP):
   $$\text{APM}_{\text{SMP}} = \frac{380}{500} \times 100\% = 76,00\%$$
   *Buktinya: $\text{APM SMP} (76,00\%) \le \text{APS}_{13-15} (86,00\%)$ terpenuhi.*
4. Menghitung Angka Melek Huruf (AMH 15+):
   $$\text{AMH}_{15+} = \frac{1.900}{2.000} \times 100\% = 95,00\%$$

**Hasil verifikasi** — `Total Sekolah=430, APS=86.00%, APM SMP=76.00%, AMH=95.00%`

## Jebakan Ujian

**9.1.1 — Aturan Prioritas ICLS terhadap Mahasiswa/IRT yang Bekerja Marginal**

- Jebakan: Menggolongkan mahasiswa atau ibu rumah tangga yang bekerja 2 jam seminggu sebagai Bukan Angkatan Kerja (Sekolah/IRT).
- Strategi aman: Patuhi aturan prioritas ICLS: Kegiatan ekonomi (bekerja minimal 1 jam) mengalahkan kegiatan non-ekonomi. Individu tersebut harus diklasifikasikan sebagai Bekerja (Angkatan Kerja).

**9.1.1 — Pekerja Sementara Tidak Bekerja (Temporarily Absent)**

- Jebakan: Menganggap karyawan yang cuti sakit seminggu penuh atau petani yang menunggu masa tanam sebagai pengangguran terbuka.
- Strategi aman: Selama memiliki ikatan kerja formal atau usaha yang masih aktif beroperasi, individu sementara tidak bekerja tetap tergolong Bekerja.

**9.1.2 — Penyebut TPAK Tertukar dengan Total Penduduk**

- Jebakan: Membagi Angkatan Kerja dengan total populasi (termasuk anak < 15 tahun).
- Strategi aman: Ingat rumus resmi BPS: Pembagi TPAK adalah Penduduk Usia Kerja (PUK >= 15 tahun), BUKAN total penduduk.

**9.1.2 — Kesimpulan Keliru bahwa Perempuan yang Tidak Masuk AK Adalah Pengangguran**

- Jebakan: Mengasumsikan rendahnya TPAK perempuan berarti tingkat pengangguran perempuan sangat tinggi.
- Strategi aman: Perempuan yang tidak berpartisipasi dalam angkatan kerja berada pada kelompok Bukan Angkatan Kerja (terutama mengurus rumah tangga), bukan pengangguran terbuka.

**9.1.3 — Penyebut TPT Dibagi dengan PUK atau PB**

- Jebakan: Menghitung TPT dengan pembagi PUK (misal 2.0 / 14.0 = 14.29%) atau membagi dengan PB (2.0 / 7.0 = 28.57%).
- Strategi aman: Pembagi TPT adalah mutlak Angkatan Kerja (AK = PB + Penganggur = 9.0). Nilai yang benar adalah 2.0 / 9.0 = 22.22%.

**9.1.3 — Mengabaikan 3 Kategori Penganggur Non-Pencari Kerja Aktif**

- Jebakan: Hanya menghitung orang yang aktif melamar pekerjaan (PHK = 1.0 juta) sehingga TPT dihitung 1.0 / 8.0 = 12.5%.
- Strategi aman: Di BPS, orang yang mempersiapkan usaha baru dan orang yang sudah diterima kerja tapi belum mulai bertugas WAJIB dimasukkan ke dalam kelompok pengangguran terbuka.

**9.1.4 — Kesalahan Pembagi TSP/TPPW Menggunakan Angkatan Kerja**

- Jebakan: Membagi jumlah setengah penganggur (1.0) dengan total angkatan kerja (9.0) sehingga memperoleh angka salah 11.11%.
- Strategi aman: Pembagi TSP dan TPPW adalah mutlak PENDUDUK BEKERJA (PB = 7.0 juta), bukan Angkatan Kerja (AK).

**9.1.4 — Menyamakan Setengah Penganggur dengan Pekerja Paruh Waktu**

- Jebakan: Menganggap semua orang yang bekerja < 35 jam sebagai setengah penganggur.
- Strategi aman: Setengah penganggur mensyaratkan kondisi keterpaksaan (masih mencari kerja/tambahan), sedangkan pekerja paruh waktu bersifat sukarela.

**9.2.1 — Mengira Nilai APK di Atas 100% Merupakan Kesalahan Hitung**

- Jebakan: Menganggap hasil hitungan APK sebesar 106% sebagai anomali atau data salah.
- Strategi aman: APK > 100% adalah fenomena lumrah dan sahih dalam statistik BPS karena pembilang mencakup murid di luar batas usia standar.

**9.2.1 — Tertukar Pembilang APM dan APK**

- Jebakan: Memasukkan total seluruh murid ke dalam rumus APM.
- Strategi aman: APM = Murni (hanya murid yang berumur sesuai jenjang). APK = Kasar (seluruh murid tanpa memandang umur).

**9.2.2 — Mengecualikan Siswa di Luar Jenjang Standar dalam Pembilang APS**

- Jebakan: Hanya menghitung siswa yang duduk di SMP saat menghitung APS 13-15 tahun sehingga mendapatkan hasil 380/500 = 76% (ini nilai APM, bukan APS).
- Strategi aman: APS tidak peduli jenjang sekolah: anak usia 13-15 tahun yang duduk di SD maupun SMA wajib dihitung dalam pembilang APS.

**9.2.2 — Memasukkan Tahun Mengulang Kelas ke dalam RLS (MYS)**

- Jebakan: Menambahkan tahun tinggal kelas ke dalam akumulasi Rata-rata Lama Sekolah.
- Strategi aman: Konsep baku BPS secara tegas mengecualikan tahun mengulang dalam perhitungan Rata-rata Lama Sekolah.

## Navigasi

- [[01-kemiskinan-dan-ketimpangan-pendapatan|← Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan]]
- [[03-indikator-kesehatan-dan-sdgs-3|→ Pertemuan 10: Indikator Kesehatan dan SDGs 3]]
- [[_formulas|Rumus lengkap OSL]]
- [[_glossary|Glosarium istilah]]

---

[[_MOC|← Back to MOC]]
