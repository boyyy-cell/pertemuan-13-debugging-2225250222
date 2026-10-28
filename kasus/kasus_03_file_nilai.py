
def baca_nilai(nama_file):
    hasil = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                nama = bagian[0]
                nilai = int(bagian[1])

                hasil.append((nama, nilai))

    except FileNotFoundError:
        print("Error: file tidak ditemukan.")
    except (ValueError, IndexError):
        print("Error: format data tidak valid.")

    return hasil


data = baca_nilai("data_nilai.txt")

print("Data nilai:")
for nama, nilai in data:
    print(f"{nama}: {nilai}")
