import setup_env  # ini tolong hapus ini ada cuma gara gara python gue fucked up
from controllers.PengelolaProyek import PengelolaProyek
from boundaries.DisplayProyek import DisplayProyek

def main():
    # Initialize the controller
    controller = PengelolaProyek()
    
    # Initialize and run the UI
    app = DisplayProyek(controller)
    app.run()

if __name__ == "__main__":
    main()
