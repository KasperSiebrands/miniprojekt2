import pygame

def draw_map(screen):

    grass_color = (23, 230, 100)
    water_color = (13, 120, 255)

    tile_size = 25  
    for x in range(10):
        for y in range(10):
            if (x + y) % 2 == 0: 
                pygame.draw.rect(screen, grass_color, (x * tile_size, y * tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(screen, water_color, (x * tile_size, y * tile_size, tile_size, tile_size))
