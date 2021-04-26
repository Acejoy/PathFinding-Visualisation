from collections import deque
import grids


class DFS:

    def __init__(self, grid):

        self.grid = grid
        #self.solved_grid = copy.deepcopy(self.grid)
        #self.queue = deque()
        self.visited= set()
        self.parent = {}
        self.path = []
        self.walls = []        
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.setup_grid()

    def setup_grid(self):

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                character = self.grid[row][col]

                if  character == 's':
                    self.start_x, self.start_y = col, row
                elif character == 'e':
                    self.path.append((col, row))
                    self.end_x, self.end_y = col, row
                elif character == ' ':
                    self.path.append((col, row))
                elif character == '+':
                    self.walls.append((col, row))         

    def search(self, cur_coordinate):
        #self.queue.append((self.start_x, self.start_y))
        self.parent[(self.start_x, self.start_y)] = (self.start_x, self.start_y)

        cur_x, cur_y = cur_coordinate

        # while len(self.queue) > 0:
               

        if (cur_x, cur_y) == (self.end_x, self.end_y):
            return
        else:
            ## check left element 
            if  not (cur_x -1, cur_y) in self.visited and \
                    (cur_x -1, cur_y) in self.path:
                self.parent[(cur_x -1, cur_y)] = cur_x, cur_y
                #self.queue.append((cur_x -1, cur_y))
                self.visited.add((cur_x -1, cur_y))
                self.search((cur_x -1, cur_y))
            
            ## check right element
            if  not (cur_x +1, cur_y) in self.visited and \
                    (cur_x +1, cur_y) in self.path:
                self.parent[(cur_x +1, cur_y)] = cur_x, cur_y
                #self.queue.append((cur_x +1, cur_y))
                self.visited.add((cur_x +1, cur_y))
                self.search((cur_x +1, cur_y))
            
            ##check up element
            if  not (cur_x, cur_y -1) in self.visited and \
                    (cur_x, cur_y -1) in self.path:
                self.parent[(cur_x, cur_y -1)] = cur_x, cur_y
                #self.queue.append((cur_x, cur_y -1))
                self.visited.add((cur_x, cur_y -1))
                self.search((cur_x, cur_y -1))
            
            ##check down element
            if  not (cur_x, cur_y +1) in self.visited and \
                    (cur_x, cur_y +1) in self.path:
                self.parent[(cur_x, cur_y +1)] = cur_x, cur_y
                #self.queue.append((cur_x, cur_y +1))
                self.visited.add((cur_x, cur_y +1))
                self.search((cur_x, cur_y +1))
                
        
    def find_path(self):

        cur_x, cur_y = self.end_x, self.end_y

        while (cur_x, cur_y) != (self.start_x, self.start_y):
            if (cur_x, cur_y) != (self.end_x, self.end_y):
                new_string = self.grid[cur_y][:cur_x]+'#'+self.grid[cur_y][cur_x+1:]
                self.grid[cur_y] = new_string
                #self.grid[cur_y][cur_x] = '#'
            
            cur_x, cur_y = self.parent.get((cur_x, cur_y))

    
    def display_grid(self):
        
        for row in range(len(self.grid)):
            #for col in range(len(self.grid[row])):
            print(f'\t\t{self.grid[row]}')



if __name__ == '__main__':
    grid_solver= DFS(grids.grid1) 
    grid_solver.display_grid()   
    print()
    grid_solver.search((grid_solver.start_x, grid_solver.start_y))
    grid_solver.find_path()
    grid_solver.display_grid()