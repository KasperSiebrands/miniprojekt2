# map.py

import pygame
import random

def draw_map(screen):

    grass_color = (23, 230, 100)   # Gras
    water_color = (13, 120, 255)    # Water
    mount_color = (160, 160, 160)   # mountain
    snoww_color = (255, 255, 255)     # Snow
    beach_color = (255, 215, 0)       # beach

   
    START_COLOR = (245, 32, 98)  # red for start
    END_COLOR = (23, 49, 235)    #  blue for end
    start_position = (50, 100)  #start
    end_position = (725, 675)   #end


    tile_size = 25  
    width, height = 32, 32   #800 / 25 = 32

    # Hardcoded map
    map_layout = [
        [ 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'snoww', 'snoww', 'snoww', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'grass', 'grass', 'mount', 'grass', 'grass', 'water', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'snoww', 'snoww', 'snoww'],
        [ 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'snoww', 'snoww', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'grass', 'mount', 'grass', 'grass', 'grass', 'water', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'snoww', 'snoww', 'snoww'],
        [ 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'snoww', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'mount', 'grass', 'water', 'water', 'water', 'water', 'water', 'grass', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'snoww', 'snoww'],
        [ 'water', 'water', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'grass', 'grass', 'water', 'grass', 'water', 'water', 'mount', 'grass', 'mount', 'snoww', 'grass', 'grass', 'grass', 'grass', 'snoww', 'grass'],
        [ 'water', 'beach', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'grass', 'water', 'water', 'mount', 'mount', 'snoww', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
        [ 'water', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'grass', 'grass', 'grass', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
        [ 'grass', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'beach', 'beach', 'beach', 'grass', 'grass', 'grass', 'water', 'water', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'grass', 'water', 'water', 'beach', 'beach', 'beach', 'grass', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'water', 'water', 'beach', 'beach', 'grass', 'grass', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'water', 'water', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'water', 'water', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'mount'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'water', 'water', 'water', 'water', 'water', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'mount', 'grass'],
        [ 'grass', 'grass', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'water', 'water', 'water', 'beach', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'mount', 'mount', 'grass'],
        [ 'grass', 'grass', 'water', 'water', 'mount', 'mount', 'grass', 'mount', 'mount', 'water', 'water', 'water', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'grass', 'snoww', 'snoww'],
        [ 'grass', 'grass', 'water', 'mount', 'mount', 'snoww', 'grass', 'mount', 'water', 'water', 'beach', 'beach', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'snoww', 'snoww', 'grass'],
        [ 'grass', 'grass', 'grass', 'grass', 'snoww', 'grass', 'grass', 'mount', 'water', 'water', 'beach', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'beach', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'water', 'grass'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'grass', 'water', 'water', 'grass', 'grass', 'mount', 'mount', 'water', 'water', 'grass'],
        [ 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass', 'grass', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'water', 'water', 'water', 'water', 'grass', 'grass', 'mount', 'grass', 'grass', 'grass', 'grass'],
        [ 'grass', 'grass', 'beach', 'grass', 'snoww', 'snoww', 'grass', 'grass', 'grass', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'water', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'snoww', 'snoww', 'grass'],
        [ 'grass', 'water', 'beach', 'mount', 'snoww', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'beach', 'water', 'mount', 'snoww', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass'],
        [ 'water', 'water', 'water', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'water', 'mount', 'beach', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount'],
        [ 'water', 'water', 'grass', 'grass', 'mount', 'grass', 'grass', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'beach', 'water', 'water', 'mount', 'water', 'water', 'water', 'water', 'beach', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount'],
        [ 'water', 'beach', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'grass', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'water', 'water', 'mount', 'mount', 'water', 'grass', 'grass', 'beach', 'beach', 'grass', 'grass', 'grass', 'mount', 'mount'],
        [ 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'water', 'grass', 'grass', 'grass', 'grass', 'beach', 'beach', 'water', 'water', 'mount', 'mount', 'mount', 'grass', 'grass', 'grass', 'mount', 'grass', 'grass', 'grass', 'grass', 'snoww', 'mount'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'water', 'grass', 'grass', 'grass', 'grass', 'beach', 'beach', 'beach', 'beach', 'water', 'mount', 'mount', 'mount', 'grass', 'grass', 'mount', 'grass', 'grass', 'grass', 'water', 'snoww', 'water'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'grass', 'beach', 'water', 'grass', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water'],
        [ 'grass', 'grass', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water'],
        [ 'grass', 'grass', 'water', 'water', 'grass', 'beach', 'grass', 'grass', 'grass', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
        [ 'grass', 'grass', 'grass', 'water', 'water', 'water', 'grass', 'grass', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'grass'],
        [ 'grass', 'grass', 'grass', 'water', 'water', 'beach', 'grass', 'grass', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount', 'grass'],
        [ 'beach', 'grass', 'grass', 'water', 'beach', 'grass', 'grass', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'mount', 'mount'],
        [ 'beach', 'grass', 'grass', 'beach', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'beach', 'beach', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'beach', 'mount'],
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'water', 'water', 'water', 'grass', 'grass', 'grass', 'grass', 'beach', 'beach', 'grass', 'grass', 'grass', 'grass', 'beach', 'water', 'water', 'grass', 'grass', 'grass', 'water', 'water', 'beach', 'grass']
    ]

    # Loop door de map-layout
    for y, row in enumerate(map_layout):
        for x, terrain_type in enumerate(row):
            # Teken de juiste kleur op basis van het type terrein
            if terrain_type == 'grass':
                pygame.draw.rect(screen, grass_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'water':
                pygame.draw.rect(screen, water_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'mount':
                pygame.draw.rect(screen, mount_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'snoww':
                pygame.draw.rect(screen, snoww_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'beach':
                pygame.draw.rect(screen, beach_color, (x * tile_size, y * tile_size, tile_size, tile_size))
      

#draw rect start and end
    pygame.draw.rect(screen, START_COLOR, (start_position[0], start_position[1], 25, 25))

    pygame.draw.rect(screen, END_COLOR, (end_position[0], end_position[1], 25, 25))

    terrain_costs = {
        'grass': 1,
        'beach': 2,
        'snow': 2,
        'water': 3,
        'mountains': 5
    }

