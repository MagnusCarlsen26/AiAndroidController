import pyautogui
from agent.utils.interpolateImgCoordinateToScreen import interpolateImgCoordinateToScreen

def click(target: dict):

    x, y = interpolateImgCoordinateToScreen(target,target["imageMeta"])

    pyautogui.click(x, y,duration=0)