# Skrip Informasi Perangkat Keras

Repositori ini berisi kumpulan skrip untuk mengambil informasi perangkat keras sistem komputer. Skrip-skrip ini ditulis dalam beberapa bahasa pemrograman dan dapat digunakan di berbagai sistem operasi seperti Linux, macOS, dan Windows.

## Daftar Isi

- **Python**: Mengambil informasi tentang CPU, RAM, disk, dan jaringan.
- **Bash**: Skrip shell untuk Linux/macOS yang mengumpulkan informasi perangkat keras.
- **PowerShell**: Skrip Windows untuk mengambil informasi perangkat keras.
- **Go**: Skrip Go untuk informasi perangkat keras menggunakan pustaka pihak ketiga.

## 1. Python

### Persyaratan
- Python 3.x
- Install pustaka `psutil`:
    ```bash
    pip install psutil
    ```

### Skrip: `check.py`

Skrip Python ini mengambil dan menampilkan informasi tentang komponen-komponen berikut:
- CPU: Jumlah core, frekuensi, penggunaan
- RAM: Total, tersedia, digunakan, dan persentase penggunaan
- Disk: Partisi disk, ruang yang digunakan, ruang yang tersedia
- Jaringan: Antarmuka jaringan dan alamat IP

Jalankan skrip dengan:
```bash
python check.py
<br>
<img src="https://raw.githubusercontent.com/Mister-RdanM19/internal_ComputerCHECK/refs/heads/main/ComputerKoe.png">
