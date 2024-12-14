class Proyek:
    def __init__(self, idProyek=None, judulProyek="", descProyek="", progressProyek="", biayaProyek=None, estimasiBiayaProyek=None, tanggalMulaiProyek=None, tanggalSelesaiProyek=None, statusProyek="Not Started"):
        self.idProyek = idProyek
        self.judulProyek = judulProyek
        self.descProyek = descProyek
        self.progressProyek = progressProyek
        self.biayaProyek = biayaProyek
        self.estimasiBiayaProyek = estimasiBiayaProyek
        self.tanggalMulaiProyek = tanggalMulaiProyek
        self.tanggalSelesaiProyek = tanggalSelesaiProyek
        self.statusProyek = statusProyek
        
    def get_idProyek(self):
        return self.idProyek

    def set_idProyek(self, idProyek):
        self.idProyek = idProyek

    def get_judulProyek(self):
        return self.judulProyek

    def set_judulProyek(self, judulProyek):
        self.judulProyek = judulProyek
        
    def get_descProyek(self):
        return self.descProyek

    def set_descProyek(self, descProyek):
        self.descProyek = descProyek

    def get_progressProyek(self):
        return self.progressProyek

    def set_progressProyek(self, progressProyek):
        self.progressProyek = progressProyek
        
    def get_biayaProyek(self):
        return self.biayaProyek

    def set_biayaProyek(self, biayaProyek):
        self.biayaProyek = biayaProyek
        
    def get_estimasiBiayaProyek(self):
        return self.estimasiBiayaProyek

    def set_estimasiBiayaProyek(self, estimasiBiayaProyek):  # Fixed method name
        self.estimasiBiayaProyek = estimasiBiayaProyek

    def get_tanggalMulaiProyek(self):
        return self.tanggalMulaiProyek

    def set_tanggalMulaiProyek(self, tanggalMulaiProyek):
        self.tanggalMulaiProyek = tanggalMulaiProyek
        
    def get_tanggalSelesaiProyek(self):
        return self.tanggalSelesaiProyek

    def set_tanggalSelesaiProyek(self, tanggalSelesaiProyek):
        self.tanggalSelesaiProyek = tanggalSelesaiProyek
        
    def get_statusProyek(self):
        return self.statusProyek

    def set_statusProyek(self, statusProyek):
        self.statusProyek = statusProyek