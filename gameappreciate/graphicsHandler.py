import sdl2.ext

class graphicsHandler(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(graphicsHandler, self).__init__(window)

    def render(self, components):
        super(graphicsHandler, self).render(components)

    def refresh(self):

    def load(self):

    def clear(self):


