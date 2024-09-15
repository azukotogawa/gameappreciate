import sys
import sdl2
import sdl2.ext

from graphics import *

class GameEngine:
    def __init__(self, title = None, width = 800, height = 600):
        self.title = title.encode() if title is not None else None
        self.width = width
        self.height = height

        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

        self.window = sdl2.SDL_CreateWindow(self.title, sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, self.width, self.height, sdl2.SDL_WINDOW_SHOWN)

        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, sdl2.SDL_RENDERER_ACCELERATED)

        self.graphics = graphics(self.window)

        self.running = True

        self.dt = 1.0 / 60

        self.update_dt = 0
        self.update_handlers = []
        self.draw_handlers = []

    def _update(self, dt):
        self.update_dt += dt
        while self.update_dt > self.dt:
            for update in self.update_handlers:
                update(self.dt)
            self.update_dt -= self.dt

    def _draw(self):
        for draw in self.draw_handlers:
            draw()

    def loop(self):
        sdl2.SDL_ShowWindow(self.window)

        event = sdl2.SDL_Event()

        current = sdl2.SDL_GetPerformanceCounter()
        freq = sdl2.SDL_GetPerformanceFrequency()

        while self.running:
            if sdl2.SDL_PollEvent(event) != 0:
                if event.type == sdl2.SDL_QUIT:
                    self.running = False

            new = sdl2.SDL_GetPerformanceFrequency()
            self._update(new - current / freq)
            current = new

            sdl2.SDL_RenderClear(self.renderer)
            self._draw()

            self.renderer.clear(0)


        sdl2.SDL_DestroyRenderer(self.renderer)
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()

def update(self, fn):
    self.update_handlers.append(fn)
    return fn

def draw(self, fn):
    self.draw_handlers.append(fn)
    return fn