# Cara Menggunakan: Scala

## Requirements

- Sistem operasi yang mendukung Scala
- Scala (instalasi: https://docs.scala-lang.org/getting-started/index.html)

## Cara Menjalankan/Melakukan Instalasi

0. Simpan nilai *data points* di sebuah file .txt dengan format sesuai dengan bagian Contoh I/O. Isi file HARUS benar/sesuai format.
1. Buka command line di folder yang mengandung file polynomial.java
2. Jalankan perintah berikut:
    scalac polynomial.java
3. Jalankan program dengan menjalankan perintah berikut, dengan mengganti [FILEPATH] dengan path menuju file .txt:
    scala polynomial [FILEPATH]

## Contoh I/O

### Contoh Isi File .txt:

    -0 1
    0.096 0.88
    0.5 3

### Contoh Perintah Menjalankan:

    scala polynomial data.txt
    
   Contoh di atas mengasumsikan file disimpan sebagai data.txt di folder yang sama dengan program.
    
### Contoh Output:

    1.0 -2.497524752475249 12.995049504950497

   Dengan nilai paling kiri berupa nilai a0 dan paling kanan berupa nilai an-1 (dalam contoh ini, a2) 
