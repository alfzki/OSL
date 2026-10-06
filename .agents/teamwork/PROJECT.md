# Project: OSL Post-UTS Comprehensive Learning Modules

## Architecture
- **Curriculum & Core Engine**: Study Assistant Suite (`.agents/skills/study-*`) managing state (`internal/state/knowledge.json`, `internal/state/progress.json`).
- **Lesson Unit Architecture**: Structured JSON per concept point at `internal/lessons/chapter-XX/<point-id>-<slug>.json` conforming to `study-teach` schema.
- **Chapter Compilation & Publishing**: `build_chapter_lecture.py` compiling individual JSON units into markdown (`chapter-XX.md`) and offline-capable HTML (`open/chapters/chapter-XX.html`).
- **Quality & Audit Assurance**: `audit_chapter.py` verifying against reference text (`internal/textbook/chapter-XX.md`), `verify_html.py` verifying offline zero-dependency HTML, and Python numerical verification scripts verifying all calculations.
- **Public Artifacts & Dashboards**: `build_dashboard.py` updating `open/dashboard.html` and `build_mindmap.py` compiling interactive mindmaps `internal/mindmaps/book.html` and `chapter-XX.html`.
- **E2E & Pipeline Testing**: `tests/test_pipeline.py` and `validate_workspace.py` asserting 100% workspace compliance and non-regression.

## Feature Inventory
| # | Feature ID | Name | Description | Milestone | Source |
|---|------------|------|-------------|-----------|--------|
| 1 | 8.1.1 | Konsep Kemiskinan Absolut dan Relatif | Konsep garis kemiskinan, pendekatan kebutuhan dasar (CBN), absolut vs relatif | M1 | survey |
| 2 | 8.1.2 | Garis Kemiskinan Makanan dan Non-Makanan | GKM (patokan 2100 kkal, 52 komoditas) & GKNM (komoditas bukan makanan) | M1 | survey |
| 3 | 8.1.3 | Metodologi Cost of Basic Needs BPS | Penentuan komoditas patokan, pembobotan pengeluaran, survei Susenas | M1 | survey |
| 4 | 8.2.1 | Headcount Index P0 | Persentase penduduk miskin terhadap total penduduk | M1 | survey |
| 5 | 8.2.2 | Poverty Gap Index P1 | Indeks kedalaman kemiskinan, rata-rata kesenjangan pengeluaran thd GK | M1 | survey |
| 6 | 8.2.3 | Poverty Severity Index P2 | Indeks keparahan kemiskinan, ketimpangan di antara penduduk miskin | M1 | survey |
| 7 | 8.3.1 | Kurva Lorenz dan Koefisien Gini | Formulasi trapesium diskrit BPS, kurva kumulatif populasi vs pengeluaran | M1 | survey |
| 8 | 8.3.2 | Kriteria Ketimpangan Bank Dunia | Distribusi 40% terbawah: <12% tinggi, 12-17% sedang, >17% rendah | M1 | survey |
| 9 | 9.1.1 | Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja | Kerangka ICLS 13, batasan PUK (15+), BUK (<15), AK, BAK | M2 | survey |
| 10 | 9.1.2 | Tingkat Partisipasi Angkatan Kerja TPAK | Rasio AK thd PUK, analisis gender dan wilayah | M2 | survey |
| 11 | 9.1.3 | Tingkat Pengangguran Terbuka TPT | Rasio penganggur terbuka thd total AK, 4 kategori penganggur BPS | M2 | survey |
| 12 | 9.1.4 | Setengah Penganggur vs Pekerja Paruh Waktu | Batas 35 jam kerja, pembagi Penduduk Bekerja (PB), voluntary vs involuntary | M2 | survey |
| 13 | 9.2.1 | Angka Partisipasi Murni APM dan Kasar APK | Definisi, formula per jenjang (SD, SMP, SMA), APK > 100% | M2 | survey |
| 14 | 9.2.2 | Angka Partisipasi Sekolah APS | Partisipasi berdasarkan kelompok umur resmi (7-12, 13-15, 16-18, 19-24) | M2 | survey |
| 15 | 10.1.1 | Angka Kematian Ibu AKI MMR | Kematian ibu per 100.000 kelahiran hidup, penyebab maternal | M3 | survey |
| 16 | 10.1.2 | Angka Kematian Bayi AKB dan Balita AKABA | IMR (per 1.000 KH), U5MR (per 1.000 KH), CMR anak 1-4 tahun | M3 | survey |
| 17 | 10.1.3 | Angka Kematian Neo-Natal NMR | Kematian bayi usia 0-28 hari per 1.000 kelahiran hidup | M3 | survey |
| 18 | 10.2.1 | Angka Kesakitan Morbiditas | Persentase penduduk mengalami keluhan kesehatan & terganggu aktivitas [SUPLEMEN] | M3 | survey |
| 19 | 10.2.2 | Imunisasi Dasar Lengkap IDL | Paket HB0, BCG, DPT-HB-Hib, Polio, Campak pada bayi usia 0-11 bulan | M3 | survey |
| 20 | 11.1.1 | Kerangka Sampel Area KSA Padi | Stratifikasi lahan, segmen 300mx300m, subsegmen 100mx100m, fase amatan | M4 | survey |
| 21 | 11.1.2 | Metode Ubinan Produktivitas | Plot 2.5m x 2.5m, multiplier 1600 (kg/petak ke kg/ha), konversi ku/ha dan ton/ha | M4 | survey |
| 22 | 11.1.3 | Survei Konversi Gabah ke Beras SKGB | Angka konversi GKP ke GKG (83.38%), GKG ke Beras (64.02%) | M4 | survey |
| 23 | 11.2.1 | Survei Industri Besar dan Sedang IBS | Definisi tenaga kerja >= 20 orang, direktori industri, nilai tambah | M4 | survey |
| 24 | 11.2.2 | Survei Industri Mikro dan Kecil IMK | Batasan TK mikro 1-4, kecil 5-19, karakteristik informal industri [SUPLEMEN] | M4 | survey |
| 25 | 12.1.1 | Margin Perdagangan dan Pengangkutan MPP | Rasio komparasi harga produsen ke konsumen, formula multiplikatif BPS | M5 | survey |
| 26 | 12.1.2 | Survei Pola Distribusi Perdagangan Poldis | Pemetaan rantai pasok komoditas strategis produsen s.d. konsumen akhir | M5 | survey |
| 27 | 12.2.1 | IHK Rumus Modified Laspeyres | Formulasi berantai relatif harga, pembobot konsumsi dasar, SBH 2018/2022 | M5 | survey |
| 28 | 12.2.2 | Tiga Laju Inflasi BPS mtom yony ytd | Perhitungan m-to-m, y-on-y, y-to-d, penentuan periode dasar pembanding | M5 | survey |
| 29 | 12.2.3 | Disagregasi Inflasi Inti Bergejolak Administered | Komponen inflasi inti (core), volatile foods, administered prices | M5 | survey |
| 30 | 12.3.1 | Konsep dan Rasio NTP It per Ib | Rasio indeks harga diterima vs dibayar petani, interpretasi kesejahteraan | M5 | survey |
| 31 | 12.3.2 | Nilai Tukar Usaha Petani NTUP | Rasio It thd BPPBM (Biaya Produksi & Penambahan Barang Modal) | M5 | survey |
| 32 | 12.3.3 | Lima Subsektor Penyusun NTP | Tanaman Pangan, Hortikultura, Perkebunan Rakyat, Peternakan, Perikanan | M5 | survey |
| 33 | 13.1.1 | Valuasi Ekspor Impor FOB vs CIF | Ekspor FOB, Impor CIF, dokumen PEB & PIB, konversi mata uang | M6 | survey |
| 34 | 13.1.2 | Barang Dagangan Tanpa Masuk Pabean Merchanting | Definisi merchanting goods SNA 2008, transaksi barang tanpa lintas batas fisik | M6 | survey |
| 35 | 13.1.3 | Net Barter Terms of Trade NBToT | Rasio indeks harga ekspor thd indeks harga impor (Px / Pm * 100) | M6 | survey |
| 36 | 13.1.4 | Gross Barter dan Income ToT | GBToT (Qm / Qx * 100) [SUPLEMEN], Income ToT (NBToT * Qx / 100) | M6 | survey |
| 37 | 13.2.1 | Definisi Wisman dan Wisnus | Kriteria UNWTO: durasi < 1 tahun, bukan bekerja di lokasi tujuan | M6 | survey |
| 38 | 13.2.2 | Tingkat Penghunian Kamar TPK Hotel | Rasio malam kamar terpakai thd malam kamar tersedia (persen) | M6 | survey |
| 39 | 13.2.3 | Rata-rata Lama Menginap Tamu RLMT | Total malam tamu menginap dibagi total tamu datang (satuan hari/malam) | M6 | survey |
| 40 | EXT-1 | Klasifikasi Tenaga Kerja Formal vs Informal | Kriteria status pekerjaan dan jenis usaha BPS (P9) | M2 | survey |
| 41 | EXT-2 | Angka Melek Huruf (AMH 15+) & Rata-rata Lama Sekolah (RLS) | Indikator IPM komposit pendidikan (P9) | M2 | survey |
| 42 | EXT-3 | Antropometri & Stunting Z-Score Balita | Standar WHO & Kemenkes untuk gizi balita TB/U (P10) | M3 | survey |
| 43 | EXT-4 | Rumah Layak Huni & Kriteria Rumah Kumuh | 4 kriteria ketahanan bangunan, sanitasi, air bersih, luas lantai (P10) | M3 | survey |
| 44 | EXT-5 | Nilai Pekerjaan Konstruksi & IMB | NK = (NP - NS) * %NR dan Indeks Masalah Bisnis Konstruksi (P11) | M4 | survey |
| 45 | EXT-6 | Indeks Kemahalan Konstruksi (IKK) | Metode Country Product Dummy (CPD) untuk DAU fiskal (P12) | M5 | survey |
| 46 | EXT-7 | Indeks Spesialisasi Perdagangan (ISP) & Siklus Produk | ISP = (X - M) / (X + M), tahapan introduksi s.d. re-impor (P13) | M6 | survey |
| 47 | EXT-8 | Revealed Comparative Advantage (RCA) & Derajat Keterbukaan | Balassa Index RCA dan Trade Openness Ratio ((X+M)/PDRB) (P13) | M6 | survey |
| 48 | EXT-9 | Workspace State Sync & Unified Pipeline Pass | Sinkronisasi knowledge.json, dashboard.html, mindmaps, dan test_pipeline | M7 | survey |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Pertemuan 8: Kemiskinan & Ketimpangan | 8 konsep (8.1.1-8.3.2): CBN, GKM, GKNM, FGT P0/P1/P2, Lorenz, Gini, Bank Dunia | none | DONE |
| M2 | Pertemuan 9: Ketenagakerjaan & Pendidikan | 6 konsep (9.1.1-9.2.2) + EXT-1, EXT-2: ICLS 13, TPAK, TPT, TSP/TPPW, APK/APM/APS | none | DONE |
| M3 | Pertemuan 10: Kesehatan & SDGs 3 | 5 konsep (10.1.1-10.2.2) + EXT-3, EXT-4: AKI, AKB, AKABA, NMR, Morbiditas, IDL | none | IN_PROGRESS |
| M4 | Pertemuan 11: Statistik Produksi & KSA | 5 konsep (11.1.1-11.2.2) + EXT-5: KSA Padi, Ubinan, SKGB, IBS, IMK | none | DONE |
| M5 | Pertemuan 12: Perdagangan, IHK & NTP | 8 konsep (12.1.1-12.3.3) + EXT-6: MPP, Poldis, IHK Laspeyres, Inflasi, NTP, NTUP | none | DONE |
| M6 | Pertemuan 13: Ekspor-Impor, ToT & Pariwisata | 7 konsep (13.1.1-13.2.3) + EXT-7, EXT-8: FOB/CIF, Merchanting, ToT, Wisman/Wisnus, TPK, RLMT | none | DONE |
| M7 | Final E2E Integration, Workspace Sync & Verification | Sinkronisasi state, rebuild dashboard, rebuild mindmaps, 100% pass E2E & test_pipeline | M1, M2, M3, M4, M5, M6 | PLANNED |

## Interface Contracts
### Lesson JSON ↔ Chapter Compilation
- Input unit path: `internal/lessons/chapter-XX/<point-id>-<slug>.json`
- Schema:
  - `point_id`: string (e.g., "8.1.1")
  - `title`: string
  - `importance`: "高" | "中" | "低"
  - `curriculum_alignment`: object with `pertemuan`, `silabus_topic`, `bps_subject`
  - `grounding`: object with `primary_sources` (list of `{"file": "...", "slide_or_page": "...", "content": "..."}`), `supplemental_sources` (list), `coverage_status` ("COVERED" | "SUPPLEMENTED" | "NOT_IN_MATERIAL")
  - `theory`: object with `intuition`, `bps_definition`, `boundary_conditions`, `formula_latex`
  - `numerical_example`: object with `problem_statement`, `data_table`, `step_by_step_solution`, `python_verification_code`, `expected_output`
  - `exam_pitfalls`: list of objects `{"trap_description": "...", "common_mistake": "...", "safe_strategy": "..."}`
- Output chapter compiled files:
  - Markdown: `internal/lessons/chapter-XX/chapter-XX.md`
  - HTML: `open/chapters/chapter-XX.html` (zero-dependency offline)
- Audit report: `internal/reports/chapter-XX-audit.json`

### Lesson Generation ↔ Question Bank
- Function: `python .agents/skills/study-quiz/scripts/bank.py . add-lecture <lecture.json>`
- Adds practice questions to `question-bank/by-point/<point-id>.json` and global bank.

### State Synchronization Contract
- `internal/state/knowledge.json`: update `status` ("已讲解"), `mastery` (4 or 5), `note` ("Lengkap terverifikasi")
- `internal/state/progress.json`: update `current_chapter`, `current_point`, `next_action`
- `open/dashboard.html`: rebuilt via `python .agents/skills/study-assistant/scripts/build_dashboard.py .`
- Mindmaps: rebuilt via `python .agents/skills/study-mindmap/scripts/build_mindmap.py internal/state/knowledge.json --book` and `--chapter XX`

## Code Layout
- Reference Textbooks: `internal/textbook/chapter-08.md` through `chapter-13.md` (copied/linked from `extracted/`)
- Lessons Units: `internal/lessons/chapter-08/` through `chapter-13/`
- Compiled Chapter Modules: `open/chapters/chapter-08.html` through `chapter-13.html`
- Mindmaps: `internal/mindmaps/book.html`, `chapter-08.html` through `chapter-13.html`
- Question Bank: `question-bank/`
- State: `internal/state/knowledge.json`, `internal/state/progress.json`
- Tests: `tests/test_pipeline.py`, `tests/test_e2e_modules.py`
