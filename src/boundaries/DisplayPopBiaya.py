import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
from entities.Biaya import Biaya

class DisplayPop:
    def __init__(self, controller):
        self.window = ttk.Window(themename="flatly")
        self.controller = controller

        # Layout
        self.displayPop()

    def displayPop(self):
        formWindow = ttk.Toplevel(self.window)
        formWindow.title("Form Edit Biaya")

        # Mengatur ukuran dan posisi popup
        window_width = 600
        window_height = 700
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        formWindow.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Membuat custom style untuk button
        style = ttk.Style()

        # Custom style for the Save button
        style.configure("Custom.TButton", 
                        background="#FFFFFF",  # White background
                        borderwidth=0,         # No border
                        font=("Poppins", 10, "bold"))  # Custom font (Poppins)
        style.map("Custom.TButton", 
                  background=[("active", "#FFFFFF"), ("pressed", "#FFFFFF")])  # White background on hover and press

        style.configure("WhiteRed.TButton", 
                        background="white",    # Background putih
                        foreground="black",      # Teks merah
                        borderwidth=0,         # Tanpa border
                        font=("Poppins", 10, "bold"))  # Changed font to Poppins
        style.map("WhiteRed.TButton", 
                  background=[("active", "white")],  # Tetap putih saat hover
                  foreground=[("active", "darkred")])  # Merah gelap saat hover

        # Button with style custom
        customButton = ttk.Button(formWindow, 
                                  text="\u2190 Back to Tugas Name", 
                                  command=formWindow.destroy, 
                                  style="WhiteRed.TButton")  # Apply custom style for the back button
        customButton.grid(row=0, column=0, sticky="W", padx=10, pady=10)

        # Header with some horizontal padding to move it to the right
        judulLabel = ttk.Label(formWindow, text="[Edit Biaya Detail]", font=("Poppins", 16, "bold"))  # Changed font to Poppins
        judulLabel.grid(row=1, column=0, columnspan=2, pady=20, padx=(0, 220))  # Add padding to left and right (move right)

        # Add text labels and entry boxes below each label
        label_names = ["Nama Barang", "Harga Satuan", "Kuantitas", "Keterangan"]
        self.entries = {}  # Dictionary to hold entry widgets, to access later

        for i, text in enumerate(label_names, start=2):
            # Create the label
            label = ttk.Label(formWindow, text=text, font=("Poppins", 12, "bold"), foreground="blue")  # Changed font to Poppins
            label.grid(row=i * 2, column=0, padx=(80, 0), pady=5, sticky="W")  # Label with padding left and right
            
            # Create the entry field with white background and border
            if text == "Keterangan":  # Use ScrolledText for the "Keterangan" field
                contentBox = scrolledtext.ScrolledText(formWindow, height=5, wrap=tk.WORD, font=("Poppins", 12))  # Changed font to Poppins
                contentBox.grid(row=i * 2 + 1, column=0, columnspan=2, padx=(75,), pady=5, sticky="W")  # Expand across columns
                contentBox.config(bg="white", bd=1, relief="solid")
                self.entries[text] = contentBox
            else:  # For other fields, use the Entry widget
                entry = ttk.Entry(formWindow, font=("Poppins", 12), bootstyle="light")  # Changed font to Poppins
                entry.grid(row=i * 2 + 1, column=0, columnspan=2, padx=(75, 0), pady=5, sticky="W")  # Expand across columns

                # Customizing the Entry widget to have a white background and a border
                entry.config(style="WhiteBorder.TEntry")

                # Store the entry widget in the dictionary
                self.entries[text] = entry

        # Custom style for the Entry field to have a white background and border
        style.configure("WhiteBorder.TEntry", 
                        fieldbackground="white", 
                        borderwidth=1, 
                        relief="solid",  # Solid border for a clear distinction
                        padding=(5, 2))  # Padding inside the entry box

        # Configuring the columns to allow expansion for the entry fields
        formWindow.grid_columnconfigure(0, weight=1)  # Column 0 will take most of the space (for entry fields)
        formWindow.grid_columnconfigure(1, weight=0)  # Column 1 takes no space

        imgIya = Image.open("../img/saveButton.png")  # Replace with your image path for the "Save" button
        photoIya = ImageTk.PhotoImage(imgIya)

        # Create the "Iya" (Save) button and apply the custom style
        iyaButton = ttk.Button(
            formWindow, 
            image=photoIya,
            style="Custom.TButton",  # Apply the custom style
            command=lambda: self.save_data()  # Replace with your function
        )
        
        iyaButton.image = photoIya  # Keep a reference to avoid garbage collection
        iyaButton.grid(row=999, column=1, pady=50, padx=75, sticky="SE")  # Place the button at the bottom-right

    def save_data(self):
        # Create a dictionary to store all entries' values
        data = {}
        
        for label, entry in self.entries.items():
            # Use the label as the key and the entry text as the value
            if isinstance(entry, scrolledtext.ScrolledText):  # If it's a ScrolledText widget
                data[label] = entry.get("1.0", "end-1c")  # Get text from the ScrolledText widget
            else:
                data[label] = entry.get()  # Get text from the Entry widget
        
        # Now 'data' contains the content of all textboxes
        print(data)  # You can replace this with saving the data to a variable or file

    def run(self):
        self.window.mainloop()

# Run the GUI
if __name__ == "__main__":
    controller = None
    app = DisplayPop(controller)
    app.run()
