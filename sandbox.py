from service.chatgptAPI import chatgptApi
from PIL import Image

def analyze_image():
    image_path = "proccessedImg.png"
    try:
        with Image.open(image_path) as img:
            message = "What do you see in this image?"
            response, _ = chatgptApi(message=message, imageData=img)
            print(response)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_image()
