import pygame 
import sys    
from Astar import Astar
from dancefloor_grid import Grid
from helpers import draw_grid
from settings import WINDOW_SIZE, TILE_SIZE, GRID_SIZE, COLORS


def window():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  
    pygame.display.set_caption("mini project 2 dancefloor")  

    return screen


def draw_path(screen, path, tile_size):
    if path:  #check if path is found 

        for i in range(len(path) - 1): 
            start_pos = (path[i][1] * tile_size + tile_size // 2, path[i][0] * tile_size + tile_size // 2)
            end_pos = (path[i + 1][1] * tile_size + tile_size // 2, path[i + 1][0] * tile_size + tile_size // 2 )

            pygame.draw.line(screen, (255, 140, 0), start_pos, end_pos, 5)  #draws line between start en end point based on values gotten from dijkstra's algoritm
            

def main():
    pygame.init()
    screen = window() #create window

     # Create and generate the grid
    grid_object = Grid(GRID_SIZE, TILE_SIZE)
    grid_object.generate_grid()
  
    # Initialize astar
    astar = Astar(grid_object.grid, TILE_SIZE)

    # Calculate the start and goal points
    start = grid_object.start
    goal = grid_object.end
    path = astar.astar_algorithm(start, goal)
    print("Found path:", path)

    # Draw the grid on the screen
    draw_grid(screen, grid_object, COLORS)
    draw_path(screen, path, TILE_SIZE)
    
    # Update the screen with the initial grid
    pygame.display.flip()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

                    # Check if 'n' key is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                #Refresh the grid and path when 'n' is pressed
                grid_object.generate_grid()  # Re-generate the grid
                start = grid_object.start
                goal = grid_object.end
                astar = Astar(grid_object.grid, TILE_SIZE)
                path = astar.astar_algorithm(start, goal)  # Re-run astar algorithm
                print("Found path:", path)

        	    #redraw
                screen.fill((0,0,0)) #clear screen
                draw_grid(screen, grid_object, COLORS)  # Redraw the grid
                draw_path(screen, path, TILE_SIZE)  # Redraw the path
                pygame.display.flip()  # Update the display

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
