
while True:
    print("\n=== PROGRAM PERHITUNGAN MATEMATIKA ===")
    print("1. Luas Persegi Panjang")
    print("2. Keliling Persegi Panjang")
    print("3. Luas Segitiga")
    print("4. Luas Lingkaran")
    print("0. Keluar")

    pilihan = input("Pilih rumus: ")

    if pilihan == "1":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))

        hasil = panjang * lebar

        print(f"\nLuas = {panjang} x {lebar} = {hasil}")

    elif pilihan == "2":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))

        hasil = 2 * (panjang + lebar)

        print(
            f"\nKeliling = 2 x ({panjang} + {lebar})"
            f" = {hasil}"
        )

    elif pilihan == "3":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))

        hasil = 0.5 * alas * tinggi

        print(
            f"\nLuas = 1/2 x {alas} x {tinggi}"
            f" = {hasil}"
        )

    elif pilihan == "4":
        import math

        jari_jari = float(input("Masukkan jari-jari: "))

        hasil = math.pi * jari_jari ** 2

        print(
            f"\nLuas = pi x {jari_jari}^2"
            f" = {hasil:.2f}"
        )

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
        continue

    print("\n1. Hitung lagi")
    print("0. Selesai")

    ulang = input("Pilihan: ")

    if ulang == "0":
        print("Program selesai.")
        break
    elif ulang == "1":
        continue
    else:
        print("Pilihan tidak valid. Program selesai.")
        break
