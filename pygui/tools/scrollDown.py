import pyautogui
from agent.utils.interpolateImgCoordinateToScreen import interpolateImgCoordinateToScreen

def scrollDown(target: dict):

    x, y = interpolateImgCoordinateToScreen(target, target["imageMeta"])
    
    pyautogui.moveTo(x, y)
    pyautogui.scroll(-100)
