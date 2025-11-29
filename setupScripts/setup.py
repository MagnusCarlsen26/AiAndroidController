from .setScreenCoordinates import setScreenCoordinates
from .setNavigationButtonCoordinates import setNavigationButtonCoordinates
from .setAndroidPhoneWindow import setAndroidPhoneWindow

def setup():
    
    print("Press 1 to setup Screen Coordinates")
    print("Press 2 to setup navigation button coordinates")
    print("Press 3 to setup Android phone window")

    setupChoice = int(input("\nEnter your choice: "))

    if setupChoice == 1: setScreenCoordinates()
    elif setupChoice == 2: setNavigationButtonCoordinates()
    elif setupChoice == 3: setAndroidPhoneWindow()
    else: print("Invalid Choice please try againn")
