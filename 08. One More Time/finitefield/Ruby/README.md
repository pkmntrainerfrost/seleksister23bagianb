# Cara Menggunakan: Python 3.x

## Requirements

- Sistem operasi yang mendukung Ruby
- Ruby (instalasi: https://www.ruby-lang.org/en/documentation/installation/)

## Cara Menjalankan/Melakukan Instalasi

0. Simpan nilai *data points* di sebuah file .txt dengan format sesuai dengan bagian Contoh I/O. Isi file HARUS benar/sesuai format. Setiap nilai HARUS berupa integer positif yang merupakan anggota dari GF(P).
1. Buka command line di folder yang mengandung file polynomial.py
2. Jalankan perintah berikut dengan mengganti [P] dengan sebuah bilangan prima yang menjadi orde Galois Field (diasumsikan valid), dan [FILEPATH] dengan path menuju file .txt:
    ruby polynomial.rb [P] [FILEPATH]

## Contoh I/O

### Contoh Isi File .txt:

    1 3
    5 7
    6 8

### Contoh Perintah Menjalankan:

    ruby polynomial.rb 11 data.txt
    
   Contoh di atas mengasumsikan file disimpan sebagai data.txt di folder yang sama dengan program.
    
### Contoh Output:

    2 1 0

   Dengan nilai paling kiri berupa nilai a0 dan paling kanan berupa nilai an-1 (dalam contoh ini, a2) 
