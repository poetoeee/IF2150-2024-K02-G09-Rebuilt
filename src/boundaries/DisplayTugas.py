from tkinter import ttk
import tkinter as tk

class DisplayTugas(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=(20, 10))
        self.controller = controller

        # Main Frame setup
        self.pack_propagate(False)  # Prevent resizing the frame itself

        # Add UI components
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        title_label = ttk.Label(self, text="Tugas Management", font=("Helvetica", 25, "bold"))
        title_label.pack(anchor="center", pady=10)

        # Add a button to switch to ProyekDisplay
        switch_button = ttk.Button(self, text="Go to Display Proyek",
                                   command=lambda: self.controller.show_frame(DisplayProyek))
        switch_button.pack(anchor="center", pady=10)
