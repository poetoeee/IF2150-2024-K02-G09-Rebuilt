import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import customtkinter as ctk

from entities.Biaya import Biaya
from boundaries.DPBEdit import DisplayPopEdit
from controllers.PengelolaBiaya import PengelolaBiaya

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
        
class DisplayPopAdd:
    def __init__(self, controller, refresh_callback):
        self.controller = controller
        self.refresh_callback = refresh_callback

        # Toplevel window sebagai popup
        self.window = ctk.CTkToplevel()
        self.window.title("Form Tambah Biaya")

        # Fokus pada popup window
        self.window.grab_set()

        # Mengatur ukuran popup lebih kecil
        window_width = 450
        window_height = 500
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Panggil form
        self.create_form()

    def create_form(self):
        # Padding umum untuk form
        padding_x = 20
        padding_y = 5

        # Nama Barang
        label1 = ctk.CTkLabel(self.window, text="Nama Barang", font=("Poppins", 14), anchor="w")
        label1.pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.entry1 = ctk.CTkEntry(self.window)
        self.entry1.pack(padx=padding_x, pady=(0, padding_y), fill="x")

        # Harga Satuan
        label2 = ctk.CTkLabel(self.window, text="Harga Satuan", font=("Poppins", 14), anchor="w")
        label2.pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.entry2 = ctk.CTkEntry(self.window)
        self.entry2.pack(padx=padding_x, pady=(0, padding_y), fill="x")

        # Kuantitas
        label3 = ctk.CTkLabel(self.window, text="Kuantitas", font=("Poppins", 14), anchor="w")
        label3.pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.entry3 = ctk.CTkEntry(self.window)
        self.entry3.pack(padx=padding_x, pady=(0, padding_y), fill="x")

        # Deskripsi
        label4 = ctk.CTkLabel(self.window, text="Deskripsi", font=("Poppins", 14), anchor="w")
        label4.pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.text_box = scrolledtext.ScrolledText(self.window, height=5, wrap="word", font=("Poppins", 12))
        self.text_box.pack(padx=padding_x, pady=(0, padding_y), fill="x")

        # Tombol SAVE
        save_button = ctk.CTkButton(self.window, text="SAVE", command=self.save_data, width=100)
        save_button.pack(pady=20)

    def save_data(self):
        try:
            # Ambil data input
            nama_barang = self.entry1.get().strip()
            harga_satuan = int(self.entry2.get().strip())
            kuantitas = int(self.entry3.get().strip())
            deskripsi = self.text_box.get("1.0", tk.END).strip()
            total_biaya = harga_satuan * kuantitas

            if harga_satuan <= 0 or kuantitas <= 0:
                raise ValueError("Harga Satuan dan Kuantitas harus lebih dari 0!")

            # Membuat objek Biaya
            new_biaya = Biaya(
                namaBarangBiaya=nama_barang,
                keteranganBiaya=deskripsi,
                hargaSatuanBiaya=harga_satuan,
                quantityBiaya=kuantitas,
                totalBiaya=total_biaya
            )

            # Simpan ke database via controller
            if self.controller.addBiaya(new_biaya):
                messagebox.showinfo("Sukses", "Data Biaya berhasil ditambahkan.")
                self.refresh_callback()
                self.window.destroy()  # Tutup popup
            else:
                messagebox.showerror("Error", "Gagal menambahkan Biaya.")
        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")




# Main Execution
# if __name__ == "__main__":
#     root = ctk.CTk()
#     app = ProjectUI(root)
#     root.mainloop()