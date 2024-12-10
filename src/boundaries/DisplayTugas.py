from tkinter import messagebox
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from entities.TugasProyek import TugasProyek
from PIL import Image, ImageTk

class DisplayTugas:
    def __init__(self, controller):
        # Membuat window utama
        self.window = ttk.Window(themename="flatly")
        self.window.title("Tugas Management")
        
        # Atur jendela menjadi fullscreen
        self.window.state('zoomed')  # Untuk Windows
        # Untuk Linux atau macOS, gunakan self.window.attributes('-zoomed', True)

        self.controller = controller

        # Layout
        self.displayAllTugas()

    def displayAllTugas(self):
    # Dapatkan ukuran layar penuh
        full = ttk.Frame(self.window)
        full.place(relx=0, rely=0, relwidth=1, relheight=1)

        screen_width = self.window.winfo_screenwidth()
        halfScreenWidth = screen_width // 2

        # Membuat frame utama untuk setengah layar kanan
        mainFrame = ttk.Frame(full, padding=10, width=halfScreenWidth)
        mainFrame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)  # Letakkan frame di setengah layar kanan

        # Frame untuk header (judul dan tombol Add)
        headerFrame = ttk.Frame(mainFrame)
        headerFrame.pack(fill="x", pady=10)

        logo = ttk.Label(headerFrame, text="ReBuilt", font=("Arial", 16, "bold"))
        logo.pack(side="right", padx=80, pady=50)

        # Menambahkan label untuk nama tugas di headerFrame
        judulLabel = ttk.Label(headerFrame, text="[Tugas]", font=("Arial", 16, "bold"))
        judulLabel.pack(side="left", padx=5, pady=(120, 40))

        style = ttk.Style()
        style.configure("Custom.TButton", background="#FFFFFF", borderwidth=0)
        style.map("Custom.TButton", background=[("active", "#FFFFFF"), ("pressed", "#FFFFFF")])

        # Tombol Add di header
        image = Image.open("img/addButton.png")  # Ganti dengan path gambar Anda
        photo = ImageTk.PhotoImage(image)
        image_button = ttk.Button(
            headerFrame,
            image=photo,
            style="Custom.TButton",
            command=self.popupFormTugas
        )
        image_button.image = photo
        image_button.pack(side="left", padx=5, pady=(120, 40))

        # Frame untuk daftar tugas dengan scrollbar
        listContainer = ttk.Frame(mainFrame)
        listContainer.pack(fill="both", expand=True, pady=10)

        # Canvas untuk daftar tugas
        canvas = tk.Canvas(listContainer)
        canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar untuk canvas
        scrollbar = ttk.Scrollbar(listContainer, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Hubungkan scrollbar dengan canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame di dalam canvas untuk isi daftar tugas
        tasksFrame = ttk.Frame(canvas)

        # Buat frame tasksFrame bisa di-scroll
        canvas.create_window((0, 0), window=tasksFrame, anchor="nw")

        # Perbarui ukuran canvas agar sesuai dengan isi tasksFrame
        def onFrameConfigure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        tasksFrame.bind("<Configure>", onFrameConfigure)

        # Fetch all tasks
        daftarTugas = self.controller.getAllTugas()

        if not daftarTugas:
            noTaskLabel = ttk.Label(tasksFrame, text="Tidak ada tugas yang ditemukan.", font=("Arial", 12), bootstyle="info")
            noTaskLabel.pack(pady=10)
        else:
            for tugas in daftarTugas:
                self.createTaskFrame(tasksFrame, tugas)


    def createTaskFrame(self, parent, tugas):
        screen_width = self.window.winfo_screenwidth()
        frame_width = screen_width / 2  # Lebar frame setengah dari lebar layar
        status = tugas.getStatusTugas()
        
        if status == 'done':
            frameColor = "#d4edda"
            image = Image.open("img/complete.png")
        else:
            frameColor = "#d6cde7"
            image = Image.open("img/onprogress.png")
        
        taskFrame = tk.Frame(
            parent, 
            bg=frameColor, 
            relief="ridge", 
            borderwidth=2, 
            width=frame_width - 80,  # Menggunakan lebar yang sudah dihitung
            height=60
        )
        taskFrame.pack(padx=10, pady=5, fill="x")
        taskFrame.pack_propagate(False)  # Pertahankan ukuran frame
        
        taskNameLabel = tk.Label(
            taskFrame, 
            text=tugas.getJudulTugas(), 
            font=("Arial", 11, "bold"), 
            bg=frameColor, 
            anchor="w", 
            cursor="hand2"
        )
        taskNameLabel.bind("<Button-1>", lambda event: self.displayPerTugas(tugas))
        taskNameLabel.pack(side="left", fill="x", expand=True, padx=(10, 5))
        
        style = ttk.Style()
        style.configure("Custom.TButton", background="#FFFFFF", borderwidth=0)
        style.map(
            "Custom.TButton", 
            background=[("active", "#FFFFFF"), ("pressed", "#FFFFFF")]
        )
        
        photo = ImageTk.PhotoImage(image)
        image_button = ttk.Button(
            taskFrame, 
            image=photo, 
            compound="center", 
            style="Custom.TButton", 
            command=lambda: self.someButtonAction(tugas)
        )
        image_button.image = photo
        image_button.pack(side="right", padx=(5, 10), pady=5)

    def displayPerTugas(self, tugas):
        full = ttk.Frame(self.window)
        full.place(relx=0, rely=0, relwidth=1, relheight=1)

        screenHeight = self.window.winfo_screenheight()
        screenWidth = self.window.winfo_screenwidth()
        mainFrameHeight = int(screenHeight * 0.4)  # 40% dari tinggi layar

        # Membuat frame utama untuk layar penuh
        mainFrame = ttk.Frame(full, padding=10, height=mainFrameHeight, width=screenWidth)
        mainFrame.place(relx=0, rely=0, relwidth=1, relheight=0.4)

        headerFrame = ttk.Frame(mainFrame)
        headerFrame.grid(row=0, column=12, padx=(450, 10), pady=(30,10), sticky="nw")

        logo = ttk.Label(headerFrame, text="ReBuilt", font=("Arial", 16, "bold"))
        logo.pack(side="right", padx=80, pady=50)

        # Tombol back di bagian atas kiri
        imgBack = Image.open("img/back.png")
        photoBack = ImageTk.PhotoImage(imgBack)
        backButton = ttk.Button(
            mainFrame,
            image=photoBack,
            compound="top",
            style="Custom.TButton",
            command=lambda: self.displayAllTugas()
        )
        backButton.image = photoBack
        backButton.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Menambahkan label untuk nama tugas
        tugas_name = ttk.Label(mainFrame, text=tugas.getJudulTugas(), font=("Arial", 16, "bold"))
        tugas_name.grid(row=1, column=0, columnspan=2, padx=50, pady=(10, 20), sticky="w")

        # Membuat frame untuk tombol (edit & delete)
        buttonFrame = ttk.Frame(mainFrame)
        buttonFrame.grid(row=3, column=0, padx=10, pady=(40, 5), sticky="nw")

        # Button edit
        image_edit = Image.open("img/editButton.png")
        photo_edit = ImageTk.PhotoImage(image_edit)
        edit_button = ttk.Button(
            buttonFrame,
            image=photo_edit,
            compound="top",
            style="Custom.TButton",
            command=lambda: self.popupEditTugas(tugas)
        )
        edit_button.image = photo_edit
        edit_button.pack(side="left", padx=10)

        # Button delete
        image_delete = Image.open("img/deleteButton.png")
        photo_delete = ImageTk.PhotoImage(image_delete)
        delete_button = ttk.Button(
            buttonFrame,
            image=photo_delete,
            compound="top",
            style="Custom.TButton",
            command=lambda: self.popupHapus(tugas)
        )
        delete_button.image = photo_delete
        delete_button.pack(side="left", padx=10)

        # Membuat frame untuk deskripsi tugas dan biaya
        desc_frame = ttk.Frame(mainFrame)
        desc_frame.grid(row=1, column=3, padx=(300, 10), pady=10, sticky="nsew")

        # Menambahkan deskripsi tugas
        desc_label = ttk.Label(desc_frame, text=tugas.getDescTugas(), font=("Arial", 12), justify="left", wraplength=600)
        desc_label.pack(fill="both", expand=True, padx=10, pady=10)

        biayaFrame = ttk.Frame(mainFrame)
        biayaFrame.grid(row=3, column=3, padx=(300,10), pady=10, sticky="nsew")

        # Menambahkan label biaya di bawah deskripsi tugas
        biaya_label = ttk.Label(biayaFrame, text=f"Biaya: Rp {tugas.getBiayaTugas():,}", font=("Arial", 12, "bold"), anchor="w")
        biaya_label.pack(fill="x", padx=10, pady=(0, 10))

        # Frame status
        statusFrame = ttk.Frame(mainFrame)
        statusFrame.grid(row=3, column=5, padx=50, pady=10, sticky="nsew")

        # Status
        status = tugas.getStatusTugas()
        if status == 'done':
            image = Image.open("img/complete.png")
        else:
            image = Image.open("img/onprogress.png")

        style = ttk.Style()
        style.configure("Custom.TButton", background="#FFFFFF", borderwidth=0)
        style.map(
            "Custom.TButton",
            background=[("active","#FFFFFF"), ("pressed","#FFFFFF")]
        )
        photo = ImageTk.PhotoImage(image)
        image_button = ttk.Button(
            statusFrame,
            image=photo,
            compound="center",
            style="Custom.TButton"
        )
        image_button.image = photo
        image_button.pack(side="right", padx=10, pady=5)


        
    def popupFormTugas(self):
        # Dapatkan ukuran layar
        screenHeight = self.window.winfo_screenheight()
        screenWidth = self.window.winfo_screenwidth()

        # Hitung posisi dan ukuran frame utama
        frame_width = 675
        frame_height = 900
        frame_x = (screenWidth - frame_width) // 2  # Posisi x di tengah layar
        frame_y = (screenHeight - frame_height) // 2  # Posisi y di tengah layar

        style = ttk.Style()
        style.configure(
            "Custom.TFrame",  # Nama style
            relief="ridge",  # Jenis border
            borderwidth=2     # Lebar border
        )

        # Membuat frame utama
        form_window = ttk.Frame(self.window, padding=10, height=frame_height, width=frame_width, style="Custom.TFrame")
        form_window.place(x=frame_x, y=frame_y)
        # Membuat jendela popup baru (Toplevel)
        
        # Tombol back di bagian atas kiri
        imgBack = Image.open("img/back.png")
        photoBack = ImageTk.PhotoImage(imgBack)
        backButton = ttk.Button(
            form_window,
            image=photoBack,
            compound="top",
            style="Custom.TButton",
            command=lambda: self.displayAllTugas()
        )
        backButton.image = photoBack
        backButton.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Header
        judulLabel = ttk.Label(form_window, text="[Add Tugas]", font=("Arial", 16, "bold"))
        judulLabel.grid(row=0, column=0, columnspan=2, pady=10)

        # Labels
        ttk.Label(form_window, text="Judul Tugas", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(form_window, text="Biaya", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        ttk.Label(form_window, text="Status", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
        ttk.Label(form_window, text="Deskripsi", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)

        # Frame untuk input dan menyesuaikan panjang
        input_frame = ttk.Frame(form_window)
        input_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.fields = {}
        self.fields["Judul Tugas"] = ttk.Entry(input_frame, width=30)
        self.fields["Judul Tugas"].grid(row=0, column=0, padx=5)

        # Frame untuk biaya
        biaya_frame = ttk.Frame(form_window)
        biaya_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.fields["Biaya Tugas"] = ttk.Entry(biaya_frame, width=30)
        self.fields["Biaya Tugas"].grid(row=0, column=0, padx=5)

        # Frame untuk status
        status_frame = ttk.Frame(form_window)
        status_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.fields["Status Proyek"] = ttk.Entry(status_frame, width=30)
        self.fields["Status Proyek"].grid(row=0, column=0, padx=5)

        # Frame untuk deskripsi
        desc_frame = ttk.Frame(form_window)
        desc_frame.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.fields["Deskripsi Tugas"] = ttk.Text(desc_frame, height=5, width=30)
        self.fields["Deskripsi Tugas"].grid(row=0, column=0, padx=5)

        # Button save
        imgSave = Image.open("img/saveButton.png")  # Ganti dengan path gambar Anda untuk tombol save
        photoSave = ImageTk.PhotoImage(imgSave)

        # Membuat button save dengan gambar
        saveButton = ttk.Button(
            form_window,  # Pastikan tombol berada di dalam form_window (popup)
            image=photoSave,
            style="Custom.TButton",
            command=lambda: self.addTugas()
        )
        saveButton.image = photoSave  # Menyimpan referensi gambar
        saveButton.grid(row=5, column=1, pady=20, sticky="e")  # Menambahkan tombol di grid dengan penataan
        

    def popupEditTugas(self, tugas):
        # Dapatkan ukuran layar
        screenHeight = self.window.winfo_screenheight()
        screenWidth = self.window.winfo_screenwidth()

        # Hitung posisi dan ukuran frame utama
        frame_width = 675
        frame_height = 900
        frame_x = (screenWidth - frame_width) // 2  # Posisi x di tengah layar
        frame_y = (screenHeight - frame_height) // 2  # Posisi y di tengah layar

        style = ttk.Style()
        style.configure(
            "Custom.TFrame",  # Nama style
            relief="ridge",  # Jenis border
            borderwidth=2     # Lebar border
        )

        # Membuat frame utama
        form_window = ttk.Frame(self.window, padding=10, height=frame_height, width=frame_width, style="Custom.TFrame")
        form_window.place(x=frame_x, y=frame_y)
        
        # Tombol back di bagian atas kiri
        imgBack = Image.open("img/back.png")
        photoBack = ImageTk.PhotoImage(imgBack)
        backButton = ttk.Button(
            form_window,
            image=photoBack,
            compound="top",
            style="Custom.TButton",
            command=lambda: self.displayPerTugas(tugas)
        )
        backButton.image = photoBack
        backButton.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Header
        judulLabel = ttk.Label(form_window, text="[Edit Tugas Detail]", font=("Arial", 16, "bold"))
        judulLabel.grid(row=0, column=0, columnspan=2, pady=10)

        # Labels
        ttk.Label(form_window, text="Judul Tugas", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(form_window, text="Status", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        ttk.Label(form_window, text="Deskripsi", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)

        # Frame untuk input dan menyesuaikan panjang
        input_frame = ttk.Frame(form_window)
        input_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.fields = {}
        self.fields["Judul Tugas"] = ttk.Entry(input_frame, width=30)
        self.fields["Judul Tugas"].grid(row=0, column=0, padx=5)

        # Frame untuk status
        status_frame = ttk.Frame(form_window)
        status_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.fields["Status Proyek"] = ttk.Entry(status_frame, width=30)
        self.fields["Status Proyek"].grid(row=0, column=0, padx=5)

        # Frame untuk deskripsi
        desc_frame = ttk.Frame(form_window)
        desc_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.fields["Deskripsi Tugas"] = ttk.Text(desc_frame, height=5, width=30)
        self.fields["Deskripsi Tugas"].grid(row=0, column=0, padx=5)

        # Button save
        imgSave = Image.open("img/saveButton.png")  # Ganti dengan path gambar Anda untuk tombol save
        photoSave = ImageTk.PhotoImage(imgSave)

        # Membuat button save dengan gambar
        saveButton = ttk.Button(
            form_window,  # Pastikan tombol berada di dalam form_window (popup)
            image=photoSave,
            style="Custom.TButton",
            command=lambda: self.editTugas(tugas)
        )
        saveButton.image = photoSave  # Menyimpan referensi gambar
        saveButton.grid(row=5, column=1, pady=20, sticky="e")  # Menambahkan tombol di grid dengan penataan
      

    def addTugas(self):
        try:
            # Collect data from form fields
            newTugas = TugasProyek(
                judulTugas=self.fields["Judul Tugas"].get().strip(),
                descTugas=self.fields["Deskripsi Tugas"].get("1.0", "end-1c").strip(),
                biayaTugas=int(self.fields["Biaya Tugas"].get().strip() or 0),
                statusTugas=self.fields["Status Proyek"].get().strip() or "Not Started"
            )

            # Save to database via controller
            success = self.controller.addTugas(newTugas)
            if success:
                messagebox.showinfo("Success", "Tugas berhasil ditambahkan.")
                self.clearForm()
                self.displayAllTugas()

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
                self.displayAllTugas()

            else:
                messagebox.showerror("Error", "Gagal memperbarui Tugas.")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    

    def popupHapus(self, tugas):

        # Dapatkan ukuran layar
        screenHeight = self.window.winfo_screenheight()
        screenWidth = self.window.winfo_screenwidth()

        # Hitung posisi dan ukuran frame utama
        frame_width = 675
        frame_height = 900
        frame_x = (screenWidth - frame_width) // 2  # Posisi x di tengah layar
        frame_y = (screenHeight - frame_height) // 2  # Posisi y di tengah layar

        style = ttk.Style()
        style.configure(
            "Custom.TFrame",  # Nama style
            relief="ridge",  # Jenis border
            borderwidth=2     # Lebar border
        )

        # Membuat frame utama
        popupWindow = ttk.Frame(self.window, padding=10, height=frame_height, width=frame_width, style="Custom.TFrame")
        popupWindow.place(x=frame_x, y=frame_y)

        # Label judul, posisikan di tengah
        judulLabel = ttk.Label(popupWindow, text="Apakah yakin ingin menghapus tugas?", font=("Helvetica", 12))
        judulLabel.grid(row=0, column=0, columnspan=2, pady=20, padx=15, sticky="nsew")  # Memastikan label menggunakan dua kolom untuk tengah

        # Mengatur agar grid di popupWindow mendukung tata letak dinamis
        popupWindow.grid_rowconfigure(0, weight=1)
        popupWindow.grid_columnconfigure(0, weight=1)
        popupWindow.grid_columnconfigure(1, weight=1)

        ## Tombol Tidak
        imgTidak = Image.open("img/tidakButton.png")  # Ganti dengan path gambar Anda untuk tombol Tidak
        photoTidak = ImageTk.PhotoImage(imgTidak)

        # Membuat button Tidak dengan gambar
        tidakButton = ttk.Button(
            popupWindow,  # Tombol berada di dalam popupHapus
            image=photoTidak,
            compound="center",
            style="Custom.TButton",
            command=lambda: self.displayPerTugas(tugas)

        )
        tidakButton.image = photoTidak  # Menyimpan referensi gambar
        tidakButton.grid(row=1, column=0, pady=20, padx=5, sticky="ew")  # Tombol di baris 1 dan kolom 0

        ## Tombol Iya
        imgIya = Image.open("img/iyaButton.png")  # Ganti dengan path gambar Anda untuk tombol Iya
        photoIya = ImageTk.PhotoImage(imgIya)

        # Membuat button Iya dengan gambar
        iyaButton = ttk.Button(
            popupWindow, 
            image=photoIya,
            style="Custom.TButton",
            command=lambda: self.hapusTugas(tugas.idTugas)
        )
        iyaButton.image = photoIya  # Menyimpan referensi gambar
        iyaButton.grid(row=1, column=1, pady=(20), padx=5, sticky="ew")
        

    def hapusTugas(self, idTugas):
        success = self.controller.deleteTugas(idTugas)
        if success:
            messagebox.showinfo("Success", "Tugas berhasil dihapus.")
            self.clearForm()
            self.displayAllTugas()
        else:
            messagebox.showerror("Error", "Gagal menghapus tugas.")


    def clearForm(self):
        for key, widget in self.fields.items():
            if isinstance(widget, ttk.Entry):
                widget.delete(0, ttk.END)
            elif isinstance(widget, ttk.Text):
                widget.delete("1.0", ttk.END)

    def run(self):
        self.window.mainloop()

        

if __name__ == "__main__":
    from controllers.PengelolaTugasProyek import PengelolaTugasProyek

    # Initialize the controller
    controller = PengelolaTugasProyek()

    # Initialize and run the UI
    app = DisplayTugas(controller)
    app.run()