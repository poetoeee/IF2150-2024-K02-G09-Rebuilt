import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from controllers.PengelolaBiaya import PengelolaBiaya
from boundaries.DPBEdit import DisplayPopEdit
from boundaries.DPBAdd import DisplayPopAdd

class ProjectUI:
    def __init__(self, root):
        ctk.set_appearance_mode("light")  # Mode 'light' atau 'dark'
        ctk.set_default_color_theme("blue")  # Warna tema: blue, green, dark-blue

        self.root = root
        self.root.title("Tugas and Biaya Management")
        self.root.geometry("1024x768")

        # Inisialisasi controller biaya
        self.controller = PengelolaBiaya()

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

        # Label "Biaya"
        label_biaya = ctk.CTkLabel(biaya_frame, text="Biaya", font=("Helvetica", 18, "bold"))
        label_biaya.place(relx=0.01, rely=0.01)

        # Frame Kiri - Scrollable Tabel Biaya
        left_frame = ctk.CTkFrame(biaya_frame, corner_radius=10)
        left_frame.place(relx=0.05, rely=0.15, relwidth=0.65, relheight=0.8)
        self.create_scrollable_table(left_frame)

        # Frame Kanan Atas - Total Biaya
        top_right_frame = ctk.CTkFrame(biaya_frame, corner_radius=10)
        top_right_frame.place(relx=0.72, rely=0.15, relwidth=0.28, relheight=0.4)

        # Hitung Total Biaya
        total_biaya = self.controller.getTotalBiaya()
        total_label = ctk.CTkLabel(
            top_right_frame,
            text=f"TOTAL\nRp{total_biaya:,}",  # Format angka dengan pemisah ribuan
            font=("Helvetica", 20, "bold"),
            text_color="green"
        )
        total_label.pack(expand=True)

        # Frame Kanan Bawah - Add Button
        bottom_right_frame = ctk.CTkFrame(biaya_frame, corner_radius=10)
        bottom_right_frame.place(relx=0.72, rely=0.62, relwidth=0.28, relheight=0.3)

        add_btn = ctk.CTkButton(bottom_right_frame, text="➕ Add", command=self.add_biaya)
        add_btn.pack(expand=True, pady=10)



    def create_scrollable_table(self, parent):
        """Creates a scrollable table populated from the database using PengelolaBiaya."""
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

        # Fetch data from PengelolaBiaya
        pengelola_biaya = PengelolaBiaya()
        biaya_list = pengelola_biaya.getAllBiaya()

        # Debug: Cetak data ke console
        print("Data Biaya dari Database:")
        for biaya in biaya_list:
            print(biaya.getnamaBarangBiaya(), biaya.gethargaSatuanBiaya(), biaya.getquantityBiaya())

        # Populate Data Rows
        for row_idx, biaya in enumerate(biaya_list, start=1):
            row_data = [
                biaya.getnamaBarangBiaya(),
                biaya.gethargaSatuanBiaya(),
                biaya.getquantityBiaya(),
                biaya.gettotalBiaya(),
                biaya.getketeranganBiaya(),
            ]
            for col_idx, value in enumerate(row_data):
                ctk.CTkLabel(
                    scrollable_frame, text=str(value), corner_radius=5, fg_color="white", text_color="black"
                ).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="ew")

            # Action Buttons
            action_frame = ctk.CTkFrame(scrollable_frame, corner_radius=5)
            action_frame.grid(row=row_idx, column=len(headers)-1, padx=5, pady=5)

            ctk.CTkButton(action_frame, text="✏", width=30, fg_color="blue", command=lambda b=biaya: self.on_edit(b)).pack(side="left", padx=2)
            ctk.CTkButton(action_frame, text="🗑", command=lambda b_id=biaya.getidBiaya(): self.on_delete(b_id)).pack()

        # Update Scroll Region
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def add_biaya(self):
        """Membuka popup untuk menambahkan data biaya dan refresh tabel setelahnya."""
        popup = DisplayPopAdd(self.controller, self.refresh_biaya_section)
        popup.run()

    def refresh_biaya_table(self):
        """Refresh tabel biaya dengan data terbaru dari database."""
        self.create_biaya_section()

    def refresh_biaya_section(self):
        """Refresh tabel biaya dan total biaya."""
        self.create_biaya_section()


    def on_edit(self, biaya):
        """Membuka popup untuk mengedit data biaya."""
        def refresh_and_close():
            self.refresh_biaya_section()  # Refresh tabel setelah update
            editor_window.window.destroy()  # Tutup popup

        # Kirim controller, data biaya, dan callback
        editor_window = DisplayPopEdit(self.controller, biaya, refresh_and_close)
        editor_window.run()


    def on_delete(self, id_biaya):
        """Action for Delete Button."""
        def on_confirm():
            if self.controller.deleteBiaya(id_biaya):
                messagebox.showinfo("Berhasil", f"Biaya dengan ID {id_biaya} berhasil dihapus.")
                self.refresh_biaya_section()  # Refresh tabel dan total
            else:
                messagebox.showerror("Gagal", f"Gagal menghapus biaya dengan ID {id_biaya}.")
            popup.destroy()

        def on_cancel():
            popup.destroy()

        # Popup Konfirmasi
        popup = ctk.CTkToplevel()
        popup.title("Konfirmasi Penghapusan")
        popup.geometry("300x150")
        popup.resizable(False, False)

        label = ctk.CTkLabel(
            popup, text=f"Apakah Anda yakin ingin menghapus biaya dengan ID {id_biaya}?", wraplength=280
        )
        label.pack(pady=20)

        yes_button = ctk.CTkButton(popup, text="Iya", command=on_confirm, fg_color="red")
        yes_button.pack(side="left", padx=(30, 10), pady=10)

        cancel_button = ctk.CTkButton(popup, text="Batal", command=on_cancel)
        cancel_button.pack(side="right", padx=(10, 30), pady=10)

        popup.grab_set()


# Main Execution
# if __name__ == "__main__":
#     root = ctk.CTk()
#     app = ProjectUI(root)
#     root.mainloop()