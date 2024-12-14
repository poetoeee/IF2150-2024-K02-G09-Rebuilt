import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from boundaries.DisplayTugas import DisplayTugas
from boundaries.DisplayInspirasi import DisplayInspirasi
from entities.Proyek import Proyek
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import datetime
from controllers.PengelolaTugasProyek import PengelolaTugasProyek

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
    def __init__(self, parent, controller, app):
        super().__init__(parent)  # Call parent constructor with only the parent parameter

        self.controller = controller
        self.app = app

        self.main_frame = ttk.Frame(self, padding=(20, 10))
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        self.setup_ui()
    
    def get_greeting_text(self):
        """Get appropriate greeting based on the local time."""
        current_hour = datetime.datetime.now().hour

        if 4 <= current_hour < 11:
            return "Good Morning!"
        elif 11 <= current_hour < 16:
            return "Good Afternoon!"
        else:
            return "Good Evening!"
        
    def setup_ui(self):
        self.titleFrame = ttk.Frame(self.main_frame)
        self.titleFrame.pack(fill=tk.X)
        
        self.titleFrame.columnconfigure(0, weight=1)
        self.titleFrame.columnconfigure(1, weight=0)
        rebuilt_title = ttk.Label(self.titleFrame, text="Rebuilt", 
                                font=("Helvetica", 20, "bold underline"))
        rebuilt_title.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="w")
        
        self.rightArrowButtonImg = tk.PhotoImage(file="img/right-arrow.png")
        
        
        self.inspirasiButtonImg = tk.PhotoImage(file="img/inspirasi-button.png")
        inspirasiButton = tk.Button(
            self.titleFrame,
            image=self.inspirasiButtonImg,  # Using the class variable
            borderwidth=0,
            cursor="hand2",
            command=lambda: self.app.show_frame(DisplayInspirasi)
        )
        inspirasiButton.grid(row=0, column=1, sticky="e")

        self.topFrame = ttk.Frame(self.main_frame)
        self.topFrame.pack(fill=tk.X)

        self.top1 = ttk.Frame(self.topFrame)
        greeting_text = self.get_greeting_text()
        greeting_label = ttk.Label(self.top1, text=greeting_text, 
                                 font=("Helvetica", 35, "bold"), 
                                 foreground="#4966FF")
        greetingTextLabel = ttk.Label(self.top1, 
                                    text="Let's make the best out of your day together with Rebuilt", 
                                    font=("Helvetica", 15))
        greeting_label.pack(anchor="w")
        greetingTextLabel.pack(anchor="w", pady=20)

        self.top2 = ttk.Frame(self.topFrame)
        self.top3 = ttk.Frame(self.topFrame)
        self.top4 = ttk.Frame(self.topFrame)

        self.top1.pack(side="left", fill=tk.Y, pady=5)

        proyekList = self.controller.getAllProyek()
        completed_cnt = sum(1 for proyek in proyekList if proyek.get_progressProyek() == 100)
        ongoing_cnt = sum(1 for proyek in proyekList if proyek.get_progressProyek() < 100)
        
        # top4 part

        onProgressNum = ttk.Label(self.top4, text=str(ongoing_cnt), 
                                font=("Helvetica", 25, "bold"))
        onProgressNum.pack(pady=(0, 10))
        
        self.textTop4 = ctk.CTkFrame(
            self.top4,
            corner_radius=int(10),  # Rounded corners
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

        # finishedWeekNum = ttk.Label(self.top3, text="11", 
        #                         font=("Helvetica", 25, "bold"))
        # finishedWeekNum.pack(pady=(0, 10))
        
        # self.textTop3 = ctk.CTkFrame(
        #     self.top3,
        #     corner_radius=10,  # Rounded corners
        #     fg_color="#4966FF",    # Background color
        #     bg_color="transparent"  # Transparent background
        # )
        
        # projectsFinishedWeekText = ctk.CTkLabel(
        #     self.textTop3,
        #     text="Projects Finished",
        #     font=("Helvetica", 16, "bold"),
        #     text_color="white"
        # )
        
        # thisWeekText = ctk.CTkLabel(
        #     self.textTop3,
        #     text="This Week",
        #     font=("Helvetica", 16, "bold"),
        #     text_color="white"
        # )
        
        # projectsFinishedWeekText.pack()
        # thisWeekText.pack()
        # self.textTop3.pack(padx=10, ipadx=10, ipady=1)
        
        # top2 part

        finishedTotalNum = ttk.Label(self.top2, text=str(completed_cnt), 
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
        
        canvas.create_line(0, 1, self.winfo_width(), 1, fill="black", width=2)

        
        
        # bottom content part
        
        self.bottomFrame = ttk.Frame(self.main_frame)
        self.bottomFrame.pack(fill=tk.BOTH,expand=True, pady=20)
        
        
        # projects part
        
        self.projectsContainer = ttk.Frame(self.bottomFrame)
        self.projectsContainer.pack(side="left", fill=tk.BOTH)
        #first row of projectContainer
        
        self.projectsContainerRow1= ttk.Frame(self.bottomFrame)
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
                       command=self.open_add_proyek_window,
                       style="Transparent.TButton")  # Apply a custom style for transparency
        addButton.image = addButtonImg  # Keep a reference to the image (important to avoid garbage collection)
        addButton.pack(pady=10, padx=20, side="left")  # Packing the button after the title

        # Customize the appearance of the Combobox
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#FFFFFF")],  # White background for the field
            background=[("readonly", "#FFFFFF")],      # White background for the dropdown
            foreground=[("readonly", "black")],        # Black text color
            selectbackground=[("readonly", "#FFFFFF")], # Remove the blue highlight
            selectforeground=[("readonly", "black")],   # Black text color for selected items
        )
        # dropdown sort
        sort_options = {
            "ID (Ascending)": ("idProyek", True),
            "ID (Descending)": ("idProyek", False),
            "Progress (Ascending)": ("progressProyek", True),
            "Progress (Descending)": ("progressProyek", False),
        }
        self.sort_options = sort_options
        dropdown = ttk.Combobox(self.projectsContainerRow1, 
                        values=list(sort_options.keys()),  # Set the dropdown options
                        state="readonly",          # Makes the combobox read-only (can't type in)
                        width=20)                  # Width of the dropdown
        dropdown.set("ID (Ascending)")  # Default value
        dropdown.pack(side="right", padx=(350,5), pady=10)
        dropdown.bind("<<ComboboxSelected>>", self.on_sort_selected)
        
        
        self.scrollable_projects_frame = ScrollableFrame(self.bottomFrame)  # Pack inside projectsContainer
        self.scrollable_projects_frame.pack(fill=tk.BOTH, expand=True)  # Fill remaining space in projectsContainer

        # Call the create_project_cards method
        # Fetch projects from the database
        self.refresh_projects("idProyek", True)  # Default sorting
    
    def on_sort_selected(self, event):
        """Handle dropdown selection for sorting."""
        selected_option = event.widget.get()
        if selected_option in self.sort_options:
            sort_by, asc = self.sort_options[selected_option]
            self.refresh_projects(sort_by, asc)
    
    def create_project_cards(self, proyek_list):
        """Dynamically creates project cards based on the list of Proyek objects."""
        self.rightArrowButtonImg = tk.PhotoImage(file="img/right-arrow.png")
        parent_frame = self.scrollable_projects_frame.scrollable_frame

        # Number of cards per row
        columns = 5
        current_row_frame = None

        card_width = 210
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
                current_row_frame.pack(fill=tk.X, pady=10, expand=True)

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
            card.pack(side=tk.LEFT, padx=10, pady=10)
            card.pack_propagate(False)  # Prevent the frame from resizing to fit its content

            # Create a frame inside the card for internal padding
            inner_frame = ttk.Frame(card, style="Inner.TFrame")
            inner_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            # Populate the card with project details
            judulLabel = ttk.Label(
                inner_frame, 
                text=proyek.get_judulProyek(), 
                style="JudulLabel.TLabel", 
                foreground="#4966FF"
            )
            judulLabel.pack(anchor="w", pady=(0, 5))

            date_label = ttk.Label(
                inner_frame, 
                text=f"{proyek.get_tanggalMulaiProyek()}", 
                style="TanggalLabel.TLabel"
            )
            date_label.pack(anchor="w", pady=(0, 5))

            # Truncate description if it exceeds a maximum length
            MAX_DESC_LENGTH = 50
            desc_text = proyek.get_descProyek()
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
            progress_value = proyek.get_progressProyek()  # Progress value from 0 to 100
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
                command= lambda idProyek = proyek.get_idProyek(): self.onRightArrowClick(idProyek)
            )
            right_arrow_button.pack(side="right")

            
    def displayProyekById(self, idProyek):
        proyek = self.controller.getProyekById(idProyek)
        if not proyek:
            tk.messagebox.showerror("Error", "Project not found!")
            return
        # Hide all existing content
        
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

        # Create a new container for the detailed view
        proyekDetailFrame = ttk.Frame(self.main_frame)
        proyekDetailFrame.pack(fill=tk.BOTH, expand=True, padx=20)

        # Configure the detailed view layout with `grid`
        proyekDetailFrame.columnconfigure(0, weight=1, uniform="half")  # Left frame
        proyekDetailFrame.columnconfigure(1, weight=1, uniform="half")  # Right frame

        # Add the left frame
        leftProyekFrame = ttk.Frame(proyekDetailFrame)
        leftProyekFrame.grid(row=0, column=0, sticky="nsew")  # Fill the first column

        style = ttk.Style()

        # Add a back button
        back_button = ttk.Button(leftProyekFrame, text="← Back",
                                command=lambda: (self.refresh_projects(), self.show_main_view()))
        back_button.pack(anchor="w", pady=(10, 20))

        # Add a title frame and label
        titleRowFrame = ttk.Frame(leftProyekFrame)
        titleRowFrame.pack(fill=tk.X, pady=(10, 20))  # Pack the title frame first

        # Configure grid layout for the titleRowFrame
        titleRowFrame.columnconfigure(0, weight=1)  # Allow column 0 to expand
        titleRowFrame.columnconfigure(1, weight=0)

        # Add the project title
        proyekJudul = ttk.Label(titleRowFrame, text=proyek.judulProyek,
                                font=("Helvetica", 30, "bold"), foreground="#4966FF")
        proyekJudul.grid(row=0, column=0, sticky="w")  # Place in the first column

        # Add the project start date beside the title
        proyekTanggalMulai = ttk.Label(titleRowFrame, text=proyek.tanggalMulaiProyek.strftime("%d-%m-%Y") if proyek.tanggalMulaiProyek else "N/A",
                                    font=("Helvetica", 13, "italic"), foreground="red")
        proyekTanggalMulai.grid(row=0, column=1, sticky="w", padx=(0, 15))  # Place in the second column

        MAX_DESC_LENGTH = 200
        desc_text = proyek.descProyek
        if len(desc_text) > MAX_DESC_LENGTH:
            desc_text = desc_text[:MAX_DESC_LENGTH] + "..."
        style.configure(
            "ProjectLabel.TLabel",
            background="SystemButtonFace",  # Matches default background of ttk frames
            font=("Helvetica", 13)
        )
        descLabel = ttk.Label(
            leftProyekFrame,
            style="ProjectLabel.TLabel",
            text=desc_text,
            wraplength=600,  # Ensure text still wraps within the card
            justify="left"   # Align text to the left
        )
        descLabel.pack(anchor="w", pady=(10, 0))

        # Create a container frame for the buttons
        buttonsFrame = ttk.Frame(leftProyekFrame)
        buttonsFrame.pack(anchor="w", pady=(10, 0))  # Pack the frame below the description

        # Add the delete button
        # Store the PhotoImage objects as instance variables
        self.deleteProyekImgButton = tk.PhotoImage(file="img/deleteProyek.png")
        self.editProyekImgButton = tk.PhotoImage(file="img/editProyek.png")

        # Add the delete button
        
        deleteProyekButton = tk.Button(
            buttonsFrame,
            image=self.deleteProyekImgButton,  # Using the instance variable
            borderwidth=0,
            cursor="hand2",
            command=lambda idProyek=idProyek: self.displayDeleteProyek(idProyek)  # Properly delay execution
        )
        deleteProyekButton.pack(side=tk.LEFT, padx=(0, 10))  # Add right padding

        # Add the edit button
        editProyekButton = tk.Button(
            buttonsFrame,
            image=self.editProyekImgButton,  # Using the instance variable
            borderwidth=0,
            cursor="hand2",
            command=lambda: self.open_edit_proyek_window(idProyek)
        )
        editProyekButton.pack(side=tk.LEFT)

        # Add the 4-grid layout
        gridFrame = ttk.Frame(leftProyekFrame)
        gridFrame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

        # count = self.controller.getTugasStatusCounts(idProyek)

        # if count[0]+count[1]==0:  # Pengecekan jika belum ada tugas
        # Configure the grid layout with 2 rows and 2 columns
        gridFrame.columnconfigure(0, weight=1, uniform="grid")
        gridFrame.columnconfigure(1, weight=1, uniform="grid")
        gridFrame.rowconfigure(0, weight=1, uniform="grid")
        gridFrame.rowconfigure(1, weight=1, uniform="grid")
    
        def create_grid_with_pie_chart(parent, percentage, description):
            # Create a CTkFrame with rounded corners and border
            if percentage <= 1:  # Assuming progress might be a float (e.g., 0.0 to 1.0)
                percentage *= 100
            frame = ctk.CTkFrame(
                parent, 
                corner_radius=15, 
                fg_color="#FFFFFF", 
                border_color="#7A7E93", 
                border_width=2
            )
            frame.grid_propagate(False)
            frame.configure(width=270, height=180)
            frame.pack_propagate(False)

            # Create a container for all content inside the frame
            content_frame = ctk.CTkFrame(
                frame, 
                corner_radius=0, 
                fg_color="#FFFFFF"  # Ensure consistent white background inside
            )
            content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

            # Create the pie chart and embed it into this frame
            fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
            data = [percentage, 100 - percentage]
            colors = ['#D1FF33', '#E0E0E0']
            ax.pie(data, colors=colors, startangle=90, counterclock=False)

            # Add the percentage text inside the circle
            ax.text(0, 0.2, f'{percentage}%', ha='center', va='center', fontsize=18, color='#4966FF', fontweight='bold')

            # Add the description text inside the circle below the percentage
            ax.text(0, -0.3, description, ha='center', va='center', fontsize=12, color='black', fontweight='bold')

            # Remove axes and adjust padding
            ax.axis('equal')
            ax.set_position([0.05, 0.05, 0.9, 0.9])

            # Embed the pie chart into the Tkinter frame
            canvas = FigureCanvasTkAgg(fig, content_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

            return frame



        def create_grid_with_numbers(parent, number1, number2, label1, label2):
        # Create a CTkFrame with rounded corners and border
            frame = ctk.CTkFrame(
                parent, 
                corner_radius=15, 
                fg_color="#FFFFFF", 
                border_color="#7A7E93", 
                border_width=2
            )
            frame.grid_propagate(False)
            frame.configure(width=260, height=170)
            frame.pack_propagate(False)

            # Create a container for all content inside the frame
            content_frame = ctk.CTkFrame(
                frame, 
                corner_radius=0, 
                fg_color="#FFFFFF"  # Ensure consistent white background inside
            )
            content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

            # Add the top row for the numbers
            numbers_frame = ttk.Frame(content_frame)
            numbers_frame.pack(anchor="center", pady=(15, 10))

            label_number1 = ttk.Label(numbers_frame, text=number1, font=("Helvetica", 25, "bold"), foreground="black", background="#FFFFFF")
            label_number1.pack(side="left", padx=(5, 0))

            colon_label = ttk.Label(numbers_frame, text=" : ", font=("Helvetica", 25, "bold"), foreground="black", background="#FFFFFF")
            colon_label.pack(side="left", padx=(0, 0))

            label_number2 = ttk.Label(numbers_frame, text=number2, font=("Helvetica", 25, "bold"), foreground="black", background="#FFFFFF")
            label_number2.pack(side="right", padx=(0, 5))

            # Add the bottom row for the labels
            labels_frame = ttk.Frame(content_frame)
            labels_frame.pack(fill="x", pady=(10, 0))

            # Configure the grid layout for labels_frame
            labels_frame.columnconfigure(0, weight=1)  # First half of the frame
            labels_frame.columnconfigure(1, weight=1)  # Second half of the frame

            # Left label (On Progress Tugas)
            left_label = ttk.Label(
                labels_frame,
                text=label1,
                font=("Helvetica", 12, "bold"),
                background="#4966FF",
                foreground="white",
                wraplength=110,  # Ensure wrapping
                anchor="center",
                justify="center"
            )
            left_label.grid(row=0, column=0, padx=(2, 2), pady=0, sticky="ew")  # Sticky ensures full width in the column

            # Right label (Completed Tugas)
            right_label = ttk.Label(
                labels_frame,
                text=label2,
                font=("Helvetica", 12, "bold"),
                background="#4966FF",
                foreground="white",
                wraplength=110,  # Ensure wrapping
                anchor="center",
                justify="center"
            )
            right_label.grid(row=0, column=1, padx=(2, 5), pady=0, sticky="ew")  # Sticky ensures full width in the column

            return frame




        def create_grid_with_expenses(parent, total, estimated):
            # Create a CTkFrame with rounded corners and border
            frame = ctk.CTkFrame(
                parent, 
                corner_radius=15, 
                fg_color="#FFFFFF", 
                border_color="#7A7E93", 
                border_width=2
            )
            frame.grid_propagate(False)
            frame.configure(width=270, height=180)
            frame.pack_propagate(False)

            # Add labels
            total_label = ttk.Label(frame, text="Total Pengeluaran", font=("Helvetica", 14, "bold"), foreground="black", background="#FFFFFF")
            total_label.pack(anchor="w", pady=(20, 0), padx=10)

            total_value_label = ttk.Label(frame, text=total, font=("Helvetica", 18, "bold"), foreground="#4966FF", background="#FFFFFF")
            total_value_label.pack(anchor="w", padx=10)

            estimated_label = ttk.Label(frame, text="Estimasi Pengeluaran", font=("Helvetica", 14, "bold"), foreground="black", background="#FFFFFF")
            estimated_label.pack(anchor="w", pady=(10, 0), padx=10)

            estimated_value_label = ttk.Label(frame, text=estimated, font=("Helvetica", 18, "bold"), foreground="#4966FF", background="#FFFFFF")
            estimated_value_label.pack(anchor="w", padx=10)

            return frame



        def create_grid_with_spending_percentage(parent, percentage, description):
            # Create a CTkFrame for the grid card with rounded corners and border
            card = ctk.CTkFrame(
                parent,
                width=270,
                height=180,
                corner_radius=15,  # Rounded corners
                fg_color="#FFFFFF",  # Background color
                border_color="#7A7E93",  # Border color
                border_width=2,  # Border width
            )
            card.grid_propagate(False)
            card.pack_propagate(False)  # Prevent resizing to fit content

            # Create an inner frame to hold the content
            inner_frame = ttk.Frame(card, style="InnerFrame.TFrame")
            inner_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            # Set the style for the inner frame
            style = ttk.Style()
            style.configure("InnerFrame.TFrame", background="#FFFFFF")

            # Create a vertical container for centering all elements
            vertical_container = ttk.Frame(inner_frame, style="InnerFrame.TFrame")
            vertical_container.pack(expand=True, fill="both")  # Vertically and horizontally centers everything

            # Add percentage label
            percentage_label = ttk.Label(
                vertical_container,
                text=percentage,
                font=("Helvetica", 30, "bold"),
                foreground="#4966FF",
                background="#FFFFFF",  # Set background explicitly
                anchor="center",  # Center-align widget
                justify="center",  # Center-align text inside the widget
            )
            percentage_label.pack(pady=(25, 5))  # Add vertical padding

            # Add description with centered alignment
            description_label = ttk.Label(
                vertical_container,
                text=description,
                font=("Helvetica", 13),
                foreground="black",
                background="#FFFFFF",  # Set background explicitly
                wraplength=240,
                justify="center",  # Center-align multi-line text
                anchor="center",  # Center-align widget
            )
            description_label.pack(pady=(5, 10))  # Add vertical padding

            return card


        proyek = self.controller.getProyekById(idProyek)

        count = self.controller.getTugasStatusCounts(idProyek)

        biaya = self.controller.getSumBiaya(idProyek)

        realBiaya = self.controller.getRealBiaya(idProyek)
        
        if count[0]==0 and count[1]==0:
            create_grid_with_pie_chart(
                gridFrame, 
                0, 
                "Completed"
            ).grid(row=0, column=0, padx=(0, 5), pady=10)
            create_grid_with_numbers(gridFrame, "0", "0", "On Progress Tugas", "Completed Tugas").grid(row=0, column=1, padx=(5, 0), pady=10)
            create_grid_with_expenses(gridFrame, f"{realBiaya}", f"{biaya}").grid(row=1, column=0, padx=(0, 5), pady=10)
            create_grid_with_spending_percentage(gridFrame, f"{round((realBiaya / biaya) * 100, 2)}%", "Money spent out of your estimation").grid(row=1, column=1, padx=(5, 0), pady=10)
        
        else:
            print(count[0], count[1])

            if proyek:
                progress = count[0]/(count[1] + count[0])
                progress = round(progress, 2)  # Round to 2 decimal places
                print(f"Progress for project {idProyek}: {progress}")
                create_grid_with_pie_chart(
                    gridFrame, 
                    progress, 
                    "Completed"
                ).grid(row=0, column=0, padx=(0, 5), pady=10)
            else:
                print(f"No project found with id {idProyek}")

            

            create_grid_with_numbers(gridFrame, f"{count[1]}", f"{count[0]}", "On Progress Tugas", "Completed Tugas").grid(row=0, column=1, padx=(5, 0), pady=10)
            create_grid_with_expenses(gridFrame, f"{realBiaya}", f"{biaya}").grid(row=1, column=0, padx=(0, 5), pady=10)
            create_grid_with_spending_percentage(gridFrame, f"{round((realBiaya / biaya) * 100, 2)}%", "Money spent out of your estimation").grid(row=1, column=1, padx=(5, 0), pady=10)
            

        # Add a placeholder for the right frame
        rightProyekFrame = ttk.Frame(proyekDetailFrame)
        rightProyekFrame.grid(row=0, column=1, sticky="nsew")
        # Integrate DisplayTugas into rightProyekFrame
        self.tugas_controller = PengelolaTugasProyek()
        # In displayProyekById method:
        displayTugas = DisplayTugas(rightProyekFrame, controller=self.tugas_controller, main_frame=proyekDetailFrame, idProyekOfTugas = idProyek)
        displayTugas.pack(fill="both", expand=True)
        # self.refresh_display_proyek_by_id(idProyek)


    def open_edit_proyek_window(self, idProyek):
        proyek = self.controller.getProyekById(idProyek)
        if not proyek:
            tk.messagebox.showerror("Error", "Project not found!")
            return
        # Create a new top-level window
        edit_window = tk.Toplevel()
        edit_window.title("Edit Proyek Detail")
        edit_window.geometry("500x600")
        edit_window.configure(bg="#FFFFFF")  # Set background color

        
        self.leftArrowButtonImg = tk.PhotoImage(file="img/left-arrow.png")
        back_button = tk.Button(
            edit_window,
            image=self.leftArrowButtonImg,  # Using the class variable
            borderwidth=0,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            cursor="hand2",
            command=edit_window.destroy
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
            text="Judul proyek",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        project_title_label.pack(anchor="w", padx=20, pady=(10, 5))

        project_title_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,  # Border radius
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"  # Light gray border
        )
        project_title_container.pack(fill="x", padx=20, pady=(0, 20))

        project_title_entry = tk.Entry(
            project_title_container,
            font=("Helvetica", 12),
            bg="#FFFFFF",
            bd=0,  # Remove default border
            highlightthickness=0,  # Remove focus border
        )
        project_title_entry.insert(0, proyek.get_judulProyek())
        project_title_entry.pack(fill="x", padx=10, pady=5)

        # Description Section
        description_label = ttk.Label(
            edit_window,
            text="Deskripsi",
            font=("Helvetica", 14, "bold"),
            foreground="#4966FF",
            background="#FFFFFF"
        )
        description_label.pack(anchor="w", padx=20, pady=(10, 5))

        description_container = ctk.CTkFrame(
            edit_window,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D3D3D3"
        )
        description_container.pack(fill="both", padx=20, pady=(0, 20))

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
            height=10,
        )
        description_text.insert("1.0", proyek.get_descProyek())
        description_text.pack(fill="both", padx=10, pady=5)
        
        def save_changes():
            title = project_title_entry.get().strip()
            description = description_text.get("1.0", "end-1c").strip()

            if not title or not description:
                tk.messagebox.showerror("Error", "Judul proyek dan deskripsi tidak boleh kosong!")
                return

            updated_proyek = Proyek(
                idProyek=idProyek,
                judulProyek=title,
                descProyek=description,
                progressProyek=proyek.get_progressProyek(),
                biayaProyek=proyek.get_biayaProyek(),
                estimasiBiayaProyek=proyek.get_estimasiBiayaProyek(),
                tanggalMulaiProyek=proyek.get_tanggalMulaiProyek(),
                tanggalSelesaiProyek=proyek.get_tanggalSelesaiProyek(),
                statusProyek=proyek.get_statusProyek()
            )
            success = self.controller.editProyek(updated_proyek)
            if success:
                tk.messagebox.showinfo("Success", "Proyek berhasil diperbarui!")
                edit_window.destroy()
                # Call refresh_display_proyek_by_id to update the view
                self.refresh_display_proyek_by_id(idProyek)
            else:
                tk.messagebox.showerror("Error", "Gagal memperbarui proyek.")



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
            command=save_changes
        )
        save_button.pack(side="bottom", pady=20)

        edit_window.mainloop()
    
    def open_add_proyek_window(self):
        # Create a new top-level window
        add_window = tk.Toplevel()
        add_window.title("Add Proyek")
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
            text="[Add Proyek]",
            font=("Helvetica", 20, "bold"),
            anchor="w",
            justify="left",
            bg="#FFFFFF",
            fg="black",
        )
        title_label.pack(fill="x", padx=20, pady=10)

        fields = {}
        field_names = [
            "Judul proyek", "Deskripsi"
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
        def save_addproyek():
            try:
                # Collect data from fields
                new_proyek = Proyek(
                    judulProyek=fields["Judul proyek"].get(),  # Use .get() to retrieve text from Entry
                    descProyek=fields["Deskripsi"].get(),      # Use .get() to retrieve text from Entry
                    progressProyek=0,
                    biayaProyek=0,
                    estimasiBiayaProyek=0,
                    tanggalMulaiProyek=datetime.date.today().isoformat(),
                    statusProyek="On Progress"
                )

                # Call the controller to save the project
                success = self.controller.addProyek(new_proyek)  # This should be implemented in your controller
                if success:
                    tk.messagebox.showinfo("Success", "Proyek berhasil ditambahkan!")
                    add_window.destroy()
                    self.refresh_projects()
                else:
                    tk.messagebox.showerror("Error", "Gagal menambahkan proyek.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


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
            command=save_addproyek
        )
        save_button.pack(side="bottom", pady=20)

        add_window.mainloop()

        
    def displayDeleteProyek(self, idProyek):
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
            success = self.controller.deleteProyek(idProyek)
            if success:
                tk.messagebox.showinfo("Success", "Proyek berhasil dihapus!")
                delete_window.destroy()  # Close the delete confirmation window
                self.refresh_projects()  # Refresh the project list or view
                self.show_main_view()
            else:
                tk.messagebox.showerror("Error", "Gagal menghapus proyek. Silakan coba lagi.")

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
    
    def displaySaveProyek(self, edit_window, updated_proyek):
        # Create a new top-level window
        saveWindow = tk.Toplevel()
        saveWindow.title("Save Confirmation")
        saveWindow.geometry("400x250")
        saveWindow.configure(bg="#FFFFFF")  # Set background color

        self.saveIcon = "img/save.png"        
        self.saveImage = tk.PhotoImage(file=self.saveIcon)

        saveLabel = tk.Label(
            saveWindow,
            image=self.saveImage,
            bg="#FFFFFF"
        )

        saveLabel.pack(pady=(30, 10))

        # Add confirmation text
        confirmationLabel = tk.Label(
            saveWindow,
            text="Yakin ingin menyimpan perubahan?",
            font=("Helvetica", 14, "bold"),
            bg="#FFFFFF",
            fg="#000000"
        )
        confirmationLabel.pack(pady=(10, 20))

        # Button frame
        buttonFrame = tk.Frame(saveWindow, bg="#FFFFFF")
        buttonFrame.pack(pady=(10, 10))

        # "Tidak" (No) button
        noButton = ctk.CTkButton(
            buttonFrame,
            text="Tidak",
            font=("Helvetica", 14, "bold"),
            fg_color="#000000",
            text_color="#FFFFFF",
            hover_color="#333333",
            corner_radius=5,
            width=100,
            height=40,
            command=saveWindow.destroy  # Close the window on "No"
        )
        noButton.pack(side="left", padx=(0, 10))

        def save_to_database():
            success = self.controller.editProyek(updated_proyek)
            if success:
                tk.messagebox.showinfo("Success", "Proyek berhasil diperbarui!")
                saveWindow.destroy()
                edit_window.destroy()
                self.refresh_display_proyek_by_id()  # Refresh the projects list
                
            else:
                tk.messagebox.showerror("Error", "Gagal memperbarui proyek. Silakan coba lagi.")
        # "Iya" (Yes) button
        yesButton = ctk.CTkButton(
            buttonFrame,
            text="Simpan",
            font=("Helvetica", 14, "bold"),
            fg_color="#4966FF",
            text_color="#FFFFFF",
            hover_color="#435CE1",
            corner_radius=5,
            width=100,
            height=40,
            command=save_to_database
        )
        yesButton.pack(side="left", padx=(10, 0))

        saveWindow.mainloop()


    def onInspirasi(self):
        print("Right arrow clicked!")
        # Navigate to the DisplayTugas frame
        command=lambda: self.controller.show_frame(DisplayInspirasi)

    def onAddButtonClick(self):
        print("Add button clicked!")
        
    def onRightArrowClick(self, idProyek):
        print("Right arrow clicked!")
        # Navigate to the DisplayTugas frame
        self.displayProyekById(idProyek=idProyek)
        
    def onDeleteButtonClick(self):
        print("delete clicked!")
    
    def onEditButtonClick(self):
        print("edit clicked!")
    
    def show_main_view(self):
        # Clear the current view
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()
            
        # Re-setup the original UI
        self.setup_ui()
    
    def refresh_projects(self, sort_by="idProyek", asc=False):
        """Refresh the project cards based on the selected sorting."""
        proyek_list = self.controller.getAllProyek(sort_by=sort_by, asc=asc)

        # Clear existing project cards
        for widget in self.scrollable_projects_frame.scrollable_frame.winfo_children():
            widget.destroy()

        # Recreate project cards
        self.create_project_cards(proyek_list)

        # Reset the scrollable frame's scroll region
        self.scrollable_projects_frame.canvas.configure(
            scrollregion=self.scrollable_projects_frame.canvas.bbox("all")
        )
    
    def refresh_display_proyek_by_id(self, idProyek):
        """Refresh the detailed view of a specific project."""
        # Fetch the updated project data
        proyek = self.controller.getProyekById(idProyek)
        if not proyek:
            tk.messagebox.showerror("Error", "Project not found!")
            return

        # Clear the current detailed view
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

        # Re-display the updated project details
        self.displayProyekById(idProyek)


# Instantiate and run the program
if __name__ == "__main__":
    controller = None  # Replace with the actual controller if needed
    app = DisplayProyek(controller)
    app.window.mainloop()