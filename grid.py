from map_layout import map_layout

def create_grid(map_layout):

    grid = []

    for row in map_layout:
        grid.append(row)

    return grid

grid = create_grid(map_layout)

for row in grid:
    print(row)
