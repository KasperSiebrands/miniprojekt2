import pygame
import random

class Grid:
    def __init__(self, grid_size, tile_size):
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.grid = []
        self.start = None
        self.end = None
 

    def generate_grid(self):
        #possible terrain types
        terrain_types = ["person", "dancefloor_tile"]

        #radom grid
        self.grid = [
            [random.choice(terrain_types) for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
        ]

        #gererate random start and end point
        self.start = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        self.end = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
  
        #start and end cannot be same
        while self.start == self.end:
            self.end = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        
        print("Found start", self.start)
        print("Found end", self.end)