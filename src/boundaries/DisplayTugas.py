import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import customtkinter as ctk
from entities.TugasProyek import TugasProyek


class DisplayTugas(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.images = {}  # To store image references and prevent garbage collection

        # Initialize UI
        self.displayAllTugas()

    def displayAllTugas(self):
        # Header
        headerFrame = tk.Frame(self, bg="#f5f5f5")
        headerFrame.pack(fill="x", pady=10, padx=10)
        
        logo = ttk.Label(headerFrame, text="ReBuilt", font=("Helvetica", 20, "bold"))
        logo.pack(side="right", padx=80, pady=50)

        judulLabel = tk.Label(headerFrame, text="[Tugas]", font=("Arial", 16, "bold"), bg="#f5f5f5")
        judulLabel.pack(side="left", padx=(0, 5))

        # Add Button
        self.images["addButton"] = ImageTk.PhotoImage(Image.open("img/addButton.png"))
        addButton = tk.Button(
            headerFrame,
            image=self.images["addButton"],
            command=self.popupFormTugas,
            bg="#f5f5f5",
            borderwidth=0
        )
        addButton.pack(side="right", pady=10)

        # Scrollable Container
        frameCanvas = tk.Frame(self)
        frameCanvas.pack(fill="both", expand=True, pady=10)

        canvas = tk.Canvas(frameCanvas)
        scrollbar = ttk.Scrollbar(frameCanvas, orient="vertical", command=canvas.yview)
        scrollableFrame = tk.Frame(canvas)

        scrollableFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Display tasks
        daftarTugas = self.controller.getAllTugas() if hasattr(self.controller, "getAllTugas") else []
        if not daftarTugas:
            noTaskLabel = tk.Label(scrollableFrame, text="Tidak ada tugas yang ditemukan.", font=("Arial", 12))
            noTaskLabel.pack(pady=10)
        else:
            for tugas in daftarTugas:
                self.createTaskFrame(scrollableFrame, tugas)

    def createTaskFrame(self, parent, tugas):
        # Determine task status and appearance
        screen_width = self.winfo_screenwidth()
        frame_width = screen_width / 2 
        status = tugas.getStatusTugas()
        frameColor = "#d4edda" if status == "done" else "#d6cde7"
        imageFile = "img/complete.png" if status == "done" else "img/onprogress.png"

        taskFrame = ttk.Frame(
            parent,
            style="TaskFrame.TFrame",  # Define a custom style
            width=frame_width - 80,  # Adjust width
            height=60
        )
        taskFrame.pack(padx=10, pady=5, fill="x")
        taskFrame.pack_propagate(False)  # Keep the frame size fixed
        
         # Apply a custom style for the task frame
        style = ttk.Style()
        style.configure(
            "TaskFrame.TFrame",
            background=frameColor,  # Set background color based on task status
            relief="ridge",
            borderwidth=2
        )

        # Task Name Label
        taskNameLabel = tk.Label(
            taskFrame,
            text=tugas.getJudulTugas(),
            font=("Arial", 11, "bold"),
            bg=frameColor,
            anchor="w",
            cursor="hand2"
        )
        taskNameLabel.bind("<Button-1>", lambda event: self.displayPerTugas(tugas))
        taskNameLabel.pack(side="left", fill="x", expand=True, padx=5)

        self.images[f"task_{tugas.getIdTugas()}"] = ImageTk.PhotoImage(Image.open(imageFile))
        imageButton = ttk.Button(
            taskFrame,
            image=self.images[f"task_{tugas.getIdTugas()}"],
            command=lambda: self.displayPerTugas(tugas),
            style="ImageButton.TButton"  # Define a custom style for image buttons
        )
        imageButton.image = self.images[f"task_{tugas.getIdTugas()}"]  # Prevent garbage collection
        imageButton.pack(side="right", padx=(5, 10), pady=5)

        # Apply a custom style for the image button
        style.configure(
            "ImageButton.TButton",
            background=frameColor,
            borderwidth=0
        )


    def displayPerTugas(self, tugas):
        # Task Details Window
        newWindow = tk.Toplevel(self)
        newWindow.title("Task Details")

        taskFrame = tk.Frame(newWindow)
        taskFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Task Name
        tugasName = tk.Label(taskFrame, text=tugas.getJudulTugas(), font=("Arial", 16, "bold"))
        tugasName.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Action Buttons
        buttonFrame = tk.Frame(taskFrame)
        buttonFrame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.images["editButton"] = ImageTk.PhotoImage(Image.open("img/editButton.png"))
        editButton = tk.Button(
            buttonFrame,
            image=self.images["editButton"],
            command=lambda: self.popupEditTugas(tugas),
            borderwidth=0
        )
        editButton.pack(side="left", padx=10)

        self.images["deleteButton"] = ImageTk.PhotoImage(Image.open("img/deleteButton.png"))
        deleteButton = tk.Button(
            buttonFrame,
            image=self.images["deleteButton"],
            command=lambda: self.popupHapus(tugas),
            borderwidth=0
        )
        deleteButton.pack(side="left", padx=10)

    def popupFormTugas(self):
        # Create a new top-level window
        edit_window = tk.Toplevel()
        edit_window.transient(self)
        edit_window.title("Add Tugas")
        edit_window.geometry("500x600")
        edit_window.configure(bg="#FFFFFF")  # Set background color

        
        self.leftArrowButtonImg = tk.PhotoImage(file="img/left-arrow.png")
        back_button = tk.Button(
            edit_window,
            image=self.leftArrowButtonImg,  # Using the class variable
            borderwidth=0,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            cursor="hand2"
        )
        back_button.pack(anchor="w", padx=(20,0), pady=(20, 20))

        # Title label
        title_label = tk.Label(
            edit_window,
            text="[Edit Proyek Detail]",
            font=("Helvetica", 20, "bold"),
            anchor="w",
            justify="left",
            bg="#FFFFFF",
            fg="black",
        )
        title_label.pack(fill="x", padx=20, pady=10)

        # Project Title Section
        project_title_label = ttk.Label(
            edit_window,
            text="Judul Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        project_title_label.pack(anchor="w", padx=20, pady=(5, 5))
        
        project_title_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,  # Border radius
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"  # Light gray border
        )
        project_title_container.pack(fill="x", padx=20, pady=(0, 5))
        
        project_title_entry = tk.Entry(
            project_title_container,
            font=("Helvetica", 12),
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
        )
        project_title_entry.pack(fill="x", padx=10, pady=5)
        
        biayaLabel = ttk.Label(
            edit_window,
            text="Biaya Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        biayaLabel.pack(anchor="w", padx=20, pady=(5, 5))
        biaya_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,  # Border radius
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"  # Light gray border
        )
        biaya_container.pack(fill="x", padx=20, pady=(0, 5))
        
        biayaEntry = tk.Entry(
            biaya_container,
            font=("Helvetica", 12),
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
        )
        biayaEntry.pack(fill="x", padx=10, pady=5)
        
        statusLabel = ttk.Label(
            edit_window,
            text="Status Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        statusLabel.pack(anchor="w", padx=20, pady=(5, 5))

        status_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,  # Border radius
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"  # Light gray border
        )
        status_container.pack(fill="x", padx=20, pady=(0, 5))
        
        
        statusEntry = tk.Entry(
            status_container,
            font=("Helvetica", 12),
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
        )
        statusEntry.pack(fill="x", padx=10, pady=5)

        # Description Section
        description_label = ttk.Label(
            edit_window,
            text="Deskripsi Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        description_label.pack(anchor="w", padx=20, pady=(5, 5))

        description_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"
        )
        description_container.pack(fill="both", padx=20, pady=(0, 5))

        description_scrollbar = tk.Scrollbar(description_container)
        description_scrollbar.pack(side="right", fill="y")
        
        description_text = tk.Text(
            description_container,
            font=("Helvetica", 12),
            wrap="word",
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
            yscrollcommand=description_scrollbar.set,
            height=6,
        )
        description_text.insert(
            "1.0",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Etiam vitae augue vitae ante feugiat placerat. Quisque pretium, "
            "nulla nec laoreet accumsan, nisl ante rhoncus ante, elementum "
            "tincidunt augue lacus posuere"
        )
        description_text.pack(fill="both", padx=10, pady=5)

        # Save Button with rounded corners
        save_button = ctk.CTkButton(
            edit_window,
            text="save",
            font=("Helvetica", 16, "bold"),
            fg_color="#4966FF",
            text_color="#FFFFFF",
            hover_color="#3B53B5",
            corner_radius=5,
            width=100,
            height=40,
            command=self.addTugas
        )
        save_button.pack(side="bottom", pady=5)
        
        # Input fields
        self.fields = {}
        self.fields["Judul Tugas"] = tk.Text(edit_window, height=1, width=40, wrap="word", font=("Calvatica", 10))
        self.fields["Judul Tugas"].grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10)

        self.fields["Biaya Tugas"] = tk.Text(edit_window, height=1, width=40, wrap="word", font=("Calvatica", 10))
        self.fields["Biaya Tugas"].grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10)

        self.fields["Status Proyek"] = tk.Text(edit_window, height=1, width=40, wrap="word", font=("Calvatica", 10))
        self.fields["Status Proyek"].grid(row=6, column=0, columnspan=2, sticky="nsew", padx=10)

        desc_frame = tk.Frame(edit_window, style="Custom.TFrame")
        desc_frame.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=10)

        self.fields["Deskripsi Tugas"] = tk.Text(desc_frame, height=8, width=40, wrap="word", font=("Calvatica", 10))
        scrollbar = tk.Scrollbar(desc_frame, orient="vertical", command=self.fields["Deskripsi Tugas"].yview)
        self.fields["Deskripsi Tugas"].configure(yscrollcommand=scrollbar.set)

        self.fields["Deskripsi Tugas"].grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        desc_frame.columnconfigure(0, weight=1)
        desc_frame.rowconfigure(0, weight=1)

        # Button save
        # try:
        #     imgSave = Image.open("img/saveButton.png")
        #     photoSave = ImageTk.PhotoImage(imgSave)
        # except FileNotFoundError:
        #     print("Save button image not found.")
        #     return

        # saveButton = ttk.Button(
        #     edit_window,
        #     image=photoSave,
        #     style="Custom.TButton",
        #     command=lambda: self.addTugas()
        # )
        # saveButton.image = photoSave
        # saveButton.grid(row=10, column=1, pady=20, sticky="e")

    def popupEditTugas(self):
        # Create a new top-level window
        edit_window = tk.Toplevel()
        edit_window.transient(self)
        edit_window.title("Add Tugas")
        edit_window.geometry("500x600")
        edit_window.configure(bg="#FFFFFF")  # Set background color

        
        self.leftArrowButtonImg = tk.PhotoImage(file="img/left-arrow.png")
        back_button = tk.Button(
            edit_window,
            image=self.leftArrowButtonImg,  # Using the class variable
            borderwidth=0,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            cursor="hand2"
        )
        back_button.pack(anchor="w", padx=(20,0), pady=(20, 20))

        # Title label
        title_label = tk.Label(
            edit_window,
            text="[Edit Proyek Detail]",
            font=("Helvetica", 20, "bold"),
            anchor="w",
            justify="left",
            bg="#FFFFFF",
            fg="black",
        )
        title_label.pack(fill="x", padx=20, pady=10)

        # Project Title Section
        project_title_label = ttk.Label(
            edit_window,
            text="Judul Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        project_title_label.pack(anchor="w", padx=20, pady=(5, 5))
        
        project_title_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,  # Border radius
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"  # Light gray border
        )
        project_title_container.pack(fill="x", padx=20, pady=(0, 5))
        
        project_title_entry = tk.Entry(
            project_title_container,
            font=("Helvetica", 12),
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
        )
        project_title_entry.insert(0, "My proyek no. 1")
        project_title_entry.pack(fill="x", padx=10, pady=5)
        
        biayaLabel = ttk.Label(
            edit_window,
            text="Biaya Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        biayaLabel.pack(anchor="w", padx=20, pady=(5, 5))
        biaya_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,  # Border radius
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"  # Light gray border
        )
        biaya_container.pack(fill="x", padx=20, pady=(0, 5))
        
        biayaEntry = tk.Entry(
            biaya_container,
            font=("Helvetica", 12),
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
        )
        biayaEntry.insert(0, "Biaya")
        biayaEntry.pack(fill="x", padx=10, pady=5)
        
        statusLabel = ttk.Label(
            edit_window,
            text="Status Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        statusLabel.pack(anchor="w", padx=20, pady=(5, 5))

        status_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,  # Border radius
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"  # Light gray border
        )
        status_container.pack(fill="x", padx=20, pady=(0, 5))
        
        
        statusEntry = tk.Entry(
            status_container,
            font=("Helvetica", 12),
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
        )
        statusEntry.insert(0, "Biaya")
        statusEntry.pack(fill="x", padx=10, pady=5)

        # Description Section
        description_label = ttk.Label(
            edit_window,
            text="Deskripsi Tugas",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        description_label.pack(anchor="w", padx=20, pady=(5, 5))

        description_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"
        )
        description_container.pack(fill="both", padx=20, pady=(0, 5))

        description_scrollbar = tk.Scrollbar(description_container)
        description_scrollbar.pack(side="right", fill="y")
        
        description_text = tk.Text(
            description_container,
            font=("Helvetica", 12),
            wrap="word",
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
            yscrollcommand=description_scrollbar.set,
            height=6,
        )
        description_text.insert(
            "1.0",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Etiam vitae augue vitae ante feugiat placerat. Quisque pretium, "
            "nulla nec laoreet accumsan, nisl ante rhoncus ante, elementum "
            "tincidunt augue lacus posuere"
        )
        description_text.pack(fill="both", padx=10, pady=5)

        # Save Button with rounded corners
        save_button = ctk.CTkButton(
            edit_window,
            text="save",
            font=("Helvetica", 16, "bold"),
            fg_color="#4966FF",
            text_color="#FFFFFF",
            hover_color="#3B53B5",
            corner_radius=5,
            width=100,
            height=40,
        )
        save_button.pack(side="bottom", pady=5)



    def addTugas(self):
        try:
            newTugas = TugasProyek(
                judulTugas=self.fields["Judul Tugas"].get("1.0", "end-1c").strip(),
                descTugas=self.fields["Deskripsi Tugas"].get().strip(),
                biayaTugas=int(self.fields["Biaya Tugas"].get("1.0", "end-1c").strip() or 0),
                statusTugas=self.fields["Status Proyek"].get("1.0", "end-1c").strip() or "Not Started"
            )
            success = self.controller.addTugas(newTugas)
            if success:
                messagebox.showinfo("Success", "Tugas berhasil ditambahkan.")
                self.clearForm()
            else:
                messagebox.showerror("Error", "Gagal menambahkan Tugas.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def clearForm(self):
        for key, widget in self.fields.items():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, tk.Text):
                widget.delete("1.0", tk.END)

    def run(self):
        self.window.mainloop()


