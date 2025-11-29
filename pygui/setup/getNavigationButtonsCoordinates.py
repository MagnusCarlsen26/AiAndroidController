from ..utils.getTargetCoordinates import getTargetCoordinates
import time

def getNavigationButtonCoordinates():

    navigationButtonCoordinates = {
        "backButton": {
            "coordinates": None
        },
        "homeButton": {
            "coordinates": None
        },
        "recentAppsButton": {
            "coordinates": None
        },
    }
    
    for target in navigationButtonCoordinates:

        navigationButtonCoordinates[target]["coordinates"] = getTargetCoordinates(target)
        time.sleep(0.5)
    return navigationButtonCoordinates
