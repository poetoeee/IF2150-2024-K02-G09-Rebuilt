class Biaya:
    def __init__(self,  idBiaya = None, namaBarangBiaya = "", keteranganBiaya = "",  hargaSatuanBiaya = None, quantityBiaya = None, totalBiaya = None, idTugasOfBiaya = None):
        self.idBiaya = idBiaya
        self.namaBarangBiaya = namaBarangBiaya
        self.keteranganBiaya = keteranganBiaya
        self.hargaSatuanBiaya = hargaSatuanBiaya
        self.quantityBiaya = quantityBiaya
        self.totalBiaya = totalBiaya
        self.idTugasOfBiaya = idTugasOfBiaya
        
    def getidBiaya(self):
        return self.idBiaya
    
    def setidBiaya(self, idBiaya):
        self.idBiaya = idBiaya

    def getnamaBarangBiaya(self):
        return self.namaBarangBiaya
    
    def setnamaBarangBiaya(self, namaBarangBiaya):
        self.namaBarangBiaya = namaBarangBiaya

    def getketeranganBiaya(self):
        return self.keteranganBiaya
    
    def setketeranganBiaya(self, keteranganBiaya):
        self.keteranganBiaya = keteranganBiaya
    
    def gethargaSatuanBiaya(self):
        return self.hargaSatuanBiaya
    
    def sethargaSatuanBiaya(self, hargaSatuanBiaya):
        self.hargaSatuanBiaya = hargaSatuanBiaya

    def getquantityBiaya(self):
        return self.quantityBiaya
    
    def setquantityBiaya(self, quantityBiaya):
        self.quantityBiaya = quantityBiaya

    def gettotalBiaya(self):
        return self.totalBiaya
    
    def settotalBiaya(self, totalBiaya):
        self.totalBiaya = totalBiaya

    def getidTugasOfBiaya(self):
        return self.idTugasOfBiaya
    
    def setidTugasOfBiaya(self, idTugasOfBiaya):
        self.idTugasOfBiaya = idTugasOfBiaya
    
        
