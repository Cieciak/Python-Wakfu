import pyautogui
from pynput import keyboard

OUT = False

width, heigth = pyautogui.size()
pyautogui.PAUSE = 0

def on_press(key):
    if OUT == True:
        print(key)

    if key == keyboard.Key.down:
        pyautogui.moveTo(width/2 - 150, heigth/2 + 75)
        pyautogui.leftClick()

    if key == keyboard.Key.up:
        pyautogui.moveTo(width/2 + 150, heigth/2 - 75)
        pyautogui.leftClick()

    if key == keyboard.Key.left:
        pyautogui.moveTo(width/2 - 150, heigth/2 - 75)
        pyautogui.leftClick()

    if key == keyboard.Key.right:
        pyautogui.moveTo(width/2 + 150, heigth/2 + 75)
        pyautogui.leftClick()



with keyboard.Listener(on_press = on_press) as listen:
    listen.join()