import tkinter as tk
import customtkinter as ctk
from boundaries.DisplayPopBiaya import DisplayPopBiaya
from controllers.PengelolaBiaya import PengelolaBiaya


class BiayaFrame(ctk.CTkFrame):
    """Frame untuk menampilkan tabel biaya, total biaya, dan tombol add."""
    def __init__(self, parent, biaya_data, total_biaya, add_callback=None, **kwargs):
        super().__init__(parent, **kwargs)
        controller = PengelolaBiaya()

        # Frame kiri - Scrollable Table
        left_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="white")
        left_frame.place(relx=0, rely=0.1, relwidth=0.65, relheight=0.8)
        self.create_scrollable_table(left_frame, biaya_data)

        # Frame kanan atas - Total Biaya
        top_right_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#f0f0f0")
        top_right_frame.place(relx=0.7, rely=0.1, relwidth=0.28, relheight=0.4)

        total_label = ctk.CTkLabel(
            top_right_frame, text="TOTAL", font=("Helvetica", 18, "bold"), text_color="black"
        )
        total_label.pack(pady=(20, 5))

        total_value = ctk.CTkLabel(
            top_right_frame, text=f"Rp{total_biaya:,}", font=("Helvetica", 22, "bold"), text_color="green"
        )
        total_value.pack(pady=5)

        # Frame kanan bawah - Add Button
        bottom_right_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#f0f0f0")
        bottom_right_frame.place(relx=0.7, rely=0.55, relwidth=0.28, relheight=0.3)

        add_button = ctk.CTkButton(
            bottom_right_frame, text="➕  Add", fg_color="#3b82f6", hover_color="#2563eb",
            text_color="white", font=("Helvetica", 14), command=add_callback
        )
        add_button.pack(expand=True, pady=10)

    def create_scrollable_table(self, parent, data):
        """Membuat tabel scrollable dengan gridlines."""
        canvas = tk.Canvas(parent, bd=0, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.CTkScrollbar(parent, command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollable_frame = ctk.CTkFrame(canvas, corner_radius=0)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
        for col_idx, header in enumerate(headers):
            ctk.CTkLabel(
                scrollable_frame, text=header, font=("Helvetica", 12, "bold"),
                fg_color="#e5e5e5", text_color="black", width=120, height=30
            ).grid(row=0, column=col_idx, sticky="nsew", padx=1, pady=1)

        for row_idx, row_data in enumerate(data, start=1):
            for col_idx, value in enumerate(row_data):
                ctk.CTkLabel(
                    scrollable_frame, text=value, font=("Helvetica", 11), fg_color="white",
                    text_color="black", width=120, height=30
                ).grid(row=row_idx, column=col_idx, sticky="nsew", padx=1, pady=1)

            # Action Buttons
            action_frame = ctk.CTkFrame(scrollable_frame, fg_color="white")
            action_frame.grid(row=row_idx, column=len(headers) - 1, sticky="nsew", padx=1, pady=1)

            ctk.CTkButton(action_frame, text="✏", fg_color="#3b82f6", width=30, height=25).pack(side="left", padx=2)
            ctk.CTkButton(action_frame, text="🗑", fg_color="#dc2626", width=30, height=25).pack(side="left", padx=2)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


class ProjectUI(ctk.CTk):
    """Main window with Tugas and Biaya section."""
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.title("Tugas dan Biaya Management")
        self.state("zoomed")

        # Sample Data
        biaya_data = [
            ("Semen", "Rp9.000", "12", "Rp108.000", "Bahan bangunan utama."),
            ("Pasir", "Rp9.000", "12", "Rp108.000", "Material pondasi."),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", "Gaji harian pekerja."),
            ("Cat dinding", "Rp9.000", "12", "Rp108.000", "Untuk finishing."),
        ]
        total_biaya = 432000

        # Frame Tugas (40% layar)
        tugas_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#f8f9fa")
        tugas_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.4, anchor="n")

        ctk.CTkLabel(
            tugas_frame, text="[Tugas Name]", font=("Helvetica", 24, "bold"), text_color="#3b82f6"
        ).pack(anchor="w", padx=20, pady=10)

        ctk.CTkLabel(
            tugas_frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
                              "Etiam vitae augue vitae ante feugiat placerat.",
            font=("Helvetica", 14), justify="left"
        ).pack(anchor="w", padx=20)

        # Frame Biaya (60% layar dengan pembagian 3 subframe)
        biaya_frame = BiayaFrame(
            self, biaya_data=biaya_data, total_biaya=total_biaya, corner_radius=10, fg_color="#f8f9fa"
        )
        biaya_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.45, anchor="n")


if __name__ == "__main__":
    app = ProjectUI()
    app.mainloop()
