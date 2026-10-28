
angka = [10, 20, 30, 40, 50]
total = 0

for i in range(len(angka)):
    total += angka[i]
    print("Iterasi:", i + 1)
    print("Angka:", angka[i])
    print("Total sementara:", total)
    print("-" * 25)

print("Total akhir:", total)
