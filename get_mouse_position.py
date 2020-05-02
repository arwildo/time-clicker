#!/usr/bin/python3
import time
from pynput.mouse import Controller

mouse = Controller()

while True:
    time.sleep(2)
    print(mouse.position)
