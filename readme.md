# Alat Perekaman Video dan Foto

Proyek ini adalah aplikasi web berbasis Flask yang memungkinkan pengguna untuk mengambil foto dan video langsung dari browser. Media yang direkam akan otomatis diunggah ke server dan disimpan di folder yang telah ditentukan.

## Fitur

- **Perekaman Media di Browser**: Pengguna dapat mengakses aplikasi ini melalui browser untuk mengambil foto dan video.
- **Unggah Otomatis**: File media yang diambil akan diunggah secara otomatis ke server.
- **Penyimpanan dengan Timestamp**: File disimpan dengan nama unik berdasarkan waktu saat pengambilan.
- **Antarmuka Sederhana**: Aplikasi ini menyediakan antarmuka yang bersih dan mudah digunakan.

## Prasyarat

- Python 3.7 atau versi lebih baru
- Flask

## Instalasi

1. **Klon Repository**:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Instal Dependensi**:

   ```bash
   pip install flask
   ```

3. **Atur Direktori**: Aplikasi akan secara otomatis membuat folder bernama `captured_media` untuk menyimpan file media yang diunggah.

## Penggunaan

1. **Jalankan Server Flask**:

   ```bash
   python app.py
   ```

2. **Akses Aplikasi**: Buka browser dan navigasikan ke `http://<server_ip>:5000/`.

3. **Izinkan Akses Kamera**: Berikan izin kepada aplikasi untuk mengakses kamera ketika diminta.

4. **Ambil Media**:

   - Klik tombol untuk mulai memindai atau merekam.
   - Foto dan video yang direkam akan diunggah ke server.

5. **Akses Media yang Tersimpan**: File yang direkam disimpan di folder `captured_media` pada server.

## Struktur Proyek

```
<repository_folder>/
├── app.py              # Aplikasi utama Flask
├── templates/
│   └── index.html      # File HTML untuk antarmuka pengguna
├── static/             # (Opsional) Direktori untuk file statis
└── captured_media/     # Direktori untuk menyimpan media yang diunggah
```

## Cara Kerja

1. Server menyajikan halaman HTML (`index.html`) yang:

   - Meminta izin akses kamera.
   - Menampilkan aliran video dari kamera ke browser.
   - Mengambil foto/video dan mengunggahnya ke server.

2. Backend Flask:

   - Menerima file media yang diunggah melalui endpoint `/upload`.
   - Menyimpan file tersebut di folder `captured_media` dengan nama file yang dilengkapi timestamp.

## Kustomisasi

- **Ubah Lokasi Penyimpanan**: Perbarui variabel `output_dir` di `app.py` untuk mengubah lokasi penyimpanan file.

- **Tingkatkan Antarmuka**: Kustomisasi file `index.html` untuk mengubah tampilan atau menambahkan fitur tambahan.

## Menjadikan Server Flask Publik dengan Ngrok

Jika ingin mengakses aplikasi ini dari jaringan luar, Anda bisa menggunakan Ngrok:

1. **Instal Ngrok**: Unduh dan instal Ngrok dari [https://ngrok.com/download](https://ngrok.com/download).

2. **Jalankan Ngrok**:

   ```bash
   ngrok http 5000
   ```

3. **Dapatkan URL Publik**: Ngrok akan memberikan URL publik (misalnya, `https://abc123.ngrok.io`). Gunakan URL tersebut untuk mengakses aplikasi dari perangkat lain.

4. **Keamanan Tambahan**: Jika aplikasi ini digunakan dalam lingkungan produksi, pastikan untuk menambahkan autentikasi atau langkah keamanan lainnya.

## Kontribusi

Silakan fork repository ini dan kirimkan pull request untuk fitur baru, perbaikan bug, atau peningkatan lainnya.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file LICENSE untuk detailnya.

## Penghargaan

- [QuaggaJS](https://github.com/serratus/quaggaJS) untuk pemindaian barcode (jika digunakan).
- Komunitas Flask untuk framework web Python yang andal.

