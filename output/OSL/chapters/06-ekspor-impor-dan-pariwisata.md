---
tags: [osl, ppt-13, universitas]
chapter: 13
status: draft
points: 7
---

# Pertemuan 13: Ekspor-Impor dan Pariwisata

> Modul ini diturunkan dari `internal/lessons/chapter-13/*.json`.
> `status: draft` karena belum ada sesi belajar yang tercatat pada `progress/tracker.json`.

## Konsep

### 13.1.1 Valuasi Ekspor Impor FOB vs CIF

- **Seksi**: 13.1 Statistik Perdagangan Internasional
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 4-9]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai prinsip alih kepemilikan ekonomi SNA 2008, perbedaan titik valuasi FOB dan CIF, peran dokumen PEB/PIB Bea Cukai, serta mekanisme konversi kurs beli vs kurs jual BPS.

**Intuisi** — Perdagangan internasional barang melibatkan batas pabean dan pergerakan fisik melintasi samudera atau perbatasan darat. Valuasi perdagangan menentukan di titik mana kepemilikan dan tanggung jawab biaya berpindah: apakah tepat saat barang dinaikkan ke kapal di pelabuhan negara pengekspor (FOB) atau sampai barang berlabuh di pelabuhan negara pengimpor termasuk ongkos kirim dan asuransi (CIF). Tanpa standardisasi valuasi dan kurs konversi, neraca perdagangan dunia akan mengalami asimetri pencatatan.

**Definisi BPS** — Ekspor dan impor menurut SNA 2008 didefinisikan sebagai transaksi alih kepemilikan ekonomi atas barang dan jasa antara penduduk (resident) suatu perekonomian dengan bukan penduduk (non-resident). Dalam statistik perdagangan barang internasional (IMTS) resmi BPS: Ekspor barang dinilai atas dasar Free on Board (FOB), yaitu nilai barang di atas kapal di pelabuhan muat eksportir; Impor barang dicatat atas dasar Cost, Insurance, and Freight (CIF), mencakup harga barang FOB ditambah biaya asuransi dan pengangkutan antarnegara hingga pelabuhan bongkar importir. Data dihimpun dari dokumen Pemberitahuan Ekspor Barang (PEB) dan Pemberitahuan Impor Barang (PIB) Ditjen Bea dan Cukai, lalu dikonversi ke Rupiah menggunakan kurs transaksi tertimbang nominal bulanan: kurs beli untuk ekspor dan kurs jual untuk impor.

**Syarat & batas** — Nilai CIF selalu lebih besar atau sama dengan nilai FOB (CIF = FOB + Freight + Insurance). Jika pengangkutan dan asuransi bernilai nol (misal perbatasan darat langsung), maka CIF = FOB. Untuk kompilasi PDB dan Neraca Pembayaran (BOP/SNA), impor barang wajib disesuaikan kembali dari CIF menjadi FOB agar komponen asuransi dan freight dapat direklasifikasi ke neraca jasa.

**Rumus** — $$\text{CIF} = \text{FOB} + \text{Freight} + \text{Insurance}, \quad X_{\text{IDR}} = X_{\text{USD}} \times \bar{K}_{\text{beli}}, \quad M_{\text{IDR}} = M_{\text{USD}} \times \bar{K}_{\text{jual}}$$

### 13.1.2 Barang Dagangan Tanpa Masuk Pabean Merchanting

- **Seksi**: 13.1 Statistik Perdagangan Internasional
- **Prioritas**: Sedang
- **Rujukan**: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 5, 10-15]
- **Cakupan**: COVERED

**Fokus ujian** — Memahami konsep merchanting goods SNA 2008, 3 syarat utama transaksi merchanting, perlakuan 'ekspor negatif' dan 'ekspor positif', serta reklasifikasi pos dari neraca jasa (BPM5) ke neraca barang (BPM6/SNA 2008).

**Intuisi** — Di era globalisasi rantai pasok, seorang pengusaha di Jakarta bisa membeli biji kopi dari petani di Vietnam lalu menjualnya langsung ke pemanggang kopi di Jerman tanpa kapal kargo pengangkut biji kopi tersebut pernah singgah di pelabuhan Tanjung Priok. Transaksi ini dinamakan merchanting. Karena pedagang Indonesia secara hukum memiliki barang tersebut dan memperoleh margin keuntungan dagang, transaksi ekonomi riil telah terjadi dan wajib dicatat dalam statistik resmi meskipun petugas Bea Cukai Indonesia tidak pernah melihat fisik barangnya.

**Definisi BPS** — Merchanting menurut standar SNA 2008 dan Manual Neraca Pembayaran Edisi Ke-6 (BPM6) adalah kegiatan pembelian barang oleh penduduk (resident merchant) suatu perekonomian dari bukan penduduk (non-resident), untuk selanjutnya dijual kembali kepada bukan penduduk di negara lain, di mana barang tersebut tidak pernah memasuki wilayah ekonomi atau batas pabean residen merchant. Syarat merchanting: (1) terjadi alih kepemilikan ekonomi barang kepada residen merchant, (2) tidak ada transformasi substansial pada barang, dan (3) barang tidak melintasi perbatasan pabean negara residen merchant.

**Syarat & batas** — Jika barang diubah bentuk atau diolah secara fisik (misal biji kopi disangrai dan dikemas menjadi produk kopi instan oleh pihak ketiga di luar negeri atas kendali merchant), maka transaksi masuk ke klasifikasi 'manufaktur atas kontrak / processing fees' bukan merchanting murni. Dalam pencatatan statistik, perolehan barang dicatat sebagai ekspor barang negatif (-USD) dan penjualan dicatat sebagai ekspor barang positif (+USD); selisihnya adalah Ekspor Neto Barang di bawah Merchanting.

**Rumus** — $$\text{Ekspor Neto Merchanting} = X_{\text{merchanting (penjualan)}} - M_{\text{merchanting (perolehan)}} = X_{\text{positif}} + X_{\text{negatif}}$$

### 13.1.3 Net Barter Terms of Trade NBToT

- **Seksi**: 13.1 Statistik Perdagangan Internasional
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 10-16]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai formulasi dan interpretasi Net Barter Terms of Trade (NBToT), formula dan 4 tahapan siklus produk Indeks Spesialisasi Perdagangan (ISP), serta formulasi Revealed Comparative Advantage (Balassa RCA) dan Openness Ratio.

**Intuisi** — Jika suatu negara mengekspor minyak kelapa sawit dan mengimpor gandum, apakah posisi tawar ekonominya semakin menguntungkan dari tahun ke tahun? Net Barter Terms of Trade (NBToT) mengukur daya beli satu unit fisik ekspor terhadap barang impor. Jika harga ekspor naik lebih cepat daripada harga impor (NBToT > 100), negara tersebut cukup mengapalkan lebih sedikit komoditas ekspor untuk membiayai jumlah barang impor yang sama (terjadi efek kekayaan / wealth effect). Sebaliknya, Indeks Spesialisasi Perdagangan (ISP) dan Balassa RCA mengukur apakah komoditas kita memiliki keunggulan kompetitif di panggung global.

**Definisi BPS** — Net Barter Terms of Trade (NBToT / Indeks Nilai Tukar Perdagangan Internasional) adalah rasio antara indeks harga ekspor (Px atau IIX - Indeks Implisit Ekspor) dengan indeks harga impor (Pm atau IIM - Indeks Implisit Impor), dinyatakan dalam persentase dengan basis tahun dasar = 100. NBToT > 100 menunjukkan perbaikan nilai tukar perdagangan (favourable terms of trade). Indeks Spesialisasi Perdagangan (ISP / Trade Specialisation Ratio) adalah rasio antara selisih ekspor-impor komoditas tertentu terhadap jumlah total perdagangannya: ISP = (X_i - M_i) / (X_i + M_i), dengan kisaran rentang [-1, +1] yang membagi siklus produk menjadi 4 tahapan: Pengenalan [-1.0 s.d. -0.5], Substitusi Impor (-0.5 s.d. 0.0], Perluasan Ekspor (0.0 s.d. 0.8], dan Pematangan (0.8 s.d. 1.0]. Revealed Comparative Advantage (RCA Balassa) membandingkan pangsa ekspor komoditas nasional terhadap pangsa ekspor komoditas tersebut di tingkat dunia, di mana nilai RCA >= 1 mengindikasikan keunggulan komparatif yang terungkap.

**Syarat & batas** — NBToT berkisar > 0 (umumnya berfluktuasi di sekitar 100). ISP berada pada interval tertutup [-1,0, +1,0]. Jika X = 0 (hanya impor), ISP = -1. Jika M = 0 (hanya ekspor), ISP = +1. Jika X = M, ISP = 0. RCA Balassa bernilai non-negatif [0, tak terhingga); ambang batas keunggulan komparatif adalah RCA = 1,0.

**Rumus** — $$\text{NBToT} = \frac{P_x}{P_m} \times 100, \quad \text{ISP}_i = \frac{X_i - M_i}{X_i + M_i}, \quad \text{RCA}_{ij} = \frac{X_{ij} / X_j}{X_{iw} / X_w}, \quad \text{Openness} = \frac{X_t + M_t}{\text{PDB}_t} \times 100\%$$

### 13.1.4 Gross Barter dan Income ToT

- **Seksi**: 13.1 Statistik Perdagangan Internasional
- **Prioritas**: Sedang
- **Rujukan**: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 15, 25-28] [SUPLEMEN: suplemen]
- **Cakupan**: SUPPLEMENTED

**Fokus ujian** — Menguasai perbedaan analitis antara Net Barter ToT, Gross Barter ToT [SUPLEMEN], dan Income ToT / Kapasitas Impor (KM), serta interpretasi kondisi di mana NBToT turun namun Kapasitas Impor naik.

**Intuisi** — NBToT hanya memberi tahu perbandingan harga satuan ekspor vs impor, tetapi mengabaikan berapa banyak barang yang sanggup kita jual. Bayangkan seorang pedagang yang menurunkan harga jual barangnya sebesar 5%, namun berhasil melipatgandakan volume penjualannya hingga 50%. Meskipun margin per unitnya menyusut (NBToT turun), uang kas yang dibawanya pulang melonjak drastis sehingga daya belinya untuk memborong barang impor meningkat. Konsep inilah yang ditangkap oleh Income Terms of Trade atau Kapasitas Impor (KM). Di sisi lain, Gross Barter Terms of Trade (GBToT) melihat pertukaran fisik murni: berapa kontainer impor yang masuk dibanding berapa kontainer ekspor yang keluar.

**Definisi BPS** — Kapasitas Impor (KM / Capacity to Import / Income Terms of Trade) menurut metodologi statistik BPS adalah ukuran kemampuan devisa hasil ekspor untuk membiayai impor barang, yang dihitung dengan membagi nilai ekspor atas dasar harga berlaku (ADHB) dengan indeks harga/implisit impor (IIM), atau secara ekivalen: Income ToT = (NBToT * Qx) / 100, di mana Qx adalah indeks volume ekspor. [SUPLEMEN] Gross Barter Terms of Trade (GBToT) adalah rasio antara indeks volume fisik impor (Qm) terhadap indeks volume fisik ekspor (Qx) dikalikan 100 (GBToT = (Qm / Qx) * 100), yang mengukur jumlah fisik barang impor yang diterima per unit fisik barang ekspor dengan memperhitungkan pembayaran sepihak, transfer modal, dan pinjaman luar negeri.

**Syarat & batas** — Income ToT dan GBToT bernilai positif (> 0). Jika pertumbuhan volume ekspor (Qx) melampaui laju penurunan harga relatif (NBToT), maka Income ToT akan meningkat meskipun NBToT memburuk. Pada kondisi neraca perdagangan seimbang tanpa aliran modal (X_nilai = M_nilai), nilai Gross Barter ToT akan bergerak sejalan dengan Net Barter ToT.

**Rumus** — $$\text{Income ToT} = \text{KM} = \frac{\text{NBToT} \times Q_x}{100} = \frac{X_{\text{ADHB}}}{P_m} \times 100, \quad \text{GBToT [SUPLEMEN]} = \frac{Q_m}{Q_x} \times 100$$

### 13.2.1 Definisi Wisman dan Wisnus

- **Seksi**: 13.2 Statistik Pariwisata dan Perhotelan
- **Prioritas**: Sedang
- **Rujukan**: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 32-38]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai definisi operasional wisman UNWTO, pembedaan wisman vs wisnas vs wisnus, kriteria durasi (< 12 bulan) dan non-remunerasi, pembedaan tourist vs excursionist, serta pergeseran konsep wisnus pasca SP 2020.

**Intuisi** — Apakah semua warga negara asing yang turun dari pesawat di Bandara Soekarno-Hatta otomatis dihitung sebagai wisatawan mancanegara? Jawabannya: tidak! Seorang diplomat yang bertugas di kedutaan, seorang ekspatriat yang telah tinggal di Kemang selama 2 tahun, atau seorang insinyur asing yang digaji langsung oleh perusahaan lokal di Cikarang bukanlah wisatawan. Pariwisata secara statistik mensyaratkan perpindahan sementara di luar lingkungan keseharian (usual environment), dengan durasi kurang dari satu tahun, dan tidak mencari nafkah dari perekonomian setempat.

**Definisi BPS** — Wisatawan Mancanegara (wisman / inbound tourist) menurut rekomendasi United Nations World Tourism Organization (UNWTO) dan BPS adalah setiap orang yang melakukan perjalanan ke suatu negara di luar tempat tinggal biasanya (usual country of residence), kurang dari satu tahun (12 bulan), didorong oleh suatu tujuan utama (berlibur, bisnis, berobat, olahraga, atau keperluan pribadi lainnya), selain untuk bekerja dan memperoleh upah dari penduduk negara yang dikunjungi. Pengunjung internasional (visitors) dibagi menjadi: (1) Wisatawan (tourist) yang tinggal minimal 24 jam (menginap di akomodasi setempat), dan (2) Pelancong (excursionist) yang tinggal kurang dari 24 jam tanpa menginap di akomodasi setempat (termasuk penumpang kapal pesiar yang tidur di kapal). Wisatawan Nusantara (wisnus) setelah SP 2020 adalah penduduk Indonesia yang melakukan perjalanan di wilayah Indonesia dengan lama kurang dari 12 bulan di luar usual environment, bukan untuk bekerja rutin atau sekolah rutin.

**Syarat & batas** — WNA yang telah menetap di Indonesia lebih dari 12 bulan berturut-turut telah berstatus sebagai penduduk (resident) Indonesia, sehingga perjalanannya kembali ke Indonesia tidak dicatat sebagai wisman. Diplomat, konsulat, anggota angkatan bersenjata asing yang bertugas, pekerja lintas batas (commuter workers), dan pengungsi dikecualikan dari statistik wisatawan. Durasi batas atas wisata adalah < 365 hari (12 bulan).

**Rumus** — $$\text{Total Pengunjung Mancanegara (Visitors)} = \text{Wisatawan (Tourists)} + \text{Pelancong (Excursionists)}$$

### 13.2.2 Tingkat Penghunian Kamar TPK Hotel

- **Seksi**: 13.2 Statistik Pariwisata dan Perhotelan
- **Prioritas**: Tinggi
- **Rujukan**: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 36-41]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai formulasi TPK BPS, penghitungan malam kamar tersedia (kamar x hari), formula TPTT, RTK, dan RTH, serta pemahaman instrumen survei VHTS vs VHTL.

**Intuisi** — Tingkat Penghunian Kamar (TPK) atau Room Occupancy Rate adalah barometer paling sensitif dari denyut ekonomi pariwisata. Jika kamar hotel banyak yang kosong, bukan hanya pemilik hotel yang merugi, tetapi pedagang oleh-oleh, sopir taksi, pemandu wisata, dan restoran di sekitarnya juga sepi pembeli. TPK mengukur persentase kapasitas kamar yang berhasil diisi oleh tamu dibandingkan total kapasitas kamar yang siap dijual selama periode operasional tertentu.

**Definisi BPS** — Tingkat Penghunian Kamar (TPK) hotel menurut BPS adalah perbandingan antara banyaknya malam kamar yang terpakai (terjual) dengan banyaknya malam kamar yang tersedia untuk disewakan selama periode pelaporan, dinyatakan dalam persentase. Malam kamar yang tersedia dihitung dari jumlah fisik kamar yang layak jual dikalikan jumlah hari operasi hotel pada periode tersebut. Data dihimpun secara rutin melalui Kuesioner Survei Perusahaan Akomodasi Bulanan (VHTS) secara sensus untuk hotel berbintang dan secara sampel untuk hotel non-bintang.

**Syarat & batas** — 0% <= TPK <= 100%. TPK = 100% berarti seluruh kamar terisi penuh setiap malam sepanjang periode (full booked). Kamar yang sedang rusak berat atau dalam renovasi jangka panjang dikeluarkan dari penghitungan malam kamar yang tersedia.

**Rumus** — $$\text{TPK} = \frac{\text{Malam Kamar Terpakai}}{\text{Malam Kamar Tersedia}} \times 100\% = \frac{\sum_{t=1}^D K_{\text{terpakai}, t}}{\text{Jumlah Kamar} \times \text{Jumlah Hari Buka}} \times 100\%$$

### 13.2.3 Rata-rata Lama Menginap Tamu RLMT

- **Seksi**: 13.2 Statistik Pariwisata dan Perhotelan
- **Prioritas**: Sedang
- **Rujukan**: [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide/hal. 40-43]
- **Cakupan**: COVERED

**Fokus ujian** — Menguasai definisi operasional dan formula RLMT BPS, perbedaan rata-rata tertimbang vs rata-rata sederhana pada RLMT gabungan, serta karakteristik durasi wisman vs wisnus.

**Intuisi** — Dua hotel sama-sama kedatangan 500 tamu dalam sebulan. Di hotel A, tamu-tamu tersebut adalah pelaku perjalanan dinas yang hanya menginap satu malam lalu pulang (total 500 malam tamu). Di hotel B, tamu-tamu tersebut adalah wisatawan liburan keluarga yang menginap rata-rata 4 malam (total 2.000 malam tamu). Meskipun jumlah tamunya sama persis, hotel B menghasilkan perputaran uang empat kali lipat lebih besar. Indikator Rata-rata Lama Menginap Tamu (RLMT) atau Average Length of Stay (ALOS) mengukur durasi rata-rata seorang tamu menghabiskan waktu di akomodasi.

**Definisi BPS** — Rata-rata Lama Menginap Tamu (RLMT / Average Length of Stay) menurut metodologi BPS adalah rata-rata lamanya seorang tamu menginap pada suatu fasilitas akomodasi perhotelan, dihitung dengan membagi total banyaknya malam tamu yang menginap dengan total banyaknya tamu yang datang dan menginap pada periode tersebut. Satuan RLMT dinyatakan dalam hari atau malam. BPS menyajikan RLMT secara disagregasi menurut klasifikasi hotel (bintang vs non-bintang) serta asal kebangsaan tamu (wisatawan mancanegara / asing vs wisatawan nusantara / domestik).

**Syarat & batas** — RLMT >= 1,00 malam (karena tamu yang tercatat di akomodasi komersial menginap minimal 1 malam). RLMT wisman umumnya lebih tinggi (berkisar 2,5 - 4,0 malam) dibandingkan RLMT wisnus (berkisar 1,5 - 2,0 malam) karena wisman menempuh perjalanan jarak jauh antarnegara.

**Rumus** — $$\text{RLMT} = \frac{\text{Total Malam Tamu Menginap}}{\text{Total Tamu yang Datang \& Menginap}} = \frac{\sum_{i=1}^N L_i}{N}, \quad \text{RLMT}_{\text{gabungan}} = \frac{M_{\text{asing}} + M_{\text{domestik}}}{T_{\text{asing}} + T_{\text{domestik}}}$$

## Contoh Hitung

### 13.1.1 — Valuasi Ekspor Impor FOB vs CIF

Pada bulan September 2026, sebuah perusahaan manufaktur di Surabaya mengekspor produk tekstil dengan nilai faktur FOB sebesar USD 120.000. Pada saat bersamaan, importir di Jakarta mengimpor bahan baku kapas dengan nilai faktur CIF sebesar USD 100.000 (terdiri dari harga barang FOB USD 90.000, biaya pengangkutan/freight USD 8.000, dan asuransi internasional USD 2.000). Rata-rata kurs beli dolar AS tertimbang transaksi pada bulan tersebut adalah Rp 15.500/USD, sedangkan rata-rata kurs jual dolar AS tertimbang adalah Rp 15.600/USD. Hitunglah:
1. Nilai ekspor FOB dalam mata uang Rupiah.
2. Nilai impor CIF dalam mata uang Rupiah (standar publikasi IMTS BPS).
3. Saldo Neraca Perdagangan Barang IMTS dalam USD dan dalam Rupiah.
4. Nilai impor barang yang dicatat dalam sistem Neraca Pembayaran / SNA 2008 (valuasi FOB) dan saldo neraca barang FOB-FOB dalam USD.

| Parameter Transaksi | Valuasi Valas (USD) | Kurs Tertimbang BPS (Rp/USD) | Nilai Konversi (Rp) |
|---|---|---|---|
| Ekspor Tekstil (FOB) | 120.000 | 15.500 (Kurs Beli) | 1.860.000.000 |
| Impor Bahan Baku (CIF) | 100.000 | 15.600 (Kurs Jual) | 1.560.000.000 |
| - Komponen Barang Murni (FOB) | 90.000 | 15.600 | 1.404.000.000 |
| - Komponen Angkut (Freight) | 8.000 | 15.600 | 124.800.000 |
| - Komponen Asuransi (Insurance) | 2.000 | 15.600 | 31.200.000 |

**Penyelesaian**

1. Menghitung Nilai Ekspor FOB dalam Rupiah:
   $$X_{\text{IDR}} = X_{\text{USD}} \times \bar{K}_{\text{beli}} = 120.000 \times 15.500 = \text{Rp } 1.860.000.000$$
2. Menghitung Nilai Impor CIF dalam Rupiah:
   $$M_{\text{IDR}} = M_{\text{USD}} \times \bar{K}_{\text{jual}} = 100.000 \times 15.600 = \text{Rp } 1.560.000.000$$
3. Menghitung Saldo Neraca Perdagangan Barang IMTS BPS (Ekspor FOB - Impor CIF):
   - Dalam USD: $$\text{Surplus}_{\text{USD}} = 120.000 - 100.000 = +\text{USD } 20.000$$
   - Dalam Rupiah: $$\text{Surplus}_{\text{IDR}} = 1.860.000.000 - 1.560.000.000 = +\text{Rp } 300.000.000$$
4. Penyesuaian ke Konsep Neraca Pembayaran / SNA 2008 (Valuasi FOB-FOB):
   - Impor barang dinilai secara FOB: $$M_{\text{FOB}} = \text{USD } 90.000$$
   - Biaya Freight (USD 8.000) dan Insurance (USD 2.000) dikeluarkan dari kelompok impor barang dan dimasukkan ke neraca jasa perdagangan luar negeri (jika penyedia jasa non-residen).
   - Saldo Neraca Barang (FOB - FOB): $$120.000 - 90.000 = +\text{USD } 30.000$$.

**Hasil verifikasi** — `Ekspor_FOB_IDR=1860000000, Impor_CIF_IDR=1560000000, Surplus_IMTS_USD=20000, Surplus_SNA_USD=30000`

### 13.1.2 — Barang Dagangan Tanpa Masuk Pabean Merchanting

Sebuah perusahaan dagang berstatus residen di Indonesia melakukan serangkaian transaksi merchanting internasional pada bulan September 2026:
1. Membeli komoditas biji kopi robusta dari eksportir di Vietnam seharga USD 200.000. Barang disimpan sementara di gudang berikat Singapura tanpa memasuki wilayah pabean Indonesia.
2. Menjual seluruh biji kopi tersebut kepada importir di Hamburg, Jerman, seharga USD 260.000 tanpa dilakukan pengolahan fisik (hanya pemindahan kepemilikan dokumen bill of lading).
3. Selain transaksi merchanting, selama bulan tersebut Indonesia mencatat ekspor barang reguler fisik (FOB) sebesar USD 1.500.000 dan impor barang reguler fisik (FOB) sebesar USD 1.080.000.
Hitunglah:
1. Nilai pencatatan perolehan barang di bawah merchanting oleh Indonesia (ekspor negatif).
2. Nilai pencatatan penjualan barang di bawah merchanting oleh Indonesia (ekspor positif/bruto).
3. Nilai ekspor neto barang di bawah merchanting (*net exports of goods under merchanting*).
4. Total ekspor barang Indonesia menurut konsep SNA 2008 dan saldo neraca perdagangan barang FOB-FOB.

| Komponen Transaksi | Nilai Transaksi (USD) | Klasifikasi Statistik SNA 2008 |
|---|---|---|
| Pembelian dari Vietnam | 200.000 | Ekspor negatif barang di bawah merchanting (-200.000) |
| Penjualan ke Jerman | 260.000 | Ekspor positif barang di bawah merchanting (+260.000) |
| Selisih Margin Dagang | 60.000 | Ekspor neto barang di bawah merchanting (+60.000) |
| Ekspor Barang Reguler (FOB) | 1.500.000 | Ekspor barang umum (*general merchandise*) |
| Impor Barang Reguler (FOB) | 1.080.000 | Impor barang umum (*general merchandise*) |

**Penyelesaian**

1. Pencatatan Perolehan Barang di Bawah Merchanting:
   $$X_{\text{negatif}} = -\text{USD } 200.000$$
   Catatan: SNA 2008 mencatat pembelian ini sebagai 'ekspor negatif' pada pos barang agar tidak dicatat sebagai impor negara pedagang (karena barang tidak dikonsumsi di dalam negeri).
2. Pencatatan Penjualan Barang di Bawah Merchanting:
   $$X_{\text{positif}} = +\text{USD } 260.000$$
3. Menghitung Ekspor Neto Barang di Bawah Merchanting:
   $$\text{Ekspor Neto} = X_{\text{positif}} + X_{\text{negatif}} = 260.000 - 200.000 = +\text{USD } 60.000$$
4. Menghitung Total Ekspor Barang SNA 2008 dan Saldo Neraca Barang:
   - Total Ekspor Barang = Ekspor Reguler FOB + Ekspor Neto Merchanting = $$1.500.000 + 60.000 = \text{USD } 1.560.000$$
   - Saldo Neraca Perdagangan Barang (FOB - FOB) = $$1.560.000 - 1.080.000 = +\text{USD } 480.000$$.

**Hasil verifikasi** — `Acq=-200000, Sales=260000, NetMerchanting=60000, TotalX_SNA=1560000, GoodsBalance_SNA=480000`

### 13.1.3 — Net Barter Terms of Trade NBToT

Berdasarkan data perdagangan komoditas karet Indonesia (rekonstruksi soal UAS OSL 2022/2023 PG 24, 25, 26 dan indikator daya saing BPS):
1. Pada tahun 2022, nilai ekspor karet Indonesia adalah USD 350 juta dan nilai impor produk olahan karet adalah USD 164 juta. Hitung nilai Indeks Spesialisasi Perdagangan (ISP) karet dan tentukan tahap perkembangannya menurut teori siklus produk.
2. Jika komoditas lain memiliki ISP sebesar -0,36, tentukan berada pada tahapan manakah komoditas tersebut dalam siklus produk.
3. Indeks harga ekspor komoditas (Px) tercatat sebesar 105 dan indeks harga impor (Pm) sebesar 100 (tahun dasar = 100). Hitung Net Barter Terms of Trade (NBToT) dan interpretasikan maknanya.
4. Total ekspor karet Indonesia adalah USD 350 juta dari total seluruh ekspor Indonesia USD 2.500 juta. Di pasar dunia, total ekspor karet dunia adalah USD 2.000 juta dari total ekspor dunia USD 40.000 juta. Hitung indeks Balassa RCA komoditas karet Indonesia.

| Indikator | Nilai Komoditas Karet | Nilai Total Agregat | Formula BPS | Hasil Perhitungan |
|---|---|---|---|---|
| Ekspor (X) | USD 350 juta | USD 2.500 juta (Total X RI) | - | - |
| Impor (M) | USD 164 juta | - | - | - |
| ISP Karet | - | - | (X - M) / (X + M) | 0,36 (Perluasan Ekspor) |
| Kasus Komoditas Q25 | - | - | ISP = -0,36 | Substitusi Impor |
| Indeks Harga Px / Pm | Px = 105 | Pm = 100 | (Px / Pm) * 100 | 105,0 (Favourable) |
| Ekspor Karet Dunia | USD 2.000 juta | USD 40.000 juta (Total X Dunia) | (X_ij/X_j) / (X_iw/X_w) | RCA = 2,80 (Kuat) |

**Penyelesaian**

1. Menghitung ISP Karet (UAS 2022/2023 PG 24):
   $$\text{ISP} = \frac{X - M}{X + M} = \frac{350 - 164}{350 + 164} = \frac{186}{514} \approx 0,3619$$
   Dibulatkan 2 desimal: $$\text{ISP} = 0,36$$.
   Karena $0,0 < 0,36 \le 0,8$, komoditas karet berada pada **Tahap Perluasan Ekspor** (*Export Expansion Stage*).
2. Menentukan Tahap Siklus Produk untuk ISP = -0,36 (UAS 2022/2023 PG 25):
   Rentang tahapan siklus produk:
   - $[-1,0 \text{ s.d. } -0,5]$: Tahap Pengenalan (*Introduction*)
   - $(-0,5 \text{ s.d. } 0,0]$: Tahap Substitusi Impor (*Import Substitution*)
   - $(0,0 \text{ s.d. } 0,8]$: Tahap Perluasan Ekspor (*Export Expansion*)
   - $(0,8 \text{ s.d. } 1,0]$: Tahap Pematangan (*Maturation*)
   Karena ISP = -0,36 berada pada rentang $(-0,5, 0,0]$, maka komoditas berada pada **Tahap Substitusi Impor**.
3. Menghitung NBToT (UAS 2022/2023 PG 26):
   $$\text{NBToT} = \frac{P_x}{P_m} \times 100 = \frac{105}{100} \times 100 = 105,0$$
   Makna: Nilai tukar perdagangan mengalami perbaikan 5% dibanding tahun dasar (daya beli riil ekspor meningkat).
4. Menghitung Indeks RCA Balassa:
   $$\text{Pangsa Domestik} = \frac{X_{ij}}{X_j} = \frac{350}{2.500} = 0,1400$$
   $$\text{Pangsa Dunia} = \frac{X_{iw}}{X_w} = \frac{2.000}{40.000} = 0,0500$$
   $$\text{RCA} = \frac{0,1400}{0,0500} = 2,80$$
   Karena $\text{RCA} = 2,80 > 1$, Indonesia memiliki keunggulan komparatif yang sangat kuat pada komoditas karet.

**Hasil verifikasi** — `ISP_Rubber=0.3619, Stage_Rubber=Perluasan Ekspor, Stage_Q25=Substitusi Impor, NBToT=105.0, RCA=2.80`

### 13.1.4 — Gross Barter dan Income ToT

Pada suatu perekonomian berkembang, diketahui dinamika perdagangan internasional antara tahun dasar (t=0) dan tahun berjalan (t=1) sebagai berikut:
- Indeks harga ekspor (Px) turun menjadi 95,0 (terdepresiasi 5%).
- Indeks harga impor (Pm) naik menjadi 105,0 (terinflasi 5%).
- Untuk mengimbangi penurunan harga, negara tersebut meningkatkan volume ekspor secara agresif sehingga indeks volume ekspor (Qx) mencapai 125,0.
- Indeks volume impor fisik yang berhasil didatangkan (Qm) tercatat sebesar 110,0.
Hitunglah:
1. Net Barter Terms of Trade (NBToT) pada tahun t=1.
2. [SUPLEMEN] Gross Barter Terms of Trade (GBToT) pada tahun t=1.
3. Income Terms of Trade / Kapasitas Impor (KM) pada tahun t=1.
4. Jelaskan paradoks ekonomi mengapa Kapasitas Impor dapat meningkat di saat Net Barter ToT mengalami penurunan.

| Indikator | Tahun Dasar (t=0) | Tahun Berjalan (t=1) | Formula Perhitungan | Hasil t=1 |
|---|---|---|---|---|
| Indeks Harga Ekspor (Px) | 100,0 | 95,0 | - | - |
| Indeks Harga Impor (Pm) | 100,0 | 105,0 | - | - |
| Indeks Volume Ekspor (Qx) | 100,0 | 125,0 | - | - |
| Indeks Volume Impor (Qm) | 100,0 | 110,0 | - | - |
| Net Barter ToT (NBToT) | 100,0 | - | (Px / Pm) * 100 | 90,48 |
| Gross Barter ToT [SUPLEMEN] | 100,0 | - | (Qm / Qx) * 100 | 88,00 |
| Income ToT / Kapasitas Impor (KM) | 100,0 | - | (NBToT * Qx) / 100 | 113,10 |

**Penyelesaian**

1. Menghitung Net Barter Terms of Trade (NBToT):
   $$\text{NBToT} = \frac{P_x}{P_m} \times 100 = \frac{95,0}{105,0} \times 100 = 90,4762 \approx 90,48$$
   Artinya: Daya beli per unit komoditas ekspor turun sebesar 9,52% terhadap barang impor.
2. Menghitung [SUPLEMEN] Gross Barter Terms of Trade (GBToT):
   $$\text{GBToT} = \frac{Q_m}{Q_x} \times 100 = \frac{110,0}{125,0} \times 100 = 88,00$$
   Artinya: Volume impor fisik yang diperoleh per unit volume ekspor fisik berkurang menjadi 88% dari tahun dasar.
3. Menghitung Income Terms of Trade / Kapasitas Impor (KM):
   $$\text{Income ToT} = \frac{\text{NBToT} \times Q_x}{100} = \frac{90,4762 \times 125,0}{100} = 113,0952 \approx 113,10$$
   Atau melalui pendekatan Nilai Ekspor ADHB:
   $$X_{\text{ADHB}} = \frac{P_x \times Q_x}{100} = \frac{95,0 \times 125,0}{100} = 118,75$$
   $$\text{KM} = \frac{X_{\text{ADHB}}}{P_m} \times 100 = \frac{118,75}{105,0} \times 100 = 113,10$$
4. Penjelasan Paradoks Ekonomi:
   Meskipun nilai tukar harga per unit (NBToT = 90,48) memburuk akibat jatuhnya harga komoditas ekspor, total daya beli ekspor untuk mengimpor barang (Income ToT = 113,10) justru melonjak naik sebesar 13,10%. Hal ini disebabkan efek ekspansi volume ekspor (+25%) jauh lebih kuat daripada efek kontraksi harga (-9,52%).

**Hasil verifikasi** — `NBToT=90.48, GBToT=88.00, IncomeToT=113.10, KM=113.10`

### 13.2.1 — Definisi Wisman dan Wisnus

Selama bulan Juli 2026, Tempat Pemeriksaan Imigrasi (TPI) dan pelabuhan laut internasional di Batam mencatat 10.000 kedatangan orang asing dari luar negeri dengan profil sebagai berikut:
1. 6.500 orang wisatawan yang menginap di berbagai hotel/resor selama rata-rata 3 malam untuk berlibur dan bermain golf.
2. 1.200 orang penumpang kapal pesiar internasional (*cruise passengers*) yang tiba di pagi hari, berbelanja dan berkuliner selama 8 jam di Batam, lalu kembali tidur di atas kapal pesiar di perairan internasional.
3. 300 orang diplomat dan pejabat konsuler asing beserta keluarganya yang tiba untuk bertugas di pos diplomatik.
4. 1.500 orang tenaga kerja asing (TKA) yang memegang visa kerja 2 tahun dan menerima gaji langsung dari entitas manufaktur lokal di Batam.
5. 500 orang warga negara asing yang telah tinggal dan menyewa rumah di Batam selama 18 bulan (sudah berstatus penduduk Indonesia) yang baru pulang dari kunjungan singkat 2 hari di Singapura.
Hitunglah:
1. Jumlah kedatangan yang sah diklasifikasikan sebagai Wisatawan Mancanegara (*tourists*).
2. Jumlah kedatangan yang diklasifikasikan sebagai Pelancong Mancanegara (*excursionists*).
3. Total Pengunjung Mancanegara yang sah (*inbound visitors*).
4. Jumlah kedatangan yang tidak dihitung sebagai pengunjung mancanegara (*non-visitors*) beserta alasannya.
5. Persentase wisatawan terhadap total pengunjung mancanegara yang sah.

| Kelompok Kedatangan | Jumlah (Orang) | Durasi / Karakteristik | Klasifikasi Statistik BPS/UNWTO |
|---|---|---|---|
| Tamu Resor / Hotel | 6.500 | Menginap 3 malam, tujuan rekreasi | Wisatawan Mancanegara (Tourist) |
| Penumpang Cruise | 1.200 | Kunjungan 8 jam, tidur di kapal | Pelancong Mancanegara (Excursionist) |
| Korps Diplomatik | 300 | Pejabat kedutaan/konsuler | Bukan Pengunjung (Immunity/Exempt) |
| Tenaga Kerja Kontrak | 1.500 | Kontrak 2 tahun, digaji residen | Bukan Wisatawan (Pekerja Remunerasi) |
| WNA Residen Batam | 500 | Tinggal > 12 bulan di Batam | Bukan Wisman (Penduduk Pulang) |

**Penyelesaian**

1. Mengidentifikasi Wisatawan Mancanegara (*tourists*):
   Kriteria UNWTO: durasi $\ge 24$ jam, $< 12$ bulan, tujuan rekreasi/pribadi/bisnis, tidak digaji lokal.
   $$\text{Tourists} = 6.500$$
2. Mengidentifikasi Pelancong Mancanegara (*excursionists*):
   Kriteria UNWTO: durasi $< 24$ jam, tidak menginap di akomodasi setempat (penumpang kapal pesiar).
   $$\text{Excursionists} = 1.200$$
3. Menghitung Total Pengunjung Mancanegara (*inbound visitors*):
   $$\text{Total Visitors} = \text{Tourists} + \text{Excursionists} = 6.500 + 1.200 = 7.700$$
4. Menghitung Kedatangan yang Dikecualikan (*non-visitors*):
   - Diplomat asing: 300 orang (ekstrateritorial).
   - Tenaga kerja asing digaji lokal: 1.500 orang (mencari nafkah dari penduduk).
   - WNA tinggal $> 12$ bulan: 500 orang (sudah berstatus penduduk Indonesia).
   $$\text{Non-Visitors} = 300 + 1.500 + 500 = 2.300$$
   Total verifikasi: $$7.700 + 2.300 = 10.000$$ (cocok).
5. Menghitung Persentase Wisatawan terhadap Total Pengunjung Sah:
   $$\% \text{Tourists} = \frac{6.500}{7.700} \times 100\% \approx 84,4156\% \rightarrow 84,42\%$$.

**Hasil verifikasi** — `Tourists=6500, Excursionists=1200, TotalVisitors=7700, NonVisitors=2300, PctTourists=84.42`

### 13.2.2 — Tingkat Penghunian Kamar TPK Hotel

Sebuah hotel berbintang di kawasan wisata memiliki kapasitas 100 kamar yang dapat disewakan dan 160 tempat tidur. Selama bulan September 2026 (periode 30 hari kalender), hotel beroperasi penuh setiap hari. Catatan operasional resepsionis menunjukkan bahwa selama bulan tersebut:
- Jumlah malam kamar yang berhasil terjual dan dihuni tamu adalah 1.800 malam kamar.
- Total tamu yang datang dan menginap adalah 1.200 orang.
- Total lama menginap seluruh tamu secara kumulatif adalah 2.700 malam tamu.
Hitunglah:
1. Jumlah malam kamar yang tersedia selama bulan September.
2. Tingkat Penghunian Kamar (TPK) hotel.
3. Tingkat Pemakaian Tempat Tidur (TPTT) hotel.
4. Rata-rata Tamu per Kamar terjual (RTK) dan Rata-rata Tamu per Hari operasi (RTH).

| Parameter Operasional | Nilai Riil | Formula BPS | Hasil Perhitungan |
|---|---|---|---|
| Kapasitas Fisik Kamar | 100 kamar | - | - |
| Jumlah Hari Operasi | 30 hari | - | - |
| Malam Kamar Tersedia | - | Kamar * Hari | 3.000 malam kamar |
| Malam Kamar Terjual | 1.800 malam kamar | - | - |
| TPK Hotel | - | (Terpakai / Tersedia) * 100% | 60,00% |
| Malam Tempat Tidur Tersedia | - | 160 tempat tidur * 30 hari | 4.800 malam bed |
| Total Malam Tamu | 2.700 malam tamu | - | - |
| TPTT Hotel | - | (Malam Tamu / Bed Tersedia) * 100% | 56,25% |
| Rata-rata Tamu per Kamar (RTK) | - | Malam Tamu / Kamar Terjual | 1,50 orang/kamar |
| Rata-rata Tamu per Hari (RTH) | - | Total Tamu / Hari Buka | 40,0 tamu/hari |

**Penyelesaian**

1. Menghitung Malam Kamar Tersedia:
   $$\text{Malam Kamar Tersedia} = \text{Jumlah Kamar} \times \text{Hari Buka} = 100 \times 30 = 3.000 \text{ malam kamar}$$
2. Menghitung Tingkat Penghunian Kamar (TPK):
   $$\text{TPK} = \frac{\text{Malam Kamar Terpakai}}{\text{Malam Kamar Tersedia}} \times 100\% = \frac{1.800}{3.000} \times 100\% = 60,00\%$$
3. Menghitung Tingkat Pemakaian Tempat Tidur (TPTT):
   - Malam tempat tidur tersedia = $$160 \times 30 = 4.800 \text{ malam tempat tidur}$$.
   $$\text{TPTT} = \frac{\text{Banyaknya Malam Tamu}}{\text{Tempat Tidur Tersedia}} \times 100\% = \frac{2.700}{4.800} \times 100\% = 56,25\%$$
4. Menghitung Indikator Turunan:
   - Rata-rata Tamu per Kamar (RTK): $$\text{RTK} = \frac{2.700}{1.800} = 1,50 \text{ orang per kamar}$$.
   - Rata-rata Tamu per Hari (RTH): $$\text{RTH} = \frac{1.200}{30} = 40,0 \text{ tamu per hari}$$.

**Hasil verifikasi** — `AvailableRoomNights=3000, TPK=60.00%, TPTT=56.25%, RTK=1.50, RTH=40.0`

### 13.2.3 — Rata-rata Lama Menginap Tamu RLMT

Sebuah hotel resor bintang 5 di kawasan pariwisata mencatat aktivitas tamu selama bulan September 2026 sebagai berikut (rekonstruksi soal ujian dan data resmi perhotelan BPS):
- Tamu Mancanegara (Wisman/Asing): 300 orang tamu datang, dengan akumulasi lama menginap mencapai 900 malam tamu.
- Tamu Nusantara (Wisnus/Domestik): 200 orang tamu datang, dengan akumulasi lama menginap mencapai 350 malam tamu.
Hitunglah:
1. Rata-rata Lama Menginap Tamu Asing (RLMT Wisman).
2. Rata-rata Lama Menginap Tamu Domestik (RLMT Wisnus).
3. Total tamu yang datang dan total malam tamu kumulatif hotel tersebut.
4. Rata-rata Lama Menginap Tamu gabungan (RLMT Total) hotel tersebut.
5. Persentase jumlah tamu asing dan tamu domestik terhadap total tamu.

| Asal Tamu | Tamu Datang (Orang) | Total Malam Tamu (Malam) | Formula BPS | RLMT (Malam) | Pangsa Tamu (%) |
|---|---|---|---|---|---|
| Tamu Asing (Wisman) | 300 | 900 | Malam Tamu / Tamu Datang | 3,00 | 60,00% |
| Tamu Domestik (Wisnus) | 200 | 350 | Malam Tamu / Tamu Datang | 1,75 | 40,00% |
| **Total Gabungan** | **500** | **1.250** | **Total Malam / Total Tamu** | **2,50** | **100,00%** |

**Penyelesaian**

1. Menghitung RLMT Tamu Asing:
   $$\text{RLMT}_{\text{asing}} = \frac{900}{300} = 3,00 \text{ malam}$$
2. Menghitung RLMT Tamu Domestik:
   $$\text{RLMT}_{\text{domestik}} = \frac{350}{200} = 1,75 \text{ malam}$$
3. Menghitung Agregat Total:
   - Total Tamu Datang = $$300 + 200 = 500 \text{ orang}$$
   - Total Malam Tamu = $$900 + 350 = 1.250 \text{ malam tamu}$$
4. Menghitung RLMT Gabungan (Total):
   $$\text{RLMT}_{\text{total}} = \frac{\text{Total Malam Tamu}}{\text{Total Tamu Datang}} = \frac{1.250}{500} = 2,50 \text{ malam}$$
5. Menghitung Persentase Tamu:
   - Asing: $$(300 / 500) \times 100\% = 60,00\%$$
   - Domestik: $$(200 / 500) \times 100\% = 40,00\%$$.

**Hasil verifikasi** — `RLMT_Foreign=3.00, RLMT_Domestic=1.75, TotalGuests=500, TotalNights=1250, RLMT_Total=2.50, PctForeign=60.0%`

## Jebakan Ujian

**13.1.1 — Tertukar antara penggunaan Kurs Beli dan Kurs Jual dalam konversi valuta ekspor-impor**

- Jebakan: Menggunakan kurs jual untuk ekspor atau kurs tengah BI tanpa penimbang transaksi.
- Strategi aman: Ingat aturan perbankan/BPS: Eksportir menerima valuta asing dan menjualnya ke bank sehingga bank menggunakan kurs 'beli' (bank membeli USD eksportir). Importir membutuhkan valuta asing dan membelinya dari bank sehingga bank menggunakan kurs 'jual' (bank menjual USD ke importir).

**13.1.1 — Perbedaan valuasi impor antara IMTS BPS dan SNA 2008 / Neraca Pembayaran BI**

- Jebakan: Mengira bahwa impor pada Neraca Pembayaran Bank Indonesia dinilai atas dasar CIF sama seperti publikasi bulanan BPS.
- Strategi aman: Publikasi IMTS BPS mencatat impor secara CIF, namun pada Neraca Pembayaran (BOP) dan Tabel Input-Output / SNA 2008, impor barang disesuaikan menjadi FOB, dan komponen ongkos angkut (freight) serta asuransi dialihkan ke neraca jasa.

**13.1.2 — Mengklasifikasikan margin keuntungan merchanting ke dalam neraca jasa perdagangan**

- Jebakan: Menganggap selisih jual-beli merchanting sebagai pendapatan jasa perantara (komisi jasa) seperti pada sistem lama BPM5.
- Strategi aman: Di bawah SNA 2008 dan BPM6, transaksi merchanting secara tegas dikelompokkan ke dalam Neraca Barang (Goods), bukan Neraca Jasa (Services), dengan nama akun 'Net exports of goods under merchanting'.

**13.1.2 — Mencatat pembelian barang luar negeri pada merchanting sebagai impor barang biasa**

- Jebakan: Mencatat pembelian USD 200.000 sebagai impor Indonesia sehingga mendistorsi statistik impor domestik.
- Strategi aman: Ingat bahwa barang merchanting tidak pernah memasuki wilayah pabean Indonesia. Pembelian dicatat sebagai 'ekspor barang bernilai negatif' di neraca barang, bukan sebagai impor.

**13.1.3 — Salah mengidentifikasi batas interval 4 tahapan siklus produk ISP**

- Jebakan: Mengira tahap substitusi impor berawal dari 0 atau tahap pematangan mulai dari 0,5.
- Strategi aman: Hafalkan pembagian standar BPS: Pengenalan [-1 s.d. -0.5], Substitusi Impor (-0.5 s.d. 0], Perluasan Ekspor (0 s.d. 0.8], Pematangan (0.8 s.d. 1.0].

**13.1.3 — Tertukar antara pembilang dan penyebut pada rumus Balassa RCA**

- Jebakan: Membagi pangsa dunia dengan pangsa domestik, atau lupa bahwa pembandingnya adalah total ekspor masing-masing.
- Strategi aman: RCA = (Pangsa komoditas di ekspor negara) / (Pangsa komoditas di ekspor dunia). Jika pangsa negara lebih besar daripada rata-rata dunia, rasio > 1.

**13.1.3 — Mengasumsikan ToT > 100 selalu berarti surplus neraca perdagangan**

- Jebakan: Menyimpulkan neraca perdagangan pasti surplus jika NBToT = 105.
- Strategi aman: NBToT hanya mengukur rasio harga (indeks Px/Pm), bukan kuantitas volume barang (Q). Jika volume ekspor anjlok drastis sementara volume impor membengkak, negara bisa tetap mengalami defisit perdagangan meski harga ekspornya relatif tinggi.

**13.1.4 — Tertukar pembilang dan penyebut antara NBToT dan Gross Barter ToT**

- Jebakan: Menulis rumus GBToT sebagai Qx / Qm (mengikuti urutan ekspor di pembilang seperti NBToT).
- Strategi aman: Ingat bahwa Gross Barter ToT mengukur apa yang kita 'terima secara fisik' (impor Qm) dibagi apa yang kita 'serahkan secara fisik' (ekspor Qx). Jadi GBToT = (Qm / Qx) * 100.

**13.1.4 — Mengira penurunan NBToT selalu menurunkan kemampuan negara untuk membeli barang impor**

- Jebakan: Menyimpulkan bahwa negara pasti mengalami krisis devisa impor hanya karena angka NBToT < 100.
- Strategi aman: Gunakan Income Terms of Trade / Kapasitas Impor (KM) untuk menilai kemampuan impor total. Jika volume ekspor meningkat cukup besar, penerimaan devisa riil tetap dapat meningkat meski harga komoditas per unit turun.

**13.2.1 — Menganggap semua pemegang paspor asing otomatis dihitung sebagai Wisman**

- Jebakan: Memasukkan ekspatriat yang telah tinggal 2 tahun di Indonesia atau TKA yang digaji lokal ke dalam jumlah wisman.
- Strategi aman: Kunci UNWTO: WNA yang tinggal > 12 bulan berstatus 'penduduk Indonesia' (bukan wisman), dan orang yang datang untuk bekerja/memperoleh penghasilan dari residen lokal dikeluarkan dari hitungan.

**13.2.1 — Menyamakan istilah 'Wisatawan' (Tourist) dengan 'Pengunjung' (Visitor)**

- Jebakan: Menghitung penumpang kapal pesiar satu hari (excursionist) sebagai 'tourist'.
- Strategi aman: Pengunjung (Visitor) adalah kategori payung besar. Jika menginap >= 24 jam disebut Wisatawan (Tourist); jika kurang dari 24 jam disebut Pelancong (Excursionist).

**13.2.2 — Salah menghitung penyebut malam kamar tersedia (lupa mengalikan dengan jumlah hari buka)**

- Jebakan: Hanya membagi malam kamar terjual dengan jumlah fisik kamar (1.800 / 100 = 1800%).
- Strategi aman: Penyebut TPK adalah 'malam kamar' (room-nights), yaitu kapasitas fisik kamar dikalikan jumlah hari dalam periode observasi (misal 100 kamar * 30 hari = 3.000 malam kamar).

**13.2.2 — Tertukar antara TPK (kamar) dan TPTT (tempat tidur)**

- Jebakan: Menggunakan data jumlah tamu pada pembilang TPK alih-alih jumlah kamar yang terpakai.
- Strategi aman: Satu kamar bisa dihuni oleh 2 orang atau lebih. TPK mengukur okupansi fisik kamar (kamar terpakai / kamar tersedia), sedangkan TPTT mengukur okupansi ranjang (malam tamu / ranjang tersedia).

**13.2.3 — Menghitung RLMT gabungan dengan merata-ratakan langsung RLMT asing dan RLMT domestik**

- Jebakan: Menghitung RLMT gabungan sebagai (3,00 + 1,75) / 2 = 2,375 malam.
- Strategi aman: RLMT adalah rata-rata tertimbang (weighted average). Hitung selalu dari total seluruh malam tamu dibagi total seluruh tamu datang: 1.250 / 500 = 2,50 malam.

**13.2.3 — Tertukar antara Malam Kamar dan Malam Tamu**

- Jebakan: Menggunakan data malam kamar terjual pada pembilang RLMT.
- Strategi aman: Pembilang RLMT adalah 'Malam Tamu' (person-nights), yaitu akumulasi malam dari setiap individu tamu yang menginap, bukan jumlah fisik kamar.

## Navigasi

- [[05-perdagangan-dan-indikator-harga|← Pertemuan 12: Perdagangan dan Indikator Harga]]
- → (bab terakhir)
- [[_formulas|Rumus lengkap OSL]]
- [[_glossary|Glosarium istilah]]

---

[[_MOC|← Back to MOC]]
