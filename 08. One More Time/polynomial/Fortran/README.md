# Cara Menggunakan: Fortran

## Requirements

- Sistem operasi yang mendukung GFortran
- GFortran (instalasi: https://fortran-lang.org/learn/os_setup/install_gfortran/)


## Cara Menjalankan/Melakukan Instalasi

0. Simpan nilai *data points* di sebuah file .txt dengan format sesuai dengan bagian Contoh I/O. Isi file harus benar - program mengasumsikan file sesuai dengan format.
1. Buka command line di folder yang mengandung file polynomial.f03
2. Jalankan perintah berikut:
    gfortran polynomial.f03 -o polynomial
3. Jalankan program dengan menjalankan perintah berikut, dengan mengganti [FILEPATH] dengan path menuju file .txt:
    ./polynomial [FILEPATH]

## Contoh I/O

### Contoh Isi File .txt:

    -0 1
    0.096 0.88
    0.5 3

### Contoh Perintah Menjalankan:

    ./polynomial data.txt
    
   Contoh di atas mengasumsikan file disimpan sebagai data.txt di folder yang sama dengan program.
    
### Contoh Output:

    1.0000000000000000 -2.4975247524752491 12.9950495049504973
    
   Dengan nilai paling kiri berupa nilai a0 dan paling kanan berupa nilai an-1 (dalam contoh ini, a2) 

