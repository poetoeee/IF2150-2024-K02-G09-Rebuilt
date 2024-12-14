import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import customtkinter as ctk

from entities.Biaya import Biaya
from controllers.PengelolaBiaya import PengelolaBiaya

class ProjectUI:
    def __init__(self, root):
        ctk.set_appearance_mode("light")  # Mode 'light' atau 'dark'
        ctk.set_default_color_theme("blue")  # Warna tema: blue, green, dark-blue

        self.root = root
        self.root.title("Tugas and Biaya Management")
        self.root.geometry("1024x768")
        self.root.configure(bg="#FFFFFF")  # Latar belakang putih

        # Inisialisasi controller biaya
        self.controller = PengelolaBiaya()

        # Tugas Frame - Top Section
        self.create_tugas_frame()

        # Biaya Frame with Sub-Frames
        self.create_biaya_section()

    def create_tugas_frame(self):
        """Creates the top 'Tugas' section occupying 40% of the window."""
        tugas_frame = ctk.CTkFrame(self.root, corner_radius=10, fg_color="#FFFFFF")  # Background putih
        tugas_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.4, anchor="n")

        ctk.CTkLabel(
            tugas_frame,
            text="[Tugas Name]",
            font=("Helvetica", 18, "bold"),
            text_color="#4B0082"  # Warna ungu gelap
        ).pack(side="left", padx=10, pady=10)

    def create_biaya_section(self):
        """Creates the 'Biaya' section divided into 3 frames."""
        biaya_frame = ctk.CTkFrame(self.root, corner_radius=10, fg_color="#FFFFFF")  # Background putih
        biaya_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.45, anchor="n")

        # Label "Biaya"
        label_biaya = ctk.CTkLabel(
            biaya_frame,
            text="Biaya",
            font=("Helvetica", 18, "bold"),
            text_color="black"  # Warna merah tua
        )
        label_biaya.place(relx=0.05, rely=0.04)

        # Frame Kiri - Scrollable Tabel Biaya
        left_frame = ctk.CTkFrame(biaya_frame, corner_radius=10, fg_color="#FFFFFF")  # Background putih
        left_frame.place(relx=0.05, rely=0.15, relwidth=0.65, relheight=0.8)
        self.create_scrollable_table(left_frame)

        # Frame Kanan Atas - Total Biaya
        top_right_frame = ctk.CTkFrame(biaya_frame, corner_radius=10, fg_color="#FFFFFF")  # Background putih
        top_right_frame.place(relx=0.71, rely=0.15, relwidth=0.28, relheight=0.4)

        # Hitung Total Biaya
        total_biaya = self.controller.getTotalBiaya()
        total_label = ctk.CTkLabel(
            top_right_frame,
            text=f"TOTAL\nRp{total_biaya:,}",  # Format angka dengan pemisah ribuan
            font=("Helvetica", 20, "bold"),
            text_color="#FF4500"  # Warna oranye
        )
        total_label.pack(expand=True)

        # Frame Kanan Bawah - Add Button
        bottom_right_frame = ctk.CTkFrame(biaya_frame, corner_radius=10, fg_color="#FFFFFF")  # Background putih
        bottom_right_frame.place(relx=0.71, rely=0.62, relwidth=0.28, relheight=0.3)

        add_btn = ctk.CTkButton(
            bottom_right_frame,
            text="➕ Add",
            command=self.add_biaya,
            fg_color="#4682B4",  # Warna biru baja
            text_color="#FFFFFF"  # Warna teks putih
        )
        add_btn.pack(expand=True, pady=10)

    def create_scrollable_table(self, parent):
        """Creates a scrollable table populated from the database using PengelolaBiaya."""
        # Frame utama untuk menampung canvas dan scrollbar horizontal
        outer_frame = ctk.CTkFrame(parent, fg_color="#FFFFFF")  # Background putih
        outer_frame.pack(fill="both", expand=True)

        # Canvas untuk scrolling
        canvas = tk.Canvas(outer_frame, bg="#FFFFFF")  # Latar belakang putih
        canvas.pack(side="left", fill="both", expand=True)

        # Scrollbars
        v_scrollbar = ctk.CTkScrollbar(outer_frame, command=canvas.yview, fg_color="#4682B4")  # Scrollbar biru
        v_scrollbar.pack(side="right", fill="y")

        h_scrollbar = ctk.CTkScrollbar(parent, command=canvas.xview, orientation="horizontal", fg_color="#4682B4")
        h_scrollbar.pack(side="bottom", fill="x")  # Posisi horizontal di bawah tabel

        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Frame untuk konten tabel di dalam canvas
        scrollable_frame = ctk.CTkFrame(canvas, fg_color="#FFFFFF")  # Latar putih untuk tabel
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Binding untuk memastikan scroll bekerja dengan benar
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))  # Update scroll region
        )

        # Table Header
        headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
        for col_idx, header in enumerate(headers):
            ctk.CTkLabel(
                scrollable_frame, 
                text=header, 
                font=("Helvetica", 14, "bold"), 
                corner_radius=5, 
                fg_color="blue",  # Warna merah tua untuk header
                text_color="#FFFFFF",  # Teks putih
                width=150  # Atur lebar kolom
            ).grid(row=0, column=col_idx, padx=5, pady=5, sticky="ew")

        # Fetch data from PengelolaBiaya
        pengelola_biaya = PengelolaBiaya()
        biaya_list = pengelola_biaya.getAllBiaya()

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
                    scrollable_frame, 
                    text=str(value), 
                    corner_radius=5, 
                    fg_color="#FFFFFF",  # Warna putih untuk sel
                    text_color="#000000",  # Warna teks hitam
                    width=150
                ).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="ew")

            # Action Buttons
            action_frame = ctk.CTkFrame(scrollable_frame, corner_radius=5, fg_color="#FFFFFF")  # Background putih
            action_frame.grid(row=row_idx, column=len(headers) - 1, padx=5, pady=5)

            ctk.CTkButton(
                action_frame,
                text="✏",
                width=30,
                fg_color="#4B0082",  # Warna ungu gelap
                text_color="#FFFFFF",
                command=lambda b=biaya: self.on_edit(b)
            ).pack(side="left", padx=2)

            ctk.CTkButton(
                action_frame,
                text="🗑",
                width=30,
                fg_color="#FF0000",  # Warna merah
                text_color="#FFFFFF",
                command=lambda b_id=biaya.getidBiaya(): self.on_delete(b_id)
            ).pack(side="left", padx=2)

        # Update Scroll Region
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def add_biaya(self):
        DisplayPopAdd(self.controller, self.refresh_biaya_section)


    def refresh_biaya_table(self):
        """Refresh tabel biaya dengan data terbaru dari database."""
        self.create_biaya_section()

    def refresh_biaya_section(self):
        """Refresh tabel biaya dan total biaya."""
        self.create_biaya_section()


    def on_edit(self, biaya):
        DisplayPopEdit(self.controller, biaya, self.refresh_biaya_section)


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

        yes_button = ctk.CTkButton(popup, text="Iya", command=on_confirm, fg_color="blue")
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

class DisplayPopEdit:
    def __init__(self, controller, biaya, refresh_callback):
        self.controller = controller
        self.current_biaya = biaya  # Menyimpan data biaya yang akan diedit
        self.refresh_callback = refresh_callback

        # Toplevel window sebagai popup
        self.window = ctk.CTkToplevel()
        self.window.title("Form Edit Biaya")

        # Fokus pada popup window
        self.window.grab_set()

        # Ukuran popup yang lebih kecil
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
        padding_x = 20
        padding_y = 5

        # Nama Barang
        ctk.CTkLabel(self.window, text="Nama Barang", font=("Poppins", 14), anchor="w").pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.entry1 = ctk.CTkEntry(self.window)
        self.entry1.insert(0, self.current_biaya.getnamaBarangBiaya())
        self.entry1.pack(padx=padding_x, pady=padding_y, fill="x")

        # Harga Satuan
        ctk.CTkLabel(self.window, text="Harga Satuan", font=("Poppins", 14), anchor="w").pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.entry2 = ctk.CTkEntry(self.window)
        self.entry2.insert(0, self.current_biaya.gethargaSatuanBiaya())
        self.entry2.pack(padx=padding_x, pady=padding_y, fill="x")

        # Kuantitas
        ctk.CTkLabel(self.window, text="Kuantitas", font=("Poppins", 14), anchor="w").pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.entry3 = ctk.CTkEntry(self.window)
        self.entry3.insert(0, self.current_biaya.getquantityBiaya())
        self.entry3.pack(padx=padding_x, pady=padding_y, fill="x")

        # Deskripsi
        ctk.CTkLabel(self.window, text="Deskripsi", font=("Poppins", 14), anchor="w").pack(padx=padding_x, pady=(padding_y, 0), fill="x")
        self.text_box = scrolledtext.ScrolledText(self.window, height=5, wrap="word", font=("Poppins", 12))
        self.text_box.insert("1.0", self.current_biaya.getketeranganBiaya())
        self.text_box.pack(padx=padding_x, pady=padding_y, fill="x")

        # Tombol SAVE
        ctk.CTkButton(self.window, text="SAVE", command=self.save_data).pack(pady=20)

    def save_data(self):
        try:
            # Ambil data input
            nama_barang = self.entry1.get().strip()
            harga_satuan = int(self.entry2.get().strip())
            kuantitas = int(self.entry3.get().strip())
            deskripsi = self.text_box.get("1.0", tk.END).strip()

            # Validasi angka positif
            if harga_satuan <= 0 or kuantitas <= 0:
                messagebox.showerror("Error", "Harga Satuan dan Kuantitas harus lebih dari 0.")
                return

            # Update data Biaya
            self.current_biaya.setnamaBarangBiaya(nama_barang)
            self.current_biaya.sethargaSatuanBiaya(harga_satuan)
            self.current_biaya.setquantityBiaya(kuantitas)
            self.current_biaya.setketeranganBiaya(deskripsi)
            self.current_biaya.settotalBiaya(harga_satuan * kuantitas)

            # Simpan perubahan
            if self.controller.editBiaya(self.current_biaya):
                messagebox.showinfo("Success", "Data berhasil diperbarui.")
                self.refresh_callback()
                self.window.destroy()
            else:
                messagebox.showerror("Error", "Gagal memperbarui data.")
        except ValueError:
            messagebox.showerror("Error", "Harga Satuan dan Kuantitas harus berupa angka valid.")
            self.entry2.focus_set()



# Main Execution
# if __name__ == "__main__":
#     root = ctk.CTk()
#     app = ProjectUI(root)
#     root.mainloop()