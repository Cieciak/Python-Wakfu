import keyboard, pyautogui, time, commands

width, heigth = pyautogui.size()
i = 0
step = 1
max = 300
pyautogui.PAUSE = 0 # Safety
wait = 1/100 # Seconds


commands.write_in_chat("/sit")
time.sleep(1)
pyautogui.leftClick(width/2, heigth/2)


while i < max:
    time.sleep(wait)
    keyboard.press_and_release("up")

    time.sleep(wait)
    keyboard.press_and_release("right")   

    time.sleep(wait)
    keyboard.press_and_release("down")   

    time.sleep(wait)
    keyboard.press_and_release("left")   

    i += step
    print(i)
