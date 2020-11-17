import signal
from pynput.mouse import Controller, Button
import sys
import time


mouse = Controller()
px, py = (0,0)

while True:
    try:
        x, y = mouse.position
        if (x != px or y != py):
            print("X:%s Y: %s" % (x,y))

        time.sleep(0.1)
        px = x
        py = y
    except KeyboardInterrupt:
        print("SIGINT Caught")
        sys.exit()

