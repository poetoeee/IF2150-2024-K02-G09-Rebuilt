import ttkbootstrap as tb
from tkinter import Canvas, ttk, PhotoImage

# Fungsi Edit dan Delete Placeholder
def edit_action():
    print("Edit Clicked")

def delete_action():
    print("Delete Clicked")

# Data Tabel
data = [
    ("Semen", "Rp9.000", "12", "Rp108.000", "-", ""),
    ("Pasir", "Rp9.000", "12", "Rp108.000", "-", ""),
    ("Pegawai", "Rp9.000", "12", "Rp108.000", "-", ""),
    ("Cat dinding", "Rp9.000", "12", "Rp108.000", "-", ""),
    ("Batu", "Rp15.000", "8", "Rp120.000", "-", ""),
    ("Keramik", "Rp50.000", "6", "Rp300.000", "-", ""),
    ("Kayu", "Rp30.000", "10", "Rp300.000", "-", ""),
    ("Paku", "Rp5.000", "15", "Rp75.000", "-", ""),
]

# Aplikasi Utama
app = tb.Window(themename="cosmo")
app.title("Biaya GUI with Canvas and Grid Example")
app.geometry("900x500")

# Frame Utama
main_frame = ttk.Frame(app, padding=10, relief="ridge")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Header
header_label = ttk.Label(main_frame, text="Biaya", font=("Arial", 16, "bold"))
header_label.pack(anchor="w", pady=(0, 10))

# Scrollable Canvas Area
canvas_frame = ttk.Frame(main_frame)
canvas_frame.pack(fill="both", expand=True)

# Scrollbar dan Canvas
scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

canvas = Canvas(canvas_frame, yscrollcommand=scrollbar.set, bg="white")
canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=canvas.yview)

# Frame untuk Grid di dalam Canvas
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Event resize untuk menyesuaikan kolom saat canvas diperbesar
def resize_columns(event):
    total_width = event.width
    col_width = total_width // len(headers)  # Lebar masing-masing kolom
    for col_index, header in enumerate(headers):
        for widget in scrollable_frame.grid_slaves(column=col_index):
            widget.configure(width=col_width // 10)

canvas.bind("<Configure>", resize_columns)

# Update scrollregion saat ukuran berubah
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Header Grid
headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
for col_index, header in enumerate(headers):
    label = ttk.Label(
        scrollable_frame,
        text=header,
        font=("Arial", 14, "bold"),
        background="#f0f0f0",
        anchor="center",
        padding=5
    )
    label.grid(row=0, column=col_index, sticky="nsew", padx=1, pady=1)

# Set column weights for equal spacing
for col_index in range(len(headers)):
    scrollable_frame.columnconfigure(col_index, weight=1)

# Load Icons
edit_icon = PhotoImage(file="editbutton.png").subsample(3, 3)
delete_icon = PhotoImage(file="deletebutton.png").subsample(3, 3)

# Isi Data ke dalam Grid
for row_index, row_data in enumerate(data, start=1):
    for col_index, cell_data in enumerate(row_data[:-1]):
        label = ttk.Label(
            scrollable_frame,
            text=f"{cell_data}",
            font=("Arial", 12),
            anchor="center",
            padding=5
        )
        label.grid(row=row_index, column=col_index, sticky="nsew", padx=1, pady=1)
    
    # Tambahkan Edit dan Delete Buttons di kolom Aksi
    action_frame = ttk.Frame(scrollable_frame)
    action_frame.grid(row=row_index, column=len(headers) - 1, sticky="nsew", padx=5, pady=5)

    # Edit Button
    edit_btn = ttk.Button(action_frame, image=edit_icon, command=edit_action)
    edit_btn.pack(side="left", padx=5)

    # Delete Button
    delete_btn = ttk.Button(action_frame, image=delete_icon, command=delete_action)
    delete_btn.pack(side="left", padx=5)

# Total Label dan Add Button
bottom_frame = ttk.Frame(main_frame)
bottom_frame.pack(fill="x", pady=(10, 0))

total_label = ttk.Label(
    bottom_frame,
    text="TOTAL   Rp1.134.000,00",
    font=("Arial", 12, "bold"),
    foreground="#4B74FF"
)
total_label.pack(side="left")

add_button = tb.Button(bottom_frame, text="Add", bootstyle="primary", command=lambda: print("Add Clicked"))
add_button.pack(side="right")

app.mainloop()
