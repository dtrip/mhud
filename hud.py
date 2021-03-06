#!/usr/bin/env python
import cairo
from gi.repository import Gtk, Gdk

class HUD(Gtk.Window):

    x, y = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.x, self.y)
    cr = cairo.Context(self.surface)

    def init(self):
        super(HUD, self).__init__()
    
        self.draw()

    def draw(self):

        self.darea = GtkDrawingArea()
        self.darea.connect('draw', self.on_draw)
        # elf.darea.set_evets
        self.add(self.darea)
        # self.cr.
        self.set_title("HUD")
        self.resize(300,)
