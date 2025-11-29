import pyautogui
import json
import time

from utils.readConfig import readConfig
# Assuming userConfig.json is in the project root or can be accessed via a utility
CONFIG_FILE_PATH = "userConfig.json"

def visualize_coordinates():

    print("Visualizing coordinates...")
    
    time.sleep(3)
    config = readConfig()

    for key, value in config.items():
        if "coordinates" in value:
            x, y = value["coordinates"]
            print(f"Drawing at {key}: ({x}, {y})")
            
            pyautogui.moveTo(x, y, duration=0.05)
            time.sleep(0.5)
            
    print("Visualization complete.")

