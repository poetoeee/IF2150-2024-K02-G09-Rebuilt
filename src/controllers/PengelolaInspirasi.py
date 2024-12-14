from entities.Inspirasi import Inspirasi
from database.db_connection import get_connection

class PengelolaInspirasi:
    def addInspirasi(self, inspirasi):
        connection = get_connection()
        if not connection:
            print("Failed to get database connection.")
            return False

        try:
            cursor = connection.cursor()
            query = '''
                    INSERT INTO t_inspirasi (
                    judulInspirasi,
                    descInspirasi,
                    imageInspirasi,
                    linkInspirasi
                ) VALUES (?, ?, ?, ?)
            '''

            values = (
                inspirasi.getjudulInspirasi(),
                inspirasi.getdescInspirasi(),
                inspirasi.getimageInspirasi(),
                inspirasi.getlinkInspirasi(),
            )
            cursor.execute(query, values)
            connection.commit()
            return True

        except Exception as err:
            print(f"Error creating inspirasi: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def getAllInspirasi(self):
        connection = get_connection()
        if not connection:
            print("Database connection failed.")
            return []

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM t_inspirasi"
            cursor.execute(query)

            inspirasiArray = []

            for (
                idInspirasi,
                judulInspirasi,
                descInspirasi,
                imageInspirasi,
                linkInspirasi
            ) in cursor:

                inspirasi = Inspirasi(
                    idInspirasi=idInspirasi,
                    judulInspirasi=judulInspirasi,
                    descInspirasi=descInspirasi,
                    imageInspirasi=imageInspirasi,
                    linkInspirasi=linkInspirasi
                )
                inspirasiArray.append(inspirasi)

            return inspirasiArray

        except Exception as err:
            print(f"Error fetching all inspirasi: {err}")
            return []

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def getInspirasiById(self, idInspirasiInput):
        connection = get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor()
            query = """
                    SELECT idInspirasi,
                        judulInspirasi,
                        descInspirasi,
                        imageInspirasi,
                        linkInspirasi
                    FROM t_inspirasi
                    WHERE idInspirasi = ?
                    """

            cursor.execute(query, (idInspirasiInput,))
            result = cursor.fetchone()

            if not result:
                return None

            (
                idInspirasi,
                judulInspirasi,
                descInspirasi,
                imageInspirasi,
                linkInspirasi
            ) = result

            return Inspirasi(
                idInspirasi=idInspirasi,
                judulInspirasi=judulInspirasi,
                descInspirasi=descInspirasi,
                imageInspirasi=imageInspirasi,
                linkInspirasi=linkInspirasi
            )

        except Exception as err:
            print(f"Error fetching inspirasi: {err}")
            return None

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def deleteInspirasi(self, idInspirasiInput):
        connection = get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            query = "DELETE FROM t_inspirasi WHERE idInspirasi = ?"
            cursor.execute(query, (idInspirasiInput,))
            connection.commit()
            return cursor.rowcount > 0

        except Exception as err:
            print(f"Error deleting inspirasi: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def editInspirasi(self, inspirasiEditted):
        connection = get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            query = """
                UPDATE t_inspirasi
                SET judulInspirasi = ?,
                    descInspirasi = ?,
                    imageInspirasi = ?,
                    linkInspirasi = ?
                WHERE idInspirasi = ?
            """

            values = (
                inspirasiEditted.getjudulInspirasi(),
                inspirasiEditted.getdescInspirasi(),
                inspirasiEditted.getimageInspirasi(),
                inspirasiEditted.getlinkInspirasi(),
                inspirasiEditted.getIdInspirasi()
            )
            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount > 0

        except Exception as err:
            print(f"Error updating inspirasi: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()