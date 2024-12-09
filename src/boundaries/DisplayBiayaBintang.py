from tkinter import messagebox
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from entities.Biaya import Biaya
from PIL import Image, ImageTk


class DisplayBiaya:
    def __init__(self, controller):
        self.window = ttk.Window(themename="flatly")
        self.window.title("Tugas Management")
        
        # Atur jendela menjadi fullscreen
        self.window.state('zoomed')  # Untuk Windows
        # Untuk Linux atau macOS, gunakan self.window.attributes('-zoomed', True)

        self.controller = controller

        # Layout
        self.displayAllBiaya()
    
    def displayAllTugas(self):
    # Dapatkan ukuran layar penuh
        screen_width = self.window.winfo_screenwidth()
        halfScreenWidth = screen_width // 2

        # Membuat frame utama untuk setengah layar kanan
        mainFrame = ttk.Frame(self.window, padding=10, width=halfScreenWidth)
        mainFrame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)  # Letakkan frame di setengah layar kanan

        # Frame untuk header (judul dan tombol Add)
        headerFrame = ttk.Frame(mainFrame)
        headerFrame.pack(fill="x", pady=10)

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

        status = tugas.getStatusTugas()
        if status == 'done':
            frameColor = "#d4edda"  # Hijau muda untuk "On Progress"
            image = Image.open("img/complete.png")
        else:
            frameColor = "#d6cde7"  # Ungu muda untuk "Completed"
            image = Image.open("img/onprogress.png")

        # Buat frame untuk tugas
        taskFrame = tk.Frame(parent, bg=frameColor, relief="ridge", borderwidth=2)
        taskFrame.pack(fill="x", padx=10, pady=5)

        # Nama tugas
        taskNameLabel = tk.Label(
            taskFrame, 
            text=tugas.getJudulTugas(), 
            font=("Arial", 11, "bold"), 
            bg=frameColor, 
            anchor="w", 
            cursor="hand2"  # Menambahkan cursor tangan untuk menandakan label bisa diklik
        )

        # Menambahkan event binding untuk mengklik label
        taskNameLabel.bind("<Button-1>", lambda event: self.displayPerTugas(tugas))

        taskNameLabel.pack(side="left", fill="x", expand=True, padx=(10, 300))


        style = ttk.Style()
        style.configure("Custom.TButton", background="#FFFFFF", borderwidth=0)
        style.map(
            "Custom.TButton",
            background=[("active","#FFFFFF"), ("pressed","#FFFFFF")]
        )
        # Ganti dengan path gambar Anda
        photo = ImageTk.PhotoImage(image)
        image_button = ttk.Button(
            taskFrame,
            image=photo,
            compound="center",
            style="Custom.TButton"
        )
        image_button.image = photo
        image_button.pack(side="right", padx=(270, 10), pady=5)