import pyautogui
import time
# from numpy import asarray
from PIL import Image, ImageGrab


def takeScreenshot():
    img = ImageGrab.grab().convert("L")  # greyscale image
    return img


def isCollidedWithRect(data):
    # Draw a black rectangle to detect cactus
    # Image[x, y](similar to pygame cartesian plane)
    # i for sideways movement and j for up and down movement
    # i for width and j for height

    # For cactus
    for i in range(650, 850):
        for j in range(1120, 1170):
            if data[i, j] > 50:  # if our imaginary rectangle collided with the cactus(white pixel)
                return "cactus"
    # For bird
    for i in range(550, 750):
        for j in range(800, 1080):
            if data[i, j] > 50:
                return "bird"
    return "None"


if __name__ == '__main__':
    time.sleep(1)
    pyautogui.press('up')
    while 1:
        sc = takeScreenshot()
        pixelData = sc.load()
        # break
        collided = isCollidedWithRect(pixelData)
        if collided == "cactus":
            pyautogui.press("up")
        elif collided == "bird":
            pyautogui.press("down")

    # # cactus avoid rect
    # for i in range(550, 750):
    #     for j in range(1120, 1170):
    #         pixelData[i, j] = 0
    # # bird avoid rect
    # for i in range(550, 750):
    #     for j in range(800, 1080):
    #         pixelData[i, j] = 100
    # sc.show()
