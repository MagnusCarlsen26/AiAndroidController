import os
from PIL import Image

from pygui.utils.getScreenshot import getScreenshot
from agent.utils.addCoordinateGrid import addCoordinateGrid
from pygui.utils.focusAndroidPhoneWindow import focusAndroidPhoneWindow

def verify_coordinate(x: int, y: int):
    # Focus on the Android phone window
    focusAndroidPhoneWindow()
    
    # Get a screenshot
    screenshot = getScreenshot()
    
    # Add marker to the screenshot
    marked_screenshot_data = addCoordinateGrid(screenshot, marks=[(x, y)], save=True)
    marked_screenshot_path = "proccessedImg.png"  # Assuming addCoordinateGrid saves to this file
    
    return {
        "marked_screenshot_path": os.path.abspath(marked_screenshot_path),
        "x": x,
        "y": y
    }
