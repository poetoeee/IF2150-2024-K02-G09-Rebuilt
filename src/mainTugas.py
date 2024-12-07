from boundaries.DisplayTugas import DisplayTugas
from controllers.PengelolaTugasProyek import PengelolaTugasProyek

def main():
    # Initialize the controller
    controller = PengelolaTugasProyek()
    
    # Initialize and run the UI
    app = DisplayTugas(controller)
    app.run()

main()
