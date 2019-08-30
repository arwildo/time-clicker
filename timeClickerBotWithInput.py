#!/usr/bin/python3
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
    keyboard.type('apt install poppler-utils binwalk binutils python-pip python3-pip tshark gdb man python-dev libssl-dev libffi-dev build-essential default-jre wpscan sqlmap grabber hashcat wapiti skipfish python-pyinotify python-yaml arachni radare2 aircrack-ng nmap wfuzz john hydra -y')

    # keyboard key press after input
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


#the time configuration
x = datetime.today()
y = x.replace(day=x.day+1, hour=2, minute=9, second=0, microsecond=0)
delta_t = y-x
secs = delta_t.seconds+1


# the trigger/count down
t = Timer(secs, runScript)
t.start()