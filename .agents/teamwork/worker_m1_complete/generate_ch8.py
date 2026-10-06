import json
import pathlib

ROOT = pathlib.Path("/home/alfzki/Documents/OSL")
LESSONS_DIR = ROOT / "internal" / "lessons" / "chapter-08"

# ---------------------------------------------------------------------------
# 1. UPDATE 8.1.1
# ---------------------------------------------------------------------------
f811 = LESSONS_DIR / "8.1.1-kemiskinan-absolut-relatif.json"
d811 = json.loads(f811.read_text(encoding="utf-8"))
d811.update({
    "point_id": "8.1.1",
    "title": "Konsep Kemiskinan Absolut dan Relatif",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Kemiskinan"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "4-13",
                "content": "Definisi kemiskinan absolut vs relatif, evolusi garis kemiskinan Purchasing Power Parity ($ PPP), dan respons indikator terhadap transformasi skala pendapatan."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Kemiskinan absolut mengukur batas fisik biologis kelangsungan hidup (garis statis riil), sedangkan kemiskinan relatif mengukur ketertinggalan ekonomi seseorang terhadap standar hidup rata-rata atau median masyarakat sekitarnya (garis dinamis mengikuti proporsi median).",
        "bps_definition": "Kemiskinan absolut adalah ketidakmampuan dari sisi ekonomi untuk memenuhi kebutuhan dasar makanan dan bukan makanan yang diukur dari sisi pengeluaran. Kemiskinan relatif diukur berdasarkan persentase penduduk dengan pendapatan/pengeluaran kurang dari proporsi tertentu (misal 50% atau 60%) terhadap median pendapatan masyarakat.",
        "boundary_conditions": "Kemiskinan absolut berkurang jika kue ekonomi tumbuh dan dinikmati kelompok di bawah garis kemiskinan riil. Kemiskinan relatif bersifat homogen berderajat nol (scale invariant): jika seluruh pengeluaran/pendapatan dikalikan konstanta positif c, persentase penduduk miskin relatif tidak berubah.",
        "formula_latex": "$$z_{\\text{abs}} = \\text{konstan riil}, \\quad z_{\\text{rel}} = k \\cdot \\text{Median}(Y), \\quad 0 < k < 1$$"
    },
    "numerical_example": {
        "problem_statement": "Terdapat data pengeluaran per kapita bulanan untuk 10 orang penduduk (dalam ribuan rupiah): [200, 250, 300, 350, 400, 500, 600, 700, 800, 1000]. Jika Garis Kemiskinan Absolut z_abs = 380 ribu rupiah dan Garis Kemiskinan Relatif z_rel = 70% dari median pengeluaran, tentukan jumlah dan persentase penduduk miskin absolut dan relatif.",
        "data_table": "| Individu | Pengeluaran (ribu Rp) |\n|---|---|\n| 1 | 200 |\n| 2 | 250 |\n| 3 | 300 |\n| 4 | 350 |\n| 5 | 400 |\n| 6 | 500 |\n| 7 | 600 |\n| 8 | 700 |\n| 9 | 800 |\n| 10 | 1000 |",
        "step_by_step_solution": "1. Kemiskinan Absolut (z_abs = 380): Penduduk dengan pengeluaran < 380 adalah individu 1, 2, 3, 4 (q = 4 orang). Prevalensi P0_abs = (4 / 10) * 100% = 40%.\n2. Median data genap (n=10): Median = (400 + 500) / 2 = 450 ribu rupiah.\n3. Garis Kemiskinan Relatif: z_rel = 0.70 * 450 = 315 ribu rupiah.\n4. Kemiskinan Relatif (z_rel = 315): Penduduk dengan pengeluaran < 315 adalah individu 1, 2, 3 (q = 3 orang). Prevalensi P0_rel = (3 / 10) * 100% = 30%.",
        "python_verification_code": "y = [200, 250, 300, 350, 400, 500, 600, 700, 800, 1000]\nz_abs = 380\npoor_abs = [x for x in y if x < z_abs]\nmed = (y[4] + y[5]) / 2\nz_rel = 0.70 * med\npoor_rel = [x for x in y if x < z_rel]\nprint(f'Absolut={len(poor_abs)} ({len(poor_abs)/len(y)*100:.0f}%), Relatif={len(poor_rel)} ({len(poor_rel)/len(y)*100:.0f}%)')",
        "expected_output": "Absolut=4 (40%), Relatif=3 (30%)"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Transformasi skala seragam terhadap kemiskinan relatif",
            "common_mistake": "Menganggap kenaikan pendapatan 20% seragam untuk semua warga menurunkan tingkat kemiskinan relatif.",
            "safe_strategy": "Ingat bahwa median ikut naik 20% sehingga garis relatif naik proporsional; persentase kemiskinan relatif tetap tidak berubah."
        },
        {
            "trap_description": "Tertukar Konversi Nominal vs Purchasing Power Parity (PPP)",
            "common_mistake": "Mengalikan garis kemiskinan global $2.15 per hari langsung dengan kurs pasar valuta asing dolar AS.",
            "safe_strategy": "Konversi wajib menggunakan faktor konversi PPP yang dihitung Bank Dunia/ICP untuk menstandarkan daya beli sekeranjang barang pokok."
        }
    ]
})
f811.write_text(json.dumps(d811, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated 8.1.1")

# ---------------------------------------------------------------------------
# 2. UPDATE 8.1.2
# ---------------------------------------------------------------------------
f812 = LESSONS_DIR / "8.1.2-garis-kemiskinan-makanan-non-makanan.json"
d812 = json.loads(f812.read_text(encoding="utf-8"))
d812.update({
    "point_id": "8.1.2",
    "title": "Garis Kemiskinan Makanan dan Non-Makanan",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Kemiskinan"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "14-16, 27",
                "content": "Garis Kemiskinan Total GK = GKM + GKNM, standar energi 2.100 kkal (WNPG 1978), 52 komoditas makanan, dan paket komoditas non-makanan perkotaan/perdesaan."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Garis Kemiskinan (GK) BPS adalah jumlah rupiah pengeluaran minimum per kapita per bulan untuk memenuhi kebutuhan makanan (setara 2.100 kkal per kapita per hari) ditambah kebutuhan dasar bukan makanan minimum esensial seperti perumahan, sandang, pendidikan, dan kesehatan.",
        "bps_definition": "Garis Kemiskinan (GK) merupakan penjumlahan dari Garis Kemiskinan Makanan (GKM) dan Garis Kemiskinan Bukan Makanan (GKNM). Penduduk dengan pengeluaran per kapita bulanan di bawah GK dikategorikan sebagai penduduk miskin.",
        "boundary_conditions": "GK = GKM + GKNM. GKM berpatokan pada 2.100 kkal dari 52 komoditas makanan rujukan. GKNM mencakup 51 komoditas di perkotaan dan 47 komoditas di perdesaan. Pangsa GKM mendominasi sekitar 73-75% dari total GK.",
        "formula_latex": "$$GK = GKM + GKNM = \\sum_{k=1}^{52} P_k \\cdot Q_k^* + \\sum_{l=1}^m \\alpha_l \\cdot P_l \\cdot Q_l$$"
    },
    "numerical_example": {
        "problem_statement": "Di suatu kabupaten pada September 2021, Garis Kemiskinan Makanan dihitung sebesar Rp367.000 per kapita per bulan dan Garis Kemiskinan Bukan Makanan sebesar Rp133.000 per kapita per bulan. Sebuah keluarga dengan 5 anggota rumah tangga memiliki total pengeluaran konsumsi bulanan Rp2.300.000. Tentukan GK total, pangsa GKM, pengeluaran per kapita sebulan, dan status kemiskinan keluarga tersebut.",
        "data_table": "| Komponen | Nilai (Rp) |\n|---|---|\n| GKM | 367.000 |\n| GKNM | 133.000 |\n| Anggota Rumah Tangga (ART) | 5 orang |\n| Total Pengeluaran RT | 2.300.000 |",
        "step_by_step_solution": "1. GK Total = GKM + GKNM = 367.000 + 133.000 = Rp500.000 per kapita per bulan.\n2. Pangsa GKM = (367.000 / 500.000) * 100% = 73,4%.\n3. Pengeluaran per kapita sebulan = 2.300.000 / 5 = Rp460.000.\n4. Karena pengeluaran per kapita Rp460.000 < GK Rp500.000, maka keluarga tersebut berstatus Miskin.",
        "python_verification_code": "gkm = 367000\ngknm = 133000\ngk = gkm + gknm\npangsa_gkm = (gkm / gk) * 100\nart = 5\ntotal_exp = 2300000\ny_capita = total_exp / art\nstatus = 'Miskin' if y_capita < gk else 'Tidak Miskin'\nprint(f'GK=Rp{gk:,}, Pangsa GKM={pangsa_gkm:.1f}%, Pengeluaran/kapita=Rp{y_capita:,.0f}, Status={status}')",
        "expected_output": "GK=Rp500,000, Pangsa GKM=73.4%, Pengeluaran/kapita=Rp460,000, Status=Miskin"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Memasukkan atau tidaknya rokok ke dalam GKM BPS",
            "common_mistake": "Mengira rokok kretek filter dikeluarkan dari GKM karena bukan makanan sehat.",
            "safe_strategy": "Rokok kretek filter secara faktual masuk ke dalam GKM dan menjadi komoditas penyumbang terbesar kedua setelah beras di perkotaan dan perdesaan."
        },
        {
            "trap_description": "Menilai kemiskinan berdasarkan total pengeluaran RT, bukan per kapita",
            "common_mistake": "Membandingkan total pengeluaran keluarga langsung dengan nilai Garis Kemiskinan.",
            "safe_strategy": "Total pengeluaran rumah tangga wajib dibagi dengan jumlah anggota rumah tangga (ART) terlebih dahulu untuk memperoleh pengeluaran per kapita sebelum dibandingkan dengan GK."
        }
    ]
})
f812.write_text(json.dumps(d812, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated 8.1.2")

# ---------------------------------------------------------------------------
# 3. UPDATE 8.1.3
# ---------------------------------------------------------------------------
f813 = LESSONS_DIR / "8.1.3-metodologi-cost-of-basic-needs-bps.json"
d813 = json.loads(f813.read_text(encoding="utf-8"))
d813.update({
    "point_id": "8.1.3",
    "title": "Metodologi Cost of Basic Needs BPS",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Kemiskinan"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "14, 17-19, 42-43",
                "content": "Metodologi Cost of Basic Needs (CBN), penentuan populasi rujukan (reference population), pemutakhiran paket komoditas, dan kerentanan kelompok near poor."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Metodologi Cost of Basic Needs (CBN) menghitung rupiah yang secara riil dibutuhkan oleh kelompok masyarakat yang hidup sedikit di atas garis kemiskinan sementara (populasi rujukan) untuk memenuhi kebutuhan makanan pokok dan bukan makanan esensial.",
        "bps_definition": "Pendekatan Kebutuhan Dasar (Cost of Basic Needs Approach) adalah metode pengukuran kemiskinan dengan menghitung besarnya rupiah yang harus dikeluarkan untuk memenuhi kebutuhan minimum makanan setara 2.100 kkal per hari serta kebutuhan minimum bukan makanan dari populasi rujukan.",
        "boundary_conditions": "Populasi rujukan didefinisikan sebagai kelompok penduduk yang berada di kelas pengeluaran marjinal (sedikit di atas garis kemiskinan sementara). Susenas menghasilkan estimasi kemiskinan tingkat makro (kabupaten/kota ke atas), bukan basis data sasaran bansos by name by address.",
        "formula_latex": "$$GK = \\sum_{k=1}^{52} P_k Q_k^* + \\sum_{l=1}^m \\alpha_l P_l Q_l, \\quad Q_k^* = Q_k \\cdot \\left(\\frac{2.100}{\\sum_{j=1}^{52} c_j Q_j}\\right)$$"
    },
    "numerical_example": {
        "problem_statement": "Suatu survei verifikasi keluarga pra-sejahtera menguji rumah tangga Bapak Joko berdasarkan kriteria kemiskinan mikro BPS. Dari hasil observasi diperoleh 13 dari 14 indikator kekurangan terpenuhi (ambang batas miskin mikro adalah minimal 9 kriteria). Tentukan status kemiskinan mikro keluarga tersebut.",
        "data_table": "| Indikator Mikro | Standar Miskin | Hasil Observasi | Terpenuhi? |\n|---|---|---|---|\n| Luas Lantai | < 8 m2/kapita | 6 m2/kapita | Ya |\n| Jenis Lantai | Tanah/Bambu murah | Tanah | Ya |\n| Bahan Bakar | Kayu/Arang/Minyak | Kayu bakar | Ya |\n| Fasilitas BAB | Bersama/Tidak ada | Bersama | Ya |\n| Sumber Air | Tak terlindung | Sumur terbuka | Ya |\n| Total Terpenuhi | - | 13 dari 14 | 13 (>= 9) |",
        "step_by_step_solution": "1. Evaluasi kriteria mikro: Sebanyak 13 dari 14 kriteria terpenuhi.\n2. Berdasarkan standar perlindungan sosial BPS, rumah tangga dengan minimal 9 kriteria terpenuhi dikategorikan miskin.\n3. Karena 13 >= 9, maka keluarga Bapak Joko diklasifikasikan sebagai Miskin (Layak Menerima Bansos).",
        "python_verification_code": "criteria_fulfilled = 13\nthreshold = 9\nstatus = 'Miskin (Layak Menerima Bansos)' if criteria_fulfilled >= threshold else 'Tidak Miskin'\nprint(f'{criteria_fulfilled} kriteria, Status={status}')",
        "expected_output": "13 kriteria, Status=Miskin (Layak Menerima Bansos)"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Kesalahan Kebijakan Penyaluran Bansos berbasis data makro Susenas",
            "common_mistake": "Menggunakan angka atau sampel data Susenas BPS untuk membagikan paket sembako kepada penduduk miskin by name by address.",
            "safe_strategy": "Susenas adalah survei sampel untuk estimasi makro dan tidak menyimpan by name by address lengkap; untuk penyaluran bansos mikro wajib digunakan basis data sensus/registrasi (Regsosek/DTKS)."
        },
        {
            "trap_description": "Mengabaikan Karakteristik Penduduk Near Poor",
            "common_mistake": "Menganggap penurunan P0 secara otomatis menyelesaikan kerentanan kemiskinan secara permanen.",
            "safe_strategy": "Perhatikan bahwa banyak penduduk keluar dari kemiskinan hanya berada tipis di atas GK (kelompok rentan/near poor) yang dapat kembali jatuh miskin akibat sedikit kenaikan inflasi pangan."
        }
    ]
})
f813.write_text(json.dumps(d813, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated 8.1.3")

# ---------------------------------------------------------------------------
# 4. UPDATE 8.2.1
# ---------------------------------------------------------------------------
f821 = LESSONS_DIR / "8.2.1-headcount-index-p0.json"
d821 = json.loads(f821.read_text(encoding="utf-8"))
d821.update({
    "point_id": "8.2.1",
    "title": "Headcount Index P0",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Kemiskinan"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "20-21, 24-28",
                "content": "Rumus FGT Headcount Index P0 = q / n, interpretasi persentase penduduk miskin, dan keterbatasan P0 terhadap kedalaman kemiskinan."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Headcount Index P0 mengukur prevalensi atau proporsi penduduk yang hidup di bawah garis kemiskinan terhadap seluruh total populasi.",
        "bps_definition": "Persentase penduduk miskin (Headcount Index / P0) mengukur proporsi penduduk yang memiliki pengeluaran per kapita sebulan di bawah garis kemiskinan.",
        "boundary_conditions": "0 <= P0 <= 1 (atau 0% s.d. 100%). P0 mengukur insidensi kemiskinan tetapi tidak sensitif terhadap seberapa jauh pengeluaran orang miskin di bawah GK (insensitif terhadap kedalaman dan keparahan kemiskinan).",
        "formula_latex": "$$P_0 = \\frac{q}{n} = \\frac{1}{n} \\sum_{i=1}^q \\left( \\frac{z - y_i}{z} \\right)^0$$"
    },
    "numerical_example": {
        "problem_statement": "Dalam suatu survei sampel di sebuah desa berpopulasi n = 20 orang, tercatat data pengeluaran per kapita bulanan (dalam ribuan rupiah): [280, 310, 350, 420, 480, 520, 550, 580, 600, 620, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200]. Jika Garis Kemiskinan ditetapkan z = 500 ribu rupiah, hitunglah jumlah orang miskin (q) dan nilai Headcount Index (P0).",
        "data_table": "| Kelompok | Pengeluaran (ribu Rp) | Jumlah Penduduk |\n|---|---|---|\n| y_i < 500 | 280, 310, 350, 420, 480 | 5 orang |\n| y_i >= 500 | 520, 550, ..., 1200 | 15 orang |\n| Total | - | 20 orang |",
        "step_by_step_solution": "1. Garis kemiskinan z = 500 ribu rupiah.\n2. Identifikasi penduduk dengan y_i < 500: 280, 310, 350, 420, 480. Diperoleh q = 5 orang miskin.\n3. Total populasi n = 20 orang.\n4. Headcount Index P0 = q / n = 5 / 20 = 0,25 (atau 25%).",
        "python_verification_code": "y = [280, 310, 350, 420, 480, 520, 550, 580, 600, 620, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200]\nz = 500\npoor = [x for x in y if x < z]\nq = len(poor)\nn = len(y)\np0 = q / n\nprint(f'q={q} orang, P0={p0:.2f} (atau {p0*100:.0f}%)')",
        "expected_output": "q=5 orang, P0=0.25 (atau 25%)"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Kesalahan Pembagi Populasi (n vs q atau angkatan kerja)",
            "common_mistake": "Membagi jumlah orang miskin q dengan jumlah kepala keluarga atau angkatan kerja.",
            "safe_strategy": "Pembagi wajib seluruh populasi individu (n), baik tua, muda, bekerja, maupun tidak bekerja."
        },
        {
            "trap_description": "Kelemahan Kebijakan Mentas Sesaat (Cream-Skimming Policy)",
            "common_mistake": "Mengasumsikan bahwa penurunan P0 selalu berarti intervensi sosial berjalan adil bagi yang paling menderita.",
            "safe_strategy": "P0 hanya menghitung orang yang melintasi garis kemiskinan, sehingga rawan dieksploitasi dengan hanya membantu orang yang sedikit di bawah GK (near poor) dan mengabaikan orang yang miskin ekstrem."
        }
    ]
})
f821.write_text(json.dumps(d821, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated 8.2.1")

# ---------------------------------------------------------------------------
# 5. UPDATE 8.2.2
# ---------------------------------------------------------------------------
f822 = LESSONS_DIR / "8.2.2-poverty-gap-index-p1.json"
d822 = json.loads(f822.read_text(encoding="utf-8"))
d822.update({
    "point_id": "8.2.2",
    "title": "Poverty Gap Index P1",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Kemiskinan"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "20, 22, 24-29",
                "content": "Indeks Kedalaman Kemiskinan P1, rata-rata kesenjangan pengeluaran terhadap garis kemiskinan, rumus FGT alfa=1 dengan pembagi n populasi total."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Poverty Gap Index P1 mengukur rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan, dirata-ratakan terhadap seluruh populasi penduduk.",
        "bps_definition": "Indeks Kedalaman Kemiskinan (Poverty Gap Index / P1) adalah ukuran rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan.",
        "boundary_conditions": "0 <= P1 <= P0 <= 1. Pembagi rumus adalah n (seluruh populasi), bukan q (jumlah orang miskin). P1 memenuhi Monotonicity Axiom namun melanggar Transfer Axiom.",
        "formula_latex": "$$P_1 = \\frac{1}{n} \\sum_{i=1}^q \\left( \\frac{z - y_i}{z} \\right)^1 = P_0 \\cdot I_{\\text{gap}}, \\quad I_{\\text{gap}} = \\frac{1}{q} \\sum_{i=1}^q \\left( \\frac{z - y_i}{z} \\right)$$"
    },
    "numerical_example": {
        "problem_statement": "Sebuah komunitas terdiri dari n = 5 orang dengan pengeluaran per kapita sebulan masing-masing (dalam ribuan rupiah): Y = [300, 400, 450, 700, 900]. Jika Garis Kemiskinan ditetapkan z = 600 ribu rupiah, hitunglah: 1) Nilai Poverty Gap Index (P1), 2) Total dana minimum per bulan yang dibutuhkan untuk mengentaskan seluruh penduduk miskin tersebut tepat ke garis kemiskinan.",
        "data_table": "| Individu | Pengeluaran (ribu Rp) | Miskin? | Shortfall (z - y_i) | Normalized Gap (z - y_i)/z |\n|---|---|---|---|---|\n| 1 | 300 | Ya | 300 | 0,500 |\n| 2 | 400 | Ya | 200 | 0,333 |\n| 3 | 450 | Ya | 150 | 0,250 |\n| 4 | 700 | Tidak | 0 | 0 |\n| 5 | 900 | Tidak | 0 | 0 |\n| Total | - | q=3 | Rp650.000 | 1,0833 |",
        "step_by_step_solution": "1. Garis kemiskinan z = 600 ribu rupiah. Penduduk miskin adalah individu 1, 2, 3 (q = 3 orang, n = 5 orang).\n2. Rasio kesenjangan (normalized poverty gap):\n   - Individu 1: (600 - 300)/600 = 0,5000\n   - Individu 2: (600 - 400)/600 = 0,3333\n   - Individu 3: (600 - 450)/600 = 0,2500\n3. Jumlah rasio gap = 0,5000 + 0,3333 + 0,2500 = 1,0833.\n4. Poverty Gap Index P1 = (1 / n) * 1,0833 = 1,0833 / 5 = 0,2167 (atau 21,67%).\n5. Total shortfall dana = (300 + 200 + 150) ribu rupiah = Rp650.000.",
        "python_verification_code": "y = [300, 400, 450, 700, 900]\nz = 600\nn = len(y)\npoor = [x for x in y if x < z]\ngaps = [(z - x) / z for x in poor]\np1 = sum(gaps) / n\ntotal_transfer = sum(z - x for x in poor) * 1000\nprint(f'P1={p1:.4f}; Total Transfer=Rp{total_transfer:,.0f}')",
        "expected_output": "P1=0.2167; Total Transfer=Rp650,000"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Jebakan Pembagi q vs n pada formula P1",
            "common_mistake": "Membagi total normalized poverty gap dengan q (jumlah orang miskin saja).",
            "safe_strategy": "Formula resmi FGT dan BPS mewajibkan pembagian dengan seluruh populasi n. Membagi dengan q hanya menghasilkan Income Gap Ratio (I_gap), bukan Poverty Gap Index (P1)."
        },
        {
            "trap_description": "Keterbatasan Aksioma Transfer pada P1",
            "common_mistake": "Menganggap P1 sensitif terhadap transfer uang antar-penduduk miskin.",
            "safe_strategy": "P1 melanggar Transfer Axiom: jika uang ditransfer dari orang miskin ekstrem ke orang miskin lain (keduanya tetap di bawah GK), total kesenjangan tidak berubah sehingga P1 tetap konstan."
        }
    ]
})
f822.write_text(json.dumps(d822, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated 8.2.2")

# ---------------------------------------------------------------------------
# 6. UPDATE 8.2.3
# ---------------------------------------------------------------------------
f823 = LESSONS_DIR / "8.2.3-poverty-severity-index-p2.json"
d823 = json.loads(f823.read_text(encoding="utf-8"))
d823.update({
    "point_id": "8.2.3",
    "title": "Poverty Severity Index P2",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Kemiskinan"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "20, 23, 24, 26, 29",
                "content": "Indeks Keparahan Kemiskinan P2, pembobotan kuadrat gap, ukuran ketimpangan di antara penduduk miskin, rumus FGT alfa=2 dengan pembagi n."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Poverty Severity Index P2 memberikan bobot lebih berat pada penduduk yang jurang kemiskinannya semakin dalam melalui pengkuadratan rasio gap, sehingga mampu menangkap ketimpangan pengeluaran di antara sesama penduduk miskin.",
        "bps_definition": "Indeks Keparahan Kemiskinan (Poverty Severity Index / P2) memberikan gambaran mengenai penyebaran pengeluaran di antara penduduk miskin.",
        "boundary_conditions": "0 <= P2 <= P1 <= P0 <= 1. Memenuhi Monotonicity Axiom dan Transfer Axiom. Pembagi adalah seluruh populasi n.",
        "formula_latex": "$$P_2 = \\frac{1}{n} \\sum_{i=1}^q \\left( \\frac{z - y_i}{z} \\right)^2$$"
    },
    "numerical_example": {
        "problem_statement": "Suatu wilayah berpopulasi n = 5 orang memiliki garis kemiskinan z = Rp600.000. Data pengeluaran per kapita sebulan 5 orang tersebut adalah: Y = [300.000, 400.000, 450.000, 750.000, 900.000]. Hitunglah: 1) Kuadrat rasio kesenjangan masing-masing penduduk miskin, 2) Nilai Poverty Severity Index (P2).",
        "data_table": "| Individu | Pengeluaran (Rp) | Miskin? | Gap (z - y_i)/z | Kuadrat Gap ((z - y_i)/z)^2 |\n|---|---|---|---|---|\n| 1 | 300.000 | Ya | 300.000/600.000 = 0,5000 | (0,5000)^2 = 0,2500 |\n| 2 | 400.000 | Ya | 200.000/600.000 = 0,3333 | (0,3333)^2 = 0,1111 |\n| 3 | 450.000 | Ya | 150.000/600.000 = 0,2500 | (0,2500)^2 = 0,0625 |\n| 4 | 750.000 | Tidak | 0 | 0 |\n| 5 | 900.000 | Tidak | 0 | 0 |\n| Total | - | q=3 | 1,0833 | 0,4236 |",
        "step_by_step_solution": "1. Garis kemiskinan z = Rp600.000. Penduduk miskin adalah individu 1, 2, 3 (q = 3 orang, n = 5 orang).\n2. Menghitung kuadrat normalized gap:\n   - Individu 1: ((600.000 - 300.000)/600.000)^2 = (0,5000)^2 = 0,2500\n   - Individu 2: ((600.000 - 400.000)/600.000)^2 = (0,3333)^2 = 0,1111\n   - Individu 3: ((600.000 - 450.000)/600.000)^2 = (0,2500)^2 = 0,0625\n3. Jumlah kuadrat gap = 0,2500 + 0,1111 + 0,0625 = 0,4236.\n4. Nilai Poverty Severity Index P2 = (1 / n) * 0,4236 = 0,4236 / 5 = 0,0847.",
        "python_verification_code": "y = [300000, 400000, 450000, 750000, 900000]\nz = 600000\nn = len(y)\npoor = [x for x in y if x < z]\nsq_gaps = [((z - x) / z) ** 2 for x in poor]\np2 = sum(sq_gaps) / n\nprint(f'P2={p2:.4f}')",
        "expected_output": "P2=0.0847"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Lupa Menguadratkan Rasio Kesenjangan pada perhitungan P2",
            "common_mistake": "Menjumlahkan deviasi tanpa dikuadratkan terlebih dahulu sehingga malah menghitung P1.",
            "safe_strategy": "Pastikan setiap suku rasio (z - y_i)/z dikuadratkan terlebih dahulu sebelum dijumlahkan dan dibagi total populasi n."
        },
        {
            "trap_description": "Kesesatan Logika 'P0 Turun Berarti Keparahan Kemiskinan Berkurang'",
            "common_mistake": "Mengira jika angka persentase penduduk miskin P0 berkurang, kondisi kelompok miskin yang tersisa pasti membaik.",
            "safe_strategy": "Jika bantuan pemerintah hanya mentaskan orang yang berada di ambang batas garis kemiskinan, P0 turun tetapi P2 dapat tetap tinggi atau bahkan memperlihatkan ketimpangan yang lebih tajam di antara penduduk miskin ekstrem yang tertinggal."
        }
    ]
})
f823.write_text(json.dumps(d823, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated 8.2.3")

# ---------------------------------------------------------------------------
# 7. CREATE 8.3.1
# ---------------------------------------------------------------------------
d831 = {
    "point_id": "8.3.1",
    "title": "Kurva Lorenz dan Koefisien Gini",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Ketimpangan Pendapatan dan Pengeluaran"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "33-40",
                "content": "Kurva Lorenz, formulasi trapesium diskrit BPS G = 1 - sum(f_i * (Y_i + Y_{i-1})), tabel kuintil pengeluaran slide 39 G = 0.3770."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Kurva Lorenz menggambarkan hubungan kumulatif antara persentase penduduk (sumbu horizontal) dan persentase pengeluaran/pendapatan kumulatif (sumbu vertikal). Garis diagonal 45 derajat adalah line of perfect equality. Semakin melengkung kurva menjauhi diagonal, semakin tinggi ketimpangan. Koefisien Gini adalah rasio area antara diagonal dan kurva Lorenz terhadap seluruh segitiga di bawah diagonal (A / (A+B)).",
        "bps_definition": "Koefisien Gini (Gini Ratio) adalah ukuran kemerataan distribusi pendapatan atau pengeluaran yang dihitung berdasarkan luas wilayah antara garis pemerataan sempurna dan kurva Lorenz riil. Nilai Gini berkisar antara 0 (pemerataan sempurna) hingga 1 (ketimpangan sempurna). BPS menggunakan pengeluaran konsumsi Susenas sebagai proksi pendapatan.",
        "boundary_conditions": "0 <= G <= 1. G = 0 berarti pemerataan sempurna (semua orang menikmati pengeluaran yang sama persis). G = 1 berarti satu orang menguasai seluruh pengeluaran. Koefisien Gini bersifat scale invariant (tidak berubah jika seluruh pengeluaran dikalikan konstanta c > 0).",
        "formula_latex": "$$G = 1 - \\sum_{i=1}^k (p_i - p_{i-1})(y_i + y_{i-1}) = 1 - \\sum_{i=1}^k f_i (Y_i + Y_{i-1})$$"
    },
    "numerical_example": {
        "problem_statement": "Diberikan data konsumsi menurut 5 kelompok kuintil penduduk (masing-masing 20% penduduk): Kuintil 1 = 50.000, Kuintil 2 = 70.000, Kuintil 3 = 100.000, Kuintil 4 = 125.000, Kuintil 5 = 350.000. Hitunglah total konsumsi, proporsi konsumsi per kuintil, kumulatif konsumsi (Y_i), luas trapesium masing-masing kelas, dan Koefisien Gini BPS menggunakan formula pendekatan trapesium diskrit.",
        "data_table": "| Kuintil | Konsumsi (Rp) | Persentase Konsumsi (p_i) | Persentase Penduduk (f_i) | Kumulatif Konsumsi (Y_i) | Kumulatif Penduduk | Y_i + Y_{i-1} | f_i * (Y_i + Y_{i-1}) |\n|---|---|---|---|---|---|---|---|\n| 1 | 50.000 | 0,0719 | 0,2000 | 0,0719 | 0,2000 | 0,0719 | 0,0144 |\n| 2 | 70.000 | 0,1007 | 0,2000 | 0,1727 | 0,4000 | 0,2446 | 0,0489 |\n| 3 | 100.000 | 0,1439 | 0,2000 | 0,3165 | 0,6000 | 0,4892 | 0,0978 |\n| 4 | 125.000 | 0,1799 | 0,2000 | 0,4964 | 0,8000 | 0,8129 | 0,1626 |\n| 5 | 350.000 | 0,5036 | 0,2000 | 1,0000 | 1,0000 | 1,4964 | 0,2993 |\n| Total | 695.000 | 1,0000 | 1,0000 | - | - | - | 0,6230 |",
        "step_by_step_solution": "1. Total konsumsi = 50.000 + 70.000 + 100.000 + 125.000 + 350.000 = 695.000.\n2. Hitung persentase konsumsi p_i:\n   - p_1 = 50.000 / 695.000 = 0,0719\n   - p_2 = 70.000 / 695.000 = 0,1007\n   - p_3 = 100.000 / 695.000 = 0,1439\n   - p_4 = 125.000 / 695.000 = 0,1799\n   - p_5 = 350.000 / 695.000 = 0,5036\n3. Hitung kumulatif konsumsi Y_i:\n   - Y_1 = 0,0719\n   - Y_2 = 0,0719 + 0,1007 = 0,1727\n   - Y_3 = 0,1727 + 0,1439 = 0,3165\n   - Y_4 = 0,3165 + 0,1799 = 0,4964\n   - Y_5 = 0,4964 + 0,5036 = 1,0000\n4. Hitung suku trapesium f_i * (Y_i + Y_{i-1}) dengan f_i = 0,2000:\n   - Kelas 1: 0,2000 * (0,0719 + 0) = 0,0144\n   - Kelas 2: 0,2000 * (0,1727 + 0,0719) = 0,2000 * 0,2446 = 0,0489\n   - Kelas 3: 0,2000 * (0,3165 + 0,1727) = 0,2000 * 0,4892 = 0,0978\n   - Kelas 4: 0,2000 * (0,4964 + 0,3165) = 0,2000 * 0,8129 = 0,1626\n   - Kelas 5: 0,2000 * (1,0000 + 0,4964) = 0,2000 * 1,4964 = 0,2993\n5. Jumlah luas area di bawah kurva Lorenz = 0,0144 + 0,0489 + 0,0978 + 0,1626 + 0,2993 = 0,6230.\n6. Koefisien Gini: G = 1 - 0,6230 = 0,3770.",
        "python_verification_code": "consumption = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]\ntotal = sum(consumption)\np_i = [c / total for c in consumption]\nf_i = 0.20\ny_cum = []\ncurr = 0.0\nfor p in p_i:\n    curr += p\n    y_cum.append(curr)\ntrapezoid_terms = []\nfor i in range(len(y_cum)):\n    prev_y = 0.0 if i == 0 else y_cum[i - 1]\n    trapezoid_terms.append(f_i * (y_cum[i] + prev_y))\nsum_trapezoid = sum(trapezoid_terms)\ngini = 1.0 - sum_trapezoid\nprint(f'Total={total:.0f}, SumTrapezoid={sum_trapezoid:.4f}, Gini={gini:.4f}')",
        "expected_output": "Total=695000, SumTrapezoid=0.6230, Gini=0.3770"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Tertukar antara formula diskrit trapesium BPS dengan luas segitiga",
            "common_mistake": "Lupa mengurangkan jumlah suku trapesium dari angka 1, atau lupa mengalikan suku trapesium dengan f_i.",
            "safe_strategy": "Ingat bahwa sum f_i * (Y_i + Y_{i-1}) adalah dua kali luas area B di bawah kurva Lorenz; rumus Gini BPS adalah G = 1 - sum f_i * (Y_i + Y_{i-1})."
        },
        {
            "trap_description": "Invariansi Skala Koefisien Gini",
            "common_mistake": "Mengira jika setiap orang mendapatkan kenaikan pendapatan 20% serempak, koefisien Gini akan berubah.",
            "safe_strategy": "Gini bersifat scale-invariant: jika seluruh pendapatan dikalikan skalar positif c, proporsi konsumsi p_i dan Gini tetap konstan."
        },
        {
            "trap_description": "Keterbatasan Persilangan Kurva Lorenz (Lorenz Crossing)",
            "common_mistake": "Menyimpulkan distribusi A lebih merata daripada B hanya dari angka Gini ketika kedua kurva Lorenz saling bersilangan.",
            "safe_strategy": "Jika kurva Lorenz saling bersilangan, perbandingan Gini dapat menyesatkan karena distribusi ketimpangan di kelompok bawah dan atas berbeda secara struktural."
        }
    ],
    "textbook": "Official Statistics Lanjutan (OSL)",
    "chapter_id": 8,
    "chapter_title": "Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan",
    "section": "8.3 Ukuran Ketimpangan Pendapatan dan Pengeluaran",
    "mode": "deep",
    "points": [
        {
            "id": "8.3.1",
            "name": "Kurva Lorenz dan Koefisien Gini",
            "importance": "高",
            "source_ref": "[Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 33-40]",
            "exam_focus": "Menguasai pembentukan kurva Lorenz, penghitungan Koefisien Gini metode trapesium diskrit BPS, interpretasi nilai Gini, dan sifat invariansi skala.",
            "textbook_excerpt": "Kurva Lorenz menggambarkan fungsi distribusi kumulatif pendapatan atau kesejahteraan dari sekelompok penduduk. Dikemukakan oleh Max O. Lorenz (1905). Line of perfect equality digambarkan oleh garis diagonal y = x. Koefisien Gini (Gini Ratio) adalah rasio wilayah antara line of perfect equality dan kurva Lorenz hasil observasi (A) ke wilayah segitiga di bawah diagonal (A+B), sehingga G = A/(A+B). BPS menghitung Gini secara diskrit dengan pendekatan luas bidang trapesium [slide 33-38].",
            "intuition": "Bayangkan kue ekonomi nasional. Jika 100 orang berbaris dari yang paling miskin hingga paling kaya:\n- Jika kue dibagi rata sempurna, 20 orang pertama mendapat 20% kue, 40 orang pertama mendapat 40% kue, dst. Ini membentuk garis diagonal lurus 45 derajat (Line of Perfect Equality).\n- Kenyataannya, 20 orang termiskin mungkin hanya mendapat 7% kue, 40 orang pertama hanya mendapat 17% kue, dst. Garis riil ini melengkung ke bawah (Kurva Lorenz).\n- Semakin melorot lengkungan kurva ke bawah, semakin timpang pembagian kue tersebut.\n- Koefisien Gini mengukur seberapa luas rongga pemisah antara garis adil ideal dan kurva riil.",
            "formal": "### 1. Landasan Konseptual Kurva Lorenz\n\nKurva Lorenz menyatakan pasangan titik koordinat $(X_i, Y_i)$ pada bidang Cartesius [slide 33-35]:\n- **Sumbu Horizontal ($X_i$)**: Persentase kumulatif penduduk penerima pendapatan/pengeluaran ($0 \\le X_i \\le 100\\%$ atau $0 \\le X_i \\le 1$).\n- **Sumbu Vertikal ($Y_i$)**: Persentase kumulatif pendapatan/pengeluaran yang diterima ($0 \\le Y_i \\le 100\\%$ atau $0 \\le Y_i \\le 1$).\n\nKarakteristik batas kurva Lorenz:\n1. **Line of Perfect Equality**: Garis lurus diagonal $Y = X$. Kelompok terendah $N\\%$ penduduk menikmati persis $N\\%$ dari total pengeluaran [slide 35].\n2. **Line of Perfect Inequality**: Kondisi batas di mana 1 orang menguasai $100\\%$ pendapatan dan penduduk lainnya memperoleh $0\\%$. Kurva berada pada sumbu horizontal $Y = 0$ untuk $X < 1$, dan melonjak ke $Y = 1$ saat $X = 1$ [slide 35].\n\n### 2. Formulasi Matematis Koefisien Gini (Gini Ratio)\n\nSecara geometris [slide 38]:\n$$G = \\frac{A}{A + B}$$\ndimana:\n- $A$ adalah luas area antara garis diagonal pemerataan sempurna dan kurva Lorenz.\n- $B$ adalah luas area di bawah kurva Lorenz.\n- Karena luas total segitiga di bawah garis diagonal adalah $A + B = \\frac{1}{2} \\times 1 \\times 1 = 0,5$, maka:\n$$G = \\frac{A}{0,5} = 2A = 2(0,5 - B) = 1 - 2B$$\n\n### 3. Formulasi Pendekatan Trapesium Diskrit BPS\n\nDalam statistik resmi BPS, data konsumsi Susenas dikelompokkan ke dalam $k$ kelas pengeluaran (misal 5 kuintil atau 10 desil). Area $B$ diestimasi sebagai penjumlahan luas bidang-bidang trapesium [slide 38]:\n$$B = \\sum_{i=1}^k \\frac{1}{2} (X_i - X_{i-1})(Y_i + Y_{i-1})$$\n\nKarena $2B = \\sum_{i=1}^k (X_i - X_{i-1})(Y_i + Y_{i-1})$, maka Koefisien Gini BPS diformulasikan sebagai [slide 38]:\n$$G = 1 - \\sum_{i=1}^k f_i \\cdot (Y_i + Y_{i-1})$$\ndimana:\n- $k$ = jumlah kelas pendapatan/pengeluaran.\n- $f_i = X_i - X_{i-1}$ = proporsi penduduk pada kelas ke-$i$ (untuk kuintil, $f_i = 0,2000$).\n- $Y_i$ = persentase/proporsi kumulatif pengeluaran hingga kelas ke-$i$, dengan $Y_0 = 0$.\n\n### 4. Pedoman Interpretasi Nilai Koefisien Gini\nBerdasarkan klasifikasi standar statistik BPS dan internasional [slide 38, 41]:\n- $G < 0,3$ : Ketimpangan Rendah\n- $0,3 \\le G \\le 0,5$ : Ketimpangan Sedang\n- $G > 0,5$ : Ketimpangan Tinggi\n\n### 5. Rekonstruksi Komputasi Slide 39\n| Kuintil | Konsumsi | Persentase Konsumsi ($p_i$) | Persentase Penduduk ($f_i$) | Kumulatif Konsumsi ($Y_i$) | Kumulatif Penduduk | $Y_i + Y_{i-1}$ | $f_i \\times (Y_i + Y_{i-1})$ |\n|---|---|---|---|---|---|---|---|\n| 1 | 50.000 | 0,0719 | 0,2000 | 0,0719 | 0,2000 | 0,0719 | 0,0144 |\n| 2 | 70.000 | 0,1007 | 0,2000 | 0,1727 | 0,4000 | 0,2446 | 0,0489 |\n| 3 | 100.000 | 0,1439 | 0,2000 | 0,3165 | 0,6000 | 0,4892 | 0,0978 |\n| 4 | 125.000 | 0,1799 | 0,2000 | 0,4964 | 0,8000 | 0,8129 | 0,1626 |\n| 5 | 350.000 | 0,5036 | 0,2000 | 1,0000 | 1,0000 | 1,4964 | 0,2993 |\n| **Total** | **695.000** | **1,0000** | **1,0000** | - | - | - | **0,6230** |\n\n$$G = 1 - 0,6230 = 0,3770$$\nNilai $G = 0,3770$ menunjukkan bahwa distribusi pengeluaran berada pada kategori **Ketimpangan Sedang**.",
            "pitfalls": "1. **Tertukar Kurva Lorenz dengan Koefisien Gini**: Kurva Lorenz adalah representasi visual grafis kumulatif, sedangkan Koefisien Gini adalah ringkasan skalar numerik rasio area.\n2. **Lupa Mengurangkan dari 1**: Nilai sum f_i * (Y_i + Y_{i-1}) adalah dua kali luas area di bawah kurva (2B). Jawaban akhir Gini wajib dihitung sebagai 1 - 2B.\n3. **Invariansi terhadap Skala**: Mengalikan seluruh konsumsi dengan faktor pengali c tidak mengubah Gini, tetapi penambahan lump-sum nominal yang sama rata ke semua orang akan menurunkan Gini.",
            "memory_hook": "Kurva Lorenz adalah Lengkungan Kumulatif; Gini adalah 1 dikurangi Luas Trapesium Kumulatif Bawah ($G = 1 - 2B$).",
            "examples": [
                {
                    "type": "single",
                    "source_ref": "[Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 35, 38]",
                    "problem": "Jika kurva Lorenz suatu negara berimpit tepat dengan garis diagonal 45 derajat (line of perfect equality), berapakah nilai Koefisien Gini negara tersebut dan apa makna ekonominya?",
                    "options": [
                        "Koefisien Gini bernilai 1; seluruh pendapatan dikuasai oleh satu individu.",
                        "Koefisien Gini bernilai 0,5; ketimpangan berada pada tingkat sedang.",
                        "Koefisien Gini bernilai 0; distribusi pendapatan merata secara sempurna.",
                        "Koefisien Gini tidak terdefinisi karena tidak ada luas area yang terbentuk."
                    ],
                    "answer": 2,
                    "solution": "Jawaban: **C**.\n\n**Pembahasan**:\n- Garis diagonal 45 derajat menyatakan distribusi pendapatan merata secara sempurna di mana setiap kelompok kumulatif n% penduduk menikmati persis n% pendapatan kumulatif [slide 35].\n- Karena kurva Lorenz berimpit dengan diagonal, area A di antara diagonal dan kurva bernilai 0 ($A = 0$).\n- Akibatnya, Koefisien Gini $G = \\frac{A}{A + B} = \\frac{0}{0,5} = 0$, yang mengindikasikan pemerataan sempurna [slide 38]."
                },
                {
                    "type": "text",
                    "source_ref": "[Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 38-39]",
                    "problem": "Diberikan data konsumsi menurut 5 kelompok kuintil penduduk (masing-masing 20% penduduk): Kuintil 1 = 50.000, Kuintil 2 = 70.000, Kuintil 3 = 100.000, Kuintil 4 = 125.000, Kuintil 5 = 350.000.\nHitunglah:\n1. Total konsumsi dan persentase konsumsi masing-masing kuintil.\n2. Nilai kumulatif konsumsi ($Y_i$) untuk setiap kuintil.\n3. Jumlah suku trapesium $\\sum f_i (Y_i + Y_{i-1})$.\n4. Koefisien Gini ($G$) BPS dan interpretasi tingkat ketimpangannya.\nTuliskan jawaban akhir dalam format: `Total=..., SumTrapezoid=..., Gini=..., Kategori=...`.",
                    "answer": "Total=695.000, SumTrapezoid=0,6230, Gini=0,3770, Kategori=Ketimpangan Sedang",
                    "solution": "Langkah-langkah perhitungan:\n1. **Total Konsumsi** = $50.000 + 70.000 + 100.000 + 125.000 + 350.000 = 695.000$.\n2. **Persentase Konsumsi ($p_i$)**:\n   - $p_1 = 50.000 / 695.000 = 0,0719$\n   - $p_2 = 70.000 / 695.000 = 0,1007$\n   - $p_3 = 100.000 / 695.000 = 0,1439$\n   - $p_4 = 125.000 / 695.000 = 0,1799$\n   - $p_5 = 350.000 / 695.000 = 0,5036$\n3. **Kumulatif Konsumsi ($Y_i$)**:\n   - $Y_1 = 0,0719$\n   - $Y_2 = 0,0719 + 0,1007 = 0,1727$\n   - $Y_3 = 0,1727 + 0,1439 = 0,3165$\n   - $Y_4 = 0,3165 + 0,1799 = 0,4964$\n   - $Y_5 = 0,4964 + 0,5036 = 1,0000$\n4. **Perhitungan Trapesium ($f_i = 0,2000$)**:\n   - Suku 1: $0,2000 \\times (0,0719 + 0) = 0,0144$\n   - Suku 2: $0,2000 \\times (0,1727 + 0,0719) = 0,0489$\n   - Suku 3: $0,2000 \\times (0,3165 + 0,1727) = 0,0978$\n   - Suku 4: $0,2000 \\times (0,4964 + 0,3165) = 0,1626$\n   - Suku 5: $0,2000 \\times (1,0000 + 0,4964) = 0,2993$\n   - **Total Luas Trapesium** = $0,0144 + 0,0489 + 0,0978 + 0,1626 + 0,2993 = 0,6230$.\n5. **Koefisien Gini**:\n   $$G = 1 - 0,6230 = 0,3770$$\n   Karena $0,3 \\le 0,3770 \\le 0,5$, maka tergolong **Ketimpangan Sedang**.\n\n**Verifikasi Kode Python**:\n```python\nconsumption = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]\ntotal = sum(consumption)\np_i = [c / total for c in consumption]\nf_i = 0.20\ny_cum = []\ncurr = 0.0\nfor p in p_i:\n    curr += p\n    y_cum.append(curr)\ntrapezoid_terms = []\nfor i in range(len(y_cum)):\n    prev_y = 0.0 if i == 0 else y_cum[i - 1]\n    trapezoid_terms.append(f_i * (y_cum[i] + prev_y))\nsum_trapezoid = sum(trapezoid_terms)\ngini = 1.0 - sum_trapezoid\nprint(f'Total={total:.0f}, SumTrapezoid={sum_trapezoid:.4f}, Gini={gini:.4f}')\n# Output: Total=695000, SumTrapezoid=0.6230, Gini=0.3770\n```"
                }
            ],
            "links": ["8.3.2", "8.2.1", "8.2.2", "8.2.3"]
        }
    ]
}

f831 = LESSONS_DIR / "8.3.1-kurva-lorenz-koefisien-gini.json"
f831.write_text(json.dumps(d831, ensure_ascii=False, indent=2), encoding="utf-8")
print("Created 8.3.1")

# ---------------------------------------------------------------------------
# 8. CREATE 8.3.2
# ---------------------------------------------------------------------------
d832 = {
    "point_id": "8.3.2",
    "title": "Kriteria Ketimpangan Bank Dunia",
    "importance": "高",
    "curriculum_alignment": {
        "pertemuan": 8,
        "silabus_topic": "Kemiskinan dan Ketimpangan Pendapatan",
        "bps_subject": "Indikator Ketimpangan Pendapatan dan Pengeluaran"
    },
    "grounding": {
        "primary_sources": [
            {
                "file": "Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md",
                "slide_or_page": "41-44",
                "content": "Kriteria ketimpangan Bank Dunia berdasarkan pangsa pengeluaran 40% penduduk terbawah: <12% tinggi, 12-17% sedang, >17% rendah."
            }
        ],
        "supplemental_sources": [],
        "coverage_status": "COVERED"
    },
    "theory": {
        "intuition": "Bank Dunia membagi penduduk menjadi tiga lapisan: 40% terbawah (kelompok pendapatan rendah), 40% menengah, dan 20% teratas (kelompok pendapatan tinggi). Ukuran ketimpangan difokuskan secara spesifik pada kue ekonomi yang dinikmati oleh 40% kelompok terbawah. Jika kelompok 40% terbawah hanya memperoleh bagian sangat kecil (<12%), ketimpangan dinilai tinggi.",
        "bps_definition": "Kriteria Ketimpangan Bank Dunia mengklasifikasikan tingkat ketimpangan pengeluaran/pendapatan berdasarkan persentase total pengeluaran yang dinikmati oleh 40 persen penduduk berpendapatan terendah: (1) Ketimpangan Tinggi jika pangsa 40% terbawah < 12%; (2) Ketimpangan Sedang jika pangsa 40% terbawah antara 12% dan 17%; (3) Ketimpangan Rendah jika pangsa 40% terbawah > 17%.",
        "boundary_conditions": "Ambang batas Bank Dunia dihitung dari kuintil 1 + kuintil 2 (Q1 + Q2) atau desil 1 s.d. 4 (D1 + D2 + D3 + D4). Nilai batas pemisah kritis adalah 12% dan 17%.",
        "formula_latex": "$$\\text{Pangsa 40\\% Terbawah} = p_1 + p_2 = Y_2 \\times 100\\%, \\quad \\text{Tingkat} = \\begin{cases} \\text{Tinggi}, & < 12\\% \\\\ \\text{Sedang}, & 12\\% \\le \\text{Pangsa} \\le 17\\% \\\\ \\text{Rendah}, & > 17\\% \\end{cases}$$"
    },
    "numerical_example": {
        "problem_statement": "Berdasarkan data kuintil konsumsi pada Slide 39 (Q1 = 50.000, Q2 = 70.000, Q3 = 100.000, Q4 = 125.000, Q5 = 350.000; total = 695.000), hitunglah persentase pengeluaran yang dinikmati oleh 40% penduduk terbawah, 40% penduduk menengah, dan 20% penduduk teratas, lalu klasifikasikan tingkat ketimpangan menurut kriteria Bank Dunia.",
        "data_table": "| Kelompok Penduduk | Kuintil Termasuk | Total Konsumsi (Rp) | Persentase Konsumsi (%) | Kriteria Bank Dunia |\n|---|---|---|---|---|\n| 40% Terbawah | Q1 + Q2 | 120.000 | 17,27% | > 17% -> Rendah |\n| 40% Menengah | Q3 + Q4 | 225.000 | 32,37% | - |\n| 20% Teratas | Q5 | 350.000 | 50,36% | - |\n| Total | Q1 s.d. Q5 | 695.000 | 100,00% | - |",
        "step_by_step_solution": "1. Total konsumsi populasi = 50.000 + 70.000 + 100.000 + 125.000 + 350.000 = 695.000.\n2. Konsumsi 40% penduduk terbawah (Q1 + Q2) = 50.000 + 70.000 = 120.000.\n3. Pangsa pengeluaran 40% terbawah = (120.000 / 695.000) * 100% = 17,266...% ≈ 17,27%.\n4. Evaluasi kriteria Bank Dunia:\n   - < 12% : Ketimpangan Tinggi\n   - 12% s.d. 17% : Ketimpangan Sedang\n   - > 17% : Ketimpangan Rendah\n5. Karena 17,27% > 17,0%, maka distribusi pengeluaran berada pada kategori Ketimpangan Rendah.",
        "python_verification_code": "consumption = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]\ntotal = sum(consumption)\nbottom_40_val = consumption[0] + consumption[1]\nbottom_40_pct = (bottom_40_val / total) * 100.0\nif bottom_40_pct < 12.0:\n    category = 'Tinggi'\nelif bottom_40_pct <= 17.0:\n    category = 'Sedang'\nelse:\n    category = 'Rendah'\nprint(f'Bottom40_Pct={bottom_40_pct:.2f}%, Category={category}')",
        "expected_output": "Bottom40_Pct=17.27%, Category=Rendah"
    },
    "exam_pitfalls": [
        {
            "trap_description": "Terbalik menafsirkan arah persentase Bank Dunia",
            "common_mistake": "Mengira jika pangsa 40% terbawah < 12%, maka ketimpangannya rendah karena angkanya kecil.",
            "safe_strategy": "Ingat bahwa semakin KECIL pangsa yang dinikmati kelompok terbawah, semakin TINGGI ketimpangannya (< 12% adalah Ketimpangan Tinggi, sedangkan > 17% adalah Ketimpangan Rendah)."
        },
        {
            "trap_description": "Tertukar cakupan kuintil pada kelompok 40-40-20",
            "common_mistake": "Mengambil hanya Kuintil 1 untuk mewakili 40% terbawah.",
            "safe_strategy": "Setiap kuintil mewakili 20% penduduk; 40% terbawah adalah penjumlahan Kuintil 1 dan Kuintil 2 (Q1 + Q2)."
        }
    ],
    "textbook": "Official Statistics Lanjutan (OSL)",
    "chapter_id": 8,
    "chapter_title": "Pertemuan 8: Kemiskinan dan Ketimpangan Pendapatan",
    "section": "8.3 Ukuran Ketimpangan Pendapatan dan Pengeluaran",
    "mode": "deep",
    "points": [
        {
            "id": "8.3.2",
            "name": "Kriteria Ketimpangan Bank Dunia",
            "importance": "高",
            "source_ref": "[Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 41-44]",
            "exam_focus": "Menguasai pembagian distribusi 40-40-20 Bank Dunia, ambang batas 12% dan 17% untuk kelompok 40% terbawah, interpretasi tingkat ketimpangan, dan perbandingannya dengan Koefisien Gini.",
            "textbook_excerpt": "Kriteria Bank Dunia mengklasifikasikan penduduk atas 3 kelompok menurut pendapatan: kelompok pendapatan terendah 40%, kelompok pendapatan menengah 40%, dan kelompok pendapatan tertinggi 20%. Ketimpangan diukur dengan menghitung persentase pendapatan yang diperoleh kelompok 40% terendah: jika < 12% ketimpangan tinggi; jika antara 12% dan 17% ketimpangan sedang; jika > 17% ketimpangan rendah [slide 37].",
            "intuition": "Bayangkan sebuah jamuan makan malam untuk 10 orang dengan 10 piring makanan:\n- Empat orang berpendapatan terendah (40% terbawah) duduk di ujung meja.\n- Jika keempat orang ini bersama-sama hanya mendapatkan kurang dari 1,2 piring (<12% total makanan), ketimpangan jamuan tersebut sangat tinggi dan tidak manusiawi.\n- Jika mereka mendapatkan antara 1,2 sampai 1,7 piring (12-17%), ketimpangan dinilai sedang.\n- Jika mereka berhasil menikmati lebih dari 1,7 piring (>17%), ketimpangan dinilai rendah dan distribusi dinilai cukup merata.",
            "formal": "### 1. Klasifikasi Distribusi Penduduk Menurut Bank Dunia\n\nBank Dunia membagi seluruh penduduk dalam perekonomian ke dalam 3 strata distribusi pendapatan/pengeluaran [slide 37]:\n1. **Kelompok 40% Terbawah** (*Low Income Group*): Penduduk pada persentil 0% s.d. 40% (mencakup Kuintil 1 dan Kuintil 2, atau Desil 1 s.d. 4).\n2. **Kelompok 40% Menengah** (*Middle Income Group*): Penduduk pada persentil 40% s.d. 80% (mencakup Kuintil 3 dan Kuintil 4, atau Desil 5 s.d. 8).\n3. **Kelompok 20% Teratas** (*High Income Group*): Penduduk pada persentil 80% s.d. 100% (mencakup Kuintil 5, atau Desil 9 dan 10).\n\n### 2. Formulasi Pengukuran Pangsa Pengeluaran 40% Terbawah\n\nMisalkan data dikelompokkan ke dalam 5 kuintil dengan pengeluaran masing-masing $C_1, C_2, C_3, C_4, C_5$ dan total konsumsi $C_{\\text{total}} = \\sum_{k=1}^5 C_k$.\nPangsa pengeluaran yang dinikmati oleh 40% penduduk terbawah ($S_{40}$) didefinisikan sebagai [slide 37, 39]:\n$$S_{40} = \\frac{C_1 + C_2}{C_{\\text{total}}} \\times 100\\% = (p_1 + p_2) \\times 100\\% = Y_2 \\times 100\\%$$\ndimana $Y_2$ adalah nilai kumulatif proporsi pengeluaran pada kuintil ke-2.\n\n### 3. Kriteria Batas Ketimpangan Bank Dunia\nBerdasarkan persentase $S_{40}$, Bank Dunia menetapkan tiga tingkatan ketimpangan distribusi [slide 37]:\n$$\\text{Kategori Ketimpangan} = \\begin{cases} \\text{Ketimpangan Tinggi}, & \\text{jika } S_{40} < 12\\% \\\\ \\text{Ketimpangan Sedang}, & \\text{jika } 12\\% \\le S_{40} \\le 17\\% \\\\ \\text{Ketimpangan Rendah}, & \\text{jika } S_{40} > 17\\% \\end{cases}$$\n\n### 4. Matriks Perbandingan: Kriteria Bank Dunia vs Koefisien Gini\n\n| Dimensi | Kriteria Bank Dunia (40% Terbawah) | Koefisien Gini (Gini Ratio) |\n|---|---|---|\n| **Fokus Pengukuran** | Spesifik pada kesejahteraan 40% lapisan penduduk termiskin | Agregat seluruh spektrum distribusi (menyeluruh dari 0 s.d. 100%) |\n| **Metrik Keluaran** | Persentase pangsa pengeluaran ($S_{40}$) dan 3 kategori verbal | Skalar kontinu indeks antara 0 s.d. 1 |\n| **Arah Interpretasi** | Semakin **besar** nilai $S_{40}$, ketimpangan semakin **rendah** | Semakin **besar** nilai Gini, ketimpangan semakin **tinggi** |\n| **Kelebihan** | Sangat intuitif dan relevan bagi kebijakan perlindungan sosial pro-poor | Memiliki landasan aksiomatis lengkap (*Pigou-Dalton transfer*) |\n| **Contoh Slide 39** | $S_{40} = 17,27\\% \\implies$ **Ketimpangan Rendah** | $G = 0,3770 \\implies$ **Ketimpangan Sedang** |\n\n### 5. Analisis Komparatif Slide 39\nPada contoh data kuintil Slide 39 [slide 39]:\n- $C_1 = 50.000$, $C_2 = 70.000$, Total = $695.000$.\n- $S_{40} = \\frac{50.000 + 70.000}{695.000} \\times 100\\% = \\frac{120.000}{695.000} \\times 100\\% = 17,27\\%$.\n- Karena $17,27\\% > 17,0\\%$, maka menurut kriteria Bank Dunia distribusi tersebut masuk ke dalam kategori **Ketimpangan Rendah**.\n- Terlihat adanya nuansa perbedaan kesimpulan: Koefisien Gini menunjukkan ketimpangan sedang ($0,3770$), sedangkan Bank Dunia menunjukkan ketimpangan rendah ($17,27\\%$). Hal ini wajar terjadi karena Bank Dunia hanya memotret kelompok 40% terbawah tanpa memperhitungkan ketimpangan yang terjadi di antara kuintil 4 dan kuintil 5 (kelompok kaya menguasai 50,36% konsumsi).",
            "pitfalls": "1. **Tertukar Arah Kategori**: Menganggap bahwa pangsa < 12% adalah ketimpangan rendah. Ingat bahwa 40% terbawah adalah kelompok miskin; jika bagian mereka makin kecil (<12%), artinya ketimpangan makin TINGGI.\n2. **Hanya Mengambil Kuintil 1**: Lupa bahwa 40% penduduk terdiri dari DUA kuintil (Q1 + Q2) atau EMPAT desil (D1 s.d. D4).\n3. **Salah Menetapkan Batas Ambang**: Angka patokan adalah 12% dan 17% (bukan 20% atau 40%).",
            "memory_hook": "Bank Dunia 40% Terbawah: < 12% Parah (Tinggi), 12-17% Sedang, > 17% Aman (Rendah).",
            "examples": [
                {
                    "type": "single",
                    "source_ref": "[Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 37]",
                    "problem": "Berdasarkan kriteria pengukuran ketimpangan Bank Dunia, suatu wilayah dikategorikan mengalami 'Ketimpangan Tinggi' apabila kelompok 40 persen penduduk berpendapatan terendah menikmati:",
                    "options": [
                        "Lebih dari 17 persen dari total pendapatan nasional.",
                        "Kurang dari 12 persen dari total pendapatan nasional.",
                        "Antara 12 persen sampai dengan 17 persen dari total pendapatan nasional.",
                        "Kurang dari 40 persen dari total pendapatan nasional."
                    ],
                    "answer": 1,
                    "solution": "Jawaban: **B**.\n\n**Pembahasan**:\nMenurut kriteria Bank Dunia [slide 37]:\n- Jika 40% penduduk terbawah memperoleh < 12% total pendapatan -> Ketimpangan Tinggi.\n- Jika memperoleh antara 12% dan 17% -> Ketimpangan Sedang.\n- Jika memperoleh > 17% -> Ketimpangan Rendah."
                },
                {
                    "type": "text",
                    "source_ref": "[Pertemuan_8_OSL_Indikator_Sosial_(1)_Indikator_Kemiskinan_dan_Ketimpangan___new.md, slide 37, 39]",
                    "problem": "Suatu provinsi memiliki distribusi pengeluaran kuintil penduduk sbb: Kuintil 1 = 50.000, Kuintil 2 = 70.000, Kuintil 3 = 100.000, Kuintil 4 = 125.000, Kuintil 5 = 350.000 (total pengeluaran = 695.000).\n1. Hitunglah persentase pengeluaran yang dinikmati oleh kelompok 40% terbawah.\n2. Tentukan kategori ketimpangan provinsi tersebut menurut kriteria Bank Dunia.\nTuliskan jawaban akhir dalam format: `Pangsa 40% Terbawah=...%, Kategori=...`.",
                    "answer": "Pangsa 40% Terbawah=17,27%, Kategori=Ketimpangan Rendah",
                    "solution": "Langkah-langkah perhitungan:\n1. Kelompok 40% terbawah terdiri dari Kuintil 1 dan Kuintil 2:\n   $$\\text{Total Pengeluaran 40\\% Terbawah} = 50.000 + 70.000 = 120.000$$\n2. Persentase terhadap total pengeluaran ($695.000$):\n   $$S_{40} = \\frac{120.000}{695.000} \\times 100\\% = 17,266...\\% \\approx 17,27\\%$$\n3. Evaluasi Kriteria Bank Dunia:\n   - Karena $17,27\\% > 17\\%$, maka provinsi tersebut masuk dalam kategori **Ketimpangan Rendah**.\n\n**Verifikasi Kode Python**:\n```python\nconsumption = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]\ntotal = sum(consumption)\nbottom_40 = (consumption[0] + consumption[1]) / total * 100.0\ncategory = 'Tinggi' if bottom_40 < 12.0 else ('Sedang' if bottom_40 <= 17.0 else 'Rendah')\nprint(f'Pangsa 40% Terbawah={bottom_40:.2f}%, Kategori=Ketimpangan {category}')\n# Output: Pangsa 40% Terbawah=17.27%, Kategori=Ketimpangan Rendah\n```"
                }
            ],
            "links": ["8.3.1", "8.2.1", "8.2.2", "8.2.3"]
        }
    ]
}

f832 = LESSONS_DIR / "8.3.2-kriteria-ketimpangan-bank-dunia.json"
f832.write_text(json.dumps(d832, ensure_ascii=False, indent=2), encoding="utf-8")
print("Created 8.3.2")
print("All 8 lesson units successfully generated and saved!")
