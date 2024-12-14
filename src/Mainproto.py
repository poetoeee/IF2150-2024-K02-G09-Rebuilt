from boundaries.proto1 import ProjectUI
import customtkinter as ctk



def main():
    # Initialize the controller
    root = ctk.CTk()
    app = ProjectUI(root)
    # Initialize and run the UI
    root.mainloop()

main()