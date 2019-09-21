#!/usr/bin/python3
from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller

mouse = Controller()

# get mouse position
mp = 0
def getMp():
    print('===========')
    print('timeClicker')
    print('===========')
    print('1. Set your mouse position, drag your mouse and hit enter when you done.')
    input('Enter...')
    mp = format(mouse.position)
    print('position = '+ mp)
    print('Mouse will be clicking that coordinate at the given setting time...')
    global mp #TODO: need to find way passing variabel

# function that will be execute
def download():
    mouse.position = mp
    mouse.press(Button.left)
    mouse.release(Button.left)


##the time configuration
#x = datetime.today()
#y = x.replace(day=x.day+1, hour=2, minute=1, second=0, microsecond=0)
#delta_t = y-x
#secs = delta_t.seconds+1
secs = 3


# the trigger/count down
getMp()
t = Timer(secs, download)
t.start()
