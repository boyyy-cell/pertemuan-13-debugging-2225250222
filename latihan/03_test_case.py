
def status_kelulusan(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_cases = [
    (80, "Lulus"),
    (60, "Lulus"),
    (59, "Tidak lulus"),
    (0, "Tidak lulus"),
]

for nomor, (nilai, expected) in enumerate(test_cases, start=1):
    actual = status_kelulusan(nilai)

    if actual == expected:
        hasil = "PASS"
    else:
        hasil = "FAIL"

    print(f"Test {nomor}: Nilai {nilai}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print(f"Hasil:    {hasil}")
    print("-" * 30)
