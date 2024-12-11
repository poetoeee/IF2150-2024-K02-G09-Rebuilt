import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox


class DisplayInspirasi:
    def __init__(self, controller):
        self.window = tk.Tk()
        self.window.title("Inspirasi Management")
        self.window.geometry("1200x800")
        self.controller = controller

        self.current_frame = None
        self.inspirasi_data = [
            {"id": 1, "title": "Inspirasi#1", "image": r"C:\Users\ASUS\Downloads\STEI.png", "description": "Deskripsi Inspirasi 1", "link": "https://linktoinspirasi1.com"},
            {"id": 2, "title": "Inspirasi#2", "image": r"C:\Users\ASUS\Downloads\03.-FTI.png", "description": "Deskripsi Inspirasi 2", "link": "https://linktoinspirasi1.com"},
            {"id": 3, "title": "Inspirasi#3", "image": r"C:\Users\ASUS\Downloads\50622553392_fbbd042e69_k.jpg", "description": "Deskripsi Inspirasi 3asd asdasdasdasf asfasfasfasf asfasfasdfasdf asdfasdfasdfasdf asdfasdfasdfsdf asdfasdfasdf asdfasdfasdfasdf asdfasdfasdfasdf asdfasdfasdfasdf asdfasdfasdfasdf asdfasdfasdfasdf sadfsadfasdfsdf asdfasdfasdfasdf asdfasdfasdfasdf sadfasdfoislknjngki inoidfnb nkdj", "link": "https://linktoinspirasi1.com"},
            {"id": 4, "title": "Inspirasi#4", "image": r"C:\Users\ASUS\Downloads\06.-FTTM.png", "description": "Deskripsi Inspirasi 4", "link": "https://linktoinspirasi1.com"},
            {"id": 5, "title": "Inspirasi#5", "image": r"C:\Users\ASUS\Downloads\10.-SF.png", "description": "Deskripsi Inspirasi 5", "link": "https://linktoinspirasi1.com"},
            {"id": 6, "title": "Inspirasi#6", "image": r"C:\Users\ASUS\Downloads\03.-FSRD.png", "description": "Deskripsi Inspirasi 6", "link": "https://linktoinspirasi1.com"},
        ]

        self.showInspirasiLists()

    def clear_frame(self):
        """Clear the current frame."""
        if self.current_frame:
            self.current_frame.destroy()

    def showInspirasiLists(self):
        """Display the project list view."""
        self.clear_frame()

        self.current_frame = ttk.Frame(self.window, padding=(50, 20))
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        # Header Section
        header_frame = ttk.Frame(self.current_frame)
        header_frame.pack(fill=tk.X)

        # Back Button
        back_button = ttk.Button(header_frame, text="← Back to Project List", command=self.window.quit)
        back_button.grid(row=0, column=0, sticky="w", pady=(0, 10))  # Pakai grid dengan baris 0

        # Title and Add Button in a separate frame
        title_add_frame = ttk.Frame(header_frame)
        title_add_frame.grid(row=1, column=0, sticky="w", pady=(10, 0))  # Pakai baris 1 untuk di bawah back_button

        # Title Label
        title_label = ttk.Label(title_add_frame, text="[Inspirasi Renovasi]", font=("Helvetica", 35, "bold"), foreground="#4966FF", background="#FFFFFF")
        title_label.pack(side=tk.LEFT)

        # Add Button
        add_button = ctk.CTkButton(title_add_frame, text="+", font=("Helvetica", 25, "bold"), width=30, height=30, fg_color="#000000", text_color="white", corner_radius=15, command=self.add_inspirasi)
        add_button.pack(side=tk.LEFT, padx=(10, 0))


        # Subtitle
        subtitle_label = ttk.Label(
            self.current_frame,
            text="Kumpulkan referensi foto yang dapat menginspirasimu dalam merancang blueprint renovasi yang menarik!",
            font=("Helvetica", 15),
            background="#FFFFFF",
        )
        subtitle_label.pack(anchor="w", pady=(10, 20))

        # Projects Grid
        projects_frame = ttk.Frame(self.current_frame)
        projects_frame.pack(fill=tk.BOTH, expand=True)

        for i, project in enumerate(self.inspirasi_data):
            # Adjust card size and grid layout
            card = ctk.CTkFrame(
                projects_frame, corner_radius=10, fg_color="#FFFFFF", border_width=1, border_color="#E0E0E0"
            )
            card.grid(row=i // 5, column=i % 5, padx=20, pady=20, sticky="nsew")  # 4 cards per row

            # Title
            title_label = tk.Label(card, text=project["title"], font=("Helvetica", 14, "bold"), bg="#FFFFFF", anchor="w")
            title_label.pack(anchor="w", padx=10, pady=(10, 0))
            # Load image with Pillow
            try:
                pil_image = Image.open(project["image"])
                resized_image = pil_image.resize((225, 200))  # Resize image
                card_image = ImageTk.PhotoImage(resized_image)
                image_label = tk.Label(card, image=card_image, bg="#FFFFFF")
                image_label.image = card_image  # Keep reference to prevent garbage collection
            except FileNotFoundError:
                image_label = tk.Label(card, text="Image Not Found", bg="#FFFFFF")

            image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)


            # Detail Button
            detail_button = ctk.CTkButton(
                card, text="Detail →", fg_color="#FFFFFF", text_color="black", command=lambda p=project: self.showInspirasiDetail(p)
            )
            detail_button.pack(pady=(0, 5))


    def showInspirasiDetail(self, project):
        """Display the project detail view."""
        self.clear_frame()

        self.current_frame = ttk.Frame(self.window, padding=(50, 20))
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        # Back Button
        back_button = ttk.Button(self.current_frame, text="← Back to Project List", command=self.showInspirasiLists)
        back_button.pack(anchor="w", pady=(0, 20))

        # Main Content Frame (Horizontal Layout)
        content_frame = ttk.Frame(self.current_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Left Frame for Image
        left_frame = ttk.Frame(content_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 20), pady=(20, 20), expand=True)

        # Image Section
        try:
            pil_image = Image.open(project["image"])
            resized_image = pil_image.resize((550, 550))  # Resize image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter-compatible format

            image_label = ctk.CTkLabel(left_frame, text="", image=tk_image)
            image_label.image = tk_image  # Prevent garbage collection
        except FileNotFoundError:
            image_label = ctk.CTkLabel(left_frame, text="Image Not Found")

        image_label.pack(anchor="n")  # Anchor to the top

        # Action Buttons (Directly Below Image)
        action_frame = ttk.Frame(left_frame)
        action_frame.pack(anchor="n", pady=(50, 0))  # Positioned below the image with some padding

        delete_button = ctk.CTkButton(action_frame, text="Delete", fg_color="#FF4C4C", command=lambda: self.delete_inspirasi(project))
        delete_button.pack(side=tk.LEFT, padx=10)

        edit_button = ctk.CTkButton(action_frame, text="Edit", fg_color="#4966FF", command=lambda: self.edit_inspirasi(project))
        edit_button.pack(side=tk.LEFT, padx=10)


        # Right Frame for Text Details
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Project Details
        title_label = ttk.Label(right_frame, text=f"[{project['title']}]", font=("Helvetica", 35, "bold"), foreground="#4966FF", background="#FFFFFF")
        title_label.pack(anchor="w", pady=(10, 10))

        description_label = ttk.Label(right_frame, text=project["description"], font=("Helvetica", 15), wraplength=500, background="#FFFFFF")
        description_label.pack(anchor="w", pady=(10, 20))

        link_label = ttk.Label(right_frame, text=project["link"], font=("Helvetica", 12), foreground="blue", background="#FFFFFF")
        link_label.pack(anchor="w", pady=(10, 20))



    def delete_inspirasi(self, project):
        """Delete the selected inspirasi."""
        result = messagebox.askyesno("Konfirmasi Hapus", f"Yakin ingin menghapus {project['title']}?")
        if result:
            self.inspirasi_data = [p for p in self.inspirasi_data if p["id"] != project["id"]]
            self.showInspirasiLists()

    def edit_inspirasi(self, project):
        """Edit the selected inspirasi in a pop-up window."""
        # Create pop-up window
        popup = tk.Toplevel(self.window)
        popup.title("Edit Inspirasi")
        popup.geometry("650x700")
        popup.grab_set()  # Disable interaction with the main window until this is closed

        # Main Frame
        style = ttk.Style()
        style.configure("TFrame", background="#FFFFFF")
        main_frame = ttk.Frame(popup, padding="50")
        main_frame.pack(fill=tk.BOTH, expand=True)

        header_label = ttk.Label(
            main_frame,
            text="[Edit Inspirasi Detail]",
            font=("Helvetica", 25, "bold"),
            foreground="#000000",  # Optional: Adjust color
            background="#FFFFFF",
            # anchor="w"
        )
        header_label.grid(row=0, column=0, sticky="w", pady=(0, 20))  # Spans across columns for centering


        # Title
        title_label = ttk.Label(main_frame, text="Judul Inspirasi:", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        title_label.grid(row=1, column=0, sticky="w", pady=(5, 0))
        title_var = tk.StringVar(value=project["title"])
        title_entry = ttk.Entry(main_frame, textvariable=title_var, font=("Helvetica", 12))
        title_entry.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        # Description
        # Description
        description_label = ttk.Label(main_frame, text="Deskripsi:", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        description_label.grid(row=3, column=0, sticky="w", pady=(5, 0))

        # Frame for Text and Scrollbar
        description_frame = ttk.Frame(main_frame)
        description_frame.grid(row=4, column=0, sticky="ew", pady=(0, 10))
        description_frame.columnconfigure(0, weight=1)

        description_entry = tk.Text(description_frame, wrap="word", height=10, font=("Helvetica", 12))
        description_entry.insert("1.0", project["description"])  # Insert initial text
        description_entry.grid(row=0, column=0, sticky="ew")

        description_scrollbar = ttk.Scrollbar(description_frame, orient="vertical", command=description_entry.yview)
        description_scrollbar.grid(row=0, column=1, sticky="ns")

        # Link scrollbar to Text widget
        description_entry.config(yscrollcommand=description_scrollbar.set)

        # Image Path
        image_label = ttk.Label(main_frame, text="File gambar:", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        image_label.grid(row=5, column=0, sticky="w", pady=(5, 0))
        image_path_var = tk.StringVar(value=project["image"])
        image_entry = ttk.Entry(main_frame, textvariable=image_path_var, font=("Helvetica", 12))
        image_entry.grid(row=6, column=0, sticky="ew", pady=(0, 5))

        def browse_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                image_path_var.set(file_path)

        browse_button = ttk.Button(main_frame, text="Masukkan gambar", command=browse_image)
        browse_button.grid(row=7, column=0, pady=5, sticky="w")

        # Link
        link_label = ttk.Label(main_frame, text="Link (opsional):", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        link_label.grid(row=8, column=0, sticky="w", pady=(5, 0))
        link_var = tk.StringVar(value=project["link"])
        link_entry = ttk.Entry(main_frame, textvariable=link_var, font=("Helvetica", 12))
        link_entry.grid(row=9, column=0, sticky="ew", pady=(0, 10))

        # Adjust column weights
        main_frame.columnconfigure(0, weight=1)

        # Save Button
        style = ttk.Style()
        style.configure(
            "Custom.TButton",
            background="#FFFFFF",  # Background color (white)
            borderwidth=0,  # Remove border
        )
        style.map(
            "Custom.TButton",
            background=[("active", "#FFFFFF"), ("pressed", "#FFFFFF")],
        )

        # Load Image for Button
        save_icon = Image.open(r"C:\Users\ASUS\OneDrive - Institut Teknologi Bandung\Pictures\Screenshots\Screenshot 2024-12-10 211906.png")  # Ganti dengan path ke file gambar Anda
        save_icon = save_icon.resize((110, 40))  # Resize sesuai kebutuhan
        save_image = ImageTk.PhotoImage(save_icon)

        # Save Button with Custom Style and Image
        save_button = ttk.Button(
            main_frame,
            text="",  # Kosongkan teks agar hanya gambar yang terlihat
            image=save_image,  # Tambahkan gambar
            style="Custom.TButton",  # Gunakan style kustom
            command=lambda: self.save_inspirasi_from_popup(
                popup,
                project,
                title_var.get(),
                description_entry.get("1.0", tk.END).strip(),
                image_path_var.get(),
                link_var.get()
            ),
        )
        save_button.image = save_image  # Simpan referensi gambar agar tidak dibuang oleh garbage collector
        save_button.grid(row=10, column=0, pady=20, sticky="e")



    def save_inspirasi_from_popup(self, popup, project, new_title, new_description, new_image, new_link):
        """Save edited inspirasi details from pop-up."""
        if not new_title or not new_description or not new_image:
            messagebox.showerror("Error", "Judul, Deskripsi, dan Gambar wajib diisi!")
            return

        project["title"] = new_title
        project["description"] = new_description
        project["image"] = new_image
        project["link"] = new_link
        self.showInspirasiLists()
        popup.destroy()  # Close the pop-up window


    def add_inspirasi(self):
        """Show a form to add a new inspirasi."""
        self.clear_frame()

        self.current_frame = ttk.Frame(self.window, padding=(50, 20))
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        back_button = ttk.Button(self.current_frame, text="← Back to Project List", command=self.showInspirasiLists)
        back_button.pack(anchor="w", pady=(0, 20))

        title_label = ttk.Label(self.current_frame, text="[Tambah Inspirasi Baru]", font=("Helvetica", 35, "bold"))
        title_label.pack(anchor="w", pady=(0, 20))

        # Form Inputs
        form_frame = ttk.Frame(self.current_frame)
        form_frame.pack(fill=tk.BOTH, padx=20, pady=10)

        title_var = tk.StringVar()
        title_label = ttk.Label(form_frame, text="Judul Inspirasi      :", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        title_label.grid(row=0, column=0, sticky="w", pady=5)
        title_entry = ttk.Entry(form_frame, textvariable=title_var)
        title_entry.grid(row=0, column=1, pady=5)

        description_var = tk.StringVar()
        description_label = ttk.Label(form_frame, text="Deskripsi              :", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        description_label.grid(row=1, column=0, sticky="w", pady=5)
        description_entry = ttk.Entry(form_frame, textvariable=description_var)
        description_entry.grid(row=1, column=1, pady=5)

        image_path_var = tk.StringVar()
        image_label = ttk.Label(form_frame, text="Gambar                :", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        image_label.grid(row=2, column=0, sticky="w", pady=5)
        image_entry = ttk.Entry(form_frame, textvariable=image_path_var)
        image_entry.grid(row=2, column=1, pady=5)

        def browse_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                image_path_var.set(file_path)

        browse_button = ttk.Button(form_frame, text="Browse", command=browse_image)
        browse_button.grid(row=2, column=2, padx=5)

        link_var = tk.StringVar()
        link_label = ttk.Label(form_frame, text="Link (Opsional)     :", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        link_label.grid(row=3, column=0, sticky="w", pady=5)
        link_entry = ttk.Entry(form_frame, textvariable=link_var)
        link_entry.grid(row=3, column=1, pady=5)

        # Submit Button
        submit_button = ctk.CTkButton(
            self.current_frame,
            text="Tambah Inspirasi",
            fg_color="#4966FF",
            command=lambda: self.save_new_inspirasi(title_var.get(), description_var.get(), image_path_var.get(), link_var.get()),
        )
        submit_button.pack(pady=20)

    def save_new_inspirasi(self, title, description, image, link):
        """Save the new inspirasi."""
        if not title or not description or not image:
            messagebox.showerror("Error", "Judul, Deskripsi, dan Gambar wajib diisi!")
            return

        new_id = max([p["id"] for p in self.inspirasi_data]) + 1 if self.inspirasi_data else 1
        new_project = {
            "id": new_id,
            "title": title,
            "description": description,
            "image": image,
            "link": link if link else "No Link Provided",
        }
        self.inspirasi_data.append(new_project)
        self.showInspirasiLists()

    def run(self):
        self.window.mainloop()


class PengelolaInspirasi:
    pass


if __name__ == "__main__":
    controller = PengelolaInspirasi()
    app = DisplayInspirasi(controller)
    app.run()
