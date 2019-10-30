#!/bin/python3
from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as ck

mouse = Controller()
keyboard = ck()

# function that will be execute
def runScript():
    mouse.position = (278, 176) 
    mouse.press(Button.left)
    mouse.release(Button.left)


#the time configuration
x = datetime.today()
y = x.replace(day=x.day+1, hour=2, minute=1, second=0, microsecond=0)
delta_t = y-x
secs = delta_t.seconds+1


# the trigger/count down
t = Timer(secs, runScript)
t.start()
