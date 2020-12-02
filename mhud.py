#!/usr/bin/env python
import signal
from pynput.mouse import Controller, Button
import sys
import os
import time
import configparser
import traceback
# import lupa
# from lupa import LuaRuntime

import hud

# mouse = Controller()


class mhud:

    #  args = None
    # lua = LuaRuntime(unpack_returned_tuples=True)
    mouse = Controller()
    config = configparser.ConfigParser()
    px, py = (0,0)

    def __init__(self):
        self.config.sections()
        self.config.read('.mhudrc')

    def run(self):

        self.px, self.py = (0,0)
        try:

            # hud = self.lua.execute(self.getLua())

            while True:
                x, y = self.mouse.position
                if (x != self.px or y != self.py):
                    # hud(x,y)
                    print("X:%s Y: %s" % (x,y))

                time.sleep(0.1)
                self.px = x
                self.py = y
        except KeyboardInterrupt:
            print("SIGINT Caught")
            sys.exit()
        except Exception as e:
            traceback.print_exc()
            print("ERROR: %s" % e)
            sys.exit()

    def getLua(self):
        luacode = None

        if (os.stat(self.config['DEFAULT']['luafile']).st_size == 0):
            raise Exception("Lua file is empty:" % (self.config['DEFAULT']['luafile']))

        with open(self.config['DEFAULT']['luafile']) as fh:
            luacode = fh.read().replace('\n', '')

        return luacode

        


if __name__ == "__main__":
    m = mhud()
    m.run()
