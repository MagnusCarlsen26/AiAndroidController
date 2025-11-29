from .setScreenCoordinates import setScreenCoordinates
from .setNavigationButtonCoordinates import setNavigationButtonCoordinates
from .setAndroidPhoneWindow import setAndroidPhoneWindow
from .setScreenResolution import setScreenResolution
from utils.updateConfig import updateConfig

def setup():
    
    print("Press 1 to setup Screen Coordinates")
    print("Press 2 to setup navigation button coordinates")
    print("Press 3 to setup Android phone window")
    print("Press 4 to setup Screen Resolution")

    setupChoice = int(input("\nEnter your choice: "))

    if setupChoice == 1: setScreenCoordinates()
    elif setupChoice == 2: setNavigationButtonCoordinates()
    elif setupChoice == 3: setAndroidPhoneWindow()
    elif setupChoice == 4: setScreenResolution()
    else: print("Invalid Choice please try againn")
