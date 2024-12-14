from tkinter import messagebox
import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk 
from entities.Biaya import Biaya
class DisplayPopEdit:
    def __init__(self, controller, biaya, refresh_callback):
        self.controller = controller
        self.current_biaya = biaya  # Menyimpan data biaya yang akan diedit
        self.refresh_callback = refresh_callback  # Callback untuk refresh tabel

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.window = ctk.CTk()
        self.window.configure(fg_color="#EBEBEB")

        self.displayPopEdit()

    def displayPopEdit(self):
        formWindow = ctk.CTkToplevel(self.window)
        formWindow.title("Form Edit Biaya")

        # Entry for Nama Barang
        label1 = ctk.CTkLabel(formWindow, text="Nama Barang", font=("Poppins", 18, "bold"))
        label1.grid(row=2, column=0, padx=50, pady=5, sticky="W")
        entry1 = ctk.CTkEntry(formWindow, width=500)
        entry1.insert(0, self.current_biaya.getnamaBarangBiaya())  # Isi data lama
        entry1.grid(row=3, column=0, padx=30, pady=10)

        # Entry for Harga Satuan
        label2 = ctk.CTkLabel(formWindow, text="Harga Satuan", font=("Poppins", 18, "bold"))
        label2.grid(row=4, column=0, padx=50, pady=5, sticky="W")
        entry2 = ctk.CTkEntry(formWindow, width=500)
        entry2.insert(0, self.current_biaya.gethargaSatuanBiaya())
        entry2.grid(row=5, column=0, padx=30, pady=10)

        # Entry for Kuantitas
        label3 = ctk.CTkLabel(formWindow, text="Kuantitas", font=("Poppins", 18, "bold"))
        label3.grid(row=6, column=0, padx=50, pady=5, sticky="W")
        entry3 = ctk.CTkEntry(formWindow, width=500)
        entry3.insert(0, self.current_biaya.getquantityBiaya())
        entry3.grid(row=7, column=0, padx=30, pady=10)

        # Textbox for Deskripsi
        label4 = ctk.CTkLabel(formWindow, text="Deskripsi", font=("Poppins", 18, "bold"))
        label4.grid(row=8, column=0, padx=50, pady=10, sticky="W")

        text_box = scrolledtext.ScrolledText(formWindow, height=5, wrap="word", font=("Poppins", 18))
        text_box.insert("1.0", self.current_biaya.getketeranganBiaya())
        text_box.grid(row=9, column=0, padx=40, pady=10, sticky="ew")

        # Save Button
        saveButton = ctk.CTkButton(
            formWindow,
            text="SAVE",
            command=lambda: self.saveData(entry1, entry2, entry3, text_box),
            hover_color="lightgray"
        )
        saveButton.grid(row=10, column=0, pady=20, padx=30, sticky="e")


    def saveData(self, entry1, entry2, entry3, text_box):
        try:
            # Ambil data input
            nama_barang = entry1.get().strip()
            harga_satuan = int(entry2.get().strip())
            kuantitas = int(entry3.get().strip())
            deskripsi = text_box.get("1.0", tk.END).strip()

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
            entry2.focus_set()




    def run(self):
        self.window.mainloop()

# Run the GUI
# if __name__ == "__main__":
#     controller = None
#     app = DisplayPop(controller)
#     app.run()
