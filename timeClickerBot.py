from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller

mouse = Controller()

# function that will be execute
def download():
    mouse.position = (1024, 288)
    mouse.press(Button.left)
    mouse.release(Button.left)

#the time configuration
x = datetime.today()
y = x.replace(day=x.day, hour=x.hour, minute=x.minute+1, second=0, microsecond=0)
delta_t = y-x
secs = delta_t.seconds+1


# the trigger/count down
t = Timer(secs, download)
t.start()