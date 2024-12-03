"""Module for managing project (proyek) operations in the system."""
from entities.Proyek import Proyek
from database.db_connector import get_connection

class PengelolaProyek:
    """Class to handle CRUD operations for Proyek entities."""

    def addProyek(self, proyek):
        """Add a new project to the database.

        Args:
            proyek: Proyek object containing project details

        Returns:
            bool: True if successful, False otherwise
        """
        connection = get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            query = '''
                INSERT INTO t_proyek (
                    judulProyek,
                    descProyek,
                    progressProyek,
                    biayaProyek,
                    estimasiBiayaProyek,
                    tanggalMulaiProyek,
                    tanggalSelesaiProyek,
                    statusProyek
                )
            '''
            values = (
                proyek.getJudulProyek(),
                proyek.getDescProyek(),
                proyek.getProgressProyek(),
                proyek.getBiayaProyek(),
                proyek.getEstimasiBiayaProyek(),
                proyek.getTanggalMulaiProyek(),
                proyek.getTanggalSelesaiProyek(),
                proyek.getStatusProyek()
            )
            cursor.execute(query, values)
            connection.commit()
            return True

        except Exception as err:
            print(f"Error creating proyek: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def getAllProyek(self, asc):
        """Retrieve all projects from database.

        Args:
            asc: Boolean for ascending/descending order

        Returns:
            list: List of Proyek objects
        """
        connection = get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor()
            sort_order = 'ASC' if asc else 'DESC'
            query = f"SELECT * FROM t_proyek ORDER BY progressProyek {sort_order}"
            cursor.execute(query)

            proyekArray = []
            for (idProyek, judulProyek, descProyek, progressProyek,
                 biayaProyek, estimasiBiayaProyek, tanggalMulaiProyek,
                 tanggalSelesaiProyek, statusProyek) in cursor:

                proyek = Proyek(
                    idProyek=idProyek,
                    judulProyek=judulProyek,
                    descProyek=descProyek,
                    progressProyek=progressProyek,
                    biayaProyek=biayaProyek,
                    estimasiBiayaProyek=estimasiBiayaProyek,
                    tanggalMulaiProyek=tanggalMulaiProyek,
                    tanggalSelesaiProyek=tanggalSelesaiProyek,
                    statusProyek=statusProyek
                )
                proyekArray.append(proyek)

            return proyekArray

        except Exception as err:
            print(f"Error fetching all proyek: {err}")
            return []

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def getProyekById(self, idProyekInput):
        """Retrieve a project by its ID.

        Args:
            idProyekInput: ID of the project to retrieve

        Returns:
            Proyek: Project object if found, None otherwise
        """
        connection = get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor()
            query = """
                SELECT idProyek, judulProyek, descProyek, progressProyek,
                       biayaProyek, estimasiBiayaProyek, tanggalMulaiProyek,
                       tanggalSelesaiProyek, statusProyek
                FROM t_proyek
                WHERE idProyek = %s
            """
            cursor.execute(query, (idProyekInput,))
            result = cursor.fetchone()

            if not result:
                return None

            (idProyek, judulProyek, descProyek, progressProyek,
             biayaProyek, estimasiBiayaProyek, tanggalMulaiProyek,
             tanggalSelesaiProyek, statusProyek) = result

            return Proyek(
                idProyek=idProyek,
                judulProyek=judulProyek,
                descProyek=descProyek,
                progressProyek=progressProyek,
                biayaProyek=biayaProyek,
                estimasiBiayaProyek=estimasiBiayaProyek,
                tanggalMulaiProyek=tanggalMulaiProyek,
                tanggalSelesaiProyek=tanggalSelesaiProyek,
                statusProyek=statusProyek
            )

        except Exception as err:
            print(f"Error fetching projects: {err}")
            return None

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def deleteProyek(self, idProyekInput):
        """Delete a project from the database.

        Args:
            idProyekInput: ID of the project to delete

        Returns:
            bool: True if successful, False otherwise
        """
        connection = get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            query = "DELETE FROM t_proyek WHERE idProyek = %s"
            cursor.execute(query, (idProyekInput,))
            connection.commit()
            return cursor.rowcount > 0

        except Exception as err:
            print(f"Error deleting proyek: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()

    def editProyek(self, proyekEditted):
        """Update project details in the database.

        Args:
            proyekEditted: Proyek object with updated details

        Returns:
            bool: True if successful, False otherwise
        """
        connection = get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            query = """
                UPDATE t_proyek
                SET judulProyek = %s,
                    descProyek = %s,
                    progressProyek = %s,
                    biayaProyek = %s,
                    estimasiBiayaProyek = %s,
                    tanggalMulaiProyek = %s,
                    tanggalSelesaiProyek = %s,
                    statusProyek = %s
                WHERE idProyek = %s
            """
            values = (
                proyekEditted.getJudulProyek(),
                proyekEditted.getDescProyek(),
                proyekEditted.getProgressProyek(),
                proyekEditted.getBiayaProyek(),
                proyekEditted.getEstimasiBiayaProyek(),
                proyekEditted.getTanggalMulaiProyek(),
                proyekEditted.getTanggalSelesaiProyek(),
                proyekEditted.getStatusProyek(),
                proyekEditted.getIdProyek()
            )
            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount > 0

        except Exception as err:
            print(f"Error updating proyek: {err}")
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()
            connection.close()
