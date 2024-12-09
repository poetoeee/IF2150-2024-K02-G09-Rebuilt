from tkinter import messagebox
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class DisplayTugas:
    def __init__(self, controller):
        self.window = ttk.Window(themename="flatly")
        self.window.title("Tugas Management")
        self.window.state('zoomed')  # Fullscreen
        self.controller = controller

        self.displayAllTugas()

    def displayAllTugas(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Top Frame (40% height)
        topFrame = ttk.Frame(self.window, padding=10, height=0.4*screen_height, width=screen_width)
        topFrame.place(relx=0, rely=0, relwidth=1, relheight=0.4)

        # Bottom Frame (60% height for the design)
        bottomFrame = ttk.Frame(self.window, padding=10, height=0.6*screen_height, width=screen_width)
        bottomFrame.place(relx=0, rely=0.4, relwidth=1, relheight=0.6)

        # Call method to populate frames
        self.populateTopFrame(topFrame)
        self.populateBottomFrame(bottomFrame)

    def populateTopFrame(self, frame):
        label = ttk.Label(frame, text="[Tugas Management - Header Section]", font=("Helvetica", 16, "bold"))
        label.pack()

    def populateBottomFrame(self, frame):
        # Treeview styling for table-like view
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.configure("Treeview", font=("Helvetica", 10), rowheight=30)

        # Table Title
        title = ttk.Label(frame, text="[Biaya]", font=("Helvetica", 16, "bold"))
        title.pack(anchor="w", pady=(0, 10))

        # Scrollable Frame
        container = ttk.Frame(frame)
        container.pack(fill="both", expand=True)

        # Create a Treeview and Scrollbar
        columns = ("Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi")
        table = ttk.Treeview(container, columns=columns, show="headings", style="Treeview")
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=table.yview)

        # Configure Treeview to use the scrollbar
        table.configure(yscrollcommand=scrollbar.set)

        # Pack the Treeview and scrollbar
        table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Define column headings
        table.heading("Barang", text="Barang")
        table.heading("Harga", text="Harga")
        table.heading("Qty", text="Qty")
        table.heading("Total", text="Total")
        table.heading("Keterangan", text="Keterangan")
        table.heading("Aksi", text="Aksi")

        # Define column widths
        table.column("Barang", width=150, anchor="center")
        table.column("Harga", width=100, anchor="center")
        table.column("Qty", width=50, anchor="center")
        table.column("Total", width=100, anchor="center")
        table.column("Keterangan", width=200, anchor="center")
        table.column("Aksi", width=100, anchor="center")

        # Add table rows (mock data for now)
        data = [
            ("Semen", "Rp9.000", "12", "Rp108.000", "", "✏️ 🗑️"),
            ("Pasir", "Rp9.000", "12", "Rp108.000", "", "✏️ 🗑️"),
            ("Pegawai", "Rp9.000", "12", "Rp108.000", "", "✏️ 🗑️"),
            ("Cat dinding", "Rp9.000", "12", "Rp108.000", "", "✏️ 🗑️"),
            # Add more rows for testing
        ] * 10  # Repeat to make the table overflow and require scrolling

        for row in data:
            table.insert("", "end", values=row)

        # Total Cost Label
        total_label = ttk.Label(frame, text="TOTAL   Rp432.000,00", font=("Helvetica", 14, "bold"), anchor="w")
        total_label.pack(anchor="w", padx=10, pady=10)

        # Add Button
        add_button = ttk.Button(frame, text="➕ Add", bootstyle="primary", command=self.addRow)
        add_button.pack(side="right", padx=10, pady=10)


    def addRow(self):
        messagebox.showinfo("Add Row", "Tombol Add ditekan!")


# Mock Controller
class MockController:
    def getAllTugas(self):
        return []



# Run the application
if __name__ == "__main__":
    controller = MockController()
    app = DisplayTugas(controller)
    app.window.mainloop()
