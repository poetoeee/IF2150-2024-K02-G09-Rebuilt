from entities.Proyek import Proyek
from database.db_connection import get_connection
from datetime import datetime
from controllers.PengelolaTugasProyek import PengelolaTugasProyek
from controllers.PengelolaBiaya import PengelolaBiaya


class PengelolaProyek:
    """Class to handle CRUD operations for Proyek entities."""

    def __init__(self):
        self.tugas_manager = PengelolaTugasProyek()  # Initialize the tugas manager
        self.biaya_manager = PengelolaBiaya()

    def addProyek(self, proyek):
        """Add a new project to the database."""
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

    # def getAllProyek(self, sort_by="progressProyek", asc=True):
    #     """Retrieve all projects from database with dynamic sorting."""
    #     connection = get_connection()
    #     if not connection:
    #         return []

    #     try:
    #         cursor = connection.cursor()

    #         # Validate and sanitize the sort_by input
    #         valid_sort_columns = ["idProyek", "progressProyek"]
    #         if sort_by not in valid_sort_columns:
    #             sort_by = "progressProyek"

    #         sort_order = 'ASC' if asc else 'DESC'
    #         query = f"SELECT * FROM t_proyek ORDER BY {sort_by} {sort_order}"
    #         cursor.execute(query)

    #         proyekArray = []
    #         for (idProyek, judulProyek, descProyek, progressProyek,
    #             biayaProyek, estimasiBiayaProyek, tanggalMulaiProyek,
    #             tanggalSelesaiProyek, statusProyek) in cursor.fetchall():

    #             # Fetch tasks for the project and calculate progress
    #             tugas_list = self.tugas_manager.getAllTugas(idProyek)
    #             if tugas_list:
    #                 total_tugas = len(tugas_list)
    #                 done_tugas = sum(1 for tugas in tugas_list if tugas.getStatusTugas().lower() == "done")
    #                 calculated_progress = int((done_tugas / total_tugas) * 100)
    #             else:
    #                 calculated_progress = 0  # No tasks, so no progress

    #             proyek = Proyek(
    #                 idProyek=idProyek,
    #                 judulProyek=judulProyek,
    #                 descProyek=descProyek,
    #                 progressProyek=calculated_progress,  # Use the calculated progress
    #                 biayaProyek=biayaProyek,
    #                 estimasiBiayaProyek=estimasiBiayaProyek,
    #                 tanggalMulaiProyek=tanggalMulaiProyek,
    #                 tanggalSelesaiProyek=tanggalSelesaiProyek,
    #                 statusProyek=statusProyek
    #             )
    #             proyekArray.append(proyek)

    #         return proyekArray

    #     except Exception as err:
    #         print(f"Error fetching all proyek: {err}")
    #         return []

    #     finally:
    #         if 'cursor' in locals():
    #             cursor.close()
    #         connection.close()

    def getAllProyek(self, sort_by="progressProyek", asc=True):
        """Retrieve all projects and sort in Python."""
        connection = get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM t_proyek"
            cursor.execute(query)

            proyekArray = []
            for (idProyek, judulProyek, descProyek, progressProyek,
                biayaProyek, estimasiBiayaProyek, tanggalMulaiProyek,
                tanggalSelesaiProyek, statusProyek) in cursor.fetchall():

                # Fetch tasks for the project and calculate progress
                tugas_list = self.tugas_manager.getAllTugas(idProyek)
                if tugas_list:
                    total_tugas = len(tugas_list)
                    done_tugas = sum(1 for tugas in tugas_list if tugas.getStatusTugas().lower() == "done")
                    calculated_progress = int((done_tugas / total_tugas) * 100)
                else:
                    calculated_progress = 0  # No tasks, so no progress

                proyek = Proyek(
                    idProyek=idProyek,
                    judulProyek=judulProyek,
                    descProyek=descProyek,
                    progressProyek=calculated_progress,  # Use the calculated progress
                    biayaProyek=biayaProyek,
                    estimasiBiayaProyek=estimasiBiayaProyek,
                    tanggalMulaiProyek=tanggalMulaiProyek,
                    tanggalSelesaiProyek=tanggalSelesaiProyek,
                    statusProyek=statusProyek
                )
                proyekArray.append(proyek)

            # Perform sorting in Python
            reverse = not asc
            if sort_by == "progressProyek":
                proyekArray.sort(key=lambda x: x.progressProyek, reverse=reverse)
            elif sort_by == "idProyek":
                proyekArray.sort(key=lambda x: x.idProyek, reverse=reverse)

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

    def getTugasStatusCounts(self, idProyek):
        # Fetch all tugas for the given project
        tugasList = self.tugas_manager.getAllTugas(idProyek)

        # if not tugasList:
        #     print("No tugas found for the given project.")
        #     return {"done": 0, "on_progress": 0}

        # Initialize counters
        done_count = 0
        on_progress_count = 0

        # Iterate through the list and count statuses
        for tugas in tugasList:
            status = tugas.statusTugas.lower()
            if status == "done":
                done_count += 1
            elif status == "on progress":  # Adjust the string if needed
                on_progress_count += 1

        # Return the counts
        return [done_count, on_progress_count]
    
    def getSumBiaya(self, idProyek):
        # Fetch all tugas for the given project
        tugasList = self.tugas_manager.getAllTugas(idProyek)

        sum = 0
        for tugas in tugasList:
            sum += tugas.biayaTugas

        return sum
    
    def getRealBiaya(self, idProyek):
        tugasList = self.tugas_manager.getAllTugas(idProyek)

        sum = 0
        for tugas in tugasList:
            sum += self.biaya_manager.getTotalBiayaByTugasId(tugas.idTugas)

        return sum

            

