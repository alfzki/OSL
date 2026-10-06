# 命题风格档案：Politeknik Statistika STIS / Official Statistics Lanjutan (OSL)
*Dosen Pengampu:* Tiodora Hadumaon Siagian  
*Sumber Data:* 42 butir Naskah Soal Resmi UAS 2022/2023 (`extracted/Soal_UAS_2022-2023.md`) & 50 butir Soal Latihan Mandiri UAS (`materials/past-exams/soal_latihan_uas.md`)  
*Tingkat Keyakinan:* Moderate (Evaluasi Silang Empiris: Top-5 Hit Rate 80.0%, MAE 8.73%)

---

## 1. 试卷结构 (Struktur Naskah Ujian)

- **Format Ujian:** Ujian Tertulis, durasi 120 menit.
- **Komposisi Butir Soal:**
  - *Bagian I: Pilihan Ganda (PG)*: 40–50 butir (bobot estimasi ~70–80%). Soal berorientasi konsep BPS, identifikasi metodologi, dan perhitungan ringkas.
  - *Bagian II: Esai & Hitungan*: 2–3 butir soal bertingkat (bobot estimasi ~20–30%). Mengharuskan penurunan/perhitungan matematis rinci (FGT kemiskinan $P_0, P_1, P_2$, Koefisien Gini, IHK Modified Laspeyres, atau ToT).
- **Distribusi Waktu Kerja:** Rata-rata 2–2,5 menit per butir PG, dengan 25–35 menit tersisa untuk pengerjaan soal esai hitungan numerik.

---

## 2. 难度与风格特征 (Karakteristik Gaya & Tingkat Kesulitan)

1. **Institusional BPS-Centric:**
   - Dosen sangat mengutamakan konvensi resmi BPS (misalnya batas jam kerja minimal 1 jam ICLS 13, metodologi KSA 9 subsegmen $300\text{ m} \times 300\text{ m}$, ubinan $2,5\text{ m} \times 2,5\text{ m}$, disagregasi inflasi inti/bergejolak/administered, valuasi CIF pada statistik perdagangan luar negeri BPS vs FOB pada SNA 2008).
2. **Pengecoh Berbasis Batas Syarat (Boundary Conditions & Distractors):**
   - Opsi pengecoh dirancang untuk menguji pemahaman syarat batas. Contoh: membedakan "pekerja paruh waktu sukarela" dengan "setengah penganggur" berdasarkan ada/tidaknya keinginan menambah jam kerja.
3. **Presisi Numerik Bertingkat:**
   - Soal hitungan tidak sekadar menanyakan rumus akhir, melainkan memerlukan langkah perantara (misal menghitung selisih garis kemiskinan $(z - y_i)/z$ per individu sebelum menjumlahkan untuk $P_1$ dan $P_2$).

---

## 3. 高频考点 → 教材章节映射 (Pemetaan Topik Frekuensi Tinggi ke Bab Kuliah)

| Peringkat | Bab / Topik | Bobot Empiris Historis | Karakteristik Soal yang Kerap Muncul |
|---|---|---|---|
| 1 | **Pertemuan 8: Kemiskinan & Ketimpangan** | 29.7% | Hitungan FGT $P_0, P_1, P_2$, rumus Koefisien Gini kurva Lorenz, batas GKM (2.100 kkal) + GKNM, kriteria Bank Dunia 40% terbawah. |
| 2 | **Pertemuan 12: Perdagangan & Indikator Harga** | 16.9% | Hitungan IHK Modified Laspeyres antar-periode, formula inflasi mtom/yony/ytd, disagregasi inflasi, rasio NTP ($It/Ib$) dan NTUP. |
| 3 | **Pertemuan 9: Ketenagakerjaan & Pendidikan** | 16.5% | Klasifikasi ICLS 13 (bekerja, penganggur, bukan angkatan kerja), TPAK, TPT, setengah penganggur vs paruh waktu, APK vs APM. |
| 4 | **Pertemuan 13: Ekspor-Impor & Pariwisata** | 15.8% | Valuasi FOB vs CIF, Merchanting Goods SNA 2008, Net Barter Terms of Trade, rumus TPK dan RLMT perhotelan. |
| 5 | **Pertemuan 11: Statistik Produksi** | 15.0% | Alur Kerangka Sampel Area (KSA), ubinan, konversi GKP ke Beras (SKGB), batasan tenaga kerja IBS ($\ge 20$) dan IMK ($1-19$). |
| 6 | **Pertemuan 10: Indikator Kesehatan** | 6.2% | Formula AKI/MMR (per 100.000 KH), AKB/IMR (per 1.000 KH), AKABA, Morbiditas 1 bulan terakhir, 5 antigen Imunisasi Dasar Lengkap. |

---

## 4. 各题型出题模板与评分标准 (Template Bentuk Soal & Rubrik Penilaian)

### Template 1: Pilihan Ganda Konseptual / Syarat Batas
- *Format:* Studi kasus pendek 1–2 kalimat mendeskripsikan aktivitas individu atau kegiatan ekonomi, diikuti pertanyaan klasifikasi status.
- *Kriteria Penilaian:* Opsi tunggal tepat (skor 2), tidak ada penalti nilai minus untuk jawaban salah.

### Template 2: Soal Hitungan Terstruktur (Esai)
- *Format:* Diberikan tabel mini pengeluaran beberapa rumah tangga / harga dan kuantitas komoditi, mahasiswa diminta menghitung indikator statistik resmi secara berurutan.
- *Rubrik Penilaian:*
  1. Penulisan formula matematis baku: 20% skor.
  2. Langkah substitusi angka ke dalam formula: 40% skor.
  3. Hasil numerik akhir dan interpretasi satuan (persen / poin indeks): 40% skor.

---

## 5. 典型真题摘录 (Kutipan Soal Ujian Riil)

1. *Kutipan Soal UAS 2022/2023 Butir 1 (Ketenagakerjaan):*
   > "Seseorang yang seminggu yang lalu membantu usaha orang tuanya tanpa dibayar selama 3 jam termasuk dalam kategori..."
   > *Kunci:* Bekerja (karena $\ge 1$ jam berturut-turut pada kegiatan ekonomi).
2. *Kutipan Soal UAS 2022/2023 Butir Esai (Kemiskinan FGT):*
   > "Diberikan data pengeluaran per kapita 5 individu dengan Garis Kemiskinan $Z = 500.000$. Hitunglah $P_0$, $P_1$, dan $P_2$ serta jelaskan arti dari masing-masing indikator tersebut."
