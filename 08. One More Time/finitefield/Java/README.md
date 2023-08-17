# Cara Menggunakan: Java

## Requirements

- Sistem operasi yang mendukung Java
- Java (instalasi: https://docs.oracle.com/en/java/javase/20/install/overview-jdk-installation.html)

## Cara Menjalankan/Melakukan Instalasi

0. Simpan nilai *data points* di sebuah file .txt dengan format sesuai dengan bagian Contoh I/O. Isi file HARUS benar/sesuai format.
1. Buka command line di folder yang mengandung file polynomial.java
2. Jalankan perintah berikut:
    javac polynomial.java
3. Jalankan perintah berikut dengan mengganti [P] dengan sebuah bilangan prima yang menjadi orde Galois Field (diasumsikan valid), dan [FILEPATH] dengan path menuju file .txt:
    java polynomial [P] [FILEPATH]

## Contoh I/O

### Contoh Isi File .txt:

    1 3
    5 7
    6 8

### Contoh Perintah Menjalankan:

    java polynomial.java 11 data.txt
    
   Contoh di atas mengasumsikan file disimpan sebagai data.txt di folder yang sama dengan program.
    
### Contoh Output:

    2 1 0

   Dengan nilai paling kiri berupa nilai a0 dan paling kanan berupa nilai an-1 (dalam contoh ini, a2) 
