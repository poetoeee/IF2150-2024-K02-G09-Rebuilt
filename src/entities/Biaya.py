class Biaya:
    def __init__(self, biaya_id = None, biaya_nilai = None, proyek_id= None, tugas_id = None):
        self.biaya_id = biaya_id
        self.biaya_nilai = biaya_nilai
        self.proyek_id = proyek_id
        self.tugas_id = tugas_id
        
    def get_biaya_id(self):
        return self.biaya_id
    
    def set_biaya_id(self, biaya_id):
        self.biaya_id = biaya_id

    def get_biaya_nilai(self):
        return self.biaya_nilai
    
    def set_biaya_nilai(self, biaya_nilai):
        self.biaya_nilai = biaya_nilai

    def get_proyek_id(self):
        return self.proyek_id
    
    def set_proyek_id(self, proyek_id):
        self.proyek_id = proyek_id
    
    def get_tugas_id(self):
        return self.tugas_id
    
    def set_tugas_id(self, tugas_id):
        self.tugas_id_id = tugas_id
    
        
