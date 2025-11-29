import pyautogui

def types(payload: dict):
    text_to_type = payload.get("text", "")
    pyautogui.write(text_to_type)
