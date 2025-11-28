import google.generativeai

def sendToGemini(
    apiKey: str,
    message: str,
    sys_prompt: str,
    model: str = "gemini-2.0-flash",
):
    google.generativeai.configure(api_key=apiKey, transport="rest")

    model_instance = google.generativeai.GenerativeModel(
        model, system_instruction=sys_prompt
    )
    chat_args = {}
    convo = model_instance.start_chat(**chat_args)

    convo.send_message(message)
    return convo.last.text, convo.history
