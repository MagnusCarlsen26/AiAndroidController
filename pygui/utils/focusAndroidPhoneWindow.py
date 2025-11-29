import pyautogui
from utils.readConfig import readConfig

def focusAndroidPhoneWindow():

    try:

        config = readConfig()
        android_window_title = config.get("androidPhoneWindow")

        if android_window_title:
            pyautogui.getWindowsWithTitle(android_window_title)[0].activate()
            print(f"Focused on '{android_window_title}'.")
        else:
            print("Android phone window title not set in config. Please run setup (option 1) and then option 3.")
    
    except Exception as e:
        print(f"Error focusing on Android phone window: {e}")
