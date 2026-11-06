import math


while True:
    print("\n=== LUAS DAN KELILING BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Trapesium")
    print("6. Jajar Genjang")
    print("7. Belah Ketupat")
    print("8. Layang-Layang")
    print("9. Segilima Beraturan")
    print("10. Segienam Beraturan")
    print("0. Keluar")

    pilihan = input("Pilih bangun datar (0-10): ")

    if pilihan == "0":
        print("Program selesai.")
        break
    elif pilihan == "1":
        nama = "Persegi"
        pertanyaan = ["sisi"]
    elif pilihan == "2":
        nama = "Persegi Panjang"
        pertanyaan = ["panjang", "lebar"]
    elif pilihan == "3":
        nama = "Segitiga"
        pertanyaan = ["sisi pertama", "sisi kedua", "sisi ketiga"]
    elif pilihan == "4":
        nama = "Lingkaran"
        pertanyaan = ["jari-jari"]
    elif pilihan == "5":
        nama = "Trapesium"
        pertanyaan = ["sisi sejajar pertama", "sisi sejajar kedua", "tinggi",
                      "sisi miring pertama", "sisi miring kedua"]
    elif pilihan == "6":
        nama = "Jajar Genjang"
        pertanyaan = ["alas", "sisi miring", "tinggi"]
    elif pilihan == "7":
        nama = "Belah Ketupat"
        pertanyaan = ["diagonal pertama", "diagonal kedua"]
    elif pilihan == "8":
        nama = "Layang-Layang"
        pertanyaan = ["diagonal pertama", "diagonal kedua",
                      "sisi pendek", "sisi panjang"]
    elif pilihan == "9":
        nama = "Segilima Beraturan"
        pertanyaan = ["sisi"]
    elif pilihan == "10":
        nama = "Segienam Beraturan"
        pertanyaan = ["sisi"]
    else:
        print("Pilihan tidak tersedia. Coba lagi.")
        continue

    # Simpan semua ukuran dalam list sesuai urutan pertanyaan.
    ukuran = []
    for bagian in pertanyaan:
        angka = float(input("Masukkan " + bagian + ": "))
        ukuran.append(angka)

    valid = True
    for angka in ukuran:
        if angka <= 0:
            valid = False

    if not valid:
        print("Semua ukuran harus lebih besar dari 0.")
        continue

    if pilihan == "1":
        sisi = ukuran[0]
        luas = sisi * sisi
        keliling = 4 * sisi
    elif pilihan == "2":
        panjang, lebar = ukuran
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
    elif pilihan == "3":
        sisi_1, sisi_2, sisi_3 = ukuran
        if (sisi_1 + sisi_2 <= sisi_3 or
                sisi_1 + sisi_3 <= sisi_2 or
                sisi_2 + sisi_3 <= sisi_1):
            print("Ketiga sisi tidak dapat membentuk segitiga.")
            continue
        keliling = sisi_1 + sisi_2 + sisi_3
        setengah_keliling = keliling / 2
        # Rumus Heron: luas dari tiga sisi segitiga.
        luas = math.sqrt(setengah_keliling *
                         (setengah_keliling - sisi_1) *
                         (setengah_keliling - sisi_2) *
                         (setengah_keliling - sisi_3))
    elif pilihan == "4":
        jari_jari = ukuran[0]
        luas = math.pi * jari_jari * jari_jari
        keliling = 2 * math.pi * jari_jari
    elif pilihan == "5":
        sisi_1, sisi_2, tinggi, sisi_3, sisi_4 = ukuran
        luas = (sisi_1 + sisi_2) * tinggi / 2
        keliling = sisi_1 + sisi_2 + sisi_3 + sisi_4
    elif pilihan == "6":
        alas, sisi_miring, tinggi = ukuran
        luas = alas * tinggi
        keliling = 2 * (alas + sisi_miring)
    elif pilihan == "7":
        diagonal_1, diagonal_2 = ukuran
        luas = diagonal_1 * diagonal_2 / 2
        sisi = math.sqrt((diagonal_1 / 2) ** 2 + (diagonal_2 / 2) ** 2)
        keliling = 4 * sisi
    elif pilihan == "8":
        diagonal_1, diagonal_2, sisi_pendek, sisi_panjang = ukuran
        luas = diagonal_1 * diagonal_2 / 2
        keliling = 2 * (sisi_pendek + sisi_panjang)
    elif pilihan == "9":
        sisi = ukuran[0]
        luas = math.sqrt(5 * (5 + 2 * math.sqrt(5))) * sisi ** 2 / 4
        keliling = 5 * sisi
    elif pilihan == "10":
        sisi = ukuran[0]
        luas = 3 * math.sqrt(3) * sisi ** 2 / 2
        keliling = 6 * sisi

    print("\nBangun datar:", nama)
    print(f"Luas     = {luas:.2f}")
    print(f"Keliling = {keliling:.2f}")
