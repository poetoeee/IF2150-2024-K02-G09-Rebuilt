from boundaries.DisplayPopBiaya import DisplayPop
from controllers.PengelolaTugasProyek import PengelolaTugasProyek

def main():
    # Initialize the controller
    controller = PengelolaTugasProyek()
    
    # Initialize and run the UI
    app = DisplayPop(controller)
    app.run()

main()
