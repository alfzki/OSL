# 🎓 UAS Study Sprint Hub (Persiapan Ujian Akhir Semester)

Repository ini telah dikonfigurasi sebagai pusat persiapan belajar dan akselerasi **Ujian Akhir Semester (UAS)** menggunakan arsitektur **Antigravity Agent Skills**.

Sistem ini menggabungkan 4 kapabilitas utama:
1. **Analisis Pola & Prediksi Soal**: Menemukan pola soal tahun lalu dan memprediksi kisi-kisi prioritas tinggi.
2. **Paket Belajar & Latihan Interaktif Offline**: Membuat kuis interaktif HTML (Material 3/Metro), ringkasan formula/cheat sheet A4, dan mock exam.
3. **Pembelajaran Sistematis Per Bab**: Pembuatan modul kuliah bertahap, peta konsep interaktif, dan bank soal global.
4. **Validasi Pemahaman Mendalam**: Pengujian teknik Feynman dan buku evaluasi salah (*mistake book*).

---

## 🛠️ Daftar Skills yang Terpasang

Semua skill tersimpan di folder [`.agents/skills/`](file:///.agents/skills/):

| Skill | Sumber | Fungsi Utama & Kapan Digunakan |
|---|---|---|
| **`exam-sprint-builder`** | [GitHub Repo](https://github.com/dentar142/exam-sprint-builder) | Membuat paket belajar kilat *offline-first* (buka langsung via browser tanpa server): aplikasi kuis HTML instan, *one-page cheat sheet* A4, Obsidian study vault, dan simulasi UAS. |
| **`exam-forecast`** | [Anthropic MCP](https://mcpservers.org/agent-skills/anthropic/exam-forecast) | Analisis longitudinal soal UAS tahun-tahun sebelumnya untuk mendeteksi bobot materi, tipe soal favorit dosen, pola jebakan, dan memproyeksikan struktur soal UAS mendatang. |
| **`exam-question-predictor`** | [FindSkill.ai](https://findskill.ai/skills/education-learning/exam-question-predictor/) | Prediktor soal berbasis *Bloom's Taxonomy* & sinyal perkuliahan dosen untuk menyusun *Study Priority Matrix* (Must Study, Should Study, Quick Review, Skip). |
| **`study-assistant`** | [GitHub Repo](https://github.com/2362094903-ops/study-assistant-skills) | **Orchestrator Utama**: Mengatur kurikulum belajar per bab, melacak progres belajar lintas sesi (*session state*), dan mengelola alur belajar terstruktur. |
| **`study-teach`** | *Study Assistant Suite* | Menghasilkan modul ajar/catatan kuliah per poin konsep dengan penjelasan mendalam, penurunan rumus LaTeX, tabel, dan contoh soal teruji. |
| **`study-quiz`** | *Study Assistant Suite* | Generator kuis interaktif HTML MathJax dengan koreksi instan, bank soal global, dan buku catatan evaluasi salah (*mistake book*). |
| **`study-mindmap`** | *Study Assistant Suite* | Membuat visualisasi peta konsep (mind map) interaktif berbasis HTML mandiri dengan pewarnaan berdasarkan tingkat penguasaan materi. |
| **`study-feynman`** | *Study Assistant Suite* | Penguji pemahaman berbasis Teknik Feynman — AI bertindak sebagai pemula kritis yang menguji apakah Anda benar-benar paham suatu konsep tanpa menghafal. |
| **`study-img`** | *Study Assistant Suite* | Ekstraksi visual, OCR soal, transkripsi tulisan tangan, dan interpretasi diagram/grafik dari foto lembar ujian atau slide kuliah. |

---

## 📁 Struktur Direktori Workspace

```text
.
├── .agents/
│   └── skills/                       # Konfigurasi skill agent
│       ├── exam-sprint-builder/
│       ├── exam-forecast/
│       ├── exam-question-predictor/
│       ├── study-assistant/
│       ├── study-feynman/
│       ├── study-img/
│       ├── study-mindmap/
│       ├── study-quiz/
│       └── study-teach/
├── materials/                        # Tempat meletakkan materi kuliah Anda
│   ├── past-exams/                   # Kumpulan soal UAS / UTS / bank soal tahun lalu
│   ├── slides/                       # Slide kuliah (PPTX, PDF)
│   ├── notes/                        # Catatan kuliah, ringkasan, atau transkrip audio
│   └── syllabus/                     # Silabus mata kuliah, RPS, atau kisi-kisi resmi
├── forecasts/                        # Hasil analisis pola & prediksi soal UAS
├── output/                           # Hasil generate paket belajar (HTML kuis, cheat sheet, mind map)
├── pyproject.toml                    # Konfigurasi dependensi Python (dikelola via uv)
└── README.md
```

---

## 🚀 Alur Kerja Persiapan UAS (Step-by-Step Workflow)

### Tahap 1: Ingest Materi & Analisis Pola Soal
1. Letakkan silabus di [`materials/syllabus/`](file:///materials/syllabus/) dan soal tahun lalu di [`materials/past-exams/`](file:///materials/past-exams/).
2. Jalankan analisis pola ujian:
   > *"Tolong analisis soal-soal tahun lalu di `materials/past-exams/` dan buatkan exam forecast untuk mata kuliah [Nama Kuliah]."*
   *(Skill yang aktif: `exam-forecast`)*
3. Prediksi soal spesifik dan tentukan matriks prioritas:
   > *"Berdasarkan silabus dan materi yang paling ditekankan dosen, buatkan prediksi soal ujian dan Study Priority Matrix."*
   *(Skill yang aktif: `exam-question-predictor`)*

### Tahap 2: Pembelajaran Sistematis & Peta Konsep
1. Mulai sesi belajar modul per bab:
   > *"Mulai belajar materi dari `materials/slides/` bab 3, buatkan peta konsep dan modul penjelasannya."*
   *(Skill yang aktif: `study-assistant`, `study-mindmap`, `study-teach`)*
2. Buka file peta konsep HTML interaktif yang dihasilkan di folder `output/` untuk melihat perkembangan penguasaan materi.

### Tahap 3: Latihan Soal & Pembuatan Sprint Kit
1. Buat paket kuis interaktif atau cram kit lengkap:
   > *"Buatkan paket latihan sprint UAS untuk bab ini: buat kuis interaktif HTML dan cheat sheet rumus A4."*
   *(Skill yang aktif: `exam-sprint-builder`, `study-quiz`)*
2. Buka kuis `.html` langsung dengan double-click di browser untuk latihan soal dengan *instant feedback*.

### Tahap 4: Uji Pemahaman Mendalam (Teknik Feynman)
1. Uji pemahaman konsep krusial:
   > *"Saya ingin uji Feynman untuk konsep [Nama Konsep]. Anggap kamu pemula yang belum paham, uji pemahaman saya."*
   *(Skill yang aktif: `study-feynman`)*

---

## ⚙️ Lingkungan & Dependensi Teknis

Proyek ini telah dikonfigurasi dengan standar isolasi lingkungan:
- **Python**: Dikelola secara hermetis via [`uv`](https://docs.astral.sh/uv/) dengan virtual environment di `.venv`.
  - Paket pendukung: `pymupdf` (ekstraksi PDF), `python-pptx` (ekstraksi slide PPT), `beautifulsoup4`, `pillow`.
- **Node.js**: Tersedia untuk kompilasi HTML dan template rendering.
- **Offline First**: Semua output kuis, mind map, dan catatan dirancang dapat dibuka langsung (`file://`) tanpa memerlukan server backend.
