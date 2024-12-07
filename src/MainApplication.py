import tkinter as tk
from tkinter import ttk
from boundaries.DisplayProyek import DisplayProyek
from boundaries.DisplayTugas import DisplayTugas

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyek Management")
        self.state('zoomed')  # Make the window maximized
        
        # Create a container frame
        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        
        # A dictionary to store frames
        self.frames = {}

        # Create the frames but don't pack them yet
        for F in (DisplayProyek, DisplayTugas):
            frame = F(self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Use grid instead of pack

        # Configure the container's grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Start with DisplayProyek
        self.show_frame(DisplayProyek)

    def show_frame(self, frame_class):
        """Raise the specified frame to the top."""
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()