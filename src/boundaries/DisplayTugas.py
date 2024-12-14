import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import customtkinter as ctk
from entities.TugasProyek import TugasProyek


class DisplayTugas(tk.Frame):
    def __init__(self, parent, controller, idProyekOfTugas=None, main_frame=None):
        super().__init__(parent)
        self.controller = controller
        self.main_frame = main_frame
        self.idProyekProyekOfTugas = idProyekOfTugas  # Properly initialize idProyek
        self.images = {}  # To store image references and prevent garbage collection

        # Initialize UI
        self.displayAllTugas(self.idProyekProyekOfTugas)

    def displayAllTugas(self, idProyek):
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
            command=self.open_add_tugas_window,
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

        # Display tasks for the given idProyek
        daftarTugas = self.controller.getAllTugas(idProyek)
        if not daftarTugas:
            noTaskLabel = tk.Label(scrollableFrame, text="Tidak ada tugas yang ditemukan.", font=("Arial", 12))
            noTaskLabel.pack(pady=10)
        else:
            for tugas in daftarTugas:
                self.createTaskFrame(scrollableFrame, tugas)



    def createTaskFrame(self, parent, tugas):
        """Creates a task frame that fills the entire parent container."""
        # Determine status and styling
        parent.place(relx=0, rely=0, relwidth=1, relheight=1)
        status = tugas.getStatusTugas()
        frameColor = "#FFFFFF" if status.lower() == 'done' else "#FFFFFF"
        imageFile = "img/complete.png" if status.lower() == 'done' else "img/onprogress.png"
        
        # Create main frame
        taskFrame = ttk.Frame(
            parent,
            style="Custom.TFrame"
        )
        taskFrame.pack(padx=10, pady=5, fill="x")

        # Configure style for the frame
        style = ttk.Style()
        style.configure(
            "Custom.TFrame",
            background=frameColor,
            bordercolor="#7A7E93",
            relief="ridge"
        )

        # Task Title Label
        taskNameLabel = ttk.Label(
            taskFrame,
            text=tugas.getJudulTugas(),
            font=("Calvatica", 11, "bold"),
            style="Custom.TLabel",
            cursor="hand2"
        )
        
        # Configure label style
        style.configure(
            "Custom.TLabel",
            background=frameColor,
            font=("Calvatica", 11, "bold"),
            anchor="w"
        )
        
        # Bind click event
        taskNameLabel.bind("<Button-1>", lambda event: self.displayPerTugas(tugas.idTugas))
        taskNameLabel.pack(side="left", fill="x", expand=True, padx=(10, 5))
        # Image Frame
        image_frame = tk.Frame(
        taskFrame,
        bg=frameColor,  # Set the same background color as the task frame
        relief="flat",  # No border
        width=40,  # Fixed width for the image
        height=40  # Fixed height for the image
        )
        image_frame.pack(side="right", padx=(5, 10), pady=5)

        # Add image to the frame
        self.images[f"task_{tugas.getIdTugas()}"] = ImageTk.PhotoImage(Image.open(imageFile))
        image_label = tk.Label(
            image_frame,
            image=self.images[f"task_{tugas.getIdTugas()}"],
            bg=frameColor
        )
        image_label.pack(fill="both", expand=True)

        def on_enter(e):
            taskFrame.configure(cursor="hand2")
            
        def on_leave(e):
            taskFrame.configure(cursor="")

        taskFrame.bind("<Enter>", on_enter)
        taskFrame.bind("<Leave>", on_leave)
            


    def displayPerTugas(self, idTugas):
        # Clear all existing content, including left and right frames
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a new container for the detailed task view
        taskDetailFrame = ttk.Frame(self.main_frame)
        taskDetailFrame.pack(fill=tk.BOTH, expand=True, padx=20)

        # Add your content
        taskFrame = tk.Frame(taskDetailFrame)
        taskFrame.pack(fill=tk.BOTH, expand=True, padx=20)

        tugasName = tk.Label(taskFrame, text="yesss", font=("Arial", 16, "bold"))
        tugasName.pack()



    def open_add_tugas_window(self):
        # Create a new top-level window
        add_window = tk.Toplevel()
        add_window.title("Add Tugas")
        add_window.geometry("500x600")
        add_window.configure(bg="#FFFFFF")  # Set background color

        # Back Button
        self.leftArrowButtonImg = tk.PhotoImage(file="img/left-arrow.png")
        back_button = tk.Button(
            add_window,
            image=self.leftArrowButtonImg,  # Using the class variable
            borderwidth=0,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            cursor="hand2",
            command=add_window.destroy 
        )
        back_button.pack(anchor="w", padx=(20, 0), pady=(20, 20))

        # Title label
        title_label = tk.Label(
            add_window,
            text="[Add Tugas]",
            font=("Helvetica", 20, "bold"),
            anchor="w",
            justify="left",
            bg="#FFFFFF",
            fg="black",
        )
        title_label.pack(fill="x", padx=20, pady=10)

        fields = {}
        field_names = [
            "Judul Tugas", "Deskripsi Tugas", "Biaya Tugas", "Status Tugas"
        ]
        
        for field_name in field_names:
            label = ttk.Label(add_window, text=field_name, font=("Helvetica", 14, "bold"), foreground="#4966FF", background="#FFFFFF")
            label.pack(anchor="w", padx=20, pady=(10, 5))

            container = ctk.CTkFrame(
                add_window,
                corner_radius=10,
                fg_color="#FFFFFF",
                border_width=1,
                border_color="#D3D3D3"
            )
            container.pack(fill="x", padx=20, pady=(0, 20))

            entry = tk.Entry(container, font=("Helvetica", 12), bg="#FFFFFF", bd=0, highlightthickness=0)
            entry.pack(fill="x", padx=10, pady=5)
            fields[field_name] = entry

        # Save Button
        def save_addtugas():
            try:
                # Collect data from fields
                new_tugas = TugasProyek(
                    judulTugas=fields["Judul Tugas"].get(),
                    descTugas=fields["Deskripsi Tugas"].get(),
                    biayaTugas=int(fields["Biaya Tugas"].get() or 0),
                    statusTugas=fields["Status Tugas"].get() or "Not Started",
                    idProyekOfTugas=self.idProyekProyekOfTugas
                )

                # Call the controller to save the task
                success = self.controller.addTugas(new_tugas, self.idProyekProyekOfTugas)
                if success:
                    messagebox.showinfo("Success", "Tugas berhasil ditambahkan!")
                    add_window.destroy()
                    self.refresh_tasks()
                else:
                    messagebox.showerror("Error", "Gagal menambahkan tugas.")
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        save_button = ctk.CTkButton(
            add_window,
            text="Add",
            font=("Helvetica", 16, "bold"),
            fg_color="#4966FF",
            text_color="#FFFFFF",
            hover_color="#3B53B5",
            corner_radius=5,
            width=100,
            height=40,
            command=save_addtugas
        )
        save_button.pack(side="bottom", pady=20)

        add_window.mainloop()
    
    def clear_frame(self):
        # Destroy all widgets in the current frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()



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



    def addTugas(self, idProyek):
        try:
            newTugas = TugasProyek(
                judulTugas=self.fields["Judul Tugas"].get().strip(),
                descTugas=self.fields["Deskripsi Tugas"].get("1.0", "end-1c").strip(),
                biayaTugas=int(self.fields["Biaya Tugas"].get().strip() or 0),
                statusTugas=self.fields["Status Proyek"].get().strip() or "Not Started",
                idProyekOfTugas=idProyek  # Associate task with the project
            )
            success = self.controller.addTugas(newTugas)
            if success:
                messagebox.showinfo("Success", "Tugas berhasil ditambahkan.")
                self.clearForm()
                self.displayAllTugas(idProyek)
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
                
    def refresh_tasks(self):
        """Refresh the task list by fetching updated data from the controller."""
        tugas_list = self.controller.getAllTugas(self.idProyekProyekOfTugas)  # Fetch updated tasks from the controller

        # Clear existing task cards
        for widget in self.winfo_children():
            widget.destroy()

        # Reinitialize the UI
        self.displayAllTugas(self.idProyekProyekOfTugas)


    def run(self):
        self.window.mainloop()


