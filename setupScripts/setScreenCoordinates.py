from pygui.setup.getScreenCoordinates import getScreenCoordinates
from utils.updateConfig import updateConfig

def setScreenCoordinates():

    newScreenCoordinates = getScreenCoordinates()

    updateConfig(newScreenCoordinates)
