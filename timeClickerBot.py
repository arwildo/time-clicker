#!/usr/bin/python3
from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller

mouse = Controller()

# get mouse position
def getMp():
    print('===========')
    print('timeClicker')
    print('===========')
    print('1. Set your mouse position, drag your mouse and hit enter when you done.')
    input('Enter...')
    mp = format(mouse.position)
    print('position = '+ mp)
    print('Mouse will be clicking that coordinate at the given setting time...')
    return mp

# function that will be execute
def download():
    mp = mouse.position 
    mouse.press(Button.left)
    mouse.release(Button.left)


#the time configuration
x = datetime.today()#NOTE: still need to configure time
y = x.replace(day=x.day+0, hour=0, minute=1, second=0, microsecond=0)
delta_t = y-x
secs = delta_t.seconds+1


# the trigger/count down
getMp()
t = Timer(secs, download)
t.start()
