class TugasProyek:
    def __init__(self, idTugas = None, judulTugas = "", descTugas = "", biayaTugas = None, statusProyek = ""):
        self.idTugas = idTugas
        self.judulTugas = judulTugas
        self.descTugas = descTugas
        self.biayaTugas = biayaTugas
        self.statusProyek = statusProyek
        

    def get_idTugas(self):
        return self.idTugas
    
    def set_tugas_id(self,idTugas):
        self.idTugas = idTugas

    def get_tugas_nama(self):
        return self.get_tugas_nama
        
    def set_judulTugas(self, judulTugas):
        self.judulTugas= judulTugas

    def get_descTugas(self):
        return self.descTugas

    def set_descTugas(self,descTugas):
        self.descTugas = descTugas

    def get_biayaTugas(self):
        return self.biayaTugas

    def set_biayaTugas(self, biayaTugas):
        self.biayaTugas = biayaTugas

    def get_statusProyek(self):
        return self.statusProyek

    def set_statusProyek(self, statusProyek):
        self.statusProyek = statusProyek

