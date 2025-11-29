import pyautogui
from agent.utils.interpolateImgCoordinateToScreen import interpolateImgCoordinateToScreen

def scrollUp(target: dict):

    x, y = interpolateImgCoordinateToScreen(target, target["imageMeta"])
    
    pyautogui.moveTo(x, y)
    pyautogui.scroll(100)
