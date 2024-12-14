from tkinter import messagebox
import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk 
from entities.Biaya import Biaya
class DisplayPopAdd:
    def __init__(self, controller, refresh_callback):
        self.controller = controller
        self.refresh_callback = refresh_callback  # Callback untuk refresh tabel
        self.window = ctk.CTk()
        self.window.configure(fg_color="#EBEBEB") 
        self.displayPopAdd()


    def displayPopAdd(self):
        formWindow = ctk.CTkToplevel(self.window)
        formWindow.title("Form Edit Biaya")

        # Mengatur ukuran dan posisi popup
        window_width = 500
        window_height = 700
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        formWindow.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Konfigurasi kolom
        formWindow.grid_columnconfigure(0, weight=1)  # Membuat kolom 0 fleksibel meluas

        # Back Button
        customButton = ctk.CTkButton(
            formWindow,
            text="\u2190 Back to Tugas Name",
            command=formWindow.destroy,
            fg_color="#EBEBEB",
            text_color="black",
            hover_color="lightgray",
            font=("Poppins", 18, "bold")
        )
        customButton.grid(row=0, column=0, sticky="W", padx=10, pady=10)

        # Title Label
        judulLabel = ctk.CTkLabel(
            formWindow,
            text="[Edit Biaya Detail]",
            font=("Poppins", 35, "bold")
        )
        judulLabel.grid(row=1, column=0, padx=50, pady=20, sticky="W")

        # Entry for Nama Barang
        label1 = ctk.CTkLabel(formWindow, text="Nama Barang", font=("Poppins", 18, "bold"))
        label1.grid(row=2, column=0, padx=50, pady=5, sticky="W")
        entry1 = ctk.CTkEntry(formWindow, width=500)
        entry1.grid(row=3, column=0, padx=30, pady=10)

        # Entry for Harga Satuan
        label2 = ctk.CTkLabel(formWindow, text="Harga Satuan", font=("Poppins", 18, "bold"))
        label2.grid(row=4, column=0, padx=50, pady=5, sticky="W")
        entry2 = ctk.CTkEntry(formWindow, width=500)
        entry2.grid(row=5, column=0, padx=30, pady=10)

        # Entry for Kuantitas
        label3 = ctk.CTkLabel(formWindow, text="Kuantitas", font=("Poppins", 18, "bold"))
        label3.grid(row=6, column=0, padx=50, pady=5, sticky="W")
        entry3 = ctk.CTkEntry(formWindow, width=500)
        entry3.grid(row=7, column=0, padx=30, pady=10)

        # Textbox for Deskripsi
        label4 = ctk.CTkLabel(formWindow, text="Deskripsi", font=("Poppins", 18, "bold"))
        label4.grid(row=8, column=0, padx=50, pady=10, sticky="W")

        text_box = scrolledtext.ScrolledText(
            formWindow,
            height=5,  # Tinggi
            wrap="word",  # Bungkus kata
            font=("Poppins", 18)
        )
        text_box.grid(row=9, column=0, padx=40, pady=10, sticky="ew")  # Sticky east-west agar melebar

        # Save Button
        # save_image = Image.open("img/saveButton.png")
        # save_image = save_image.resize((150, 60))  # Ubah ukuran gambar sesuai keperluan
        # save_photo = ImageTk.PhotoImage(save_image)

        saveButton = ctk.CTkButton(
            formWindow,
            text="SAVE",  # Hapus teks karena menggunakan gambar
            command=lambda: self.saveData(entry1, entry2, entry3, text_box),
            hover_color="lightgray"
        )
        # saveButton.image = save_photo  # Penting untuk mencegah garbage collection
        saveButton.grid(row=10, column=0, pady=20, padx = 30, sticky="e")
        
    def clearForm(self):
        """Mengosongkan semua input di form."""
        for widget in self.window.winfo_children():
            if isinstance(widget, ctk.CTkEntry):
                widget.delete(0, tk.END)  # Menghapus teks di Entry
            elif isinstance(widget, scrolledtext.ScrolledText):
                widget.delete("1.0", tk.END)  # Menghapus teks di Textbox



    def saveData(self, entry1, entry2, entry3, text_box):
        # Retrieve data from entry widgets and text box
        nama_barang = entry1.get().strip()
        harga_satuan = entry2.get().strip()
        kuantitas = entry3.get().strip()
        deskripsi = text_box.get("1.0", tk.END).strip()

        try:
            # Validasi Input Numerik
            harga_satuan = int(harga_satuan)
            kuantitas = int(kuantitas)
            total_biaya = harga_satuan * kuantitas

            # Collect data into Biaya object
            newBiaya = Biaya(
                namaBarangBiaya=nama_barang,
                keteranganBiaya=deskripsi,
                hargaSatuanBiaya=harga_satuan,
                quantityBiaya=kuantitas,
                totalBiaya=total_biaya
            )

            # Save to database via controller
            success = self.controller.addBiaya(newBiaya)
            if success:
                messagebox.showinfo("Success", "Biaya berhasil ditambahkan.")
                self.clearForm()
                self.refresh_callback()  # Panggil fungsi untuk refresh tabel di GUI utama
                self.window.destroy()  # Tutup popup setelah berhasil menambahkan data
            else:
                messagebox.showerror("Error", "Gagal menambahkan Biaya.")


        except ValueError:
            messagebox.showerror("Error", "Harga Satuan dan Kuantitas harus berupa angka.")

        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

        # You can add code here to store data to a database or file



    def run(self):
        self.window.mainloop()

# Run the GUI
# if __name__ == "__main__":
#     controller = None
#     app = DisplayPop(controller)
#     app.run()
