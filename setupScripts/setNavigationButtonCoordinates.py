from pygui.setup.getNavigationButtonsCoordinates import getNavigationButtonCoordinates
from utils.updateConfig import updateConfig

def setNavigationButtonCoordinates():

    newScreenCoordinates = getNavigationButtonCoordinates()

    updateConfig(newScreenCoordinates)

