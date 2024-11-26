"""
This file contains helper functions that are not directly tied to any specific 
class or object. These utility functions handle tasks like terrain cost 
retrieval, grid drawing, and window management for the visualization.
"""
import pygame
import random

def get_terrain_costs():
    """
    Returns a dictionary mapping terrain types to their traversal costs.
    
    - "person": Represents an occupied tile with a high traversal cost.
    - "dancefloor_tile": Represents an open tile with a low traversal cost.
    
    Returns:
    - dict: Terrain types mapped to costs.
    """
    terrain_costs = {
    "person": 1000, #high cost to cross a person tile, because you dont want to make someone angry
    "dancefloor_tile": 1 #open tile with low teraversal cost
    }
    
    return terrain_costs

def get_terrain_type(grid, x, y):
    """
    Retrieves the terrain type for a specific grid cell.
    
    Parameters:
    - grid (list of lists): The terrain grid.
    - x (int): Row index in the grid.
    - y (int): Column index in the grid.
    
    Returns:
    - str: The terrain type of the specified cell.
    """
    return grid[x][y]  # Accessing the terrain type from the grid

def draw_grid(screen, grid, tile_colors):
    """
    Draws the grid on the screen, coloring each tile based on its type.
    
    Parameters:
    - screen (pygame.Surface): The surface to draw on.
    - grid (Grid object): Contains the grid data and metadata.
    - tile_colors (dict): Maps terrain types to color options.
    
    Each tile is drawn based on its terrain type, with special colors for the 
    start and end points. A black gridline separates each tile.
    """
    #Get start and end positions once to avoid repeating the check in the loop
    start = grid.route_start
    end = grid.route_end

    for row in range(grid.grid_size):
        for col in range(grid.grid_size):
            tile = grid.grid[row][col] # Get the terrain type of the current cell
            color = random.choice(tile_colors[tile]) # Pick a random color for the terrain

            #draw start
            if (row, col) == start:
                color = tile_colors["start"]
                
            #draw end
            elif (row, col) == end:
                color = tile_colors["end"]

            #draw a tile
            pygame.draw.rect(screen, color,
                             (col * grid.tile_size, row * grid.tile_size, grid.tile_size, grid.tile_size))

            #draw blackgridlines
            pygame.draw.rect(screen, (0, 0, 0),  
                             (col * grid.tile_size, row * grid.tile_size, grid.tile_size, grid.tile_size), 1)

def window(x_size, y_size, title):
    """
    Creates a Pygame window with the specified dimensions and title.
    
    Parameters:
    - x_size (int): The width of the window in pixels.
    - y_size (int): The height of the window in pixels.
    - title (str): The title to display in the window's title bar.
    
    Returns:
    - pygame.Surface: The created Pygame window surface.
    """
    screen = pygame.display.set_mode((x_size, y_size))  
    pygame.display.set_caption(title)  
    return screen


def draw_path(screen, path, tile_size):
    """
    Draws the path found by the A* algorithm as a series of connected lines.
    
    Parameters:
    - screen (pygame.Surface): The surface to draw on.
    - path (list of tuples): The list of nodes in the path [(x1, y1), (x2, y2), ...].
    - tile_size (int): The size of each grid cell in pixels.
    
    The path is drawn as orange lines connecting each consecutive node.
    """
    if path:  #check if path is found/exists 

        for i in range(len(path) - 1): 
            # Calculate the center of the current node and the next node
            start_pos = (path[i][1] * tile_size + tile_size // 2, path[i][0] * tile_size + tile_size // 2)
            end_pos = (path[i + 1][1] * tile_size + tile_size // 2, path[i + 1][0] * tile_size + tile_size // 2 )

            # Draw a thick orange line between the two nodes
            pygame.draw.line(screen, (255, 140, 0), start_pos, end_pos, 5)  #draws line between start en end point based on values gotten from dijkstra's algoritm
            
