# Tugas 5 PBP

## Perbedaan Inline, Internal, dan External CSS
Perbedaan yang dapat kita lihat dari lokasi dan range penggunaannya. Contohnya untuk inline berada dalam elemen yang menggunakan atribut style. Internal dalam HTML yang ber-tag <style> dan external berada diluar file html yang nantinya akan di import menggunakan load static dan implementasinya sesuai dengan tag yang diedit.
Masing-masing memiliki kelebihan, untuk external design-nya bisa dipakai untuk beberapa laman sekaligus sehingga tidak perlu membuat design berulang kali. Untuk Inline CSS kelebihannya lebih terfokus pada satu elemen sehingga pengaturannya bisa lebih detail. Namun, code akan terlihat membingungkan karna berantakan. Internal CSS memiliki kelebihan yaitu khusus untuk satu page tertentu dan lebih mudah untuk dimodifikasi atau dilihat.

## Tag HTML5 yang saya ketahui
main, yaitu tag yang menandakan konten utama dari suatu laman. Selanjutnya ada section yang menunjukkan bagian dari halaman lain, lalu aside yaitu tag yang menandakan bagian tersebut tidak berhubungan dengan konten utama.

## Tipe-tipe CSS Selector
"*" yaitu universal selector, bisa dipakai oleh semua elemen.
element yaitu selector untuk suatu tag seperti input, h1, a, dll.
class atau biasa ditulis .class digunakan untuk tag yang menggunakan class itu.
Terakhir ada id atau #id yaitu selector untuk elemen yang menggunakan id itu.

## Cara saya mengimplementasikan checklist diatas
1. Pada bagian login saya menggunakan external css untuk memberi design pada laman login. External CSS ini saya pakai dengan mengimport dan memanggil load.static agar CSS dapat diimplementasikan pada website.
2. Saya juga menambahkan beberapa fungsi pada back-end aplikasi agar fungsi yang saya tambahkan dapat berjalan.
3. Pada bagian register saya menggunakan Internal CSS untuk memberikan design pada laman web register.
4. Pada bagian home dan create task saya menggunakan komponen yang ada di dokumentasi DaisyUI dengan Tailwind CSS.