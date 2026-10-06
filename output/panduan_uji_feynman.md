# Panduan Uji Feynman — Official Statistics Lanjutan (OSL)

> **Tujuan**: Menguji pemahaman konsep fundamental mahasiswa secara mendalam tanpa hafalan istilah rumit.  
> **Peran AI**: Berperan sebagai "Pemula Kritis (*Sharp Beginner*)" yang ingin memahami esensi konsep, mustahil dikelabui jargon, namun suportif dan analitis.  
> **Skala Penilaian**: Skor 1 s.d. 5 (1 = Miskonsepsi Fatal, 3 = Cukup tetapi Berlubang, 5 = Penguasaan Sempurna & Mampu Mengabstraksi).

---

## Modul 1: Kemiskinan FGT ($P_0, P_1, P_2$) — Pertemuan 8
- **Prompt Tantangan**:
  > *"Bayangkan saya sama sekali belum pernah belajar statistik. Coba jelaskan, kenapa pemerintah tidak cukup menghitung persentase orang miskin ($P_0$) saja? Kenapa kita repot-repot butuh $P_1$ dan $P_2$? Apa perbedaan nyata di lapangan antara wilayah dengan $P_1$ tinggi vs wilayah dengan $P_2$ tinggi?"*
- **Pertanyaan Penguji (Probing Questions)**:
  1. *"Jika saya punya uang bantuan Rp 10 juta, dan saya berikan ke orang yang pengeluarannya hanya Rp 5.000 di bawah garis kemiskinan agar dia langsung lewat garis kemiskinan, apakah itu kebijakan yang baik menurut $P_0$ vs $P_2$?"*
  2. *"Kenapa pada rumus FGT, pembaginya selalu seluruh penduduk ($n$), bukan hanya orang miskin ($q$)? Apa akibatnya kalau pembaginya diganti $q$?"*
- **Rubrik Skor 5 (Jawaban Ideal)**:
  - Mampu menjelaskan bahwa $P_0$ memiliki *perverse incentive* (mendorong pemerintah menolong orang miskin yang paling dekat dengan garis kemiskinan demi menurunkan angka statistik).
  - $P_1$ mengukur berapa rata-rata defisit anggaran yang dibutuhkan untuk mengentaskan orang miskin.
  - $P_2$ memberi bobot kuadrat (penalti lebih berat) bagi mereka yang berada di kemiskinan paling ekstrem (ketimpangan antar sesama miskin).
  - Pembagi $n$ menjamin sifat *subgroup decomposability* (dapat dijumlahkan secara konsisten antar wilayah).

---

## Modul 2: Diferensiasi Ketenagakerjaan ICLS 13 — Pertemuan 9
- **Prompt Tantangan**:
  > *"Mengapa seseorang yang membantu menjaga warung orang tuanya tanpa dibayar selama 2 jam seminggu sudah dikategorikan 'Bekerja' oleh BPS? Lalu bagaimana membedakan antara Setengah Penganggur dengan Pekerja Paruh Waktu jika sama-sama bekerja 20 jam seminggu?"*
- **Pertanyaan Penguji (Probing Questions)**:
  1. *"Bukankah tidak adil orang yang hanya kerja 2 jam tanpa upah disebut 'bekerja'? Kenapa patokannya harus 1 jam?"*
  2. *"Jika ada lulusan sarjana bekerja 15 jam seminggu di kafe dan sangat puas dengan waktunya karena ingin fokus hobinya, apakah dia setengah penganggur?"*
- **Rubrik Skor 5 (Jawaban Ideal)**:
  - Kriteria 1 jam adalah standar global ILO/ICLS untuk menangkap sekecil apa pun kontribusi aktivitas ekonomi terhadap output nasional (PDRB/PDB) dan mencegah bias gender pada pekerjaan subsisten keluarga.
  - Setengah penganggur mensyaratkan dua kondisi simultan: waktu (<35 jam) **DAN** kemauan (*willing & seeking additional work*). Jika sukarela dan tidak mencari kerja tambahan, statusnya adalah Pekerja Paruh Waktu (*Part-time*).

---

## Modul 3: Kerangka Sampel Area (KSA) vs Metode Konvensional — Pertemuan 11
- **Prompt Tantangan**:
  > *"Kenapa BPS beralih menggunakan Kerangka Sampel Area (KSA) dengan citra satelit dan aplikasi HP untuk menghitung produksi beras, dan meninggalkan laporan dinas pertanian (SP-Padi)? Apa kelemahan metode lama dan bagaimana KSA bekerja?"*
- **Pertanyaan Penguji (Probing Questions)**:
  1. *"Kapan petugas KSA turun ke sawah dan apa yang sebenarnya mereka foto?"*
  2. *"Bagaimana dari foto fase pertanaman bisa menjadi angka ton gabah kering giling?"*
- **Rubrik Skor 5 (Jawaban Ideal)**:
  - Metode SP-Padi lama berbasis laporan administratif aparat dinas di lapangan yang rawan bias subjektivitas dan *over-estimate* luas panen.
  - KSA berbasis sains geospasial objektif: membagi wilayah dalam grid $300\text{ m} \times 300\text{ m}$ dengan 9 titik subsegmen tetap yang difoto pada 7 hari terakhir setiap bulan.
  - Fase amatan (vegetatif, generatif, panen, puso) memodelkan siklus tanam secara probabilistik, yang dikombinasikan dengan ubinan acak ($2,5\text{ m} \times 2,5\text{ m}$) untuk menghitung produktivitas riil per hektar.

---

## Modul 4: IHK Modified Laspeyres & Disagregasi Inflasi — Pertemuan 12
- **Prompt Tantangan**:
  > *"Apa perbedaan rumus Laspeyres klasik dengan rumus Laspeyres yang dimodifikasi oleh BPS? Kenapa BPS tidak menghitung harga dikali kuantitas tahun dasar secara langsung?"*
- **Pertanyaan Penguji (Probing Questions)**:
  1. *"Dari mana angka diagram timbang ($W$) diperoleh, dan apakah diagram timbang itu berubah setiap bulan?"*
  2. *"Mengapa inflasi dibagi menjadi Inflasi Inti, Komponen Bergejolak, dan Harga Diatur? Siapa yang bertanggung jawab mengendalikan masing-masing?"*
- **Rubrik Skor 5 (Jawaban Ideal)**:
  - Laspeyres klasik membutuhkan kuantitas fisik tahun dasar ($Q_0$) yang sulit diperbarui. Formula Laspeyres modifikasi menggunakan *chaining* rasio harga relatif ($P_t / P_{t-1}$) dikalikan penimbang nilai konsumsi periode sebelumnya ($W_{t-1}$), bersumber dari Survei Biaya Hidup (SBH).
  - Inflasi Inti dipengaruhi faktor moneter fundamental (wilayah Bank Indonesia).
  - Inflasi Bergejolak (*Volatile Foods*) dipengaruhi panen/musim (wilayah Kementan/Kemendag).
  - Inflasi Diatur (*Administered*) dipengaruhi kebijakan tarif pemerintah/BUMN (BBM, listrik, tarif angkutan).

---

## Modul 5: Nilai Tukar Petani (NTP) & NTUP — Pertemuan 12
- **Prompt Tantangan**:
  > *"Jika sebuah provinsi mengumumkan bahwa NTP petaninya adalah 105, apakah itu berarti petani di sana sudah sejahtera dan kaya? Apa bedanya dengan NTUP?"*
- **Pertanyaan Penguji (Probing Questions)**:
  1. *"Komponen apa saja yang ada di dalam $I_b$ (Indeks Harga yang Dibayar Petani)?"*
  2. *"Bisakah seorang petani mengalami NTUP naik tinggi tetapi NTP-nya justru turun? Berikan contoh situasinya!"*
- **Rubrik Skor 5 (Jawaban Ideal)**:
  - NTP adalah ukuran daya tukar relatif (*terms of trade* relatif terhadap tahun dasar), bukan ukuran nominal laba bersih atau kekayaan total petani.
  - $I_b = \text{IKRT (Konsumsi Keluarga)} + \text{BPPBM (Biaya Produksi \& Modal)}$.
  - NTUP hanya membagi $I_t$ dengan BPPBM (kelayakan usaha murni).
  - Jika harga pupuk dan bibit stabil (NTUP tinggi), tetapi terjadi lonjakan inflasi beras/sembako dan biaya sekolah anak di desa (IKRT melonjak), maka NTP petani bisa merosot di bawah 100 meskipun usaha taninya untung.

---

## Modul 6: Merchanting & Valuasi FOB/CIF — Pertemuan 13
- **Prompt Tantangan**:
  > *"Perusahaan Indonesia membeli minyak dari Arab Saudi seharga USD 1 juta, lalu langsung menjualnya ke Filipina seharga USD 1,2 juta tanpa minyak itu pernah mendarat di pelabuhan Indonesia. Bagaimana BPS dan Neraca Pembayaran mencatat transaksi aneh ini?"*
- **Pertanyaan Penguji (Probing Questions)**:
  1. *"Apakah itu dicatat sebagai ekspor dan impor biasa? Mengapa?"*
  2. *"Kenapa impor di statistik BPS memakai CIF, tapi di Neraca Pembayaran memakai FOB?"*
- **Rubrik Skor 5 (Jawaban Ideal)**:
  - Berdasarkan standar SNA 2008 & BPM6, transaksi ini adalah *Merchanting of Goods*. Dicatat sebagai ekspor negatif saat barang dibeli (USD -1 juta) dan ekspor positif saat barang dijual (USD +1,2 juta), menghasilkan **ekspor barang neto sebesar USD 200 ribu**. Tidak dicatat sebagai impor karena tidak ada barang yang melintasi wilayah pabean domestik.
  - Impor BPS dinilai CIF karena dokumen kepabeanan (PIB) mencatat harga tiba di pelabuhan bongkar. Di Neraca Pembayaran, komponen asuransi dan pengangkutan dikeluarkan dari barang agar valuasi simetris dengan ekspor (FOB) dan dipindahkan ke neraca jasa angkutan/asuransi.
