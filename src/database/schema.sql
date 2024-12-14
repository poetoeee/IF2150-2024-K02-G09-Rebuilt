CREATE TABLE IF NOT EXISTS t_proyek (
    idProyek INTEGER PRIMARY KEY AUTOINCREMENT,
    judulProyek VARCHAR(40),
    descProyek TEXT,
    progressProyek FLOAT,
    biayaProyek INT,
    estimasiBiayaProyek INT,
    tanggalMulaiProyek DATE,
    tanggalSelesaiProyek DATE,
    statusProyek VARCHAR(15)
);


CREATE TABLE IF NOT EXISTS t_tugas (
    idTugas INTEGER PRIMARY KEY AUTOINCREMENT,
    judulTugas VARCHAR(40),
    descTugas TEXT,
    biayaTugas INT,
    statusTugas VARCHAR(15),
    idProyekOfTugas INTEGER, 
    CONSTRAINT fk_idProyekOfTugas FOREIGN KEY (idProyekOfTugas) REFERENCES t_proyek(idProyek)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS t_biaya (
    idBiaya INTEGER PRIMARY KEY AUTOINCREMENT,
    namaBarangBiaya TEXT,
    keteranganBiaya TEXT,
    hargaSatuanBiaya INT,
    quantityBiaya INT,
    totalBiaya INT,
    idTugasOfBiaya INTEGER, 
    CONSTRAINT fk_idTugasOfBiaya FOREIGN KEY (idTugasOfBiaya) REFERENCES t_tugas(idTugas)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS t_inspirasi (
    idInspirasi INTEGER PRIMARY KEY AUTOINCREMENT,
    judulInspirasi TEXT,
    descInspirasi TEXT,
    imageInspirasi TEXT,
    linkInspirasi TEXT
);

-- Menambahkan data awal ke tabel t_biaya
INSERT INTO t_biaya (namaBarangBiaya, keteranganBiaya, hargaSatuanBiaya, quantityBiaya, totalBiaya, idTugasOfBiaya) 
VALUES 
('Kertas A4', 'Pembelian kertas A4 untuk dokumentasi', 50000, 10, 500000, 1),
('Pulpen', 'Pembelian pulpen untuk kebutuhan kantor', 2000, 50, 100000, 1),
('Printer', 'Pembelian printer untuk kebutuhan cetak', 1500000, 1, 1500000, 2),
('Meja Kerja', 'Pembelian meja kerja tambahan', 500000, 2, 1000000, 2),
('Laptop', 'Pembelian laptop untuk pekerja proyek', 7500000, 1, 7500000, 3);
