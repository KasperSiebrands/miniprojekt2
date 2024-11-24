"""
this file is to keep a overview of all helper functions. that are not part of any classes/objects.
"""

def get_terrain_costs():
    terrain_costs = {
    "person": 1000,
    "dancefloor_tile": 1
    }
    
    return terrain_costs

def get_terrain_type(grid, x, y):
    """Returns the terrain type at position (x, y)"""
    return grid[x][y]  # Accessing the terrain type from the grid

