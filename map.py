
import pygame
import random

def draw_map(screen):

    grass_color = (23, 230, 100)  # Gras
    water_color = (13, 120, 255)   # Water
    mountain_color = (160, 160, 160)  # Bergen
    snow_color = (255, 255, 255)   # Sneeuw


    tile_size = 25  


    for x in range(32):  # 800 / 25 = 32
        for y in range(32):
   
            #make a map with different terrains
            terrain_type = random.choice(['grass', 'water', 'mountain', 'snow'])

            if terrain_type == 'grass':
                pygame.draw.rect(screen, grass_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'water':
                pygame.draw.rect(screen, water_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'mountain':
                pygame.draw.rect(screen, mountain_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif terrain_type == 'snow':
                pygame.draw.rect(screen, snow_color, (x * tile_size, y * tile_size, tile_size, tile_size))
