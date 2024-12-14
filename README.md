# IF2110 - Algoritma dan Struktur Data 2024
> Tugas Besar - IF2150 Rekayasa Perangkat Lunak 2024

## Kelompok 09
## Kelas K02

## Contributors
<div align="center">

| **NIM**  | **Nama**                       |
|----------|--------------------------------|
| 13523011 | Noumisyifa Nabila Nareswari    |
| 13523038 | Abrar Abhirama Widyadhana      |
| 13523080 | Diyah Susan Nugrahani          |
| 13523096 | Muhammad Edo Raduputu Aprima   |
| 13523106 | Athian Nugraha Muarajuang      |

</div>


## Penjelasan Singkat
Rebuilt adalah aplikasi desktop berbasis python untuk membuat perencanaan dan pengelolaan proyek-proyek renovasi rumah. 

## Cara Menjalankan Program
1. Install release repository dan unzip
2. Buka terminal dan ganti direktori ke tempat folder aplikasi berada
    ```sh
    cd /path/to/folder
    ```
3. Masuk ke virtual environment
    ```sh
    pip install virtualenv
    python -m venv .venv
    ./.venv/Scripts/activate
    ```
4. Install library dalam requirements.txt
    ```sh
    pip install -r requirements.txt
    ```
5. Run program python
    ```sh
    python src/main.py
    ```




## Daftar Modul yang Diimplementasi

### 1. Modul Entity
- **`Proyek`**: Modul ini mengelola data proyek dalam sistem, termasuk atribut seperti nama proyek, deskripsi, dan status.
- **`Tugas`**: Modul ini mengelola data tugas dalam proyek, mencakup nama tugas, deskripsi, deadline, dan status tugas.
- **`Biaya`**: Modul ini mengelola data biaya yang terkait dengan tugas atau proyek, termasuk nama barang, harga satuan, kuantitas, total biaya, dan keterangan.

### 2. Modul Boundary
- **`Boundary Controller Proyek`**: Menyediakan antarmuka antara UI dan sistem untuk entitas proyek. Mengelola tampilan dan interaksi untuk data proyek.
- **`Boundary Controller Tugas`**: Menyediakan antarmuka antara UI dan sistem untuk entitas tugas. Mengelola tampilan dan interaksi untuk data tugas.
- **`Boundary Controller Biaya`**: Menyediakan antarmuka antara UI dan sistem untuk entitas biaya. Mengelola tampilan dan interaksi untuk data biaya.

### 3. Modul Controller
- **`Pengelola Proyek`**: Menangani logika bisnis dan operasi terkait proyek, termasuk menambah, mengedit, dan menghapus data proyek.
- **`Pengelola Tugas`**: Menangani logika bisnis dan operasi terkait tugas, termasuk menambah, mengedit, dan menghapus data tugas.
- **`Pengelola Biaya`**: Menangani logika bisnis dan operasi terkait biaya, termasuk menambah, mengedit, dan menghapus biaya terkait dengan proyek atau tugas.

---

## Pembagian Tugas

| **Nama Modul**                  | **Tugas**                | **Nama Anggota** |
|----------------------------------|--------------------------|------------------|
| **Modul Inspirasi**              | Full Inspiration         | Muhammad Edo Raduputu Aprima            |
| **Modul Entity Proyek**          | Membuat entity proyek    | Athian Nugraha Muarajuang         |
| **Modul Entity Tugas**           | Membuat entity tugas     | Abrar Abhirama Widyadhana            |
| **Modul Boundary Controller Proyek** | Membuat boundary controller proyek | Noumisyifa Nabila Nareswari     |
| **Modul Boundary Controller Tugas**  | Membuat boundary controller tugas | Diyah Susan Nugrahani    |
| **Modul Entity Boundary Controller Biaya** | Membuat entity dan boundary controller biaya | Athian Nugraha Muarajuang, Abrar Abhirama Widyadhana|

---


## Daftar Tabel Basis Data

| **Nama Tabel**  | **Deskripsi**                                    | **Atribut**                                                                                      |
|-----------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **`biaya`**     | Tabel yang menyimpan data terkait biaya.         | - idBiaya (Primary Key) <br> - namaBarangBiaya <br> - hargaSatuanBiaya <br> - quantityBiaya <br> - totalBiaya <br> - keteranganBiaya |
| **`tugas`**     | Tabel yang menyimpan informasi tugas atau proyek.| - idTugas (Primary Key) <br> - namaTugas <br> - deskripsiTugas <br> - tanggalMulai <br> - tanggalSelesai <br> - statusTugas |
| **`user`**      | Tabel yang menyimpan data pengguna.              | - idUser (Primary Key) <br> - namaUser <br> - emailUser <br> - passwordUser <br> - roleUser |
| **`log_activity`** | Tabel yang menyimpan aktivitas atau riwayat log. | - idLog (Primary Key) <br> - idUser (Foreign Key) <br> - aktivitas <br> - waktu |
