# Cara Menggunakan: Rust

## Requirements

- Sistem operasi yang mendukung Rust
- Rust (instalasi: https://www.rust-lang.org/tools/install)

## Cara Menjalankan/Melakukan Instalasi

0. Simpan nilai *data points* di sebuah file .txt dengan format sesuai dengan bagian Contoh I/O. Isi file HARUS benar/sesuai format.
1. Buka command line di folder yang mengandung file polynomial.rs
2. Jalankan perintah berikut:
    rustc polynomial.rs
3. Jalankan program dengan menjalankan perintah berikut (untuk Windows), dengan mengganti [FILEPATH] dengan path menuju file .txt:
    .\polynomial.exe [FILEPATH]

## Contoh I/O

### Contoh Isi File .txt:

    -0 1
    0.096 0.88
    0.5 3

### Contoh Perintah Menjalankan:

    .\polynomial.exe data.txt
    
   Contoh di atas mengasumsikan file disimpan sebagai data.txt di folder yang sama dengan program. Untuk MacOS/Linux, gunakan perintah ./polynomial data.txt
    
### Contoh Output:

    1 -2.497524752475249 12.995049504950497

   Dengan nilai paling kiri berupa nilai a0 dan paling kanan berupa nilai an-1 (dalam contoh ini, a2) 
