class Biaya:
    def __init__(self,  idBiaya = None, namaBarangBiaya = "", keteranganBiaya = "",  hargaSatuanBiaya = None, quantityBiaya = None, totalBiaya = None):
        self.idBiaya = idBiaya
        self.namaBarangBiaya = namaBarangBiaya
        self.keteranganBiaya = keteranganBiaya
        self.hargaSatuanBiaya = hargaSatuanBiaya
        self.quantityBiaya = quantityBiaya
        self.totalBiaya = totalBiaya
        self.idTugasOfBiaya= totalBiaya
        
    def get_idBiaya(self):
        return self.idBiaya
    
    def set_idBiaya(self, idBiaya):
        self.idBiaya = idBiaya

    def get_namaBarangBiaya(self):
        return self.namaBarangBiaya
    
    def set_namaBarangBiaya(self, namaBarangBiaya):
        self.namaBarangBiaya = namaBarangBiaya

    def get_keteranganBiaya(self):
        return self.keteranganBiaya
    
    def set_keteranganBiaya(self, keteranganBiaya):
        self.keteranganBiaya = keteranganBiaya
    
    def get_hargaSatuanBiaya(self):
        return self.hargaSatuanBiaya
    
    def set_hargaSatuanBiaya(self, hargaSatuanBiaya):
        self.hargaSatuanBiaya = hargaSatuanBiaya

    def get_quantityBiaya(self):
        return self.quantityBiaya
    
    def set_quantityBiaya(self, quantityBiaya):
        self.quantityBiaya = quantityBiaya

    def get_totalBiaya(self):
        return self.totalBiaya
    
    def set_totalBiaya(self, totalBiaya):
        self.totalBiaya = totalBiaya

    def get_idTugasOfBiaya(self):
        return self.idTugasOfBiaya
    
    def set_totalBiaya(self, totalBiaya):
        self.idTugasOfBiaya = idTugasOfBiaya
    
        
