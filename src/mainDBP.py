from boundaries.DPBEdit import DisplayPopEdit
from controllers.PengelolaBiaya import PengelolaBiaya

def main():
    # Initialize the controller
    controller = PengelolaBiaya()
    
    # Initialize and run the UI
    app = DisplayPopEdit(controller)
    app.run()
    

main()
