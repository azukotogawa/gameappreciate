from world import World
from world_drawer import *
from config import *

class WorldLoad():
    def __init__(self, target_pos):
        self.target_pos = target_pos
        # The order of weight values for each terrain type:
        # WEIGHTS = [WEIGHT_OCEAN3, WEIGHT_OCEAN2, WEIGHT_OCEAN1, WEIGHT_BEACH, WEIGHT_GRASS, WEIGHT_MOUNTAIN, WEIGHT_SNOW]
        WEIGHTS1 = [70, 20, 20, 12, 35, 30, 0]  # Islands
        WEIGHTS2 = [35, 20, 20, 15, 30, 30, 25]  #
        WEIGHTS3 = [20, 15, 15, 15, 50, 35, 45]  # Lakes

        self.test_generate_world(WEIGHTS1, random_seed=21)

    def draw(self, target_pos):
        self.target_pos = target_pos
        self.world_drawer.draw(self.target_pos, self.tile_map, wait_for_key=False)

    def test_generate_world(self, weights, random_seed):
        self.world_drawer = WorldDrawer()
        self.world = World(WORLD_X, WORLD_Y, random_seed)
        self.tile_map = self.world.get_tiled_map(weights)
        #self.world_drawer.draw(self.target_pos, self.tile_map, wait_for_key = True)
