import pyautogui
from utils.readConfig import readConfig

def pressBack():

    config = readConfig()
    x, y = config["backButton"]["coordinates"]
    
    pyautogui.click(x, y, duration=0)
