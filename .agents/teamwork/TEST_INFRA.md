# TEST_INFRA — Infrastruktur & Metodologi Pengujian E2E OSL

**Mata Kuliah**: Official Statistics Lanjutan (OSL) — Kode MK: K200207  
**Dosen Pengampu**: Dr. Tiodora Hadumaon Siagian  
**Penyusun**: E2E Test Writer (`e2e_test_writer_1`)  
**Tanggal**: 2026-09-29  
**Status**: Authoritative Test Infrastructure Specification  
**Lokasi**: `/home/alfzki/Documents/OSL/.agents/teamwork/TEST_INFRA.md` & `/home/alfzki/Documents/OSL/TEST_INFRA.md`

---

## 1. Filosofi & Metodologi Pengujian (Test Philosophy)

Infrastruktur pengujian E2E pada repositori **Official Statistics Lanjutan (OSL)** dirancang dengan filosofi **Opaque-Box (Black-Box), Requirement-Driven, and Mathematically Grounded Verification**. Pengujian tidak menguji implementasi internal pembuat kode (generator logic), melainkan menguji kepatuhan artefak keluaran terhadap kontrak data, skema baku, ketepatan matematika BPS, dan batasan infrastruktur.

### Prinsip Utama Pengujian:
1. **Opaque-Box Verification**: Seluruh unit materi (`internal/lessons/chapter-XX/*.json`), modul ajar terkompilasi (`open/chapters/chapter-XX.html`), dan peta konsep (`internal/mindmaps/*.html`) diuji melalui antarmuka dan spesifikasi yang dapat diobservasi (observables: struktur JSON, formula LaTeX, sitasi sumber, elemen DOM HTML, dan nilai numerik).
2. **Requirement-Driven & Strict Grounding**: Berlandaskan pada hierarki sumber otoritatif:
   $$\text{Silabus / RPS} > \text{Slide Dosen Pengampu} > \text{Publikasi Resmi BPS} > \text{Soal Ujian Riil} > \text{Suplemen Eksternal}$$
   Setiap formula dan klaim wajib memuat sitasi berformat `[nama-file, slide/hal. N]` atau tanda eksplisit `[SUPLEMEN]`.
3. **Deterministic Mathematical Oracles**: Formula dan kalkulasi diuji terhadap *oracle* komputasi Python independen berbasis definisi resmi BPS dan naskah ujian resmi UAS 2022/2023.
4. **Offline Self-Containment (Zero Remote Dependency)**: Seluruh berkas HTML pembelajaran dan visualisasi wajib beroperasi 100% mandiri secara offline tanpa memanggil pustaka remote (CDN, Web Fonts, skrip eksternal).
5. **Zero Host Mutation**: Seluruh pengujian dieksekusi di dalam virtual environment lokal melalui `uv run python` tanpa memodifikasi sistem operasi host atau menginstal paket global.
6. **Progressive Testability & Lifecycle Grace**: Suite pengujian mendukung siklus hidup bertahap (Milestone M1 s.d. M7). Bila suatu modul pelajaran belum diimplementasikan oleh agen pekerja (*worker*), pengujian melaporkan status `PENDING` secara anggun tanpa menyebabkan kegagalan palsu (*false failure*), namun menerapkan validasi ketat (*hard assertion*) pada seluruh komponen yang telah aktif.

---

## 2. Metodologi Pengujian 4-Tier (4-Tier Test Suite)

Arsitektur pengujian diorganisasikan ke dalam 4 tingkatan (*tiers*) komprehensif:

```
+-----------------------------------------------------------------------------------+
| TIER 1: Category-Partition & Feature Coverage (39 Konsep Silabus + 8 Suplemen)   |
|         - Schema validation per lesson JSON (point_id, theory, pitfalls, code)    |
|         - Grounding & citation format regex [file, slide/hal. N]                  |
|         - Lesson compilation status and tracking synchronization                  |
+-----------------------------------------------------------------------------------+
                                          |
+-----------------------------------------------------------------------------------+
| TIER 2: Boundary Value Analysis (BVA) & Edge Conditions                           |
|         - 10 kondisi batas kritis (MMR 100.000, Ubinan 1.600, Batas 35 Jam,      |
|           GKM 2.100 kkal, Laspeyres Berantai, Pembagi FGT n, APK > 100%, dll.)     |
+-----------------------------------------------------------------------------------+
                                          |
+-----------------------------------------------------------------------------------+
| TIER 3: Pairwise & Cross-Feature Integration                                      |
|         - Kemiskinan FGT vs Kurva Lorenz/Gini (Invariansi Skala Pendapatan)       |
|         - Ketenagakerjaan vs Partisipasi Pendidikan (PUK vs APS vs Informal)       |
|         - Nilai Tukar Petani (NTP) vs Inflasi Perdesaan (Dinamika IKRT vs BPPBM)  |
|         - Perdagangan Luar Negeri: FOB vs CIF, Merchanting SNA 2008, ToT          |
+-----------------------------------------------------------------------------------+
                                          |
+-----------------------------------------------------------------------------------+
| TIER 4: Real-World Workload & Historical Exam Calculations                        |
|         - Rekonstruksi Soal UAS 2022/2023 (Tabel IHK, Tabel NTP, Esai Naker,     |
|           Ubinan Padi, ISP Karet, ToT, Perhotelan, Gini Kuintil Slide 39)        |
+-----------------------------------------------------------------------------------+
                                          |
+-----------------------------------------------------------------------------------+
| OFFLINE & ZERO MUTATION CHECK: Scanning HTMLs for 0 remote CDNs / HTTP links      |
+-----------------------------------------------------------------------------------+
```

---

## 3. Inventarisasi Fitur Lengkap (Complete Feature Inventory)

Total **47 Fitur** yang mencakup **39 Konsep Inti Silabus** dan **8 Fitur Tambahan Resmi BPS (EXT-1 s.d. EXT-8)** ditambah **1 Fitur Integrasi Workspace (EXT-9)**:

| # | ID Fitur | Pertemuan | Nama Konsep / Indikator | Milestone | Rujukan Sumber Primer |
|---|---|---|---|---|---|
| 1 | `8.1.1` | P8 | Konsep Kemiskinan Absolut dan Relatif | M1 | `[Pertemuan 8...pptx, slide 4-9]` |
| 2 | `8.1.2` | P8 | Garis Kemiskinan Makanan dan Non-Makanan | M1 | `[Pertemuan 8...pptx, slide 14-16]` |
| 3 | `8.1.3` | P8 | Metodologi Cost of Basic Needs BPS | M1 | `[Pertemuan 8...pptx, slide 14-19]` |
| 4 | `8.2.1` | P8 | Headcount Index P0 | M1 | `[Pertemuan 8...pptx, slide 20-21]` |
| 5 | `8.2.2` | P8 | Poverty Gap Index P1 | M1 | `[Pertemuan 8...pptx, slide 20, 22]` |
| 6 | `8.2.3` | P8 | Poverty Severity Index P2 | M1 | `[Pertemuan 8...pptx, slide 20, 23]` |
| 7 | `8.3.1` | P8 | Kurva Lorenz dan Koefisien Gini | M1 | `[Pertemuan 8...pptx, slide 27, 38-41]` |
| 8 | `8.3.2` | P8 | Kriteria Ketimpangan Bank Dunia | M1 | `[Pertemuan 8...pptx, slide 34, 37]` |
| 9 | `9.1.1` | P9 | Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja | M2 | `[Pertemuan 9...pptx, slide 5-12]` |
| 10 | `9.1.2` | P9 | Tingkat Partisipasi Angkatan Kerja TPAK | M2 | `[Pertemuan 9...pptx, slide 13-14]` |
| 11 | `9.1.3` | P9 | Tingkat Pengangguran Terbuka TPT | M2 | `[Pertemuan 9...pptx, slide 15-16]` |
| 12 | `9.1.4` | P9 | Setengah Penganggur vs Pekerja Paruh Waktu | M2 | `[Pertemuan 9...pptx, slide 17-20]` |
| 13 | `9.2.1` | P9 | Angka Partisipasi Murni APM dan Kasar APK | M2 | `[Pertemuan 9...pptx, slide 66-71]` |
| 14 | `9.2.2` | P9 | Angka Partisipasi Sekolah APS | M2 | `[Pertemuan 9...pptx, slide 62-65]` |
| 15 | `10.1.1` | P10 | Angka Kematian Ibu AKI MMR | M3 | `[Pertemuan 10...pptx, slide 12-16]` |
| 16 | `10.1.2` | P10 | Angka Kematian Bayi AKB dan Balita AKABA | M3 | `[Pertemuan 10...pptx, slide 18-23]` |
| 17 | `10.1.3` | P10 | Angka Kematian Neo-Natal NMR | M3 | `[Pertemuan 10...pptx, slide 24-25]` |
| 18 | `10.2.1` | P10 | Angka Kesakitan Morbiditas | M3 | `[Pertemuan 10...pptx, slide 30, 38]` & `[SUPLEMEN]` |
| 19 | `10.2.2` | P10 | Imunisasi Dasar Lengkap IDL | M3 | `[Pertemuan 10...pptx, slide 40-42]` |
| 20 | `11.1.1` | P11 | Kerangka Sampel Area KSA Padi | M4 | `[Pertemuan 11...pdf, slide 10, 13-17]` |
| 21 | `11.1.2` | P11 | Metode Ubinan Produktivitas | M4 | `[Pertemuan 11...pdf, slide 10, 18-20]` |
| 22 | `11.1.3` | P11 | Survei Konversi Gabah ke Beras SKGB | M4 | `[Pertemuan 11...pdf, slide 10, 22-23]` |
| 23 | `11.2.1` | P11 | Survei Industri Besar dan Sedang IBS | M4 | `[Pertemuan 11...pdf, slide 24-28]` |
| 24 | `11.2.2` | P11 | Survei Industri Mikro dan Kecil IMK | M4 | `[Pertemuan 11...pdf, slide 24, 28]` & `[SUPLEMEN]` |
| 25 | `12.1.1` | P12 | Margin Perdagangan dan Pengangkutan MPP | M5 | `[Pertemuan 12...pdf, slide 4-6]` |
| 26 | `12.1.2` | P12 | Survei Pola Distribusi Perdagangan Poldis | M5 | `[Pertemuan 12...pdf, slide 6-8]` |
| 27 | `12.2.1` | P12 | IHK Rumus Modified Laspeyres | M5 | `[Pertemuan 12...pdf, slide 14-16]` |
| 28 | `12.2.2` | P12 | Tiga Laju Inflasi BPS mtom yony ytd | M5 | `[Pertemuan 12...pdf, slide 19-21]` |
| 29 | `12.2.3` | P12 | Disagregasi Inflasi Inti Bergejolak Administered | M5 | `[Pertemuan 12...pdf, slide 15, 18]` |
| 30 | `12.3.1` | P12 | Konsep dan Rasio NTP It per Ib | M5 | `[Pertemuan 12...pdf, slide 31-37]` |
| 31 | `12.3.2` | P12 | Nilai Tukar Usaha Petani NTUP | M5 | `[Pertemuan 12...pdf, slide 38-39]` |
| 32 | `12.3.3` | P12 | Lima Subsektor Penyusun NTP | M5 | `[Pertemuan 12...pdf, slide 31, 36]` |
| 33 | `13.1.1` | P13 | Valuasi Ekspor Impor FOB vs CIF | M6 | `[Pertemuan 13...pdf, slide 5-7]` |
| 34 | `13.1.2` | P13 | Barang Dagangan Tanpa Masuk Pabean Merchanting | M6 | `[Pertemuan 13...pdf, slide 5]` |
| 35 | `13.1.3` | P13 | Net Barter Terms of Trade NBToT | M6 | `[Pertemuan 13...pdf, slide 8, 13-15]` |
| 36 | `13.1.4` | P13 | Gross Barter dan Income ToT | M6 | `[Pertemuan 13...pdf, slide 10, 13]` & `[SUPLEMEN]` |
| 37 | `13.2.1` | P13 | Definisi Wisman dan Wisnus | M6 | `[Pertemuan 13...pdf, slide 32-38]` |
| 38 | `13.2.2` | P13 | Tingkat Penghunian Kamar TPK Hotel | M6 | `[Pertemuan 13...pdf, slide 39-41]` |
| 39 | `13.2.3` | P13 | Rata-rata Lama Menginap Tamu RLMT | M6 | `[Pertemuan 13...pdf, slide 40-41]` |
| 40 | `EXT-1` | P9 | Klasifikasi Tenaga Kerja Formal vs Informal | M2 | `[Pertemuan 9...pptx, slide 24-28]` |
| 41 | `EXT-2` | P9 | Angka Melek Huruf (AMH 15+) & RLS | M2 | `[Pertemuan 9...pptx, slide 57-60]` |
| 42 | `EXT-3` | P10 | Antropometri & Stunting Z-Score Balita (TB/U) | M3 | `[Pertemuan 10...pptx, slide 48-61]` |
| 43 | `EXT-4` | P10 | Rumah Layak Huni & Kriteria Rumah Kumuh | M3 | `[Pertemuan 10...pptx, slide 62-89]` |
| 44 | `EXT-5` | P11 | Nilai Pekerjaan Konstruksi & IMB Konstruksi | M4 | `[Pertemuan 11...pdf, slide 50-58]` |
| 45 | `EXT-6` | P12 | Indeks Kemahalan Konstruksi (IKK) | M5 | `[Pertemuan 12...pdf, slide 22-29]` |
| 46 | `EXT-7` | P13 | Indeks Spesialisasi Perdagangan (ISP) & Siklus | M6 | `[Pertemuan 13...pdf, slide 10-11]` |
| 47 | `EXT-8` | P13 | Revealed Comparative Advantage (RCA) & Openness | M6 | `[Pertemuan 13...pdf, slide 9, 12]` |
| 48 | `EXT-9` | M7 | Workspace State Sync & Unified Pipeline Pass | M7 | `validate_workspace.py` & `test_pipeline.py` |

---

## 4. Ambang Batas Pengujian (Testing Thresholds)

Suite pengujian menerapkan batas kuantitatif rigor pada setiap tingkatan:

1. **Threshold Tier 1 (Coverage & Schema)**:
   - $\ge 5$ uji per kategori fitur:
     1. Keberadaan point_id pada registri kurikulum `internal/state/knowledge.json`.
     2. Validitas skema JSON pelajaran (8 field wajib: `point_id`, `title`, `importance`, `curriculum_alignment`, `grounding`, `theory`, `numerical_example`, `exam_pitfalls`).
     3. Kepatuhan regex sitasi presisi: `r'\[.*?, (?:slide|hal\.) \d+.*?\]'` atau `[SUPLEMEN]` atau `TIDAK ADA DI MATERI`.
     4. Kelengkapan LaTeX formula matematis baku pada bagian `theory`.
     5. Keberadaan jebakan dosen (*exam pitfalls*) minimal 1 entri per konsep.

2. **Threshold Tier 2 (Boundary Value Analysis)**:
   - $\ge 5$ kondisi batas kritis per bab / kelompok indikator:
     1. Rasio kematian maternal (AKI): wajib per 100.000 KH vs anak per 1.000 KH.
     2. Ubinan plot $2,5\text{ m} \times 2,5\text{ m}$: faktor pengali 1.600 (kg/ha), 16 (ku/ha), 1.6 (ton/ha).
     3. Ambang batas 35 jam kerja: klasifikasi setengah penganggur vs pekerja paruh waktu, pembagi adalah Penduduk Bekerja ($PB$).
     4. Garis Kemiskinan Makanan (GKM): patokan 2.100 kkal/kapita/hari, 52 komoditas makanan.
     5. Modified Laspeyres IHK: formula berantai relatif harga $P_t / P_{t-1}$ berbobot $W_{t-1}$.
     6. APK vs APM: $\text{APM} \le 100\%$ dan $\text{APM} \le \text{APK}$, sedangkan $\text{APK}$ dapat $>100\%$.
     7. FGT divisor: pembagi populasi $n$, bukan jumlah miskin $q$.
     8. Inversi ToT: $\text{GBToT} = (Q_m/Q_x) \times 100$ vs $\text{NBToT} = (P_x/P_m) \times 100$.
     9. TPK Hotel: pembagi malam kamar tersedia ($\text{kamar} \times \text{hari operasional}$).
     10. ISP rentang $[-1, +1]$ dan 4 kuadran siklus produk.

3. **Threshold Tier 3 (Cross-Feature Pairwise Interactions)**:
   - 4 suite interaksi lintas modul:
     1. Kemiskinan vs Ketimpangan (Invariansi Kurva Lorenz terhadap penggandaan skala pengeluaran).
     2. Ketenagakerjaan vs Pendidikan (Status sekolah pada PUK vs APS 4 kelompok umur).
     3. NTP vs Inflasi Perdesaan (Dekomposisi indeks harga dibayar petani menjadi IKRT dan BPPBM).
     4. Perdagangan Luar Negeri: Sinkronisasi valuasi ekspor (FOB) vs impor BPS (CIF) vs BOP (FOB) dan Income ToT.

4. **Threshold Tier 4 (Real-World Historical Exam Scenarios)**:
   - 9 skenario kalkulasi riil dari Naskah Resmi UAS 2022/2023 & Slide Dosen:
     1. Gini Kuintil Slide 39: $G = 0,3770$, 40% terbawah $= 17,27\% \to$ Rendah.
     2. FGT Data 20 Sampel ($z=600.000, q=5$): $P_0 = 25,00\%, P_1 = 6,67\%, P_2 = 2,29\%$.
     3. UAS 2022/2023 Esai 1 Naker: $\text{TPAK} = 64,29\%, \text{TPT} = 22,22\%, \text{TSP} = 14,29\%$.
     4. UAS 2022/2023 Esai 2a Ubinan: $4,5\text{ kg} \to 7.200\text{ kg/ha} = 72\text{ ku/ha} = 7,2\text{ ton/ha}$.
     5. UAS 2022/2023 Esai 2b.1 Tabel IHK: $\text{IHK Mei 2023} = 114,84, \text{y-to-d} = 1,10\%, \text{y-on-y} = 4,01\%$.
     6. UAS 2022/2023 Esai 2b.3 Tabel NTP: $\text{NTP Apr} = 110,58, \text{NTUP Apr} = 110,92, I_{t\text{ Mei}} = 128,61, \text{NTP Mei} = 110,20, \text{Inflasi Des} = 0,40\%$.
     7. UAS 2022/2023 PG Ekspor-Impor: $\text{ISP Karet} = 0,36$ (Tahap Perluasan Ekspor), $\text{ISP} = -0,36$ (Substitusi Impor), $\text{ToT} = 105$.
     8. Statistik Perhotelan: $\text{TPK} = 60,00\%, \text{RLMT} = 2,50\text{ malam}$.
     9. Konstruksi BPS: Nilai Pekerjaan Bersih $NK = (NP - NS) \times \%NR = 6,4\text{ Miliar}$.

5. **Threshold Offline & Zero Mutation**:
   - 0 tautan `http://` atau `https://` ke CDN eksternal pada berkas HTML di `open/` dan `internal/mindmaps/`.
   - 100% eksekusi menggunakan `uv run python`.

---

## 5. Cara Menjalankan Pengujian

Eksekusi suite pengujian dilakukan melalui perintah standar:

```bash
uv run python tests/test_e2e_modules.py
```

Untuk menjalankan seluruh pipeline (pipeline audit dan modul E2E):
```bash
uv run python tests/test_pipeline.py
uv run python tests/test_e2e_modules.py
```
