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
    keyboard.type('ls')

    # keyboard key press after input
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


# #the time configuration
# x = datetime.today()
# y = x.replace(day=x.day+1, hour=2, minute=9, second=0, microsecond=0)
# delta_t = y-x
# secs = delta_t.seconds+1


# # the trigger/count down
# t = Timer(secs, runScript)
# t.start()
runScript()