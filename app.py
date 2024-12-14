from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Folder untuk menyimpan gambar dan video
output_dir = "captured_media"
os.makedirs(output_dir, exist_ok=True)

@app.route('/')
def index():
    """Halaman utama untuk menangkap video dan foto."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    """Menerima file video atau foto dari browser pengguna."""
    print('Menerima permintaan unggah')
    if 'file' not in request.files:
        print('Tidak ada file yang diunggah')
        return "Tidak ada file yang diunggah", 400

    file = request.files['file']
    if file.filename == '':
        print('Nama file kosong')
        return "Nama file kosong", 400

    # Simpan file dengan nama berdasarkan waktu saat ini
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"{timestamp}_{file.filename}")
    file.save(filename)
    print(f'File berhasil disimpan: {filename}')

    return "File berhasil diunggah", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)