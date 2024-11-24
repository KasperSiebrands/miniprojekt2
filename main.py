import pygame 
import sys    
from helpers import window, draw_grid, draw_path
from dancefloor_grid import Grid
from Astar import Astar
from settings import WINDOW_SIZE, TILE_SIZE, GRID_SIZE, COLORS, TITLE

def show_map_and_route(screen, grid_size, tile_size, colors):

    #clear screen
    screen.fill((0,0,0)) 

    # Create and generate the grid
    grid_object = Grid(grid_size, tile_size)
    grid_object.generate_grid()
  
    # Initialize astar
    astar = Astar(grid_object.grid, tile_size)

    # Calculate the start and goal points
    path = astar.astar_algorithm(grid_object.route_start, grid_object.route_end)
    print("Found path:", path)

    # Draw the grid on the screen
    draw_grid(screen, grid_object, colors)
    draw_path(screen, path, tile_size)
    
    # Update the screen with the initial grid
    pygame.display.flip()


def main():
    pygame.init()
    screen = window(WINDOW_SIZE, WINDOW_SIZE, TITLE) #create window

    show_map_and_route(screen, GRID_SIZE, TILE_SIZE, COLORS)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check if 'n' key is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                #Refresh the grid and path when 'n' is pressed
                show_map_and_route(screen, GRID_SIZE, TILE_SIZE, COLORS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
