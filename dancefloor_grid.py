import random 

class Grid:
    """
    Represents a grid for a dance floor simulation. The grid consists of tiles, 
    each with a randomly assigned terrain type. A random start and end point are 
    also generated for pathfinding.

    Attributes:
    - grid_size (int): The dimensions of the grid (rows and columns).
    - tile_size (int): The size of each tile in pixels (useful for rendering).
    - grid (list of lists): The generated grid with terrain types.
    - route_start (tuple): The starting point (row, column) for pathfinding.
    - route_end (tuple): The ending point (row, column) for pathfinding.
    """

    def __init__(self, grid_size, tile_size):
        """
        Initializes the Grid class with the specified grid size and tile size.
        
        Parameters:
        - grid_size (int): The dimensions of the grid (e.g., 10 for a 10x10 grid).
        - tile_size (int): The size of each tile in pixels.
        """
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.grid = []
        self.route_start = None
        self.route_end = None
    

    def generate_grid(self):
        """
        Generates a grid with random terrain types and determines random start 
        and end points for pathfinding.

        - Terrain types are chosen randomly for each tile.
        - Start and end points are unique and cannot overlap.
        """

        #possible terrain types
        terrain_types = ["person", "dancefloor_tile"]

        # Generate a grid with random terrain types
        self.grid = [
            [random.choice(terrain_types) for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
        ]

        #generate random start and end point
        self.route_start = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        self.route_end = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
  
        #start and end cannot be same
        while self.route_start == self.route_end:
            self.route_end = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        
        # Debugging output for the generated start and end points
        print("Found start", self.route_start)
        print("Found end", self.route_end)