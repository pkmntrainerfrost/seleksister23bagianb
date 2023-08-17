# Cara Menggunakan: Go

## Requirements

- Sistem operasi yang mendukung Go
- Go (instalasi: https://go.dev/doc/install)


## Cara Menjalankan/Melakukan Instalasi

0. Simpan nilai *data points* di sebuah file .txt dengan format sesuai dengan bagian Contoh I/O. Isi file HARUS benar/sesuai format.
1. Buka command line di folder yang mengandung file polynomial.go
2. Jalankan perintah berikut untuk menjalankan, dengan mengganti [P] dengan sebuah bilangan prima yang menjadi orde Galois Field (diasumsikan valid), dan [FILEPATH] dengan path menuju file .txt:
    go run polynomial.go [FILEPATH]

## Contoh I/O

### Contoh Isi File .txt:

    1 3
    5 7
    6 8

### Contoh Perintah Menjalankan:

    go run polynomial.go 11 data.txt
    
   Contoh di atas mengasumsikan file disimpan sebagai data.txt di folder yang sama dengan program.
    
### Contoh Output:

    2 1 0 

   Dengan nilai paling kiri berupa nilai a0 dan paling kanan berupa nilai an-1 (dalam contoh ini, a2) 
