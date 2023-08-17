# Cara Menggunakan: Ruby

## Requirements

- Sistem operasi yang mendukung Ruby
- Ruby (instalasi: https://www.ruby-lang.org/en/documentation/installation/)

## Cara Menjalankan/Melakukan Instalasi

0. Simpan nilai *data points* di sebuah file .txt dengan format sesuai dengan bagian Contoh I/O. Isi file HARUS benar/sesuai format.
1. Buka command line di folder yang mengandung file polynomial.rb
2. Jalankan perintah berikut dengan mengganti [FILEPATH] dengan path menuju file .txt:
    ruby polynomial.rb [FILEPATH]

## Contoh I/O

### Contoh Isi File .txt:

    -0 1
    0.096 0.88
    0.5 3

### Contoh Perintah Menjalankan:

    ruby polynomial.rb data.txt
    
   Contoh di atas mengasumsikan file disimpan sebagai data.txt di folder yang sama dengan program.
    
### Contoh Output:

    1.0 -2.497524752475249 12.995049504950497

   Dengan nilai paling kiri berupa nilai a0 dan paling kanan berupa nilai an-1 (dalam contoh ini, a2) 
