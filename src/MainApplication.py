import tkinter as tk
from tkinter import ttk
from boundaries.DisplayProyek import DisplayProyek
from boundaries.DisplayTugas import DisplayTugas
from controllers.PengelolaProyek import PengelolaProyek
from controllers.PengelolaTugasProyek import PengelolaTugasProyek  # Import the correct controller for DisplayTugas

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyek Management")
        self.state('zoomed')  # Make the window maximized

        # Initialize controllers
        self.proyek_controller = PengelolaProyek()
        self.tugas_controller = PengelolaTugasProyek()

        # Create a container frame
        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # A dictionary to store frames
        self.frames = {}

        # Create the frames and pass the appropriate controller to each
        self.init_frames()

        # Configure the container's grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Start with DisplayProyek
        self.show_frame(DisplayProyek)

    def init_frames(self):
        """Initialize frames with the appropriate controllers."""
        frame_controller_mapping = [
            (DisplayProyek, self.proyek_controller),
            (DisplayTugas, self.tugas_controller),
        ]
        for FrameClass, controller in frame_controller_mapping:
            frame = FrameClass(self.container, controller=controller)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Use grid instead of pack

    def show_frame(self, frame_class):
        """Raise the specified frame to the top."""
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
