from entities.TugasProyek import TugasProyek
from database.db_connection import get_connection

class PengelolaTugasProyek:
    from entities.TugasProyek import TugasProyek
from database.db_connection import get_connection

class PengelolaTugasProyek:
    def addTugas(self, tugas):
        connection = get_connection()
        if not connection:
            print("Failed to get database connection.")
            return False
    
        try:
            cursor = connection.cursor()
            query = '''
                    INSERT INTO t_tugas (
                    judulTugas,
                    descTugas,
                    biayaTugas,
                    statusTugas
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
            print(f"Error creating tugas: {err}")
            return False
        
        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def getAllTugas(self):
        connection = get_connection()
        if not connection:
            print("Database connection failed.")
            return []
        
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM t_tugas"
            print("Executing query:", query)  # Debugging

            cursor.execute(query)

            tugasArray = []

            for (idTugas,
                judulTugas,
                descTugas,
                biayaTugas,
                statusTugas,
                idProyekOfTugas
                ) in cursor:

                tugas = TugasProyek(
                    idTugas=idTugas,
                    judulTugas=judulTugas,
                    descTugas=descTugas,
                    biayaTugas=biayaTugas,
                    statusTugas=statusTugas,
                    idProyekOfTugas=idProyekOfTugas
                )
                tugasArray.append(tugas)
                print(f"Fetched tugas: {idTugas}, {judulTugas}, {descTugas}, {biayaTugas}, {statusTugas}")

            return tugasArray
        
        except Exception as err:
            print(f"Error fetching all tugas: {err}")
            return []
        
        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def getTugasById(self, idTugasInput):
        connection = get_connection()
        if not connection:
            return None
        
        try :
            cursor = connection.cursor()
            query = """
                    SELECT idTugas,
                        judulTugas,
                        descTugas,
                        biayaTugas,
                        statusTugas
                    FROM t_tugas
                    WHERE idTugas = %s
                    """
            
            cursor.execute(query, (idTugasInput,))
            result = cursor.fetchone()

            if not result:
                return None
            
            (idTugas, judulTugas, descTugas,
            biayaTugas, statusTugas, idProyekOfTugas) = result

            return TugasProyek(
                idTugas=idTugas,
                judulTugas=judulTugas,
                descTugas=descTugas,
                biayaTugas=biayaTugas,
                statusTugas=statusTugas,
                idProyekOfTugas=idProyekOfTugas
            )
        except Exception as err:
            print(f"Error fetching projects: {err}")
            return None

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def deleteTugas(self, idTugasInput):
        connection = get_connection()
        if not connection:
            return False
        
        try:
            cursor = connection.cursor()
            query = "DELETE FROM t_tugas WHERE idTugas = ?"
            cursor.execute(query, (idTugasInput,))
            connection.commit()
            return cursor.rowcount > 0

        except Exception as err:
            print(f"Error deleting proyek: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def editTugas(self, tugasEditted):
        connection = get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            query = """
                UPDATE t_tugas
                SET judulTugas = ?,
                    descTugas = ?,
                    statusTugas = ?
                WHERE idTugas = ?
            """

            values = (
                tugasEditted.getJudulTugas(),
                tugasEditted.getDescTugas(),
                tugasEditted.getStatusTugas(),
                tugasEditted.getIdTugas()
            )
            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount > 0
        
        except Exception as err:
            print(f"Error updating tugas: {err}")
            return False
        
        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()
        
        