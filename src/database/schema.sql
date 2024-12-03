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
    statusProyek VARCHAR(15),
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