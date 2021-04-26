from collections import deque
import grids
import turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('A BFS MAze solving program')
# wn.setup(1300, 700)

SCREEN_SIZE= None

def setup_grid(grid):

    global SCREEN_SIZE
    # print(len(grid))
    # print(len(grid[0]))
    SCREEN_SIZE = ( len(grid[0])*23 +20, len(grid)*23 +20)
    # print(SCREEN_SIZE)



def transform_coordinate(x, y):

    transform_x = x*22 - SCREEN_SIZE[0]//2.2 +10
    transform_y = -y*22 + SCREEN_SIZE[1]//2.2 -10

    return transform_x,transform_y





class DrawPixel(turtle.Turtle):
    def __init__(self, color):
        turtle.Turtle.__init__(self, visible=False)
        self.shape('square')
        self.color(color)
        self.penup()
        self.speed(0)


class BFS:

    def __init__(self, grid, wallPixel, startPixel, endPixel):

        self.grid = grid
        #self.solved_grid = copy.deepcopy(self.grid)
        self.queue = deque()
        self.visited= set()
        self.parent = {}
        self.path = []
        self.walls = []        
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.setup_grid(wallPixel, startPixel, endPixel)

    def setup_grid(self, wallPixel, startPixel, endPixel):

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                character = self.grid[row][col]

                if  character == 's':
                    self.start_x, self.start_y = col, row
                    screen_x, screen_y = transform_coordinate(col, row)
                    startPixel.goto(screen_x, screen_y)
                    startPixel.stamp()

                elif character == 'e':
                    self.path.append((col, row))
                    self.end_x, self.end_y = col, row
                    screen_x, screen_y = transform_coordinate(col, row)
                    endPixel.goto(screen_x, screen_y)
                    endPixel.stamp()

                elif character == ' ':
                    self.path.append((col, row))
                elif character == '+':
                    self.walls.append((col, row))         
                    screen_x, screen_y = transform_coordinate(col, row)
                    wallPixel.goto(screen_x, screen_y)
                    wallPixel.stamp()

    def search(self, visitedPixel):
        self.queue.append((self.start_x, self.start_y))
        self.parent[(self.start_x, self.start_y)] = (self.start_x, self.start_y)

        cur_coordinate = None

        while len(self.queue) > 0:

            cur_x, cur_y = self.queue.popleft()            

            if (cur_x, cur_y) == (self.end_x, self.end_y):
                break
            else:
                ## check left element 
                if  not (cur_x -1, cur_y) in self.visited and \
                        (cur_x -1, cur_y) in self.path:
                    self.parent[(cur_x -1, cur_y)] = cur_x, cur_y
                    self.queue.append((cur_x -1, cur_y))
                    self.visited.add((cur_x -1, cur_y))
                    screen_x, screen_y = transform_coordinate(cur_x -1, cur_y)
                    visitedPixel.goto(screen_x, screen_y)
                    visitedPixel.stamp()
                
                ## check right element
                if  not (cur_x +1, cur_y) in self.visited and \
                        (cur_x +1, cur_y) in self.path:
                    self.parent[(cur_x +1, cur_y)] = cur_x, cur_y
                    self.queue.append((cur_x +1, cur_y))
                    self.visited.add((cur_x +1, cur_y))
                    screen_x, screen_y = transform_coordinate(cur_x +1, cur_y)
                    visitedPixel.goto(screen_x, screen_y)
                    visitedPixel.stamp()
                
                ##check up element
                if  not (cur_x, cur_y -1) in self.visited and \
                        (cur_x, cur_y -1) in self.path:
                    self.parent[(cur_x, cur_y -1)] = cur_x, cur_y
                    self.queue.append((cur_x, cur_y -1))
                    self.visited.add((cur_x, cur_y -1))
                    screen_x, screen_y = transform_coordinate(cur_x, cur_y -1)
                    visitedPixel.goto(screen_x, screen_y)
                    visitedPixel.stamp()
                
                ##check down element
                if  not (cur_x, cur_y +1) in self.visited and \
                        (cur_x, cur_y +1) in self.path:
                    self.parent[(cur_x, cur_y +1)] = cur_x, cur_y
                    self.queue.append((cur_x, cur_y +1))
                    self.visited.add((cur_x, cur_y +1))
                    screen_x, screen_y = transform_coordinate(cur_x, cur_y +1)
                    visitedPixel.goto(screen_x, screen_y)
                    visitedPixel.stamp()
                
        
    def find_path(self, backpathPixel):

        cur_x, cur_y = self.end_x, self.end_y

        while (cur_x, cur_y) != (self.start_x, self.start_y):
            if (cur_x, cur_y) != (self.end_x, self.end_y):
                new_string = self.grid[cur_y][:cur_x]+'#'+self.grid[cur_y][cur_x+1:]
                self.grid[cur_y] = new_string
                #self.grid[cur_y][cur_x] = '#'
                screen_x, screen_y = transform_coordinate(cur_x, cur_y)
                backpathPixel.goto(screen_x, screen_y)
                backpathPixel.stamp()

            cur_x, cur_y = self.parent.get((cur_x, cur_y))

    
    def display_grid(self):
        
        for row in range(len(self.grid)):
            #for col in range(len(self.grid[row])):
            print(f'\t\t{self.grid[row]}')


if __name__ == '__main__':
    setup_grid(grids.grid1)
    wn.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])

    wallBlock = DrawPixel('white')
    startBlock = DrawPixel('red')
    endBlock = DrawPixel('blue')
    visitedBlock = DrawPixel('green')
    backtrackBlock = DrawPixel('yellow')
    
    #display_grid(grid5, wallBlock, startBlock, endBlock)

    bfsvisual  = BFS(grids.grid1, wallBlock, startBlock, endBlock)
    bfsvisual.search(visitedBlock)
    bfsvisual.find_path(backtrackBlock)
   
    wn.exitonclick()
