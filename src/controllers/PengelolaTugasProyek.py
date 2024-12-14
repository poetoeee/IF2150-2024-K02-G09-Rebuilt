from entities.TugasProyek import TugasProyek
from database.db_connection import get_connection

class PengelolaTugasProyek:
    from entities.TugasProyek import TugasProyek
from database.db_connection import get_connection

class PengelolaTugasProyek:
    def addTugas(self, tugas, idProyek):
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
                        statusTugas,
                        idProyekOfTugas
                    ) VALUES (?, ?, ?, ?, ?)
            '''

            values = (
                tugas.getJudulTugas(),
                tugas.getDescTugas(),
                tugas.getBiayaTugas(),
                tugas.getStatusTugas(),
                idProyek,
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


    def getAllTugas(self, idProyek):
        # Validate idProyek input
        if idProyek is None or not isinstance(idProyek, int):
            print("Invalid idProyek provided.")
            return []

        # Establish database connection
        connection = get_connection()
        if not connection:
            print("Database connection failed.")
            return []

        try:
            cursor = connection.cursor()
            query = """
                SELECT idTugas, judulTugas, descTugas, biayaTugas, statusTugas, idProyekOfTugas
                FROM t_tugas
                WHERE idProyekOfTugas = ?
            """
            print("Executing query:", query, "with idProyekOfTugas =", idProyek)

            # Execute the query with idProyek as a parameter
            cursor.execute(query, (idProyek,))

            result = cursor.fetchall()
            print(f"Number of tugas: {len(result)}")

            tugasArray = []

            # Fetch all results from the query
            for row in result:
                (
                idTugas,
                judulTugas,
                descTugas,
                biayaTugas,
                statusTugas,
                idProyekOfTugas
                ) = row
                # Create a TugasProyek object for each record
                tugas = TugasProyek(
                    idTugas=idTugas,
                    judulTugas=judulTugas,
                    descTugas=descTugas,
                    biayaTugas=biayaTugas,
                    statusTugas=statusTugas,
                    idProyekOfTugas=idProyekOfTugas
                )
                tugasArray.append(tugas)
                print(f"Fetched Tugas: {idTugas}, {judulTugas}, {descTugas}, {biayaTugas}, {statusTugas}, {idProyekOfTugas}")

            return tugasArray

        except Exception as err:
            print(f"Error fetching tugas by idProyek: {err}")
            return []

        finally:
            # Ensure resources are cleaned up properly
            if "cursor" in locals():
                cursor.close()
            if connection:
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
                        statusTugas,
                        idProyekOfTugas
                    FROM t_tugas
                    WHERE idTugas = ?
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
            print(f"Error fetching tugas: {err}")
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
        
        