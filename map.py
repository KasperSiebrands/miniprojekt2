# map.py

import pygame
import random

def draw_map(screen):
    # Definieer kleuren
    grass_color = (23, 230, 100)   # Gras
    water_color = (13, 120, 255)    # Water
    mount_color = (160, 160, 160)   # mountain
    snoww_color = (255, 255, 255)     # Snow
    beach_color = (255, 215, 0)       # beach

    # Grootte van de tegels
    tile_size = 25  
    width, height = 32, 32  # Aantal tegels in de breedte en hoogte

    # Hardcoded map-indeling met variatie
    map_layout = [
        [ 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass']




    ]

    # Loop door de map-layout
    for y, row in enumerate(map_layout):
        for x, terrain_type in enumerate(row):
            # Teken de juiste kleur op basis van het type terrein
            if terrain_type == 'grass':
                pygame.draw.rect(screen, grass_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'water':
                pygame.draw.rect(screen, water_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'mountain':
                pygame.draw.rect(screen, mountain_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'snow':
                pygame.draw.rect(screen, snow_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'sand':
                pygame.draw.rect(screen, sand_color, (x * tile_size, y * tile_size, tile_size, tile_size))
