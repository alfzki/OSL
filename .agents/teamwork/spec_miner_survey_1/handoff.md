# 5-Component Handoff Report: Specification Mining Survey (Pertemuan 8 s.d. 13)

**Author**: Survey Agent 1 (Specification Miner)  
**Recipient**: Parent Agent (ID: `71881272-af99-4fce-b62d-35b299508d76`)  
**Working Directory**: `/home/alfzki/Documents/OSL/.agents/teamwork/spec_miner_survey_1/`  
**Date**: 2026-09-29  
**Type**: Hard Handoff (Task Complete)  

---

## 1. Observation

1. **Struktur Kurikulum dan Silabus OSL**:
   - `materials/syllabus/Tiodora_3SI1_Kontrak Perkuliahan OSL Genap TA 2025 2026 Politeknik Statistika STIS.pptx` (ekstraksi: `extracted/Tiodora_3SI1_Kontrak_Perkuliahan_OSL_Genap_TA_2025_2026_Politeknik_Statistika_STIS.md`, slide 11) menetapkan 6 pertemuan pasca-UTS:
     * Pekan 9 (Pertemuan 8): Indikator Sosial (Kemiskinan & Ketimpangan)
     * Pekan 10 (Pertemuan 9): Indikator Sosial (Ketenagakerjaan & Pendidikan)
     * Pekan 11 (Pertemuan 10): Indikator Sosial (Kesehatan & SDGs 3)
     * Pekan 12 (Pertemuan 11): Indikator Ekonomi (Statistik Produksi & KSA)
     * Pekan 13 (Pertemuan 12): Indikator Ekonomi (Perdagangan, IHK, NTP)
     * Pekan 14 (Pertemuan 13): Indikator Ekonomi (Ekspor-Impor, ToT, Pariwisata)
2. **Kesesuaian State Workspace**:
   - `internal/state/knowledge.json` mendefinisikan 39 poin konsep hierarkis:
     * Bab 8: 8.1.1 s.d. 8.3.2 (8 poin konsep)
     * Bab 9: 9.1.1 s.d. 9.2.2 (6 poin konsep)
     * Bab 10: 10.1.1 s.d. 10.2.2 (5 poin konsep)
     * Bab 11: 11.1.1 s.d. 11.2.2 (5 poin konsep)
     * Bab 12: 12.1.1 s.d. 12.3.3 (8 poin konsep)
     * Bab 13: 13.1.1 s.d. 13.2.3 (7 poin konsep)
     * Total: $8 + 6 + 5 + 5 + 8 + 7 = 39$ poin konsep.
   - Eksekusi `uv run python .agents/skills/study-assistant/scripts/validate_workspace.py .` menghasilkan:
     `OK: state files in internal/state (39 points) conform to the contract` (Exit code: 0).
3. **Bukti Tekstual Slide & Handout**:
   - Pertemuan 8: `extracted/Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md` (44 slide), memuat formula FGT $P_\alpha$ (slide 20-23) dan formula Gini diskrit trapesium $G = 1 - \sum f_i(Y_i + Y_{i-1})$ (slide 38-39).
   - Pertemuan 9: `extracted/Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md` (75 slide) dan `materials/notes/Kuesioner SAK.AGS25-AK.pdf` (27 hal), memuat standar ICLS 13 (slide 10-12), batas 35 jam setengah penganggur (slide 17-18) dan paruh waktu (slide 19-20), serta formula APK (slide 66), APM (slide 69), dan APS (slide 63).
   - Pertemuan 10: `extracted/Pertemuan_10_Indikator_Kesehatan.md` (91 slide), memuat formula AKI dengan konstanta $100.000$ (slide 13), AKB konstanta $1.000$ (slide 26), AKABA (slide 19), NMR (slide 24), dan IDL (slide 41-42).
   - Pertemuan 11: `extracted/Pertemuan_11_OSL_Indikator_Ekonomi_(1)_Produksi.md` (59 slide), memuat KSA subsegmen amatan dan fase tanam (slide 13-17), formula produktivitas ubinan $2,5\text{ m} \times 2,5\text{ m} \times 16$ (slide 23), angka konversi SKGB (GKP ke GKG $83,38\%$, GKG ke Beras $64,02\%$) (slide 22-23), dan efisiensi IBS (slide 26-28).
   - Pertemuan 12: `extracted/Pertemuan_12_OSL_Indikator_Ekonomi_(2)_Perdagangan&Harga.md` (40 slide) dan `materials/notes/indeks-harga-konsumen-38-provinsi-di-indonesia-2025--2022-100-.pdf` (hal. 13-14), memuat MPP multiplikatif (slide 6), formula Modified Laspeyres IHK $I_t = \sum (P_{ti}/P_{t-1, i} \times W_{t-1, i})$ (slide 14 & publikasi IHK), 3 laju inflasi (slide 20), dan rasio NTP $I_t/I_b \times 100$ serta NTUP $I_t/\text{BPPBM} \times 100$ (slide 31, 38).
   - Pertemuan 13: `extracted/Pertemuan_13_OSL_Indikator_Ekonomi_(3)_X-M,_KTI,_Pariwisata.md` (43 slide), memuat valuasi FOB/CIF dan PEB/PIB (slide 6-7), merchanting goods SNA 2008 (slide 5), Net Barter ToT (slide 14), definisi Wisman/Wisnus UNWTO (slide 33-36), TPK hotel (slide 41), dan RLMT (slide 41).
4. **Fitur Ekstra yang Ditemukan di Luar 39 Konsep Utama**:
   - P9: Klasifikasi Tenaga Kerja Formal vs Informal (slide 24-28), Angka Melek Huruf (slide 57-60), dan RLS (slide 72-74).
   - P10: Antropometri Status Gizi Balita & Stunting Z-Score (slide 48-61), Rumah Tidak Layak Huni & Kriteria Rumah Kumuh (slide 62-89).
   - P11: Nilai Pekerjaan Konstruksi $NK = (NP - NS) \times \%NR$ (slide 50) dan Indeks Masalah Bisnis (IMB) Konstruksi (slide 52-58).
   - P12: Indeks Kemahalan Konstruksi (IKK) metode CPD untuk celah fiskal DAU (slide 22-29).
   - P13: Indeks Spesialisasi Perdagangan (ISP) siklus produk (slide 10-11), Revealed Comparative Advantage (RCA) (slide 12), Derajat Keterbukaan (*Trade Openness*) (slide 9), dan Indeks Konsentrasi Pasar Gini-Hirschman (slide 20).
5. **Hasil Eksekusi Pengujian**:
   - `uv run python tests/test_pipeline.py` lulus 100% (8 test suites passed).

---

## 2. Logic Chain

1. Dari Observasi 1 dan 2, kurikulum resmi pasca-UTS OSL terdiri dari tepat 6 pertemuan (Pertemuan 8 s.d. 13) yang terbagi menjadi 39 poin konsep terdaftar pada `internal/state/knowledge.json`.
2. Dari Observasi 3, dilakukan penelusuran (*deep probing*) terhadap setiap segmen teks pada repositori materi (`materials/slides/`, `materials/notes/`, `extracted/`). Hasilnya menunjukkan bahwa:
   - 36 konsep memiliki sumber rujukan langsung eksplisit pada slide perkuliahan dosen pengampu atau publikasi resmi BPS yang disertakan di repositori.
   - 3 konsep membutuhkan pelabelan eksplisit `[SUPLEMEN]` sesuai aturan grounding CLAUDE.md dan AGENTS.md, yaitu:
     * Poin 10.2.1 (*Angka Kesakitan / Morbiditas*): Slide 10 dan 51 hanya menyebutkan istilah secara kualitatif, sedangkan formula operasional matematisnya mengacu pada standar baku Susenas Kor BPS (`[SUPLEMEN: Standar Susenas BPS]`).
     * Poin 11.2.2 (*Survei Industri Mikro dan Kecil / IMK*): Slide 24-28 fokus menjabarkan IBS (tenaga kerja $\ge 20$), sehingga batasan tenaga kerja IMK (1-4 mikro, 5-19 kecil) diturunkan dari pedoman statistik industri BPS (`[SUPLEMEN: Standar Industri BPS]`).
     * Poin 13.1.4 (*Gross Barter Terms of Trade / GBToT*): Slide 13-15 menguraikan Net Barter ToT, sedangkan formula rasio kuantitas $GBToT = (Q_m / Q_x) \times 100$ berasal dari teori baku perdagangan internasional (`[SUPLEMEN: Teori Perdagangan Luar Negeri]`).
3. Dari Observasi 4, aturan Specification Miner mewajibkan penambangan fitur tambahan yang ditemukan selama penyelidikan agar tidak ada fitur yang terlewat. Sebanyak 8 kelompok fitur tambahan berhasil dipetakan ke dalam tabel inventarisasi fitur dan kondisi batas.
4. Dari Observasi 5, seluruh dependensi, format JSON, dan jalur sitasi telah divalidasi dengan test suite independen dan tidak menimbulkan regresi.

---

## 3. Caveats

- **Variasi Angka Dasar Survei Biaya Hidup (SBH)**: Pada slide Pertemuan 12, contoh perhitungan IHK sebagian besar menggunakan SBH 2018 ($2018=100$, 90 kota), sementara publikasi di `materials/notes/` telah memperbarui ke SBH 2022 ($2022=100$, 150 kota di 38 provinsi). Modul ajar yang akan diproduksi wajib menyajikan formulasi Modified Laspeyres yang berlaku universal untuk kedua tahun dasar tersebut dan mencatat perbedaan cakupan wilayahnya.
- **Satuan Pengukuran RLMT**: Slide 41 Pertemuan 13 mencantumkan notasi cetak `x 100%` pada baris RLMT, padahal definisi operasional resmi BPS untuk Rata-rata Lama Menginap Tamu bersatuan **hari/malam**, bukan persentase. Dalam laporan spesifikasi, hal ini telah dikoreksi dan ditandai sebagai catatan kritis.
- **Asumsi Zero Host Mutation**: Tidak ada paket Python atau sistem operasi baru yang diinstal selama investigasi; seluruh eksekusi mengandalkan lingkungan virtual yang telah ada via `uv run`.

---

## 4. Conclusion

- **Status Tugas**: Selesai Penuh (*Complete & Authoritative*).
- Seluruh 39 konsep silabus inti OSL (Pertemuan 8 s.d. 13) plus 8 fitur pelengkap telah selesai ditambang spesifikasinya, dipetakan sitasi presisi `[nama-file, slide/hal. N]`, dirumuskan formulanya dalam LaTeX, dan diinventarisasi syarat batas serta potensi jebakannya.
- Berkas laporan komprehensif telah ditulis di `/home/alfzki/Documents/OSL/.agents/teamwork/spec_miner_survey_1/survey_report.md`.
- Workspace telah tervalidasi memenuhi kontrak kurikulum (`internal/state/knowledge.json`), siap dilanjutkan ke tahap pembuatan modul belajar oleh `study-teach` dan bank soal oleh `study-quiz`.

---

## 5. Verification Method

Untuk memverifikasi temuan dan integritas laporan secara independen:

1. **Verifikasi Integritas Workspace & Skema State**:
   ```bash
   uv run python .agents/skills/study-assistant/scripts/validate_workspace.py .
   ```
   *Kriteria Lolos*: Mengembalikan kode exit 0 (`OK: state files in internal/state (39 points) conform to the contract`).

2. **Verifikasi Test Suite Pipeline**:
   ```bash
   uv run python tests/test_pipeline.py
   ```
   *Kriteria Lolos*: 8 pengujian integritas pipeline lulus 100% tanpa kegagalan.

3. **Inspeksi Berkas Hasil Survei**:
   Periksa keberadaan dan kelengkapan tabel pada berkas:
   - `/home/alfzki/Documents/OSL/.agents/teamwork/spec_miner_survey_1/survey_report.md`
   - `/home/alfzki/Documents/OSL/.agents/teamwork/spec_miner_survey_1/handoff.md`

4. **Kondisi Invalidasi (Invalidation Conditions)**:
   - Ada poin konsep dari ke-39 silabus yang tidak memiliki pasangan sitasi slide/publikasi.
   - Ditemukan formula resmi BPS yang tidak sesuai dengan teks rujukan primer.
   - Status suplemen eksternal tidak ditandai secara eksplisit dengan label `[SUPLEMEN]`.
