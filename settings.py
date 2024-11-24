"""
central file for settings
"""

#colors
COLORS = {
    "person": [(139, 69, 19)], # Brown
    "dancefloor_tile": [
        (0, 0, 255), 
        (128, 0, 128), 
        (0, 255, 255), 
        (64, 224, 208), 
        (173, 216, 230), 
        (255, 255, 0),
        (128, 0, 128),
        (144, 238, 144)
    ], #dancefloor colours
    "start": (0, 255, 0),  # green
    "end": (255, 0, 0)  # red
}

#settings
TILE_SIZE = 25  # each tile is 25 pixels
GRID_SIZE = 32  # window / tilesize = 32
WINDOW_SIZE = GRID_SIZE * TILE_SIZE #change window with tiles and size
TITLE = "mini project 2 dancefloor"