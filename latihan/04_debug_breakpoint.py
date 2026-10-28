
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon


harga = 200000
persentase = 10

hasil = hitung_diskon(harga, persentase)

print("Harga awal:", harga)
print("Persentase diskon:", persentase, "%")
print("Harga setelah diskon:", hasil)
