import pyautogui
from utils.readConfig import readConfig

# TODO: This is buggy
def pressRecentApps():

    config = readConfig()
    x, y = config["recentAppsButton"]["coordinates"]
    
    pyautogui.click(x, y, duration=0)
