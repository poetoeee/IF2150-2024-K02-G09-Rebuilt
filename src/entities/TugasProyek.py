class TugasProyek:
    def __init__(self, idTugas = None, judulTugas = "", descTugas = "", biayaTugas = None, statusTugas = "", idProyekOfTugas = None):

        self.idTugas = idTugas
        self.judulTugas = judulTugas
        self.descTugas = descTugas
        self.biayaTugas = biayaTugas
        self.statusTugas = statusTugas
        self.idProyekOfTugas = idProyekOfTugas

    def getIdTugas(self):
        return self.idTugas
    
    def setIdTugas(self, idTugas):
        self.idTugas = idTugas

    def getJudulTugas(self):
        return self.judulTugas
    
    def setJudulTugas(self, judulTugas):
        self.judulTugas = judulTugas


    def getDescTugas(self):
        return self.descTugas

    def setDescTugas(self, descTugas):
        self.descTugas = descTugas
 
    def getBiayaTugas(self):
        return self.biayaTugas

    def setBiayaTugas(self, biayaTugas):
        self.biayaTugas = biayaTugas

    def getStatusTugas(self):
        return self.statusTugas

    def setStatusTugas(self, statusTugas):
        self.statusTugas = statusTugas

    def getIdProyekOfTugas(self):
        return self.idProyekOfTugas
    
    def setIdProyekOfTugas(self, idProyekOfTugas):
        self.idProyekOfTugas = idProyekOfTugas