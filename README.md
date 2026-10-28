# Pertemuan 13 — Debugging, Tracing, dan Testing Python

## Identitas Mahasiswa

- Nama: Farid Syahputra
- NIM: 2225250222
- Kelas: 3F
- Program Studi: S1 Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman
- Tahun Akademik: 2026/2027 Ganjil

## Tujuan Praktikum

Memahami proses debugging, tracing, testing, penyusunan test case, serta memperbaiki kesalahan pada program Python.

## Daftar Praktikum

- `latihan/01_trace_loop.py`: melakukan tracing pada perulangan.
- `latihan/02_trace_fungsi.py`: memahami alur pemanggilan fungsi.
- `latihan/03_test_case.py`: menjalankan pengujian test case.
- `latihan/04_debug_breakpoint.py`: memeriksa nilai variabel menggunakan breakpoint.
- `kasus/kasus_01_batas_kelulusan.py`: menguji batas kelulusan.
- `kasus/kasus_02_rata_rata.py`: memperbaiki perhitungan rata-rata.
- `kasus/kasus_03_file_nilai.py`: menangani kesalahan pembacaan file.
- `praktik/praktik_4_debugging.py`: memperbaiki dan menguji program.

## Bug Report

### Bug 1 — Batas Kelulusan

- Gejala: nilai 60 dinyatakan tidak lulus.
- Penyebab: kondisi menggunakan `nilai > 60`.
- Perbaikan: mengganti kondisi menjadi `nilai >= 60`.

### Bug 2 — Perhitungan Rata-rata

- Gejala: rata-rata dihitung menggunakan pembagi tetap.
- Penyebab: program menggunakan angka 5, bukan jumlah data.
- Perbaikan: menggunakan `len(nilai)` sebagai pembagi.

### Bug 3 — Nilai Tertinggi

- Gejala: nilai tertinggi menghasilkan angka yang salah.
- Penyebab: kondisi perbandingan menggunakan operator `<` dan nilai awal 0.
- Perbaikan: menggunakan elemen pertama sebagai nilai awal dan operator `>`.

## Hasil Pengujian Setelah Perbaikan

| Test Case | Expected | Hasil |
|---|---|---|
| Rata-rata 4 data | 75.0 | PASS |
| Rata-rata 2 data | 90.0 | PASS |
| Nilai 60 | Lulus | PASS |
| Nilai 59 | Tidak lulus | PASS |
| Nilai tertinggi | 90 | PASS |

## Cara Menjalankan Program

Jalankan perintah berikut melalui terminal pada folder utama proyek:

`python praktik/praktik_4_debugging.py`

## Kesimpulan

Melalui praktikum ini, saya mempelajari bahwa debugging membantu menemukan dan memperbaiki kesalahan program. Tracing memudahkan pemahaman alur eksekusi dan perubahan variabel, sedangkan testing digunakan untuk memastikan hasil program sesuai dengan yang diharapkan. Pengujian ulang diperlukan untuk memastikan perbaikan tidak menimbulkan kesalahan baru.
