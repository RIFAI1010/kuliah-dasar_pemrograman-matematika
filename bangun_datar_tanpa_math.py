# Nilai pendekatan pi tanpa mengimpor library.
pi = 3.14

nama_bangun = [
    "Persegi", "Persegi Panjang", "Segitiga", "Lingkaran", "Trapesium",
    "Jajar Genjang", "Belah Ketupat", "Layang-Layang",
    "Segilima Beraturan", "Segienam Beraturan"
]

while True:
    print("\n=== PROGRAM BANGUN DATAR ===")
    for nomor in range(10):
        print(f"{nomor + 1}. {nama_bangun[nomor]}")
    print("0. Keluar")

    pilihan = input("Pilih bangun datar (0-10): ")
    if pilihan == "0":
        print("Program selesai.")
        break
    if pilihan not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print("Pilihan bangun datar tidak tersedia.")
        continue

    bangun = nama_bangun[int(pilihan) - 1]
    print(f"\n=== {bangun} ===")
    print("1. Hitung luas")
    print("2. Hitung keliling")
    jenis = input("Pilih perhitungan (1/2): ")
    if jenis != "1" and jenis != "2":
        print("Pilihan perhitungan tidak tersedia.")
        continue

    # Hanya minta ukuran yang diperlukan untuk pilihan perhitungan.
    if pilihan == "1":
        pertanyaan = ["sisi"]
    elif pilihan == "2":
        pertanyaan = ["panjang", "lebar"]
    elif pilihan == "3":
        if jenis == "1":
            pertanyaan = ["alas", "tinggi"]
        else:
            pertanyaan = ["sisi pertama", "sisi kedua", "sisi ketiga"]
    elif pilihan == "4":
        pertanyaan = ["jari-jari"]
    elif pilihan == "5":
        if jenis == "1":
            pertanyaan = ["sisi sejajar pertama", "sisi sejajar kedua", "tinggi"]
        else:
            pertanyaan = ["sisi pertama", "sisi kedua", "sisi ketiga", "sisi keempat"]
    elif pilihan == "6":
        if jenis == "1":
            pertanyaan = ["alas", "tinggi"]
        else:
            pertanyaan = ["alas", "sisi miring"]
    elif pilihan == "7":
        if jenis == "1":
            pertanyaan = ["diagonal pertama", "diagonal kedua"]
        else:
            pertanyaan = ["sisi"]
    elif pilihan == "8":
        if jenis == "1":
            pertanyaan = ["diagonal pertama", "diagonal kedua"]
        else:
            pertanyaan = ["sisi pendek", "sisi panjang"]
    else:
        pertanyaan = ["sisi"]

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
        if jenis == "1":
            hasil = ukuran[0] ** 2
        else:
            hasil = 4 * ukuran[0]
    elif pilihan == "2":
        if jenis == "1":
            hasil = ukuran[0] * ukuran[1]
        else:
            hasil = 2 * (ukuran[0] + ukuran[1])
    elif pilihan == "3":
        if jenis == "1":
            hasil = ukuran[0] * ukuran[1] / 2
        else:
            if (ukuran[0] + ukuran[1] <= ukuran[2] or
                    ukuran[0] + ukuran[2] <= ukuran[1] or
                    ukuran[1] + ukuran[2] <= ukuran[0]):
                print("Ketiga sisi tidak dapat membentuk segitiga.")
                continue
            hasil = ukuran[0] + ukuran[1] + ukuran[2]
    elif pilihan == "4":
        if jenis == "1":
            hasil = pi * ukuran[0] ** 2
        else:
            hasil = 2 * pi * ukuran[0]
    elif pilihan == "5":
        if jenis == "1":
            hasil = (ukuran[0] + ukuran[1]) * ukuran[2] / 2
        else:
            hasil = ukuran[0] + ukuran[1] + ukuran[2] + ukuran[3]
    elif pilihan == "6":
        if jenis == "1":
            hasil = ukuran[0] * ukuran[1]
        else:
            hasil = 2 * (ukuran[0] + ukuran[1])
    elif pilihan == "7":
        if jenis == "1":
            hasil = ukuran[0] * ukuran[1] / 2
        else:
            hasil = 4 * ukuran[0]
    elif pilihan == "8":
        if jenis == "1":
            hasil = ukuran[0] * ukuran[1] / 2
        else:
            hasil = 2 * (ukuran[0] + ukuran[1])
    elif pilihan == "9":
        if jenis == "1":
            hasil = (5 * (5 + 2 * 5 ** 0.5)) ** 0.5 * ukuran[0] ** 2 / 4
        else:
            hasil = 5 * ukuran[0]
    elif pilihan == "10":
        if jenis == "1":
            hasil = 3 * 3 ** 0.5 * ukuran[0] ** 2 / 2
        else:
            hasil = 6 * ukuran[0]

    if jenis == "1":
        print(f"\nLuas {bangun} = {hasil:.2f}")
    else:
        print(f"\nKeliling {bangun} = {hasil:.2f}")

    print("\n1. Hitung lagi")
    print("0. Selesai")
    ulang = input("Pilihan: ")
    while ulang != "1" and ulang != "0":
        print("Pilih 1 atau 0.")
        ulang = input("Pilihan: ")
    if ulang == "0":
        print("Program selesai.")
        break
