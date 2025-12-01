import os
from dotenv import load_dotenv
import openai
import base64
from io import BytesIO

load_dotenv()
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

def chatgptApi(
    message: str,
    sys_prompt: str = "",
    model: str = "gpt-4o", 
    imageData: None = None, 
    chatHistory: list = []
):
    try:

        openai.api_key = CHATGPT_API_KEY

        messages = []
        if sys_prompt:
            messages.append({"role": "system", "content": sys_prompt})
        
        for item in chatHistory:
            if hasattr(item, 'role') and item.role == 'user':
                messages.append({"role": "user", "content": item.parts[0].text})
            elif hasattr(item, 'role') and item.role == 'model':
                messages.append({"role": "assistant", "content": item.parts[0].text})

        if imageData:
            messages.append({"role": "user", "content": _prepare_image_message(message, imageData)})
        else:
            messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        
        new_history_entry_user = type('obj', (object,), {'role' : 'user', 'parts' : [type('obj', (object,), {'text': message})]})
        new_history_entry_model = type('obj', (object,), {'role' : 'model', 'parts' : [type('obj', (object,), {'text': response.choices[0].message['content']})]})

        chatHistory.append(new_history_entry_user)
        chatHistory.append(new_history_entry_model)

        return response.choices[0].message['content'], chatHistory
    except Exception as e:
        print(f"Error in chatgptApi: {e}")
        return None, []

def _prepare_image_message(message: str, imageData):
    buffered = BytesIO()
    imageData.save(buffered, format="PNG")
    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return [
        {"type": "text", "text": message},
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
                "detail": "high"
            },
        },
    ]
