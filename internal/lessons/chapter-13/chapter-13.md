---
textbook: Official Statistics Lanjutan (OSL)
chapter: 13
chapter_title: "Pertemuan 13: Ekspor-Impor, Terms of Trade, dan Pariwisata"
sections: ["13.1 Statistik Perdagangan Internasional", "13.2 Statistik Pariwisata dan Perhotelan"]
points: 7
generated: 2026-09-29
---

# Pertemuan 13: Ekspor-Impor, Terms of Trade, dan Pariwisata

> 《Official Statistics Lanjutan (OSL)》 ｜ 2 Bagian ｜ 7 Poin Konsep ｜ Dibuat: 2026-09-29

## 13.1 Statistik Perdagangan Internasional `[Pembahasan Mendalam]`

### 13.1.1 Valuasi Ekspor Impor FOB vs CIF ⭐

> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 4-9]

> [!info]
> Menguasai prinsip alih kepemilikan ekonomi SNA 2008, perbedaan titik valuasi FOB dan CIF, peran dokumen PEB/PIB Bea Cukai, serta mekanisme konversi kurs beli vs kurs jual BPS.

> [!quote]
> **Teks Materi Kuliah**
> Ekspor-impor didefinisikan sebagai transaksi alih kepemilikan ekonomi atas barang dan jasa antara residen suatu perekonomian dengan non-residen, termasuk re-ekspor dan merchanting. Ekspor dan impor barang dinilai menurut harga Free on Board (FOB). Pada International Merchandise Trade Statistics (IMTS), impor barang dicatat dalam nilai cost, insurance, and freight (CIF) sehingga biaya angkut barang dan asuransi harus dikeluarkan jika disesuaikan ke FOB. Data dikumpulkan dari PEB dan PIB Ditjen Bea Cukai. Ekspor dikonversi dengan kurs beli tertimbang, sedangkan impor dengan kurs jual tertimbang [slide 5-7].

**Intuisi Konsep**　Bayangkan Anda memesan barang dari pabrik di luar negeri:
- **FOB (Free on Board)**: Harga barang hanya sampai di atas dek kapal pelabuhan asal. Setelah tali kapal dilepas, semua risiko gelombang, badai, biaya bahan bakar kapal laut, dan asuransi perjalanan menjadi urusan Anda.
- **CIF (Cost, Insurance, and Freight)**: Penjual mengurus segalanya sampai kapal bersandar di pelabuhan negara Anda. Harga yang Anda bayar sudah 'paket komplit' meliputi harga barang, premi asuransi, dan tarif kapal kargo.
- Oleh karena itu, neraca perdagangan resmi BPS mencatat ekspor barang kita dengan FOB (karena pembeli asing menanggung ongkos kirim internasionalnya), sedangkan impor kita dicatat dengan CIF (karena devisa kita keluar untuk membayar barang sekaligus jasa angkut dan asuransinya).

**Definisi & Penjelasan Rigor**　### 1. Landasan Konseptual Ekspor-Impor (SNA 2008)

Berdasarkan kerangka kerja *System of National Accounts* (SNA 2008) dan *BPM6* [slide 5]:
- **Ekspor dan Impor**: Transaksi alih kepemilikan ekonomi (*change of economic ownership*) atas barang dan jasa antara penduduk (*resident*) suatu wilayah ekonomi dengan bukan penduduk (*non-resident*).
- Mencakup barang dagangan reguler, barang kiriman pos/kurir, re-ekspor, barang *merchanting*, serta pembelian langsung (*direct purchase*) oleh penduduk Indonesia di luar negeri maupun warga asing di Indonesia [slide 5].

### 2. Skema Valuasi Internasional: FOB vs CIF

Dalam statistik perdagangan luar negeri, terdapat dua titik penilaian harga utama [slide 6]:

1. **Free on Board (FOB)**:
   - Titik penilaian: Di atas kapal pengangkut di pelabuhan muat negara pengekspor.
   - Eksportir menanggung biaya produksi, pengangkutan dari gudang ke pelabuhan domestik, biaya muat (*loading* / *stevedoring*), dan bea keluar/pajak ekspor.
   - Importir menanggung biaya transportasi lintas samudra (*ocean/air freight*), premi asuransi perjalanan internasional, dan bea masuk di negara tujuan.
   - **Standar Ekspor BPS**: Seluruh barang ekspor Indonesia dinilai menurut harga FOB [slide 6].

2. **Cost, Insurance, and Freight (CIF)**:
   - Titik penilaian: Di pelabuhan bongkar negara pengimpor sebelum bea masuk dibayarkan.
   - Mencakup tiga komponen terpadu:
     $$\text{CIF} = \text{FOB} + \text{Freight} + \text{Insurance}$$
   - **Standar Impor IMTS BPS**: Impor barang dicatat dalam nilai CIF karena faktur perdagangan internasional yang diterima oleh Bea Cukai umumnya memuat total biaya sampai di pelabuhan Indonesia [slide 6].
   - **Penyesuaian SNA/BOP**: Untuk penyusunan PDB penggunaan dan Neraca Pembayaran oleh Bank Indonesia, impor CIF harus dikurangi komponen *freight* dan *insurance* agar menjadi impor barang FOB murni, sedangkan biaya angkut dan asuransi asing dipindahkan ke pos Neraca Jasa [slide 6].

### 3. Sumber Data dan Prosedur Konversi Valuta BPS

Alur pengumpulan dan konversi data statistik perdagangan [slide 7]:
1. **Dokumen Pabean Legal**:
   - Ekspor: Pemberitahuan Ekspor Barang (PEB).
   - Impor: Pemberitahuan Impor Barang (PIB).
   - Dikelola oleh Direktorat Jenderal Bea dan Cukai (DJBC), lalu diserahkan secara elektronik ke BPS dan BI.
2. **Konversi Mata Uang Asing ke Rupiah**:
   - Data faktur perdagangan mayoritas dinyatakan dalam Dolar Amerika Serikat (USD).
   - **Nilai Ekspor**: Dikonversi menggunakan **rata-rata kurs beli** dolar AS yang ditimbang dengan nilai nominal transaksi ekspor bulanan:
     $$X_{\text{IDR}} = X_{\text{USD}} \times \bar{K}_{\text{beli}}$$
   - **Nilai Impor**: Dikonversi menggunakan **rata-rata kurs jual** dolar AS yang ditimbang dengan nilai nominal transaksi impor bulanan:
     $$M_{\text{IDR}} = M_{\text{USD}} \times \bar{K}_{\text{jual}}$$
   - Dasar pertimbangan: Dari perspektif perbankan devisa, eksportir menukarkan USD hasil ekspor ke Rupiah (Bank membeli valas -> Kurs Beli), sedangkan importir membeli USD dari bank untuk membayar ke luar negeri (Bank menjual valas -> Kurs Jual).

### 4. Ringkasan Perbandingan Valuasi IMTS vs SNA 2008

| Dimensi | Publikasi IMTS BPS | Neraca Pembayaran (BI) / SNA 2008 |
|---|---|---|
| **Valuasi Ekspor Barang** | Free on Board (FOB) | Free on Board (FOB) |
| **Valuasi Impor Barang** | Cost, Insurance, Freight (CIF) | Free on Board (FOB) |
| **Pos Asuransi & Freight Impor** | Melekat di dalam Impor Barang | Dikeluarkan dari barang, dicatat di Neraca Jasa |
| **Sumber Data Barang** | BPS (dokumen PEB/PIB Bea Cukai) | BPS disesuaikan Bank Indonesia |
| **Sumber Data Jasa** | Bank Indonesia (ITRS & Survei) | Bank Indonesia |

**Contoh Soal 1 (Pilihan Ganda)**　Dalam statistik perdagangan luar negeri resmi BPS, mengapa data transaksi impor pada dokumen PIB yang dinyatakan dalam USD dikonversikan ke Rupiah menggunakan kurs 'jual' dolar AS?
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 6, 7]

- A. Karena nilai kurs jual selalu lebih rendah sehingga menekan angka defisit perdagangan.
- B. Karena dari sudut pandang bank devisa, importir harus membeli valas dari bank untuk membayar kewajiban ke luar negeri.
- C. Karena eksportir di luar negeri menjual barangnya dengan mata uang lokal.
- D. Karena peraturan menteri keuangan mengharuskan penggunaan kurs tengah Bank Indonesia.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan**:
> Sesuai metodologi BPS [slide 7], konversi valuta transaksi perdagangan luar negeri didasarkan pada posisi perbankan devisa. Importir membutuhkan mata uang asing (USD) untuk melunasi pembayaran barang ke mitra dagang non-residen. Oleh karena itu, importir mendatangi bank devisa untuk membeli USD, sehingga bank mengenakan kurs 'jual' (kurs di mana bank menjual valas kepada nasabah). Sebaliknya, untuk ekspor digunakan kurs 'beli' karena eksportir menjual valas penerimaan ekspor kepada bank.

**Contoh Soal 2 (Isian/Esai)**　Sebuah perusahaan di Medan mengekspor CPO dengan nilai FOB USD 120.000 (kurs beli Rp 15.500/USD). Pada saat yang sama, perusahaan lain mengimpor mesin dengan nilai CIF USD 100.000 yang terdiri dari komponen FOB USD 90.000, freight USD 8.000, dan asuransi USD 2.000 (kurs jual Rp 15.600/USD).
Hitunglah:
1. Nilai Ekspor FOB dalam Rupiah.
2. Nilai Impor CIF dalam Rupiah.
3. Saldo neraca perdagangan barang IMTS dalam USD.
4. Saldo neraca perdagangan barang menurut SNA 2008 (valuasi FOB-FOB) dalam USD.
Tuliskan format: `Ekspor_FOB_IDR=..., Impor_CIF_IDR=..., Surplus_IMTS_USD=..., Surplus_SNA_USD=...`.
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 6, 7, 9]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah Perhitungan:
> 1. **Ekspor FOB (IDR)**:
>    $$X_{\text{IDR}} = 120.000 \times 15.500 = \text{Rp } 1.860.000.000$$
> 2. **Impor CIF (IDR)**:
>    $$M_{\text{IDR}} = 100.000 \times 15.600 = \text{Rp } 1.560.000.000$$
> 3. **Surplus IMTS (USD)** (FOB - CIF):
>    $$\text{Surplus}_{\text{IMTS}} = 120.000 - 100.000 = +\text{USD } 20.000$$
> 4. **Surplus SNA (USD)** (FOB - FOB):
>    $$M_{\text{FOB}} = 100.000 - 8.000 - 2.000 = \text{USD } 90.000$$
>    $$\text{Surplus}_{\text{SNA}} = 120.000 - 90.000 = +\text{USD } 30.000$$
> 
> **Verifikasi Kode Python**:
> ```python
> x_fob_usd = 120000.0
> kurs_beli = 15500.0
> x_fob_idr = x_fob_usd * kurs_beli
> m_cif_usd = 100000.0
> freight_usd = 8000.0
> ins_usd = 2000.0
> m_fob_usd = m_cif_usd - freight_usd - ins_usd
> kurs_jual = 15600.0
> m_cif_idr = m_cif_usd * kurs_jual
> m_fob_idr = m_fob_usd * kurs_jual
> surplus_imts_usd = x_fob_usd - m_cif_usd
> surplus_imts_idr = x_fob_idr - m_cif_idr
> surplus_sna_usd = x_fob_usd - m_fob_usd
> print(f'Ekspor_FOB_IDR={x_fob_idr:.0f}, Impor_CIF_IDR={m_cif_idr:.0f}, Surplus_IMTS_USD={surplus_imts_usd:.0f}, Surplus_SNA_USD={surplus_sna_usd:.0f}')
> # Ekspor_FOB_IDR=1860000000, Impor_CIF_IDR=1560000000, Surplus_IMTS_USD=20000, Surplus_SNA_USD=30000
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Tertukar Kurs Konversi**: Eksportir memakai kurs beli bank, importir memakai kurs jual bank. Jangan gunakan kurs tengah atau membalik keduanya.
> 2. **Menyamakan Valuasi Impor BPS dan Neraca Pembayaran**: BPS merilis impor CIF secara bulanan, tetapi BI dan PDB penggunaan menghitung impor secara FOB (CIF dikurangi ongkos angkut dan asuransi).
> 3. **Menyertakan Pajak Impor dalam Nilai CIF**: Nilai CIF hanya mencakup harga barang + freight + insurance sampai pelabuhan bongkar, belum termasuk Bea Masuk, PPN Impor, atau PPh Pasal 22.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Ekspor itu Pergi (FOB di Pelabuhan Kita, Kurs Beli Bank); Impor itu Datang (CIF sampai Pelabuhan Kita, Kurs Jual Bank).

*Keterkaitan Konsep: 13.1.2, 13.1.3, 13.1.4*

### 13.1.2 Barang Dagangan Tanpa Masuk Pabean Merchanting

> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 5, 10-15]

> [!info]
> Memahami konsep merchanting goods SNA 2008, 3 syarat utama transaksi merchanting, perlakuan 'ekspor negatif' dan 'ekspor positif', serta reklasifikasi pos dari neraca jasa (BPM5) ke neraca barang (BPM6/SNA 2008).

> [!quote]
> **Teks Materi Kuliah**
> Merchanting adalah pembelian barang oleh residen (merchant) dari nonresiden, untuk selanjutnya dijual kembali pada nonresiden negara lain, dimana barang itu tanpa atau tidak berada di wilayah ekonomi residen merchant. Terjadi perubahan kepemilikan; tidak ada transformasi substansial pada barang; barang tidak memasuki wilayah residen merchant [slide 5].

**Intuisi Konsep**　Pernahkah Anda mendengar model bisnis dropshipping atau perantara komoditas global? Pedagang di Indonesia membeli batubara dari Australia dan menjualnya langsung ke pabrik baja di India. Kapal batubara berlayar lurus dari Sydney ke Mumbai tanpa pernah lewat laut Indonesia. Pedagang Indonesia menanggung risiko harga dan memiliki hak milik legal atas batubara tersebut sebelum menjualnya dengan keuntungan. Inilah *merchanting*. Meskipun Bea Cukai Indonesia tidak mencatatnya di pelabuhan, rekening bank pedagang di Indonesia menerima devisa neto hasil perdagangan barang tersebut.

**Definisi & Penjelasan Rigor**　### 1. Definisi dan Karakteristik Utama Merchanting (SNA 2008 & BPM6)

Menurut standar statistik internasional SNA 2008 paragraf 14.73 dan *Balance of Payments Manual 6th Edition* (BPM6) [slide 5]:
*Merchanting* didefinisikan sebagai perolehan barang oleh penduduk dari bukan penduduk yang diikuti oleh penjualan kembali barang tersebut kepada bukan penduduk lain, tanpa barang tersebut pernah memasuki wilayah ekonomi penduduk pedagang (*resident merchant*).

Tiga syarat kumulatif yang wajib dipenuhi [slide 5]:
1. **Alih Kepemilikan Ekonomi (*Change of Economic Ownership*)**:
   Pedagang residen benar-benar memegang hak milik legal dan menanggung risiko ekonomi atas barang tersebut di antara saat pembelian dan penjualan.
2. **Tanpa Transformasi Substansial (*No Substantial Transformation*)**:
   Barang tidak mengalami proses manufaktur atau fabrikasi yang mengubah klasifikasi kode HS barang. Tindakan yang diperbolehkan hanyalah penyimpanan, inspeksi, sortasi mutu, atau *packaging* kecil.
3. **Tanpa Lintasan Wilayah Pabean Fisik (*No Physical Entry into Domestic Territory*)**:
   Barang bergerak langsung dari negara pemasok asal ke negara pembeli akhir, atau singgah di pelabuhan/gudang transit negara ketiga tanpa pernah melintasi pabean negara pedagang.

### 2. Standar Pencatatan Akuntansi Neraca Perdagangan

Dalam pedoman manual terdahulu (BPM5), selisih nilai jual dan beli dicatat sebagai 'ekspor jasa perantara perdagangan'. Namun, dalam SNA 2008 dan BPM6 dilakukan reformasi fundamental [slide 5]:
1. **Transaksi Perolehan (Pembelian)**:
   Dicatat sebagai **ekspor barang bernilai negatif** (*negative exports of goods under merchanting*) di negara residen pedagang pada periode pembelian terjadi.
   - Alasan: Mencegah distorsi pada angka impor barang domestik (karena barang tersebut tidak pernah dinikmati atau dikonsumsi oleh masyarakat domestik).
2. **Transaksi Penjualan**:
   Dicatat sebagai **ekspor barang bernilai positif** (*goods sold under merchanting*) di negara residen pedagang pada periode penjualan terealisasi.
3. **Penyajian Neto**:
   Pada tabel ringkasan neraca transaksi berjalan, disajikan pos tunggal:
   $$\text{Ekspor Neto Barang di Bawah Merchanting} = \text{Nilai Penjualan} - \text{Nilai Perolehan}$$

### 3. Matriks Perbedaan Transaksi Perdagangan Khusus

| Jenis Transaksi | Alih Kepemilikan Barang? | Melintasi Fisik Pabean Domestik? | Ada Transformasi Fisik? | Pencatatan Neraca (SNA 2008) |
|---|---|---|---|---|
| **Perdagangan Reguler** | Ya | Ya | Tidak / Ya | Ekspor FOB / Impor CIF Barang Umum |
| **Merchanting Goods** | Ya | **Tidak** | Tidak | Ekspor Neto pada Neraca Barang |
| **Jasa Maklon (Outward Processing)** | Tidak | Ya | **Ya** | Impor/Ekspor Jasa Manufaktur |
| **Komisi Perantara (Brokerage)** | **Tidak** | Tidak | Tidak | Neraca Jasa (Fee Keagenan) |

**Contoh Soal 1 (Pilihan Ganda)**　Manakah pernyataan yang BENAR mengenai perlakuan pencatatan transaksi merchanting dalam neraca pembayaran menurut manual BPM6 dan SNA 2008?
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 5, 10]

- A. Selisih antara harga jual dan beli barang dicatat sebagai ekspor jasa perdagangan.
- B. Pembelian barang oleh pedagang residen dicatat sebagai impor barang biasa.
- C. Perolehan barang dicatat sebagai ekspor negatif dan penjualannya dicatat sebagai ekspor positif dalam neraca barang.
- D. Transaksi tidak dicatat sama sekali karena barang tidak melewati kawasan pabean fisik nasional.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: C**
> Jawaban: **C**.
> 
> **Pembahasan**:
> Sesuai standar BPM6 dan SNA 2008 [slide 5], transaksi merchanting dicatat sepenuhnya dalam Neraca Barang (Goods Account). Saat merchant residen membeli barang dari luar negeri, dicatat sebagai ekspor barang bernilai negatif (-). Ketika barang tersebut dijual kembali ke non-residen di negara lain, dicatat sebagai ekspor barang bernilai positif (+). Jumlah neto dari kedua aliran ini menghasilkan 'ekspor neto barang di bawah merchanting'.

**Contoh Soal 2 (Isian/Esai)**　Sebuah entitas dagang berstatus residen Indonesia membeli komoditas nikel dari Filipina seharga USD 200.000, lalu menjualnya ke pabrik baterai di Jepang seharga USD 260.000 tanpa membawa nikel tersebut ke wilayah Indonesia. Di samping itu, ekspor barang reguler fisik Indonesia adalah USD 1.500.000 dan impor barang reguler fisik FOB adalah USD 1.080.000.
Hitunglah:
1. Nilai perolehan barang merchanting (ekspor negatif).
2. Nilai penjualan barang merchanting (ekspor positif).
3. Ekspor neto barang di bawah merchanting.
4. Total ekspor barang SNA 2008 dan saldo neraca barang FOB-FOB.
Tuliskan jawaban format: `Acq=..., Sales=..., NetMerchanting=..., TotalX_SNA=..., GoodsBalance_SNA=...`.
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 5, 9, 10]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah Perhitungan:
> 1. **Nilai Perolehan (Ekspor Negatif)**: $$\text{Acq} = -\text{USD } 200.000$$
> 2. **Nilai Penjualan (Ekspor Positif)**: $$\text{Sales} = +\text{USD } 260.000$$
> 3. **Ekspor Neto Merchanting**:
>    $$\text{NetMerchanting} = 260.000 + (-200.000) = +\text{USD } 60.000$$
> 4. **Total Ekspor Barang SNA 2008**:
>    $$\text{TotalX\_SNA} = 1.500.000 + 60.000 = \text{USD } 1.560.000$$
>    - Saldo Neraca Barang (FOB - FOB):
>    $$\text{GoodsBalance\_SNA} = 1.560.000 - 1.080.000 = +\text{USD } 480.000$$
> 
> **Verifikasi Kode Python**:
> ```python
> acq_usd = -200000.0
> sales_usd = 260000.0
> net_merchanting = sales_usd + acq_usd
> x_regular_fob = 1500000.0
> total_x_sna = x_regular_fob + net_merchanting
> m_regular_fob = 1080000.0
> goods_balance_sna = total_x_sna - m_regular_fob
> print(f'Acq={acq_usd:.0f}, Sales={sales_usd:.0f}, NetMerchanting={net_merchanting:.0f}, TotalX_SNA={total_x_sna:.0f}, GoodsBalance_SNA={goods_balance_sna:.0f}')
> # Acq=-200000, Sales=260000, NetMerchanting=60000, TotalX_SNA=1560000, GoodsBalance_SNA=480000
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Menganggap Merchanting sebagai Jasa**: Sejak SNA 2008 dan BPM6, merchanting resmi masuk ke Neraca Barang (Goods), bukan Neraca Jasa.
> 2. **Mengabaikan Alih Kepemilikan**: Jika pedagang hanya menerima komisi 2% sebagai agen pencari pembeli tanpa pernah membeli dan memiliki barang, transaksi tersebut adalah jasa broker murni, bukan merchanting.
> 3. **Jika Barang Mengalami Pengolahan Pabrik**: Bila barang diubah bentuk secara fisik di negara ketiga, transaksi beralih menjadi 'goods for processing' / jasa manufaktur.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Merchanting: Barang Tidak Datang, Tapi Uang Datang; Dicatat di Neraca Barang Bukan Jasa.

*Keterkaitan Konsep: 13.1.1, 13.1.3*

### 13.1.3 Net Barter Terms of Trade NBToT ⭐

> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 10-16]

> [!info]
> Menguasai formulasi dan interpretasi Net Barter Terms of Trade (NBToT), formula dan 4 tahapan siklus produk Indeks Spesialisasi Perdagangan (ISP), serta formulasi Revealed Comparative Advantage (Balassa RCA) dan Openness Ratio.

> [!quote]
> **Teks Materi Kuliah**
> Indeks Spesialisasi Perdagangan (ISP) digunakan untuk menganalisis posisi atau tahapan perkembangan suatu produk sesuai siklus produk: Pengenalan (-1 s.d. -0,5), Substitusi Impor (-0,5 s.d. 0), Perluasan Ekspor (0 s.d. 0,8), Pematangan (mendekati 1). Formula ISP = (Xi - Mi)/(Xi + Mi). Revealed Comparative Advantage (RCA) mengukur keunggulan komparatif komoditi dengan membandingkan pangsa ekspor komoditi terhadap total ekspor negara dibanding pangsa dunia. Term of Trade (ToT) suatu negara dihitung dengan membagi indeks harga barang ekspornya dengan indeks harga barang impornya [slide 10-14].

**Intuisi Konsep**　Dua pertanyaan paling krusial bagi kementerian perdagangan suatu negara adalah:
1. *Apakah harga barang yang kita jual ke dunia naik lebih cepat dibanding harga barang yang kita beli dari luar negeri?* Ini dijawab oleh **Net Barter Terms of Trade (NBToT)**. Bila harga 1 ton batubara ekspor dulunya hanya bisa membeli 5 ton beras impor, lalu kini bisa membeli 7 ton beras impor, maka nilai tukar perdagangan kita membaik.
2. *Apakah komoditas kita menjadi tuan rumah di negeri sendiri dan mampu merajai pasar dunia?* Ini dijawab oleh **Indeks Spesialisasi Perdagangan (ISP)** dan **RCA Balassa**. ISP melacak perjalanan suatu industri dari bayi (baru kenal impor, ISP -1) hingga menjadi raksasa dunia (tahap matang, ISP mendekati +1).

**Definisi & Penjelasan Rigor**　### 1. Net Barter Terms of Trade (NBToT / Commodity Terms of Trade)

Net Barter Terms of Trade mengukur rasio pertukaran riil harga barang ekspor terhadap harga barang impor suatu negara [slide 13-15]:
$$\text{NBToT} = \frac{P_x}{P_m} \times 100 = \frac{\text{IIX}}{\text{IIM}} \times 100$$
dimana:
- $P_x$ / $\text{IIX}$ = Indeks harga (implisit) ekspor.
- $P_m$ / $\text{IIM}$ = Indeks harga (implisit) impor.
- Tahun dasar ditetapkan bernilai 100.

**Interpretasi Pergerakan Nilai ToT** [slide 14-15]:
1. **$\text{ToT} > 100$ (Favourable)**:
   - Harga ekspor meningkat relatif lebih cepat dibandingkan harga impor.
   - Memberikan *competitive effect* dan *wealth effect*: dengan volume ekspor yang sama, negara mampu membeli lebih banyak unit barang impor.
2. **$\text{ToT} < 100$ (Unfavourable)**:
   - Daya beli per unit ekspor terhadap impor terdepresiasi.
3. **Analisis Runtun Waktu (Slide 14 BPS)**:
   - Tahun 1 (Tahun Dasar): $P_x = 100, P_m = 100 \implies \text{ToT} = 100,0$.
   - Tahun 2: $P_x = 102, P_m = 100 \implies \text{ToT} = 102,0$ (naik 2%).
   - Tahun 3: $P_x = 106, P_m = 104 \implies \text{ToT} = 101,92$ (turun dibanding tahun 2, namun tetap di atas tahun dasar).
   - Tahun 4: $P_x = 110, P_m = 110 \implies \text{ToT} = 100,0$ (kembali ke daya beli tahun 1).
   - Tahun 5: $P_x = 108, P_m = 106 \implies \text{ToT} = 101,89$ (kedua harga turun, namun $P_m$ turun lebih dalam).

### 2. Indeks Spesialisasi Perdagangan (ISP / Trade Specialisation Ratio)

ISP menggambarkan apakah suatu negara berposisi sebagai eksportir neto atau importir neto untuk suatu komoditas, serta melacak siklus hidup produk (*product life-cycle*) [slide 10-11]:
$$\text{ISP}_i = \frac{X_i - M_i}{X_i + M_i}$$
dimana:
- $X_i$ = Nilai ekspor komoditas $i$.
- $M_i$ = Nilai impor komoditas $i$.
- Kisaran rentang: $-1,0 \le \text{ISP}_i \le +1,0$.

**Empat Tahapan Siklus Produk Berdasarkan Nilai ISP** [slide 10, diuji pada UAS 2022/2023]:

| Rentang Nilai ISP | Tahapan Siklus Produk | Karakteristik Perdagangan |
|---|---|---|
| $-1,00 \le \text{ISP} \le -0,50$ | **Tahap Pengenalan (*Introduction*)** | Produksi domestik baru dimulai/belum ada; kebutuhan dalam negeri didominasi impor secara masif ($M \gg X$). |
| $-0,50 < \text{ISP} \le 0,00$ | **Tahap Substitusi Impor (*Import Substitution*)** | Industri domestik mulai tumbuh mengurangi ketergantungan impor ($M > X$, namun defisit mengecil). |
| $0,00 < \text{ISP} \le 0,80$ | **Tahap Perluasan Ekspor (*Export Expansion*)** | Pasokan domestik melebihi kebutuhan lokal sehingga surplus mulai diekspor ke pasar dunia ($X > M$). |
| $0,80 < \text{ISP} \le 1,00$ | **Tahap Pematangan (*Maturation*)** | Komoditas berdaya saing global sangat tinggi dan merajai pasar ekspor ($X \gg M$, impor mendekati nol). |

### 3. Revealed Comparative Advantage (RCA Balassa)

Dikembangkan oleh Bela Balassa (1965) untuk mengukur keunggulan komparatif relatif suatu komoditas negara tertentu terhadap rata-rata perdagangan dunia [slide 12]:
$$\text{RCA}_{ij} = \frac{X_{ij} / X_j}{X_{iw} / X_w}$$
dimana:
- $X_{ij}$ = Nilai ekspor komoditas $i$ oleh negara $j$.
- $X_j$ = Nilai total ekspor seluruh komoditas oleh negara $j$.
- $X_{iw}$ = Nilai ekspor komoditas $i$ oleh seluruh dunia.
- $X_w$ = Nilai total ekspor seluruh komoditas dunia.

**Pedoman Interpretasi RCA** [slide 12]:
- $\text{RCA}_{ij} \ge 1$ : Negara $j$ memiliki **keunggulan komparatif kuat** (di atas rata-rata dunia) pada komoditas $i$.
- $\text{RCA}_{ij} < 1$ : Komoditas $i$ memiliki daya saing komparatif yang rendah/lemah di panggung internasional.

### 4. Derajat Keterbukaan Ekonomi (Trade Openness Ratio)

Mengukur seberapa besar integrasi perekonomian domestik terhadap pasar global [slide 9]:
$$\text{Trade Openness} = \frac{X_t + M_t}{\text{PDB}_t} \times 100\%$$

**Contoh Soal 1 (Pilihan Ganda)**　Berdasarkan data perdagangan komoditas suatu negara, jika nilai ekspor komoditas X adalah USD 350 juta dan nilai impornya adalah USD 164 juta, berapakah nilai Indeks Spesialisasi Perdagangan (ISP) dan berada pada tahapan apakah produk tersebut dalam siklus produk?
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 10-11 / UAS 2022-2023 PG 24, 25]

- A. ISP = 0,36; Tahap Perluasan Ekspor
- B. ISP = -0,36; Tahap Substitusi Impor
- C. ISP = 0,53; Tahap Pematangan
- D. ISP = 0,36; Tahap Substitusi Impor

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: A**
> Jawaban: **A**.
> 
> **Pembahasan**:
> 1. Hitung ISP:
>    $$\text{ISP} = \frac{X - M}{X + M} = \frac{350 - 164}{350 + 164} = \frac{186}{514} \approx 0,3619 \rightarrow 0,36$$
> 2. Tentukan tahapan siklus produk:
>    Karena ISP = 0,36 berada pada rentang $0,0 < \text{ISP} \le 0,8$, maka komoditas tersebut berada pada **Tahap Perluasan Ekspor** (*Export Expansion*).

**Contoh Soal 2 (Isian/Esai)**　Diberikan serangkaian indikator perdagangan luar negeri (rekonstruksi UAS OSL 2022/2023):
1. Komoditas karet: Ekspor $X = 350$, Impor $M = 164$. Hitung ISP karet dan tentukan tahapannya.
2. Jika komoditas lain memiliki nilai $\text{ISP} = -0,36$, tentukan tahapannya.
3. Indeks harga ekspor $P_x = 105$ dan indeks harga impor $P_m = 100$. Hitung nilai NBToT.
4. Ekspor karet nasional adalah USD 350 juta dari total ekspor nasional USD 2.500 juta. Ekspor karet dunia adalah USD 2.000 juta dari total ekspor dunia USD 40.000 juta. Hitung indeks RCA Balassa.
Tuliskan jawaban format: `ISP_Rubber=..., Stage_Rubber=..., Stage_Q25=..., NBToT=..., RCA=...`.
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 10-14 / UAS 2022-2023 PG 24, 25, 26]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah Perhitungan:
> 1. **ISP Karet**: $$\text{ISP} = \frac{350 - 164}{350 + 164} = \frac{186}{514} \approx 0,3619$$.
>    Karena $0,0 < 0,3619 \le 0,8$, maka **Perluasan Ekspor**.
> 2. **Tahap untuk ISP = -0,36**:
>    Karena $-0,5 < -0,36 \le 0,0$, maka **Substitusi Impor**.
> 3. **NBToT**:
>    $$\text{NBToT} = \frac{105}{100} \times 100 = 105,0$$
> 4. **RCA Balassa**:
>    $$\text{RCA} = \frac{350 / 2500}{2000 / 40000} = \frac{0,1400}{0,0500} = 2,80$$
> 
> **Verifikasi Kode Python**:
> ```python
> x_rubber = 350.0
> m_rubber = 164.0
> isp_rubber = (x_rubber - m_rubber) / (x_rubber + m_rubber)
> def get_stage(isp):
>     if -1.0 <= isp <= -0.5:
>         return 'Pengenalan'
>     elif -0.5 < isp <= 0.0:
>         return 'Substitusi Impor'
>     elif 0.0 < isp <= 0.8:
>         return 'Perluasan Ekspor'
>     elif 0.8 < isp <= 1.0:
>         return 'Pematangan'
>     return 'Invalid'
> stage_rubber = get_stage(isp_rubber)
> isp_q25 = -0.36
> stage_q25 = get_stage(isp_q25)
> px = 105.0
> pm = 100.0
> nbtot = (px / pm) * 100.0
> x_ij = 350.0
> x_j = 2500.0
> x_iw = 2000.0
> x_w = 40000.0
> rca = (x_ij / x_j) / (x_iw / x_w)
> print(f'ISP_Rubber={isp_rubber:.4f}, Stage_Rubber={stage_rubber}, Stage_Q25={stage_q25}, NBToT={nbtot:.1f}, RCA={rca:.2f}')
> # ISP_Rubber=0.3619, Stage_Rubber=Perluasan Ekspor, Stage_Q25=Substitusi Impor, NBToT=105.0, RCA=2.80
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Tertukar Tahap Siklus Produk**: Tahap Substitusi Impor bernilai negatif (-0,50 s.d. 0,00), bukan positif. Nilai positif (0,00 s.d. 0,80) adalah Perluasan Ekspor.
> 2. **Kekeliruan Ambang Batas RCA**: Ambang batas keunggulan komparatif adalah 1,0 (bukan 0 atau 100). RCA = 1 berarti pangsa ekspor negara persis sama dengan rata-rata dunia.
> 3. **Menyamakan ToT dengan Neraca Perdagangan**: ToT mengukur rasio harga indeks, sedangkan Neraca Perdagangan mengukur nilai total mata uang ($P \times Q$).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　ISP di bawah nol itu Masih Impor (Pengenalan & Substitusi); ISP di atas nol itu Sudah Ekspor (Perluasan & Pematangan).

*Keterkaitan Konsep: 13.1.1, 13.1.2, 13.1.4*

### 13.1.4 Gross Barter dan Income ToT

> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 13-16]

> [!info]
> Menguasai perbedaan analitis antara Net Barter ToT, Gross Barter ToT [SUPLEMEN], dan Income ToT / Kapasitas Impor (KM), serta interpretasi kondisi di mana NBToT turun namun Kapasitas Impor naik.

> [!quote]
> **Teks Materi Kuliah**
> Ada dua parameter yang dibahas yaitu Indeks Nilai Tukar (INT) dan Kapasitas Impor (KM) yang masing-masing menjelaskan tentang daya beli dan kemampuan mengimpor berdasarkan nilai ekspor. Indeks nilai tukar diperoleh dengan cara membagi indeks implisit (harga) ekspor (IIX) dengan indeks implisit (harga) impor (IIM). Sedangkan KM diperoleh dengan cara membagi nilai ekspor atas dasar harga berlaku dengan indeks implisit impor (IIM) [slide 15].

**Intuisi Konsep**　Jika harga satu kilogram kopi kita turun dari Rp 100 ribu menjadi Rp 90 ribu (harga relatif turun -> NBToT memburuk), apakah kita otomatis jatuh miskin? Belum tentu! Jika petani kita sebelumnya hanya mampu memanen 100 kg dan sekarang mampu memanen 200 kg kopi, penerimaan total melonjak dari Rp 10 juta menjadi Rp 18 juta. Dengan uang Rp 18 juta tersebut, jumlah karung gandum impor yang bisa dibeli justru meningkat drastis. Itulah intisari **Income Terms of Trade (Kapasitas Impor)**: daya beli riil devisa hasil ekspor menggabungkan efek harga DAN volume.

**Definisi & Penjelasan Rigor**　### 1. Taksonomi Tiga Konsep Terms of Trade Utama

Dalam literatur ekonomi perdagangan internasional dan statistik neraca nasional BPS [slide 15]:

1. **Net Barter Terms of Trade (NBToT / Commodity ToT)**:
   $$\text{NBToT} = \frac{P_x}{P_m} \times 100$$
   - Mengukur rasio harga pertukaran per unit komoditas ekspor terhadap impor.
   - Bersifat statis harga, tidak memperhitungkan kuantitas barang yang diperdagangkan.

2. **Gross Barter Terms of Trade (GBToT) [SUPLEMEN]**:
   Diformulasikan oleh ekonom Frank W. Taussig (1927):
   $$\text{GBToT} = \frac{Q_m}{Q_x} \times 100$$
   - Mengukur rasio volume fisik barang impor yang diperoleh ($Q_m$) per unit volume fisik barang ekspor yang dikirim ($Q_x$).
   - Digunakan untuk melihat transfer riil sumber daya fisik, terutama bila negara menerima pinjaman luar negeri, bantuan hibah modal (*unilateral transfers*), atau pembayaran bunga utang.

3. **Income Terms of Trade (Kapasitas Impor / KM)**:
   Diformulasikan oleh G.S. Dorrance (1948) dan diadopsi dalam publikasi BPS [slide 15]:
   $$\text{Income ToT} = \text{KM} = \frac{\text{NBToT} \times Q_x}{100} = \frac{P_x \times Q_x}{P_m} = \frac{X_{\text{ADHB}}}{\text{IIM}} \times 100$$
   - Mengukur daya beli riil total dari seluruh devisa ekspor terhadap barang impor.
   - Menunjukkan kapasitas atau daya serap impor yang dapat dibiayai murni dari penerimaan ekspor tanpa menguras cadangan devisa atau menambah utang luar negeri.

### 2. Matriks Perbandingan Ketiga Indikator Terms of Trade

| Karakteristik | Net Barter ToT (NBToT) | Gross Barter ToT (GBToT) [SUPLEMEN] | Income ToT / Kapasitas Impor (KM) |
|---|---|---|---|
| **Variabel Utama** | Indeks Harga ($P_x, P_m$) | Indeks Volume Kuantum ($Q_m, Q_x$) | Indeks Nilai Riil ($P_x, P_m, Q_x$) |
| **Formula Matematis** | $(P_x / P_m) \times 100$ | $(Q_m / Q_x) \times 100$ | $(\text{NBToT} \times Q_x) / 100$ |
| **Dimensi Pengukuran** | Daya beli per unit barang ekspor | Rasio pertukaran fisik kuantum | Total kapasitas membeli barang impor |
| **Status Publikasi BPS** | Diterbitkan resmi (Indeks Nilai Tukar) | Indikator riset akademis / suplemen | Diterbitkan resmi (Kapasitas Impor / KM) |
| **Respon terhadap Kuantitas** | Tidak terpengaruh perubahan $Q_x$ | Berbanding terbalik dengan $Q_x$ | Meningkat seiring kenaikan $Q_x$ |

### 3. Dinamika Hubungan NBToT dan Kapasitas Impor

Hubungan pertumbuhan antara Kapasitas Impor dan komponennya dapat diturunkan secara logaritmik:
$$\ln(\text{KM}) = \ln(\text{NBToT}) + \ln(Q_x) - \ln(100)$$
$$\Delta \% \text{KM} \approx \Delta \% \text{NBToT} + \Delta \% Q_x$$
- Jika $\Delta \% Q_x > |\Delta \% \text{NBToT}|$, maka Kapasitas Impor akan tetap tumbuh positif meskipun Net Barter Terms of Trade mengalami penurunan (pemburukan harga relatif). Kondisi ini sangat umum terjadi pada negara berkembang pengekspor komoditas primer yang melakukan modernisasi dan hilirisasi kuantitas.

**Contoh Soal 1 (Pilihan Ganda)**　Jika indeks harga ekspor suatu negara turun 5% sementara indeks harga impor naik 5%, namun pada saat yang sama volume ekspor berhasil dinaikkan sebesar 25%, bagaimana arah pergerakan Net Barter Terms of Trade (NBToT) dan Kapasitas Impor (Income ToT)?
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 15]

- A. NBToT naik dan Kapasitas Impor naik.
- B. NBToT turun dan Kapasitas Impor turun.
- C. NBToT turun namun Kapasitas Impor naik.
- D. NBToT naik namun Kapasitas Impor turun.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: C**
> Jawaban: **C**.
> 
> **Pembahasan**:
> 1. Hitung perubahan NBToT:
>    $$\text{NBToT} = \frac{95,0}{105,0} \times 100 = 90,48 < 100 \quad (\text{turun / memburuk})$$
> 2. Hitung Kapasitas Impor (Income ToT):
>    $$\text{Income ToT} = \frac{\text{NBToT} \times Q_x}{100} = \frac{90,48 \times 125,0}{100} = 113,10 > 100 \quad (\text{naik / membaik})$$
> Karena kenaikan volume ekspor (+25%) lebih besar daripada kontraksi rasio harga (-9,52%), maka daya beli devisa total (Kapasitas Impor) justru mengalami kenaikan.

**Contoh Soal 2 (Isian/Esai)**　Diberikan data indeks perdagangan tahun berjalan (tahun dasar t=0 = 100):
- Indeks harga ekspor $P_x = 95,0$
- Indeks harga impor $P_m = 105,0$
- Indeks volume ekspor $Q_x = 125,0$
- Indeks volume impor $Q_m = 110,0$
Hitunglah:
1. Net Barter Terms of Trade (NBToT).
2. Gross Barter Terms of Trade (GBToT) [SUPLEMEN].
3. Income Terms of Trade / Kapasitas Impor (KM).
Tuliskan jawaban format: `NBToT=..., GBToT=..., IncomeToT=..., KM=...`.
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 13-16]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah Perhitungan:
> 1. **NBToT**:
>    $$\text{NBToT} = \frac{95,0}{105,0} \times 100 = 90,4762 \approx 90,48$$
> 2. **GBToT [SUPLEMEN]**:
>    $$\text{GBToT} = \frac{110,0}{125,0} \times 100 = 88,00$$
> 3. **Income ToT / KM**:
>    $$\text{Income ToT} = \frac{90,4762 \times 125,0}{100} = 113,0952 \approx 113,10$$
>    - Nilai KM ekivalen dengan Income ToT: $$\text{KM} = 113,10$$
> 
> **Verifikasi Kode Python**:
> ```python
> px = 95.0
> pm = 105.0
> qx = 125.0
> qm = 110.0
> nbtot = (px / pm) * 100.0
> gbtot = (qm / qx) * 100.0
> income_tot = (nbtot * qx) / 100.0
> export_val_adhb = (px * qx) / 100.0
> km = (export_val_adhb / pm) * 100.0
> print(f'NBToT={nbtot:.2f}, GBToT={gbtot:.2f}, IncomeToT={income_tot:.2f}, KM={km:.2f}')
> # NBToT=90.48, GBToT=88.00, IncomeToT=113.10, KM=113.10
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Tertukar Formulasi GBToT**: Pembilangnya adalah Impor ($Q_m$), penyebutnya adalah Ekspor ($Q_x$). Jangan menyamakan dengan NBToT yang pembilangnya adalah Ekspor ($P_x$).
> 2. **Mengabaikan Efek Volume pada Kapasitas Impor**: Jangan hanya melihat penurunan NBToT saat menganalisis kemampuan impor suatu negara; selalu periksa apakah volume ekspor mengalami lonjakan.
> 3. **Satuan Tahun Dasar**: Ingat bahwa pada tahun dasar, $\text{NBToT} = 100$, $Q_x = 100$, dan $\text{Income ToT} = 100$. Nilai perhitungan berikutnya diinterpretasikan terhadap basis 100.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Net Barter itu Harga Per Unit; Gross Barter itu Volume Fisik; Income ToT itu Total Uang Kas Belanja Impor.

*Keterkaitan Konsep: 13.1.1, 13.1.3*

## 13.2 Statistik Pariwisata dan Perhotelan `[Pembahasan Mendalam]`

### 13.2.1 Definisi Wisman dan Wisnus

> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 32-38]

> [!info]
> Menguasai definisi operasional wisman UNWTO, pembedaan wisman vs wisnas vs wisnus, kriteria durasi (< 12 bulan) dan non-remunerasi, pembedaan tourist vs excursionist, serta pergeseran konsep wisnus pasca SP 2020.

> [!quote]
> **Teks Materi Kuliah**
> Definisi wisatawan mancanegara (wisman) sesuai rekomendasi UNWTO: setiap orang yang melakukan perjalanan ke suatu negara di luar tempat tinggalnya (usual country of residence), kurang dari satu tahun, didorong oleh suatu tujuan utama (bisnis, berlibur, atau tujuan pribadi lainnya), selain untuk bekerja dengan penduduk negara yang dikunjungi. Wisatawan (tourist) tinggal paling sedikit 24 jam; pelancong (excursionist) tinggal kurang dari 24 jam. Wisnus pasca SP 2020: perjalanan < 12 bulan bukan untuk bekerja/sekolah rutin [slide 33-36].

**Intuisi Konsep**　Statistik pariwisata adalah pengukur konsumsi devisa dan peredaran uang rekreasi. Jika seorang turis asal Australia berlibur 5 hari di Bali, dia membawa tabungan dari negaranya untuk dibelanjakan di restoran, hotel, dan toko kerajinan lokal. Ini adalah *inbound tourism* murni. Sebaliknya, jika ada insinyur Australia yang dikontrak setahun oleh pabrik semen di Gresik dan digaji rupiah dari kas pabrik tersebut, uangnya berasal dari dalam negeri, sehingga ia bukan wisatawan melainkan tenaga kerja.

**Definisi & Penjelasan Rigor**　### 1. Klasifikasi Pengunjung Menurut Rekomendasi UNWTO

Dalam *International Recommendations for Tourism Statistics* (IRTS 2008) yang diadopsi BPS [slide 33]:
- **Wisatawan Mancanegara (Wisman / Inbound Tourists)**: Orang yang melakukan perjalanan ke suatu negara di luar lingkungan tempat tinggal biasanya (*usual country of residence*), berlangsung selama **kurang dari 12 bulan**, dengan tujuan apa pun selain dipekerjakan oleh entitas residen di negara yang dikunjungi.
- **Wisatawan Nasional (Wisnas / Outbound Tourists)**: Penduduk Indonesia yang melakukan perjalanan ke luar negeri bukan untuk bekerja tetap atau memperoleh penghasilan di luar negeri, berlangsung kurang dari 12 bulan [slide 35].
- **Wisatawan Nusantara (Wisnus / Domestic Tourists)**: Penduduk Indonesia yang melakukan perjalanan di dalam wilayah teritori Indonesia di luar *usual environment* [slide 36].

### 2. Pembedaan Wisatawan (*Tourist*) vs Pelancong (*Excursionist*)

Berdasarkan durasi menginap pada lokasi tujuan [slide 34]:
1. **Wisatawan (*Tourist* / Pengunjung Menginap)**:
   - Menginap paling sedikit 24 jam (minimal satu malam) di fasilitas akomodasi komersial maupun akomodasi pribadi di tempat yang dikunjungi.
   - Durasi: $24 \text{ jam} \le t < 12 \text{ bulan}$.
2. **Pelancong (*Excursionist* / Same-day Visitor / Day Tripper)**:
   - Berada di wilayah tujuan kurang dari 24 jam (tidak bermalam di akomodasi setempat).
   - Termasuk penumpang kapal pesiar (*cruise passengers*) yang singgah di pelabuhan untuk berkeliling di darat pada siang hari namun kembali tidur di kabin kapal pesiar.

### 3. Pengecualian dari Kategori Wisatawan Mancanegara (UNWTO)

Kelompok yang **tidak dicatat** sebagai wisman saat memasuki perbatasan [slide 35]:
1. Pejabat diplomatik, korps konsuler, dan anggota angkatan bersenjata asing yang ditugaskan resmi beserta tanggungan keluarganya.
2. Warga Negara Asing (WNA) yang telah tinggal di Indonesia lebih dari 12 bulan (berstatus *resident* penduduk Indonesia).
3. Pekerja migran dan tenaga kerja asing yang datang dengan tujuan utama bekerja dan menerima remunerasi dari perusahaan residen Indonesia.
4. Pengungsi (*refugees*) dan nomad imigran yang mencari suaka.

### 4. Pergeseran Konsep Wisatawan Nusantara (Wisnus) BPS

| Dimensi | Konsep Sebelum Sensus Penduduk 2020 | Konsep Setelah Sensus Penduduk 2020 |
|---|---|---|
| **Batas Waktu** | Kurang dari 6 bulan | Kurang dari 12 bulan (selaras UNWTO) |
| **Kriteria Perjalanan** | Menuju objek komersial berbayar, menginap di hotel, ATAU jarak $> 100\text{ km}$ pp | Di luar *usual environment*, bukan perjalanan rutin bekerja/sekolah |
| **Definisi Lingkungan Keseharian** | Belum terdefinisi secara ketat berbasis geolokasi | Rumah tinggal, tempat bekerja, dan rumah kedua |
| **Pendekatan Sumber Data** | Survei Susenas & Survei Wisnus konvensional | Integrasi Big Data **Mobile Positioning Data (MPD)** operator seluler + Penimbang Susenas Maret |

**Contoh Soal 1 (Pilihan Ganda)**　Manakah dari individu berikut yang SAH diklasifikasikan sebagai wisatawan mancanegara (inbound tourist) ke Indonesia menurut standar UNWTO dan BPS?
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 33-35]

- A. Seorang WNA yang bertugas sebagai sekretaris kedutaan besar asing di Jakarta selama 3 tahun.
- B. Warga negara Jepang yang berlibur di Bali selama 7 hari dan menginap di hotel kawasan Nusa Dua.
- C. Penumpang kapal pesiar yang turun berbelanja cenderamata di Pelabuhan Benoa selama 6 jam lalu kembali tidur di kapal.
- D. Warga negara asing yang bekerja dan menerima gaji bulanan sebagai manajer pabrik tekstil di Karawang.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan**:
> - Pilihan A: Diplomat asing dikecualikan dari statistik pariwisata [slide 35].
> - Pilihan B: WNA Jepang menginap $\ge 24$ jam (7 hari), $< 12$ bulan, tujuan rekreasi, tidak digaji penduduk lokal -> sah sebagai Wisatawan Mancanegara (Tourist) [slide 33-34].
> - Pilihan C: Penumpang kapal pesiar $< 24$ jam dan tidur di kapal diklasifikasikan sebagai Pelancong (Excursionist), bukan Tourist [slide 34].
> - Pilihan D: Bekerja dan digaji oleh entitas lokal merupakan kriteria eksklusi (bukan wisatawan) [slide 33].

**Contoh Soal 2 (Isian/Esai)**　Dari 10.000 kedatangan WNA di pelabuhan laut internasional, terdapat: 6.500 wisatawan menginap di hotel, 1.200 penumpang cruise singgah 8 jam (tidur di kapal), 300 staf kedutaan asing, 1.500 TKA kontrak 2 tahun digaji lokal, dan 500 ekspatriat residen Indonesia pulang dari luar negeri.
Hitunglah:
1. Jumlah wisatawan mancanegara (tourists).
2. Jumlah pelancong mancanegara (excursionists).
3. Total pengunjung mancanegara (inbound visitors).
4. Total bukan pengunjung mancanegara (non-visitors).
5. Persentase wisatawan terhadap total pengunjung sah.
Tuliskan format: `Tourists=..., Excursionists=..., TotalVisitors=..., NonVisitors=..., PctTourists=...`.
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 33-35]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah Perhitungan:
> 1. **Tourists** = 6.500 orang (menginap $\ge 24$ jam, non-remunerasi).
> 2. **Excursionists** = 1.200 orang (kunjungan $< 24$ jam kapal pesiar).
> 3. **Total Visitors** = $6.500 + 1.200 = 7.700$ orang.
> 4. **Non-Visitors** = $300 (\text{diplomat}) + 1.500 (\text{TKA}) + 500 (\text{residen}) = 2.300$ orang.
> 5. **Persentase Wisatawan**:
>    $$\% \text{Tourists} = \frac{6.500}{7.700} \times 100\% \approx 84,42\%$$
> 
> **Verifikasi Kode Python**:
> ```python
> total_arrivals = 10000
> tourists = 6500
> excursionists = 1200
> diplomats = 300
> contract_workers = 1500
> residents_foreign = 500
> total_inbound_visitors = tourists + excursionists
> non_visitors = diplomats + contract_workers + residents_foreign
> pct_tourists = (tourists / total_inbound_visitors) * 100.0
> print(f'Tourists={tourists}, Excursionists={excursionists}, TotalVisitors={total_inbound_visitors}, NonVisitors={non_visitors}, PctTourists={pct_tourists:.2f}')
> # Tourists=6500, Excursionists=1200, TotalVisitors=7700, NonVisitors=2300, PctTourists=84.42
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Tertukar Batas 24 Jam**: Menginap minimal 24 jam adalah syarat menjadi Tourist (bukan Excursionist).
> 2. **Salah Memperlakukan WNA Residen**: WNA yang sudah tinggal > 1 tahun di Indonesia dianggap penduduk; saat pulang dari luar negeri dicatat sebagai 'penduduk yang kembali', bukan wisman.
> 3. **Penumpang Cruise**: Penumpang kapal pesiar yang singgah 1-2 hari namun tidur di atas kapal dihitung sebagai Excursionist (bukan Tourist).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Tourist itu Tidur/Menginap (>= 24 jam); Excursionist itu Ekskursi Singkat (< 24 jam); Keduanya adalah Pengunjung (Visitor).

*Keterkaitan Konsep: 13.2.2, 13.2.3*

### 13.2.2 Tingkat Penghunian Kamar TPK Hotel ⭐

> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 36-41]

> [!info]
> Menguasai formulasi TPK BPS, penghitungan malam kamar tersedia (kamar x hari), formula TPTT, RTK, dan RTH, serta pemahaman instrumen survei VHTS vs VHTL.

> [!quote]
> **Teks Materi Kuliah**
> Tingkat Penghunian Kamar (TPK) hotel yaitu perbandingan antara banyaknya malam kamar yang terpakai dengan banyaknya malam kamar yang tersedia (dalam persen). Angka ini memberikan gambaran berapa persen kamar yang tersedia pada akomodasi terisi oleh tamu yang menginap dalam suatu waktu tertentu. Sumber data: Kuesioner VHTS (bulanan) secara sensus untuk hotel berbintang dan sampel untuk non-bintang; VHTL (tahunan) secara sensus [slide 39-41].

**Intuisi Konsep**　Jika sebuah hotel memiliki 100 kamar dan di suatu malam terisi 60 kamar, maka TPK malam itu adalah 60%. Bagaimana jika kita menghitung selama satu bulan penuh (30 hari)? Hotel tersebut memiliki 'stok jualan' sebanyak 100 kamar x 30 malam = 3.000 malam kamar. Jika selama sebulan itu total transaksi menginap mencapai 1.800 malam kamar, maka TPK bulanannya adalah 1.800 / 3.000 = 60%. Angka 60% ini mencerminkan produktivitas aset hotel.

**Definisi & Penjelasan Rigor**　### 1. Definisi dan Konseptualisasi TPK Hotel

Tingkat Penghunian Kamar (TPK / Room Occupancy Rate) adalah indikator pokok kinerja industri akomodasi [slide 39]:
- Mengukur efisiensi pemanfaatan fasilitas akomodasi komersial.
- Menjadi indikator proksi sisi penawaran (*supply side*) dalam Neraca Satelit Pariwisata Nasional (NESPARNAS) menggunakan kerangka Tabel Input-Output (I-O).

### 2. Formulasi Matematis Indikator Akomodasi Perhotelan BPS

Berdasarkan pedoman Survei VHTS BPS [slide 41]:

1. **Tingkat Penghunian Kamar (TPK)**:
   $$\text{TPK} = \frac{\text{Malam Kamar Terpakai}}{\text{Malam Kamar Tersedia}} \times 100\%$$
   $$\text{Malam Kamar Tersedia} = \text{Jumlah Kamar yang Siap Jual} \times \text{Jumlah Hari Operasi Hotel}$$

2. **Tingkat Pemakaian Tempat Tidur (TPTT / Bed Occupancy Rate)**:
   $$\text{TPTT} = \frac{\text{Banyaknya Malam Tamu}}{\text{Tempat Tidur yang Tersedia}} \times 100\%$$
   $$\text{Tempat Tidur Tersedia} = \text{Jumlah Tempat Tidur Fisik} \times \text{Jumlah Hari Operasi Hotel}$$

3. **Rata-rata Tamu per Kamar (RTK / Guests per Room)**:
   $$\text{RTK} = \frac{\text{Banyaknya Malam Tamu}}{\text{Malam Kamar yang Terjual}}$$
   - Menunjukkan rata-rata densitas hunian per kamar yang disewa (biasanya bernilai antara 1,2 s.d. 2,0 orang per kamar).

4. **Rata-rata Tamu per Hari (RTH)**:
   $$\text{RTH} = \frac{\text{Banyaknya Tamu yang Menginap}}{\text{Jumlah Hari Kerja/Operasi Hotel}}$$

### 3. Instrumen Pengumpulan Data Akomodasi BPS

| Karakteristik | Survei VHTS (Bulanan) | Survei VHTL (Tahunan) |
|---|---|---|
| **Frekuensi Pendataan** | Bulanan | Tahunan |
| **Cakupan Akomodasi** | Sensus untuk Hotel Berbintang; Sampel probabilitas untuk Hotel Non-Bintang | Sensus seluruh usaha akomodasi (berbintang dan non-bintang) |
| **Variabel Utama** | TPK, RLMT, jumlah tamu datang (wisman & wisnus), malam kamar terjual | Direktori hotel, tenaga kerja, tarif kamar, fasilitas, pendapatan usaha, neraca rugi-laba |

**Contoh Soal 1 (Pilihan Ganda)**　Sebuah hotel memiliki 50 kamar dan buka selama 30 hari dalam sebulan. Jika selama bulan tersebut tercatat 900 malam kamar yang terhuni oleh tamu, berapakah Tingkat Penghunian Kamar (TPK) hotel tersebut?
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 39-41]

- A. 30,0%
- B. 45,0%
- C. 60,0%
- D. 75,0%

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: C**
> Jawaban: **C**.
> 
> **Pembahasan**:
> 1. Malam kamar tersedia = 50 kamar x 30 hari = 1.500 malam kamar.
> 2. TPK = (Malam kamar terpakai / Malam kamar tersedia) x 100%:
>    $$\text{TPK} = \frac{900}{1.500} \times 100\% = 60,0\%$$ [slide 41].

**Contoh Soal 2 (Isian/Esai)**　Sebuah hotel berbintang memiliki 100 kamar dan 160 tempat tidur, beroperasi selama 30 hari di bulan September. Terjual 1.800 malam kamar, 1.200 tamu menginap, dengan total akumulasi 2.700 malam tamu.
Hitunglah:
1. Malam kamar tersedia.
2. TPK hotel (persen).
3. TPTT hotel (persen).
4. Rata-rata tamu per kamar (RTK).
5. Rata-rata tamu per hari (RTH).
Tuliskan jawaban format: `AvailableRoomNights=..., TPK=..., TPTT=..., RTK=..., RTH=...`.
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 40-41 / Rekonstruksi Uji OSL]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah Perhitungan:
> 1. **AvailableRoomNights** = $100 \times 30 = 3.000$.
> 2. **TPK** = $(1.800 / 3.000) \times 100\% = 60,00\%$.
> 3. **TPTT** = Bed tersedia = $160 \times 30 = 4.800$.
>    $$\text{TPTT} = \frac{2.700}{4.800} \times 100\% = 56,25\%$$
> 4. **RTK** = $2.700 / 1.800 = 1,50$ orang/kamar.
> 5. **RTH** = $1.200 / 30 = 40,0$ tamu/hari.
> 
> **Verifikasi Kode Python**:
> ```python
> rooms = 100
> days = 30
> available_room_nights = rooms * days
> sold_room_nights = 1800
> tpk = (sold_room_nights / available_room_nights) * 100.0
> beds = 160
> available_bed_nights = beds * days
> guest_nights = 2700
> tptt = (guest_nights / available_bed_nights) * 100.0
> rtk = guest_nights / sold_room_nights
> total_guests = 1200
> rth = total_guests / days
> print(f'AvailableRoomNights={available_room_nights}, TPK={tpk:.2f}%, TPTT={tptt:.2f}%, RTK={rtk:.2f}, RTH={rth:.1f}')
> # AvailableRoomNights=3000, TPK=60.00%, TPTT=56.25%, RTK=1.50, RTH=40.0
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Lupa Faktor Hari**: Menghitung malam kamar tersedia hanya dari jumlah kamar tanpa dikali jumlah hari dalam sebulan.
> 2. **Kamar Rusak / Renovasi**: Kamar yang sedang rusak berat atau tidak dapat dihuni (*out of order*) dikeluarkan dari pembagi malam kamar tersedia.
> 3. **Komplementer Tamu**: Tamu komplementer (gratis) yang menempati kamar tetap dihitung sebagai kamar terpakai jika kamar tersebut tercatat dihuni dalam sistem reservasi.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　TPK = Kamar Terjual dibagi (Jumlah Kamar x Jumlah Hari Buka) x 100%.

*Keterkaitan Konsep: 13.2.1, 13.2.3*

### 13.2.3 Rata-rata Lama Menginap Tamu RLMT

> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 40-43]

> [!info]
> Menguasai definisi operasional dan formula RLMT BPS, perbedaan rata-rata tertimbang vs rata-rata sederhana pada RLMT gabungan, serta karakteristik durasi wisman vs wisnus.

> [!quote]
> **Teks Materi Kuliah**
> Rata-rata Lama Menginap Tamu dihitung dari banyaknya malam tamu dibagi tamu yang datang dan menginap. Indikator ini mencerminkan loyalitas dan pola konsumsi wisatawan di destinasi wisata. Disagregasi menurut tamu asing dan tamu nasional disajikan rutin dalam Berita Resmi Statistik (BRS) Perkembangan Pariwisata BPS [slide 41-42].

**Intuisi Konsep**　Jika sebuah bus pariwisata menurunkan 40 orang wisatawan dan mereka tinggal di hotel selama 3 malam, maka mereka menyumbang $40 \times 3 = 120$ malam tamu. Jika ada tamu lain sebanyak 10 orang yang hanya tinggal 1 malam (10 malam tamu), total tamu datang adalah 50 orang dan total malam tamu adalah 130 malam tamu. Rata-rata lama menginap mereka adalah $130 / 50 = 2,6$ malam. RLMT memberitahu manajer hotel dan dinas pariwisata berapa lama uang belanja turis bertahan di daerah tersebut.

**Definisi & Penjelasan Rigor**　### 1. Definisi dan Signifikansi RLMT

Rata-rata Lama Menginap Tamu (RLMT / Average Length of Stay - ALOS) mengukur durasi retensi wisatawan di suatu wilayah [slide 41]:
- Semakin tinggi RLMT, semakin besar multiplier effect pengeluaran wisatawan terhadap perekonomian lokal (transportasi, kuliner, suvenir, atraksi).
- Menjadi parameter penting dalam memproyeksikan devisa pariwisata pada *Passenger Exit Survey* (PES) dan Neraca Satelit Pariwisata Nasional (NESPARNAS).

### 2. Formulasi Matematis BPS

Berdasarkan kuesioner bulanan VHTS BPS [slide 41]:

1. **RLMT Total / Gabungan**:
   $$\text{RLMT} = \frac{\text{Banyaknya Malam Tamu Menginap}}{\text{Banyaknya Tamu yang Datang dan Menginap}}$$
   $$\text{RLMT} = \frac{\sum_{j=1}^m T_j \times d_j}{\sum_{j=1}^m T_j}$$
   dimana $T_j$ adalah jumlah tamu pada rombongan ke-$j$ dan $d_j$ adalah lama menginap rombongan ke-$j$.

2. **Disagregasi Menurut Kebangsaan Tamu**:
   - **RLMT Wisman (Tamu Asing)**:
     $$\text{RLMT}_{\text{wisman}} = \frac{\text{Malam Tamu Asing}}{\text{Tamu Asing yang Datang}}$$
   - **RLMT Wisnus (Tamu Domestik/Nasional)**:
     $$\text{RLMT}_{\text{wisnus}} = \frac{\text{Malam Tamu Nasional}}{\text{Tamu Nasional yang Datang}}$$

3. **Formula Agregasi Tertimbang**:
   $$\text{RLMT}_{\text{total}} = \frac{\text{Malam Tamu}_{\text{wisman}} + \text{Malam Tamu}_{\text{wisnus}}}{\text{Tamu}_{\text{wisman}} + \text{Tamu}_{\text{wisnus}}}$$
   Atau dapat dituliskan sebagai rata-rata tertimbang (*weighted average*):
   $$\text{RLMT}_{\text{total}} = w_{\text{wisman}} \cdot \text{RLMT}_{\text{wisman}} + w_{\text{wisnus}} \cdot \text{RLMT}_{\text{wisnus}}$$
   dimana pembobot $w$ adalah proporsi jumlah tamu yang datang:
   $$w_{\text{wisman}} = \frac{\text{Tamu}_{\text{wisman}}}{\text{Total Tamu}}, \quad w_{\text{wisnus}} = \frac{\text{Tamu}_{\text{wisnus}}}{\text{Total Tamu}}$$

### 3. Matriks Perbedaan Indikator Perhotelan BPS

| Indikator | Satuan | Pembilang | Penyebut | Fungsi Analisis |
|---|---|---|---|---|
| **TPK (Room Occupancy)** | Persen (%) | Malam Kamar Terpakai | Malam Kamar Tersedia | Produktivitas kapasitas kamar fisik |
| **TPTT (Bed Occupancy)** | Persen (%) | Malam Tamu Terpakai | Tempat Tidur Tersedia | Pemanfaatan kapasitas ranjang |
| **RLMT (Length of Stay)** | Hari / Malam | Total Malam Tamu | Total Tamu Datang | Durasi retensi tamu di destinasi |
| **RTK (Guests per Room)** | Orang / Kamar | Total Malam Tamu | Malam Kamar Terjual | Kepadatan hunian kamar |

**Contoh Soal 1 (Pilihan Ganda)**　Di sebuah hotel resor, terdapat 300 tamu asing dengan 900 malam tamu dan 200 tamu domestik dengan 350 malam tamu. Berapakah Rata-rata Lama Menginap Tamu (RLMT) secara total?
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 41]

- A. 2,38 malam
- B. 2,50 malam
- C. 2,75 malam
- D. 3,00 malam

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan**:
> 1. Total malam tamu = $900 + 350 = 1.250$ malam tamu.
> 2. Total tamu datang = $300 + 200 = 500$ orang.
> 3. RLMT total = Total malam tamu / Total tamu datang:
>    $$\text{RLMT}_{\text{total}} = \frac{1.250}{500} = 2,50 \text{ malam}$$ [slide 41].
> (Catatan: Menghitung rata-rata sederhana $(3,00 + 1,75) / 2 = 2,375$ malam adalah salah karena jumlah tamu asing dan domestik tidak seimbang).

**Contoh Soal 2 (Isian/Esai)**　Data tamu hotel bintang 5: Tamu asing 300 orang (900 malam tamu), tamu domestik 200 orang (350 malam tamu).
Hitunglah:
1. RLMT tamu asing.
2. RLMT tamu domestik.
3. Total tamu dan total malam tamu.
4. RLMT gabungan (total).
5. Persentase tamu asing dari total tamu.
Tuliskan format: `RLMT_Foreign=..., RLMT_Domestic=..., TotalGuests=..., TotalNights=..., RLMT_Total=..., PctForeign=...`.
> 📎 [Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md, slide 40-42 / Rekonstruksi Uji OSL]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah Perhitungan:
> 1. **RLMT Tamu Asing** = $900 / 300 = 3,00$ malam.
> 2. **RLMT Tamu Domestik** = $350 / 200 = 1,75$ malam.
> 3. **Total Tamu** = $300 + 200 = 500$ orang. **Total Malam Tamu** = $900 + 350 = 1.250$ malam.
> 4. **RLMT Total** = $1.250 / 500 = 2,50$ malam.
> 5. **Persentase Tamu Asing** = $(300 / 500) \times 100\% = 60,0\%$.
> 
> **Verifikasi Kode Python**:
> ```python
> guests_foreign = 300
> nights_foreign = 900
> rlmt_foreign = nights_foreign / guests_foreign
> guests_domestic = 200
> nights_domestic = 350
> rlmt_domestic = nights_domestic / guests_domestic
> total_guests = guests_foreign + guests_domestic
> total_nights = nights_foreign + nights_domestic
> rlmt_total = total_nights / total_guests
> pct_foreign = (guests_foreign / total_guests) * 100.0
> print(f'RLMT_Foreign={rlmt_foreign:.2f}, RLMT_Domestic={rlmt_domestic:.2f}, TotalGuests={total_guests}, TotalNights={total_nights}, RLMT_Total={rlmt_total:.2f}, PctForeign={pct_foreign:.1f}%')
> # RLMT_Foreign=3.00, RLMT_Domestic=1.75, TotalGuests=500, TotalNights=1250, RLMT_Total=2.50, PctForeign=60.0%
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Rata-rata Sederhana yang Menyesatkan**: Jangan pernah merata-ratakan langsung $\frac{\text{RLMT}_{\text{asing}} + \text{RLMT}_{\text{domestik}}}{2}$ kecuali jumlah tamu kedua kelompok persis sama.
> 2. **Tertukar Tamu Datang vs Tamu yang Masih Menginap**: Pembagi RLMT adalah jumlah tamu baru yang datang mendaftar (*arrivals / check-in*), bukan jumlah tamu yang tercatat ada di hotel setiap harinya.
> 3. **Satuan**: Pastikan satuan akhir dinyatakan dalam hari atau malam (bukan persen).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　RLMT = Total Malam Tamu dibagi Tamu Datang (Bukan dibagi Kamar, Bukan Persen).

*Keterkaitan Konsep: 13.2.1, 13.2.2*
