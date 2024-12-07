from ../entities/Biaya import Biaya
from ../database/db_connection import get_connection

class PengelolaBiaya:
    def addBiaya(self, biaya):
        connection = get_connection()
        if not connection:
            print("Failed to get database connection.")
            return False
    
        try:
            cursor = connection.cursor()
            query = '''
                    INSERT INTO t_biaya (
                    namaBarangBiaya,
                    keteranganBiaya,
                    hargaSatuanBiaya,
                    quantityBiaya,
                    totalBiaya
                ) VALUES (?, ?, ?, ?)
            '''

            values = (
                tugas.getJudulTugas(),
                tugas.getDescTugas(),
                tugas.getBiayaTugas(),
                tugas.getStatusTugas(),
            )
            cursor.execute(query, values)
            connection.commit()
            return True
        
        except Exception as err:
            print(f"Error creating biaya: {err}")
            return False
        
        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()
            
    def getAllBiaya(self):
        connection = get_connection()
        if not connection:
            print("Database connection failed.")
            return []
        
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM t_biaya"
            print("Executing query:", query)  # Debugging

            cursor.execute(query)

            biayaArray = []

            for (idBiaya,
                namaBarangBiaya,
                keteranganBiaya,
                hargaSatuanBiaya,
                quantityBiaya,
                totalBiaya,
                idTugasOfBiaya
                ) in cursor:

                biaya = Biaya(
                    namaBarangBiaya = namaBarangBiaya,
                    keteranganBiaya = keteranganBiaya,
                    hargaSatuanBiaya = hargaSatuanBiaya,
                    quantityBiaya = quantityBiaya,
                    totalBiaya = totalBiaya,
                    idTugasOfBiaya = idTugasOfBiaya
                )
                biayaArray.append(biaya)
                print(f"Fetched tugas: {namaBarangBiaya}, {keteranganBiaya}, {hargaSatuanBiaya}, {quantityBiaya}, {totalBiaya}, {idTugasOfBiaya}")

            return biayaArray
        
        except Exception as err:
            print(f"Error fetching all tugas: {err}")
            return []
        
        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()