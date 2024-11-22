import pygame 
import sys    
from dijkstra import Dijkstra
from dancefloor import Grid, draw_grid, WINDOW_SIZE, TILE_SIZE, GRID_SIZE

def window():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  
    pygame.display.set_caption("mini project 2 dancefloor")  

    return screen

def draw_path(screen, path, tile_size):
    if path:  #check if path is found 
        for i in range(len(path) - 1): 

            start_pos = (path[i][0] * tile_size + tile_size // 2, path[i][1] * tile_size + tile_size // 2)
            end_pos = (path[i + 1][0] * tile_size + tile_size // 2, path[i + 1][1] * tile_size + tile_size // 2)

            pygame.draw.aaline(screen, (255, 0, 0), start_pos, end_pos, 5)  #draws line between start en end point based on values gotten from dijkstra's algoritm

def main():
    pygame.init()
    screen = window() #create window

     # Create and generate the grid
    grid_object = Grid(GRID_SIZE, TILE_SIZE)
    grid_object.generate_grid()

    # Draw the grid on the screen
    draw_grid(screen, grid_object)

    # Calculate the start and goal points
    start = grid_object.start
    goal = grid_object.end

    # Initialize Dijkstra
    dijkstra = Dijkstra(grid_object.grid, TILE_SIZE)
    path = dijkstra.dijkstra_algorithm(start, goal)
    print("Found path:", path)

    # Update the screen with the initial grid
    pygame.display.flip()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the path on the screen
        draw_path(screen, path, TILE_SIZE)

        # Update the display
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
