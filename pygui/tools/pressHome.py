import pyautogui
from utils.readConfig import readConfig

def pressHome():

    config = readConfig()
    x, y = config["homeButton"]["coordinates"]
    
    pyautogui.click(x, y, duration=0)
