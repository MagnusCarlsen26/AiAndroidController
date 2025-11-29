import pyautogui

def getScreenshot(coordinates: dict):
    x1, y1 = coordinates["topLeftCorner"]["coordinates"]
    x2, y2 = coordinates["bottomRightCorner"]["coordinates"]

    width = x2 - x1
    height = y2 - y1
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))

    return screenshot

# Debug
if __name__ == "__main__":
    config_data = {
        "topLeftCorner": {
            "coordinates": [
                1460,
                42
            ]
        },
        "bottomRightCorner": {
            "coordinates": [
                1911,
                1019
            ]
        }
    }

    screenshot_coordinates = {
        "topLeftCorner": config_data["topLeftCorner"],
        "bottomRightCorner": config_data["bottomRightCorner"]
    }

    screenshot_image = getScreenshotOfBox(screenshot_coordinates)

    screenshot_image.save("test_screenshot.png")
    print("Screenshot saved as test_screenshot.png")
