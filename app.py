
def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)


def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar


def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


def luas_lingkaran(jari_jari):
    import math
    return math.pi * jari_jari ** 2


# Database rumus
rumus = [
    {
        "id": 1,
        "nama": "Keliling Persegi Panjang",
        "deskripsi": "Menghitung keliling persegi panjang",
        "input": [
            {"nama": "panjang", "label": "Sisi panjang"},
            {"nama": "lebar", "label": "Sisi lebar"}
        ],
        "formula": "2 x (panjang + lebar)",
        "hitung": keliling_persegi_panjang,
        "format_hasil": lambda v: f"2 × ({v[0]:g} + {v[1]:g})"

    },
    {
        "id": 2,
        "nama": "Luas Persegi Panjang",
        "deskripsi": "Menghitung luas persegi panjang",
        "input": [
            {"nama": "panjang", "label": "Panjang"},
            {"nama": "lebar", "label": "Lebar"}
        ],
        "formula": "panjang x lebar",
        "hitung": luas_persegi_panjang,
        "format_hasil": lambda v: f"{v[0]:g} × {v[1]:g}"

    },
    {
        "id": 3,
        "nama": "Luas Segitiga",
        "deskripsi": "Menghitung luas segitiga",
        "input": [
            {"nama": "alas", "label": "Alas"},
            {"nama": "tinggi", "label": "Tinggi"}
        ],
        "formula": "0.5 x alas x tinggi",
        "hitung": luas_segitiga,
        "format_hasil": lambda v: f"0.5 × {v[0]:g} × {v[1]:g}"

    },
    {
        "id": 4,
        "nama": "Luas Lingkaran",
        "deskripsi": "Menghitung luas lingkaran",
        "input": [
            {"nama": "jari_jari", "label": "Jari-jari"}
        ],
        "formula": "π x jari-jari²",
        "hitung": luas_lingkaran,
        "format_hasil": lambda v: f"π × {v[0]:g}²"
    }
]


def tampilkan_menu():
    print("\n=== KALKULATOR RUMUS MATEMATIKA ===")

    for item in rumus:
        print(f"{item['id']}. {item['nama']}")

    print("0. Keluar")


def minta_angka(label):
    while True:
        try:
            nilai = float(input(f"Masukkan {label}: "))

            if nilai < 0:
                print("Nilai tidak boleh negatif.")
                continue

            return nilai

        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


def jalankan_rumus(item):
    print(f"\n=== {item['nama']} ===")
    print(f"Formula: {item['formula']}")

    nilai_input = []

    for field in item["input"]:
        nilai = minta_angka(field["label"])
        nilai_input.append(nilai)

    hasil = item["hitung"](*nilai_input)

    ekspresi = item["format_hasil"](nilai_input)

    print(f"\nPerhitungan: {ekspresi} = {hasil:g}")



def main():
    while True:
        tampilkan_menu()

        try:
            pilihan = int(input("\nPilih rumus: "))
        except ValueError:
            print("Masukkan nomor menu yang valid.")
            continue

        if pilihan == 0:
            print("Program selesai.")
            break

        item = next(
            (r for r in rumus if r["id"] == pilihan),
            None
        )

        if item is None:
            print("Pilihan tidak tersedia.")
            continue

        try:
            jalankan_rumus(item)
        except (ValueError, OverflowError) as error:
            print(f"Perhitungan gagal: {error}")

        # Konfirmasi setelah perhitungan
        while True:
            print("\n1. Hitung lagi")
            print("0. Selesai")

            konfirmasi = input("Pilihan: ").strip()

            if konfirmasi == "1":
                break
            elif konfirmasi == "0":
                print("Program selesai.")
                return
            else:
                print("Pilihan tidak valid. Masukkan 1 atau 0.")


if __name__ == "__main__":
    main()
