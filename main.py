import pygame  
import sys    

from helpers import window, draw_grid, draw_path # Utility functions for window management and rendering
from dancefloor_grid import Grid # Handles grid creation and management
from Astar import Astar # Implementation of the A* pathfinding algorithm
from settings import WINDOW_SIZE, TILE_SIZE, GRID_SIZE, COLORS, TITLE #constants for this script

"""
This program creates a visual representation of a grid-based map (a dancefloor) where 
an A* pathfinding algorithm calculates and displays with an orange line the shortest path 
between a start and goal point. 

- The grid/map is generated dynamically.
- The user can press 'n' to refresh the grid and path.  ('n' for new)
- Pygame is used for graphical rendering.
"""

def show_map_and_route(screen, grid_size, tile_size, colors):
    """
    Generates and displays the grid along with the path calculated by 
    the A* algorithm on the given screen.

    Parameters:
    - screen (pygame.Surface): The Pygame window where everything is drawn.
    - grid_size (tuple): The dimensions of the grid (rows, columns).
    - tile_size (int): The size of each tile in pixels.
    - colors (dict): A dictionary of color definitions used for the grid.
    """
    #clear screen
    screen.fill((0,0,0)) 

    # Create and generate the grid
    grid_object = Grid(grid_size, tile_size)
    grid_object.generate_grid()
  
    # Initialize Astar algorithm with the generated grid
    astar = Astar(grid_object.grid, tile_size)

    # Calculate the shortest path using A*
    path = astar.astar_algorithm(grid_object.route_start, grid_object.route_end)
    print("Found path:", path)

    # Draw the grid and calculated path on the screen
    draw_grid(screen, grid_object, colors)
    draw_path(screen, path, tile_size)
    
    # Update the screen with the initial grid
    pygame.display.flip()


def main():
    """
    The main entry point of the program. Initializes Pygame, creates the window, 
    and runs the main loop for rendering the grid and responding to user input.
    """

    pygame.init()
    screen = window(WINDOW_SIZE, WINDOW_SIZE, TITLE) #create a pygame window

    #display the initial grid and path
    show_map_and_route(screen, GRID_SIZE, TILE_SIZE, COLORS)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Handles window close
                running = False

            # Check if 'n' key is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                #Refresh the grid and path when 'n' is pressed
                show_map_and_route(screen, GRID_SIZE, TILE_SIZE, COLORS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
