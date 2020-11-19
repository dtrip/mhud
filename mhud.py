import signal
from pynput.mouse import Controller, Button
import sys
import os
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
        try:
            while True:
                x, y = mouse.position
                if (x != px or y != py):
                    print("X:%s Y: %s" % (x,y))



                time.sleep(0.1)
                px = x
                py = y
        except KeyboardInterrupt:
            print("SIGINT Caught")
            sys.exit()
        except Exception as e:
            print("ERROR: %s" % e)
            sys.exit()

    def getLua(self):
        
        lua = None

        if (os.stat("hud.lua").st_size == 0):
            raise Exception("Lua code is empty!")

        with open("hud.lua") as fh:

        


if __name__ == "__main__":
    m = mhud()
    m.run()
