import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import customtkinter as ctk
from entities.TugasProyek import TugasProyek
from boundaries.DisplayBiaya import DisplayBiaya  # Import DisplayBiaya


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

    def go_back_to_display_proyek_by_id(self):
        """
        Transitions back to DisplayProyekById from DisplayTugas.
        """
        # First, safely remove CustomTkinter widgets if any exist
        for widget in self.main_frame.winfo_children():
            if 'CTk' in widget.__class__.__name__:  # Check if it's a CustomTkinter widget
                widget.after_cancel('check_dpi_scaling')  # Cancel any pending scaling checks
                widget.after_cancel('update')  # Cancel any pending updates
            widget.destroy()
        
        # Get the root window
        root = self.winfo_toplevel()
        
        # Schedule the reload after the current event completes
        root.after(10, lambda: self._reload_proyek_view())

    def _reload_proyek_view(self):
        """
        Helper method to reload the project view safely
        """
        # Get the root window
        root = self.winfo_toplevel()
        
        # Find the main application instance
        main_app = None
        for widget in root.winfo_children():
            if hasattr(widget, 'displayProyekById'):
                main_app = widget
                break
        
        if main_app:
            main_app.displayProyekById(self.idProyekProyekOfTugas)
        else:
            print("Could not find DisplayProyekById instance")
        
    def displayPerTugas(self, idTugas):
        tugas = self.controller.getTugasById(idTugas)
        print(idTugas)

        if not tugas:
            print("Tugas not found.")
            return

        # Clear all existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a container for the task view
        taskDetailFrame = tk.Frame(self.main_frame, bg="#FFFFFF")
        taskDetailFrame.pack(fill=tk.BOTH, expand=True)

        # Configure grid layout to split into two halves
        taskDetailFrame.rowconfigure(0, weight=1)  # Top frame
        taskDetailFrame.rowconfigure(1, weight=5)  # Bottom frame
        taskDetailFrame.columnconfigure(0, weight=1)

        # Create the top frame
        topFrame = tk.Frame(taskDetailFrame, bg="#FFFFFF")
        topFrame.grid(row=0, column=0, sticky="nsew", pady=(0,50))  # Removed padx and pady

        # Configure grid for topFrame (1 row, 2 columns)
        topFrame.rowconfigure(0, weight=1)
        topFrame.columnconfigure(0, weight=1)  # Left part
        topFrame.columnconfigure(1, weight=1)  # Right part

        # Left Frame
        leftFrame = tk.Frame(topFrame, bg="#FFFFFF")
        leftFrame.grid(row=0, column=0, sticky="nsew")

        # Right Frame
        rightFrame = tk.Frame(topFrame, bg="#FFFFFF")
        rightFrame.grid(row=0, column=1, sticky="nsew")

        # --- Left Frame Content ---
        # Back Button
        # Create and configure the style
        style = ttk.Style()
        style.configure(
            "Back.TButton",
            font=("Helvetica", 12, "bold")
        )

        # Create the button using the style
        back_button = ttk.Button(
            leftFrame,
            text="← Back",
            style="Back.TButton",
            command=lambda: self.go_back_to_display_proyek_by_id()
        )
        back_button.pack(anchor="w", pady=5)
        

        # Task Title
        tugasTitle = tk.Label(
            leftFrame,
            text=f"[{tugas.judulTugas}]",
            font=("Helvetica", 18, "bold"),
            fg="#4966FF",
            bg="#FFFFFF",
        )
        tugasTitle.pack(anchor="w", pady=(40, 5), padx=(50, 5))

        # Buttons for delete and edit
        buttonsFrame = tk.Frame(leftFrame, bg="#FFFFFF")
        buttonsFrame.pack(anchor="w", pady=5)

        self.deleteProyekImgButton = tk.PhotoImage(file="img/deleteProyek.png")
        self.editProyekImgButton = tk.PhotoImage(file="img/editProyek.png")
        deleteButton = tk.Button(
            buttonsFrame,
            image=self.deleteProyekImgButton,  # Using the instance variable
            borderwidth=0,
            padx=10,
            pady=5,
            relief="flat",
            cursor="hand2",
            command=lambda: self.popupDeleteTugas(idTugas),
        )
        deleteButton.pack(side=tk.LEFT, padx=5)

        editButton = tk.Button(
            buttonsFrame,
            image=self.editProyekImgButton,  # Using the instance variable
            borderwidth=0,
            padx=10,
            pady=5,
            relief="flat",
            cursor="hand2",
            command=lambda: self.popupEditTugas(idTugas),
        )
        editButton.pack(side=tk.LEFT, padx=5)

        # --- Right Frame Content ---
        rebuiltLabel = tk.Label(
            rightFrame,
            text="Rebuilt",
            font=("Helvetica", 20, "bold"),
            bg="#FFFFFF",
            fg="#000000",
        )
        rebuiltLabel.pack(anchor="e", pady=(10, 5))

        # Task Description
        descLabel = tk.Label(
            rightFrame,
            text=tugas.descTugas,
            font=("Helvetica", 12),
            wraplength=400,
            justify="left",
            bg="#FFFFFF",
        )
        descLabel.pack(anchor="e", pady=5, padx=30)

        # Total Cost
        totalCostFrame = tk.Frame(rightFrame, bg="#FFFFFF")
        totalCostFrame.pack(anchor="e", pady=5)

        totalCostLabel = tk.Label(
            totalCostFrame,
            text="Total Pengeluaran:",
            font=("Helvetica", 12, "bold"),
            bg="#FFFFFF",
        )
        totalCostLabel.pack(side=tk.LEFT, padx=5)

        totalCostValue = tk.Label(
            totalCostFrame,
            text=f"Rp{tugas.biayaTugas:,.2f}",
            font=("Helvetica", 20, "bold"),
            fg="#4966FF",
            bg="#FFFFFF",
        )
        totalCostValue.pack(side=tk.LEFT, padx=30, pady=(50, 5))

        # Task Status
        # Task Status
        status = tugas.getStatusTugas()
        imageFile = "img/complete.png" if status.lower() == 'done' else "img/onprogress.png"

        # Ensure the PhotoImage instance is saved as an instance variable to prevent garbage collection
        self.gambarTugas = tk.PhotoImage(file=imageFile)

        statusButton = tk.Button(
            rightFrame,
            image=self.gambarTugas,  # Assign the image
            borderwidth=0,
            padx=10,
            pady=5,
            relief="flat",
            cursor="hand2",
        )
        statusButton.pack(anchor="e", pady=5, padx=30)


        # Create the bottom frame for DisplayBiaya
        bottomFrame = tk.Frame(taskDetailFrame, bg="#FFEEDD")
        bottomFrame.grid(row=1, column=0, columnspan=2, sticky="nsew")  # Use grid to span across columns

        # Configure row and column weights to allow resizing
        taskDetailFrame.rowconfigure(1, weight=1)
        taskDetailFrame.columnconfigure(0, weight=1)

        # Load DisplayBiaya for the specific tugas
        self.load_display_biaya(bottomFrame, idTugas)
    
    def load_display_biaya(self, parent, idTugas):
        """
        Loads the DisplayBiaya frame into the provided parent frame.
        """
        # Initialize DisplayBiaya and load it into the parent frame
        display_biaya = DisplayBiaya(parent, idTugas)
        display_biaya.create_biaya_section()


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



    def popupEditTugas(self, idTugas):
        tugas = self.controller.getTugasById(idTugas)
        if not tugas:
            messagebox.showerror("Error", "Tugas not found.")
            return

        # Create a new top-level window
        editTugasWindow = tk.Toplevel()
        editTugasWindow.title("Edit Tugas")
        editTugasWindow.geometry("500x600")
        editTugasWindow.configure(bg="#FFFFFF")  # Set background color

        # Back Button
        self.leftArrowButtonImg = tk.PhotoImage(file="img/left-arrow.png")
        back_button = tk.Button(
            editTugasWindow,
            image=self.leftArrowButtonImg,
            borderwidth=0,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            cursor="hand2",
            command=editTugasWindow.destroy
        )
        back_button.pack(anchor="w", padx=(20, 0), pady=(20, 20))

        # Title label
        title_label = tk.Label(
            editTugasWindow,
            text="[Edit Tugas]",
            font=("Helvetica", 20, "bold"),
            anchor="w",
            justify="left",
            bg="#FFFFFF",
            fg="black",
        )
        title_label.pack(fill="x", padx=20, pady=10)

        fields = {}
        field_names = ["Judul Tugas", "Deskripsi Tugas", "Status Tugas"]

        # Prepopulate fields with existing data
        for field_name in field_names:
            label = ttk.Label(editTugasWindow, text=field_name, font=("Helvetica", 14, "bold"), foreground="#4966FF", background="#FFFFFF")
            label.pack(anchor="w", padx=20, pady=(10, 5))

            container = ctk.CTkFrame(
                editTugasWindow,
                corner_radius=10,
                fg_color="#FFFFFF",
                border_width=1,
                border_color="#D3D3D3"
            )
            container.pack(fill="x", padx=20, pady=(0, 20))

            entry = tk.Entry(container, font=("Helvetica", 12), bg="#FFFFFF", bd=0, highlightthickness=0)
            entry.pack(fill="x", padx=10, pady=5)

            # Pre-fill fields with existing data
            if field_name == "Judul Tugas":
                entry.insert(0, tugas.getJudulTugas())
            elif field_name == "Deskripsi Tugas":
                entry.insert(0, tugas.getDescTugas())
            elif field_name == "Status Tugas":
                entry.insert(0, tugas.getStatusTugas())

            fields[field_name] = entry

        def save_edit_tugas():
            try:
                # Collect data from fields
                edited_tugas = TugasProyek(
                    idTugas=idTugas,  # Include idTugas for updating
                    judulTugas=fields["Judul Tugas"].get(),
                    descTugas=fields["Deskripsi Tugas"].get(),
                    biayaTugas=tugas.getBiayaTugas(),  # Retain existing biayaTugas
                    statusTugas=fields["Status Tugas"].get() or "Not Started",
                    idProyekOfTugas=tugas.getIdProyekOfTugas()  # Retain existing idProyekOfTugas
                )

                # Call the controller to save the task
                success = self.controller.editTugas(edited_tugas)
                if success:
                    messagebox.showinfo("Success", "Tugas berhasil dirubah!")
                    editTugasWindow.destroy()
                    self.refresh_tasks()
                else:
                    messagebox.showerror("Error", "Gagal mengedit tugas.")
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        save_button = ctk.CTkButton(
            editTugasWindow,
            text="Save",
            font=("Helvetica", 16, "bold"),
            fg_color="#4966FF",
            text_color="#FFFFFF",
            hover_color="#3B53B5",
            corner_radius=5,
            width=100,
            height=40,
            command=save_edit_tugas
        )
        save_button.pack(side="bottom", pady=20)
        editTugasWindow.mainloop()


    def popupDeleteTugas(self, idTugas):
        # Create a new top-level window
        delete_window = tk.Toplevel()
        delete_window.title("Delete Confirmation")
        delete_window.geometry("400x250")
        delete_window.configure(bg="#FFFFFF")  # Set background color

        self.trashIcon = "img/trash.png"        
        self.trashImage = tk.PhotoImage(file=self.trashIcon)

        trash_label = tk.Label(
            delete_window,
            image=self.trashImage,
            bg="#FFFFFF"
        )

        trash_label.pack(pady=(30, 10))

        # Add confirmation text
        confirmation_label = tk.Label(
            delete_window,
            text="Yakin ingin menghapus?",
            font=("Helvetica", 14, "bold"),
            bg="#FFFFFF",
            fg="#000000"
        )
        confirmation_label.pack(pady=(10, 20))

        # Button frame
        button_frame = tk.Frame(delete_window, bg="#FFFFFF")
        button_frame.pack(pady=(10, 10))

        # "Tidak" (No) button
        no_button = ctk.CTkButton(
            button_frame,
            text="Tidak",
            font=("Helvetica", 14, "bold"),
            fg_color="#000000",
            text_color="#FFFFFF",
            hover_color="#333333",
            corner_radius=5,
            width=100,
            height=40,
            command=delete_window.destroy  # Close the window on "No"
        )
        no_button.pack(side="left", padx=(0, 10))
        
        def delete_and_close():
            success = self.controller.deleteTugas(idTugas)
            if success:
                tk.messagebox.showinfo("Success", "Tugas berhasil dihapus!")
                delete_window.destroy()  # Close the delete confirmation window
                self.refresh_projects()  # Refresh the project list or view
                self.show_main_view()
            else:
                tk.messagebox.showerror("Error", "Gagal menghapus tugas. Silakan coba lagi.")

        # "Iya" (Yes) button
        yes_button = ctk.CTkButton(
            button_frame,
            text="Iya",
            font=("Helvetica", 14, "bold"),
            fg_color="#FF4B4B",
            text_color="#FFFFFF",
            hover_color="#CC0000",
            corner_radius=5,
            width=100,
            height=40,
            command=lambda: delete_and_close()
        )
        yes_button.pack(side="left", padx=(10, 0))

        delete_window.mainloop()

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
