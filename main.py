import pygame 
import sys    
from map import draw_map 
from grid import create_grid
from map_layout import map_layout
from dijkstra import Dijkstra
from map import draw_map, get_start_end_positions, terrain_tile_size

pygame.init()

def window():
    window_width = 800
    window_height = 800
    screen = pygame.display.set_mode((window_width, window_height))  
    pygame.display.set_caption("mini project 2")  
    return screen

tile_size = terrain_tile_size()

def draw_path(screen, path):

    if path:  #check if path is found 
        for i in range(len(path) - 1): 

            start_pos = (path[i][0] * tile_size + tile_size // 2, path[i][1] * tile_size + tile_size // 2)
            end_pos = (path[i + 1][0] * tile_size + tile_size // 2, path[i + 1][1] * tile_size + tile_size // 2)

            pygame.draw.aaline(screen, (255, 0, 0), start_pos, end_pos, 5)  #draws line between start en end point based on values gotten from dijkstra's algoritm

screen = window()

white = (255, 255, 255)
black = (0, 0, 0)

screen.fill(white)

draw_map(screen)
grid = create_grid(map_layout) #from grid.py

start_pos, end_pos = get_start_end_positions()

start = (start_pos[0] // tile_size, start_pos[1] // tile_size)  # start converted to grid index
goal = (end_pos[0] // tile_size, end_pos[1] // tile_size)        #end converted to grid index 


#implement dijkstra's algoritm 
dijkstra_implement = Dijkstra(grid, tile_size)
path = dijkstra_implement.dijkstra_algorithm(start, goal)
print("Found path:", path)#if no path is found

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    draw_path(screen, path)#draw a aalines from the values as result of dijkstra's algorthm

    pygame.display.update()

pygame.quit()
sys.exit()
