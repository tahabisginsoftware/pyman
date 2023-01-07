# tahabisginsoftware.com

# import stuff
import pyautogui
import time

# variables
msg = input("msg: ")
n = input("msg count (full numbers): ")

# loop for spam
for x in range(0, int(n)):
    time.sleep(0.5) # -> only typewrite after 0.5 seconds
    pyautogui.typewrite(msg + '\n')
