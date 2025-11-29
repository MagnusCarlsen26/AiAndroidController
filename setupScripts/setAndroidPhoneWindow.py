import pyautogui
from utils.updateConfig import updateConfig

def setAndroidPhoneWindow():
    print("Listing all open window titles:")
    windows = []
    for window in pyautogui.getAllWindows():
        if window.title:
            windows.append(window)

    if not windows:
        print("No windows with titles found.")
        return

    for i, window in enumerate(windows):
        print(f"{i + 1}. {window.title}")

    choice = int(input("Enter the number corresponding to your Android phone window: "))
    selected_window_title = windows[choice - 1].title

    updateConfig({"androidPhoneWindow": selected_window_title})
    
    print(f"'{selected_window_title}' set as Android phone window.")
