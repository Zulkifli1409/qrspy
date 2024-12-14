# Alat Perekaman Foto QrSpy

QrSpy adalah aplikasi web berbasis Flask yang memungkinkan pengguna untuk mengambil foto langsung dari browser setiap detik. Foto yang diambil akan otomatis diunggah ke server dan disimpan di folder yang telah ditentukan. Dengan antarmuka yang bersih dan mudah digunakan, QrSpy menyediakan solusi yang efisien untuk perekaman foto secara real-time.

## Fitur

- 📸 **Perekaman Foto Setiap Detik**: Pengguna dapat mengakses aplikasi ini melalui browser untuk mengambil foto setiap detik.
- 🚀 **Unggah Otomatis**: Foto yang diambil akan diunggah secara otomatis ke server.
- 📁 **Penyimpanan dengan Timestamp**: Foto disimpan dengan nama unik berdasarkan waktu saat pengambilan.
- 🌟 **Antarmuka Sederhana**: Aplikasi ini menyediakan antarmuka yang bersih dan mudah digunakan.

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

3. **Atur Direktori**: Aplikasi akan secara otomatis membuat folder bernama `captured_media` untuk menyimpan foto yang diunggah.

## Penggunaan

1. **Jalankan Server Flask**:

   ```bash
   python app.py
   ```

2. **Akses Aplikasi**: Buka browser dan navigasikan ke [http://<server_ip>:5000/](http://<server_ip>:5000/).

3. **Izinkan Akses Kamera**: Berikan izin kepada aplikasi untuk mengakses kamera ketika diminta.

4. **Ambil Foto Setiap Detik**:

   - Foto akan diambil secara otomatis setiap detik.
   - Foto yang direkam akan diunggah ke server.

5. **Akses Foto yang Tersimpan**: Foto yang diambil disimpan di folder `captured_media` pada server.

## Struktur Proyek

```
<repository_folder>/
├── app.py              # Aplikasi utama Flask
├── templates/
│   └── index.html      # File HTML untuk antarmuka pengguna
├── static/             # (Opsional) Direktori untuk file statis
└── captured_media/     # Direktori untuk menyimpan foto yang diunggah
```

## Cara Kerja

1. Server menyajikan halaman HTML (`index.html`) yang:
   - Meminta izin akses kamera.
   - Menampilkan aliran video dari kamera ke browser.
   - Mengambil foto setiap detik dan mengunggahnya ke server.

2. Backend Flask:
   - Menerima file foto yang diunggah melalui endpoint `/upload`.
   - Menyimpan foto tersebut di folder `captured_media` dengan nama file yang dilengkapi timestamp.

## Kustomisasi

- **Ubah Lokasi Penyimpanan**: Perbarui variabel `output_dir` di `app.py` untuk mengubah lokasi penyimpanan foto.

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

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file LICENSE untuk detailnya.

---
