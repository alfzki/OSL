#!/usr/bin/env python3
"""Generate all 6 concept JSON files for Chapter 09: Ketenagakerjaan dan Pendidikan.
Follows dual-compatible schema: 8 root keys for test_e2e_modules.py and study-teach keys for build_chapter_lecture.py.
"""

import json
from pathlib import Path

CHAPTER_DIR = Path("internal/lessons/chapter-09")
CHAPTER_DIR.mkdir(parents=True, exist_ok=True)

LESSONS = [
    {
        "filename": "9.1.1-konsep-bekerja-minimal-1-jam-dan-angkatan-kerja.json",
        "point_id": "9.1.1",
        "title": "Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja",
        "importance": "高",
        "curriculum_alignment": {
            "pertemuan": 9,
            "silabus_topic": "Ketenagakerjaan dan Pendidikan",
            "bps_subject": "Statistik Ketenagakerjaan"
        },
        "grounding": {
            "primary_sources": [
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "4-20",
                    "content": "Kerangka ICLS 13, batasan Penduduk Usia Kerja (PUK >= 15 tahun), Bukan Usia Kerja (BUK < 15 tahun), konsep bekerja minimal 1 jam, Angkatan Kerja (AK), dan Bukan Angkatan Kerja (BAK)."
                },
                {
                    "file": "Kuesioner_SAK.AGS25-AK.md",
                    "slide_or_page": "15-22",
                    "content": "Rincian kegiatan seminggu yang lalu, batasan 1 jam berturut-turut untuk kegiatan ekonomi, dan penapisan sementara tidak bekerja."
                }
            ],
            "supplemental_sources": [],
            "coverage_status": "COVERED"
        },
        "theory": {
            "intuition": "Kerangka ketenagakerjaan membagi seluruh penduduk ke dalam piramida aktivitas ekonomi. Ambang batas 'bekerja minimal 1 jam tanpa putus dalam seminggu terakhir' diadopsi dari standar internasional ILO (ICLS 13) dengan filosofi inklusivitas: menangkap setiap sumbangan marginal terhadap produksi nasional barang dan jasa, sekecil apa pun jam kerjanya. Aturan prioritas menetapkan bahwa kegiatan ekonomi (bekerja atau mencari kerja) mengalahkan kegiatan non-ekonomi (sekolah atau mengurus rumah tangga).",
            "bps_definition": "Penduduk Usia Kerja (PUK) adalah seluruh penduduk berumur 15 tahun ke atas. PUK terbagi menjadi Angkatan Kerja (AK) dan Bukan Angkatan Kerja (BAK). Bekerja adalah kegiatan ekonomi yang dilakukan seseorang dengan maksud memperoleh atau membantu memperoleh pendapatan/keuntungan, paling sedikit 1 jam secara tidak terputus dalam seminggu terakhir. Bekerja juga mencakup pekerja keluarga tak dibayar (unpaid worker) dan mereka yang sementara tidak bekerja karena sakit, cuti, atau mogok.",
            "boundary_conditions": "1. Batas umur PUK di Indonesia sejak 1998 adalah >= 15 tahun (sebelumnya >= 10 tahun). Pekerja anak (< 15 tahun) tidak dimasukkan dalam statistik resmi PUK/AK.\n2. Bekerja minimal 1 jam harus dalam kurun waktu 7 hari terakhir (reference period).\n3. Pekerja yang sementara tidak bekerja (cuti sakit, cuti melahirkan, menunggu panen) tetap diklasifikasikan sebagai Bekerja, bukan Pengangguran.\n4. Persamaan identitas demografi ketenagakerjaan: PUK = AK + BAK = (Bekerja + Penganggur) + (Sekolah + Mengurus Rumah Tangga + Lainnya).",
            "formula_latex": "$$\\text{Populasi} = \\text{PUK} + \\text{BUK}, \\quad \\text{PUK} = \\text{AK} + \\text{BAK}, \\quad \\text{AK} = \\text{Bekerja} + \\text{Penganggur}$$"
        },
        "numerical_example": {
            "problem_statement": "Dalam suatu wilayah sensus terdapat total populasi 20.000.000 jiwa. Dari jumlah tersebut, penduduk berusia 0-14 tahun berjumlah 5.000.000 jiwa. Di antara penduduk usia 15 tahun ke atas, tercatat 9.500.000 orang aktif bekerja (termasuk 200.000 pekerja yang sedang cuti/sementara tidak bekerja), 500.000 orang sedang mencari pekerjaan secara aktif, 2.000.000 orang bersekolah penuh waktu, 2.500.000 orang mengurus rumah tangga tanpa kegiatan komersial, dan 500.000 orang lansia/penerima pensiun (lainnya). Hitunglah nilai PUK, AK, BAK, dan buktikan persamaan PUK = AK + BAK.",
            "data_table": "| Komponen Ketenagakerjaan | Jumlah Jiwa |\n|---|---|\n| Penduduk Berumur 0-14 Tahun (BUK) | 5.000.000 |\n| Penduduk Bekerja (termasuk cuti sementara) | 9.500.000 |\n| Pengangguran Terbuka (mencari kerja) | 500.000 |\n| Sekolah Penuh Waktu | 2.000.000 |\n| Mengurus Rumah Tangga | 2.500.000 |\n| Lainnya (Pensiunan/Lansia/Disabilitas) | 500.000 |",
            "step_by_step_solution": "1. Menghitung Penduduk Usia Kerja (PUK):\n   $$\\text{PUK} = \\text{Total Populasi} - \\text{BUK} = 20.000.000 - 5.000.000 = 15.000.000$$\n2. Menghitung Angkatan Kerja (AK):\n   $$\\text{AK} = \\text{Bekerja} + \\text{Pengangguran} = 9.500.000 + 500.000 = 10.000.000$$\n3. Menghitung Bukan Angkatan Kerja (BAK):\n   $$\\text{BAK} = \\text{Sekolah} + \\text{Mengurus RT} + \\text{Lainnya} = 2.000.000 + 2.500.000 + 500.000 = 5.000.000$$\n4. Verifikasi Identitas Neraca Tenaga Kerja:\n   $$\\text{AK} + \\text{BAK} = 10.000.000 + 5.000.000 = 15.000.000 = \\text{PUK} \\quad (\\text{Terbukti Identik})$$",
            "python_verification_code": "total_pop = 20000000\nbuk = 5000000\npuk = total_pop - buk\nbekerja = 9500000\npenganggur = 500000\nak = bekerja + penganggur\nsekolah = 2000000\nirt = 2500000\nlainnya = 500000\nbak = sekolah + irt + lainnya\nvalid = (puk == ak + bak)\nprint(f'PUK={puk}, AK={ak}, BAK={bak}, Valid={valid}')",
            "expected_output": "PUK=15000000, AK=10000000, BAK=5000000, Valid=True"
        },
        "exam_pitfalls": [
            {
                "trap_description": "Aturan Prioritas ICLS terhadap Mahasiswa/IRT yang Bekerja Marginal",
                "common_mistake": "Menggolongkan mahasiswa atau ibu rumah tangga yang bekerja 2 jam seminggu sebagai Bukan Angkatan Kerja (Sekolah/IRT).",
                "safe_strategy": "Patuhi aturan prioritas ICLS: Kegiatan ekonomi (bekerja minimal 1 jam) mengalahkan kegiatan non-ekonomi. Individu tersebut harus diklasifikasikan sebagai Bekerja (Angkatan Kerja)."
            },
            {
                "trap_description": "Pekerja Sementara Tidak Bekerja (Temporarily Absent)",
                "common_mistake": "Menganggap karyawan yang cuti sakit seminggu penuh atau petani yang menunggu masa tanam sebagai pengangguran terbuka.",
                "safe_strategy": "Selama memiliki ikatan kerja formal atau usaha yang masih aktif beroperasi, individu sementara tidak bekerja tetap tergolong Bekerja."
            }
        ],
        "textbook": "Official Statistics Lanjutan (OSL)",
        "chapter_id": 9,
        "chapter_title": "Pertemuan 9: Ketenagakerjaan dan Pendidikan",
        "section": "9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS",
        "mode": "deep",
        "points": [
            {
                "id": "9.1.1",
                "name": "Konsep Bekerja Minimal 1 Jam dan Angkatan Kerja",
                "importance": "高",
                "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 4-20]",
                "exam_focus": "Menguasai dekomposisi piramida ketenagakerjaan ICLS 13, definisi bekerja minimal 1 jam, pemilahan AK vs BAK, dan penerapan aturan prioritas ketenagakerjaan pada Sakernas BPS.",
                "textbook_excerpt": "Klasifikasi 2 kelompok penduduk dalam statistik tenaga kerja: Penduduk mencapai usia minimum bekerja (berumur >= 15 tahun) => PUK juga disebut angkatan kerja potensi; Selebihnya (berumur < 15 tahun) => bukan usia kerja (BUK). PUK yang aktif secara ekonomi terdiri dari: (1) bekerja, dan (2) mencari pekerjaan => unemployed. PUK 'tidak siap bekerja' karena sekolah, atau mengurus rumahtangga => bukan angkatan kerja [slide 6]. Batasan usia kerja di Indonesia >= 15 tahun sesuai konvensi ILO [slide 8]. Bekerja adalah melakukan kegiatan ekonomi minimal 1 jam berturut-turut selama seminggu yang lalu [slide 7].",
                "intuition": "Statistik ketenagakerjaan dirancang untuk mengukur dua hal: pasokan daya kerja (labor supply) dan tingkat penyerapan oleh sistem ekonomi (labor absorption). Batasan 1 jam seminggu tampak sangat longgar, namun ini adalah standar global ILO agar tidak ada satu pun kontribusi ekonomi riil yang terlewatkan (misalnya membantu panen keluarga, berdagang online sesaat, atau ojek sambilan).",
                "formal": "### 1. Kerangka Ketenagakerjaan ICLS 13\n\nBerdasarkan resolusi International Conference of Labour Statisticians ke-13 (ICLS 13 tahun 1982) yang diadopsi resmi oleh Badan Pusat Statistik (BPS):\n\n| Tingkat Klasifikasi | Kategori | Batasan Operasional BPS |\n|---|---|---|\n| **Tingkat 1: Batas Usia** | Penduduk Usia Kerja (PUK) | Penduduk berumur $\\ge 15$ tahun pada saat pencacahan [slide 6, 8] |\n| | Bukan Usia Kerja (BUK) | Penduduk berumur $< 15$ tahun [slide 6] |\n| **Tingkat 2: Aktivitas Ekonomi** | Angkatan Kerja (AK) | Penduduk usia kerja yang aktif secara ekonomi (*economically active*): Bekerja atau Pengangguran [slide 6] |\n| | Bukan Angkatan Kerja (BAK) | Penduduk usia kerja yang tidak aktif secara ekonomi (*economically inactive*): Sekolah, Mengurus Rumah Tangga, atau Lainnya [slide 6, 21] |\n| **Tingkat 3: Status Angkatan Kerja** | Bekerja (*Employed*) | Melakukan kegiatan ekonomi $\\ge 1$ jam berturut-turut dalam seminggu terakhir demi upah/laba, atau sementara tidak bekerja [slide 5, 7] |\n| | Pengangguran (*Unemployed*) | Tidak bekerja, bersedia bekerja, dan aktif mencari kerja atau mempersiapkan usaha [slide 5, 16] |\n\n### 2. Aturan Prioritas Ketenagakerjaan (The Priority Rule)\n\nDalam kuesioner Sakernas, seorang individu dapat melakukan beberapa aktivitas sekaligus dalam seminggu terakhir (misalnya kuliah sambil menjadi barista 4 jam seminggu, atau ibu rumah tangga yang menjual kue secara daring). BPS menerapkan **Aturan Prioritas** hierarkis sbb:\n\n$$\\text{Bekerja} \\succ \\text{Mencari Kerja (Penganggur)} \\succ \\text{Bukan Angkatan Kerja (Sekolah/IRT/Lainnya)}$$\n\n- Jika seseorang bekerja $\\ge 1$ jam, statusnya mutlak **Bekerja**, mengabaikan status sekolah atau mengurus rumah tangganya.\n- Jika seseorang tidak bekerja tetapi aktif mencari pekerjaan atau mempersiapkan usaha baru, statusnya mutlak **Pengangguran**, mengabaikan waktu luangnya yang dihabiskan di rumah.\n- Hanya jika seseorang tidak bekerja dan tidak mencari kerja, barulah diklasifikasikan ke dalam salah satu dari tiga sub-kelompok **BAK**:\n  1. **Sekolah**: Bersekolah formal atau nonformal.\n  2. **Mengurus Rumah Tangga**: Mengurus keluarga tanpa upah/laba ekonomi komersial.\n  3. **Lainnya**: Penerima pensiun, lansia tidak berdaya, orang dengan disabilitas berat yang tidak mampu bekerja.",
                "pitfalls": "1. **Mengabaikan Pekerja Keluarga Tak Dibayar**: Dianggap BAK karena tidak menerima gaji uang. Padahal BPS menghitung pekerja keluarga tak dibayar minimal 1 jam sebagai Bekerja.\n2. **Kekeliruan Ambang Batas 15 Jam Internasional**: Beberapa literatur asing mencantumkan 15 jam untuk unpaid worker, namun BPS secara konsisten menetapkan batas 1 jam tanpa putus untuk seluruh kategori pekerja.",
                "memory_hook": "Piramida Tenaga Kerja: PUK (15+) = AK (Bekerja + Penganggur) + BAK (Sekolah + IRT + Lainnya). Prioritas: Bekerja > Penganggur > BAK.",
                "examples": [
                    {
                        "type": "single",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 6-8]",
                        "problem": "Seorang pemuda berusia 19 tahun merupakan mahasiswa aktif semester 3. Pada hari Sabtu minggu lalu, ia bekerja selama 3 jam sebagai barista di kedai kopi pamannya dan menerima upah harian. Berdasarkan konsep ketenagakerjaan BPS dan aturan prioritas ICLS, pemuda tersebut diklasifikasikan sebagai:",
                        "options": [
                            "Bukan Angkatan Kerja karena kegiatan utamanya adalah mahasiswa aktif.",
                            "Angkatan Kerja dengan status Bekerja karena melakukan kegiatan ekonomi minimal 1 jam seminggu terakhir.",
                            "Pengangguran Terbuka karena belum tamat kuliah dan belum memiliki pekerjaan tetap.",
                            "Pekerja Paruh Waktu sukarela yang digolongkan ke dalam Bukan Usia Kerja."
                        ],
                        "answer": 1,
                        "solution": "Jawaban: **B**.\n\n**Pembahasan Bertahap**:\n1. Berdasarkan aturan prioritas ICLS 13 dan BPS, kegiatan ekonomi (bekerja $\\ge 1$ jam) mendapat prioritas tertinggi di atas kegiatan non-ekonomi (bersekolah/kuliah).\n2. Pemuda tersebut berusia 19 tahun (PUK $\\ge 15$) dan bekerja selama 3 jam (memenuhi syarat $\\ge 1$ jam berturut-turut untuk memperoleh upah).\n3. Oleh karena itu, ia sah diklasifikasikan ke dalam **Angkatan Kerja** dengan status **Bekerja**."
                    },
                    {
                        "type": "text",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 21]",
                        "problem": "Berdasarkan data Sakernas suatu kabupaten, penduduk usia 15 tahun ke atas berjumlah 500.000 orang. Diketahui penduduk yang bekerja berjumlah 320.000 orang, pengangguran terbuka berjumlah 20.000 orang, penduduk yang bersekolah 60.000 orang, dan mengurus rumah tangga 90.000 orang. Tentukan:\n1. Jumlah Angkatan Kerja (AK).\n2. Jumlah Bukan Angkatan Kerja kategori 'Lainnya'.\nTuliskan jawaban akhir dalam format: `AK=X, Lainnya=Y`.",
                        "answer": "AK=340000, Lainnya=10000",
                        "solution": "Langkah-langkah perhitungan:\n1. Menghitung Angkatan Kerja (AK):\n   $$\\text{AK} = \\text{Bekerja} + \\text{Pengangguran} = 320.000 + 20.000 = 340.000$$\n2. Menghitung total Bukan Angkatan Kerja (BAK):\n   $$\\text{BAK} = \\text{PUK} - \\text{AK} = 500.000 - 340.000 = 160.000$$\n3. Menghitung BAK kategori 'Lainnya':\n   $$\\text{BAK} = \\text{Sekolah} + \\text{Mengurus RT} + \\text{Lainnya}$$\n   $$160.000 = 60.000 + 90.000 + \\text{Lainnya}$$\n   $$\\text{Lainnya} = 160.000 - 150.000 = 10.000$$\n\n**Verifikasi Kode Python**:\n```python\npuk = 500000\nbekerja = 320000\npenganggur = 20000\nsekolah = 60000\nirt = 90000\nak = bekerja + penganggur\nbak = puk - ak\nlainnya = bak - (sekolah + irt)\nprint(f'AK={ak}, Lainnya={lainnya}')\n# Output: AK=340000, Lainnya=10000\n```"
                    }
                ],
                "links": ["9.1.2", "9.1.3", "9.1.4"]
            }
        ]
    },
    {
        "filename": "9.1.2-tingkat-partisipasi-angkatan-kerja-tpak.json",
        "point_id": "9.1.2",
        "title": "Tingkat Partisipasi Angkatan Kerja TPAK",
        "importance": "高",
        "curriculum_alignment": {
            "pertemuan": 9,
            "silabus_topic": "Ketenagakerjaan dan Pendidikan",
            "bps_subject": "Statistik Ketenagakerjaan"
        },
        "grounding": {
            "primary_sources": [
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "13-14",
                    "content": "Definisi, formula TPAK = (a / b) * 100 dimana a = Angkatan Kerja dan b = Penduduk 15 tahun ke atas, kegunaan, dan interpretasi pasokan tenaga kerja (labor supply)."
                },
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "21-23",
                    "content": "Tabel seri perkembangan TPAK nasional 2019-2021 Sakernas menurut perkotaan, perdesaan, dan gender."
                }
            ],
            "supplemental_sources": [],
            "coverage_status": "COVERED"
        },
        "theory": {
            "intuition": "TPAK mengukur proporsi penduduk usia kerja yang benar-benar terjun ke gelanggang pasar kerja, baik yang sudah berhasil mendapatkan pekerjaan maupun yang masih aktif mencari kerja. TPAK merupakan indikator utama dari sisi penawaran tenaga kerja (labor supply side). Jika TPAK naik, ekonomi memiliki lebih banyak tangan produktif; namun jika tidak diimbangi penciptaan lapangan kerja, kenaikan TPAK dapat memicu lonjakan angka pengangguran.",
            "bps_definition": "Tingkat Partisipasi Angkatan Kerja (TPAK) adalah persentase penduduk usia 15 tahun ke atas yang merupakan angkatan kerja terhadap seluruh penduduk usia 15 tahun ke atas. Sumber data resmi diperoleh dari Survei Angkatan Kerja Nasional (SAKERNAS).",
            "boundary_conditions": "1. Rentang matematis: $0\\% \\le \\text{TPAK} \\le 100\\%$. Pada praktiknya di Indonesia, TPAK berkisar antara 67% hingga 70%.\n2. Pembagi mutlak: Penduduk Usia Kerja (PUK, 15+ tahun). Pembagian dengan total populasi (0+ tahun) adalah kekeliruan fatal.\n3. Disagregasi gender: TPAK laki-laki konsisten jauh lebih tinggi (~83%) dibanding perempuan (~54%), karena sebagian besar perempuan yang tidak bekerja berada di kelompok mengurus rumah tangga (BAK).\n4. Disagregasi wilayah: TPAK perdesaan umumnya lebih tinggi dibanding perkotaan karena dominasi sektor pertanian keluarga.",
            "formula_latex": "$$\\text{TPAK} = \\frac{\\text{AK}}{\\text{PUK}} \\times 100\\% = \\frac{\\text{Bekerja} + \\text{Penganggur}}{\\text{Penduduk Usia } \\ge 15 \\text{ Tahun}} \\times 100\\%$$"
        },
        "numerical_example": {
            "problem_statement": "Dalam publikasi profil ketenagakerjaan Provinsi Harmoni, tercatat data demografi penduduk usia 15 tahun ke atas sbb: Penduduk usia kerja laki-laki berjumlah 5.000.000 jiwa dengan 4.150.000 jiwa di antaranya tergolong angkatan kerja. Penduduk usia kerja perempuan berjumlah 5.000.000 jiwa dengan 2.700.000 jiwa di antaranya tergolong angkatan kerja. Hitunglah: (1) TPAK Laki-laki, (2) TPAK Perempuan, (3) TPAK Total Provinsi, dan (4) Kesenjangan Partisipasi Gender (Gender Gap).",
            "data_table": "| Kelompok Gender | PUK (15+ Tahun) | Angkatan Kerja (AK) |\n|---|---|---|\n| Laki-laki | 5.000.000 | 4.150.000 |\n| Perempuan | 5.000.000 | 2.700.000 |\n| Total Provinsi | 10.000.000 | 6.850.000 |",
            "step_by_step_solution": "1. TPAK Laki-laki:\n   $$\\text{TPAK}_L = \\frac{4.150.000}{5.000.000} \\times 100\\% = 83,00\\%$$\n2. TPAK Perempuan:\n   $$\\text{TPAK}_P = \\frac{2.700.000}{5.000.000} \\times 100\\% = 54,00\\%$$\n3. TPAK Total Provinsi:\n   $$\\text{TPAK}_{\\text{Total}} = \\frac{4.150.000 + 2.700.000}{5.000.000 + 5.000.000} \\times 100\\% = \\frac{6.850.000}{10.000.000} \\times 100\\% = 68,50\\%$$\n4. Gender Gap TPAK:\n   $$\\Delta \\text{TPAK} = \\text{TPAK}_L - \\text{TPAK}_P = 83,00\\% - 54,00\\% = 29,00\\%$$",
            "python_verification_code": "puk_l = 5000000\nak_l = 4150000\ntpak_l = (ak_l / puk_l) * 100\n\npuk_p = 5000000\nak_p = 2700000\ntpak_p = (ak_p / puk_p) * 100\n\npuk_tot = puk_l + puk_p\nak_tot = ak_l + ak_p\ntpak_tot = (ak_tot / puk_tot) * 100\ngap = tpak_l - tpak_p\n\nprint(f'TPAK L={tpak_l:.2f}%, TPAK P={tpak_p:.2f}%, TPAK Total={tpak_tot:.2f}%, Gap={gap:.2f}%')",
            "expected_output": "TPAK L=83.00%, TPAK P=54.00%, TPAK Total=68.50%, Gap=29.00%"
        },
        "exam_pitfalls": [
            {
                "trap_description": "Penyebut TPAK Tertukar dengan Total Penduduk",
                "common_mistake": "Membagi Angkatan Kerja dengan total populasi (termasuk anak < 15 tahun).",
                "safe_strategy": "Ingat rumus resmi BPS: Pembagi TPAK adalah Penduduk Usia Kerja (PUK >= 15 tahun), BUKAN total penduduk."
            },
            {
                "trap_description": "Kesimpulan Keliru bahwa Perempuan yang Tidak Masuk AK Adalah Pengangguran",
                "common_mistake": "Mengasumsikan rendahnya TPAK perempuan berarti tingkat pengangguran perempuan sangat tinggi.",
                "safe_strategy": "Perempuan yang tidak berpartisipasi dalam angkatan kerja berada pada kelompok Bukan Angkatan Kerja (terutama mengurus rumah tangga), bukan pengangguran terbuka."
            }
        ],
        "textbook": "Official Statistics Lanjutan (OSL)",
        "chapter_id": 9,
        "chapter_title": "Pertemuan 9: Ketenagakerjaan dan Pendidikan",
        "section": "9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS",
        "mode": "deep",
        "points": [
            {
                "id": "9.1.2",
                "name": "Tingkat Partisipasi Angkatan Kerja TPAK",
                "importance": "高",
                "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 13-14, 21-23]",
                "exam_focus": "Formula resmi TPAK, perhitungan bobot disagregasi wilayah/gender, analisis dinamika penawaran tenaga kerja (labor supply), dan interpretasi tren TPAK BPS.",
                "textbook_excerpt": "Tingkat Partisipasi Angkatan Kerja (TPAK) = a / b * 100, dimana a = Jumlah Angkatan Kerja, b = Jumlah penduduk 15 tahun ke atas [slide 13]. Kondef: Persentase penduduk usia 15 tahun ke atas yang merupakan angkatan kerja. Kegunaan: Mengindikasikan besarnya persentase penduduk usia kerja yang aktif secara ekonomi di suatu negara/wilayah. Interpretasi: Semakin tinggi TPAK menunjukkan semakin tinggi pasokan tenaga kerja (labour supply) yang tersedia untuk memproduksi barang dan jasa dalam suatu perekonomian [slide 14].",
                "intuition": "Jika ada 100 orang berumur 15 tahun ke atas di suatu desa, berapa orang yang siap bekerja atau sudah bekerja? Angka itulah TPAK. Bila TPAK bernilai 68%, artinya 68 orang aktif mencari nafkah atau menyediakan jasanya di pasar kerja, sedangkan 32 orang lainnya sedang fokus sekolah, mengurus rumah tangga, atau sudah pensiun.",
                "formal": "### 1. Definisi dan Formulasi Matematis\n\nBerdasarkan pedoman resmi BPS:\n$$\\text{TPAK} = \\frac{\\text{AK}}{\\text{PUK}} \\times 100\\% = \\frac{\\text{Bekerja} + \\text{Pengangguran}}{P_{15+}} \\times 100\\%$$\n\nSecara demografis, TPAK dapat didekomposisi berdasarkan kelompok jenis kelamin atau wilayah:\n$$\\text{TPAK}_{\\text{Total}} = w_L \\cdot \\text{TPAK}_L + w_P \\cdot \\text{TPAK}_P$$\ndi mana bobot $w_L = \\frac{\\text{PUK}_L}{\\text{PUK}_{\\text{Total}}}$ dan $w_P = \\frac{\\text{PUK}_P}{\\text{PUK}_{\\text{Total}}}$.\n\n### 2. Tren Empiris Sakernas BPS 2019-2021\n\nBerdasarkan data seri Sakernas BPS [slide 21]:\n\n| Periode Survei | Penduduk 15+ (PUK) | Angkatan Kerja (AK) | Bekerja | Pengangguran | TPAK (%) |\n|---|---|---|---|---|---|\n| **Februari 2019** | 199.785.195 | 138.591.388 | 131.692.592 | 6.898.796 | **69,37** |\n| **Agustus 2019** | 201.185.014 | 135.859.695 | 128.755.271 | 7.104.424 | **67,53** |\n| **Februari 2020** | 202.597.063 | 140.218.352 | 133.292.866 | 6.925.486 | **69,21** |\n| **Agustus 2020** | 203.972.460 | 138.221.938 | 128.454.184 | 9.767.754 | **67,77** |\n| **Februari 2021** | 205.360.436 | 139.810.313 | 131.064.305 | 8.746.008 | **68,08** |\n| **Agustus 2021** | 206.708.299 | 140.152.575 | 131.050.523 | 9.102.052 | **67,80** |\n\n*Catatan Pola Musiman*: TPAK Februari selalu lebih tinggi dari TPAK Agustus karena siklus panen raya pertanian menyerap banyak tenaga kerja musiman.",
                "pitfalls": "Menghitung rata-rata sederhana TPAK Laki-laki dan Perempuan tanpa pembobotan populasi PUK. Jika jumlah laki-laki dan perempuan tidak sama, rata-rata sederhana akan bias.",
                "memory_hook": "TPAK = AK / PUK * 100%. Mengukur labor supply. Pria ~83%, Wanita ~54%.",
                "examples": [
                    {
                        "type": "single",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 13-14]",
                        "problem": "Pernyataan manakah yang paling tepat mengenai karakteristik dan interpretasi indikator TPAK di Indonesia?",
                        "options": [
                            "Kenaikan TPAK selalu menjamin penurunan angka pengangguran di suatu daerah.",
                            "TPAK mengindikasikan besarnya penawaran tenaga kerja (labour supply) yang tersedia dalam perekonomian.",
                            "TPAK dihitung dengan membagi penduduk yang bekerja dengan total seluruh penduduk.",
                            "TPAK perkotaan di Indonesia umumnya selalu lebih tinggi daripada TPAK perdesaan."
                        ],
                        "answer": 1,
                        "solution": "Jawaban: **B**.\n\n**Pembahasan**:\n- Pilihan A salah: Jika peningkatan penawaran tenaga kerja tidak disertai ekspansi lapangan kerja, pengangguran justru meningkat.\n- Pilihan B benar: Sesuai slide 14, interpretasi resmi TPAK adalah mengindikasikan besarnya penawaran tenaga kerja (labour supply) yang tersedia untuk memproduksi barang dan jasa.\n- Pilihan C salah: Pembaginya adalah PUK (15+), dan pembilangnya adalah AK (Bekerja + Penganggur).\n- Pilihan D salah: TPAK perdesaan secara empiris lebih tinggi daripada perkotaan."
                    },
                    {
                        "type": "text",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 13, 21]",
                        "problem": "Suatu wilayah memiliki 60.000 penduduk usia kerja laki-laki dan 40.000 penduduk usia kerja perempuan. Jika TPAK Laki-laki adalah 80% dan TPAK Perempuan adalah 50%, hitunglah TPAK Gabungan wilayah tersebut. Tuliskan jawaban dalam format: `TPAK=X%` (dengan 1 desimal).",
                        "answer": "TPAK=68.0%",
                        "solution": "Langkah-langkah perhitungan:\n1. Angkatan Kerja Laki-laki:\n   $$\\text{AK}_L = 80\\% \\times 60.000 = 48.000$$\n2. Angkatan Kerja Perempuan:\n   $$\\text{AK}_P = 50\\% \\times 40.000 = 20.000$$\n3. Total Angkatan Kerja:\n   $$\\text{AK}_{\\text{Total}} = 48.000 + 20.000 = 68.000$$\n4. Total PUK:\n   $$\\text{PUK}_{\\text{Total}} = 60.000 + 40.000 = 100.000$$\n5. TPAK Gabungan:\n   $$\\text{TPAK} = \\frac{68.000}{100.000} \\times 100\\% = 68,0\\%$$\n\n**Verifikasi Kode Python**:\n```python\npuk_l = 60000\nak_l = 0.80 * puk_l\npuk_p = 40000\nak_p = 0.50 * puk_p\ntpak = (ak_l + ak_p) / (puk_l + puk_p) * 100\nprint(f'TPAK={tpak:.1f}%')\n# Output: TPAK=68.0%\n```"
                    }
                ],
                "links": ["9.1.1", "9.1.3", "9.1.4"]
            }
        ]
    },
    {
        "filename": "9.1.3-tingkat-pengangguran-terbuka-tpt.json",
        "point_id": "9.1.3",
        "title": "Tingkat Pengangguran Terbuka TPT",
        "importance": "高",
        "curriculum_alignment": {
            "pertemuan": 9,
            "silabus_topic": "Ketenagakerjaan dan Pendidikan",
            "bps_subject": "Statistik Ketenagakerjaan"
        },
        "grounding": {
            "primary_sources": [
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "15-16",
                    "content": "Formula TPT = (PP / PAK) * 100, definisi pengangguran terbuka yang mencakup 4 kategori penganggur BPS."
                },
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "21-23",
                    "content": "Data seri pengangguran terbuka nasional Sakernas 2019-2021 dan lonjakan TPT pada masa pandemi Covid-19."
                }
            ],
            "supplemental_sources": [],
            "coverage_status": "COVERED"
        },
        "theory": {
            "intuition": "TPT mengukur sejauh mana pasokan tenaga kerja yang telah aktif di bursa kerja gagal diserap oleh aktivitas ekonomi. TPT bukan cerminan dari seluruh orang yang tidak bekerja, melainkan hanya mereka yang 'siap dan berupaya' bekerja tetapi belum memperoleh pekerjaan. Oleh sebab itu, pembagi TPT adalah Angkatan Kerja (AK), bukan total penduduk usia kerja.",
            "bps_definition": "Tingkat Pengangguran Terbuka (TPT) adalah persentase jumlah pengangguran terhadap jumlah angkatan kerja. Pengangguran Terbuka BPS terdiri atas 4 kategori: (1) Penduduk yang aktif mencari pekerjaan, (2) Penduduk yang sedang mempersiapkan usaha/pekerjaan baru, (3) Penduduk yang tidak mencari kerja karena merasa tidak mungkin mendapat pekerjaan (discouraged workers / putus asa), dan (4) Penduduk yang sudah memiliki pekerjaan/diterima kerja tetapi belum mulai bekerja (future starts).",
            "boundary_conditions": "1. Pembagi resmi: Angkatan Kerja (AK = Bekerja + Pengangguran). Bukan PUK, bukan total penduduk, dan bukan penduduk bekerja.\n2. Batasan kategori: Seseorang yang tidak bekerja tetapi tidak mencari pekerjaan karena sedang sekolah atau mengurus rumah tangga TIDAK boleh dimasukkan sebagai pengangguran terbuka (mereka adalah BAK).\n3. Kategori 'putus asa' dan 'mempersiapkan usaha' secara eksplisit dihitung sebagai pengangguran terbuka di Indonesia, berbeda dengan definisi ILO murni yang mensyaratkan pencarian kerja aktif.",
            "formula_latex": "$$\\text{TPT} = \\frac{\\text{Penganggur}}{\\text{AK}} \\times 100\\% = \\frac{\\text{Penganggur}}{\\text{Bekerja} + \\text{Penganggur}} \\times 100\\%$$"
        },
        "numerical_example": {
            "problem_statement": "Rekonstruksi Soal UAS 2022/2023 Esai 1 Ketenagakerjaan: Suatu negara berpenduduk 18,0 juta jiwa dengan 4,0 juta jiwa di antaranya belum mencapai usia 15 tahun (BUK). Dari penduduk usia kerja (PUK), 5,0 juta jiwa tergolong bukan angkatan kerja (2,0 juta bersekolah, 2,0 juta mengurus rumah tangga, dan 1,0 juta lainnya). Penduduk yang bekerja berjumlah 7,0 juta orang (6,0 juta bekerja penuh dan 1,0 juta bekerja paruh waktu). Terdapat 1,0 juta orang yang terkena PHK dan sedang aktif mencari kerja, 0,5 juta orang sedang mempersiapkan usaha kedai kopi, serta 0,5 juta orang telah dinyatakan lulus seleksi kerja tetapi baru akan mulai bertugas bulan depan. Hitunglah nilai TPAK dan TPT negara tersebut!",
            "data_table": "| Komponen Ketenagakerjaan | Jumlah Jiwa (Juta) |\n|---|---|\n| Total Populasi | 18,0 |\n| Bukan Usia Kerja (< 15 Tahun) | 4,0 |\n| Penduduk Usia Kerja (PUK >= 15 Tahun) | 14,0 |\n| Bukan Angkatan Kerja (Sekolah, IRT, Lainnya) | 5,0 |\n| Penduduk Bekerja Penuh (>= 35 jam) | 6,0 |\n| Penduduk Bekerja Kurang Jam Kerja (< 35 jam) | 1,0 |\n| Penganggur: Terkena PHK mencari kerja | 1,0 |\n| Penganggur: Sedang mempersiapkan usaha | 0,5 |\n| Penganggur: Sudah diterima kerja belum mulai | 0,5 |",
            "step_by_step_solution": "1. Identifikasi PUK dan Angkatan Kerja (AK):\n   $$\\text{PUK} = 18,0 - 4,0 = 14,0 \\text{ juta jiwa}$$\n   $$\\text{Total Bekerja (PB)} = 6,0 + 1,0 = 7,0 \\text{ juta jiwa}$$\n   $$\\text{Total Penganggur} = 1,0 + 0,5 + 0,5 = 2,0 \\text{ juta jiwa}$$\n   $$\\text{Angkatan Kerja (AK)} = \\text{PB} + \\text{Penganggur} = 7,0 + 2,0 = 9,0 \\text{ juta jiwa}$$\n2. Perhitungan TPAK:\n   $$\\text{TPAK} = \\frac{\\text{AK}}{\\text{PUK}} \\times 100\\% = \\frac{9,0}{14,0} \\times 100\\% = 64,2857\\% \\approx 64,29\\%$$\n3. Perhitungan TPT:\n   $$\\text{TPT} = \\frac{\\text{Penganggur}}{\\text{AK}} \\times 100\\% = \\frac{2,0}{9,0} \\times 100\\% = 22,2222\\% \\approx 22,22\\%$$",
            "python_verification_code": "pop_total = 18.0\nbuk = 4.0\npuk = pop_total - buk\npb_full = 6.0\npb_part = 1.0\npb_total = pb_full + pb_part\nunemployed_phk = 1.0\nunemployed_startup = 0.5\nunemployed_waiting = 0.5\nunemployed_total = unemployed_phk + unemployed_startup + unemployed_waiting\nak = pb_total + unemployed_total\ntpak = (ak / puk) * 100.0\ntpt = (unemployed_total / ak) * 100.0\nprint(f'TPAK={tpak:.2f}%, TPT={tpt:.2f}%')",
            "expected_output": "TPAK=64.29%, TPT=22.22%"
        },
        "exam_pitfalls": [
            {
                "trap_description": "Penyebut TPT Dibagi dengan PUK atau PB",
                "common_mistake": "Menghitung TPT dengan pembagi PUK (misal 2.0 / 14.0 = 14.29%) atau membagi dengan PB (2.0 / 7.0 = 28.57%).",
                "safe_strategy": "Pembagi TPT adalah mutlak Angkatan Kerja (AK = PB + Penganggur = 9.0). Nilai yang benar adalah 2.0 / 9.0 = 22.22%."
            },
            {
                "trap_description": "Mengabaikan 3 Kategori Penganggur Non-Pencari Kerja Aktif",
                "common_mistake": "Hanya menghitung orang yang aktif melamar pekerjaan (PHK = 1.0 juta) sehingga TPT dihitung 1.0 / 8.0 = 12.5%.",
                "safe_strategy": "Di BPS, orang yang mempersiapkan usaha baru dan orang yang sudah diterima kerja tapi belum mulai bertugas WAJIB dimasukkan ke dalam kelompok pengangguran terbuka."
            }
        ],
        "textbook": "Official Statistics Lanjutan (OSL)",
        "chapter_id": 9,
        "chapter_title": "Pertemuan 9: Ketenagakerjaan dan Pendidikan",
        "section": "9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS",
        "mode": "deep",
        "points": [
            {
                "id": "9.1.3",
                "name": "Tingkat Pengangguran Terbuka TPT",
                "importance": "高",
                "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 15-16, 21-23]",
                "exam_focus": "Definisi 4 kategori penganggur BPS, rekonstruksi soal hitungan esai UAS, rumus TPT terhadap AK, dan analisis dampak ekonomi makro (Okun's law context).",
                "textbook_excerpt": "Tingkat Pengangguran Terbuka (TPT) = PP / PAK * 100, dimana PP = Jumlah pengangguran, PAK = Jumlah angkatan kerja [slide 15]. Kondef: Tingkat pengangguran terbuka adalah persentase jumlah pengangguran terhadap jumlah angkatan kerja. Pengangguran yaitu: (1) penduduk yang aktif mencari pekerjaan, (2) penduduk yang sedang mempersiapkan usaha/pekerjaan baru, (3) penduduk yang tidak mencari pekerjaan karena merasa tidak mungkin mendapat pekerjaan (discouraged worker), (4) kelompok penduduk yang tidak aktif mencari pekerjaan dengan alasan sudah mempunyai pekerjaan tetapi belum mulai bekerja [slide 16].",
                "intuition": "Jika ada 100 orang yang terjun ke bursa tenaga kerja, berapa orang yang belum berhasil diserap oleh roda perekonomian? Indikator inilah yang dijawab oleh TPT. Semakin tinggi TPT, semakin besar kapasitas produksi nasional yang menganggur secara sia-sia (*economic waste*), mengurangi pendapatan keluarga, dan menurunkan penerimaan pajak.",
                "formal": "### 1. Empat Kategori Pengangguran Terbuka BPS\n\nBPS mengklasifikasikan pengangguran terbuka ke dalam 4 kelompok operasional yang sangat sering diuji dalam soal esai ujian [slide 16]:\n\n| No | Kategori Pengangguran BPS | Deskripsi dan Kriteria Operasional | Contoh Kasus Nyata |\n|---|---|---|---|\n| **1** | **Mencari Pekerjaan** | Mereka yang dalam 7 hari terakhir aktif mencari pekerjaan (mengirim surat lamaran, mendaftar bursa kerja, mengikuti wawancara). | Korban PHK yang melamar pekerjaan ke berbagai pabrik. |\n| **2** | **Mempersiapkan Usaha** | Mereka yang melakukan tindakan nyata untuk mendirikan usaha baru (mencari modal, menyewa tempat, mengurus izin usaha). | Sarjana yang sedang menyewa ruko dan membeli peralatan kedai kopi. |\n| **3** | **Merasa Tidak Mungkin Mendapat Pekerjaan (*Discouraged Worker*)** | Mereka yang tidak bekerja dan bersedia bekerja, tetapi tidak lagi mencari kerja karena putus asa merasa tidak ada lowongan yang sesuai. | Pekerja lansia/difabel yang berulang kali ditolak kerja sehingga berhenti melamar. |\n| **4** | **Sudah Diterima Kerja Tetapi Belum Mulai Bekerja (*Future Starts*)** | Mereka yang telah lolos seleksi dan memiliki kepastian tanggal mulai bekerja, namun pada minggu pencacahan belum resmi bertugas. | Calon ASN yang telah menerima SK dan menunggu jadwal penempatan bulan depan. |\n\n### 2. Formula Matematis\n$$\\text{TPT} = \\frac{\\text{Jumlah Penganggur}}{\\text{Jumlah Angkatan Kerja}} \\times 100\\% = \\frac{\\sum_{k=1}^4 \\text{Penganggur}_k}{\\text{PB} + \\sum_{k=1}^4 \\text{Penganggur}_k} \\times 100\\%$$",
                "pitfalls": "Salah menempatkan kategori 'mempersiapkan usaha' atau 'sudah diterima kerja' ke dalam kelompok Bekerja atau Bukan Angkatan Kerja. Di BPS, kedua kelompok ini SAH sebagai Pengangguran Terbuka.",
                "memory_hook": "TPT = Penganggur / AK * 100. Penganggur BPS ada 4: Cari Kerja, Bikin Usaha, Putus Asa, Sudah Diterima Belum Kerja.",
                "examples": [
                    {
                        "type": "single",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 16]",
                        "problem": "Berdasarkan pedoman operasional BPS, manakah di antara individu berikut yang TIDAK digolongkan sebagai pengangguran terbuka?",
                        "options": [
                            "Seseorang yang sedang mengumpulkan modal dan mencari lokasi sewa ruko untuk membuka minimarket.",
                            "Seseorang yang telah lulus wawancara kerja dan dijadwalkan mulai bertugas dua pekan mendatang.",
                            "Seseorang yang berhenti mencari kerja karena merasa di daerahnya tidak ada lowongan yang cocok bagi dirinya.",
                            "Seseorang yang mengundurkan diri dari pekerjaannya demi fokus mengasuh anak balita di rumah tanpa mencari kerja."
                        ],
                        "answer": 3,
                        "solution": "Jawaban: **D**.\n\n**Pembahasan**:\n- Pilihan A: Masuk kategori (2) Sedang mempersiapkan usaha/pekerjaan baru.\n- Pilihan B: Masuk kategori (4) Sudah mempunyai pekerjaan tetapi belum mulai bekerja.\n- Pilihan C: Masuk kategori (3) Merasa tidak mungkin mendapat pekerjaan (*discouraged worker*).\n- Pilihan D: Masuk ke dalam **Bukan Angkatan Kerja (BAK)** kategori Mengurus Rumah Tangga karena tidak berkeinginan mencari pekerjaan komersial."
                    },
                    {
                        "type": "text",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 15-16, 21]",
                        "problem": "Di suatu kota industri, terdapat 190.000 penduduk usia kerja yang bekerja dan 10.000 orang pengangguran terbuka. Karena krisis ekonomi global, 5.000 pekerja mengalami pemutusan hubungan kerja (PHK) dan langsung aktif mencari pekerjaan baru di bursa kerja. Asumsikan tidak ada perubahan pada komponen angkatan kerja lainnya. Hitunglah TPT kota tersebut sebelum dan sesudah krisis ekonomi. Tuliskan jawaban dalam format: `Sebelum=X.XX%, Sesudah=Y.YY%`.",
                        "answer": "Sebelum=5.00%, Sesudah=7.50%",
                        "solution": "Langkah-langkah perhitungan:\n1. Kondisi Sebelum Krisis:\n   $$\\text{PB} = 190.000, \\quad \\text{Penganggur} = 10.000$$\n   $$\\text{AK} = 190.000 + 10.000 = 200.000$$\n   $$\\text{TPT}_{\\text{awal}} = \\frac{10.000}{200.000} \\times 100\\% = 5,00\\%$$\n2. Kondisi Sesudah Krisis:\n   - Pekerja berkurang 5.000 menjadi $190.000 - 5.000 = 185.000$.\n   - Pengangguran bertambah 5.000 menjadi $10.000 + 5.000 = 15.000$.\n   - Total Angkatan Kerja (AK) tetap sama: $185.000 + 15.000 = 200.000$.\n   $$\\text{TPT}_{\\text{akhir}} = \\frac{15.000}{200.000} \\times 100\\% = 7,50\\%$$\n\n**Verifikasi Kode Python**:\n```python\nak = 200000\ntpt_awal = (10000 / ak) * 100\ntpt_akhir = (15000 / ak) * 100\nprint(f'Sebelum={tpt_awal:.2f}%, Sesudah={tpt_akhir:.2f}%')\n# Output: Sebelum=5.00%, Sesudah=7.50%\n```"
                    }
                ],
                "links": ["9.1.1", "9.1.2", "9.1.4"]
            }
        ]
    },
    {
        "filename": "9.1.4-setengah-penganggur-vs-pekerja-paruh-waktu.json",
        "point_id": "9.1.4",
        "title": "Setengah Penganggur vs Pekerja Paruh Waktu",
        "importance": "高",
        "curriculum_alignment": {
            "pertemuan": 9,
            "silabus_topic": "Ketenagakerjaan dan Pendidikan",
            "bps_subject": "Statistik Ketenagakerjaan"
        },
        "grounding": {
            "primary_sources": [
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "17-20",
                    "content": "Definisi batas 35 jam seminggu, formula Tingkat Setengah Pengangguran (TSP = PBJK<35 / PB * 100), formula Tingkat Pekerja Paruh Waktu (TPPW = PBPW / PB * 100), pembagi penduduk bekerja (PB)."
                },
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "24-28",
                    "content": "EXT-1: Penentuan status pekerjaan formal vs informal BPS (Proxy 2) berdasarkan 7 status pekerjaan dan jenis/lapangan usaha (KBLI 2020)."
                }
            ],
            "supplemental_sources": [],
            "coverage_status": "COVERED"
        },
        "theory": {
            "intuition": "Mempunyai pekerjaan tidak serta-merta berarti terhindar dari pemborosan kapasitas tenaga kerja. BPS menetapkan standar jam kerja normal adalah 35 jam per minggu. Pekerja dengan jam kerja < 35 jam dipilah berdasarkan kesukarelaannya: mereka yang masih ingin bekerja lebih banyak jam adalah Setengah Penganggur (involuntary underemployment), sedangkan mereka yang memang puas dengan jam kerja pendek adalah Pekerja Paruh Waktu (voluntary part-time). Selain kuantitas jam, kualitas kerja diukur melalui sektor Formal vs Informal.",
            "bps_definition": "Pekerja Setengah Pengangguran adalah mereka yang bekerja di bawah jam kerja normal (< 35 jam seminggu) dan masih mencari pekerjaan atau masih bersedia menerima pekerjaan tambahan. Pekerja Paruh Waktu adalah mereka yang bekerja < 35 jam seminggu tetapi tidak mencari atau tidak bersedia menerima pekerjaan lain. Sektor informal didefinisikan berdasarkan status pekerjaan berusaha sendiri, berusaha dibantu buruh tidak tetap, pekerja bebas, dan pekerja keluarga tak dibayar.",
            "boundary_conditions": "1. Pembagi resmi TSP dan TPPW adalah Penduduk Bekerja (PB), BUKAN Angkatan Kerja (AK) dan BUKAN PUK.\n2. Cut-off jam kerja: persis < 35 jam seminggu. Bekerja tepat 35 jam seminggu tergolong jam kerja normal (bekerja penuh).\n3. Klasifikasi Formal BPS: Berusaha dibantu buruh tetap dan Buruh/Karyawan/Pegawai selalu formal; Pekerja bebas dan Pekerja keluarga selalu informal; Berusaha sendiri dipilah menurut keahlian jabatan.",
            "formula_latex": "$$\\text{TSP} = \\frac{\\text{PB}_{<35, \\text{mencari}}}{\\text{PB}} \\times 100\\%, \\quad \\text{TPPW} = \\frac{\\text{PB}_{<35, \\text{sukarela}}}{\\text{PB}} \\times 100\\%, \\quad \\text{Proporsi INF} = \\frac{\\text{PB}_{\\text{INF}}}{\\text{PB}} \\times 100\\%$$"
        },
        "numerical_example": {
            "problem_statement": "Melanjutkan Soal UAS 2022/2023 Esai 1 dan integrasi EXT-1: Dari 7,0 juta penduduk yang bekerja, terdapat 5,0 juta orang bekerja penuh (>= 35 jam). Dari 2,0 juta orang yang bekerja < 35 jam seminggu, 1,0 juta orang masih aktif mencari pekerjaan tambahan (setengah penganggur), sedangkan 1,0 juta orang lainnya puas dengan jam kerjanya (pekerja paruh waktu sukarela). Di samping itu, berdasarkan audit status pekerjaan, terdapat 3,5 juta pekerja berstatus informal (pekerja bebas, pekerja keluarga, dan pedagang keliling mandiri) dan 3,5 juta pekerja formal. Hitunglah: (1) Tingkat Setengah Pengangguran (TSP), (2) Tingkat Pekerja Paruh Waktu (TPPW), dan (3) Proporsi Tenaga Kerja Informal.",
            "data_table": "| Klasifikasi Pekerja | Jumlah (Juta Jiwa) | Pembagi Resmi BPS |\n|---|---|---|\n| Bekerja Penuh (>= 35 Jam) | 5,0 | Penduduk Bekerja (PB = 7,0) |\n| Setengah Penganggur (< 35 Jam, Masih Mencari) | 1,0 | Penduduk Bekerja (PB = 7,0) |\n| Pekerja Paruh Waktu (< 35 Jam, Sukarela) | 1,0 | Penduduk Bekerja (PB = 7,0) |\n| Pekerja Sektor Informal | 3,5 | Penduduk Bekerja (PB = 7,0) |\n| Total Penduduk Bekerja (PB) | 7,0 | - |",
            "step_by_step_solution": "1. Menghitung Tingkat Setengah Pengangguran (TSP):\n   $$\\text{TSP} = \\frac{1,0}{7,0} \\times 100\\% = 14,2857\\% \\approx 14,29\\%$$\n2. Menghitung Tingkat Pekerja Paruh Waktu (TPPW):\n   $$\\text{TPPW} = \\frac{1,0}{7,0} \\times 100\\% = 14,2857\\% \\approx 14,29\\%$$\n3. Menghitung Proporsi Tenaga Kerja Informal:\n   $$\\text{Proporsi INF} = \\frac{3,5}{7,0} \\times 100\\% = 50,00\\%$$",
            "python_verification_code": "pb = 7.0\nsetengah_penganggur = 1.0\nparuh_waktu = 1.0\ninformal = 3.5\ntsp = (setengah_penganggur / pb) * 100.0\ntppw = (paruh_waktu / pb) * 100.0\np_inf = (informal / pb) * 100.0\nprint(f'TSP={tsp:.2f}%, TPPW={tppw:.2f}%, Proporsi Informal={p_inf:.2f}%')",
            "expected_output": "TSP=14.29%, TPPW=14.29%, Proporsi Informal=50.00%"
        },
        "exam_pitfalls": [
            {
                "trap_description": "Kesalahan Pembagi TSP/TPPW Menggunakan Angkatan Kerja",
                "common_mistake": "Membagi jumlah setengah penganggur (1.0) dengan total angkatan kerja (9.0) sehingga memperoleh angka salah 11.11%.",
                "safe_strategy": "Pembagi TSP dan TPPW adalah mutlak PENDUDUK BEKERJA (PB = 7.0 juta), bukan Angkatan Kerja (AK)."
            },
            {
                "trap_description": "Menyamakan Setengah Penganggur dengan Pekerja Paruh Waktu",
                "common_mistake": "Menganggap semua orang yang bekerja < 35 jam sebagai setengah penganggur.",
                "safe_strategy": "Setengah penganggur mensyaratkan kondisi keterpaksaan (masih mencari kerja/tambahan), sedangkan pekerja paruh waktu bersifat sukarela."
            }
        ],
        "textbook": "Official Statistics Lanjutan (OSL)",
        "chapter_id": 9,
        "chapter_title": "Pertemuan 9: Ketenagakerjaan dan Pendidikan",
        "section": "9.1 Kerangka Ketenagakerjaan ICLS 13 dan Konsep BPS",
        "mode": "deep",
        "points": [
            {
                "id": "9.1.4",
                "name": "Setengah Penganggur vs Pekerja Paruh Waktu",
                "importance": "高",
                "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 17-20, 24-28]",
                "exam_focus": "Batas 35 jam kerja normal, perbedaan esensial voluntary vs involuntary part-time, pembagi resmi PB, dan penentuan klasifikasi formal vs informal BPS (EXT-1).",
                "textbook_excerpt": "Persentase Setengah Pengangguran: TSP = PBJK<35 / PB * 100, dimana PBJK<35 = Jumlah pekerja setengah penganggur, PB = Jumlah penduduk yang bekerja [slide 17]. Kondef: Pekerja setengah pengangguran adalah mereka yang bekerja di bawah jam kerja normal (< 35 jam seminggu) dan masih mencari pekerjaan atau masih bersedia menerima pekerjaan (dahulu disebut setengah pengangguran terpaksa) [slide 18]. Persentase Pekerja Paruh Waktu: TPPW = PBPW / PB * 100 [slide 19]. Kondef: Pekerja paruh waktu adalah mereka yang bekerja di bawah jam kerja normal (< 35 jam seminggu), tetapi tidak mencari pekerjaan atau tidak bersedia menerima pekerjaan lain (dahulu disebut setengah pengangguran sukarela) [slide 20]. Proporsi Lapangan Kerja Informal: Pr PB INF = PB INF / PB * 100 [slide 27].",
                "intuition": "Seorang guru les privat yang mengajar 15 jam seminggu dan merasa waktu itu sudah cukup karena ingin fokus merawat keluarga adalah Pekerja Paruh Waktu. Namun seorang buruh pabrik garmen yang jam kerjanya dipangkas manajemen menjadi 20 jam seminggu dan terus melamar kerja sampingan ke sana ke mari adalah Setengah Penganggur. Keduanya bekerja < 35 jam, tetapi status ekonominya sangat bertolak belakang.",
                "formal": "### 1. Perbandingan Karakteristik Jam Kerja Rendah\n\nBerdasarkan pedoman operasional BPS [slide 17-20]:\n\n| Dimensi | Setengah Penganggur (*Underemployed*) | Pekerja Paruh Waktu (*Part-Time*) |\n|---|---|---|\n| **Ambang Jam Kerja** | $< 35$ jam seminggu [slide 18] | $< 35$ jam seminggu [slide 20] |\n| **Sifat Keterlibatan** | Terpaksa (*Involuntary*) | Sukarela (*Voluntary*) |\n| **Pencarian Kerja Tambahan** | **Ya**, aktif mencari atau bersedia menerima pekerjaan tambahan | **Tidak**, tidak mencari dan tidak bersedia menerima pekerjaan lain |\n| **Formula Rasio Resmi** | $\\text{TSP} = \\frac{\\text{PBJK}_{<35}}{\\text{PB}} \\times 100\\%$ [slide 17] | $\\text{TPPW} = \\frac{\\text{PBPW}}{\\text{PB}} \\times 100\\%$ [slide 19] |\n| **Penyebut / Pembagi** | **Penduduk Bekerja (PB)** | **Penduduk Bekerja (PB)** |\n| **Implikasi Kebijakan** | Sinyal kegagalan utilisasi kapasitas tenaga kerja penuh | Kebutuhan fleksibilitas pasar kerja dan keseimbangan kerja-keluarga |\n\n### 2. Klasifikasi Tenaga Kerja Formal vs Informal (EXT-1)\n\nBPS membagi status pekerjaan utama ke dalam 7 kategori yang kemudian dipetakan menjadi Formal dan Informal melalui **Proxy 2** [slide 26, 28]:\n\n| No | Status Pekerjaan Utama BPS | Klasifikasi Formal / Informal |\n|---|---|---|\n| 1 | Berusaha sendiri | Dipilah: Formal jika profesional/manajerial; Informal jika penjualan/jasa kasar [slide 26] |\n| 2 | Berusaha dibantu buruh tidak tetap/buruh tidak dibayar | Dipilah: Formal jika non-pertanian teknis; Informal jika pertanian/buruh [slide 26] |\n| 3 | Berusaha dibantu buruh tetap/buruh dibayar | **Pasti Formal (F)** |\n| 4 | Buruh / Karyawan / Pegawai | **Pasti Formal (F)** |\n| 5 | Pekerja bebas di sektor pertanian | **Pasti Informal (INF)** |\n| 6 | Pekerja bebas di sektor non-pertanian | **Pasti Informal (INF)** |\n| 7 | Pekerja keluarga / tidak dibayar (*unpaid worker*) | **Pasti Informal (INF)** |\n\nFormula Proporsi Lapangan Kerja Informal [slide 27]:\n$$\\text{Proporsi INF} = \\frac{\\text{Jumlah Penduduk Bekerja Status Informal (PB}_{\\text{INF}})}{\\text{Total Penduduk Bekerja (PB)}} \\times 100\\%$$",
                "pitfalls": "Menggunakan pembagi PUK atau Angkatan Kerja saat menghitung persentase pekerja informal. Seluruh indikator kualitas kerja (TSP, TPPW, Proporsi Informal) menggunakan pembagi PENDUDUK BEKERJA (PB).",
                "memory_hook": "Pembeda 35 Jam: Masih cari kerja = Setengah Penganggur (TSP). Puas/sukarela = Paruh Waktu (TPPW). Pembagi selalu Penduduk Bekerja (PB).",
                "examples": [
                    {
                        "type": "single",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 17-20]",
                        "problem": "Dalam analisis pasar kerja BPS, perbedaan fundamental antara pekerja setengah penganggur dan pekerja paruh waktu terletak pada:",
                        "options": [
                            "Ambang batas jumlah jam kerja kumulatif selama seminggu terakhir.",
                            "Tingkat upah atau kompensasi finansial yang diterima per jam kerja.",
                            "Kesediaan atau upaya aktif untuk mencari pekerjaan tambahan di bawah jam kerja normal.",
                            "Klasifikasi kepemilikan izin usaha resmi tempat mereka bekerja."
                        ],
                        "answer": 2,
                        "solution": "Jawaban: **C**.\n\n**Pembahasan**:\nKedua kelompok sama-sama bekerja di bawah jam kerja normal (< 35 jam seminggu). Perbedaan penentu menurut BPS adalah kesediaan atau upaya mencari pekerjaan tambahan: Setengah penganggur bersedia/mencari kerja tambahan (*involuntary*), sedangkan pekerja paruh waktu tidak mencari pekerjaan tambahan (*voluntary*)."
                    },
                    {
                        "type": "text",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 17, 27]",
                        "problem": "Di sebuah kabupaten agraris, terdapat 80.000 penduduk bekerja. Dari jumlah tersebut, 20.000 orang bekerja < 35 jam seminggu dengan rincian 8.000 orang masih mencari kerja tambahan dan 12.000 orang tidak mencari kerja tambahan. Selain itu, terdapat 48.000 orang yang bekerja pada sektor informal. Hitunglah Tingkat Setengah Pengangguran (TSP) dan Proporsi Tenaga Kerja Informal. Tuliskan jawaban dalam format: `TSP=X.X%, Informal=Y.Y%`.",
                        "answer": "TSP=10.0%, Informal=60.0%",
                        "solution": "Langkah-langkah perhitungan:\n1. Tingkat Setengah Pengangguran (TSP):\n   $$\\text{TSP} = \\frac{8.000}{80.000} \\times 100\\% = 10,0\\%$$\n2. Proporsi Tenaga Kerja Informal:\n   $$\\text{Proporsi INF} = \\frac{48.000}{80.000} \\times 100\\% = 60,0\\%$$\n\n**Verifikasi Kode Python**:\n```python\npb = 80000\nsetengah_p = 8000\ninformal = 48000\ntsp = (setengah_p / pb) * 100\np_inf = (informal / pb) * 100\nprint(f'TSP={tsp:.1f}%, Informal={p_inf:.1f}%')\n# Output: TSP=10.0%, Informal=60.0%\n```"
                    }
                ],
                "links": ["9.1.1", "9.1.2", "9.1.3"]
            }
        ]
    },
    {
        "filename": "9.2.1-angka-partisipasi-murni-apm-dan-kasar-apk.json",
        "point_id": "9.2.1",
        "title": "Angka Partisipasi Murni APM dan Kasar APK",
        "importance": "高",
        "curriculum_alignment": {
            "pertemuan": 9,
            "silabus_topic": "Ketenagakerjaan dan Pendidikan",
            "bps_subject": "Indikator Pendidikan"
        },
        "grounding": {
            "primary_sources": [
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "66-71",
                    "content": "Definisi, formula, dan interpretasi Angka Partisipasi Kasar (APK) dan Angka Partisipasi Murni (APM) per jenjang sekolah (SD, SMP, SMA, PT), kondisi APM <= 100%, APM <= APK, dan kemungkinan APK > 100%."
                },
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "51-55",
                    "content": "Indikator pendidikan untuk SDGs 4 dalam Susenas (Target 4.1 APK pendidikan dasar & menengah, Target 4.2 APK PAUD, Target 4.5 Rasio gender APM/APK)."
                }
            ],
            "supplemental_sources": [],
            "coverage_status": "COVERED"
        },
        "theory": {
            "intuition": "APM mengukur ketepatan usia siswa pada jenjang pendidikannya (apakah anak usia SD bersekolah tepat di SD). Sebaliknya, APK mengukur daya tampung atau kapasitas fisik sistem pendidikan pada jenjang tertentu tanpa memedulikan umur siswa (berapa total kursi siswa yang terisi di SD dibandingkan jumlah anak usia SD). Oleh karena itu, jika ada murid yang masuk sekolah lebih awal (usia dini) atau terlambat/mengulang kelas, pembilang APK akan membengkak sehingga nilai APK dapat melampaui 100%, sementara APM tidak pernah bisa melebihi 100%.",
            "bps_definition": "Angka Partisipasi Murni (APM) adalah proporsi anak kelompok usia sekolah tertentu yang sedang bersekolah tepat di jenjang pendidikan yang seharusnya terhadap penduduk kelompok usia sekolah yang bersangkutan. Angka Partisipasi Kasar (APK) adalah rasio antara jumlah siswa yang bersekolah di suatu jenjang pendidikan tertentu (tanpa memandang usia) terhadap jumlah penduduk kelompok usia sekolah resmi pada jenjang yang sama. Sejak 2007, Susenas turut memperhitungkan Pendidikan Non-Formal (Paket A, Paket B, dan Paket C).",
            "boundary_conditions": "1. Kondisi Batas Matematika Kritis:\n   - $\\text{APM} \\le \\text{APK}$ (selalu berlaku karena pembilang APM adalah bagian himpunan bagian dari pembilang APK).\n   - $\\text{APM} \\le 100\\%$ (mutlak secara teoritis).\n   - $\\text{APK}$ dapat $> 100\\%$ jika terdapat pendaftaran usia dini, terlambat masuk, atau pengulangan kelas.\n2. Kelompok umur resmi jenjang BPS: SD (7-12 tahun), SMP (13-15 tahun), SMA/SMK (16-18 tahun), Perguruan Tinggi (19-24 tahun).",
            "formula_latex": "$$\\text{APM}_J = \\frac{S_{J, \\text{usia } J}}{P_{\\text{usia } J}} \\times 100\\%, \\quad \\text{APK}_J = \\frac{\\sum_{\\text{semua umur}} S_J}{P_{\\text{usia } J}} \\times 100\\%$$"
        },
        "numerical_example": {
            "problem_statement": "Verifikasi Batas Kritis BVA Pendidikan (test_bva_06): Di suatu distrik pendidikan, populasi anak usia resmi sekolah dasar (7-12 tahun) berjumlah 1.000 orang. Data dinas pendidikan mencatat total siswa yang terdaftar di jenjang SD adalah 1.060 anak, yang terdiri atas 40 anak berusia di bawah 7 tahun (masuk dini), 920 anak berusia 7-12 tahun (usia tepat jenjang), dan 100 anak berusia di atas 12 tahun (tinggal kelas/terlambat). Hitunglah nilai APM SD dan APK SD distrik tersebut, serta buktikan kondisi batas APM <= 100%, APM <= APK, dan APK > 100%!",
            "data_table": "| Komponen Siswa / Penduduk | Jumlah Anak |\n|---|---|\n| Penduduk Usia Resmi SD (7-12 Tahun) | 1.000 |\n| Siswa SD Berusia Tepat (7-12 Tahun) | 920 |\n| Siswa SD Berusia Dini (< 7 Tahun) | 40 |\n| Siswa SD Berusia Lebih (> 12 Tahun) | 100 |\n| Total Seluruh Siswa Terdaftar di SD | 1.060 |",
            "step_by_step_solution": "1. Menghitung Angka Partisipasi Murni (APM) SD:\n   $$\\text{APM}_{\\text{SD}} = \\frac{\\text{Siswa SD Usia 7-12}}{\\text{Penduduk Usia 7-12}} \\times 100\\% = \\frac{920}{1.000} \\times 100\\% = 92,00\\%$$\n2. Menghitung Angka Partisipasi Kasar (APK) SD:\n   $$\\text{APK}_{\\text{SD}} = \\frac{\\text{Total Siswa Terdaftar di SD}}{\\text{Penduduk Usia 7-12}} \\times 100\\% = \\frac{1.060}{1.000} \\times 100\\% = 106,00\\%$$\n3. Verifikasi Kondisi Batas Matematika BPS:\n   - $\\text{APM} = 92,00\\% \\le 100\\%$ (Terpenuhi)\n   - $\\text{APM} (92,00\\%) \\le \\text{APK} (106,00\\%)$ (Terpenuhi)\n   - $\\text{APK} = 106,00\\% > 100\\%$ (Menunjukkan kapasitas sistem menampung siswa di luar usia standar)",
            "python_verification_code": "pop_7_12 = 1000\nsd_usia_tepat = 920\nsd_total = 1060\napm = (sd_usia_tepat / pop_7_12) * 100.0\napk = (sd_total / pop_7_12) * 100.0\ncond1 = (apm <= 100.0)\ncond2 = (apm <= apk)\ncond3 = (apk > 100.0)\nprint(f'APM={apm:.2f}%, APK={apk:.2f}%, APM<=APK={cond2}, APK>100={cond3}')",
            "expected_output": "APM=92.00%, APK=106.00%, APM<=APK=True, APK>100=True"
        },
        "exam_pitfalls": [
            {
                "trap_description": "Mengira Nilai APK di Atas 100% Merupakan Kesalahan Hitung",
                "common_mistake": "Menganggap hasil hitungan APK sebesar 106% sebagai anomali atau data salah.",
                "safe_strategy": "APK > 100% adalah fenomena lumrah dan sahih dalam statistik BPS karena pembilang mencakup murid di luar batas usia standar."
            },
            {
                "trap_description": "Tertukar Pembilang APM dan APK",
                "common_mistake": "Memasukkan total seluruh murid ke dalam rumus APM.",
                "safe_strategy": "APM = Murni (hanya murid yang berumur sesuai jenjang). APK = Kasar (seluruh murid tanpa memandang umur)."
            }
        ],
        "textbook": "Official Statistics Lanjutan (OSL)",
        "chapter_id": 9,
        "chapter_title": "Pertemuan 9: Ketenagakerjaan dan Pendidikan",
        "section": "9.2 Indikator Pendidikan",
        "mode": "deep",
        "points": [
            {
                "id": "9.2.1",
                "name": "Angka Partisipasi Murni APM dan Kasar APK",
                "importance": "高",
                "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 66-71]",
                "exam_focus": "Definisi perbedaan pembilang APM vs APK, rentang usia resmi 4 jenjang sekolah, pembuktian ketidaksamaan APM <= APK dan batas APK > 100%, serta aplikasi pada neraca pendidikan BPS.",
                "textbook_excerpt": "APK SD = Jumlah murid SD / Jumlah penduduk usia 7-12 tahun * 100 [slide 66]. Kondef: Perbandingan antara jumlah penduduk yang masih bersekolah di jenjang pendidikan tertentu (tanpa memandang usia) dengan jumlah penduduk yang memenuhi syarat resmi usia sekolah di jenjang pendidikan yang sama [slide 67]. Nilai APK bisa lebih dari 100 persen karena populasi murid mencakup anak di luar batas usia sekolah. Penyebabnya adalah pendaftaran usia dini, terlambat sekolah, atau pengulangan kelas [slide 67]. APM SD = Jumlah murid SD umur 7-12 tahun / Jumlah penduduk usia 7-12 tahun * 100 [slide 69]. Nilai APM berkisar antara 0-100. Secara umum, APM akan selalu lebih rendah dari APK [slide 70].",
                "intuition": "Jika sebuah bus sekolah berkapasitas 50 kursi diisi oleh 53 penumpang (termasuk beberapa balita dan orang dewasa yang ikut menumpang), rasio penumpangnya melebihi 100% kapasitas resmi (ini analogi APK). Namun jika kita hanya menghitung anak-anak pemegang tiket resmi di dalam bus tersebut, jumlahnya tidak akan pernah melebihi 100% (ini analogi APM).",
                "formal": "### 1. Formulasi Matematis APM dan APK menurut Jenjang Sekolah\n\nBerdasarkan klasifikasi resmi Kemendikbudristek dan BPS [slide 62, 66, 69]:\n\n| Jenjang Pendidikan ($J$) | Rentang Usia Resmi | Formula APM (Murni) | Formula APK (Kasar) |\n|---|---|---|---|\n| **SD / MI / Paket A** | 7 - 12 Tahun | $\\text{APM}_{\\text{SD}} = \\frac{\\text{Murid SD Usia 7-12}}{P_{7-12}} \\times 100\\%$ [slide 69] | $\\text{APK}_{\\text{SD}} = \\frac{\\sum \\text{Murid SD}}{P_{7-12}} \\times 100\\%$ [slide 66] |\n| **SMP / MTs / Paket B** | 13 - 15 Tahun | $\\text{APM}_{\\text{SMP}} = \\frac{\\text{Murid SMP Usia 13-15}}{P_{13-15}} \\times 100\\%$ [slide 69] | $\\text{APK}_{\\text{SMP}} = \\frac{\\sum \\text{Murid SMP}}{P_{13-15}} \\times 100\\%$ [slide 66] |\n| **SMA / SMK / MA / Paket C** | 16 - 18 Tahun | $\\text{APM}_{\\text{SM}} = \\frac{\\text{Murid SMA Usia 16-18}}{P_{16-18}} \\times 100\\%$ [slide 69] | $\\text{APK}_{\\text{SM}} = \\frac{\\sum \\text{Murid SMA}}{P_{16-18}} \\times 100\\%$ [slide 66] |\n| **Perguruan Tinggi (PT)** | 19 - 24 Tahun | $\\text{APM}_{\\text{PT}} = \\frac{\\text{Mhs PT Usia 19-24}}{P_{19-24}} \\times 100\\%$ [slide 69] | $\\text{APK}_{\\text{PT}} = \\frac{\\sum \\text{Mahasiswa PT}}{P_{19-24}} \\times 100\\%$ [slide 66] |\n\n### 2. Teorema Hubungan APM dan APK\n\nMisalkan himpunan seluruh siswa yang bersekolah pada jenjang $J$ adalah $S_J$. Himpunan siswa usia tepat adalah $S_J^* = \\{s \\in S_J \\mid \\text{Usia}(s) \\in \\text{Rentang}(J)\\}$. Himpunan siswa di luar usia standar adalah $S_J^{\\text{luar}} = S_J \\setminus S_J^*$.\n\nKarena $|S_J| = |S_J^*| + |S_J^{\\text{luar}}|$ dan $|S_J^{\\text{luar}}| \\ge 0$, maka:\n$$|S_J^*| \\le |S_J|$$\nDengan membagi kedua sisi dengan jumlah penduduk kelompok usia resmi $P_{\\text{usia } J} > 0$ dan mengalikan 100%, diperoleh:\n$$\\text{APM}_J \\le \\text{APK}_J$$\n\nSelisih antara APK dan APM ($\\text{APK} - \\text{APM}$) mengukur besarnya proporsi penduduk yang bersekolah tidak tepat waktu (*overage and underage enrollment ratio*).",
                "pitfalls": "Mengabaikan siswa pendidikan non-formal (Paket A, B, C). Sejak tahun 2007, BPS secara resmi memasukkan siswa program kesetaraan ke dalam perhitungan APM dan APK Susenas.",
                "memory_hook": "APM = Murni (Usia Tepat, <= 100%). APK = Kasar (Semua Usia, Bisa > 100%). APM <= APK selalu.",
                "examples": [
                    {
                        "type": "single",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 67, 70]",
                        "problem": "Jika di suatu provinsi nilai APK jenjang Sekolah Menengah Pertama (SMP) tercatat sebesar 104,5% dan nilai APM SMP tercatat sebesar 82,3%, maka kesimpulan yang paling tepat adalah:",
                        "options": [
                            "Terjadi kesalahan pendataan lapangan pada Susenas karena partisipasi tidak mungkin melebihi 100%.",
                            "Terdapat 22,2% anak usia 13-15 tahun yang tidak tertampung di fasilitas pendidikan SMP.",
                            "Kapasitas sekolah SMP mampu menampung siswa melebihi populasi usia 13-15 tahun karena adanya siswa usia dini atau siswa yang mengulang.",
                            "Seluruh anak usia 13-15 tahun di provinsi tersebut telah bersekolah tepat waktu di jenjang SMP."
                        ],
                        "answer": 2,
                        "solution": "Jawaban: **C**.\n\n**Pembahasan**:\nNilai APK > 100% mengindikasikan bahwa daya tampung sekolah jenjang tersebut mencakup siswa di luar usia 13-15 tahun (misalnya siswa usia < 13 tahun yang cerdas istimewa atau usia > 15 tahun yang terlambat tamat SD/mengulang kelas). Selisih $104,5\\% - 82,3\\% = 22,2\\%$ mencerminkan proporsi siswa di luar usia standar yang bersekolah di SMP."
                    },
                    {
                        "type": "text",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 66, 69]",
                        "problem": "Sebuah kota memiliki 50.000 penduduk usia 16-18 tahun. Dari hasil pendataan sekolah jenjang SMA/SMK, terdaftar 32.000 siswa berusia 16-18 tahun, 1.000 siswa berusia 15 tahun (akselerasi), dan 7.000 siswa berusia di atas 18 tahun. Hitunglah APM dan APK jenjang SMA/SMK kota tersebut. Tuliskan jawaban dalam format: `APM=X.X%, APK=Y.Y%`.",
                        "answer": "APM=64.0%, APK=80.0%",
                        "solution": "Langkah-langkah perhitungan:\n1. Menghitung APM SMA:\n   $$\\text{APM}_{\\text{SMA}} = \\frac{32.000}{50.000} \\times 100\\% = 64,0\\%$$\n2. Menghitung total murid SMA:\n   $$\\sum \\text{Murid SMA} = 32.000 + 1.000 + 7.000 = 40.000$$\n3. Menghitung APK SMA:\n   $$\\text{APK}_{\\text{SMA}} = \\frac{40.000}{50.000} \\times 100\\% = 80,0\\%$$\n\n**Verifikasi Kode Python**:\n```python\npop = 50000\nsiswa_tepat = 32000\nsiswa_total = 32000 + 1000 + 7000\napm = (siswa_tepat / pop) * 100\napk = (siswa_total / pop) * 100\nprint(f'APM={apm:.1f}%, APK={apk:.1f}%')\n# Output: APM=64.0%, APK=80.0%\n```"
                    }
                ],
                "links": ["9.1.1", "9.2.2"]
            }
        ]
    },
    {
        "filename": "9.2.2-angka-partisipasi-sekolah-aps.json",
        "point_id": "9.2.2",
        "title": "Angka Partisipasi Sekolah APS",
        "importance": "高",
        "curriculum_alignment": {
            "pertemuan": 9,
            "silabus_topic": "Ketenagakerjaan dan Pendidikan",
            "bps_subject": "Indikator Pendidikan"
        },
        "grounding": {
            "primary_sources": [
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "61-65",
                    "content": "Definisi, formula, 4 kelompok umur standar APS (7-12, 13-15, 16-18, 19-24 tahun), data Susenas 2021 menurut gender, tipe daerah, dan kuintil ekonomi."
                },
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "57-60",
                    "content": "EXT-2: Angka Melek Huruf (AMH 15+), konsep membaca menulis kalimat sederhana, braille, dan data Susenas 2019-2021."
                },
                {
                    "file": "Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md",
                    "slide_or_page": "72-74",
                    "content": "EXT-2: Rata-rata Lama Sekolah (RLS / MYS), formula tahun belajar formal yang telah diselesaikan tanpa menghitung tahun mengulang."
                }
            ],
            "supplemental_sources": [],
            "coverage_status": "COVERED"
        },
        "theory": {
            "intuition": "Jika APM bertanya 'apakah kamu sekolah di jenjang yang benar?', maka APS bertanya lebih mendasar: 'apakah kamu sekolah atau tidak, di jenjang mana pun itu?'. APS memantau hak asasi anak untuk menikmati fasilitas pendidikan formal/kesetaraan pada kelompok umurnya tanpa menghakimi apakah anak tersebut tertinggal kelas atau mengalami percepatan belajar. Indikator outcome pendidikan dalam IPM melengkapinya melalui Angka Melek Huruf (AMH 15+) dan Rata-rata Lama Sekolah (RLS).",
            "bps_definition": "Angka Partisipasi Sekolah (APS) adalah proporsi dari semua anak yang masih bersekolah pada suatu kelompok umur tertentu terhadap jumlah penduduk dengan kelompok umur yang sesuai, tanpa memandang jenjang pendidikan yang sedang ditempuh. Angka Melek Huruf (AMH 15+) adalah persentase penduduk usia 15 tahun ke atas yang dapat membaca dan menulis kalimat sederhana. Rata-rata Lama Sekolah (RLS) adalah jumlah tahun belajar penduduk usia 15 tahun ke atas yang telah diselesaikan dalam pendidikan formal tanpa mengulang.",
            "boundary_conditions": "1. Pada APS, jenjang pendidikan tidak dipedulikan: murid usia 13-15 tahun yang masih duduk di bangku SD tetap dihitung dalam pembilang APS 13-15 tahun.\n2. Hubungan hirarkis indikator partisipasi: $\\text{APM}_J \\le \\text{APS}_{\\text{Usia}(J)} \\le 100\\%$.\n3. Aturan RLS: Tahun mengulang kelas (tinggal kelas) TIDAK dihitung sebagai penambah tahun belajar formal.",
            "formula_latex": "$$\\text{APS}_{x-y} = \\frac{\\sum \\text{Siswa Bersekolah Usia } x-y}{P_{x-y}} \\times 100\\%, \\quad \\text{AMH}_{15+} = \\frac{\\text{MH}_{15+}}{P_{15+}} \\times 100\\%$$"
        },
        "numerical_example": {
            "problem_statement": "Di sebuah perdesaan terpencil terdapat 500 orang penduduk berusia 13-15 tahun (usia kelompok SMP). Berdasarkan pencacahan Susenas: 380 anak bersekolah tepat di jenjang SMP/MTs, 40 anak masih duduk di bangku SD karena terlambat masuk, 10 anak bersekolah akselerasi di jenjang SMA, dan 70 anak sudah putus sekolah. Di samping itu, dari 2.000 penduduk usia 15 tahun ke atas, terdapat 1.900 orang yang melek huruf. Hitunglah: (1) Total anak usia 13-15 tahun yang masih bersekolah, (2) APS 13-15 tahun, (3) APM SMP, dan (4) AMH 15+ desa tersebut!",
            "data_table": "| Kelompok Penduduk / Siswa | Jumlah Jiwa |\n|---|---|\n| Penduduk Usia 13-15 Tahun | 500 |\n| Siswa Usia 13-15 di Jenjang SMP/MTs | 380 |\n| Siswa Usia 13-15 di Jenjang SD | 40 |\n| Siswa Usia 13-15 di Jenjang SMA | 10 |\n| Anak Usia 13-15 Tidak Bersekolah Lagi | 70 |\n| Penduduk Usia 15 Tahun ke Atas (P15+) | 2.000 |\n| Penduduk Usia 15+ yang Melek Huruf (MH15+) | 1.900 |",
            "step_by_step_solution": "1. Menghitung Total Penduduk 13-15 Tahun yang Masih Bersekolah:\n   $$\\text{Total Siswa}_{13-15} = 380 (\\text{SMP}) + 40 (\\text{SD}) + 10 (\\text{SMA}) = 430 \\text{ anak}$$\n2. Menghitung Angka Partisipasi Sekolah (APS 13-15):\n   $$\\text{APS}_{13-15} = \\frac{430}{500} \\times 100\\% = 86,00\\%$$\n3. Menghitung Angka Partisipasi Murni (APM SMP):\n   $$\\text{APM}_{\\text{SMP}} = \\frac{380}{500} \\times 100\\% = 76,00\\%$$\n   *Buktinya: $\\text{APM SMP} (76,00\\%) \\le \\text{APS}_{13-15} (86,00\\%)$ terpenuhi.*\n4. Menghitung Angka Melek Huruf (AMH 15+):\n   $$\\text{AMH}_{15+} = \\frac{1.900}{2.000} \\times 100\\% = 95,00\\%$$",
            "python_verification_code": "pop_13_15 = 500\nsmp_tepat = 380\nsd_tertinggal = 40\nsma_akselerasi = 10\ntotal_sekolah = smp_tepat + sd_tertinggal + sma_akselerasi\naps = (total_sekolah / pop_13_15) * 100.0\napm_smp = (smp_tepat / pop_13_15) * 100.0\npokok_15 = 2000\nmh_15 = 1900\namh = (mh_15 / pokok_15) * 100.0\nprint(f'Total Sekolah={total_sekolah}, APS={aps:.2f}%, APM SMP={apm_smp:.2f}%, AMH={amh:.2f}%')",
            "expected_output": "Total Sekolah=430, APS=86.00%, APM SMP=76.00%, AMH=95.00%"
        },
        "exam_pitfalls": [
            {
                "trap_description": "Mengecualikan Siswa di Luar Jenjang Standar dalam Pembilang APS",
                "common_mistake": "Hanya menghitung siswa yang duduk di SMP saat menghitung APS 13-15 tahun sehingga mendapatkan hasil 380/500 = 76% (ini nilai APM, bukan APS).",
                "safe_strategy": "APS tidak peduli jenjang sekolah: anak usia 13-15 tahun yang duduk di SD maupun SMA wajib dihitung dalam pembilang APS."
            },
            {
                "trap_description": "Memasukkan Tahun Mengulang Kelas ke dalam RLS (MYS)",
                "common_mistake": "Menambahkan tahun tinggal kelas ke dalam akumulasi Rata-rata Lama Sekolah.",
                "safe_strategy": "Konsep baku BPS secara tegas mengecualikan tahun mengulang dalam perhitungan Rata-rata Lama Sekolah."
            }
        ],
        "textbook": "Official Statistics Lanjutan (OSL)",
        "chapter_id": 9,
        "chapter_title": "Pertemuan 9: Ketenagakerjaan dan Pendidikan",
        "section": "9.2 Indikator Pendidikan",
        "mode": "deep",
        "points": [
            {
                "id": "9.2.2",
                "name": "Angka Partisipasi Sekolah APS",
                "importance": "高",
                "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 61-65, 57-60, 72-74]",
                "exam_focus": "Formula 4 kelompok usia APS, komparasi analitis APM vs APK vs APS, integrasi indikator pendidikan IPM (AMH 15+ dan RLS/MYS) (EXT-2).",
                "textbook_excerpt": "ANGKA PARTISIPASI SEKOLAH (APS): APS 7-12 = Jumlah penduduk 7-12 tahun bersekolah / Jumlah penduduk usia 7-12 tahun * 100 [slide 63]. Kondef: Proporsi dari semua anak yang masih sekolah pada suatu kelompok umur tertentu terhadap penduduk dengan kelompok umur yang sesuai. Sejak 2009 Pendidikan Non Formal turut diperhitungkan [slide 64]. Angka Melek Huruf: AMH15+ = MH15+ / P15+ * 100 [slide 58]. Kondef: Proporsi penduduk berusia 15 tahun ke atas yang memiliki kemampuan membaca dan menulis kalimat sederhana dalam huruf latin/arab/lainnya [slide 59]. Rata-rata Lama Sekolah (MYS): Jumlah tahun belajar penduduk usia 15 tahun ke atas yang telah diselesaikan dalam pendidikan formal (tidak termasuk tahun yang mengulang) [slide 73].",
                "intuition": "Jika ada sensus di suatu RT, petugas hanya bertanya kepada anak usia 14 tahun: 'Adik masih sekolah atau sudah berhenti?'. Petugas tidak peduli apakah si adik masih kelas 6 SD atau sudah kelas 1 SMA. Selama dia masih aktif sekolah, dia dihitung dalam APS kelompok 13-15 tahun.",
                "formal": "### 1. Formulasi Matematis Empat Kelompok Usia APS\n\nBPS membagi APS ke dalam 4 kelompok umur standar yang bersesuaian dengan jenjang wajar Dikdasmen dan Dikti [slide 63]:\n\n$$\\text{APS}_{7-12} = \\frac{\\text{Penduduk usia 7-12 tahun masih bersekolah}}{\\text{Jumlah penduduk usia 7-12 tahun}} \\times 100\\%$$\n$$\\text{APS}_{13-15} = \\frac{\\text{Penduduk usia 13-15 tahun masih bersekolah}}{\\text{Jumlah penduduk usia 13-15 tahun}} \\times 100\\%$$\n$$\\text{APS}_{16-18} = \\frac{\\text{Penduduk usia 16-18 tahun masih bersekolah}}{\\text{Jumlah penduduk usia 16-18 tahun}} \\times 100\\%$$\n$$\\text{APS}_{19-24} = \\frac{\\text{Penduduk usia 19-24 tahun masih bersekolah}}{\\text{Jumlah penduduk usia 19-24 tahun}} \\times 100\\%$$\n\n### 2. Matriks Komparasi Segitiga Partisipasi Pendidikan: APM vs APK vs APS\n\n| Aspek Pembeda | Angka Partisipasi Murni (APM) | Angka Partisipasi Kasar (APK) | Angka Partisipasi Sekolah (APS) |\n|---|---|---|---|\n| **Fokus Utama** | Ketepatan usia sekolah (*on-time schooling*) [slide 70] | Kapasitas/daya tampung sekolah (*capacity*) [slide 67] | Akses riil penduduk usia sekolah (*access*) [slide 64] |\n| **Pembilang** | Siswa usia resmi pada jenjang yang sesuai | Seluruh siswa di jenjang tsb (semua umur) | Seluruh anak pada usia tsb yang sekolah (semua jenjang) |\n| **Penyebut** | Penduduk kelompok umur jenjang tsb | Penduduk kelompok umur jenjang tsb | Penduduk kelompok umur tsb |\n| **Rentang Nilai** | $0\\% \\le \\text{APM} \\le 100\\%$ | Bisa $> 100\\%$ | $0\\% \\le \\text{APS} \\le 100\\%$ |\n| **Sifat Relatif** | $\\text{APM} \\le \\text{APK}$ dan $\\text{APM} \\le \\text{APS}$ | APK bisa paling tinggi di antara ketiganya | Selalu lebih besar atau sama dengan APM |\n\n### 3. Indikator Komposit Pendidikan IPM (EXT-2)\n\nDalam mengukur dimensi pengetahuan pada Indeks Pembangunan Manusia (IPM) BPS [slide 58, 73]:\n- **Angka Melek Huruf (AMH 15+)**: Mengukur stok keaksaraan dasar. Sejak metode baru IPM 2014, AMH digantikan oleh Harapan Lama Sekolah (HLS), namun AMH tetap menjadi indikator pemantauan SDGs Target 4.6 [slide 56, 58].\n- **Rata-rata Lama Sekolah (RLS / Mean Years of Schooling)**: Mengukur akumulasi modal manusia (*human capital stock*). Dihitung dari kombinasi ijazah tertinggi dan kelas tertinggi yang pernah diselesaikan, dengan syarat **tahun mengulang tidak dihitung** [slide 73].",
                "pitfalls": "Mengasumsikan APS bisa melebihi 100%. Berbeda dengan APK yang pembilangnya mencakup siswa lintas umur, pembilang APS adalah subset dari penyebutnya (hanya anak-anak pada kelompok umur tersebut yang bersekolah), sehingga APS secara matematis tidak pernah bisa melebihi 100%.",
                "memory_hook": "APS = Hak Sekolah pada Kelompok Umur (Tidak peduli jenjang). RLS = Tahun sekolah formal selesai (tidak termasuk mengulang).",
                "examples": [
                    {
                        "type": "single",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 62-64, 70]",
                        "problem": "Manakah pernyataan yang paling akurat mengenai perbandingan antara APM, APK, dan APS untuk kelompok jenjang SMP (usia 13-15 tahun)?",
                        "options": [
                            "Nilai APS 13-15 tahun selalu lebih kecil atau sama dengan APM SMP.",
                            "Nilai APM SMP selalu lebih kecil atau sama dengan APS 13-15 tahun.",
                            "Nilai APK SMP tidak mungkin lebih besar daripada APS 13-15 tahun.",
                            "Nilai APS 13-15 tahun dapat melebihi 100% jika banyak siswa mengulang kelas."
                        ],
                        "answer": 1,
                        "solution": "Jawaban: **B**.\n\n**Pembahasan**:\n- Pembilang APM SMP hanya menghitung anak usia 13-15 tahun yang bersekolah di SMP.\n- Pembilang APS 13-15 tahun menghitung seluruh anak usia 13-15 tahun yang bersekolah di jenjang apa pun (SD, SMP, maupun SMA).\n- Karena pembilang APM adalah himpunan bagian dari pembilang APS, maka nilai $\\text{APM} \\le \\text{APS}$ mutlak selalu berlaku."
                    },
                    {
                        "type": "text",
                        "source_ref": "[Pertemuan_9_Indikator_Ketenagakerjaan_dan_Pendidikan.md, slide 58, 73]",
                        "problem": "Seseorang menempuh pendidikan SD selama 7 tahun (tinggal kelas 1 kali saat kelas 3), kemudian menyelesaikan SMP selama 3 tahun, SMA selama 3 tahun, dan kuliah D4/S1 selama 4 tahun hingga wisuda. Berdasarkan konsep BPS, berapakah Rata-rata Lama Sekolah (RLS) yang disumbangkan oleh individu tersebut? Tuliskan dalam format: `RLS=X tahun`.",
                        "answer": "RLS=16 tahun",
                        "solution": "Langkah-langkah perhitungan:\n1. Pendidikan yang diselesaikan:\n   - SD: 6 tahun jenjang resmi (tahun ke-7 adalah tahun mengulang).\n   - SMP: 3 tahun.\n   - SMA: 3 tahun.\n   - Perguruan Tinggi (S1): 4 tahun.\n2. Sesuai konsep baku BPS [slide 73], tahun yang mengulang TIDAK dihitung sebagai lama sekolah.\n3. Total tahun belajar yang diakui:\n   $$\\text{RLS} = 6 + 3 + 3 + 4 = 16 \\text{ tahun}$$\n\n**Verifikasi Kode Python**:\n```python\nsd_resmi = 6\nsmp = 3\nsma = 3\nperti = 4\nrls = sd_resmi + smp + sma + perti\nprint(f'RLS={rls} tahun')\n# Output: RLS=16 tahun\n```"
                    }
                ],
                "links": ["9.1.1", "9.2.1"]
            }
        ]
    }
]

for lesson in LESSONS:
    filename = lesson.pop("filename")
    target_path = CHAPTER_DIR / filename
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(lesson, f, indent=2, ensure_ascii=False)
    print(f"Generated: {target_path}")

print("All 6 lessons generated successfully!")
