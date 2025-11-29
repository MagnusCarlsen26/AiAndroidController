from ..utils.getTargetCoordinates import getTargetCoordinates
import time

def getScreenCoordinates():

    screenCoordinates = {
        "topLeftCorner" : {
            "coordinates" : None
        },
        "topRightCorner" : {
            "coordinates" : None
        },
        "bottomLeftCorner" : {
            "coordinates" : None
        },
        "bottomRightCorner" : {
            "coordinates" : None
        },
    }

    for target in screenCoordinates:
        screenCoordinates[target]["coordinates"] = getTargetCoordinates(target)
        time.sleep(0.5)
    
    return screenCoordinates
