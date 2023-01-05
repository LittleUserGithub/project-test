import time 
from pyautogui import click, displayMousePosition, typewrite, hotkey
#open teams
click(800,170)
click(800,170)
time.sleep(3)
#open the app
click(50,350)
time.sleep(3)
click(200,650)
time.sleep(3)
click(750,250)
time.sleep(3)
typewrite('x')
hotkey('alt gr', 'q')
typewrite('mymoodbit.com')
#hotkey('enter')