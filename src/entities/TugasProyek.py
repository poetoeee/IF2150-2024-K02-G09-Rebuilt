class TugasProyek:
    def __init__(self, tugas_id = None, tugas_nama = "", tugas_deskripsi = "", tugas_status = "Not Started", proyek_id = None):
        self.tugas_id = tugas_id
        self.tugas_nama = tugas_nama
        self.tugas_deskripsi = tugas_deskripsi
        self.tugas_status = tugas_status
        self.proyek_id = proyek_id
        

    def get_tugas_id(self):
        return self.tugas_id
    
    def set_tugas_id(self, tugas_id):
        self.tugas_id = tugas_id

    def get_tugas_nama(self):
        return self.get_tugas_nama
        
    def set_tugas_nama(self, tugas_nama):
        self.tugas_nama = tugas_nama

    def get_tugas_deskripsi(self):
        return self.tugas_deskripsi

    def set_tugas_deskripsi(self, tugas_deskripsi):
        self.tugas_deskripsi = tugas_deskripsi

    def get_tugas_status(self):
        return self.tugas_status 

    def set_tugas_status(self,tugas_status):
        self.tugas_status = tugas_status

    def get_proyek_id(self):
        return self.proyek_id

    def set_proyek_id(self, proyek_id):
        self.proyek_id = proyek_id

