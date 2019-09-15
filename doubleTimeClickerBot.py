#!/usr/bin/python3
from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller

mouse = Controller()

## get mouse position
#def getMp():
#	print('===========')
#	print('timeClicker')
#	print('===========')
#	print('1. Set your mouse position, drag your mouse and hit enter when you done.')
#	input('Enter...')
#	mp = format(mouse.position)
#	print('position = '+ mp)
#	return mp
#
# function that will be execute
def download():
	mouse.position = (107, 523)
	mouse.press(Button.left)
	mouse.release(Button.left)


#the time configuration
x = datetime.today()
y = x.replace(day=x.day+1, hour=2, minute=1, second=0, microsecond=0)
delta_t = y-x
secs = delta_t.seconds+1


# the trigger/count down
t = Timer(secs, download)
t.start()
download()
