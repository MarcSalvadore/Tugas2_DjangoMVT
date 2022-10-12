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

# Tugas 6 PBP

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

### Asynchronous programming
merupakan bentuk dari paralel programming yang mengatur suatu pekerjaan untuk berjalan terpisah dari program utamanya. Async juga bersifat non-blocking yang berarti bisa mengirimkan beberapa sinyal sekaligus kepada server. Async biasa digunakan untuk meningkatkan pengalaman pengguna karena sifatnya yang responsif.
### Synchronous programming
merupakan bentuk dari single-thread programming yang berarti hanya menjalankan satu operasi atau program secara bersamaan. Sync bersifat blocking yang berarti hanya bisa mengirimkan satu sinyal/request kepada server dalam satu waktu dan sinyal berikutnya baru bisa dikirim ketika sudah mendapat jawaban dari server. Sync ditujukan untuk membantu developers dalam membangun app mereka, karena lebih mudah untuk di coding.

## Event-Driven Programming
merupakan paradigma yang menjelaskan bahwa alur yang dijalankan suatu program bergantung pada event atau tindakan yang terjadi antara user dan client. Pada tugas 6 ini paradigma terdapat pada dokumen yang akan ditampilkan, button untuk membuat form baru, dan event saat pemanggilan AJAX berhasil.

## Penerapan asynchronous programming pada AJAX
dapat terlihat dari keresponsifan web saat AJAX dijalankan, dimana tidak ada lagging yang berarti operasi berjalan tanpa adanya delay. Penerapan ini juga akan terlihat jika kita melakukan beberapa operasi secara langsung dan dapat langsung melihat hasilnya tanpa perlu memuat ulang laman. AJAX sendiri juga menggunakan asynchronous programming saat memanggil fungsi yang mengecek AJAX berhasil dipanggil atau tidak lalu memberikan sinyalnya ke fungsi tersebut.

## Implementasi checklist
1. Membuat tiga fungsi baru pada views.py yang masing-masingnya diberikan kode untuk autentikasi pengguna.
2. Membuat tiga routing tambahan untuk 3 fungsi yang baru dibuat di views.py tersebut.
3. Mengubah rendering menjadi AJAX, serta melakukan GET ke JSON B yang dilanjut dengan pembuatan card dari data yang dimasukkan.
4. Menyambungkan button create task dengan event onClick untuk menerapkan AJAX.
5. Mengatur ulang task untuk di render kembali ketika ada perubahaan yang dilakukan.
6. Jika tombol Delete di pencet maka laman akan langsung menghilangkan card-nya tanpa perlu reload laman.