
def status_kelulusan(nilai):
    if nilai > 60:
        return "Lulus"
    else:
        return "Tidak lulus"


test_nilai = [80, 60, 59]

for nilai in test_nilai:
    hasil = status_kelulusan(nilai)
    print(f"Nilai: {nilai} -> {hasil}")
