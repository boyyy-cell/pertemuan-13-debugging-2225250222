
def hitung_rata_rata(nilai):
    total = sum(nilai)
    rata_rata = total / 5
    return rata_rata


data_nilai = [80, 60, 90, 70]

hasil = hitung_rata_rata(data_nilai)

print("Data nilai:", data_nilai)
print("Jumlah nilai:", sum(data_nilai))
print("Banyak data:", len(data_nilai))
print("Rata-rata:", hasil)
