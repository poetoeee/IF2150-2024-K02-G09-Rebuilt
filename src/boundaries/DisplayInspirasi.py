import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from controllers.PengelolaInspirasi import PengelolaInspirasi  # Sesuaikan dengan struktur folder Anda
from entities.Inspirasi import Inspirasi

class DisplayInspirasi(tk.Frame):  # Ensure it inherits from ttk.Frame
    def __init__(self, parent, controller, app):
        super().__init__(parent)  # Use tk.Frame's initializer
        self.controller = controller
        self.app = app
        self.current_frame = None  # Track the current sub-frame
        self.showInspirasiLists() 


    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def showInspirasiLists(self):
        from boundaries.DisplayProyek import DisplayProyek
        self.clear_frame()

        self.current_frame = ttk.Frame(self, padding=(50, 30))
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        header_frame = ttk.Frame(self.current_frame)
        header_frame.pack(fill=tk.X)

        back_button = ttk.Button(
            header_frame, 
            text="\u2190 Back to Project List", 
            command=lambda: self.app.show_frame(DisplayProyek)  # Use self.app instead of self.controller
        )
        back_button.grid(row=0, column=0, sticky="w", pady=(0, 10))

        title_add_frame = ttk.Frame(header_frame)
        title_add_frame.grid(row=1, column=0, sticky="w", pady=(10, 0))

        title_label = ttk.Label(title_add_frame, text="[Inspirasi Renovasi]", font=("Helvetica", 35, "bold"), foreground="#4966FF", background="#FFFFFF")
        title_label.pack(side=tk.LEFT)

        add_icon = Image.open("img/addButton.png")
        add_icon = add_icon.resize((30, 30))
        add_image = ImageTk.PhotoImage(add_icon)
        add_button = ttk.Button(title_add_frame, text="", image=add_image, style="Custom.TButton", command=self.add_inspirasi)
        add_button.image = add_image
        add_button.pack(side=tk.LEFT, padx=(10, 0))

        subtitle_label = ttk.Label(
            self.current_frame,
            text="Kumpulkan referensi foto yang dapat menginspirasimu dalam merancang blueprint renovasi yang menarik!",
            font=("Helvetica", 15),
            background="#FFFFFF",
        )
        subtitle_label.pack(anchor="w", pady=(10, 20))

        # Create a canvas and scrollbar for inspirasi cards
        canvas_frame = ttk.Frame(self.current_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(canvas_frame)
        scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a frame inside the canvas
        inspirasiFrame = ttk.Frame(canvas, style="TFrame")

        # Add the frame to the canvas
        canvas.create_window((0, 0), window=inspirasiFrame, anchor="nw")

        # Populate the inspirasi cards
        for i, inspirasi in enumerate(self.controller.getAllInspirasi()):
            card = ctk.CTkFrame(
                inspirasiFrame, corner_radius=10, fg_color="#FFFFFF", border_width=1, border_color="#E0E0E0"
            )
            card.grid(row=i // 5, column=i % 5, padx=20, pady=20, sticky="nsew")

            title_label = tk.Label(card, text=inspirasi.judulInspirasi, font=("Helvetica", 14, "bold"), bg="#FFFFFF", anchor="w")
            title_label.pack(anchor="w", padx=10, pady=(10, 0))
            try:
                pil_image = Image.open(inspirasi.imageInspirasi)
                resized_image = pil_image.resize((225, 200)) 
                card_image = ImageTk.PhotoImage(resized_image)
                image_label = tk.Label(card, image=card_image, bg="#FFFFFF")
                image_label.image = card_image 
            except FileNotFoundError:
                image_label = tk.Label(card, text="Image Not Found", bg="#FFFFFF")

            image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

            detail_button = ctk.CTkButton(
                card, text="Detail \u2192", fg_color="#FFFFFF", text_color="black", command=lambda p=inspirasi: self.showInspirasiDetail(p)
            )
            detail_button.pack(pady=(0, 5))

        # Update the canvas scroll region after adding all widgets
        inspirasiFrame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))



    def showInspirasiDetail(self, inspirasi):
        self.clear_frame()

        self.current_frame = ttk.Frame(self, padding=(50, 30))
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        back_button = ttk.Button(self.current_frame, text="← Back to Project List", command=self.showInspirasiLists)
        back_button.pack(anchor="w", pady=(0, 20))

        content_frame = ttk.Frame(self.current_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = ttk.Frame(content_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 20), pady=(20, 20), expand=True)

        try:
            pil_image = Image.open(inspirasi.imageInspirasi)
            resized_image = pil_image.resize((400, 400)) 
            tk_image = ImageTk.PhotoImage(resized_image) 

            image_label = ctk.CTkLabel(left_frame, text="", image=tk_image)
            image_label.image = tk_image 
        except FileNotFoundError:
            image_label = ctk.CTkLabel(left_frame, text="Image Not Found")

        image_label.pack(anchor="n")

        action_frame = ttk.Frame(left_frame)
        action_frame.pack(anchor="n", pady=(50, 0)) 

        delete_icon = Image.open(r"img/deleteButton.png") 
        delete_icon = delete_icon.resize((110, 40)) 
        delete_image = ImageTk.PhotoImage(delete_icon)

        edit_icon = Image.open(r"img/editButton.png") 
        edit_icon = edit_icon.resize((110, 40))
        edit_image = ImageTk.PhotoImage(edit_icon)

        # Delete Button
        delete_button = ttk.Button(
            action_frame,
            text="", 
            image=delete_image, 
            style="Custom.TButton", 
            command=lambda: self.delete_inspirasi(inspirasi)
        )
        delete_button.image = delete_image 
        delete_button.pack(side=tk.LEFT, padx=10)

        edit_button = ttk.Button(
            action_frame,
            text="",  
            image=edit_image,
            style="Custom.TButton", 
            command=lambda: self.edit_inspirasi(inspirasi)
        )
        edit_button.image = edit_image 
        edit_button.pack(side=tk.LEFT, padx=10)

        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        title_label = ttk.Label(right_frame, text=f"[{inspirasi.judulInspirasi}]", font=("Helvetica", 35, "bold"), foreground="#4966FF", background="#FFFFFF")
        title_label.pack(anchor="w", pady=(10, 10))

        description_label = ttk.Label(right_frame, text=inspirasi.descInspirasi, font=("Helvetica", 15), wraplength=500, background="#FFFFFF")
        description_label.pack(anchor="w", pady=(10, 20))

        link_label = ttk.Label(right_frame, text=inspirasi.linkInspirasi, font=("Helvetica", 12), foreground="blue", background="#FFFFFF")
        link_label.pack(anchor="w", pady=(10, 20))



    def delete_inspirasi(self, inspirasi):
        result = messagebox.askyesno("Konfirmasi Hapus", f"Yakin ingin menghapus {inspirasi.judulInspirasi}?")
        if result:
            success = self.controller.deleteInspirasi(inspirasi.idInspirasi)
            if success:
                messagebox.showinfo("Success", "Inspirasi berhasil dihapus.")
                self.showInspirasiLists()
            else:
                messagebox.showerror("Error", "Gagal menghapus Inspirasi.")

    def edit_inspirasi(self, inspirasi):
        popup = tk.Toplevel()
        popup.title("Edit Inspirasi")
        popup.geometry("650x700")
        popup.grab_set() 
        main_frame = ttk.Frame(popup, padding="50")
        main_frame.pack(fill=tk.BOTH, expand=True)

        header_label = ttk.Label(
            main_frame,
            text="[Edit Inspirasi Detail]",
            font=("Helvetica", 25, "bold"),
            foreground="#000000", 
            background="#FFFFFF",
            # anchor="w"
        )
        header_label.grid(row=0, column=0, sticky="w", pady=(0, 20)) 

        title_label = ttk.Label(main_frame, text="Judul Inspirasi:", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        title_label.grid(row=1, column=0, sticky="w", pady=(5, 0))
        title_var = tk.StringVar(value=inspirasi.judulInspirasi)
        title_entry = ttk.Entry(main_frame, textvariable=title_var, font=("Helvetica", 12))
        title_entry.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        description_label = ttk.Label(main_frame, text="Deskripsi:", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        description_label.grid(row=3, column=0, sticky="w", pady=(5, 0))

        description_frame = ttk.Frame(main_frame)
        description_frame.grid(row=4, column=0, sticky="ew", pady=(0, 10))
        description_frame.columnconfigure(0, weight=1)

        description_entry = tk.Text(description_frame, wrap="word", height=10, font=("Helvetica", 12))
        description_entry.insert("1.0", inspirasi.descInspirasi) 
        description_entry.grid(row=0, column=0, sticky="ew")

        description_scrollbar = ttk.Scrollbar(description_frame, orient="vertical", command=description_entry.yview)
        description_scrollbar.grid(row=0, column=1, sticky="ns")

        description_entry.config(yscrollcommand=description_scrollbar.set)

        image_label = ttk.Label(main_frame, text="File gambar:", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        image_label.grid(row=5, column=0, sticky="w", pady=(5, 0))
        image_path_var = tk.StringVar(value=inspirasi.imageInspirasi)
        image_entry = ttk.Entry(main_frame, textvariable=image_path_var, font=("Helvetica", 12))
        image_entry.grid(row=6, column=0, sticky="ew", pady=(0, 5))

        def browse_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                image_path_var.set(file_path)

        browse_button = ttk.Button(main_frame, text="Masukkan gambar", command=browse_image)
        browse_button.grid(row=7, column=0, pady=5, sticky="w")

        link_label = ttk.Label(main_frame, text="Link (opsional):", font=("Helvetica", 15, "bold"), foreground="#4966FF", background="#FFFFFF")
        link_label.grid(row=8, column=0, sticky="w", pady=(5, 0))
        link_var = tk.StringVar(value=inspirasi.linkInspirasi)
        link_entry = ttk.Entry(main_frame, textvariable=link_var, font=("Helvetica", 12))
        link_entry.grid(row=9, column=0, sticky="ew", pady=(0, 10))

        main_frame.columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure(
            "Custom.TButton",
            background="#FFFFFF",  
            bd=0,
        )
        style.map(
            "Custom.TButton",
            background=[("active", "#FFFFFF"), ("pressed", "#FFFFFF")],
        )

        save_icon = Image.open(r"img/saveButton.png") 
        save_icon = save_icon.resize((110, 40))
        save_image = ImageTk.PhotoImage(save_icon)

        save_button = ttk.Button(
            main_frame,
            text="", 
            image=save_image,
            style="Custom.TButton", 
            command=lambda: self.save_inspirasi_from_popup(
                popup,
                inspirasi,
                title_var.get(),
                description_entry.get("1.0", tk.END).strip(),
                image_path_var.get(),
                link_var.get()
            ),
        )
        save_button.image = save_image  
        save_button.grid(row=10, column=0, pady=20, sticky="e")



    def save_inspirasi_from_popup(self, popup, inspirasi, new_title, new_description, new_image, new_link):
        existingID = inspirasi.getIdInspirasi()
        if not new_title or not new_description or not new_image:
            messagebox.showerror("Error", "Judul, Deskripsi, dan Gambar wajib diisi!")
            return
        
        try:
            existingInpirasi = Inspirasi(
                judulInspirasi= new_title,
                descInspirasi= new_description,
                imageInspirasi= new_image,
                linkInspirasi= new_link if new_link else "No Link Provided",
                idInspirasi= existingID,
            )
            success = self.controller.editInspirasi(existingInpirasi)
            if success:
                self.showInspirasiLists()
                popup.destroy()
                messagebox.showinfo("Success", "Inspirasi berhasil diubah.")
            else:
                messagebox.showerror("Error", "Gagal mengubah Inspirasi.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")


    def add_inspirasi(self):
        popup = tk.Toplevel()
        popup.title("Tambah Inspirasi")
        popup.geometry("650x700") 
        popup.grab_set()

        main_frame = ttk.Frame(popup, padding="50")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="[Tambah Inspirasi Baru]", font=("Helvetica", 25, "bold"), foreground="#000000")
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 20))

        title_var = tk.StringVar()
        ttk.Label(main_frame, text="Judul Inspirasi:", font=("Helvetica", 15, "bold"), foreground="#4966FF").grid(row=1, column=0, sticky="w", pady=(5,0))
        title_entry = ttk.Entry(main_frame, textvariable=title_var, font=("Helvetica", 12))
        title_entry.grid(row=2, column=0, pady=(0, 10), sticky="ew")

        description_var = tk.StringVar()
        ttk.Label(main_frame, text="Deskripsi:", font=("Helvetica", 15, "bold"), foreground="#4966FF").grid(row=3, column=0, sticky="w", pady=(5,0))
        # description_entry = tk.Text(main_frame, textvariable=description_var)
        # description_entry.grid(row=4, column=0, pady=(0, 10), sticky="ew")
        description_frame = ttk.Frame(main_frame)
        description_frame.grid(row=4, column=0, sticky="ew", pady=(0, 10))
        description_frame.columnconfigure(0, weight=1)

        description_entry = tk.Text(description_frame, wrap="word", height=10, font=("Helvetica", 12))
        # description_entry.insert("1.0", project["description"])  # Insert initial text
        description_entry.grid(row=0, column=0, sticky="ew")

        description_scrollbar = ttk.Scrollbar(description_frame, orient="vertical", command=description_entry.yview)
        description_scrollbar.grid(row=0, column=1, sticky="ns")

        description_entry.config(yscrollcommand=description_scrollbar.set)

        image_path_var = tk.StringVar()
        ttk.Label(main_frame, text="Gambar:", font=("Helvetica", 15, "bold"), foreground="#4966FF").grid(row=5, column=0, sticky="w", pady=(5,0))
        image_entry = ttk.Entry(main_frame, textvariable=image_path_var, font=("Helvetica", 12))
        image_entry.grid(row=6, column=0, pady=(0, 10), sticky="ew")

        def browse_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                image_path_var.set(file_path)

        browse_button = ttk.Button(main_frame, text="Masukkan gambar", command=browse_image)
        browse_button.grid(row=7, column=0, pady=5, sticky="w")

        link_var = tk.StringVar()
        ttk.Label(main_frame, text="Link (Opsional):", font=("Helvetica", 15, "bold"), foreground="#4966FF").grid(row=8, column=0, sticky="w", pady=(5,0))
        link_entry = ttk.Entry(main_frame, textvariable=link_var, font=("Helvetica", 12))
        link_entry.grid(row=9, column=0, pady=(0, 10), sticky="ew")

        main_frame.columnconfigure(0, weight=1)
        save_icon = Image.open(r"img/saveButton.png") 
        save_icon = save_icon.resize((110, 40))  
        save_image = ImageTk.PhotoImage(save_icon)
        submit_button = ttk.Button(
            main_frame,
            text="",
            image=save_image,
            style="Custom.TButton",
            command=lambda: self.save_new_inspirasi(
                popup,
                title_var.get(),
                description_entry.get("1.0", tk.END).strip(),
                image_path_var.get(),
                link_var.get(),
            )
        )
        submit_button.image = save_image
        submit_button.grid(row=10, column=0, pady=20, sticky="e")


    def save_new_inspirasi(self, popup, title, description, image, link):
        if not title or not description or not image:
            messagebox.showerror("Error", "Judul, Deskripsi, dan Gambar wajib diisi!")
            return

        new_inspirasi = Inspirasi(
            judulInspirasi= title,
            descInspirasi= description,
            imageInspirasi= image,
            linkInspirasi= link if link else "No Link Provided",
        )
        success = self.controller.addInspirasi(new_inspirasi)
        if success:
            self.showInspirasiLists()
            popup.destroy()
            messagebox.showinfo("Success", "Inspirasi berhasil ditambahkan.")
        else:
            messagebox.showerror("Error", "Gagal menambahkan Inspirasi.")


    def run(self):
        self.window.mainloop()


class PengelolaInspirasi:
    pass


# if __name__ == "__main__":
#     controller = PengelolaInspirasi()
#     app = DisplayInspirasi(controller)
#     app.run()