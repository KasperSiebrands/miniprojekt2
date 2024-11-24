import pygame
import random

#colors
COLORS = {
    "person": [(139, 69, 19)], # Brown and blonde
    "dancefloor_tile": [(0, 0, 255), (128, 0, 128), (0, 255, 255), (64, 224, 208), (173, 216, 230), (255, 255, 0), (128, 0, 128), (144, 238, 144) ], #blue, purple, cyan, turqoice.
    
    "start": (0, 255, 0),  # green
    "end": (255, 0, 0)  # red
}

#settings
TILE_SIZE = 25  # each tile is 25 pixels
GRID_SIZE = 32  # window / tilesize = 32
WINDOW_SIZE = GRID_SIZE * TILE_SIZE #change window with tiles and size


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

def get_terrain_costs():
    terrain_costs = {
    "person": 1000,
    "dancefloor_tile": 1
    }
    
    return terrain_costs

def get_terrain_type(grid, x, y):
    """Returns the terrain type at position (x, y)"""
    return grid[y][x]  # Accessing the terrain type from the grid


def draw_grid(screen, grid):
    """draw grid on screen"""
    #Get start and end positions once to avoid repeating the check in the loop
    start = grid.start
    end = grid.end

    for row in range(grid.grid_size):
        for col in range(grid.grid_size):
            tile = grid.grid[row][col]
            color = random.choice(COLORS[tile])

            #draw start
            if (row, col) == start:
                color = COLORS["start"]
                
            #draw end
            elif (row, col) == end:
                color = COLORS["end"]

            #draw a tile
            pygame.draw.rect(screen, color,
                             (col * grid.tile_size, row * grid.tile_size, grid.tile_size, grid.tile_size))

            #draw gridlines
            pygame.draw.rect(screen, (0, 0, 0),  #black lines
                             (col * grid.tile_size, row * grid.tile_size, grid.tile_size, grid.tile_size), 1)

