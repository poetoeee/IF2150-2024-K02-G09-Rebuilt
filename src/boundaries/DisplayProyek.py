import os
import tkinter as tk
from tkinter import ttk, messagebox
from controllers.PengelolaProyek import PengelolaProyek

# Set TCL library path
os.environ['TCL_LIBRARY'] = r"C:\Users\mia\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\mia\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

class DisplayProyek:
    def __init__(self): 
        self.window = tk.Tk()
        self.window.title("Rebuilt")
        self.window.state("zoomed")
        self.controller = PengelolaProyek()
        self.setup_ui()
        
    def setup_ui(self):
        # Create frames
        self.form_frame = ttk.LabelFrame(self.window, text="Add New Project", padding=20)
        self.form_frame.pack(fill="x", padx=20, pady=10)
        
        self.list_frame = ttk.LabelFrame(self.window, text="Project List", padding=20)
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    def run(self):
        self.window.mainloop()