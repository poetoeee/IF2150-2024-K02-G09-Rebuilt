import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from boundaries.DisplayTugas import DisplayTugas

class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Create a canvas and a vertical scrollbar
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Configure the canvas
        self.scrollable_frame_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the widgets
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Bind events for resizing and scrolling
        self.scrollable_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        
        self.rightArrowButtonPath = "img/right-arrow.png"        
        self.rightArrowButtonImg = tk.PhotoImage(file=self.rightArrowButtonPath)

    def _on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        """Adjust the frame width to match the canvas."""
        canvas_width = event.width
        self.canvas.itemconfig(self.scrollable_frame_id, width=canvas_width)

class DisplayProyek(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)  # Call parent constructor with only the parent parameter

        self.controller = controller
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)  # Use pack to make it appear

        self.main_frame = ttk.Frame(self, padding=(20, 10))
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        self.pack_propagate(False)
        
        self.setup_ui()
        
    def setup_ui(self):
        rebuilt_title = ttk.Label(self.main_frame, text="Rebuilt", 
                                font=("Helvetica", 20, "bold underline"))
        rebuilt_title.pack(anchor="w", pady=10)

        self.topFrame = ttk.Frame(self.main_frame)
        self.topFrame.pack(fill=tk.X)

        self.top1 = ttk.Frame(self.topFrame)
        greeting_label = ttk.Label(self.top1, text="Good Morning!", 
                                 font=("Helvetica", 35, "bold"), 
                                 foreground="#4966FF")
        greetingTextLabel = ttk.Label(self.top1, 
                                    text="Let's make the best out of your morning together with Rebuilt", 
                                    font=("Helvetica", 15))
        greeting_label.pack(anchor="w")
        greetingTextLabel.pack(anchor="w", pady=20)

        self.top2 = ttk.Frame(self.topFrame)
        self.top3 = ttk.Frame(self.topFrame)
        self.top4 = ttk.Frame(self.topFrame)

        self.top1.pack(side="left", fill=tk.Y, pady=5)
        
        # top4 part

        onProgressNum = ttk.Label(self.top4, text="11", 
                                font=("Helvetica", 25, "bold"))
        onProgressNum.pack(pady=(0, 10))
        
        self.textTop4 = ctk.CTkFrame(
            self.top4,
            corner_radius=10,  # Rounded corners
            fg_color="#4966FF",    # Background color
            bg_color="transparent"  # Transparent background
        )
        
        onProgressText = ctk.CTkLabel(
            self.textTop4,
            text="    On Progress    ",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        )
        
        proyekText = ctk.CTkLabel(
            self.textTop4,
            text="Proyek",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        )
        
        onProgressText.pack()
        proyekText.pack()
        self.textTop4.pack(padx=10, ipadx=10, ipady=1)
        
        # top3 part

        finishedWeekNum = ttk.Label(self.top3, text="11", 
                                font=("Helvetica", 25, "bold"))
        finishedWeekNum.pack(pady=(0, 10))
        
        self.textTop3 = ctk.CTkFrame(
            self.top3,
            corner_radius=10,  # Rounded corners
            fg_color="#4966FF",    # Background color
            bg_color="transparent"  # Transparent background
        )
        
        projectsFinishedWeekText = ctk.CTkLabel(
            self.textTop3,
            text="Projects Finished",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        )
        
        thisWeekText = ctk.CTkLabel(
            self.textTop3,
            text="This Week",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        )
        
        projectsFinishedWeekText.pack()
        thisWeekText.pack()
        self.textTop3.pack(padx=10, ipadx=10, ipady=1)
        
        # top2 part

        finishedTotalNum = ttk.Label(self.top2, text="11", 
                                font=("Helvetica", 25, "bold"))
        finishedTotalNum.pack(pady=(0, 10))
        
        self.textTop2 = ctk.CTkFrame(
            self.top2,
            corner_radius=10,  # Rounded corners
            fg_color="#4966FF",    # Background color
            bg_color="transparent"  # Transparent background
        )
        
        projectsFinishedText = ctk.CTkLabel(
            self.textTop2,
            text="Projects Finished",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        )
        
        totalText = ctk.CTkLabel(
            self.textTop2,
            text="Total",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        )
        
        projectsFinishedText.pack()
        totalText.pack()
        self.textTop2.pack(padx=10, ipadx=10, ipady=1)

        for frame in [self.top4, self.top3, self.top2]:
            frame.pack(side="right", fill=tk.Y, padx=5, pady=5)
            
        # Drawing the line
        canvas = tk.Canvas(self.main_frame, height=0.5, bg="#7A7E93", bd=0, highlightthickness=0)
        canvas.pack(fill=tk.X, pady=5)  # Add the canvas and make it stretch across the width of the window
        
        canvas.create_line(0, 1, self.winfo_width(), 1, fill="white", width=2)

        
        
        # bottom content part
        
        self.bottomFrame = ttk.Frame(self.main_frame)
        self.bottomFrame.pack(fill=tk.BOTH,expand=True, pady=20)
        
        
        # projects part
        
        self.projectsContainer = ttk.Frame(self.bottomFrame)
        self.projectsContainer.pack(side="left", fill=tk.Y)
        #first row of projectContainer
        
        self.projectsContainerRow1= ttk.Frame(self.projectsContainer)
        self.projectsContainerRow1.pack(fill=tk.X)
        projectsTitle = ttk.Label(self.projectsContainerRow1, text="[ Projects ]", 
                                font=("Helvetica", 25, "bold"))
        projectsTitle.pack(side="left")
        
        style = ttk.Style()
        style.configure("Transparent.TButton",
                        background="#FFFFFF",
                        borderwidth=0,
                        relief="flat",
                        padding=0)
        
        addButtonPath = "img/subway_add.png"
        addButtonImg = tk.PhotoImage(file=addButtonPath)
        
        addButton = ttk.Button(self.projectsContainerRow1, 
                       image=addButtonImg, 
                       command=self.onAddButtonClick,
                       style="Transparent.TButton")  # Apply a custom style for transparency
        addButton.image = addButtonImg  # Keep a reference to the image (important to avoid garbage collection)
        addButton.pack(pady=10, padx=20, side="left")  # Packing the button after the title
        
        
        # dropdown sort
        dropdownOptions = ["date-asc", "date-desc", "progress-asc", "progress-desc"]
        dropdown = ttk.Combobox(self.projectsContainerRow1, 
                        values=dropdownOptions,  # Set the dropdown options
                        state="readonly",          # Makes the combobox read-only (can't type in)
                        width=20)                  # Width of the dropdown
        dropdown.set("date-asc")
        dropdown.pack(side="right", padx=(350,5), pady=10)
        
        
        self.scrollable_projects_frame = ScrollableFrame(self.projectsContainer)  # Pack inside projectsContainer
        self.scrollable_projects_frame.pack(fill=tk.BOTH, expand=True)  # Fill remaining space in projectsContainer

        # Call the create_project_cards method
        proyek_list = [
            {"title": "Project#1", "date": "2024-12-01", "progress": 70, "status": "In Progress", "desc": "lorem ipsum dolor sit amet ametnya ganteng yay"},
            {"title": "Project#2", "date": "2024-12-02", "progress": 50, "status": "In Progress", "desc": "lorem ipsum dolor sit amet ametnya ganteng yay"},
            {"title": "Project#3", "date": "2024-12-03", "progress": 80, "status": "In Progress", "desc": "lorem ipsum dolor sit amet ametnya ganteng yay"}
        ]
        
        self.create_project_cards(proyek_list)
    
    def create_project_cards(self, proyek_list):
        # Use the scrollable frame for project cards
        self.rightArrowButtonImg = tk.PhotoImage(file="img/right-arrow.png")
        parent_frame = self.scrollable_projects_frame.scrollable_frame

        # Number of cards per row
        columns = 3
        current_row_frame = None

        card_width = 220
        card_height = 220

        # Create a style for the inner frame and label elements
        style = ttk.Style()
        style.configure("Inner.TFrame", background="#FFFFFF")  # Same as card background color
        style.configure("ProjectLabel.TLabel", background="#FFFFFF", anchor="w", font=("Helvetica", 12))  # Labels styling
        style.configure("ProjectProgress.TLabel", background="#FFFFFF", anchor="w", font=("Helvetica", 13, "bold"))  # Labels styling
        style.configure("JudulLabel.TLabel", background="#FFFFFF", anchor="w", font=("Helvetica", 18, "bold"))  # Labels styling
        style.configure("TanggalLabel.TLabel", background="#FFFFFF", anchor="w", font=("Helvetica", 12, "italic"))  # Labels styling

        for index, proyek in enumerate(proyek_list):
            # Create a new row frame if needed
            if index % columns == 0:
                current_row_frame = ttk.Frame(parent_frame)
                current_row_frame.pack(fill=tk.X, pady=10)

            # Create a CTkFrame for the card with rounded corners
            card = ctk.CTkFrame(
                current_row_frame,
                width=card_width,
                height=card_height,
                corner_radius=15,  # Rounded corners
                fg_color="#FFFFFF",  # Card background color (white or transparent)
                border_color="#7A7E93",  # Border color
                border_width=2,  # Border width
            )
            card.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)
            card.pack_propagate(False)  # Prevent the frame from resizing to fit its content

            # Create a frame inside the card for internal padding
            inner_frame = ttk.Frame(card, style="Inner.TFrame")
            inner_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            # Populate the card with project details
            judulLabel = ttk.Label(inner_frame, text=proyek["title"], style="JudulLabel.TLabel", foreground="#4966FF")
            judulLabel.pack(anchor="w", pady=(0, 5))

            date_label = ttk.Label(inner_frame, text=f"{proyek['date']}", style="TanggalLabel.TLabel")
            date_label.pack(anchor="w", pady=(0, 5))

            # Truncate description if it exceeds a maximum length
            MAX_DESC_LENGTH = 50
            desc_text = proyek["desc"]
            if len(desc_text) > MAX_DESC_LENGTH:
                desc_text = desc_text[:MAX_DESC_LENGTH] + "..."
            
            descLabel = ttk.Label(
                inner_frame,
                text=desc_text,
                style="ProjectLabel.TLabel",
                wraplength=180,  # Ensure text still wraps within the card
                justify="left"   # Align text to the left
            )
            descLabel.pack(anchor="w", pady=(20, 0))

            # Add a spacer frame to push the progress section to the bottom
            spacer = ttk.Frame(inner_frame, style="Inner.TFrame")
            spacer.pack(fill="both", expand=True)

            # Create a frame to hold progress bar and percentage at the bottom
            progress_frame = ttk.Frame(inner_frame, style="Inner.TFrame")
            progress_frame.pack(anchor="w", fill="x", side="bottom")

            # Create a progress bar using CTkProgressBar
            progress_value = proyek["progress"]  # Progress value from 0 to 100
            progress_bar = ctk.CTkProgressBar(
                progress_frame,
                width=90,  # Further reduced width to make room for the button
                height=12,   # Set progress bar height
                corner_radius=10,  # Set border radius
                progress_color="#BFFC34",  # Fill color
                border_color="#7A7E93",  # Border color
                bg_color="#FFFFFF"  # Background color to match the card
            )
            progress_bar.set(progress_value / 100)  # CTkProgressBar uses values between 0 and 1
            progress_bar.pack(side="left", padx=(0, 5))

            # Add percentage label
            percentage_label = ttk.Label(
                progress_frame,
                text=f"{progress_value}%",
                style="ProjectProgress.TLabel"
            )
            percentage_label.pack(side="left")

            # Add spacer frame to push the button to the right
            spacer_right = ttk.Frame(progress_frame, style="Inner.TFrame")
            spacer_right.pack(side="left", fill="x", expand=True)
            

            right_arrow_button = tk.Button(
                progress_frame,
                image=self.rightArrowButtonImg,  # Using the class variable
                borderwidth=0,
                bg="#FFFFFF",
                activebackground="#FFFFFF",
                cursor="hand2",
                command=self.onRightArrowClick
            )
            right_arrow_button.pack(side="right")

    def onAddButtonClick(self):
        print("Add button clicked!")
        
    def onRightArrowClick(self):
        print("Right arrow clicked!")
        # Navigate to the DisplayTugas frame
        self.controller.show_frame(DisplayTugas)

# Instantiate and run the program
if __name__ == "__main__":
    controller = None  # Replace with the actual controller if needed
    app = DisplayProyek(controller)
    app.window.mainloop()
