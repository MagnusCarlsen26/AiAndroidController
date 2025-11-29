import pyautogui
from agent.utils.interpolateImgCoordinateToScreen import interpolateImgCoordinateToScreen
from utils.readConfig import readConfig

def click(target: dict):

    x, y = interpolateImgCoordinateToScreen(target,target["imageMeta"])

    pyautogui.click(x, y,duration=0)