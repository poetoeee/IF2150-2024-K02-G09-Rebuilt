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
app.title("Biaya GUI with Fixed Header")
app.geometry("900x500")

# Frame Utama
main_frame = ttk.Frame(app, padding=10, relief="ridge")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Header Label
header_label = ttk.Label(main_frame, text="Biaya", font=("Arial", 16, "bold"))
header_label.pack(anchor="w", pady=(0, 10))

# Header Frame (Baris Header)
header_frame = ttk.Frame(main_frame)
header_frame.pack(fill="x")

headers = ["Barang", "Harga", "Qty", "Total", "Keterangan", "Aksi"]
for col_index, header in enumerate(headers):
    label = ttk.Label(
        header_frame,
        text=header,
        font=("Arial", 14, "bold"),
        background="#f0f0f0",
        anchor="center",
        padding=5
    )
    label.grid(row=0, column=col_index, sticky="nsew", padx=1, pady=1)

# Atur column weight dengan minsize untuk header frame
for col_index in range(len(headers)):
    header_frame.columnconfigure(col_index, weight=1, minsize=100)

# Scrollable Canvas Area for Data Rows
canvas_frame = ttk.Frame(main_frame)
canvas_frame.pack(fill="both", expand=True)

canvas = Canvas(canvas_frame, bg="white")
scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

# Configure Canvas dan Scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Load Icons
edit_icon = PhotoImage(file="img/editbutton.png").subsample(3, 3)
delete_icon = PhotoImage(file="img/deletebutton.png").subsample(3, 3)

# Isi Data ke dalam Scrollable Grid
for row_index, row_data in enumerate(data, start=1):
    for col_index, cell_data in enumerate(row_data[:-1]):
        label = ttk.Label(
            scrollable_frame,
            text=f"  {cell_data}  ",
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

# Atur column weight dan minsize untuk scrollable frame (data rows)
for col_index in range(len(headers)):
    scrollable_frame.columnconfigure(col_index, weight=1, minsize=100)

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

add_icon = PhotoImage(file="img/addbutton.png").subsample(3, 3)
add_button = tb.Button(bottom_frame, image=add_icon, bootstyle="primary", command=lambda: print("Add Clicked"))
add_button.pack(side="right", padx=10, pady=10)

app.mainloop()
