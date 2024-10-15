import pygame
from map_layout import map_layout  # Import the map layout from the new file

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

    # Loop map_layout
    for y, row in enumerate(map_layout):
        for x, terrain_type in enumerate(row):
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

