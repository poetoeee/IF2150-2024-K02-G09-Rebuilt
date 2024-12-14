"""Module for managing project (proyek) operations in the system."""
from entities.Proyek import Proyek
from database.db_connection import get_connection
from datetime import datetime


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
            print("Failed to get database connection.")
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
                    statusProyek
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            values = (
                proyek.get_judulProyek(),
                proyek.get_descProyek(),
                proyek.get_progressProyek() or 0,
                proyek.get_biayaProyek() or 0,
                proyek.get_estimasiBiayaProyek() or 0,
                proyek.get_tanggalMulaiProyek(),
                proyek.get_statusProyek() or "On Progress"
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
                 tanggalSelesaiProyek, statusProyek) in cursor.fetchall():

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
                WHERE idProyek = ?
            """
            cursor.execute(query, (idProyekInput,))
            result = cursor.fetchone()

            if not result:
                return None

            (idProyek, judulProyek, descProyek, progressProyek,
            biayaProyek, estimasiBiayaProyek, tanggalMulaiProyek,
            tanggalSelesaiProyek, statusProyek) = result

            # Periksa dan konversi tanggal dengan waktu jika ada
            def parse_date(date_string):
                if not date_string:
                    return None
                try:
                    return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    return datetime.strptime(date_string, "%Y-%m-%d")

            tanggalMulaiProyek = parse_date(tanggalMulaiProyek)
            tanggalSelesaiProyek = parse_date(tanggalSelesaiProyek)

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
            query = "DELETE FROM t_proyek WHERE idProyek = ?"
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
                SET judulProyek = ?,
                    descProyek = ?,
                    progressProyek = ?,
                    biayaProyek = ?,
                    estimasiBiayaProyek = ?,
                    tanggalMulaiProyek = ?,
                    tanggalSelesaiProyek = ?,
                    statusProyek = ?
                WHERE idProyek = ?
            """
            
            # Pastikan tanggalMulaiProyek dan tanggalSelesaiProyek diformat dengan benar
            tanggalMulaiProyek = (
                proyekEditted.get_tanggalMulaiProyek().strftime('%Y-%m-%d %H:%M:%S')
                if proyekEditted.get_tanggalMulaiProyek() else None
            )
            tanggalSelesaiProyek = (
                proyekEditted.get_tanggalSelesaiProyek().strftime('%Y-%m-%d %H:%M:%S')
                if proyekEditted.get_tanggalSelesaiProyek() else None
            )

            values = (
                proyekEditted.get_judulProyek(),
                proyekEditted.get_descProyek(),
                proyekEditted.get_progressProyek(),
                proyekEditted.get_biayaProyek(),
                proyekEditted.get_estimasiBiayaProyek(),
                tanggalMulaiProyek,
                tanggalSelesaiProyek,
                proyekEditted.get_statusProyek(),
                proyekEditted.get_idProyek()
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
