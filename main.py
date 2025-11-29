import pyautogui

from utils.readConfig import readConfig
from pygui.utils.focusAndroidPhoneWindow import focusAndroidPhoneWindow
from service.geminiApi import geminiApi 
from setupScripts.setup import setup
from pygui.utils.visualizeCoordinates import visualize_coordinates
import agent.agent

focusAndroidPhoneWindow()


print("Press 1 for setup.")
print("Press 2 for agentic control")
print("Press 3 to visualize coordinates")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    setup()
elif choice == 2:
    pass
elif choice == 3:
    visualize_coordinates()
else:
   print("invalid choice")
