import tkinter as tk
from ttkbootstrap import ttk, Style
from ttkbootstrap.constants import *

class ProjectUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tugas and Biaya Management")
        self.root.geometry("1024x768")  # Fixed window size
        self.style = Style("flatly")

        # Tugas Frame - Top Section
        self.create_tugas_frame()

        # Biaya Frame with Sub-Frames
        self.create_biaya_section()

    def create_tugas_frame(self):
        """Creates the top 'Tugas' section occupying 40% of the window."""
        tugas_frame = ttk.Frame(self.root, padding=10, borderwidth=2, relief="ridge")
        tugas_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.4, anchor="n")

        ttk.Label(tugas_frame, text="[Tugas Name]", font=("Helvetica", 18, "bold"), bootstyle="primary").pack(
            side="left", padx=10, pady=10
        )

    def create_biaya_section(self):
        """Creates the 'Biaya' section divided into 3 frames."""
        biaya_frame = ttk.Frame(self.root, padding=10, borderwidth=2, relief="ridge")
        biaya_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.47, anchor="n")

        # Label "Biaya" di atas tabel
        label_biaya = ttk.Label(biaya_frame, text="Biaya", font=("Helvetica", 18, "bold"), bootstyle="primary")
        label_biaya.place(relx=0.01, rely=0.01)  # Posisi di kiri atas

        # Frame Kiri - Scrollable Tabel Biaya (diperkecil)
        left_frame = ttk.Frame(biaya_frame, borderwidth=2, relief="groove")
        left_frame.place(relx=0.05, rely=0.15, relwidth=0.65, relheight=0.8)  # Tinggi diperkecil dengan relheight=0.9

        self.create_scrollable_table(left_frame)

        # Frame Kanan Atas - Total Biaya
        top_right_frame = ttk.Frame(biaya_frame, borderwidth=2, relief="groove", padding=20)
        top_right_frame.place(relx=0.72, rely=0.15, relwidth=0.28, relheight=0.4)

        total_label = ttk.Label(top_right_frame, text="TOTAL\nRp432.000,00", font=("Helvetica", 20, "bold"), bootstyle="success")
        total_label.pack(expand=True)

        # Frame Kanan Bawah - Add Button
        bottom_right_frame = ttk.Frame(biaya_frame, borderwidth=2, relief="groove", padding=10)
        bottom_right_frame.place(relx=0.72, rely=0.62, relwidth=0.28, relheight=0.3)

        add_btn = ttk.Button(bottom_right_frame, text="➕  Add", bootstyle="primary", command=self.add_biaya)
        add_btn.pack(expand=True, pady=10)


    def create_scrollable_table(self, parent):
        """Creates a scrollable table within the left frame."""
        canvas = tk.Canvas(parent)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Konfigurasi bobot kolom untuk mengatur ukuran relatif
        scrollable_frame.grid_columnconfigure(0, weight=2)  # Barang (lebih besar)
        scrollable_frame.grid_columnconfigure(1, weight=1)  # Harga
        scrollable_frame.grid_columnconfigure(2, weight=1)  # Qty (lebih kecil)
        scrollable_frame.grid_columnconfigure(3, weight=1)  # Total
        scrollable_frame.grid_columnconfigure(4, weight=4)  # Keterangan (paling luas)
        scrollable_frame.grid_columnconfigure(5, weight=1)  # Aksi

        # Table Header
        headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
        for col_idx, header in enumerate(headers):
            ttk.Label(
                scrollable_frame, 
                text=header, 
                font=("Helvetica", 14, "bold"), 
                anchor="center"
            ).grid(row=0, column=col_idx, padx=10, pady=5, sticky="ew")

        # Sample Data
        sample_data = [
            ("Semen", "Rp9.000", "12", "Rp108.000", "Bahan bangunan yang sangat penting untuk pembangunan rumah dan gedung."),
            ("Pasir", "Rp9.000", "12", "Rp108.000", "Untuk pondasi sebagai elemen utama konstruksi bangunan."),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", "Gaji harian untuk tenaga pekerja di proyek."),
            ("Kayu", "Rp15.000", "8", "Rp120.000", "Material konstruksi yang digunakan untuk rangka atap dan furniture.")
        ]

        # Populate Data Rows
        for row_idx, row_data in enumerate(sample_data, start=1):
            for col_idx, value in enumerate(row_data):
                if col_idx == 4:  # Keterangan (Kolom lebih luas)
                    padx_value = 20
                elif col_idx == 2:  # Qty (Kolom lebih kecil)
                    padx_value = 5
                else:
                    padx_value = 10

                ttk.Label(
                    scrollable_frame, 
                    text=value, 
                    anchor="center", 
                    wraplength=300 if col_idx == 4 else 150  # Perbesar wraplength untuk Keterangan
                ).grid(row=row_idx, column=col_idx, padx=padx_value, pady=5, sticky="ew")

            # Add Action Buttons
            action_frame = ttk.Frame(scrollable_frame)
            action_frame.grid(row=row_idx, column=len(headers)-1, padx=5, pady=5)

            ttk.Button(action_frame, text="✏", bootstyle="info.Outline", width=3, command=self.on_edit).pack(side="left", padx=2)
            ttk.Button(action_frame, text="🗑", bootstyle="danger.Outline", width=3, command=self.on_delete).pack(side="left", padx=2)

        # Update Scroll Region
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


    def add_biaya(self):
        """Action for Add Biaya."""
        print("Add Biaya Clicked")

    def on_edit(self):
        """Action for Edit Button."""
        print("Edit button clicked")

    def on_delete(self):
        """Action for Delete Button."""
        print("Delete button clicked")

# Main Execution
if __name__ == "__main__":
    style = Style("flatly")  # Use a modern style
    root = style.master
    app = ProjectUI(root)
    root.mainloop()