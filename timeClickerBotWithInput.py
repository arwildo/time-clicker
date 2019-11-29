#!/bin/python3
from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as ck

mouse = Controller()
keyboard = ck()

# function that will be execute
def runScript():
    mouse.position = (422, 323) 
    mouse.press(Button.left)
    mouse.release(Button.left)

    # keyboard input here
    keyboard.type('apt get update && pip install keras')

    # keyboard key press enter the after input
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


# the time configuration, in this case the next day by 2:01 AM
x = datetime.today()
y = x.replace(day=x.day+1, hour=2, minute=15, second=0, microsecond=0)
delta_t = y-x
secs = delta_t.seconds+1


# the trigger/count down
t = Timer(secs, runScript)
t.start()
