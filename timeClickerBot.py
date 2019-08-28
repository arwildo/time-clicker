#!/usr/bin/python3
from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller

mouse = Controller()

# function that will be execute
def download():
    mouse.position = (759, 211)
    mouse.press(Button.left)
    mouse.release(Button.left)


##the time configuration
#x = datetime.today()
#y = x.replace(day=x.day+1, hour=2, minute=9, second=0, microsecond=0)
#delta_t = y-x
#secs = delta_t.seconds+1
#
#
## the trigger/count down
#t = Timer(secs, download)
#t.start()
download()
