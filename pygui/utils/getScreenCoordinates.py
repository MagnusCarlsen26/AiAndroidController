import pyautogui
import time
from pynput import mouse

logging = True

def on_click(x, y, button, pressed):
    global logging
    if pressed:
        logging = False
        return False  # Stop listener

def log_mouse_coordinates():
    print("Logging mouse coordinates. Click to stop.")
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    while logging:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}")
        time.sleep(0.1)

    listener.join()
    print("Logging stopped.")

if __name__ == "__main__":
    log_mouse_coordinates()
