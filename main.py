from dotenv import load_dotenv
from service.geminiApi import sendToGemini
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
