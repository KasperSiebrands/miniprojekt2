import pygame
from map_layout import map_layout  

def get_start_end_positions():

    start_position = (100, 150)  # start
    end_position = (725, 675)   #end

    return start_position, end_position

def start_end_colour():
    START_COLOR = (245, 32, 98)  #start
    END_COLOR = (98, 49, 235)    #end

    return START_COLOR, END_COLOR

def get_terrain_costs():
    terrain_costs = {
        'grass': 1,
        'beach': 2,
        'snow': 2,
        'water': 3,
        'mountains': 5
    }
    return terrain_costs

def terrain_tile_size():
    tile_size = 25
    return tile_size

def draw_map(screen):

    grass_color = (23, 230, 100)   #grass
    water_color = (13, 120, 255)    #water
    mount_color = (160, 160, 160)   # mountain
    snoww_color = (255, 255, 255)     # Snow
    beach_color = (255, 215, 0)       # beach

    size_tile = terrain_tile_size()

    start_position, end_position = get_start_end_positions()
    START_COLOR, END_COLOR = start_end_colour()

    # Loop map_layout
    for y, row in enumerate(map_layout):
        for x, terrain_type in enumerate(row):
            if terrain_type == 'grass':
                pygame.draw.rect(screen, grass_color, (x * size_tile, y * size_tile, size_tile, size_tile))
            elif terrain_type == 'water':
                pygame.draw.rect(screen, water_color, (x * size_tile, y * size_tile, size_tile, size_tile))
            elif terrain_type == 'mount':
                pygame.draw.rect(screen, mount_color, (x * size_tile, y * size_tile, size_tile, size_tile))
            elif terrain_type == 'snoww':
                pygame.draw.rect(screen, snoww_color, (x * size_tile, y * size_tile, size_tile, size_tile))
            elif terrain_type == 'beach':
                pygame.draw.rect(screen, beach_color, (x * size_tile, y * size_tile, size_tile, size_tile))
      

#draw rect start and end
    pygame.draw.rect(screen, START_COLOR, (start_position[0], start_position[1], 25, 25))

    pygame.draw.rect(screen, END_COLOR, (end_position[0], end_position[1], 25, 25))


