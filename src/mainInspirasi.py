import setup_env  # ini tolong hapus ini ada cuma gara gara python gue fucked up

from boundaries.DisplayInspirasi import DisplayInspirasi
from controllers.PengelolaInspirasi import PengelolaInspirasi

def main():
    # Initialize the controller
    controller = PengelolaInspirasi()
    
    # Initialize and run the UI
    app = DisplayInspirasi(controller)
    app.run()

main()