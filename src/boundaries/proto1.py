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

        # Biaya Frame - Bottom Section with Scrollable Table
        self.create_biaya_frame()

    def create_tugas_frame(self):
        """Creates the top 'Tugas' section occupying 40% of the window."""
        tugas_frame = ttk.Frame(self.root, padding=10, borderwidth=2, relief="ridge")
        tugas_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.4, anchor="n")

        ttk.Label(tugas_frame, text="[Tugas Name]", font=("Arial", 18, "bold"), bootstyle="primary").pack(
            side="left", padx=10, pady=10
        )

    def create_biaya_frame(self):
        """Creates the bottom 'Biaya' section with a scrollable table."""
        biaya_frame = ttk.Frame(self.root, padding=10, borderwidth=2, relief="ridge")
        biaya_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.45, anchor="n")

        # Header
        ttk.Label(biaya_frame, text="[Biaya]", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)

        # Canvas for Scrollable Table
        canvas = tk.Canvas(biaya_frame)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(biaya_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Table Header
        headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
        for col_idx, header in enumerate(headers):
            ttk.Label(scrollable_frame, text=header, font=("Arial", 16, "bold"), anchor="center").grid(
                row=0, column=col_idx, padx=30, pady=5, sticky="nsew"
            )
            scrollable_frame.grid_columnconfigure(col_idx, weight=1)

        # Sample Data
        sample_data = [
            ("Semen", "Rp9.000", "12", "Rp108.000", ""),
            ("Pasir", "Rp9.000", "12", "Rp108.000", ""),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", ""),
            ("Cat dinding", "Rp9.000", "12", "Rp108.000", ""),
            ("Batu Bata", "Rp10.000", "5", "Rp50.000", ""),
            ("Kayu", "Rp15.000", "8", "Rp120.000", ""),
            ("Semen", "Rp9.000", "12", "Rp108.000", ""),
            ("Pasir", "Rp9.000", "12", "Rp108.000", ""),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", ""),
            ("Cat dinding", "Rp9.000", "12", "Rp108.000", ""),
            ("Batu Bata", "Rp10.000", "5", "Rp50.000", ""),
            ("Kayu", "Rp15.000", "8", "Rp120.000", ""),
            ("Semen", "Rp9.000", "12", "Rp108.000", ""),
            ("Pasir", "Rp9.000", "12", "Rp108.000", ""),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", ""),
            ("Cat dinding", "Rp9.000", "12", "Rp108.000", ""),
            ("Batu Bata", "Rp10.000", "5", "Rp50.000", ""),
            ("Kayu", "Rp15.000", "8", "Rp120.000", ""),
            ("Semen", "Rp9.000", "12", "Rp108.000", ""),
            ("Pasir", "Rp9.000", "12", "Rp108.000", ""),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", ""),
            ("Cat dinding", "Rp9.000", "12", "Rp108.000", ""),
            ("Batu Bata", "Rp10.000", "5", "Rp50.000", ""),
            ("Kayu", "Rp15.000", "8", "Rp120.000", ""),

        ]

        # Populate Table Rows
        for row_idx, row_data in enumerate(sample_data, start=1):
            for col_idx, value in enumerate(row_data):
                ttk.Label(scrollable_frame, text=value, anchor="center", font=("Arial", 11)).grid(
                    row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew"
                )

            # Add Action Buttons in Aksi Column
            action_frame = ttk.Frame(scrollable_frame)
            action_frame.grid(row=row_idx, column=len(headers)-1, padx=5, pady=5)

            ttk.Button(action_frame, text="✏", bootstyle="info.Outline", width=3, command=self.on_edit).pack(side="left", padx=2)
            ttk.Button(action_frame, text="🗑", bootstyle="danger.Outline", width=3, command=self.on_delete).pack(side="left", padx=2)

        # Update Scroll Region
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Bottom Section: Total and Add Button
        bottom_frame = ttk.Frame(biaya_frame)
        bottom_frame.pack(fill="x", pady=30, padx=1)

        # Total Label
        total_label = ttk.Label(bottom_frame, text="       TOTAL\n Rp432.000,00", font=("Arial", 20, "bold"), bootstyle="success")
        total_label.pack(side="top", pady= 20, padx= 20)

        # Add Button
        add_btn = ttk.Button(bottom_frame, text="➕  Add", bootstyle="primary", command=self.add_biaya)
        add_btn.pack(side="bottom", pady=10, padx=55 )

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