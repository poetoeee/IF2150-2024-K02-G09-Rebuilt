from tkinter import messagebox
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from entities.TugasProyek import TugasProyek
from PIL import Image, ImageTk

class DisplayTugas:
    def __init__(self, controller):
        self.window = ttk.Window(themename="flatly")
        self.window.title("Tugas Management")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        half_width = screen_width // 2
        half_height = screen_height // 2
        x_position = screen_width // 4
        y_position = screen_height // 4
        self.window.geometry(f"{half_width}x{half_height}+{x_position}+{y_position}")

        self.controller = controller

        # layout
        self.displayAllTugas()

    def displayAllTugas(self):
        # header
        headerFrame = ttk.Frame(self.window)
        headerFrame.pack(fill="x", pady=10, padx=10)

        judulLabel = ttk.Label(headerFrame, text="[Tugas]", font=("Arial", 16, "bold"))
        judulLabel.pack(side="left", padx=(0, 5))

        # button Add
        style = ttk.Style()
        style.configure("Custom.TButton", background="#FFFFFF", borderwidth=0)
        style.map(
            "Custom.TButton",
            background=[("active","#FFFFFF"), ("pressed","#FFFFFF")]
        )
        image = Image.open("img/addButton.png")  
        photo = ImageTk.PhotoImage(image)

        addButton = ttk.Button(
            headerFrame,
            image=photo,
            compound="top",
            style="Custom.TButton",
            command=self.popupFormTugas
        )
        addButton.image = photo
        addButton.pack(pady=10)
        

        # Scrollable container
        frameCanvas = ttk.Frame(self.window)
        frameCanvas.pack(fill="both", expand=True, pady=10)

        canvas = ttk.Canvas(frameCanvas)
        scrollbar = ttk.Scrollbar(frameCanvas, orient="vertical", command=canvas.yview)
        scrollableFrame = ttk.Frame(canvas)

        scrollableFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # fetch all tasks untuk debugging
        daftarTugas = self.controller.getAllTugas()

        if not daftarTugas:
            noTaskLabel = ttk.Label(scrollableFrame, text="Tidak ada tugas yang ditemukan.", font=("Arial", 12), bootstyle="info")
            noTaskLabel.pack(pady=10)
        else:
            for tugas in daftarTugas:
                self.createTaskFrame(scrollableFrame, tugas)


    def createTaskFrame(self, parent, tugas):

        status = tugas.getStatusTugas()
        if status == 'done':
            frameColor = "#d4edda"  
            image = Image.open("img/complete.png")
        else:
            frameColor = "#d6cde7"  
            image = Image.open("img/onprogress.png")

        taskFrame = tk.Frame(parent, bg=frameColor, relief="ridge", borderwidth=2)
        taskFrame.pack(fill="x", padx=10, pady=5)

        # nama tugas
        taskNameLabel = tk.Label(
            taskFrame, 
            text=tugas.getJudulTugas(), 
            font=("Arial", 11, "bold"), 
            bg=frameColor, 
            anchor="w", 
            cursor="hand2"  # cursor tangan
        )

        taskNameLabel.bind("<Button-1>", lambda event: self.displayPerTugas(tugas))

        taskNameLabel.pack(side="left", fill="x", expand=True, padx=5)


        style = ttk.Style()
        style.configure("Custom.TButton", background="#FFFFFF", borderwidth=0)
        style.map(
            "Custom.TButton",
            background=[("active","#FFFFFF"), ("pressed","#FFFFFF")]
        )

        photo = ImageTk.PhotoImage(image)
        image_button = ttk.Button(
            taskFrame,
            image=photo,
            compound="top",
            style="Custom.TButton"
        )
        image_button.image = photo
        image_button.pack(side="right", padx=10, pady=5)

    def displayPerTugas(self, tugas):
        # window baru
        new_window = ttk.Toplevel(self.window)
        new_window.title("Task Details") 

        # frame konten
        taskFrame = ttk.Frame(new_window)
        taskFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # label nama tugas
        tugas_name = ttk.Label(taskFrame, text=tugas.getJudulTugas(), font=("Arial", 16, "bold"))
        tugas_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # frame tombol
        buttonFrame = ttk.Frame(taskFrame)
        buttonFrame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # button edit
        style = ttk.Style()
        style.configure("Custom.TButton", background="#FFFFFF", borderwidth=0)
        style.map("Custom.TButton", background=[("active", "#FFFFFF"), ("pressed", "#FFFFFF")])

        imgEdit = Image.open("img/editButton.png") 
        photoEdit = ImageTk.PhotoImage(imgEdit)

        editButton = ttk.Button(
            buttonFrame,
            image=photoEdit,
            compound="top",
            style="Custom.TButton",
            command=lambda: self.popupEditTugas(tugas)
        )
        editButton.image = photoEdit  
        editButton.pack(side="left", padx=10)

        # delete button
        imgDelete = Image.open("img/deleteButton.png")  
        photoDelete = ImageTk.PhotoImage(imgDelete)

        deleteButton = ttk.Button(
            buttonFrame,
            image=photoDelete,
            compound="top",
            style="Custom.TButton",
            command=lambda: self.popupHapus(tugas)
        )
        deleteButton.image = photoDelete  
        deleteButton.pack(side="left", padx=10)

        # frame untuk konten deskripsi tugas dan scrollbar
        descFrame = ttk.Frame(taskFrame)
        descFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # scrollbar
        canvas = ttk.Canvas(descFrame)
        scrollbar = ttk.Scrollbar(descFrame, orient="vertical", command=canvas.yview)
        srollFrame = ttk.Frame(canvas)

        srollFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=srollFrame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # deskripsi tugas 
        desc_label = ttk.Label(srollFrame, text=tugas.getDescTugas(), font=("Arial", 12), justify="left", wraplength=400)
        desc_label.pack(padx=10, pady=10)

        # label biaya 
        biaya_label = ttk.Label(srollFrame, text=f"Biaya: Rp {tugas.getBiayaTugas():,}", font=("Arial", 12, "bold"), anchor="w")
        biaya_label.pack(padx=10, pady=(10, 20))  

        # menempatkan scrollbar dan canvas
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        taskFrame.grid_columnconfigure(0, weight=1)
        taskFrame.grid_columnconfigure(1, weight=3)
        taskFrame.grid_rowconfigure(0, weight=1)
        taskFrame.grid_rowconfigure(1, weight=0)

        
    def popupFormTugas(self):
        # membuat jendela popup
        formWindow = ttk.Toplevel(self.window)
        formWindow.title("Form Input Tugas")  

        # header
        judulLabel = ttk.Label(formWindow, text="[Edit Tugas Detail]", font=("Arial", 16, "bold"))
        judulLabel.grid(row=0, column=0, columnspan=2, pady=10)

        # labels
        ttk.Label(formWindow, text="Judul Tugas", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(formWindow, text="Biaya", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        ttk.Label(formWindow, text="Status", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
        ttk.Label(formWindow, text="Deskripsi", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)

        # frame untuk input dan menyesuaikan panjang
        inputFrame = ttk.Frame(formWindow)
        inputFrame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.fields = {}
        self.fields["Judul Tugas"] = ttk.Entry(inputFrame, width=30)
        self.fields["Judul Tugas"].grid(row=0, column=0, padx=5)

        # frame untuk biaya
        biaya_frame = ttk.Frame(formWindow)
        biaya_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.fields["Biaya Tugas"] = ttk.Entry(biaya_frame, width=30)
        self.fields["Biaya Tugas"].grid(row=0, column=0, padx=5)

        # frame untuk status
        status_frame = ttk.Frame(formWindow)
        status_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.fields["Status Proyek"] = ttk.Entry(status_frame, width=30)
        self.fields["Status Proyek"].grid(row=0, column=0, padx=5)

        # frame untuk deskripsi
        desc_frame = ttk.Frame(formWindow)
        desc_frame.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.fields["Deskripsi Tugas"] = ttk.Text(desc_frame, height=5, width=30)
        self.fields["Deskripsi Tugas"].grid(row=0, column=0, padx=5)

        # button save
        imgSave = Image.open("img/saveButton.png")  # Ganti dengan path gambar Anda untuk tombol save
        photoSave = ImageTk.PhotoImage(imgSave)

        saveButton = ttk.Button(
            formWindow,  
            image=photoSave,
            style="Custom.TButton",
            command=lambda: self.addTugas()
        )
        saveButton.image = photoSave 
        saveButton.grid(row=5, column=1, pady=20, sticky="e")  
        

    def popupEditTugas(self, tugas):
        # membuat popup
        formWindow = ttk.Toplevel(self.window)
        formWindow.title("Form Input Tugas")  

        # header
        judulLabel = ttk.Label(formWindow, text="[Edit Tugas Detail]", font=("Arial", 16, "bold"))
        judulLabel.grid(row=0, column=0, columnspan=2, pady=10)

        # Labels
        ttk.Label(formWindow, text="Judul Tugas", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(formWindow, text="Status", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        ttk.Label(formWindow, text="Deskripsi", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)

        # frame untuk input dan menyesuaikan panjang
        inputFrame = ttk.Frame(formWindow)
        inputFrame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.fields = {}
        self.fields["Judul Tugas"] = ttk.Entry(inputFrame, width=30)
        self.fields["Judul Tugas"].grid(row=0, column=0, padx=5)

        # frame untuk status
        status_frame = ttk.Frame(formWindow)
        status_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.fields["Status Proyek"] = ttk.Entry(status_frame, width=30)
        self.fields["Status Proyek"].grid(row=0, column=0, padx=5)

        # frame untuk deskripsi
        desc_frame = ttk.Frame(formWindow)
        desc_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.fields["Deskripsi Tugas"] = ttk.Text(desc_frame, height=5, width=30)
        self.fields["Deskripsi Tugas"].grid(row=0, column=0, padx=5)

        # button save
        imgSave = Image.open("img/saveButton.png")  
        photoSave = ImageTk.PhotoImage(imgSave)

        saveButton = ttk.Button(
            formWindow,  
            image=photoSave,
            style="Custom.TButton",
            command=lambda: self.editTugas(tugas)
        )
        saveButton.image = photoSave  
        saveButton.grid(row=5, column=1, pady=20, sticky="e")  
      

    def addTugas(self):
        try:
            # collect data from form fields
            newTugas = TugasProyek(
                judulTugas=self.fields["Judul Tugas"].get().strip(),
                descTugas=self.fields["Deskripsi Tugas"].get("1.0", "end-1c").strip(),
                biayaTugas=int(self.fields["Biaya Tugas"].get().strip() or 0),
                statusTugas=self.fields["Status Proyek"].get().strip() or "Not Started"
            )

            # save to database via controller
            success = self.controller.addTugas(newTugas)
            if success:
                messagebox.showinfo("Success", "Tugas berhasil ditambahkan.")
                self.clearForm()
            else:
                messagebox.showerror("Error", "Gagal menambahkan Tugas.")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def editTugas(self, tugas):
        existingID = tugas.getIdTugas()
        try:
            existingTugas = TugasProyek(
                idTugas=existingID,
                judulTugas=self.fields["Judul Tugas"].get().strip(),
                descTugas=self.fields["Deskripsi Tugas"].get("1.0", "end-1c").strip(),
                statusTugas=self.fields["Status Proyek"].get().strip() or "Not Started",
            )


            # Save to database via controller
            success = self.controller.editTugas(existingTugas)
            if success:
                messagebox.showinfo("Success", "Tugas berhasil diperbarui.")
                self.clearForm()
            else:
                messagebox.showerror("Error", "Gagal memperbarui Tugas.")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    

    def popupHapus(self, tugas):
        
        # membuat popup 
        popupWindow = ttk.Toplevel(self.window)
        popupWindow.title("Form Input Tugas")  

        judulLabel = ttk.Label(popupWindow, text="Apakah yakin ingin menghapus tugas?", font=("Helvetica", 12))
        judulLabel.grid(row=0, column=0, pady=20, padx=15, sticky="nsew")
        
        # tidak button
        imgTidak = Image.open("img/tidakButton.png")  
        photoTidak = ImageTk.PhotoImage(imgTidak)

        tidakButton = ttk.Button(
            popupWindow,  
            image=photoTidak,
            style="Custom.TButton"
        )
        tidakButton.image = photoTidak  
        tidakButton.grid(row=1, column=0, pady=20, padx=5, sticky="ew")  

        # iyaButton
        imgIya = Image.open("img/iyaButton.png")  # Ganti dengan path gambar Anda untuk tombol Iya
        photoIya = ImageTk.PhotoImage(imgIya)

        
        iyaButton = ttk.Button(
            popupWindow, 
            image=photoIya,
            style="Custom.TButton",
            command=lambda: self.controller.deleteTugas(tugas.idTugas)
        )
        iyaButton.image = photoIya  
        iyaButton.grid(row=1, column=1, pady=20, padx=5, sticky="ew")  


    def clearForm(self):
        for key, widget in self.fields.items():
            if isinstance(widget, ttk.Entry):
                widget.delete(0, ttk.END)
            elif isinstance(widget, ttk.Text):
                widget.delete("1.0", ttk.END)

    def run(self):
        self.window.mainloop()

        