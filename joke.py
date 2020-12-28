import keyboard, pyautogui, time

OUT = False
i = 0
step = 1
max = 30
width, heigth = pyautogui.size()
pyautogui.PAUSE = 0
braek = 0.25

pyautogui.moveTo(284, 2085)
pyautogui.leftClick()
keyboard.write("/sit")
keyboard.press_and_release("enter")
pyautogui.moveTo(width/2, heigth/2)
pyautogui.leftClick()
time.sleep(1)

while i < max:
    time.sleep(braek)
    keyboard.press_and_release("up")

    time.sleep(braek)
    keyboard.press_and_release("right")   

    time.sleep(braek)
    keyboard.press_and_release("down")   

    time.sleep(braek)
    keyboard.press_and_release("left")   


    i += step
    print(i)
