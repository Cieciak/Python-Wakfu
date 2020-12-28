import keyboard, pyautogui
width, heigth = pyautogui.size()

default_chat_constant = 284/3840 + 2085j/2160
default_tile_size_constant = 150/3840 + 75j/2160

def write_in_chat(text, pos_x = default_chat_constant.real*width, pos_y = default_chat_constant.imag*heigth , end = "enter"):
    pyautogui.leftClick(pos_x, pos_y)
    keyboard.write(text)
    keyboard.press_and_release(end)

