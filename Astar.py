import heapq
from helpers import	get_terrain_costs, get_terrain_type

class Astar:
    """
    Implements the A* pathfinding algorithm on a grid. A* is used to find the 
    shortest path between a start and goal node, considering terrain costs.

    Attributes:
    - grid (list of lists): The grid representing the map/terrain.
    - box_size (int): Size of each grid cell (useful for visualization or scaling).
    - terrain_costs (dict): Mapping of terrain types to their traversal costs.
    """

    
    def __init__(self, grid, box_size):
        """
        Initializes the A* algorithm with a grid and terrain properties.
        
        Parameters:
        - grid (list of lists): The terrain grid.
        - box_size (int): The size of each grid cell in pixels.
        """
        self.grid = grid 
        self.box_size = box_size  
        self.terrain_costs = get_terrain_costs()  # Terrain costs are retrieved from helpers.

    def heuristic(self, node, goal):
        """
        Calculates the heuristic for the A* algorithm, guiding the search 
        towards the goal.

        Parameters:
        - node (tuple): The current node as (x, y).
        - goal (tuple): The goal node as (x, y).

        Returns:
        - int: The Manhattan distance between the current node and the goal.
       
        Alternative:
        -Euclidisch with sqrt((x2-x1)^2 + (y2-y1)^2))
        """
        x1, y1 = node
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2) 

    def astar_algorithm(self, start, goal):
        """
        Executes the A* pathfinding algorithm to find the shortest path between
        a start and goal node.

        Parameters:
        - start (tuple): The starting node (x, y).
        - goal (tuple): The goal node (x, y).

        Returns:
        - list of tuples: The shortest path from start to goal, or an empty list 
          if no path exists.
        """
        # Priority queue to store nodes to explore
        queue = [] #list to store nodes able to explore....
        heapq.heappush(queue, (0, start))  #startnode with cost 0
        
        costs = {start: 0} #tracks costs to reach node...
        previous = {start: None} #stores previous node so able to make a path in the end
        
        while queue: #keeps looping untill no nodes left, while better than for loop because not know left.
            _, current_node = heapq.heappop(queue)


            if current_node == goal: 
                break # if the end or better called goal is reached stop looking....

            neighbors = self.get_neighbors(current_node) #neighbors of current node

            for neighbor in neighbors:
                x, y = neighbor
                terrain_type = get_terrain_type(self.grid, x, y)  # Use new method to get terrain
                terrain_cost = self.terrain_costs.get(terrain_type, float('inf'))  #what does terrain cost?
                new_cost = costs[current_node] + terrain_cost #what is the new cost?
                
                #wants cheapest path, keeps checking for cheaper alternatives...
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost #updates costs
                    priority = new_cost + self.heuristic(neighbor, goal)  # A*: kosten + heuristiek
                    heapq.heappush(queue, (priority, neighbor))
                    previous[neighbor] = current_node

        #reconstruct path from goal to start       
        path = [] 
        current = goal

        #to build path
        while current is not None:
            path.append(current)
            current = previous.get(current)
        path.reverse() # reverse the path to start -> goal
        return path

        
    def get_neighbors(self, node):
        """
        Finds the valid neighbors of a given node.

        Parameters:
        - node (tuple): The current node as (x, y).

        Returns:
        - list of tuples: Neighboring nodes that are within the grid boundaries.
        """
        x, y = node #curent node
        neighbors = [] #lists to store valid neigbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #directions; right, down, left, up (is changeable)
        
        for dx, dy in directions:
            neighbor = (x + dx, y + dy) #calculate neighbor coordinates
            if 0 <= neighbor[0] < len(self.grid[0]) and 0 <= neighbor[1] < len(self.grid): #if neighborg is in the grid add to list
                neighbors.append(neighbor)
                
        return neighbors #return list of neigbors
        
    
    
