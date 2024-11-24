"""
this file is to keep a overview of all helper functions. that are not part of any classes/objects.
"""

import pygame
import random

def get_terrain_costs():
    terrain_costs = {
    "person": 1000,
    "dancefloor_tile": 1
    }
    
    return terrain_costs

def get_terrain_type(grid, x, y):
    """Returns the terrain type at position (x, y)"""
    return grid[x][y]  # Accessing the terrain type from the grid

def draw_grid(screen, grid, tile_colors):
    """draw grid on screen"""
    #Get start and end positions once to avoid repeating the check in the loop
    start = grid.start
    end = grid.end

    for row in range(grid.grid_size):
        for col in range(grid.grid_size):
            tile = grid.grid[row][col]
            color = random.choice(tile_colors[tile])

            #draw start
            if (row, col) == start:
                color = tile_colors["start"]
                
            #draw end
            elif (row, col) == end:
                color = tile_colors["end"]

            #draw a tile
            pygame.draw.rect(screen, color,
                             (col * grid.tile_size, row * grid.tile_size, grid.tile_size, grid.tile_size))

            #draw gridlines
            pygame.draw.rect(screen, (0, 0, 0),  #black lines
                             (col * grid.tile_size, row * grid.tile_size, grid.tile_size, grid.tile_size), 1)


