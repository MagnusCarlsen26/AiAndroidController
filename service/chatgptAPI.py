import os
from dotenv import load_dotenv
import openai

load_dotenv()
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

def chatgptApi(
    message: str,
    sys_prompt: str = "",
    model: str = "gpt-5-nano", 
    imageData: None = None, 
    chatHistory: list = []
):
    try:

        print(message, "chatgptAPI")

        openai.api_key = CHATGPT_API_KEY

        messages = []
        if sys_prompt:
            messages.append({"role": "system", "content": sys_prompt})
        
        for item in chatHistory:
            if hasattr(item, 'role') and item.role == 'user':
                messages.append({"role": "user", "content": item.parts[0].text})
            elif hasattr(item, 'role') and item.role == 'model':
                messages.append({"role": "assistant", "content": item.parts[0].text})

        messages.append({"role": "user", "content": message})

        if imageData:
            print("Warning: imageData is not supported by OpenAI's ChatCompletion API in this implementation and will be ignored.")


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
