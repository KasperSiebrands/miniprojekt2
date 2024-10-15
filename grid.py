from collections import deque
from map_layout import map_layout 

def create_grid(map_layout):

    grid = [] #empty list

    for row in map_layout:
        grid.append(row)
    
    print(grid)

    return grid
