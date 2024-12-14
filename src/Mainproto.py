from boundaries.DisplayBiaya import DisplayBiaya
import customtkinter as ctk

def main():
    # Initialize the controller
    root = ctk.CTk()
    app = DisplayBiaya(root)
    # Initialize and run the UI
    root.mainloop()

main()