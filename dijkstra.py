import heapq
from map import get_terrain_costs

#mabye looks like much from start, made first a pseudocode on paper. 
# then drawed it on paper
#then gave it a try in code and worked first try.... ups....


class Dijkstra:

    def __init__(self, grid, box_size):
        self.grid = grid 
        self.box_size = box_size  
        self.terrain_costs = get_terrain_costs()  

    def dijkstra(self, start, goal):

        queue = [] #list to store nodes able to explore...
        heapq.heappush(queue, (0, start))  #startnode with cost 0
        
        costs = {start: 0} #calculates or tracks costs to reach node...
        previous = {start: None} #stores previous node so able to make a path in the end
        
        while queue: #keeps looping untill no nodes left, while better than for loop because not know left.
            current_cost, current_node = heapq.heappop(queue)

            if current_node == goal: 
                break # if the end or better called goal is reached stop looking....

            neighbors = self.get_neighbors(current_node) #neighbors of current node

            for neighbor in neighbors:
                terrain_type = self.grid[neighbor[1]][neighbor[0]]  #what is the terrain type?
                terrain_cost = self.terrain_costs.get(terrain_type, float('inf'))  #what does terrain cost?
                new_cost = current_cost + terrain_cost #what is the new cost?
                
                #wants cheapest path, keeps checking for cheaper alternatives...
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost #updates costs
                    previous[neighbor] = current_node #what is the previeuws node
                    heapq.heappush(queue, (new_cost, neighbor)) #pushes neighbort onto queue

        path = [] #important to keep track
        current = goal

        #to build path
        while current is not None:
            path.append(current)
            current = previous.get(current)
        path.reverse()
        return path

    def get_neighbors(node, grid):
        x, y = node #curent node
        neighbors = [] #lists of neigbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #directions; down, right, up, left (is changeable)
        
        for dx, dy in directions:
            neighbor = (x + dx, y + dy) #calculate neighbor coordinates
            if 0 <= neighbor[0] < len(grid[0]) and 0 <= neighbor[1] < len(grid): #if neighborg is in the grid add to list
                neighbors.append(neighbor)
        return neighbors #return list of neigbors
