import google.generativeai
from PIL import Image

def sendToGemini(
    apiKey: str,
    message: str,
    sys_prompt: str,
    model: str = "gemini-2.0-flash",
    image_data: Image = None,
):
    google.generativeai.configure(api_key=apiKey, transport="rest")

    model_instance = google.generativeai.GenerativeModel(
        model, system_instruction=sys_prompt
    )
    chat_args = {}
    convo = model_instance.start_chat(**chat_args)

    content = [message]
    if image_data:
        content.append(image_data)

    convo.send_message(content)
    return convo.last.text, convo.history
