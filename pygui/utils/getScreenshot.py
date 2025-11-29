from os import read
import pyautogui
from PIL import Image
from pygui.utils.focusAndroidPhoneWindow import focusAndroidPhoneWindow
from utils.readConfig import readConfig

config = readConfig()

def getScreenshot(coordinates: dict = config ) -> Image:

    focusAndroidPhoneWindow()

    x1, y1 = coordinates["topLeftCorner"]["coordinates"]
    x2, y2 = coordinates["bottomRightCorner"]["coordinates"]

    width = x2 - x1
    height = y2 - y1
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))

    return screenshot

# Debug
if __name__ == "__main__":

    screenshot_image = getScreenshot(config)

    screenshot_image.save("test_screenshot.png")
    print("Screenshot saved as test_screenshot.png")
