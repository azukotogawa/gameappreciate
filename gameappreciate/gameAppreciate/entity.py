import sdl2
from graphics import *

class Entity(object):
    def __init__(self, window, graphics, hitboxX = None, hitboxY = None, x = None, y = None):
        self.window = window
        self.graphics = graphics
        self.hitboxX = hitboxX
        self.hitboxY = hitboxY
        self.x = x
        self.y = y

        entity = graphics.graphicsEntity(self, "button.bmp", 50, 50)
