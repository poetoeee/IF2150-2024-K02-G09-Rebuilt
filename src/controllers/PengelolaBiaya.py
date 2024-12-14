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
                ) VALUES (?, ?, ?, ?, ?)
            '''

            values = (
                biaya.getnamaBarangBiaya(),
                biaya.getketeranganBiaya(),
                biaya.gethargaSatuanBiaya(),
                biaya.getquantityBiaya(),
                biaya.gettotalBiaya()            
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
            print("Executing query:", query)

            cursor.execute(query)
            biayaArray = []

            for (idBiaya, namaBarangBiaya, keteranganBiaya, hargaSatuanBiaya, quantityBiaya, totalBiaya, idTugasOfBiaya) in cursor:
                biaya = Biaya(
                    idBiaya=idBiaya,
                    namaBarangBiaya=namaBarangBiaya,
                    keteranganBiaya=keteranganBiaya,
                    hargaSatuanBiaya=hargaSatuanBiaya,
                    quantityBiaya=quantityBiaya,
                    totalBiaya=totalBiaya,
                    idTugasOfBiaya=idTugasOfBiaya
                )
                biayaArray.append(biaya)
            
            return biayaArray

        except Exception as err:
            print(f"Error fetching all tugas: {err}")
            return []

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

    def editBiaya(self, biayaEditted):
        connection = get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            query = """
                UPDATE t_biaya
                SET namaBarangBiaya = ?,
                    keteranganBiaya = ?,
                    hargaSatuanBiaya = ?,
                    quantityBiaya = ?,
                    totalBiaya = ?
                WHERE idBiaya = ?
            """

            values = (
                biayaEditted.getnamaBarangBiaya(),
                biayaEditted.getketeranganBiaya(),
                biayaEditted.gethargaSatuanBiaya(),
                biayaEditted.getquantityBiaya(),
                biayaEditted.gettotalBiaya(),
                biayaEditted.getidBiaya()
            )
            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount > 0
        
        except Exception as err:
            print(f"Error updating biaya: {err}")
            return False
        
        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()
        

    def getAllBiayaInTugas(self, id_tugas):
        connection = get_connection()
        if not connection:
            print("Database connection failed.")
            return []
        
        try:
            cursor = connection.cursor()
            query = """
                SELECT * FROM t_biaya
                WHERE idTugasOfBiaya = ?
            """
            cursor.execute(query, (id_tugas,))
            
            biayaArray = []
            for row in cursor:
                biaya = Biaya(*row)
                biayaArray.append(biaya)
            
            return biayaArray
        
        except Exception as err:
            print(f"Error fetching biaya for proyek {id_tugas}: {err}")
            return []
        
        finally:
            cursor.close()
            connection.close()