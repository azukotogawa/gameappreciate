from main import *
from entity import *

#starts the gameEngine and creates a window
gameEngineMain = GameEngine(title = "gameAppreciate", width = 800, height = 600)

#creates an entity
#entity1 = Entity(hitboxX = 50, hitboxY = 50, x = 375, y = 275)

@gameEngineMain.update
def update(dt):
    print("s")

gameEngineMain.loop()