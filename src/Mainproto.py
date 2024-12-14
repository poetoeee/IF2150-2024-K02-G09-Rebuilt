from boundaries.proto1 import ProjectUI
import customtkinter as ctk

def main():
    root = ctk.CTk()
    app = ProjectUI(root)
    root.mainloop()

main()