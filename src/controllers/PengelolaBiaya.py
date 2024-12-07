from entities.Biaya import Biaya
from database.db_connection import get_connection

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

def deleteBiaya(self, idBiayaInput):
        connection = get_connection()
        if not connection:
            print("Failed to get database connection.")
            return False
    
        try:
            cursor = connection.cursor()
            query = "DELETE FROM t_biaya WHERE idBiaya = ?"
            cursor.execute(query, (idBiayaInput,))
            connection.commit()
            return cursor.rowcount > 0
        
        except Exception as err:
            print(f"Error deleting Biaya: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()