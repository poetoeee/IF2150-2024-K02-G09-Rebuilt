import tkinter as tk
from ttkbootstrap import ttk, Style
from ttkbootstrap.constants import *
from PIL import Image, ImageTk


class ProjectUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tugas and Biaya Management")
        self.root.geometry("1024x768")  # Fixed device window size
        self.style = Style("flatly")

        # Tugas Frame - Top Section (40% Height)
        self.create_tugas_frame()

        # Biaya Frame - Bottom Section (Centered with Scroll)
        self.create_biaya_frame()

    def create_tugas_frame(self):
        """Creates the top 'Tugas' section occupying 40% of the window."""
        tugas_frame = ttk.Frame(self.root, padding=10, borderwidth=2, relief="ridge")
        tugas_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.4, anchor="n")

        # Sample Tugas Header Content
        ttk.Label(tugas_frame, text="[Tugas Name]", font=("Arial", 18, "bold"), bootstyle="primary").pack(
            side="left", padx=10, pady=10
        )

        # Edit and Delete Buttons
        button_frame = ttk.Frame(tugas_frame)
        button_frame.pack(side="right", padx=10, pady=10)

        delete_btn = ttk.Button(button_frame, text="delete", bootstyle="danger.Outline")
        delete_btn.pack(side="left", padx=5)

        edit_btn = ttk.Button(button_frame, text="edit", bootstyle="primary.Outline")
        edit_btn.pack(side="left", padx=5)

        # Descriptive Text
        desc_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vitae augue vitae ante feugiat placerat."
        ttk.Label(tugas_frame, text=desc_text, wraplength=700, justify="left").pack(pady=5, padx=10)

        # Total Pengeluaran
        total_label = ttk.Label(tugas_frame, text="Total Pengeluaran\nRp432.000,00", 
                                font=("Arial", 14, "bold"), bootstyle="success")
        total_label.pack(anchor="e", padx=10, pady=5)

    def create_biaya_frame(self):
        """Creates the bottom 'Biaya' section centered below the Tugas frame with scrollable items."""
        # Create a Canvas widget for scrolling the rows
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.45, anchor="n")

        # Create a Canvas inside the frame
        canvas = tk.Canvas(canvas_frame)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Add a Scrollbar linked to the Canvas
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a Frame inside the Canvas to hold the content
        content_frame = ttk.Frame(canvas, padding=10, borderwidth=2, relief="ridge")
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Header Section (Fixed)
        header_frame = ttk.Frame(content_frame)
        header_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
        for col_idx, header in enumerate(headers):
            header_label = ttk.Label(header_frame, text=header, font=("Arial", 12, "bold"), anchor="center", 
                                     bootstyle="secondary")
            header_label.grid(row=0, column=col_idx, padx=5, pady=5, sticky="nsew")
            header_frame.grid_columnconfigure(col_idx, weight=1)

        # Create a Frame inside the row_canvas to hold the rows (this frame will be scrollable)
        row_content_frame = ttk.Frame(content_frame)
        row_content_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Table Rows with Sample Data
        sample_data = [
            ("Semen", "Rp9.000", "12", "Rp108.000", "", ""),
            ("Pasir", "Rp9.000", "12", "Rp108.000", "", ""),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", "", ""),
            ("Cat dinding", "Rp9.000", "12", "Rp108.000", "", ""),
            ("Cement", "Rp9.000", "10", "Rp90.000", "", ""),
            ("Batu Bata", "Rp10.000", "5", "Rp50.000", "", ""),
            ("Pasir Merah", "Rp8.000", "15", "Rp120.000", "", ""),
            ("Kayu", "Rp15.000", "8", "Rp120.000", "", ""),
            # Add more rows as needed...
        ]
        for row_idx, row_data in enumerate(sample_data, start=1):
            for col_idx, value in enumerate(row_data[:-1]):  # Exclude Aksi column
                ttk.Label(row_content_frame, text=value, anchor="center", font=("Arial", 11)).grid(
                    row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew"
                )

            # Add Action Buttons in Aksi Column
            action_frame = ttk.Frame(row_content_frame)
            action_frame.grid(row=row_idx, column=len(headers)-1, padx=5, pady=5)

            edit_btn = ttk.Button(action_frame, text="✏", bootstyle="info.Outline", width=3)
            edit_btn.pack(side="left", padx=2)

            delete_btn = ttk.Button(action_frame, text="🗑", bootstyle="danger.Outline", width=3)
            delete_btn.pack(side="left", padx=2)

        # Update the row_content_frame scroll region
        row_content_frame.update_idletasks()  # Ensure the content is fully loaded
        canvas.config(scrollregion=canvas.bbox("all"))

        # Bottom Section: Total and Add Button (Fixed)
        bottom_frame = ttk.Frame(content_frame)
        bottom_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

        # Total Label on the Left
        total_label = ttk.Label(bottom_frame, text="TOTAL   Rp432.000,00", font=("Arial", 12, "bold"), bootstyle="success")
        total_label.pack(side="left")

        # Add Button on the Right
        add_btn = ttk.Button(bottom_frame, text="➕  Add", bootstyle="primary", command=self.add_biaya)
        add_btn.pack(side="right")

    def add_biaya(self):
        """Action for Add Biaya."""
        print("Add Biaya Clicked")


# Main Execution
if __name__ == "__main__":
    style = Style("flatly")  # Use a modern style
    root = style.master
    app = ProjectUI(root)
    root.mainloop()
