from boundaries.DisplayBiaya import DisplayBiaya
import customtkinter as ctk

def main():
    root = ctk.CTk()
    app = DisplayBiaya(root)
    root.mainloop()

main()