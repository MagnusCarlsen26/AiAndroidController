import google.generativeai
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def geminiApi(
    message: str,
    sys_prompt: str = "",
    model: str = "gemini-2.0-flash",
    imageData: Image = None,
    chatHistory: list = []
):
    google.generativeai.configure(
        api_key=GEMINI_API_KEY,
        transport="rest"
    )

    model_instance = google.generativeai.GenerativeModel(
        model, system_instruction=sys_prompt
    )

    if chatHistory:
        convo = model_instance.start_chat(history=chatHistory)
    else:
        convo = model_instance.start_chat()
    
    content = [message]
    if imageData:
        content.append(imageData)

    convo.send_message(content)
    return convo.last.text, convo.history
