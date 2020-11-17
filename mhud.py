import signal
from pynput.mouse import Controller, Button
import sys
import time
import lupa
from lupa import LuaRuntime

mouse = Controller()
px, py = (0,0)


class mhud:

    args = None
    lua = LuaRuntime(unpack_returned_tuples=False)
    mouse = Controller()



    def __init__(self):
        pass

    def run(self):

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


if __name__ == "__main__":
    m = mhud()
    m.run()
