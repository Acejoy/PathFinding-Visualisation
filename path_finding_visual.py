import pygame
from collections import deque
import time


pygame.init()
width = 600
height = 400




white_color = (255, 255, 255)
red_color = (255,0,0)
blue_color  = (0, 0, 255)
green_color = (0, 255, 0)
yellow_color = (255, 255, 0)
black_color = (0,0,0)

class Grid:

    def draw_rect(self, x, y, color):
        rect = pygame.Rect(x, y, 20, 20)
        rectBorder = pygame.Rect(x, y, 20, 20)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, black_color, rectBorder, 2)

    def __init__(self):
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Grid')
        self.grid = [[' ' for i in range(width//20)] for j in range(height//20)]

        for row in range(height//20):
            
            self.grid[row][0] = '+'
            self.grid[row][(width-20)//20] = '+'
            
            self.draw_rect(0, row*20, white_color)
            self.draw_rect(width-20, row*20, white_color)

        for col in range(width//20):

            self.grid[0][col] = '+'
            self.grid[(height-20)//20][col] = '+'

            self.draw_rect(col*20, 0, white_color)
            self.draw_rect(col*20, height-20, white_color)
                    
        self.start_x = 20
        self.start_y = 20
        self.end_x = width-40
        self.end_y = height-40

        self.draw_rect(20,20, red_color)
        self.draw_rect(width-40,height-40, blue_color)

        self.grid[self.start_y//20][self.start_x//20] = 's'
        self.grid[self.end_y//20][self.end_x//20] = 'e'
        
        self.walls = []
        self.path = []
        self.parent = {}
        self.visited= set()             
        self.solved = False
        pygame.display.flip()

    def clear(self):
        self.__init__()

    def bfs(self):       
        queue = deque()

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                character = self.grid[row][col]

                
                if character == 'e':
                    self.path.append((col, row))                    
                elif character == ' ':
                    self.path.append((col, row))
                elif character == '+':
                    self.walls.append((col, row))   
            
        queue.append((self.start_x//20, self.start_y//20))
        self.parent[(self.start_x//20, self.start_y//20)] = (self.start_x//20, self.start_y//20)

        while len(queue) > 0:
            
            time.sleep(0.02)

            cur_x, cur_y = queue.popleft()            

            if (cur_x, cur_y) == (self.end_x//20, self.end_y//20):
                break
            else:
                ## check left element 
                if  not (cur_x -1, cur_y) in self.visited and \
                        (cur_x -1, cur_y) in self.path:
                    self.parent[(cur_x -1, cur_y)] = cur_x, cur_y
                    queue.append((cur_x -1, cur_y))
                    self.visited.add((cur_x -1, cur_y))
                    self.draw_rect((cur_x -1)*20, cur_y*20, green_color)
                    pygame.display.flip()

                ##check down element
                if  not (cur_x, cur_y +1) in self.visited and \
                        (cur_x, cur_y +1) in self.path:
                    self.parent[(cur_x, cur_y +1)] = cur_x, cur_y
                    queue.append((cur_x, cur_y +1))
                    self.visited.add((cur_x, cur_y +1))
                    self.draw_rect(cur_x*20, (cur_y +1)*20, green_color)
                    pygame.display.flip()
                
                ## check right element
                if  not (cur_x +1, cur_y) in self.visited and \
                        (cur_x +1, cur_y) in self.path:
                    self.parent[(cur_x +1, cur_y)] = cur_x, cur_y
                    queue.append((cur_x +1, cur_y))
                    self.visited.add((cur_x +1, cur_y))
                    self.draw_rect((cur_x +1)*20, cur_y*20, green_color)
                    pygame.display.flip()
                
                ##check up element
                if  not (cur_x, cur_y -1) in self.visited and \
                        (cur_x, cur_y -1) in self.path:
                    self.parent[(cur_x, cur_y -1)] = cur_x, cur_y
                    queue.append((cur_x, cur_y -1))
                    self.visited.add((cur_x, cur_y -1))
                    self.draw_rect(cur_x*20, (cur_y -1)*20, green_color)
                    pygame.display.flip()          
        
        self.display_backtrack_path()

    def dfs(self):
        
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                character = self.grid[row][col]

                
                if character == 'e':
                    self.path.append((col, row))                    
                elif character == ' ':
                    self.path.append((col, row))
                elif character == '+':
                    self.walls.append((col, row))   
        self.dfs_search(self.start_x//20, self.start_y//20)
        self.display_backtrack_path()


    def dfs_search(self, cur_x, cur_y):
        time.sleep(0.02)
        self.parent[(self.start_x//20, self.start_y//20)] = (self.start_x//20, self.start_y//20)

        time.sleep(0.02)                
        
        if self.solved:
            return

        if (cur_x, cur_y) == (self.end_x//20, self.end_y//20):
            self.solved = True
            return
        else:

             ## check right element
            if  not self.solved and not (cur_x +1, cur_y) in self.visited and \
                    (cur_x +1, cur_y) in self.path:
                self.parent[(cur_x +1, cur_y)] = cur_x, cur_y
                self.visited.add((cur_x +1, cur_y))
                self.draw_rect((cur_x +1)*20, cur_y*20, green_color)
                pygame.display.flip()
                self.dfs_search(cur_x +1, cur_y)

            
            ##check down element
            if  not self.solved and not (cur_x, cur_y +1) in self.visited and \
                    (cur_x, cur_y +1) in self.path:
                self.parent[(cur_x, cur_y +1)] = cur_x, cur_y
                self.visited.add((cur_x, cur_y +1))
                self.draw_rect(cur_x*20, (cur_y +1)*20, green_color)
                pygame.display.flip()
                self.dfs_search(cur_x , cur_y +1)
            
            ## check left element 
            if  not self.solved and not (cur_x -1, cur_y) in self.visited and \
                    (cur_x -1, cur_y) in self.path:
                self.parent[(cur_x -1, cur_y)] = cur_x, cur_y
                self.visited.add((cur_x -1, cur_y))
                self.draw_rect((cur_x -1)*20, cur_y*20, green_color)
                pygame.display.flip()
                self.dfs_search(cur_x -1, cur_y)
        
            ##check up element
            if  not self.solved and not (cur_x, cur_y -1) in self.visited and \
                    (cur_x, cur_y -1) in self.path:
                self.parent[(cur_x, cur_y -1)] = cur_x, cur_y
                self.visited.add((cur_x, cur_y -1))
                self.draw_rect(cur_x*20, (cur_y -1)*20, green_color)
                pygame.display.flip()
                self.dfs_search(cur_x, cur_y -1)
        
        #self.display_backtrack_path()

    def display_backtrack_path(self):
        #print()
        cur_x = self.end_x//20
        cur_y = self.end_y//20
        
        while (cur_x, cur_y) != (self.start_x//20, self.start_y//20):
            time.sleep(0.02)
            self.draw_rect(cur_x*20, cur_y*20, yellow_color)
            cur_x, cur_y = self.parent.get((cur_x, cur_y))
            pygame.display.flip()
        
            
        

    def draw_block(self, x, y):
        rec_x = (x//20)*20
        rec_y = (y//20)*20
        
        self.grid[y//20][x//20] = '+'

        if rec_x not in [0, width-20] and rec_y not in [0, height-20]:
            self.draw_rect(rec_x, rec_y, white_color)
            pygame.display.flip()


    def mainloop(self):
        running = True

        mouse_down = False

        while running:

            for event in pygame.event.get():
                

                if event.type == pygame.QUIT:
                    running =False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True
                    x, y = event.pos
                    self.draw_block(x,y)

                if mouse_down and event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    self.draw_block(x,y)

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_down = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_d:
                        self.dfs()

                    if event.key == pygame.K_b:
                        self.bfs()                    

                    if event.key == pygame.K_c:
                        self.clear()    
                        
                    

if __name__ == "__main__":
    grid = Grid()
    grid.mainloop()

    pygame.quit()