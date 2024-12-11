from boundaries.DisplayPopBiaya import DisplayPop
from controllers.PengelolaBiaya import PengelolaBiaya

def main():
    # Initialize the controller
    controller = PengelolaBiaya()
    
    # Initialize and run the UI
    app = DisplayPop(controller)
    app.run()

main()
