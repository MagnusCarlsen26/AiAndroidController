import pyautogui

def currMouseCoordinates() -> tuple[int, int]:

    x, y = pyautogui.position()
    
    return x, y
