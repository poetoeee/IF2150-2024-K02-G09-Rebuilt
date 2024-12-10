from boundaries.DisplayPopBiayaAdd import DisplayPopAdd
from controllers.PengelolaTugasProyek import PengelolaTugasProyek

def main():
    # Initialize the controller
    controller = PengelolaTugasProyek()
    
    # Initialize and run the UI
    app = DisplayPopAdd(controller)
    app.run()

main()
