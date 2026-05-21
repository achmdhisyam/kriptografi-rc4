* Nama: Achmad Hisyammuddin
* NIM : 24051204165
* Kelas : TI 2024 E

Link Youtube:https://youtu.be/IQsFp0LGZ3g

# Implementasi Algoritma Kriptografi RC4 

Repositori ini dibuat untuk memenuhi Tugas Individu: Analisis dan Implementasi Mekanisme Kriptografi pada mata kuliah keamanan data dan informasi. Program ini mengimplementasikan algoritma **RC4 (Stream Cipher)**  menggunakan bahasa pemrograman Python .

##  Tujuan Proyek
* Memahami mekanisme internal dari *Symmetric Stream Cipher*, khususnya algoritma RC4.
* Mengimplementasikan tahap *Key-Scheduling Algorithm* (KSA) dan *Pseudo-Random Generation Algorithm* (PRGA) secara murni menggunakan logika matematika bitwise.
* Menyediakan antarmuka terminal yang interaktif bagi pengguna untuk melakukan enkripsi dan dekripsi teks.

## Struktur Algoritma
Program ini dibagi menjadi beberapa fungsi inti sesuai dengan standar akademik algoritma RC4:
1. **KSA (Key-Scheduling Algorithm):** Menginisialisasi dan mengacak array status awal (S-Box) berukuran 256 byte berdasarkan kunci (*key*) yang dimasukkan pengguna.
2. **PRGA (Pseudo-Random Generation Algorithm):** Menghasilkan kunci acak (*keystream*) secara dinamis dari S-Box yang terus dimodifikasi di setiap iterasinya sepanjang teks input.
3. **Enkripsi:** Mengubah karakter teks asli (*plaintext*) menjadi deretan angka ASCII, mengombinasikannya dengan *keystream* menggunakan operasi ** XOR (`^`)**, dan mengonversinya ke format Hexadecimal.
4. **Dekripsi:** Kebalikan dari proses enkripsi, memotong string Hexadecimal, melakukan operasi XOR ulang dengan *keystream* yang sama untuk mengembalikan data ke teks asli.

##   Sistem
* Python versi 3.x atau yang lebih baru.

##  Cara Menjalankan Program

1. **Clone atau Download Repositori**
   git clone https://github.com/achmdhisyam/kriptografi-rc4

2. **Buka Terminal / Command Prompt**
   Arahkan terminal ke direktori tempat file Python tersebut disimpan.

3. **Jalankan Perintah Berikut:**
   ```bash
   python kripto.py