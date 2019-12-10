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
    mouse.position = (422, 323)
    mouse.press(Button.left)
    mouse.release(Button.left)

    # continue with typer
    typer(KEYBOARD_INPUT)


def typer(KEYBOARD_INPUT):
    keyboard.type(KEYBOARD_INPUT)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    exit()


if __name__ == "__main__":
    KEYBOARD_INPUT = "apt get update && pip install keras"

    x = datetime.today()
    # the time configuration, in this case the next day by 2:01 AM
    y = x.replace(day=x.day+0, hour=14, minute=44, second=1, microsecond=0)
    delta_t = y-x
    secs = delta_t.seconds+1

    print(x)
    print(y)
    print(delta_t)
    print(secs)
    
    
    # the trigger/count down
    t = Timer(secs, clicker)
    t.start()

