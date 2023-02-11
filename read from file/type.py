import pyautogui
import time
 
time.sleep(4)
 
for line in open("text.txt", "r"):
    pyautogui.typewrite(line)
    pyautogui.press("enter")