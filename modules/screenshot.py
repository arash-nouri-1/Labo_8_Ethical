import os
from PIL import ImageGrab

def run():
    im = ImageGrab.grab()
    im.save('screenshot.jpg')
    with open("screenshot.jpg", "rb") as file:
        data = file.read()    
    os.remove("screenshot.jpg")
    return data