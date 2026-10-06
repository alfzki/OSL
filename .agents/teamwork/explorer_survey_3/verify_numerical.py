"""
Script Verifikasi Numerik Mandiri Persiapan UAS OSL (Standard Library Python)
Pertemuan 8 s.d. 13
"""

def verify_gini_slide39():
    print("=== 1. VERIFIKASI GINI RATIO (Pertemuan 8 Slide 39) ===")
    konsumsi = [50000.0, 70000.0, 100000.0, 125000.0, 350000.0]
    total_konsumsi = sum(konsumsi)
    pct_konsumsi = [k / total_konsumsi for k in konsumsi]
    fi = [0.2, 0.2, 0.2, 0.2, 0.2]
    
    # Hitung kumulatif pengeluaran Yi
    Yi = []
    cum = 0.0
    for p in pct_konsumsi:
        cum += p
        Yi.append(cum)
        
    term = []
    for i in range(len(fi)):
        y_prev = Yi[i-1] if i > 0 else 0.0
        term.append(fi[i] * (Yi[i] + y_prev))
        
    sum_term = sum(term)
    gini = 1.0 - sum_term
    
    print(f"Total Konsumsi: {total_konsumsi:,.2f}")
    print(f"Persentase Konsumsi: {[round(x, 4) for x in pct_konsumsi]}")
    print(f"Kumulatif Pengeluaran (Yi): {[round(x, 4) for x in Yi]}")
    print(f"fi * (Yi + Yi-1): {[round(x, 4) for x in term]}")
    print(f"Sum fi*(Yi + Yi-1): {sum_term:.4f}")
    print(f"Koefisien Gini: {gini:.4f}")
    
    # Kriteria Bank Dunia 40% terbawah (Q1 + Q2)
    wb_40 = Yi[1] * 100
    print(f"Proporsi 40% Terbawah: {wb_40:.2f}%")
    if wb_40 < 12:
        kategori = "Tinggi"
    elif wb_40 <= 17:
        kategori = "Sedang"
    else:
        kategori = "Rendah"
    print(f"Ketimpangan Bank Dunia: {kategori}")
    assert abs(gini - 0.3770) < 1e-4
    print("-> Verifikasi Gini: LULUS\n")

def verify_fgt():
    print("=== 2. VERIFIKASI INDEKS FGT (P0, P1, P2) ===")
    z = 600000.0
    n = 20
    incomes = [300000.0, 400000.0, 450000.0, 500000.0, 550000.0]
    q = len(incomes)
    
    gaps = [(z - y) / z for y in incomes]
    p0 = q / n
    p1 = sum(gaps) / n
    p2 = sum(g**2 for g in gaps) / n
    
    print(f"Garis Kemiskinan (z): {z}")
    print(f"Total Populasi (n): {n}, Jumlah Penduduk Miskin (q): {q}")
    print(f"Poverty Gaps ((z-y)/z): {[round(g, 4) for g in gaps]}")
    print(f"P0 (Headcount Index): {p0:.4f} ({p0*100:.2f}%)")
    print(f"P1 (Poverty Gap Index): {p1:.4f} ({p1*100:.2f}%)")
    print(f"P2 (Poverty Severity Index): {p2:.4f} ({p2*100:.2f}%)")
    assert abs(p0 - 0.25) < 1e-4
    assert abs(p1 - (1.3333333333333333 / 20)) < 1e-4
    print("-> Verifikasi FGT: LULUS\n")

def verify_ketenagakerjaan_essay():
    print("=== 3. VERIFIKASI ESSAY KETENAGAKERJAAN UAS 2022/2023 ===")
    total_pop = 18.0
    puk = 14.0 # 15+
    under_15 = 4.0
    ak = 9.0
    sekolah = 2.0
    irt = 2.0
    manula = 1.0
    bak = sekolah + irt + manula # 5.0
    
    bekerja_full = 6.0 # >= 35 jam
    bekerja_under = 1.0 # < 35 jam
    bekerja = bekerja_full + bekerja_under # 7.0
    
    phk = 1.0
    usaha = 0.5
    menunggu = 0.5
    pengangguran = phk + usaha + menunggu # 2.0
    
    tpak = (ak / puk) * 100.0
    tpt = (pengangguran / ak) * 100.0
    
    # Tingkat setengah penganggur menurut BPS: dihitung terhadap yang bekerja
    tsp = (bekerja_under / bekerja) * 100.0
    
    print(f"Penduduk Usia Kerja (PUK): {puk} juta")
    print(f"Angkatan Kerja (AK): {ak} juta")
    print(f"Bukan Angkatan Kerja (BAK): {bak} juta")
    print(f"Penduduk Bekerja: {bekerja} juta")
    print(f"Pengangguran Terbuka: {pengangguran} juta")
    print(f"TPAK: {tpak:.4f}% ({tpak:.2f}%)")
    print(f"TPT: {tpt:.4f}% ({tpt:.2f}%)")
    print(f"Jumlah Setengah Pengangguran: {bekerja_under} juta")
    print(f"Tingkat Setengah Penganggur (TSP BPS): {tsp:.4f}% ({tsp:.2f}%)")
    assert abs(tpak - 64.2857) < 0.01
    assert abs(tpt - 22.2222) < 0.01
    print("-> Verifikasi Ketenagakerjaan: LULUS\n")

def verify_ubinan():
    print("=== 4. VERIFIKASI SURVEI UBINAN PADI ===")
    plot_luas = 2.5 * 2.5 # 6.25 m2
    faktor_ha = 10000.0 / plot_luas # 1600
    
    # Kasus Soal Latihan PG 33
    hasil_pg33 = 4.0 # kg
    prod_kg_pg33 = hasil_pg33 * faktor_ha
    prod_ku_pg33 = prod_kg_pg33 / 100.0
    print(f"Kasus PG 33 (4.0 kg): {prod_kg_pg33} kg/ha = {prod_ku_pg33} ku/ha")
    assert prod_ku_pg33 == 64.0
    
    # Kasus UAS 2022/2023 Essay 2a
    hasil_uas = 4.5 # kg
    prod_kg_uas = hasil_uas * faktor_ha
    prod_ku_uas = prod_kg_uas / 100.0
    prod_ton_uas = prod_kg_uas / 1000.0
    print(f"Kasus UAS 2022/2023 Essay 2a (4.5 kg): {prod_kg_uas} kg/ha = {prod_ku_uas} ku/ha = {prod_ton_uas} ton/ha")
    assert prod_kg_uas == 7200.0
    print("-> Verifikasi Ubinan: LULUS\n")

def verify_inflasi_table():
    print("=== 5. VERIFIKASI TABEL INFLASI UAS 2022/2023 ESSAY 2b.1 ===")
    ihk_apr22 = 109.98
    ihk_mei22 = 110.42
    ihk_des22 = 113.59
    ihk_apr23 = 114.74
    inflasi_mtom_mei23 = 0.09 # persen
    
    # Hitung IHK Mei 2023
    ihk_mei23 = ihk_apr23 * (1.0 + inflasi_mtom_mei23 / 100.0)
    
    # Hitung Inflasi y-to-d Mei 2023
    inflasi_ytod_mei23 = ((ihk_mei23 - ihk_des22) / ihk_des22) * 100.0
    
    # Hitung Inflasi y-on-y Mei 2023
    inflasi_yony_mei23 = ((ihk_mei23 - ihk_mei22) / ihk_mei22) * 100.0
    
    print(f"IHK Mei 2023: {ihk_mei23:.6f} (dibulatkan: {ihk_mei23:.2f})")
    print(f"Inflasi y-to-d Mei 2023: {inflasi_ytod_mei23:.4f}% ({inflasi_ytod_mei23:.2f}%)")
    print(f"Inflasi y-on-y Mei 2023: {inflasi_yony_mei23:.4f}% ({inflasi_yony_mei23:.2f}%)")
    
    assert round(ihk_mei23, 2) == 114.84
    assert round(inflasi_ytod_mei23, 2) == 1.10
    assert round(inflasi_yony_mei23, 2) == 4.01
    print("-> Verifikasi Tabel Inflasi: LULUS\n")

def verify_ntp_table():
    print("=== 6. VERIFIKASI TABEL NTP UAS 2022/2023 ESSAY 2b.3 ===")
    # Data April 2023
    it_apr = 128.64
    ib_apr = 116.33
    ikrt_apr = 116.71
    bppbm_apr = 115.98
    
    ntp_apr = (it_apr / ib_apr) * 100.0
    ntup_apr = (it_apr / bppbm_apr) * 100.0
    
    # Data Mei 2023
    ntup_mei = 110.75
    bppbm_mei = 116.13
    ib_mei = 116.71
    ikrt_mei = 117.18
    
    it_mei = (ntup_mei * bppbm_mei) / 100.0
    ntp_mei = (it_mei / ib_mei) * 100.0
    inflasi_des_mei = ((ikrt_mei - ikrt_apr) / ikrt_apr) * 100.0
    
    print("April 2023:")
    print(f"  NTP: {ntp_apr:.4f} ({ntp_apr:.2f})")
    print(f"  NTUP: {ntup_apr:.4f} ({ntup_apr:.2f})")
    print("Mei 2023:")
    print(f"  It (dihitung dari NTUP & BPPBM): {it_mei:.6f} ({it_mei:.2f})")
    print(f"  NTP: {ntp_mei:.4f} ({ntp_mei:.2f})")
    print(f"  Inflasi Perdesaan (dari IKRT): {inflasi_des_mei:.4f}% ({inflasi_des_mei:.2f}%)")
    
    assert round(ntp_apr, 2) == 110.58
    assert round(ntup_apr, 2) == 110.92
    assert round(it_mei, 2) == 128.61
    assert round(ntp_mei, 2) == 110.20
    assert round(inflasi_des_mei, 2) == 0.40
    print("-> Verifikasi Tabel NTP: LULUS\n")

def verify_trade_tourism():
    print("=== 7. VERIFIKASI PERDAGANGAN LUAR NEGERI & PARIWISATA ===")
    # ISP Karet
    X_karet = 350.0
    M_karet = 164.0
    isp = (X_karet - M_karet) / (X_karet + M_karet)
    print(f"ISP Karet: {isp:.4f} ({isp:.2f})")
    assert round(isp, 2) == 0.36
    
    # ToT
    Px = 105.0
    Pm = 100.0
    tot = (Px / Pm) * 100.0
    print(f"ToT: {tot:.2f}")
    assert tot == 105.0
    
    # TPK & RLMT
    malam_kamar_terpakai = 1800
    malam_kamar_tersedia = 3000
    tpk = (malam_kamar_terpakai / malam_kamar_tersedia) * 100.0
    
    malam_tamu = 2500
    tamu = 1000
    rlmt = malam_tamu / tamu
    print(f"TPK Hotel: {tpk:.2f}%")
    print(f"RLMT Hotel: {rlmt:.2f} malam")
    assert tpk == 60.0
    assert rlmt == 2.5
    print("-> Verifikasi Perdagangan & Pariwisata: LULUS\n")

if __name__ == "__main__":
    verify_gini_slide39()
    verify_fgt()
    verify_ketenagakerjaan_essay()
    verify_ubinan()
    verify_inflasi_table()
    verify_ntp_table()
    verify_trade_tourism()
    print("ALL 7 VERIFICATION SUITES PASSED SUCCESSFULLY!")
