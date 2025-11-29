from dotenv import load_dotenv

import os

from service.geminiApi import sendToGemini
from setupScripts.setup import setup
from pygui.utils.visualizeCoordinates import visualize_coordinates

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

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
