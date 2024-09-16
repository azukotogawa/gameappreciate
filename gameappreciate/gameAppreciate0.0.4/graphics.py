import sys
import sdl2
import sdl2.ext


# Create a resource, so we have easy access to the example images.

#
#
#
# located in the same directory in a folder names "resources"
RESOURCES = sdl2.ext.Resources(__file__, "resources")

class graphics:
    def __init__(self, window):

        self.window = window

        # Create a sprite factory that allows us to create visible 2D elements
        # easily. Depending on what the user chosses, we either create a factory
        # that supports hardware-accelerated sprites or software-based ones.
        # The hardware-accelerated SpriteFactory requres a rendering context
        # (or SDL_Renderer), which will create the underlying textures for us.
        if "-hardware" in sys.argv:
            print("Using hardware acceleration")
            renderer = sdl2.ext.Renderer(self.window, flags=sdl2.render.SDL_RENDERER_ACCELERATED)
            actory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
        else:
            print("Using software rendering")
            renderer = sdl2.ext.Renderer(self.window, flags=sdl2.render.SDL_RENDERER_SOFTWARE)
            factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        # Create a UI factory, which will handle several defaults for
        # us. Also, the UIFactory can utilises software-based UI elements as
        # well as hardware-accelerated ones; this allows us to keep the UI
        # creation code clean.
        self.uifactory = sdl2.ext.UIFactory(factory)

        # Since all gui elements are sprites, we can use the
        # SpriteRenderSystem class, we learned about in helloworld.py, to
        # draw them on the Window.
        spriterenderer = factory.create_sprite_render_system(window)

    def renderSprite(self):
        # Render all user interface elements on the window.
        self.spriterenderer.render(button)

    def graphicsButton(self, source = None, x = None, y = None):
        self.x = x
        self.y = y

        button = self.uifactory.from_image(sdl2.ext.BUTTON, RESOURCES.get_path(source))
        button.position = self.x, self.y

    def graphicsEntity(self, source = None, x = None, y = None):
        entity = self.uifactory.from_image(sdl2.ext.Entity, RESOURCES.get_path(source))
        entity.position = self.x, self.y
