import random

class Grid:
    def __init__(self, grid_size, tile_size):
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.grid = []
        self.route_start = None
        self.route_end = None
 

    def generate_grid(self):
        #possible terrain types
        terrain_types = ["person", "dancefloor_tile"]

        #radom grid
        self.grid = [
            [random.choice(terrain_types) for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
        ]

        #gererate random start and end point
        self.route_start = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        self.route_end = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
  
        #start and end cannot be same
        while self.route_start == self.route_end:
            self.route_end = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        
        print("Found start", self.route_start)
        print("Found end", self.route_end)