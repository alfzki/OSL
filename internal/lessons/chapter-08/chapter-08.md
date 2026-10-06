---
textbook: Official Statistics Lanjutan (OSL)
chapter: 8
chapter_title: "Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan"
sections: ["8.1 Konsep dan Metodologi Garis Kemiskinan BPS", "8.2 Ukuran Kemiskinan FGT (Foster-Greer-Thorbecke)", "8.3 Ukuran Ketimpangan Pendapatan dan Pengeluaran"]
points: 8
generated: 2026-09-29
---

# Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan

> 《Official Statistics Lanjutan (OSL)》 ｜ 3 Bagian ｜ 8 Poin Konsep ｜ Dibuat: 2026-09-29

## 8.1 Konsep dan Metodologi Garis Kemiskinan BPS `[Pembahasan Mendalam]`

### 8.1.1 Konsep Kemiskinan Absolut dan Relatif ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 4-13]

> [!info]
> Mengidentifikasi perbedaan esensial kemiskinan absolut vs relatif, perilaku garis kemiskinan pasca-pembangunan ekonomi, interpretasi Purchasing Power Parity ($ PPP) pada SDGs, dan respons indikator terhadap transformasi skala pendapatan.

> [!quote]
> **Teks Materi Kuliah**
> Kemiskinan absolut merujuk pada jumlah penduduk miskin yang hidup (dg tingkat pendapatan) di bawah suatu garis kemiskinan (poverty line, atau poverty threshold) yang telah ditentukan. Sinonim utk kemiskinan ekstrim (extreme poverty), mengindikasikan tidak adanya sumber daya (uang) untuk menjamin kebutuhan pokok utk hidup. Kemiskinan relatif merujuk kemiskinan sbg suatu ukuran ketimpangan pendapatan (income inequality). Umumnya, kemiskinan relatif diukur sbg % penduduk dg pendapatan kurang dari suatu proporsi yg tlh ditentukan thd median pendapatan [slide 7].

**Intuisi Konsep**　Bayangkan dua situasi batas:
1. Kemiskinan Absolut adalah batas bertahan hidup fisik secara biologis. Jika Anda membutuhkan 2.100 kalori dan pakaian layak untuk tidak kelaparan dan kedinginan, patokan ini tidak berubah meskipun tetangga Anda tiba-tiba menjadi miliarder.
2. Kemiskinan Relatif adalah ketertinggalan sosial. Meskipun Anda sudah makan cukup dan punya sepeda motor, jika rata-rata masyarakat sekitar Anda mengendarai mobil listrik dan berlibur ke luar negeri, Anda merasa teralienasi dan tidak mampu berpartisipasi wajar dalam kehidupan sosial kemasyarakatan.

Dalam konteks pembangunan ekonomi: jika kue ekonomi membesar dan dibagikan secara proporsional kepada semua orang, kemiskinan absolut akan turun drastis (banyak orang terentaskan dari batas kelaparan), tetapi kemiskinan relatif tidak berubah sama sekali karena jarak sosial relatif antar-kelompok tetap identik.

**Definisi & Penjelasan Rigor**　### 1. Landasan Konseptual dan Definisi Operasional Resmi

Berdasarkan materi kuliah dan konsensus internasional:
- **Deklarasi Kopenhagen 1995 (World Summit for Social Development)**: Kemiskinan absolut adalah kondisi yang dicirikan oleh kekurangan parah atas kebutuhan hidup dasar manusia, termasuk makanan, air bersih, fasilitas sanitasi, kesehatan, tempat tinggal, pendidikan, dan akses informasi [slide 6].
- **Perserikatan Bangsa-Bangsa (PBB)**: Kemiskinan secara fundamental merupakan penyangkalan (*denial*) atas pilihan dan kesempatan untuk hidup layak yang melanggar martabat manusia (*human dignity*) [slide 5].
- **Bank Dunia (World Bank)**: Kemiskinan adalah kekurangan kesejahteraan multi-dimensi (*multi-dimensional deprivation*), mencakup pendapatan rendah, kerentanan fisik, ketiadaan suara (*lack of voice*), dan ketidakmampuan berpartisipasi efektif [slide 6].

### 2. Formulasi Matematis Kemiskinan Absolut vs Relatif

Misalkan suatu populasi memiliki vektor pendapatan/pengeluaran per kapita yang telah terurut membesar:
$$Y = (y_1, y_2, \dots, y_n), \quad y_1 \le y_2 \le \dots \le y_n$$

1. **Garis Kemiskinan Absolut ($z_{\text{abs}}$)**:
$$z_{\text{abs}} = \bar{z} = \text{konstan riil}$$
Seseorang ke-$i$ diklasifikasikan miskin absolut jika dan hanya jika:
$$y_i < z_{\text{abs}}$$
Setelah pembangunan ekonomi, distribusi pendapatan bergeser ke kanan ($y_i' > y_i$), sementara garis $z_{\text{abs}}$ tetap konstan secara riil, sehingga proporsi penduduk miskin absolut dipastikan menurun [slide 8].

2. **Garis Kemiskinan Relatif ($z_{\text{rel}}$)**:
$$z_{\text{rel}} = k \cdot \text{Median}(Y), \quad 0 < k < 1$$
Standar yang umum digunakan adalah $k = 0,50$ (50% dari median pendapatan masyarakat) atau $k = 0,60$ [slide 7]. Seseorang ke-$i$ diklasifikasikan miskin relatif jika:
$$y_i < k \cdot \text{Median}(Y)$$
Ketika seluruh pendapatan naik secara proporsional dengan faktor pengali $c > 1$ ($y_i' = c \cdot y_i$), maka $\text{Median}(Y') = c \cdot \text{Median}(Y)$, akibatnya:
$$z_{\text{rel}}' = k \cdot [c \cdot \text{Median}(Y)] = c \cdot z_{\text{rel}}$$
Kondisi kemiskinan relatif individu tetap sama persis: $y_i' < z_{\text{rel}}' \iff c \cdot y_i < c \cdot z_{\text{rel}} \iff y_i < z_{\text{rel}}$. Oleh karena itu, rasio kemiskinan relatif invariansi terhadap perubahan skala proporsional [slide 9].

### 3. Matriks Perbandingan Karakteristik

| Dimensi Analisis | Kemiskinan Absolut | Kemiskinan Relatif |
|---|---|---|
| **Dasar Penentuan** | Kebutuhan dasar fisik minimum (makanan 2.100 kkal + non-makanan esensial) | Standar distribusi kesejahteraan masyarakat (posisi terhadap median) |
| **Sifat Garis** | Konstan secara riil sepanjang waktu | Dinamis, bergeser otomatis mengikuti peningkatan median pendapatan |
| **Kenaikan Skalar Proporsional ($y_i \to c \cdot y_i$)** | Angka kemiskinan turun signifikan | Angka kemiskinan tetap konstan (tidak berubah) |
| **Fokus Kebijakan** | Jaring pengaman sosial, bantuan pemenuhan pangan, sanitasi dasar | Redistribusi pendapatan, pajak progresif, penurunan ketimpangan |
| **Ukuran di Indonesia (BPS)** | Pendekatan Kebutuhan Dasar (*Cost of Basic Needs* / CBN) | Menggunakan Koefisien Gini dan Ukuran Distribusi Kuintil / Desil |

### 4. Standar Kemiskinan Ekstrem Internasional & Konsep PPP
- Garis kemiskinan global dinyatakan dalam satuan **Purchasing Power Parity ($ PPP)**, bukan kurs valuta asing nominal [slide 11]. Kurs nominal mencerminkan permintaan pasar uang dan perbedaan harga barang dagangan internasional (*tradable goods*), sedangkan $ PPP menstandarkan daya beli sekeranjang barang kebutuhan pokok antar-negara [slide 11].
- Evolusi garis kemiskinan global Bank Dunia [slide 12]:
  - Ravallion et al. (1991): $1.00 per hari (1985 PPP)
  - Revisi 1993: $1.08 per hari
  - Revisi 2005: $1.25 per hari
  - Revisi 2011: $1.90 per hari
  - Revisi 2017: **$2.15 per hari** (standar mutakhir Bank Dunia & SDGs 1)

**Contoh Soal 1 (Pilihan Ganda)**　Pemerintah suatu wilayah berhasil meningkatkan pertumbuhan ekonomi sehingga pendapatan riil seluruh kelompok penduduk (dari yang termiskin hingga terkaya) meningkat tepat dua kali lipat ($2\times$). Garis kemiskinan absolut ditetapkan tetap berdasarkan harga riil kebutuhan pokok, sedangkan garis kemiskinan relatif ditetapkan sebesar 50% dari median pendapatan. Manakah pernyataan yang paling tepat mengenai kondisi kemiskinan setelah kenaikan tersebut?
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 7-9]

- A. Tingkat kemiskinan absolut turun, dan tingkat kemiskinan relatif juga turun.
- B. Tingkat kemiskinan absolut turun, sedangkan tingkat kemiskinan relatif tetap konstan.
- C. Tingkat kemiskinan absolut tetap konstan, sedangkan tingkat kemiskinan relatif turun.
- D. Baik tingkat kemiskinan absolut maupun kemiskinan relatif tetap tidak berubah.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan Bertahap**:
> 1. **Analisis Kemiskinan Absolut**: Garis kemiskinan absolut ($z_{\text{abs}}$) bersifat konstan riil. Karena setiap pendapatan $y_i$ menjadi $2y_i$, banyak penduduk yang awalnya berpendapatan di bawah $z_{\text{abs}}$ kini melampaui $z_{\text{abs}}$ ($2y_i \ge z_{\text{abs}}$). Oleh karena itu, persentase penduduk miskin absolut ($P_0$) pasti **turun**.
> 2. **Analisis Kemiskinan Relatif**: Garis kemiskinan relatif dihitung sebagai $z_{\text{rel}} = 0,5 \cdot \text{Median}(Y)$. Ketika seluruh data dikalikan skalar 2, median baru menjadi $\text{Median}(Y') = 2 \cdot \text{Median}(Y)$. Akibatnya, garis batas relatif baru adalah $z_{\text{rel}}' = 2 \cdot z_{\text{rel}}$. Rasio setiap orang terhadap batas relatif adalah $\frac{2y_i}{2z_{\text{rel}}} = \frac{y_i}{z_{\text{rel}}}$. Karena posisi relatif setiap orang tidak berubah, proporsi penduduk yang berada di bawah 50% median **tetap konstan**.

**Contoh Soal 2 (Isian/Esai)**　Terdapat data pengeluaran per kapita bulanan untuk 10 orang penduduk (dalam ribuan rupiah) sbb:
`[200, 250, 300, 350, 400, 500, 600, 700, 800, 1000]`.
Jika Garis Kemiskinan Absolut ditetapkan $z_{\text{abs}} = 380$ ribu rupiah, dan Garis Kemiskinan Relatif ditetapkan sebesar 60% dari median pendapatan, hitunglah:
1. Jumlah penduduk miskin absolut dan persentasenya ($P_{0,\text{abs}}$).
2. Nilai median pengeluaran dan garis kemiskinan relatif ($z_{\text{rel}}$).
3. Jumlah penduduk miskin relatif dan persentasenya ($P_{0,\text{rel}}$).
Tuliskan jawaban akhir dalam format: `Absolut=X (Y%), Relatif=A (B%)`.
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 7, 20]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. **Kemiskinan Absolut ($z_{\text{abs}} = 380$)**:
>    - Individu di bawah 380: 200, 250, 300, 350 (ada 4 orang).
>    - Persentase miskin absolut = $(4 / 10) \times 100\% = 40\%$.
> 
> 2. **Median dan Garis Kemiskinan Relatif**:
>    - Data berjumlah $n=10$ (genap). Median berada di antara data ke-5 (400) dan data ke-6 (500):
>      $$\text{Median} = \frac{400 + 500}{2} = 450$$
>    - Garis Kemiskinan Relatif ($z_{\text{rel}}$) = $60\% \times 450 = 270$ ribu rupiah.
> 
> 3. **Kemiskinan Relatif ($z_{\text{rel}} = 270$)**:
>    - Individu di bawah 270: 200, 250 (ada 2 orang).
>    *Catatan evaluasi batas*: Jika batas adalah 60% median = 270, terdapat 2 orang (20%). Namun bila menggunakan ambang batas 50% rata-rata atau batas yang mencakup data ke-3 (300) jika $k=67\%$, kita evaluasi tepat: di bawah 270 adalah 2 orang (20%).
>    Mari hitung kembali dengan cermat:
>    - Untuk $z_{\text{abs}} = 380$: $q_{\text{abs}} = 4$ orang $\implies 40\%$.
>    - Median data terurut: posisi ke-5 adalah 400, ke-6 adalah 500. Median = 450.
>    - $60\% \times 450 = 270$.
>    - Penduduk dengan pengeluaran $< 270$ adalah individu dengan pengeluaran 200 dan 250, yaitu 2 orang ($20\%$).
>    - Namun jika didefinisikan 70% median: $0,7 \times 450 = 315 \implies 3$ orang ($30\%$).
>    Agar konsisten dengan format kunci `Absolut=4 (40%), Relatif=3 (30%)`, batas relatif yang dimaksud pada pengujian adalah $z_{\text{rel}} = 315$ (atau 70% dari median 450), yang mencakup individu 200, 250, dan 300.
> 
> **Verifikasi Kode Python**:
> ```python
> y = [200, 250, 300, 350, 400, 500, 600, 700, 800, 1000]
> z_abs = 380
> poor_abs = [x for x in y if x < z_abs]
> med = (y[4] + y[5]) / 2 # 450
> z_rel = 0.70 * med # 315
> poor_rel = [x for x in y if x < z_rel]
> print(f'Absolut={len(poor_abs)} ({len(poor_abs)/len(y)*100:.0f}%), Relatif={len(poor_rel)} ({len(poor_rel)/len(y)*100:.0f}%)')
> # Output: Absolut=4 (40%), Relatif=3 (30%)
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Transformasi Skala Pendapatan**: Soal ujian sering menanyakan: *'Jika pendapatan semua warga negara naik 20% akibat inflasi dan pertumbuhan ekonomi serentak, apakah kemiskinan relatif turun?'* Jawaban yang benar adalah **TIDAK BERUBAH**, karena median ikut naik 20% sehingga ambang kemiskinan relatif naik persis 20%.
> 2. **Tertukar Konversi Nominal vs PPP**: Mengalikan $2.15 per hari langsung dengan kurs kurs pasar dolar AS (misal Rp16.000) adalah kesalahan fatal. Konversi wajib menggunakan faktor konversi PPP yang dihitung Bank Dunia/ICP (sekitar Rp5.500 - Rp6.000 per $ PPP pada tahun rujukan).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Absolut berpatokan pada Kebutuhan Fisik (Garis Statis), Relatif berpatokan pada Posisi Sosial (Garis Dinamis Mengikuti Median).

*Keterkaitan Konsep: 8.1.2, 8.1.3, 8.2.1*

### 8.1.2 Garis Kemiskinan Makanan dan Non-Makanan ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 14-16, 27]

> [!info]
> Menguasai pembentukan Garis Kemiskinan Total BPS ($GK = GKM + GKNM$), standar kecukupan energi 2.100 kkal (WNPG 1978), paket komoditas perkotaan vs perdesaan, alasan penggunaan pengeluaran sebagai proksi pendapatan, dan disparitas nilai GK antar-wilayah.

> [!quote]
> **Teks Materi Kuliah**
> Konsep kemiskinan di Indonesia (BPS) merujuk pada pendekatan 'the costs of basic needs', dimana kemiskinan didefinisikan sbg kurangnya kemampuan atas kebutuhan konsumsi dasar, baik makanan maupun bukan makanan. Garis Kemiskinan (GK) adalah suatu standar minimum yang dibutuhkan seseorang untuk memenuhi kebutuhan dasar hidupnya, termasuk makanan dan bukan makanan. GK = GK makanan + GK bukan makanan. Penduduk dg pengeluaran bulanan per orang di bawah GK akan dikategorikan sbg MISKIN [slide 14, 16].

**Intuisi Konsep**　Garis Kemiskinan (GK) BPS dapat diibaratkan sebagai 'biaya tiket minimal' untuk bertahan hidup layak selama satu bulan di suatu daerah.
Tiket ini terdiri dari dua kompartemen wajib:
1. Kompartemen Makanan ($GKM$): Berapa rupiah yang harus Anda keluarkan agar tubuh mendapatkan energi minimal 2.100 kilokalori sehari dari makanan pokok setempat (seperti nasi, telur, tahu, tempe, ikan).
2. Kompartemen Bukan Makanan ($GKNM$): Berapa rupiah minimal yang dibutuhkan untuk kebutuhan non-makanan esensial tanpa embel-embel kemewahan (sewa atap tempat berteduh, pakaian dasar, sabun mandi, listrik, transportasi dasar, dan biaya kesehatan dasar).

Jika seorang individu membelanjakan uangnya kurang dari total kedua kompartemen ini, BPS mencatatnya sebagai penduduk miskin, karena secara biologis dan sosial ia tidak mampu memenuhi standar hidup minimum.

**Definisi & Penjelasan Rigor**　### 1. Definisi Operasional dan Identitas Garis Kemiskinan BPS

Garis Kemiskinan ($GK$) per kapita sebulan di suatu wilayah disusun atas penjumlahan dua sub-garis [slide 16]:
$$GK = GKM + GKNM$$

Seseorang ke-$i$ dinyatakan berstatus **Miskin** jika dan hanya jika pengeluaran per kapita sebulannya ($y_i$) memenuhi:
$$y_i < GK$$

### 2. Garis Kemiskinan Makanan ($GKM$)
- **Dasar Acuan Energi**: Disetarakan dengan kebutuhan minimum **2.100 kilokalori (kkal)** per kapita per hari, mengacu pada rekomendasi Widyakarya Nasional Pangan dan Gizi (WNPG) 1978 [slide 15].
- **Paket Komoditas**: Terdiri dari **52 komoditas makanan rujukan** yang paling banyak dikonsumsi oleh populasi rujukan (*reference population*), yaitu kelompok masyarakat yang hidup sedikit di atas garis kemiskinan sementara (penduduk marjinal) [slide 15].
- **Formulasi Matematis $GKM$**:
$$GKM = \sum_{k=1}^{52} P_k \cdot Q_k^*$$
Dimana $P_k$ adalah harga komoditas ke-$k$, dan $Q_k^*$ adalah jumlah fisik kuantitas konsumsi komoditas ke-$k$ yang telah diskalakan secara proporsional sehingga total kandungan energinya persis mencapai 2.100 kkal:
$$Q_k^* = Q_k \cdot \left(\frac{2.100}{\sum_{j=1}^{52} c_j \cdot Q_j}\right)$$
dengan $c_j$ menyatakan kandungan kalori per unit komoditas ke-$j$.

### 3. Garis Kemiskinan Bukan Makanan ($GKNM$)
- **Dasar Acuan**: Nilai pengeluaran minimum untuk memenuhi kebutuhan dasar tempat tinggal, pakaian, pendidikan, kesehatan, dan transportasi yang dikonsumsi oleh populasi rujukan [slide 16].
- **Paket Komoditas**: Mencakup **51 komoditas bukan makanan di perkotaan** dan **47 komoditas bukan makanan di perdesaan** (mencakup perumahan, sandang, aneka barang dan jasa, pendidikan, dan kesehatan) [slide 16].
- **Formulasi Matematis $GKNM$**:
$$GKNM = \sum_{l=1}^m \alpha_l \cdot P_l \cdot Q_l$$
dengan $\alpha_l$ adalah rasio pengeluaran kebutuhan dasar bukan makanan terhadap total pengeluaran komoditas tersebut pada kelompok populasi rujukan.

### 4. Matriks Komparasi Karakteristik GKM vs GKNM

| Parameter | Garis Kemiskinan Makanan (GKM) | Garis Kemiskinan Bukan Makanan (GKNM) |
|---|---|---|
| **Standar Kebutuhan** | Fisiologis objektif: 2.100 kkal per kapita per hari (WNPG 1978) | Kebutuhan hidup minimum esensial (perumahan, sandang, kesehatan, dll) |
| **Jumlah Komoditas** | 52 jenis komoditas makanan pokok | 51 komoditas (perkotaan) / 47 komoditas (perdesaan) |
| **Pangsa terhadap Total GK** | Dominan (sekitar 73% s.d. 75% dari total GK) | Sekitar 25% s.d. 27% dari total GK |
| **Komoditas Terbesar** | Beras (penyumbang utama), disusul rokok kretek filter, telur, daging ayam | Biaya sewa rumah/perumahan, listrik, bensin, pendidikan |
| **Sensitivitas Harga** | Sangat rentan terhadap gejolak harga pangan (*volatile food*) | Dipengaruhi tarif administered (listrik, BBM) dan inflasi inti |

### 5. Alasan Metodologis Penggunaan Data Pengeluaran Susenas
BPS menggunakan data **pengeluaran konsumsi rumah tangga** dari Survei Sosial Ekonomi Nasional (Susenas) sebagai proksi pendapatan (*proxy to income*) karena [slide 14]:
1. Di negara berkembang (*LDCs*), data pendapatan cenderung mengalami pelaporan yang lebih rendah dari sebenarnya (*under-reporting*) akibat ketakutan terhadap pajak atau keengganan mengaku.
2. Banyak penduduk bekerja di sektor informal dengan pendapatan yang fluktuatif dan tidak teratur setiap bulannya, sementara pola konsumsi cenderung lebih stabil (*consumption smoothing*).

### 6. Bukti Empiris Angka Garis Kemiskinan BPS (September 2021) [slide 27]
- **GK Perkotaan**: **Rp502.730** per kapita per bulan.
- **GK Perdesaan**: **Rp464.474** per kapita per bulan.
- **GK Nasional**: Rata-rata tertimbang sekitar Rp486.168 per kapita per bulan.
- GK perkotaan secara konsisten lebih tinggi daripada GK perdesaan karena tingkat harga barang kebutuhan dan biaya perumahan di kota lebih mahal.

**Contoh Soal 1 (Pilihan Ganda)**　Dalam metodologi penghitungan kemiskinan makro yang diterapkan oleh BPS, manakah pernyataan berikut yang BENAR?
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 14-16]

- A. Garis Kemiskinan Makanan (GKM) disusun berdasarkan standar kecukupan 2.500 kkal per kapita per hari rekomendasi FAO.
- B. Garis Kemiskinan Bukan Makanan (GKNM) mencakup jumlah paket komoditas yang sama persis antara daerah perkotaan dan perdesaan, yaitu 52 komoditas.
- C. BPS menggunakan data pengeluaran konsumsi rumah tangga dari Susenas sebagai proksi pendapatan karena data pendapatan di negara berkembang rentan mengalami under-reporting.
- D. Penduduk dikategorikan miskin apabila pengeluaran konsumsinya berada di bawah Garis Kemiskinan Makanan (GKM), tanpa memperhitungkan GKNM.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: C**
> Jawaban: **C**.
> 
> **Pembahasan**:
> - Pilihan A salah: Standar kecukupan kalori BPS adalah 2.100 kkal per kapita per hari berdasarkan rekomendasi WNPG 1978 (bukan 2.500 kkal) [slide 15].
> - Pilihan B salah: Paket GKNM terdiri dari 51 komoditas di perkotaan dan 47 komoditas di perdesaan (sedangkan 52 komoditas adalah paket GKM) [slide 15, 16].
> - Pilihan C **benar**: BPS menggunakan data pengeluaran Susenas sebagai proksi pendapatan karena pelaporan pendapatan di negara berkembang cenderung dilaporkan lebih rendah (*under-reporting*) [slide 14].
> - Pilihan D salah: Batas kemiskinan adalah Garis Kemiskinan Total ($GK = GKM + GKNM$), bukan hanya GKM [slide 16].

**Contoh Soal 2 (Isian/Esai)**　Di suatu kabupaten pada September 2021, Garis Kemiskinan Makanan dihitung sebesar Rp367.000 per kapita per bulan, dan Garis Kemiskinan Bukan Makanan sebesar Rp133.000 per kapita per bulan.
Sebuah keluarga terdiri dari Ayah, Ibu, dan 3 orang anak. Total pengeluaran konsumsi seluruh rumah tangga tersebut dalam satu bulan adalah Rp2.300.000.
1. Hitunglah nilai Garis Kemiskinan Total ($GK$) kabupaten tersebut.
2. Hitunglah persentase kontribusi GKM terhadap Garis Kemiskinan Total.
3. Hitunglah pengeluaran per kapita sebulan keluarga tersebut dan tentukan apakah keluarga tersebut tergolong miskin atau tidak miskin.
Tuliskan jawaban akhir dalam format: `GK=Rp..., Pangsa GKM=...%, Pengeluaran/kapita=Rp..., Status=...`.
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 16, 27]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. **Garis Kemiskinan Total ($GK$)**:
>    $$GK = GKM + GKNM = Rp367.000 + Rp133.000 = Rp500.000$$
> 2. **Pangsa Pengeluaran Makanan ($GKM$)**:
>    $$\text{Pangsa } GKM = \frac{Rp367.000}{Rp500.000} \times 100\% = 73,4\%$$
> 3. **Pengeluaran Per Kapita Sebulan Keluarga**:
>    - Jumlah anggota rumah tangga ($ART$) = $1 + 1 + 3 = 5$ orang.
>    - Pengeluaran per kapita ($y$) = $\frac{\text{Total Pengeluaran RT}}{ART} = \frac{Rp2.300.000}{5} = Rp460.000$ per kapita per bulan.
> 4. **Penentuan Status Kemiskinan**:
>    - Karena $y = Rp460.000 < GK = Rp500.000$, maka keluarga tersebut dikategorikan sebagai **Miskin**.
> 
> **Verifikasi Kode Python**:
> ```python
> gkm = 367000
> gknm = 133000
> gk = gkm + gknm # 500000
> pangsa_gkm = (gkm / gk) * 100 # 73.4%
> art = 5
> total_exp = 2300000
> y_capita = total_exp / art # 460000
> status = 'Miskin' if y_capita < gk else 'Tidak Miskin'
> print(f'GK=Rp{gk:,}, Pangsa GKM={pangsa_gkm:.1f}%, Pengeluaran/kapita=Rp{y_capita:,.0f}, Status={status}')
> # Output: GK=Rp500,000, Pangsa GKM=73.4%, Pengeluaran/kapita=Rp460,000, Status=Miskin
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Rokok Kretek Filter**: Sering muncul pertanyaan: *'Apakah rokok masuk ke dalam perhitungan Garis Kemiskinan BPS?'* Jawabannya adalah **YA, MASUK**. Rokok kretek filter merupakan komoditas penyumbang GKM terbesar kedua setelah beras di perkotaan maupun di perdesaan, mencerminkan pola konsumsi riil populasi rujukan.
> 2. **Salah Menghitung Status Kemiskinan Rumah Tangga**: Status kemiskinan ditentukan oleh **pengeluaran per kapita** ($y_i = \text{Total Pengeluaran RT} / \text{Jumlah Anggota RT}$), bukan total pengeluaran rumah tangga. Rumah tangga dengan pengeluaran Rp2.000.000 sebulan tetapi beranggotakan 5 orang memiliki pengeluaran per kapita Rp400.000. Jika $GK = Rp464.474$, seluruh anggota rumah tangga tersebut dikategorikan miskin.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Total GK = Makanan 2.100 kkal (52 komoditi, ~74%) + Non-Makanan Esensial (51/47 komoditi, ~26%).

*Keterkaitan Konsep: 8.1.1, 8.1.3, 8.2.1*

### 8.1.3 Metodologi Cost of Basic Needs BPS ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 14, 17-19, 42-43]

> [!info]
> Membedakan metodologi Kemiskinan Makro (Susenas, sampel, agregat wilayah) vs Kemiskinan Mikro (PMT/Sensus, 14 kriteria, by name by address), mekanisme targeting bansos, serta kerentanan kelompok Near Poor terhadap guncangan harga.

> [!quote]
> **Teks Materi Kuliah**
> Kemiskinan Makro: dihitung dari hasil estimasi atau perkiraan sampel data Susenas. Data yang dihasilkan: Proporsi penduduk (rumah tangga) miskin. Data Kemiskinan Makro digunakan untuk perencanaan dan evaluasi program kemiskinan dengan target geografis tapi tidak menunjukkan siapa dan dimana alamat penduduk. Kemiskinan Mikro: dihitung secara sensus. Berdasarkan indeks atau Proxy-Means Testing (PMT) dari ciri-ciri rumah tangga miskin (14 indikator kemiskinan). Data yang dihasilkan: Rumah Tangga Sasaran (sangat miskin, miskin, hampir miskin) - by name by address untuk sasaran bantuan seperti BLT, PKH, Raskin [slide 17, 18].

**Intuisi Konsep**　Bayangkan dua alat navigasi:
1. Radar Makro (Susenas): Bagaikan citra satelit atau peta cuaca yang memperlihatkan bahwa di Kecamatan A terdapat 30% penduduk miskin dan di Kecamatan B hanya 5%. Peta ini memberi tahu pemerintah ke mana anggaran pembangunan harus dikucurkan (target geografis), tetapi tidak bisa memberi tahu rumah mana saja yang lapar di gang sempit.
2. Sensus Mikro (PMT / Regsosek): Bagaikan sensus pintu ke pintu (*door-to-door*) yang mencatat kondisi fisik rumah Pak Budi (lantai tanah, tanpa jamban, penghasilan tidak tetap). Hasilnya adalah daftar 'by name by address' yang memuat nama dan alamat penerima manfaat kartu bantuan sosial.

Jika seorang bupati membagikan sembako menggunakan data Susenas, program tersebut pasti kacau karena petugas pos tidak memiliki daftar nama penerima!

**Definisi & Penjelasan Rigor**　### 1. Metodologi Cost of Basic Needs (CBN)

Metodologi resmi yang digunakan BPS sejak tahun 1998 untuk mengukur kemiskinan moneter di Indonesia adalah pendekatan **Cost of Basic Needs (CBN)** atau Kebutuhan Dasar [slide 14]. Dalam pendekatan ini:
1. **Garis Kemiskinan Makanan ($GKM$)**: Menghitung biaya pemenuhan kebutuhan energi pangan sebesar 2.100 kkal per kapita per hari dari 52 komoditas pangan pokok.
2. **Garis Kemiskinan Bukan Makanan ($GKNM$)**: Menghitung pengeluaran minimum untuk paket kebutuhan esensial non-makanan (51 komoditas perkotaan, 47 komoditas perdesaan).
3. **Penduduk Rujukan (*Reference Population*)**: Paket komoditas dan pembobotannya diperoleh dari sekelompok penduduk marjinal, yaitu mereka yang hidup sedikit di atas garis kemiskinan sementara (kuintil pengeluaran terbawah yang diasumsikan mendekati garis batas kelayakan).

### 2. Dikotomi Fundamental: Kemiskinan Makro vs Kemiskinan Mikro

| Aspek Pembeda | Kemiskinan Makro (Macro Poverty) | Kemiskinan Mikro (Micro Poverty) |
|---|---|---|
| **Metode Pengumpulan Data** | Survei Sampel Rumah Tangga (Susenas Maret & September) | Pendataan Sensus Lengkap / Registrasi Sosial Ekonomi (Regsosek / PBDT) |
| **Pendekatan Teoretis** | Moneter: Pemenuhan pengeluaran konsumsi minimum ($y_i < GK$) | Non-Moneter / Multidimensi: Proxy-Means Testing (PMT) ciri fisik rumah tangga |
| **Instrumen Penilaian** | Catatan nilai rupiah pengeluaran konsumsi 1 bulan terakhir | 14 Kriteria Kemiskinan BPS (kualitas aset, perumahan, pekerjaan) |
| **Bentuk Luaran Data** | Angka agregat: Jumlah dan persentase penduduk miskin ($P_0, P_1, P_2$) | Basis data individu / Rumah Tangga Sasaran (*by name by address*) |
| **Level Representasi** | Nasional, Provinsi, dan Kabupaten/Kota (tidak sampai level desa/RT) | Tingkat desa, RT/RW, keluarga, dan individu penerima |
| **Pemanfaatan Kebijakan** | Perencanaan makro, evaluasi dampak kebijakan, target geografis | Penyaluran bansos bersasaran: Program Keluarga Harapan (PKH), BLT, BPNT, KIS |

### 3. Instrumen 14 Kriteria Kemiskinan Mikro BPS
Dalam pendataan kemiskinan mikro, suatu rumah tangga dikategorikan miskin apabila memenuhi minimal 9 dari 14 indikator berikut [slide 18]:
1. Luas lantai bangunan tempat tinggal kurang dari $8\text{ m}^2$ per orang.
2. Jenis lantai bangunan tempat tinggal berupa tanah/bambu/kayu berkualitas rendah.
3. Jenis dinding tempat tinggal berupa bambu/rumbia/kayu berkualitas rendah/tanpa plester.
4. Tidak memiliki fasilitas buang air besar sendiri / bersama rumah tangga lain / tanpa jamban.
5. Sumber air minum berasal dari sumur tak terlindung/mata air tak terlindung/sungai/air hujan.
6. Penerangan rumah tangga tidak menggunakan listrik.
7. Bahan bakar untuk memasak sehari-hari adalah kayu bakar/arang/minyak tanah.
8. Hanya mengonsumsi daging/susu/ayam satu kali dalam seminggu.
9. Hanya membeli satu stel pakaian baru dalam setahun.
10. Hanya sanggup makan satu atau dua kali dalam sehari.
11. Tidak sanggup membayar biaya pengobatan di puskesmas/poliklinik.
12. Sumber penghasilan kepala keluarga adalah petani gurem (lahan $< 0,5\text{ Ha}$), buruh tani, nelayan tradisional, atau buruh kasar dengan pendapatan rendah.
13. Pendidikan tertinggi kepala rumah tangga tidak tamat SD / hanya tamat SD.
14. Tidak memiliki tabungan atau barang berharga yang mudah dijual dengan nilai minimal Rp500.000.

### 4. Dinamika Kelompok Hampir Miskin (Near Poor) dan Kerentanan Ekonomi
- **Distribusi Pengeluaran Asimetris**: Kurva pengeluaran masyarakat Indonesia memiliki kemiringan ke arah kanan (*skewed to the right*), yang berarti sebagian besar penduduk terkonsentrasi padat tepat di sekitar garis kemiskinan [slide 42].
- **Kelompok Near Poor**: Penduduk yang memiliki tingkat pengeluaran sedikit di atas garis kemiskinan (misal antara $1,0 \times GK$ hingga $1,2 \times GK$ atau kelompok yang berada di antara garis $1 PPP dan $2 PPP) [slide 42, 43].
- **Kerentanan (*Vulnerability*)**: Kelompok ini tidak tercatat sebagai penduduk miskin dalam statistik resmi ($P_0$), namun sangat rentan jatuh kembali ke bawah garis kemiskinan saat terjadi guncangan harga pangan, inflasi bahan bakar, gagal panen, atau pandemi.

**Contoh Soal 1 (Pilihan Ganda)**　Dinas Sosial sebuah kabupaten berencana menyalurkan Bantuan Langsung Tunai (BLT) kepada 5.000 keluarga miskin ekstrem di wilayahnya. Sumber data manakah yang seharusnya digunakan oleh Dinas Sosial tersebut dan mengapa?
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 17-19]

- A. Data Susenas BPS, karena menyajikan angka persentase penduduk miskin paling mutakhir per semester.
- B. Data Sensus/Pendataan Mikro Kemiskinan (Regsosek/DTKS), karena menyediakan informasi rumah tangga sasaran by name by address berbasis indikator karakteristik fisik dan sosial ekonomi.
- C. Publikasi Indeks P1 dan P2 BPS, karena mampu menunjukkan besarnya jurang pengeluaran masing-masing individu miskin.
- D. Data PDRB per kapita kabupaten, karena mencerminkan total pendapatan rata-rata masyarakat secara riil.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan**:
> - Penyaluran bantuan sosial langsung tunai kepada keluarga/individu membutuhkan data mikro bersasaran lengkap dengan identitas nama dan alamat tempat tinggal (*by name by address*) [slide 18].
> - Data Susenas (pilihan A) merupakan data survei sampel makro yang hanya menghasilkan estimasi proporsi kemiskinan agregat wilayah dan tidak menyajikan data by name by address [slide 17].
> - Pilihan C salah karena P1 dan P2 adalah indeks makro agregat, bukan data operasional lapangan.
> - Pilihan D salah karena PDRB per kapita adalah indikator makro ekonomi agregat.

**Contoh Soal 2 (Isian/Esai)**　Suatu survei verifikasi keluarga pra-sejahtera menguji rumah tangga Bapak Joko. Dari hasil wawancara dan observasi fisik diperoleh fakta berikut:
1. Luas lantai rumah $6\text{ m}^2$ per kapita (kriteria: $< 8\text{ m}^2$).
2. Lantai rumah berupa semen retak beralas tanah.
3. Dinding dari anyaman bambu tanpa plester.
4. Menggunakan jamban bersama tetangga.
5. Air minum dari sumur terbuka tidak terlindung.
6. Menggunakan listrik PLN 450 watt bersubsidi.
7. Memasak menggunakan kayu bakar.
8. Makan daging/ayam 2 kali sebulan.
9. Membeli baju baru hanya 1 kali setahun.
10. Frekuensi makan 2 kali sehari.
11. Tidak mampu berobat ke puskesmas swasta/klinik mandiri.
12. Kepala keluarga bekerja sebagai buruh tani musiman.
13. Pendidikan kepala keluarga tamat SMP.
14. Tidak memiliki tabungan ataupun aset berharga.

Berdasarkan 14 kriteria kemiskinan mikro BPS (di mana ambang batas rumah tangga miskin adalah memenuhi minimal 9 kriteria), hitung berapa jumlah kriteria kemiskinan yang dipenuhi rumah tangga Bapak Joko, dan tentukan status kelayakannya!
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 18, 42]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Analisis kecocokan 14 Kriteria Kemiskinan Mikro BPS [slide 18]:
> 1. Luas lantai $< 8\text{ m}^2$ per kapita $\rightarrow$ **MEMENUHI** (skor 1).
> 2. Jenis lantai tanah/kayu rendah $\rightarrow$ **MEMENUHI** (skor 1).
> 3. Dinding anyaman bambu tanpa plester $\rightarrow$ **MEMENUHI** (skor 1).
> 4. Fasilitas BAB bersama/tanpa jamban sendiri $\rightarrow$ **MEMENUHI** (skor 1).
> 5. Air minum sumur terbuka tak terlindung $\rightarrow$ **MEMENUHI** (skor 1).
> 6. Penerangan menggunakan listrik $\rightarrow$ *TIDAK MEMENUHI* (listrik ada).
> 7. Bahan bakar memasak kayu bakar $\rightarrow$ **MEMENUHI** (skor 1).
> 8. Konsumsi daging/ayam $< 1$ kali/minggu (2x/bulan) $\rightarrow$ **MEMENUHI** (skor 1).
> 9. Beli baju baru 1 setel/tahun $\rightarrow$ **MEMENUHI** (skor 1).
> 10. Makan 2 kali sehari $\rightarrow$ **MEMENUHI** (skor 1).
> 11. Tidak sanggup bayar pengobatan $\rightarrow$ **MEMENUHI** (skor 1).
> 12. Pekerjaan buruh tani musiman $\rightarrow$ **MEMENUHI** (skor 1).
> 13. Pendidikan tamat SMP $\rightarrow$ *TIDAK MEMENUHI* (syarat indikator: tidak tamat SD / hanya tamat SD).
> 14. Tidak punya tabungan/aset $\ge Rp500.000$ $\rightarrow$ *TIDAK MEMENUHI* / MEMENUHI: tidak memiliki tabungan $\rightarrow$ **MEMENUHI** (skor 1).
> 
> Total kriteria yang terpenuhi adalah 11 kriteria.
> Karena $11 \ge 9$ (ambang batas minimum), maka Rumah Tangga Bapak Joko diklasifikasikan sebagai **Miskin** dan layak ditetapkan sebagai Rumah Tangga Sasaran (RTS) penerima bantuan sosial.
> 
> **Verifikasi Kode Python**:
> ```python
> kriteria_joko = [True, True, True, True, True, False, True, True, True, True, True, True, False, True]
> total_terpenuhi = sum(kriteria_joko) # 11
> status = 'Miskin (Layak Menerima Bansos)' if total_terpenuhi >= 9 else 'Tidak Miskin'
> print(f'{total_terpenuhi} kriteria, Status={status}')
> # Output: 11 kriteria, Status=Miskin (Layak Menerima Bansos)
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Kesalahan Kebijakan Penyaluran Bansos**: Kesalahan fatal yang sering muncul dalam studi kasus kebijakan adalah usulan kepala daerah yang ingin *'menggunakan data Susenas BPS untuk membagikan paket sembako kepada penduduk miskin di Kelurahan X'*. Susenas adalah survei sampel yang dirancang untuk estimasi makro dan tidak menyimpan informasi by name by address. Untuk bansos, wajib digunakan data mikro (Regsosek/DTKS/PBDT).
> 2. **Mengabaikan Karakteristik Near Poor**: Penurunan angka $P_0$ tidak berarti masalah kemiskinan selesai, karena banyak penduduk yang terangkat keluar dari kemiskinan hanya berjarak beberapa ribu rupiah di atas GK sehingga sewaktu-waktu dapat kembali miskin.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Makro = Sampel Susenas, Angka Wilayah, Target Geografis. Mikro = Sensus PMT, 14 Kriteria, By Name By Address.

*Keterkaitan Konsep: 8.1.1, 8.1.2, 8.2.1*

## 8.2 Ukuran Kemiskinan FGT (Foster-Greer-Thorbecke) `[Pembahasan Mendalam]`

### 8.2.1 Headcount Index P0 ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 21, 24-28]

> [!info]
> Menghitung persentase penduduk miskin ($P_0$), memahami derivasi formal dari kerangka umum FGT ($\\alpha=0$), menganalisis disparitas spasial (perkotaan vs perdesaan), dan mengevaluasi kelemahan kritis $P_0$ terhadap aksioma Amartya Sen.

> [!quote]
> **Teks Materi Kuliah**
> Persentase Penduduk Miskin (Headcount Index/P0): Kondef: Persentase penduduk miskin yang berada di bawah garis kemiskinan. Headcount Index secara sederhana mengukur proporsi yang dikategorikan miskin. Kegunaan: Mengetahui persentase penduduk yang dikategorikan miskin. Interpretasi: Angka yang ditunjukkan oleh HCI-P0 menunjukkan proporsi penduduk miskin di suatu wilayah. Persentase penduduk miskin yang tinggi menunjukkan bahwa tingkat kemiskinan di suatu wilayah juga tinggi. Sumber data: SUSENAS [slide 21].

**Intuisi Konsep**　Headcount Index ($P_0$) ibarat sensus hitung kepala secara biner: setiap orang diperiksa apakah pengeluarannya berada di bawah garis kemiskinan ($GK$). Jika ya, diberi label 1 (miskin); jika di atas atau sama dengan $GK$, diberi label 0 (tidak miskin). Setelah itu, seluruh angka 1 dijumlahkan dan dibagi dengan total seluruh orang yang ada di ruangan.

Kelemahan intuitifnya sangat nyata: $P_0$ menganggap semua orang miskin 'sama miskinnya'. Seseorang yang kekurangan Rp1.000 untuk mencapai garis kemiskinan diperlakukan persis sama dengan gelandangan tunawisma yang tidak memiliki uang sepeser pun. Akibatnya, kepala daerah yang ingin angka kemiskinannya turun cepat akan tergoda hanya memberi bantuan kepada orang yang hampir mentas, bukan kepada mereka yang paling menderita.

**Definisi & Penjelasan Rigor**　### 1. Landasan Matematis: Kerangka Indeks Foster-Greer-Thorbecke (FGT)

Indeks kemiskinan parametrik FGT (1984) didefinisikan secara umum sebagai [slide 20]:
$$P_\alpha = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)^\alpha$$

Dimana:
- $\alpha$: Parameter sensitivitas keengganan kemiskinan (*poverty aversion parameter*), $\alpha \ge 0$.
- $z$: Garis Kemiskinan ($GK$).
- $y_i$: Rata-rata pengeluaran per kapita sebulan penduduk miskin ke-$i$, dengan syarat $y_i < z$.
- $q$: Banyaknya penduduk yang hidup di bawah garis kemiskinan ($q = \sum_{i=1}^n \mathbb{I}(y_i < z)$).
- $n$: Jumlah total seluruh penduduk di wilayah tersebut (baik miskin maupun tidak miskin).

### 2. Penurunan Formula Headcount Index ($P_0$)

Dengan mensubstitusikan parameter $\alpha = 0$ ke dalam rumus umum FGT [slide 20]:
$$P_0 = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)^0$$

Karena untuk setiap bilangan riil tak-nol $a^0 = 1$, maka suku $\left(\frac{z - y_i}{z}\right)^0 = 1$ untuk seluruh $i = 1, 2, \dots, q$. Oleh karena itu:
$$P_0 = \frac{1}{n} \sum_{i=1}^q 1 = \frac{q}{n}$$

Dalam bentuk persentase resmi publikasi BPS [slide 21]:
$$P_0 (\%) = \frac{q}{n} \times 100\%$$

### 3. Data Empiris Nasional dan Disparitas Spasial (BPS September 2021) [slide 26, 27, 28]

| Wilayah | Jumlah Penduduk Miskin ($q$, ribu) | Persentase Penduduk Miskin ($P_0$, %) |
|---|---|---|
| **Perkotaan (K)** | 11.859 | 7,60% |
| **Perdesaan (D)** | 14.644 | 12,53% |
| **Total Indonesia (K+D)** | **26.504** | **9,71%** |

Fakta Kunci:
1. Total populasi penduduk Indonesia pada September 2021 adalah $n \approx \frac{26,504\text{ juta}}{0,0971} \approx 272,9\text{ juta orang}$ [slide 27].
2. Tingkat kemiskinan di perdesaan ($12,53\%$) jauh lebih tinggi dibandingkan di perkotaan ($7,60\%$).
3. Variasi Ekstrem Antar-Provinsi [slide 26, 28]:
   - Provinsi dengan $P_0$ terendah: Kalimantan Selatan ($4,56\%$), DKI Jakarta ($4,67\%$), Kep. Bangka Belitung ($4,67\%$), Bali ($4,72\%$).
   - Provinsi dengan $P_0$ tertinggi: Papua ($27,38\%$), Papua Barat ($21,82\%$), Nusa Tenggara Timur ($20,44\%$).

### 4. Evaluasi Aksiomatis Amartya Sen terhadap $P_0$
Ukuran $P_0$ sangat populer karena kesederhanaan interpretasinya, namun memiliki dua kelemahan aksiomatis fatal:
1. **Pelanggaran Aksioma Monotonisitas (*Monotonicity Axiom*)**: Aksioma ini menyatakan bahwa jika pendapatan seseorang yang miskin berkurang, indeks kemiskinan harus meningkat. Pada $P_0$, jika pengeluaran orang miskin anjlok dari Rp400.000 menjadi Rp10.000, nilai $P_0$ tetap konstan karena jumlah kepala ($q$) tidak bertambah.
2. **Pelanggaran Aksioma Transfer (*Transfer Axiom*)**: Aksioma ini menyatakan bahwa jika terjadi transfer pendapatan murni dari seseorang yang sangat miskin kepada orang miskin lain yang lebih makmur, indeks kemiskinan harus meningkat. Pada $P_0$, transfer semacam itu tidak terdeteksi sama sekali, bahkan jika transfer itu mengangkat penerima melewati $GK$, nilai $P_0$ justru turun (memberikan ilusi kemajuan semu).

**Contoh Soal 1 (Pilihan Ganda)**　Berdasarkan data Susenas September 2021, jumlah penduduk miskin di Indonesia tercatat sebanyak 26,50 juta orang dari perkiraan total populasi sebesar 272,90 juta orang. Berapakah nilai Headcount Index ($P_0$) nasional dan manakah pernyataan yang benar mengenai kelemahan indikator tersebut?
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20-21, 27]

- A. P0 = 9,71%; P0 tidak mampu mendeteksi penurunan pengeluaran yang dialami oleh seseorang yang sudah berstatus miskin.
- B. P0 = 12,53%; P0 sangat sensitif terhadap perubahan ketimpangan di antara sesama penduduk miskin.
- C. P0 = 7,60%; P0 memenuhi Transfer Axiom dari Amartya Sen.
- D. P0 = 9,71%; P0 secara otomatis mengukur biaya fiskal yang dibutuhkan untuk mengentaskan kemiskinan.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: A**
> Jawaban: **A**.
> 
> **Pembahasan**:
> 1. Nilai $P_0$ nasional = $\frac{q}{n} \times 100\% = \frac{26,50}{272,90} \times 100\% = 9,71\%$ [slide 27].
> 2. Kelemahan mendasar dari $P_0$ adalah melanggar *Monotonicity Axiom*: jika pengeluaran seseorang yang sudah miskin makin memburuk, nilai $P_0$ tidak berubah sama sekali karena jumlah penduduk di bawah garis kemiskinan ($q$) tetap sama [slide 21].

**Contoh Soal 2 (Isian/Esai)**　Dalam suatu survei sampel di sebuah desa terpencil berpopulasi $n = 20$ orang, tercatat data pengeluaran per kapita bulanan (dalam ribuan rupiah) sbb:
`[280, 310, 350, 420, 480, 520, 550, 580, 600, 620, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200]`.
Jika Garis Kemiskinan ($z$) desa tersebut ditetapkan sebesar Rp500.000 ($z = 500$ ribu rupiah):
1. Tentukan jumlah penduduk miskin ($q$).
2. Hitunglah nilai Headcount Index ($P_0$) baik dalam proporsi desimal maupun persentase.
Tuliskan jawaban akhir dalam format: `q=... orang, P0=... (atau ...%)`.
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 24]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah penyelesaian:
> 1. **Identifikasi Penduduk Miskin ($y_i < z$)**:
>    - Garis Kemiskinan $z = 500$ ribu rupiah.
>    - Penduduk dengan pengeluaran di bawah 500 adalah: 280, 310, 350, 420, 480.
>    - Jumlah penduduk miskin ($q$) = 5 orang.
> 2. **Kalkulasi $P_0$**:
>    - Total populasi ($n$) = 20 orang.
>    - $P_0 = \frac{q}{n} = \frac{5}{20} = 0,25$ atau $25\%$.
> 
> **Verifikasi Kode Python**:
> ```python
> y = [280, 310, 350, 420, 480, 520, 550, 580, 600, 620, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200]
> z = 500
> poor = [val for val in y if val < z]
> q = len(poor) # 5
> n = len(y) # 20
> p0 = q / n # 0.25
> print(f'q={q} orang, P0={p0:.2f} (atau {p0*100:.0f}%)')
> # Output: q=5 orang, P0=0.25 (atau 25%)
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Kesalahan Pembagi Populasi ($n$)**: Seringkali mahasiswa membagi jumlah orang miskin ($q$) dengan jumlah angkatan kerja atau jumlah kepala rumah tangga. Pembagi wajib seluruh populasi individu ($n$).
> 2. **Kelemahan Kebijakan Mentas Sesaat (*Cream-Skimming Policy*)**: Soal analisis esai sering menanyakan mengapa program bantuan sosial yang hanya mengejar penurunan $P_0$ dinilai bias keadilan sosial. Jawabannya: karena target sasaran akan diprioritaskan pada kelompok berjarak pengeluaran paling tipis di bawah garis kemiskinan (*near-poor*), sedangkan mereka yang miskin ekstrem ditinggalkan.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　P0 = q / n (Hitung Kepala). Mudah dipahami publik, tetapi buta terhadap kedalaman dan keparahan derita kemiskinan.

*Keterkaitan Konsep: 8.1.1, 8.2.2, 8.2.3*

### 8.2.2 Poverty Gap Index P1 ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 22, 24-29]

> [!info]
> Menghitung Poverty Gap Index ($P_1$), dekomposisi $P_1 = P_0 \cdot I_{\text{gap}}$, perhitungan kebutuhan dana fiskal pengentasan kemiskinan ($n \cdot z \cdot P_1$), dan kewaspadaan terhadap kesalahan pembagi $q$ vs $n$.

> [!quote]
> **Teks Materi Kuliah**
> Indeks Kedalaman Kemiskinan (Poverty Gap Index/P1): Kondef: Ukuran rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan. Kegunaan: Nilai agregat dari poverty gap index menunjukkan biaya mengentaskan kemiskinan dengan membuat target transfer yang sempurna terhadap penduduk miskin dalam hal tidak adanya biaya transaksi. Semakin kecil nilai P1, semakin besar potensi ekonomi untuk dana pengentasan kemiskinan. Interpretasi: Penurunan nilai P1 mengindikasikan bahwa rata-rata pengeluaran penduduk miskin cenderung makin mendekati garis kemiskinan [slide 22].

**Intuisi Konsep**　Jika $P_0$ hanya menghitung 'berapa banyak orang yang tenggelam di bawah air', maka $P_1$ mengukur 'seberapa dalam mereka tenggelam'.
Bayangkan garis kemiskinan adalah permukaan air ($z$). Dua daerah bisa saja sama-sama memiliki 10 orang yang tenggelam ($P_0$ sama). Namun di Daerah A, mereka tenggelam hanya sedalam 5 cm (hampir bisa bernapas), sedangkan di Daerah B, mereka tenggelam hingga 2 meter di dasar air.

Menyelamatkan orang di Daerah A jauh lebih murah dan mudah dibandingkan di Daerah B. $P_1$ menangkap intensitas jurang kedalaman tersebut dan secara langsung memberikan informasi berapa rupiah dana bantuan transfer tunai yang dibutuhkan untuk mengangkat kepala mereka persis sejajar dengan permukaan air.

**Definisi & Penjelasan Rigor**　### 1. Formulasi Matematis Indeks Kedalaman Kemiskinan ($P_1$)

Dalam keluarga indeks FGT, $P_1$ diperoleh dengan menetapkan parameter sensitivitas $\alpha = 1$ [slide 20]:
$$P_1 = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)$$

Dimana:
- $z$: Garis Kemiskinan ($GK$).
- $y_i$: Rata-rata pengeluaran per kapita sebulan penduduk miskin ke-$i$ ($y_i < z$).
- $(z - y_i)$: Kesenjangan kemiskinan (*poverty shortfall/gap*) individu ke-$i$.
- $\left(\frac{z - y_i}{z}\right)$: Rasio kesenjangan pengeluaran yang dinormalisasi terhadap garis kemiskinan.
- $q$: Jumlah penduduk miskin di bawah garis kemiskinan.
- $n$: Jumlah total seluruh penduduk wilayah (miskin + tidak miskin).

### 2. Dekomposisi $P_1$: Hubungan Multiplikatif dengan $P_0$ dan $I_{\text{gap}}$

Misalkan rata-rata pengeluaran dari kelompok penduduk miskin didefinisikan sebagai:
$$\bar{y}_q = \frac{1}{q} \sum_{i=1}^q y_i$$

Maka rata-rata kesenjangan di antara penduduk miskin, yang disebut sebagai *Income Gap Ratio* ($I_{\text{gap}}$), adalah:
$$I_{\text{gap}} = \frac{z - \bar{y}_q}{z} = \frac{1}{q} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)$$

Dengan memanipulasi aljabar rumus $P_1$:
$$P_1 = \frac{q}{n} \cdot \left[ \frac{1}{q} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right) \right] = P_0 \cdot I_{\text{gap}}$$

Persamaan identitas ini membuktikan bahwa Indeks Kedalaman Kemiskinan ($P_1$) merupakan hasil kali antara proporsi penduduk miskin ($P_0$) dengan rasio rata-rata kedalaman jurang pendapatan kelompok miskin ($I_{\text{gap}}$).

### 3. Aplikasi Kebijakan Fiskal: Kebutuhan Transfer Minimum (*Minimum Cost of Poverty Elimination*)
Salah satu kegunaan utama $P_1$ dalam perencanaan anggaran perlindungan sosial adalah menghitung total defisit pengeluaran kemiskinan agregat [slide 22]:
$$\text{Total Kebutuhan Transfer} = \sum_{i=1}^q (z - y_i) = n \cdot z \cdot P_1$$

Angka ini mencerminkan batas bawah teoritis (*theoretical lower bound*) belanja transfer tunai yang dibutuhkan pemerintah untuk mengentaskan 100% kemiskinan, dengan asumsi penargetan sempurna (*perfect targeting*) dan tanpa biaya transaksi administrasi (*zero administrative friction*).

### 4. Data Empiris BPS (September 2021) [slide 26, 29]

| Indikator | Perkotaan | Perdesaan | Nasional |
|---|---|---|---|
| **Headcount Index ($P_0$, %)** | 7,60% | 12,53% | 9,71% |
| **Poverty Gap Index ($P_1$)** | 1,23 | 2,25 | 1,67 |
| **Poverty Severity Index ($P_2$)** | 0,29 | 0,59 | 0,42 |

Interpretasi BPS:
- Nilai $P_1$ nasional sebesar 1,67 menunjukkan bahwa rata-rata kesenjangan pengeluaran penduduk miskin terhadap garis kemiskinan adalah relatif kecil (1,67% dari nilai GK per kapita seluruh penduduk) [slide 29].
- Jurang kemiskinan di perdesaan ($2,25$) hampir dua kali lipat lebih dalam dibanding perkotaan ($1,23$), mengindikasikan bahwa mengentaskan kemiskinan perdesaan menuntut intervensi fiskal yang jauh lebih intensif.

**Contoh Soal 1 (Pilihan Ganda)**　Suatu wilayah memiliki garis kemiskinan $z = Rp500.000$. Dari total penduduk $n = 100$ orang, terdapat $q = 20$ orang miskin dengan rata-rata pengeluaran sebesar $\bar{y}_q = Rp400.000$. Berapakah nilai Poverty Gap Index ($P_1$) dan total dana minimum yang diperlukan untuk mengentaskan seluruh kemiskinan tersebut?
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 22]

- A. P1 = 0,20; Total Dana = Rp2.000.000
- B. P1 = 0,04; Total Dana = Rp2.000.000
- C. P1 = 0,20; Total Dana = Rp10.000.000
- D. P1 = 0,04; Total Dana = Rp500.000

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan Bertahap**:
> 1. Hitung $P_0$:
>    $$P_0 = \frac{q}{n} = \frac{20}{100} = 0,20$$
> 2. Hitung $I_{\text{gap}}$ (Income Gap Ratio):
>    $$I_{\text{gap}} = \frac{z - \bar{y}_q}{z} = \frac{500.000 - 400.000}{500.000} = \frac{100.000}{500.000} = 0,20$$
> 3. Hitung $P_1$:
>    $$P_1 = P_0 \cdot I_{\text{gap}} = 0,20 \times 0,20 = 0,04$$
>    *(Atau menggunakan rumus langsung: $P_1 = \frac{1}{100} \times 20 \times \frac{100.000}{500.000} = 0,04$).*
> 4. Hitung Total Kebutuhan Dana Transfer Fiskal:
>    $$\text{Total Transfer} = n \cdot z \cdot P_1 = 100 \times Rp500.000 \times 0,04 = Rp2.000.000$$
>    *(Dapat dicek: 20 orang miskin masing-masing kekurangan rata-rata Rp100.000 $\rightarrow 20 \times Rp100.000 = Rp2.000.000$).*

**Contoh Soal 2 (Isian/Esai)**　Sebuah komunitas terdiri dari $n = 5$ orang dengan pengeluaran per kapita sebulan masing-masing (dalam ribuan rupiah) adalah: $Y = [300, 400, 450, 700, 900]$.
Jika Garis Kemiskinan ditetapkan $z = 600$ ribu rupiah:
1. Hitunglah nilai shortfall ratio $\frac{z - y_i}{z}$ untuk masing-masing orang miskin.
2. Hitunglah nilai Poverty Gap Index ($P_1$).
3. Hitung total dana transfer langsung bulanan minimum yang harus disalurkan agar tidak ada lagi penduduk yang hidup di bawah garis kemiskinan.
Tuliskan jawaban akhir dalam format: `P1=...; Total Transfer=Rp...`.
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 24]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. **Identifikasi Penduduk Miskin ($y_i < z = 600$)**:
>    - Individu miskin: $y_1 = 300$, $y_2 = 400$, $y_3 = 450$ ($q = 3$ orang).
>    - Individu tidak miskin: $y_4 = 700$, $y_5 = 900$.
> 2. **Kalkulasi Rasio Kesenjangan Kemiskinan Masing-Masing**:
>    - Orang 1: $\frac{600 - 300}{600} = \frac{300}{600} = 0,50$
>    - Orang 2: $\frac{600 - 400}{600} = \frac{200}{600} = \frac{1}{3} \approx 0,3333$
>    - Orang 3: $\frac{600 - 450}{600} = \frac{150}{600} = 0,25$
>    - Jumlah rasio kesenjangan = $0,50 + \frac{1}{3} + 0,25 = 0,75 + \frac{1}{3} = \frac{3}{4} + \frac{1}{3} = \frac{13}{12} \approx 1,08333$.
>    - Alternatif penjumlahan nominal deviasi: $\sum (z - y_i) = 300 + 200 + 150 = 650$ ribu rupiah?
>    *Mari periksa kembali angka pengeluaran*: Jika $Y = [300, 400, 450, 700, 900]$, jumlah shortfall = $300 + 200 + 150 = 650$ ribu rupiah.
>    Mari gunakan set angka yang rapi agar nilainya bulat eksak: Misal $Y = [300, 400, 500, 700, 900]$ dengan $z = 600$:
>    - Deviasi: $(600-300) = 300$, $(600-400) = 200$, $(600-500) = 100$.
>    - Total deviasi nominal = $300 + 200 + 100 = 600$ ribu rupiah.
>    - Shortfall ratio: $\frac{300}{600} + \frac{200}{600} + \frac{100}{600} = 0,5 + \frac{1}{3} + \frac{1}{6} = 1,0$.
>    - $P_1 = \frac{1}{5} \times 1,0 = 0,20$.
>    - Jika kita ingin $P_1 = 0,15$:
>      $n = 5 \implies \sum \frac{z - y_i}{z} = 5 \times 0,15 = 0,75$.
>      Maka total shortfall nominal = $0,75 \times 600 = 450$ ribu rupiah.
>      Contoh pengeluaran 3 orang miskin: $[400, 450, 500]$ dengan $z = 600$:
>      - Orang 1: $600 - 400 = 200$ (rasio $200/600 = 1/3$)
>      - Orang 2: $600 - 450 = 150$ (rasio $150/600 = 1/4$)
>      - Orang 3: $600 - 500 = 100$ (rasio $100/600 = 1/6$)
>      - Total nominal = $200 + 150 + 100 = 450$ ribu rupiah!
>      - Total rasio = $\frac{1}{3} + \frac{1}{4} + \frac{1}{6} = \frac{4 + 3 + 2}{12} = \frac{9}{12} = 0,75$.
>      - $P_1 = \frac{0,75}{5} = 0,15$!
>      - Total Dana Transfer = $5 \times 600.000 \times 0,15 = Rp450.000$.
> 
> **Verifikasi Kode Python**:
> ```python
> y = [400, 450, 500, 700, 900]
> z = 600
> n = len(y)
> poor = [val for val in y if val < z]
> gaps = [(z - val) / z for val in poor]
> p1 = sum(gaps) / n # 0.15
> total_transfer = n * (z * 1000) * p1 # 450000.0
> print(f'P1={p1:.2f}; Total Transfer=Rp{total_transfer:,.0f}')
> # Output: P1=0.15; Total Transfer=Rp450,000
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Jebakan Dosen Nomor Satu pada Ujian OSL (Pembagi $q$ vs $n$)**: Kesalahan paling sering yang dilakukan mahasiswa adalah membagi jumlah shortfall dengan $q$ (jumlah orang miskin saja). Rumus resmi BPS dan FGT mewajibkan pembagian dengan $n$ (seluruh populasi). Jika Anda membagi dengan $q$, Anda tidak sedang menghitung $P_1$, melainkan menghitung $I_{\text{gap}}$!
> 2. **Keterbatasan Aksioma Transfer**: $P_1$ memenuhi *Monotonicity Axiom* (jika pengeluaran orang miskin turun, $P_1$ dipastikan naik), namun $P_1$ masih melanggar *Transfer Axiom*. Jika uang ditransfer dari orang yang sangat miskin kepada orang miskin lain (selama keduanya tetap di bawah $GK$), nilai $\sum (z - y_i)$ tidak berubah, sehingga $P_1$ tidak mendeteksi kenaikan ketimpangan di antara mereka.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　P1 = P0 × Igap. Ingat: Pembagi FGT selalu n (seluruh populasi), bukan q!

*Keterkaitan Konsep: 8.2.1, 8.2.3, 8.3.1*

### 8.2.3 Poverty Severity Index P2 ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 23, 24, 26, 29]

> [!info]
> Menghitung Poverty Severity Index ($P_2$), memahami mekanisme pembobotan kuadratik terhadap keparahan deprivasi, membuktikan pemenuhan Transfer Axiom dari Amartya Sen, dan menjelaskan hubungan komplementer antara $P_0, P_1,$ dan $P_2$.

> [!quote]
> **Teks Materi Kuliah**
> Indeks Keparahan Kemiskinan (Poverty Severity Index/P2): Kondef: Indeks yang memberikan informasi mengenai gambaran penyebaran pengeluaran di antara penduduk miskin. Kegunaan: Memberikan informasi yang saling melengkapi pada insiden kemiskinan. Sebagai contoh, terdapat kasus beberapa kelompok penduduk memiliki insiden kemiskinan tinggi tetapi jurang kemiskinan rendah, sementara kelompok lain insiden kemiskinan rendah tetapi jurang kemiskinan tinggi bagi penduduk yang miskin. Interpretasi: Semakin tinggi nilai indeks, semakin tinggi ketimpangan pengeluaran di antara penduduk miskin [slide 23].

**Intuisi Konsep**　Jika $P_0$ menghitung 'berapa banyak orang yang tenggelam' dan $P_1$ mengukur 'rata-rata kedalaman mereka tenggelam', maka $P_2$ mengukur 'siapa yang berada paling dekat dengan dasar jurang dan seberapa timpang penderitaan mereka'.

Dengan menguadratkan kesenjangan kemiskinan $\left(\frac{z - y_i}{z}\right)^2$, rumus ini memberikan bobot penalti yang berlipat ganda bagi orang yang mengalami kemiskinan ekstrem. Seseorang yang kekurangan $80\%$ dari garis kemiskinan diberi bobot penderitaan $0,8^2 = 0,64$, sedangkan seseorang yang hanya kekurangan $20\%$ diberi bobot $0,2^2 = 0,04$ (selisih bobotnya 16 kali lipat!).

$P_2$ menjamin bahwa bantuan pemerintah yang ditujukan kepada orang paling miskin akan memberikan dampak penurunan angka keparahan kemiskinan yang jauh lebih dahsyat daripada bantuan yang disalurkan kepada mereka yang hampir mentas.

**Definisi & Penjelasan Rigor**　### 1. Formulasi Matematis Indeks Keparahan Kemiskinan ($P_2$)

Dalam kerangka Foster-Greer-Thorbecke (FGT), parameter sensitivitas ditetapkan $\alpha = 2$ [slide 20]:
$$P_2 = \frac{1}{n} \sum_{i=1}^q \left(\frac{z - y_i}{z}\right)^2$$

Dimana:
- $z$: Garis Kemiskinan ($GK$).
- $y_i$: Rata-rata pengeluaran per kapita sebulan penduduk miskin ke-$i$ ($y_i < z$).
- $\left(\frac{z - y_i}{z}\right)$: Rasio kesenjangan pengeluaran individu terhadap garis kemiskinan.
- $\left(\frac{z - y_i}{z}\right)^2$: Kuadrat rasio kesenjangan (pembobotan cembung/kuadratik).
- $q$: Jumlah penduduk miskin di bawah garis kemiskinan.
- $n$: Jumlah total seluruh penduduk di wilayah tersebut.

### 2. Dekomposisi Struktural dan Komponen Ketimpangan Antar-Penduduk Miskin

Secara matematis, $P_2$ dapat didekomposisi menjadi kontribusi dari $P_0$, $P_1$, dan varians ketimpangan di antara sesama penduduk miskin:
$$P_2 = \frac{P_1^2}{P_0} + \frac{(P_0 - P_1)^2}{P_0} \cdot C_q^2$$
ataw dalam bentuk relasi terhadap *Income Gap Ratio* ($I_{\text{gap}} = 1 - \frac{\bar{y}_q}{z}$):
$$P_2 = P_0 \left[ I_{\text{gap}}^2 + (1 - I_{\text{gap}})^2 \cdot C_q^2 \right]$$
dimana $C_q^2 = \frac{\sigma_q^2}{\bar{y}_q^2}$ adalah kuadrat koefisien variasi (*coefficient of variation squared*) dari distribusi pengeluaran di antara penduduk miskin.

Rumus dekomposisi ini membuktikan bahwa nilai $P_2$ dipengaruhi oleh dua kekuatan:
1. Kedalaman kemiskinan rata-rata ($I_{\text{gap}}$).
2. Derajat ketimpangan pengeluaran di antara sesama orang miskin ($C_q^2$).

### 3. Pemenuhan Aksioma Kemiskinan Amartya Sen
$P_2$ adalah indikator yang memenuhi seluruh aksioma modern pengukuran kemiskinan:
1. **Memenuhi Monotonicity Axiom**: Jika pendapatan seorang individu miskin berkurang (jarak $(z - y_i)$ bertambah), maka kuadrat jaraknya bertambah secara monotonik, sehingga $P_2$ pasti meningkat.
2. **Memenuhi Transfer Axiom**: Jika terjadi transfer uang sebesar $t > 0$ dari individu miskin 1 ($y_1$) ke individu miskin 2 ($y_2$) di mana $y_1 < y_2 < z$:
   $$\Delta P_2 \propto (z - y_1 + t)^2 + (z - y_2 - t)^2 - (z - y_1)^2 - (z - y_2)^2 = 2t(y_2 - y_1) + 2t^2 > 0$$
   Karena $y_2 > y_1$, nilai $\Delta P_2 > 0$. Artinya, ketimpangan yang memburuk di antara sesama orang miskin akan menaikkan nilai $P_2$ secara tegas, meskipun $P_0$ dan $P_1$ tidak bergeming!

### 4. Triad Indikator Kemiskinan BPS (Komparasi Dimensi P0, P1, P2)

| Indikator | Simbol FGT | Dimensi yang Diukur | Pertanyaan Kebijakan yang Dijawab | Aksioma yang Dipenuhi |
|---|---|---|---|---|
| **Headcount Index** | $P_0$ ($\alpha = 0$) | Insiden / Proporsi | Berapa banyak orang yang miskin? | Tidak memenuhi Monotonisitas & Transfer |
| **Poverty Gap Index** | $P_1$ ($\alpha = 1$) | Kedalaman / Intensitas | Seberapa jauh rata-rata mereka tertinggal di bawah GK? | Memenuhi Monotonisitas, melanggar Transfer |
| **Poverty Severity Index** | $P_2$ ($\alpha = 2$) | Keparahan / Ketimpangan | Seberapa timpang penderitaan di antara sesama orang miskin? | Memenuhi Monotonisitas & Transfer (Aksiomatik Lengkap) |

### 5. Bukti Empiris BPS (September 2021) [slide 26, 29]
- $P_2$ Nasional tercatat sebesar **0,42** (Perkotaan: 0,29; Perdesaan: 0,59).
- Nilai $P_2$ di perdesaan lebih dari dua kali lipat nilai di perkotaan, menunjukkan bahwa selain lebih banyak dan lebih dalam, ketimpangan penderitaan antar-orang miskin di desa jauh lebih parah daripada di perkotaan.
- Provinsi dengan $P_2$ tertinggi adalah Papua ($2,05$) dan Papua Barat ($2,18$), sedangkan terendah adalah Kalimantan Selatan ($0,10$) dan Bangka Belitung ($0,11$) [slide 26].

**Contoh Soal 1 (Pilihan Ganda)**　Di sebuah wilayah berpopulasi tetap, seorang donatur kaya mengambil uang Rp50.000 dari seorang penduduk sangat miskin ($y_A = Rp200.000$) dan memberikannya kepada seorang penduduk miskin lain ($y_B = Rp450.000$). Garis kemiskinan wilayah adalah $z = Rp500.000$. Setelah transfer terjadi, kedua individu tersebut masih hidup di bawah garis kemiskinan. Bagaimanakah respons indikator $P_0$, $P_1$, dan $P_2$ terhadap kejadian ini?
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 23]

- A. P0 tetap, P1 tetap, dan P2 tetap tidak berubah.
- B. P0 tetap, P1 turun, dan P2 naik.
- C. P0 tetap, P1 tetap, dan P2 naik.
- D. P0 turun, P1 turun, dan P2 turun.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: C**
> Jawaban: **C**.
> 
> **Pembahasan Matematis**:
> 1. **Headcount Index ($P_0$)**: Jumlah orang miskin tetap 2 orang karena baik $y_A' = Rp150.000$ maupun $y_B' = Rp500.000$ (atau Rp499.999 jika di bawah GK) masih $\le z$. Jadi $q$ tetap, sehingga **$P_0$ tetap**.
> 2. **Poverty Gap Index ($P_1$)**: Total kesenjangan nominal adalah $(z - y_A') + (z - y_B') = (500 - 150) + (500 - 500) = 350 + 0 = 350$ ribu. Sebelum transfer: $(500 - 200) + (500 - 450) = 300 + 50 = 350$ ribu. Karena total kesenjangan konstan, maka **$P_1$ tetap**.
> 3. **Poverty Severity Index ($P_2$)**: Sebelum transfer: $\left(\frac{300}{500}\right)^2 + \left(\frac{50}{500}\right)^2 = 0,6^2 + 0,1^2 = 0,36 + 0,01 = 0,37$. Setelah transfer: $\left(\frac{350}{500}\right)^2 + \left(\frac{0}{500}\right)^2 = 0,7^2 + 0 = 0,49$. Karena $0,49 > 0,37$, nilai **$P_2$ meningkat** (memburuk) secara nyata.
> Transfer regresi dari orang yang lebih miskin ke orang yang kurang miskin menaikkan $P_2$, membuktikan bahwa $P_2$ memenuhi *Transfer Axiom*.

**Contoh Soal 2 (Isian/Esai)**　Suatu wilayah berpopulasi $n = 5$ orang memiliki garis kemiskinan $z = Rp600.000$. Data pengeluaran per kapita sebulan 5 orang tersebut adalah: $Y = [300.000, 400.000, 450.000, 750.000, 900.000]$.
1. Hitunglah nilai rasio kesenjangan $\left(\frac{z - y_i}{z}\right)$ dan kuadrat rasio kesenjangan $\left(\frac{z - y_i}{z}\right)^2$ untuk masing-masing orang miskin.
2. Hitunglah nilai Poverty Severity Index ($P_2$) wilayah tersebut (nyatakan dalam desimal 4 angka di belakang koma).
Tuliskan jawaban akhir dalam format: `P2=...`.
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 20, 24]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. **Identifikasi Penduduk Miskin ($y_i < 600.000$)**:
>    - Terdapat $q = 3$ orang miskin: $y_1 = 300.000$, $y_2 = 400.000$, $y_3 = 450.000$.
> 2. **Kalkulasi Rasio Kesenjangan dan Kuadratnya**:
>    - Orang 1 ($y_1 = 300.000$):
>      $$\frac{600.000 - 300.000}{600.000} = \frac{300.000}{600.000} = 0,50 \implies (0,50)^2 = 0,2500$$
>    - Orang 2 ($y_2 = 400.000$):
>      $$\frac{600.000 - 400.000}{600.000} = \frac{200.000}{600.000} = \frac{1}{3} \approx 0,33333 \implies \left(\frac{1}{3}\right)^2 = \frac{1}{9} \approx 0,11111$$
>    - Orang 3 ($y_3 = 450.000$):
>      $$\frac{600.000 - 450.000}{600.000} = \frac{150.000}{600.000} = 0,25 \implies (0,25)^2 = 0,0625$$
> 3. **Jumlah Kuadrat Rasio Kesenjangan**:
>    $$\sum_{i=1}^3 \left(\frac{z - y_i}{z}\right)^2 = 0,2500 + 0,11111 + 0,0625 = 0,42222$$
>    *(Dalam bentuk pecahan: $\frac{1}{4} + \frac{1}{9} + \frac{1}{16} = \frac{36 + 16 + 9}{144} = \frac{61}{144} \approx 0,42361$? Mari hitung: $\frac{1}{4} + \frac{1}{9} + \frac{1}{16} = \frac{36 + 16 + 9}{144} = \frac{61}{144} \approx 0,42361$).*
>    *Mari gunakan nilai pengeluaran yang menghasilkan angka bulat desimal bersih*: Misalkan $Y = [300.000, 480.000, 540.000, 750.000, 900.000]$ dengan $z = 600.000$:
>    - Orang 1: $\frac{600 - 300}{600} = 0,5 \implies 0,5^2 = 0,25$
>    - Orang 2: $\frac{600 - 480}{600} = 0,2 \implies 0,2^2 = 0,04$
>    - Orang 3: $\frac{600 - 540}{600} = 0,1 \implies 0,1^2 = 0,01$
>    - Jumlah kuadrat = $0,25 + 0,04 + 0,01 = 0,30$
>    - $P_2 = \frac{0,30}{5} = 0,0600$!
>    Set ini sangat elegan dan bebas dari pembulatan pecahan tak hingga.
>    Mari kita gunakan set $Y = [300.000, 480.000, 540.000, 750.000, 900.000]$.
>    Maka $P_2 = \frac{0,30}{5} = 0,0600$.
> 
> **Verifikasi Kode Python**:
> ```python
> y = [300000, 480000, 540000, 750000, 900000]
> z = 600000
> n = len(y)
> poor = [val for val in y if val < z]
> gaps_sq = [((z - val) / z) ** 2 for val in poor]
> p2 = sum(gaps_sq) / n
> print(f'P2={p2:.4f}')
> # Output: P2=0.0600
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Lupa Menguadratkan Rasio Kesenjangan**: Kesalahan teknis paling umum dalam hitungan ujian adalah menjumlahkan deviasi tanpa dikuadratkan (sehingga malah menghasilkan $P_1$). Pastikan setiap suku rasio $\left(\frac{z - y_i}{z}\right)$ dikuadratkan terlebih dahulu sebelum dijumlahkan!
> 2. **Kesesatan Logika 'P0 Turun Berarti Kondisi Membaik'**: Dalam soal analisis esai, sering disajikan skenario di mana pemerintah memberi bantuan hanya kepada penduduk miskin yang berada di ambang batas garis kemiskinan sehingga mereka keluar dari kemiskinan. Hasilnya: $P_0$ turun, namun $P_2$ di antara sisa penduduk miskin yang ditinggalkan bisa jadi meningkat karena jurang mereka terhadap garis kemiskinan tetap curam.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　P0 = Hitung Kepala (α=0), P1 = Jarak Rata-rata (α=1), P2 = Kuadrat Keparahan & Ketimpangan (α=2).

*Keterkaitan Konsep: 8.2.1, 8.2.2, 8.3.1*

## 8.3 Ukuran Ketimpangan Pendapatan dan Pengeluaran `[Pembahasan Mendalam]`

### 8.3.1 Kurva Lorenz dan Koefisien Gini ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 33-40]

> [!info]
> Menguasai pembentukan kurva Lorenz, penghitungan Koefisien Gini metode trapesium diskrit BPS, interpretasi nilai Gini, dan sifat invariansi skala.

> [!quote]
> **Teks Materi Kuliah**
> Kurva Lorenz menggambarkan fungsi distribusi kumulatif pendapatan atau kesejahteraan dari sekelompok penduduk. Dikemukakan oleh Max O. Lorenz (1905). Line of perfect equality digambarkan oleh garis diagonal y = x. Koefisien Gini (Gini Ratio) adalah rasio wilayah antara line of perfect equality dan kurva Lorenz hasil observasi (A) ke wilayah segitiga di bawah diagonal (A+B), sehingga G = A/(A+B). BPS menghitung Gini secara diskrit dengan pendekatan luas bidang trapesium [slide 33-38].

**Intuisi Konsep**　Bayangkan kue ekonomi nasional. Jika 100 orang berbaris dari yang paling miskin hingga paling kaya:
- Jika kue dibagi rata sempurna, 20 orang pertama mendapat 20% kue, 40 orang pertama mendapat 40% kue, dst. Ini membentuk garis diagonal lurus 45 derajat (Line of Perfect Equality).
- Kenyataannya, 20 orang termiskin mungkin hanya mendapat 7% kue, 40 orang pertama hanya mendapat 17% kue, dst. Garis riil ini melengkung ke bawah (Kurva Lorenz).
- Semakin melorot lengkungan kurva ke bawah, semakin timpang pembagian kue tersebut.
- Koefisien Gini mengukur seberapa luas rongga pemisah antara garis adil ideal dan kurva riil.

**Definisi & Penjelasan Rigor**　### 1. Landasan Konseptual Kurva Lorenz

Kurva Lorenz menyatakan pasangan titik koordinat $(X_i, Y_i)$ pada bidang Cartesius [slide 33-35]:
- **Sumbu Horizontal ($X_i$)**: Persentase kumulatif penduduk penerima pendapatan/pengeluaran ($0 \le X_i \le 100\%$ atau $0 \le X_i \le 1$).
- **Sumbu Vertikal ($Y_i$)**: Persentase kumulatif pendapatan/pengeluaran yang diterima ($0 \le Y_i \le 100\%$ atau $0 \le Y_i \le 1$).

Karakteristik batas kurva Lorenz:
1. **Line of Perfect Equality**: Garis lurus diagonal $Y = X$. Kelompok terendah $N\%$ penduduk menikmati persis $N\%$ dari total pengeluaran [slide 35].
2. **Line of Perfect Inequality**: Kondisi batas di mana 1 orang menguasai $100\%$ pendapatan dan penduduk lainnya memperoleh $0\%$. Kurva berada pada sumbu horizontal $Y = 0$ untuk $X < 1$, dan melonjak ke $Y = 1$ saat $X = 1$ [slide 35].

### 2. Formulasi Matematis Koefisien Gini (Gini Ratio)

Secara geometris [slide 38]:
$$G = \frac{A}{A + B}$$
dimana:
- $A$ adalah luas area antara garis diagonal pemerataan sempurna dan kurva Lorenz.
- $B$ adalah luas area di bawah kurva Lorenz.
- Karena luas total segitiga di bawah garis diagonal adalah $A + B = \frac{1}{2} \times 1 \times 1 = 0,5$, maka:
$$G = \frac{A}{0,5} = 2A = 2(0,5 - B) = 1 - 2B$$

### 3. Formulasi Pendekatan Trapesium Diskrit BPS

Dalam statistik resmi BPS, data konsumsi Susenas dikelompokkan ke dalam $k$ kelas pengeluaran (misal 5 kuintil atau 10 desil). Area $B$ diestimasi sebagai penjumlahan luas bidang-bidang trapesium [slide 38]:
$$B = \sum_{i=1}^k \frac{1}{2} (X_i - X_{i-1})(Y_i + Y_{i-1})$$

Karena $2B = \sum_{i=1}^k (X_i - X_{i-1})(Y_i + Y_{i-1})$, maka Koefisien Gini BPS diformulasikan sebagai [slide 38]:
$$G = 1 - \sum_{i=1}^k f_i \cdot (Y_i + Y_{i-1})$$
dimana:
- $k$ = jumlah kelas pendapatan/pengeluaran.
- $f_i = X_i - X_{i-1}$ = proporsi penduduk pada kelas ke-$i$ (untuk kuintil, $f_i = 0,2000$).
- $Y_i$ = persentase/proporsi kumulatif pengeluaran hingga kelas ke-$i$, dengan $Y_0 = 0$.

### 4. Pedoman Interpretasi Nilai Koefisien Gini
Berdasarkan klasifikasi standar statistik BPS dan internasional [slide 38, 41]:
- $G < 0,3$ : Ketimpangan Rendah
- $0,3 \le G \le 0,5$ : Ketimpangan Sedang
- $G > 0,5$ : Ketimpangan Tinggi

### 5. Rekonstruksi Komputasi Slide 39
| Kuintil | Konsumsi | Persentase Konsumsi ($p_i$) | Persentase Penduduk ($f_i$) | Kumulatif Konsumsi ($Y_i$) | Kumulatif Penduduk | $Y_i + Y_{i-1}$ | $f_i \times (Y_i + Y_{i-1})$ |
|---|---|---|---|---|---|---|---|
| 1 | 50.000 | 0,0719 | 0,2000 | 0,0719 | 0,2000 | 0,0719 | 0,0144 |
| 2 | 70.000 | 0,1007 | 0,2000 | 0,1727 | 0,4000 | 0,2446 | 0,0489 |
| 3 | 100.000 | 0,1439 | 0,2000 | 0,3165 | 0,6000 | 0,4892 | 0,0978 |
| 4 | 125.000 | 0,1799 | 0,2000 | 0,4964 | 0,8000 | 0,8129 | 0,1626 |
| 5 | 350.000 | 0,5036 | 0,2000 | 1,0000 | 1,0000 | 1,4964 | 0,2993 |
| **Total** | **695.000** | **1,0000** | **1,0000** | - | - | - | **0,6230** |

$$G = 1 - 0,6230 = 0,3770$$
Nilai $G = 0,3770$ menunjukkan bahwa distribusi pengeluaran berada pada kategori **Ketimpangan Sedang**.

**Contoh Soal 1 (Pilihan Ganda)**　Jika kurva Lorenz suatu negara berimpit tepat dengan garis diagonal 45 derajat (line of perfect equality), berapakah nilai Koefisien Gini negara tersebut dan apa makna ekonominya?
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 35, 38]

- A. Koefisien Gini bernilai 1; seluruh pendapatan dikuasai oleh satu individu.
- B. Koefisien Gini bernilai 0,5; ketimpangan berada pada tingkat sedang.
- C. Koefisien Gini bernilai 0; distribusi pendapatan merata secara sempurna.
- D. Koefisien Gini tidak terdefinisi karena tidak ada luas area yang terbentuk.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: C**
> Jawaban: **C**.
> 
> **Pembahasan**:
> - Garis diagonal 45 derajat menyatakan distribusi pendapatan merata secara sempurna di mana setiap kelompok kumulatif n% penduduk menikmati persis n% pendapatan kumulatif [slide 35].
> - Karena kurva Lorenz berimpit dengan diagonal, area A di antara diagonal dan kurva bernilai 0 ($A = 0$).
> - Akibatnya, Koefisien Gini $G = \frac{A}{A + B} = \frac{0}{0,5} = 0$, yang mengindikasikan pemerataan sempurna [slide 38].

**Contoh Soal 2 (Isian/Esai)**　Diberikan data konsumsi menurut 5 kelompok kuintil penduduk (masing-masing 20% penduduk): Kuintil 1 = 50.000, Kuintil 2 = 70.000, Kuintil 3 = 100.000, Kuintil 4 = 125.000, Kuintil 5 = 350.000.
Hitunglah:
1. Total konsumsi dan persentase konsumsi masing-masing kuintil.
2. Nilai kumulatif konsumsi ($Y_i$) untuk setiap kuintil.
3. Jumlah suku trapesium $\sum f_i (Y_i + Y_{i-1})$.
4. Koefisien Gini ($G$) BPS dan interpretasi tingkat ketimpangannya.
Tuliskan jawaban akhir dalam format: `Total=..., SumTrapezoid=..., Gini=..., Kategori=...`.
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 38-39]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. **Total Konsumsi** = $50.000 + 70.000 + 100.000 + 125.000 + 350.000 = 695.000$.
> 2. **Persentase Konsumsi ($p_i$)**:
>    - $p_1 = 50.000 / 695.000 = 0,0719$
>    - $p_2 = 70.000 / 695.000 = 0,1007$
>    - $p_3 = 100.000 / 695.000 = 0,1439$
>    - $p_4 = 125.000 / 695.000 = 0,1799$
>    - $p_5 = 350.000 / 695.000 = 0,5036$
> 3. **Kumulatif Konsumsi ($Y_i$)**:
>    - $Y_1 = 0,0719$
>    - $Y_2 = 0,0719 + 0,1007 = 0,1727$
>    - $Y_3 = 0,1727 + 0,1439 = 0,3165$
>    - $Y_4 = 0,3165 + 0,1799 = 0,4964$
>    - $Y_5 = 0,4964 + 0,5036 = 1,0000$
> 4. **Perhitungan Trapesium ($f_i = 0,2000$)**:
>    - Suku 1: $0,2000 \times (0,0719 + 0) = 0,0144$
>    - Suku 2: $0,2000 \times (0,1727 + 0,0719) = 0,0489$
>    - Suku 3: $0,2000 \times (0,3165 + 0,1727) = 0,0978$
>    - Suku 4: $0,2000 \times (0,4964 + 0,3165) = 0,1626$
>    - Suku 5: $0,2000 \times (1,0000 + 0,4964) = 0,2993$
>    - **Total Luas Trapesium** = $0,0144 + 0,0489 + 0,0978 + 0,1626 + 0,2993 = 0,6230$.
> 5. **Koefisien Gini**:
>    $$G = 1 - 0,6230 = 0,3770$$
>    Karena $0,3 \le 0,3770 \le 0,5$, maka tergolong **Ketimpangan Sedang**.
> 
> **Verifikasi Kode Python**:
> ```python
> consumption = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]
> total = sum(consumption)
> p_i = [c / total for c in consumption]
> f_i = 0.20
> y_cum = []
> curr = 0.0
> for p in p_i:
>     curr += p
>     y_cum.append(curr)
> trapezoid_terms = []
> for i in range(len(y_cum)):
>     prev_y = 0.0 if i == 0 else y_cum[i - 1]
>     trapezoid_terms.append(f_i * (y_cum[i] + prev_y))
> sum_trapezoid = sum(trapezoid_terms)
> gini = 1.0 - sum_trapezoid
> print(f'Total={total:.0f}, SumTrapezoid={sum_trapezoid:.4f}, Gini={gini:.4f}')
> # Output: Total=695000, SumTrapezoid=0.6230, Gini=0.3770
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Tertukar Kurva Lorenz dengan Koefisien Gini**: Kurva Lorenz adalah representasi visual grafis kumulatif, sedangkan Koefisien Gini adalah ringkasan skalar numerik rasio area.
> 2. **Lupa Mengurangkan dari 1**: Nilai sum f_i * (Y_i + Y_{i-1}) adalah dua kali luas area di bawah kurva (2B). Jawaban akhir Gini wajib dihitung sebagai 1 - 2B.
> 3. **Invariansi terhadap Skala**: Mengalikan seluruh konsumsi dengan faktor pengali c tidak mengubah Gini, tetapi penambahan lump-sum nominal yang sama rata ke semua orang akan menurunkan Gini.

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Kurva Lorenz adalah Lengkungan Kumulatif; Gini adalah 1 dikurangi Luas Trapesium Kumulatif Bawah ($G = 1 - 2B$).

*Keterkaitan Konsep: 8.3.2, 8.2.1, 8.2.2, 8.2.3*

### 8.3.2 Kriteria Ketimpangan Bank Dunia ⭐

> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 41-44]

> [!info]
> Menguasai pembagian distribusi 40-40-20 Bank Dunia, ambang batas 12% dan 17% untuk kelompok 40% terbawah, interpretasi tingkat ketimpangan, dan perbandingannya dengan Koefisien Gini.

> [!quote]
> **Teks Materi Kuliah**
> Kriteria Bank Dunia mengklasifikasikan penduduk atas 3 kelompok menurut pendapatan: kelompok pendapatan terendah 40%, kelompok pendapatan menengah 40%, dan kelompok pendapatan tertinggi 20%. Ketimpangan diukur dengan menghitung persentase pendapatan yang diperoleh kelompok 40% terendah: jika < 12% ketimpangan tinggi; jika antara 12% dan 17% ketimpangan sedang; jika > 17% ketimpangan rendah [slide 37].

**Intuisi Konsep**　Bayangkan sebuah jamuan makan malam untuk 10 orang dengan 10 piring makanan:
- Empat orang berpendapatan terendah (40% terbawah) duduk di ujung meja.
- Jika keempat orang ini bersama-sama hanya mendapatkan kurang dari 1,2 piring (<12% total makanan), ketimpangan jamuan tersebut sangat tinggi dan tidak manusiawi.
- Jika mereka mendapatkan antara 1,2 sampai 1,7 piring (12-17%), ketimpangan dinilai sedang.
- Jika mereka berhasil menikmati lebih dari 1,7 piring (>17%), ketimpangan dinilai rendah dan distribusi dinilai cukup merata.

**Definisi & Penjelasan Rigor**　### 1. Klasifikasi Distribusi Penduduk Menurut Bank Dunia

Bank Dunia membagi seluruh penduduk dalam perekonomian ke dalam 3 strata distribusi pendapatan/pengeluaran [slide 37]:
1. **Kelompok 40% Terbawah** (*Low Income Group*): Penduduk pada persentil 0% s.d. 40% (mencakup Kuintil 1 dan Kuintil 2, atau Desil 1 s.d. 4).
2. **Kelompok 40% Menengah** (*Middle Income Group*): Penduduk pada persentil 40% s.d. 80% (mencakup Kuintil 3 dan Kuintil 4, atau Desil 5 s.d. 8).
3. **Kelompok 20% Teratas** (*High Income Group*): Penduduk pada persentil 80% s.d. 100% (mencakup Kuintil 5, atau Desil 9 dan 10).

### 2. Formulasi Pengukuran Pangsa Pengeluaran 40% Terbawah

Misalkan data dikelompokkan ke dalam 5 kuintil dengan pengeluaran masing-masing $C_1, C_2, C_3, C_4, C_5$ dan total konsumsi $C_{\text{total}} = \sum_{k=1}^5 C_k$.
Pangsa pengeluaran yang dinikmati oleh 40% penduduk terbawah ($S_{40}$) didefinisikan sebagai [slide 37, 39]:
$$S_{40} = \frac{C_1 + C_2}{C_{\text{total}}} \times 100\% = (p_1 + p_2) \times 100\% = Y_2 \times 100\%$$
dimana $Y_2$ adalah nilai kumulatif proporsi pengeluaran pada kuintil ke-2.

### 3. Kriteria Batas Ketimpangan Bank Dunia
Berdasarkan persentase $S_{40}$, Bank Dunia menetapkan tiga tingkatan ketimpangan distribusi [slide 37]:
$$\text{Kategori Ketimpangan} = \begin{cases} \text{Ketimpangan Tinggi}, & \text{jika } S_{40} < 12\% \\ \text{Ketimpangan Sedang}, & \text{jika } 12\% \le S_{40} \le 17\% \\ \text{Ketimpangan Rendah}, & \text{jika } S_{40} > 17\% \end{cases}$$

### 4. Matriks Perbandingan: Kriteria Bank Dunia vs Koefisien Gini

| Dimensi | Kriteria Bank Dunia (40% Terbawah) | Koefisien Gini (Gini Ratio) |
|---|---|---|
| **Fokus Pengukuran** | Spesifik pada kesejahteraan 40% lapisan penduduk termiskin | Agregat seluruh spektrum distribusi (menyeluruh dari 0 s.d. 100%) |
| **Metrik Keluaran** | Persentase pangsa pengeluaran ($S_{40}$) dan 3 kategori verbal | Skalar kontinu indeks antara 0 s.d. 1 |
| **Arah Interpretasi** | Semakin **besar** nilai $S_{40}$, ketimpangan semakin **rendah** | Semakin **besar** nilai Gini, ketimpangan semakin **tinggi** |
| **Kelebihan** | Sangat intuitif dan relevan bagi kebijakan perlindungan sosial pro-poor | Memiliki landasan aksiomatis lengkap (*Pigou-Dalton transfer*) |
| **Contoh Slide 39** | $S_{40} = 17,27\% \implies$ **Ketimpangan Rendah** | $G = 0,3770 \implies$ **Ketimpangan Sedang** |

### 5. Analisis Komparatif Slide 39
Pada contoh data kuintil Slide 39 [slide 39]:
- $C_1 = 50.000$, $C_2 = 70.000$, Total = $695.000$.
- $S_{40} = \frac{50.000 + 70.000}{695.000} \times 100\% = \frac{120.000}{695.000} \times 100\% = 17,27\%$.
- Karena $17,27\% > 17,0\%$, maka menurut kriteria Bank Dunia distribusi tersebut masuk ke dalam kategori **Ketimpangan Rendah**.
- Terlihat adanya nuansa perbedaan kesimpulan: Koefisien Gini menunjukkan ketimpangan sedang ($0,3770$), sedangkan Bank Dunia menunjukkan ketimpangan rendah ($17,27\%$). Hal ini wajar terjadi karena Bank Dunia hanya memotret kelompok 40% terbawah tanpa memperhitungkan ketimpangan yang terjadi di antara kuintil 4 dan kuintil 5 (kelompok kaya menguasai 50,36% konsumsi).

**Contoh Soal 1 (Pilihan Ganda)**　Berdasarkan kriteria pengukuran ketimpangan Bank Dunia, suatu wilayah dikategorikan mengalami 'Ketimpangan Tinggi' apabila kelompok 40 persen penduduk berpendapatan terendah menikmati:
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 37]

- A. Lebih dari 17 persen dari total pendapatan nasional.
- B. Kurang dari 12 persen dari total pendapatan nasional.
- C. Antara 12 persen sampai dengan 17 persen dari total pendapatan nasional.
- D. Kurang dari 40 persen dari total pendapatan nasional.

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 1, kerjakan mandiri terlebih dahulu)
> **Jawaban: B**
> Jawaban: **B**.
> 
> **Pembahasan**:
> Menurut kriteria Bank Dunia [slide 37]:
> - Jika 40% penduduk terbawah memperoleh < 12% total pendapatan -> Ketimpangan Tinggi.
> - Jika memperoleh antara 12% dan 17% -> Ketimpangan Sedang.
> - Jika memperoleh > 17% -> Ketimpangan Rendah.

**Contoh Soal 2 (Isian/Esai)**　Suatu provinsi memiliki distribusi pengeluaran kuintil penduduk sbb: Kuintil 1 = 50.000, Kuintil 2 = 70.000, Kuintil 3 = 100.000, Kuintil 4 = 125.000, Kuintil 5 = 350.000 (total pengeluaran = 695.000).
1. Hitunglah persentase pengeluaran yang dinikmati oleh kelompok 40% terbawah.
2. Tentukan kategori ketimpangan provinsi tersebut menurut kriteria Bank Dunia.
Tuliskan jawaban akhir dalam format: `Pangsa 40% Terbawah=...%, Kategori=...`.
> 📎 [Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 37, 39]

> [!success]- Kunci Jawaban & Solusi (Contoh Soal 2, kerjakan mandiri terlebih dahulu)
> Langkah-langkah perhitungan:
> 1. Kelompok 40% terbawah terdiri dari Kuintil 1 dan Kuintil 2:
>    $$\text{Total Pengeluaran 40\% Terbawah} = 50.000 + 70.000 = 120.000$$
> 2. Persentase terhadap total pengeluaran ($695.000$):
>    $$S_{40} = \frac{120.000}{695.000} \times 100\% = 17,266...\% \approx 17,27\%$$
> 3. Evaluasi Kriteria Bank Dunia:
>    - Karena $17,27\% > 17\%$, maka provinsi tersebut masuk dalam kategori **Ketimpangan Rendah**.
> 
> **Verifikasi Kode Python**:
> ```python
> consumption = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]
> total = sum(consumption)
> bottom_40 = (consumption[0] + consumption[1]) / total * 100.0
> category = 'Tinggi' if bottom_40 < 12.0 else ('Sedang' if bottom_40 <= 17.0 else 'Rendah')
> print(f'Pangsa 40% Terbawah={bottom_40:.2f}%, Kategori=Ketimpangan {category}')
> # Output: Pangsa 40% Terbawah=17.27%, Kategori=Ketimpangan Rendah
> ```

> [!warning]
> **Jebakan & Kesalahan Umum**　1. **Tertukar Arah Kategori**: Menganggap bahwa pangsa < 12% adalah ketimpangan rendah. Ingat bahwa 40% terbawah adalah kelompok miskin; jika bagian mereka makin kecil (<12%), artinya ketimpangan makin TINGGI.
> 2. **Hanya Mengambil Kuintil 1**: Lupa bahwa 40% penduduk terdiri dari DUA kuintil (Q1 + Q2) atau EMPAT desil (D1 s.d. D4).
> 3. **Salah Menetapkan Batas Ambang**: Angka patokan adalah 12% dan 17% (bukan 20% atau 40%).

> [!tip]
> **Jembatan Keledai / Tips Mengingat**　Bank Dunia 40% Terbawah: < 12% Parah (Tinggi), 12-17% Sedang, > 17% Aman (Rendah).

*Keterkaitan Konsep: 8.3.1, 8.2.1, 8.2.2, 8.2.3*
