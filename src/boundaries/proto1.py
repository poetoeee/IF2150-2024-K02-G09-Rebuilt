import tkinter as tk
import customtkinter as ctk
from controllers.PengelolaBiaya import PengelolaBiaya
# from ..entities.Biaya import Biaya
from boundaries.DPBEdit import DisplayPopEdit

class ProjectUI:
    def __init__(self, root):
        ctk.set_appearance_mode("light")  # Mode 'light' atau 'dark'
        ctk.set_default_color_theme("blue")  # Warna tema: blue, green, dark-blue

        self.root = root
        self.root.title("Tugas and Biaya Management")
        self.root.geometry("1024x768")

        # Tugas Frame - Top Section
        self.create_tugas_frame()

        # Biaya Frame with Sub-Frames
        self.create_biaya_section()

    def create_tugas_frame(self):
        """Creates the top 'Tugas' section occupying 40% of the window."""
        tugas_frame = ctk.CTkFrame(self.root, corner_radius=10)
        tugas_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.4, anchor="n")

        ctk.CTkLabel(
            tugas_frame, text="[Tugas Name]", font=("Helvetica", 18, "bold"), text_color="blue"
        ).pack(side="left", padx=10, pady=10)

    def create_biaya_section(self):
        """Creates the 'Biaya' section divided into 3 frames."""
        biaya_frame = ctk.CTkFrame(self.root, corner_radius=10)
        biaya_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.45, anchor="n")

        # Label "Biaya" di atas tabel
        label_biaya = ctk.CTkLabel(biaya_frame, text="Biaya", font=("Helvetica", 18, "bold"))
        label_biaya.place(relx=0.01, rely=0.01)

        # Frame Kiri - Scrollable Tabel Biaya
        left_frame = ctk.CTkFrame(biaya_frame, corner_radius=10)
        left_frame.place(relx=0.05, rely=0.15, relwidth=0.65, relheight=0.8)

        self.create_scrollable_table(left_frame)

        # Frame Kanan Atas - Total Biaya
        top_right_frame = ctk.CTkFrame(biaya_frame, corner_radius=10)
        top_right_frame.place(relx=0.72, rely=0.15, relwidth=0.28, relheight=0.4)

        total_label = ctk.CTkLabel(
            top_right_frame, text="TOTAL\nRp432.000,00", font=("Helvetica", 20, "bold"), text_color="green"
        )
        total_label.pack(expand=True)

        # Frame Kanan Bawah - Add Button
        bottom_right_frame = ctk.CTkFrame(biaya_frame, corner_radius=10)
        bottom_right_frame.place(relx=0.72, rely=0.62, relwidth=0.28, relheight=0.3)

        add_btn = ctk.CTkButton(bottom_right_frame, text="➕ Add", command=self.add_biaya)
        add_btn.pack(expand=True, pady=10)

    def create_scrollable_table(self, parent):
        """Creates a scrollable table within the left frame."""
        canvas = tk.Canvas(parent)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.CTkScrollbar(parent, command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollable_frame = ctk.CTkFrame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Table Header
        headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
        for col_idx, header in enumerate(headers):
            ctk.CTkLabel(
                scrollable_frame, text=header, font=("Helvetica", 14, "bold"), corner_radius=5, fg_color="#d9d9d9"
            ).grid(row=0, column=col_idx, padx=5, pady=5, sticky="ew")

        # Sample Data
        sample_data = [
            ("Semen", "Rp9.000", "12", "Rp108.000", "Bahan bangunan."),
            ("Pasir", "Rp9.000", "12", "Rp108.000", "Material pondasi."),
            ("Kayu", "Rp15.000", "8", "Rp120.000", "Rangka atap."),
        ]

        # Populate Data Rows
        for row_idx, row_data in enumerate(sample_data, start=1):
            for col_idx, value in enumerate(row_data):
                ctk.CTkLabel(
                    scrollable_frame, text=value, corner_radius=5, fg_color="white", text_color="black"
                ).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="ew")

            # Action Buttons
            action_frame = ctk.CTkFrame(scrollable_frame, corner_radius=5)
            action_frame.grid(row=row_idx, column=len(headers)-1, padx=5, pady=5)

            ctk.CTkButton(action_frame, text="✏", width=30, fg_color="blue", command=self.on_edit).pack(side="left", padx=2)
            ctk.CTkButton(action_frame, text="🗑", width=30, fg_color="red", command=self.on_delete).pack(side="left", padx=2)

        # Update Scroll Region
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def add_biaya(self):
        """Action for Add Biaya."""
        print("Add Biaya Clicked")

    def on_edit(self):
        """Action for Edit Button."""
        print("Edit button clicked")
        controller = PengelolaBiaya() # Replace with an actual controller instance if available
        editor = DisplayPopEdit(controller)
        editor.run()

    def on_delete(self):
        """Action for Delete Button."""
        print("Delete button clicked")


# Main Execution
if __name__ == "__main__":
    root = ctk.CTk()
    app = ProjectUI(root)
    root.mainloop()
