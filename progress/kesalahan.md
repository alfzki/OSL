# Buku Evaluasi Kesalahan (Mistake Book) - OSL

Dokumen ini berfungsi mencatat dan membedah setiap butir soal yang dijawab salah atau ragu-ragu selama sesi latihan soal persiapan ujian **Official Statistics Lanjutan (OSL)**.

---

## 1. Aturan Pengisian Log Kesalahan

Setiap kali menyelesaikan latihan soal:
1. Identifikasi butir soal dengan jawaban keliru atau evaluasi belum sempurna.
2. Klasifikasikan jenis kesalahan:
   - **Konsep**: Tidak memahami teori, batasan definisi BPS, atau cakupan indikator.
   - **Rumus**: Salah menerapkan rumus, lupa konstanta penimbang, atau tertukar pembilang/penyebut.
   - **Ketelitian**: Keliru membaca soal (misal mengabaikan kata *kecuali*, salah konversi satuan/skala).
   - **Hafalan**: Lupa klasifikasi baku (misal rincian ICLS 13, batas tenaga kerja industri, atau periode referensi survei).
3. Tuliskan akar masalah dan tindakan perbaikan (rujuk berkas di `extracted/` atau slide terkait).
4. Tandai butir soal pada `progress/tracker.json` agar masuk dalam siklus *spaced repetition* berikutnya (1, 3, 7, 14 hari).

---

## 2. Tabel Ringkasan Riwayat Kesalahan

| No | Tanggal | ID Soal | Topik / Bab | Jenis Kesalahan | Status Remedial |
|:---:|:---:|:---:|:---|:---|:---:|
| 1 | 2026-09-29 | **OSL-P09-PG-002** | Ketenagakerjaan (P9) | **Konsep**: Klasifikasi Bukan Angkatan Kerja | **Tuntas (Lulus Remedial)** |
| 2 | 2026-09-29 | **OSL-P11-HIT-004** | Nilai Tukar Petani (P11/P12) | **Rumus & Ketelitian**: Skala pengali & makna NTP | Menunggu Siklus Ulang |
| 3 | 2026-09-29 | **OSL-P12-PG-005** | Indikator Harga & IHK (P12) | **Konsep/Hafalan**: Sumber diagram timbang IHK | **Tuntas (Lulus Remedial)** |
| 4 | 2026-09-29 | **OSL-P08-ESAI-007** | Kemiskinan FGT (P8) | **Konsep**: Perbedaan P1 vs P2 dan implikasi kebijakan | **Tuntas (Lulus Remedial)** |
| 5 | 2026-09-29 | **OSL-UAS22-ISN-009** | Indikator Harga & IHK (P12) | **Konsep**: Sumber penimbang Modified Laspeyres | **Tuntas (Lulus Remedial)** |
| 6 | 2026-09-29 | **OSL-P09-HIT-013** | Ketenagakerjaan (P9) | **Rumus**: Penyebut TPAK (PUK) vs TPT (Angkatan Kerja) | **Tuntas (Lulus Remedial)** |
| 7 | 2026-09-29 | **OSL-P10-PG-015** | Kesehatan & Morbiditas (P10) | **Hafalan**: Periode referensi morbiditas Susenas | **Tuntas (Lulus Remedial)** |
| 8 | 2026-09-29 | **OSL-P11-ISN-017** | Statistik Industri (P11) | **Hafalan/Konsep**: Batasan tenaga kerja IBS vs IMK | **Tuntas (Lulus Remedial)** |
| 9 | 2026-09-29 | **OSL-REM-01** | Ketenagakerjaan (P9) | **Konsep**: Batas Bekerja (1 jam) vs Pekerja Penuh (35 jam) | **Tuntas (Lulus Tematik)** |
| 10 | 2026-09-29 | **OSL-REM-02** | Nilai Tukar Petani (P11) | **Rumus & Skala**: Skala 100 NTP & makna surplus daya tukar | Menunggu Siklus Ulang |
| 11 | 2026-09-29 | **OSL-REM-05** | Indikator Harga & IHK (P12) | **Cakupan Wilayah**: Cakupan 150 kab/kota SBH 2022 vs 514 | **Tuntas (Lulus Tematik)** |
| 12 | 2026-09-29 | **OSL-REM-09** | Statistik Pertanian (P11) | **Konversi Satuan**: Faktor konversi ubinan ke kuintal/ha (16) vs kg/ha (1600) | Menunggu Siklus Ulang |
| 13 | 2026-09-29 | **OSL-IHK-08** | Indikator Harga & IHK (P12) | **Konsep**: Inflasi Inti target acuan moneter BI (missed 1 opt) | Pemantapan Teori |

---

## 3. Rincian Analisis Per Butir Soal

### [2026-09-29] - OSL-P09-PG-002: Indikator Ketenagakerjaan dan Pendidikan (Pertemuan 9)
- **Soal**: Berdasarkan kerangka ketenagakerjaan ICLS 13 yang diterapkan oleh BPS, manakah kelompok berikut yang TIDAK dikategorikan sebagai Bukan Angkatan Kerja?
- **Jawaban Saya**: C (Penduduk yang mengurus rumah tangga)
- **Kunci Sebenarnya**: **B** (Penduduk yang sementara tidak bekerja namun memiliki ikatan pekerjaan tetap)
- **Sumber Rujukan**: `[Pertemuan 9 Indikator Ketenagakerjaan dan Pendidikan.pptx, slide 12]`
- **Jenis Kesalahan**: **Konsep**
- **Akar Masalah**: Tertukar antara Bukan Angkatan Kerja (Sekolah, Mengurus Rumah Tangga, Lainnya) dengan kelompok Bekerja. Pekerja yang cuti sakit, cuti melahirkan, atau menunggu panen tetapi tetap memiliki ikatan kerja sah (*temporarily absent*) tetap diklasifikasikan sebagai **Bekerja** (Angkatan Kerja).
- **Tindakan Remedial**: Pelajari diagram alir ICLS 13 pada slide 11-12 dan periksa kuesioner Sakernas Rincian 15-18.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-P11-HIT-004: Statistik Produksi & Nilai Tukar Petani (Pertemuan 11/12)
- **Soal**: Diketahui indeks harga yang diterima petani ($I_t$) sebesar 118,50 dan indeks harga yang dibayar petani ($I_b$) sebesar 112,00. Berapakah NTP dan bagaimana interpretasinya?
- **Jawaban Saya**: 1.058 keuntungan yang didapat petani (Evaluasi Mandiri: Benar Separuh)
- **Kunci Sebenarnya**: **105,80** (Petani mengalami surplus daya tukar / menguntungkan karena NTP > 100)
- **Sumber Rujukan**: `[Pertemuan 11 OSL Indikator Ekonomi (1) Produksi.pdf, slide 16]` & `[Pertemuan 12, hal. 31]`
- **Jenis Kesalahan**: **Rumus & Ketelitian**
- **Akar Masalah**: Lupa mengalikan konstanta 100 pada rumus indeks $\text{NTP} = (I_t / I_b) \times 100$, dan menginterpretasikannya sebagai "keuntungan rupiah nominal", padahal NTP adalah ukuran rasio daya tukar relatif terhadap tahun dasar (daya beli produk tani terhadap kebutuhan konsumsi dan sarana produksi membaik).
- **Tindakan Remedial**: Ulangi rumus dasar NTP dan catat bahwa indeks selalu berskala 100.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-P12-PG-005: Indikator Ekonomi: Perdagangan dan Harga (Pertemuan 12)
- **Soal**: Data utama yang menjadi diagram timbang (bobot konsumsi tahun dasar) dalam penghitungan Indeks Harga Konsumen (IHK) metode Modified Laspeyres bersumber dari survei...
- **Jawaban Saya**: D (Survei Sosial Ekonomi Nasional / Susenas)
- **Kunci Sebenarnya**: **A** (Survei Biaya Hidup / SBH)
- **Sumber Rujukan**: `[Pertemuan 12 OSL Indikator Ekonomi (2) Perdagangan&Harga.pdf, slide 12, hal. 14]`
- **Jenis Kesalahan**: **Konsep / Hafalan**
- **Akar Masalah**: Terkecoh karena Susenas juga mengumpulkan data pengeluaran konsumsi rumah tangga, namun secara khusus BPS menyelenggarakan **Survei Biaya Hidup (SBH)** (terakhir SBH 2018 dan SBH 2022 di 150 kabupaten/kota) untuk menyusun paket komoditas dan diagram timbang IHK.
- **Tindakan Remedial**: Baca publikasi IHK BPS bab metodologi mengenai SBH sebagai sumber diagram timbang $W_{t-1}$.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-P08-ESAI-007: Indikator Kemiskinan dan Ketimpangan (Pertemuan 8)
- **Soal**: Jelaskan perbedaan mendasar antara Indeks Kedalaman Kemiskinan ($P_1$) dan Indeks Keparahan Kemiskinan ($P_2$) FGT beserta implikasi kebijakannya!
- **Jawaban Saya**: ......... (Evaluasi Mandiri: Belum Menguasai)
- **Kunci Sebenarnya**: $P_1$ mengukur rata-rata kesenjangan pengeluaran orang miskin terhadap garis kemiskinan (kedalaman defisit konsumsi). Sedangkan $P_2$ mengukur ketimpangan pengeluaran di antara sesama penduduk miskin (pembobotan kuadrat memberi penalti lebih besar pada yang paling miskin/kronis). Implikasi: Bantuan yang hanya menyasar orang miskin di dekat garis kemiskinan menurunkan $P_0$ dan $P_1$ tapi tidak menyentuh $P_2$.
- **Sumber Rujukan**: `[Pertemuan 8 OSL Indikator Sosial (1) Indikator Kemiskinan dan Ketimpangan _ new.pptx, slide 24-28]`
- **Jenis Kesalahan**: **Konsep**
- **Akar Masalah**: Belum menghafal dan memahami filosofi matematis parameter $\alpha=1$ (gap linier) vs $\alpha=2$ (gap kuadratik) pada formula FGT.
- **Tindakan Remedial**: Baca bagian penurunan rumus FGT pada modul Bab 8 dan modul Uji Feynman Modul 1.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-UAS22-ISN-009: Perdagangan dan Harga (Pertemuan 12)
- **Soal**: Metode indeks harga yang digunakan BPS dalam penghitungan IHK adalah Modified Laspeyres, di mana penimbang tahun dasar bersumber dari survei...
- **Jawaban Saya**: survei harga barang
- **Kunci Sebenarnya**: **Survei Biaya Hidup (SBH)**
- **Sumber Rujukan**: `[Soal UAS 2022-2023.pdf, hal. 4]` & `[Pertemuan 12, slide 12]`
- **Jenis Kesalahan**: **Konsep**
- **Akar Masalah**: Menjawab deskriptif umum "survei harga barang" padahal yang ditanyakan adalah nama survei resmi BPS penyedia diagram timbang konsumsi, yaitu Survei Biaya Hidup (SBH).
- **Tindakan Remedial**: Tautkan ingatan: IHK = Harga rutin (Survei Harga Konsumen/HK) $\times$ Penimbang (SBH).
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-P09-HIT-013: Indikator Ketenagakerjaan dan Pendidikan (Pertemuan 9)
- **Soal**: PUK (15+) = 20.000 jiwa. Bekerja = 12.000, Pengangguran = 1.000, Sekolah = 4.000, Mengurus RT = 3.000. Hitunglah TPAK dan TPT!
- **Jawaban Saya**: 60% 5% (Evaluasi Mandiri: Belum Menguasai)
- **Kunci Sebenarnya**: **TPAK = 65,00%** dan **TPT = 7,69%**
- **Sumber Rujukan**: `[Pertemuan 9 Indikator Ketenagakerjaan dan Pendidikan.pptx, slide 13-15]`
- **Jenis Kesalahan**: **Rumus**
- **Akar Masalah**:
  1. Salah menghitung Angkatan Kerja: $\text{AK} = 12.000 + 1.000 = 13.000$ (bukan hanya yang bekerja).
  2. $\text{TPAK} = (\text{AK} / \text{PUK}) \times 100\% = (13.000 / 20.000) \times 100\% = 65,00\%$.
  3. Salah pembagi TPT: Pembagi TPT adalah **Angkatan Kerja**, bukan PUK! $\text{TPT} = (1.000 / 13.000) \times 100\% = 7,69\%$ (bukan $1.000 / 20.000 = 5\%$).
- **Tindakan Remedial**: Garis bawahi: Pembagi TPT selalu Angkatan Kerja ($Bekerja + Penganggur$), jangan pernah membagi pengangguran dengan total PUK.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-P10-PG-015: Indikator Kesehatan (Pertemuan 10)
- **Soal**: Dalam statistik kesehatan Susenas BPS, Morbiditas (Angka Kesakitan) mengukur persentase penduduk yang mengalami keluhan kesehatan yang mengganggu kegiatan sehari-hari dalam kurun waktu referensi...
- **Jawaban Saya**: A (1 minggu terakhir)
- **Kunci Sebenarnya**: **B** (1 bulan terakhir)
- **Sumber Rujukan**: `[Pertemuan 10 Indikator Kesehatan.pptx, slide 32]`
- **Jenis Kesalahan**: **Hafalan**
- **Akar Masalah**: Mengira periode referensi morbiditas sama dengan ketenagakerjaan Sakernas (1 minggu terakhir). Pada Susenas Kesehatan BPS, keluhan kesehatan ditanyakan dalam rentang **1 bulan terakhir**.
- **Tindakan Remedial**: Buat tabel pembeda periode referensi: Sakernas = 1 minggu, Susenas Kesehatan = 1 bulan.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-P11-ISN-017: Statistik Produksi Pertanian dan Industri (Pertemuan 11)
- **Soal**: Dalam klasifikasi statistik industri pengolahan BPS, Industri Besar dan Sedang (IBS) didefinisikan sebagai usaha manufaktur dengan tenaga kerja minimal...
- **Jawaban Saya**: (Belum Menjawab)
- **Kunci Sebenarnya**: **20 orang**
- **Sumber Rujukan**: `[Pertemuan 11 OSL Indikator Ekonomi (1) Produksi.pdf, hal. 37]`
- **Jenis Kesalahan**: **Hafalan / Konsep**
- **Akar Masalah**: Lupa batas numerik klasifikasi industri BPS berdasarkan jumlah tenaga kerja.
- **Tindakan Remedial**: Hafalkan batas baku BPS:
  - Industri Mikro: 1 - 4 orang
  - Industri Kecil: 5 - 19 orang
  - **Industri Mikro & Kecil (IMK)**: 1 - 19 orang
  - Industri Sedang: 20 - 99 orang
  - Industri Besar: $\ge 100$ orang
  - **Industri Besar & Sedang (IBS)**: $\ge 20$ orang.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-REM-01: Indikator Ketenagakerjaan (Pertemuan 9)
- **Soal**: Seseorang dikategorikan sebagai 'Bekerja' (ICLS 13 BPS) jika melakukan kegiatan ekonomi untuk memperoleh pendapatan/keuntungan dengan durasi minimal...
- **Jawaban Saya**: D (Minimal 35 jam dalam seminggu terakhir)
- **Kunci Sebenarnya**: **A** (1 jam berturut-turut dalam seminggu terakhir)
- **Sumber Rujukan**: `[Pertemuan 9 Indikator Ketenagakerjaan dan Pendidikan.pptx, slide 12]`
- **Jenis Kesalahan**: **Konsep & Hafalan**
- **Akar Masalah**: Tertukar antara kriteria minimum "Bekerja" (minimal 1 jam dalam seminggu terakhir) dengan batas "Pekerja Penuh" ($\ge 35$ jam seminggu). Seseorang yang bekerja 5 jam seminggu sudah sah berstatus Bekerja (masuk kategori Pekerja Paruh Waktu atau Setengah Penganggur tergantung apakah ia masih mencari kerja).
- **Tindakan Remedial**: Catat tegas hierarki ketenagakerjaan: Bekerja = $\ge 1$ jam seminggu. Pekerja Penuh = $\ge 35$ jam. Kurang dari 35 jam = Paruh waktu / Setengah penganggur.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-REM-02: Nilai Tukar Petani - NTP (Pertemuan 11)
- **Soal**: Jika $I_t = 116,38$ dan $I_b = 110,00$, berapakah nilai NTP dan interpretasinya?
- **Jawaban Saya**: B (NTP = 1,058; Keuntungan absolut sebesar Rp1.058 per komoditas)
- **Kunci Sebenarnya**: **A** (NTP = 105,80; Petani surplus daya tukar 5,80% terhadap tahun dasar)
- **Sumber Rujukan**: `[Pertemuan 11 Indikator Ekonomi - Produksi.pptx, slide 28]`
- **Jenis Kesalahan**: **Rumus & Skala**
- **Akar Masalah**: Masih memperlakukan indeks sebagai rasio desimal murni tanpa mengalikan 100, dan mengartikannya sebagai "rupiah keuntungan", padahal NTP adalah angka indeks harga relatif terhadap tahun dasar.
- **Tindakan Remedial**: Selalu ingat formula berbobot 100: $\text{NTP} = \frac{I_t}{I_b} \times 100$. Jika $\text{NTP} > 100$, petani mengalami surplus daya beli sebesar $(\text{NTP} - 100)\%$.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-REM-05: Indikator Harga & IHK (Pertemuan 12)
- **Soal**: Berapakah jumlah kota/kabupaten yang dicakup dalam penghitungan IHK tahun dasar 2022 ($2022=100$)?
- **Jawaban Saya**: D (514 seluruh kabupaten/kota se-Indonesia)
- **Kunci Sebenarnya**: **A** (150 kabupaten/kota: 90 kota lama + 60 kabupaten baru)
- **Sumber Rujukan**: `[Pertemuan 12 Indikator Ekonomi - Perdagangan dan Harga.pptx, slide 22; Publikasi IHK BPS 2025]`
- **Jenis Kesalahan**: **Cakupan Wilayah / Fakta BPS**
- **Akar Masalah**: Mengira BPS melakukan survei harga konsumen untuk IHK di seluruh 514 kabupaten/kota se-Indonesia. Penghitungan IHK BPS berbasis sampel wilayah hasil Survei Biaya Hidup (SBH).
- **Tindakan Remedial**: Hafalkan kronologi cakupan kota IHK BPS:
  - SBH 2007: 66 kota
  - SBH 2012: 82 kota
  - SBH 2018: 90 kota
  - **SBH 2022 (tahun dasar saat ini): 150 kabupaten/kota**.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)

---

### [2026-09-29] - OSL-REM-09: Metode Ubinan Pertanian (Pertemuan 11)
- **Soal**: Berapakah faktor konversi (pengali) hasil timbangan ubinan ($2,5\text{ m} \times 2,5\text{ m}$) ke produktivitas per hektar dalam kuintal/ha?
- **Jawaban Saya**: B (1.600 langsung dalam kuintal)
- **Kunci Sebenarnya**: **A** (16 ke kuintal/ha; atau 1.600 ke kg/ha)
- **Sumber Rujukan**: `[Pertemuan 11 Indikator Ekonomi - Produksi.pptx, slide 16]`
- **Jenis Kesalahan**: **Konversi Satuan**
- **Akar Masalah**: Angka 1.600 adalah jumlah plot per hektar ($10.000 / 6,25 = 1.600$), sehingga jika dikalikan hasil timbangan dalam kg, satuannya masih **kg/ha**. Untuk mengubah ke kuintal/ha harus dibagi 100 ($1.600 / 100 = 16$), dan untuk ke ton/ha harus dibagi 1.000 ($1.600 / 1.000 = 1,6$).
- **Tindakan Remedial**:
  - Hasil kg ubinan $\times 1.600 \rightarrow$ **kg/ha**
  - Hasil kg ubinan $\times 16 \rightarrow$ **kuintal/ha**
  - Hasil kg ubinan $\times 1,6 \rightarrow$ **ton/ha**.
- **Jadwal Review Berikutnya**: 2026-09-30 (Interval Hari ke-1)
