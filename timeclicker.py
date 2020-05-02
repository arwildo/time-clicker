#!/bin/python3
from datetime import datetime
from threading import Timer
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as ck


mouse = Controller()
keyboard = ck()

# functions that will be execute
# mouse position can get using mousepos tool

def clicker():
    mouse.position = (420, 224)
    mouse.press(Button.left)
    mouse.release(Button.left)
    
    # continue with typer
    typer(KEYBOARD_INPUT)


def typer(KEYBOARD_INPUT):
    keyboard.type(KEYBOARD_INPUT)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


if __name__ == "__main__":
    KEYBOARD_INPUT = "apt get update && pip install keras"
    
    t0 = datetime.today()
    # the time configuration, in this case the next day by 2:01 AM
    t1 = t0.replace(day=t0.day+0, hour=15, minute=12, second=0, microsecond=0)
    delta_t = t1 - t0
    # secs will be the seconds reminder till 2:01 AM
    secs = delta_t.seconds
    
    # the trigger/count down
    t = Timer(secs, clicker)
    t.start()
