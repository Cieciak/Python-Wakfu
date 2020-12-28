import pyautogui, commands
from pynput import keyboard

default_tile_size_constant = commands.default_tile_size_constant

OUT = False

width, heigth = pyautogui.size()
pyautogui.PAUSE = 0

def on_press(key):
    if OUT == True:
        print(key)

    if key == keyboard.Key.down:
        pyautogui.moveTo(width/2 - default_tile_size_constant.real*width, heigth/2 + default_tile_size_constant.imag*heigth)
        pyautogui.leftClick()

    if key == keyboard.Key.up:
        pyautogui.moveTo(width/2 + default_tile_size_constant.real*width, heigth/2 - default_tile_size_constant.imag*heigth)
        pyautogui.leftClick()

    if key == keyboard.Key.left:
        pyautogui.moveTo(width/2 - default_tile_size_constant.real*width, heigth/2 - default_tile_size_constant.imag*heigth)
        pyautogui.leftClick()

    if key == keyboard.Key.right:
        pyautogui.moveTo(width/2 + default_tile_size_constant.real*width, heigth/2 + default_tile_size_constant.imag*heigth)
        pyautogui.leftClick()

with keyboard.Listener(on_press = on_press) as listen:
    listen.join()