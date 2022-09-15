Nama : Marc Salvadore Silitonga
NPM  : 2106705543
Link aplikasi Heroku : https://tugas2django.herokuapp.com/katalog/

Bagan Penjelasan


Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Penggunaan virtual environtment ditujukan untuk memastikkan library di suatu project tidak berubah apabila kita melakukan perubahaan pada library tersebut. Jika kita tidak menggunakan virtual environtment, maka jika kita melakukan perubahaan pada library untuk sebuah project baru, project lama akan mengalami eror karena library-nya tidak sesuai.
Kita tidak bisa membuat aplikasi berbasis django tanpa menggunakan virtual environtment, karena jika django melakukan pembaharuan, versi baru tersebut akan tidak cocok dengan aplikasi atau program kita sehingga terjadi eror. Kita harus membalikan ke versi sebelumnya agar aplikasi dapat kembali berjalan.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Pengambilan data dari model dan mengembalikannya ke dalam bentuk HTML, saya lakukan dengan membuat fungsi def yang menerima parameter request. Fungsi ini akan memasukkan request serta data barang yang akan di tampilkan dengan mengambil seluruh objek dari class CatalogItem dengan mengimport class moduls dari katalog dan memasukkannya ke dalam katalog html menggunakan import render, sehingga fungsi def tersebut akan me-return render(parameter, html, model data).
2. Routing dengan mengedit urls.py pada folder katalog dan folder project_django. Pada folder katalog, saya menggunakan modul dari django untuk mengaplikasikan output pada urls atau app yang dibuat dan katalog untuk memakai fungsi yang ada. Dari modul django saya menggunakan fungsi path untuk memberikan output dari katalog yang sudah dibuat. Katalog tersebut saya dapatkan dari class views dan mengambil fungsi show_katalog yang sudah dibuat pada tahap pertama. Pada folder project_django saya menambahkan path yang akan diisi oleh urls katalog tersebut.
3. Memetakan data dapat dilakukan menggunakan fungsi views.py yang memberikan query ke database berdasarkan model dari CatalogItem, kemudian mengasiggnya dengan variabel context yang nantinya akan dimunculkan oleh Django pada laman HTML.
4. Deployment dilakukan dengan membuat aplikasi terlebih dahulu pada Heroku, kemudian memasukkan APP NAME dan API KEY pada repository secret yang digunakan. Setelah tahap tersebut berhasil, Github akan terhubung dengan Heroku dan berhasil mendeploy aplikasi katalog.