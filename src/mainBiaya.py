import ttkbootstrap as tb
from ttkbootstrap.constants import *
from boundaries.DisplayBiayaBintang import DisplayBiaya  # Import the DisplayBiaya UI class
from controllers.PengelolaBiaya import PengelolaBiaya  # Import the Biaya controller
from database.db_connection import get_connection  # Database connection test

# Main Application Class
class MainApplication(tb.Window):
    def __init__(self, themename="darkly"):
        # Initialize ttkbootstrap Window with chosen theme
        super().__init__(themename=themename)
        self.title("Manajemen Proyek - Biaya")
        self.geometry("600x400")
        
        # Initialize the PengelolaBiaya controller
        self.pengelolaBiaya = PengelolaBiaya()
        
        # Header Label
        header = tb.Label(
            self, text="Manajemen Biaya Proyek", 
            font=("Arial", 20, "bold"), bootstyle="info"
        )
        header.pack(pady=20)

        # Buttons for DisplayBiaya functionalities
        button_frame = tb.Frame(self)
        button_frame.pack(pady=20)

        # Button: Add Biaya
        tb.Button(
            button_frame, text="Tambah Biaya", bootstyle="success",
            command=self.open_add_biaya_form
        ).grid(row=0, column=0, padx=10)

        # Button: Edit Biaya (test with dummy data)
        tb.Button(
            button_frame, text="Edit Biaya", bootstyle="warning",
            command=self.open_edit_biaya_form
        ).grid(row=0, column=1, padx=10)

        # Button: Exit
        tb.Button(
            button_frame, text="Keluar", bootstyle="danger",
            command=self.quit
        ).grid(row=0, column=2, padx=10)

        # Footer
        footer = tb.Label(
            self, text="© 2024 Manajemen Proyek - Kelompok 09", 
            font=("Arial", 10), bootstyle="secondary"
        )
        footer.pack(side="bottom", pady=10)

    # Method to open Add Biaya Form
    def open_add_biaya_form(self):
        display_biaya = DisplayBiaya(self, self.pengelolaBiaya)
        display_biaya.popupFormBiaya()

    # Method to open Edit Biaya Form with dummy data
    def open_edit_biaya_form(self):
        from entities.Biaya import Biaya
        # Dummy Biaya data for testing
        dummy_biaya = Biaya(
            idBiaya=1,
            namaBarangBiaya="Besi Beton",
            keteranganBiaya="Material untuk konstruksi",
            hargaSatuanBiaya=50000,
            quantityBiaya=20,
            totalBiaya=1000000
        )
        display_biaya = DisplayBiaya(self, self.pengelolaBiaya)
        display_biaya.popupEditBiaya(dummy_biaya)

# Run the Main Application
if __name__ == "__main__":
    # Check Database Connection
    try:
        connection = get_connection()
        if connection:
            print("Database connected successfully!")
            connection.close()
    except Exception as e:
        print(f"Database connection failed: {e}")

    # Launch the Main Application
    app = MainApplication(themename="darkly")  # Choose theme: darkly, flatly, etc.
    app.mainloop()
