def create_project_cards(self, proyek_list):
        # Use the scrollable frame for project cards
        parent_frame = self.scrollable_projects_frame.scrollable_frame

        # Number of cards per row
        columns = 3
        current_row_frame = None

        card_width = 200
        card_height = 220

        # Create a style for the inner frame and label elements
        style = ttk.Style()
        style.configure("Inner.TFrame", background="#FFFFFF")  # Same as card background color
        style.configure("ProjectLabel.TLabel", background="#FFFFFF", anchor="w", font=("Helvetica", 12))  # Labels styling
        style.configure("JudulLabel.TLabel", background="#FFFFFF", anchor="w", font=("Helvetica", 18, "bold"))  # Labels styling
        style.configure("TanggalLabel.TLabel", background="#FFFFFF", anchor="w", font=("Helvetica", 12, "italic"))  # Labels styling

        # Style for the progress bar
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor="#E0E0E0",  # Background color of the trough
            bordercolor="#7A7E93",  # Border color of the progress bar
            background="#FF0000",  # Progress bar fill color
            lightcolor="#4966FF",  # Top gradient color (if applicable)
            darkcolor="#4966FF",  # Bottom gradient color (if applicable)
            thickness=10,  # Height of the progress bar
        )

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
            date_label = ttk.Label(inner_frame, text=f"{proyek['date']}", style="TanggalLabel.TLabel")

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

            # Create a progress bar for the progress percentage
            progress_value = proyek["progress"]  # Progress value from 0 to 100
            progress_bar = ttk.Progressbar(
                inner_frame,
                length=90,  # Set progress bar width
                maximum=100,  # Maximum value for the progress bar
                mode="determinate",  # Determinate mode for exact progress
                style="Custom.Horizontal.TProgressbar",  # Use custom style
            )
            progress_bar["value"] = progress_value  # Set the current progress value

            # Add status label
            status_label = ttk.Label(
                inner_frame,
                text=f"Status: {proyek['status']}",
                style="ProjectLabel.TLabel",
                foreground="green" if proyek["status"] == "Done" else "orange"
            )

            # Add labels and progress bar to the inner frame
            judulLabel.pack(anchor="w", pady=(0, 5))
            date_label.pack(anchor="w", pady=(0, 5))
            descLabel.pack(anchor="w", pady=(0, 5))
            progress_bar.pack(anchor="w", pady=(5, 5))  # Add some padding for the progress bar
            status_label.pack(anchor="w")