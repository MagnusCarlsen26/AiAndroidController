from .setScreenCoordinates import setScreenCoordinates
from .setNavigationButtonCoordinates import setNavigationButtonCoordinates

def setup():
    
    print("Press 1 to setup Screen Coordinates")
    print("Press 2 to setup navigation button coordinates")

    setupChoice = int(input("\nEnter your choice: "))

    if setupChoice == 1: setScreenCoordinates()
    elif setupChoice == 2: setNavigationButtonCoordinates()
    else: print("Invalid Choice please try againn")
