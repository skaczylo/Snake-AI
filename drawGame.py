import pygame
import snake

SNAKE_COLOR = "Red"
APPLE_COLOR = "Blue"

class DrawBoard:

    def __init__(self,board,cell_size, color1,color2):

        self.board = board
        self.cell_size = cell_size
        self.rows = board.rows
        self.cols = board.cols
        self.color1 = color1
        self.color2 = color2
        self.snake = board.snake

        #Establece el tamanyo de la pantalla
        self.screen = pygame.display.set_mode((cell_size*self.cols, cell_size*self.rows))



    def drawBoard(self):

        for row in range(self.rows):
            for col in range(self.cols):
                color = self.color1 if (row + col) % 2 == 0 else self.color2
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size) #Rect(esquina_sup_izq,ancho,alto)
                pygame.draw.rect(self.screen, color, rect)

    def drawSnake2(self,speed):
         for i in range(self.snake.length):
            rect = pygame.Rect(int(self.snake.body[i][0])*self.cell_size +speed,
                               int(self.snake.body[i][1])*self.cell_size+speed,
                               self.cell_size,self.cell_size)
            pygame.draw.rect(self.screen,SNAKE_COLOR,rect)
            
    def drawSnake(self):
        for i in range(self.snake.length):
            rect = pygame.Rect(int(self.snake.body[i][0])*self.cell_size,
                               int(self.snake.body[i][1])*self.cell_size,
                               self.cell_size,self.cell_size)
            pygame.draw.rect(self.screen,SNAKE_COLOR,rect)
        
    
    def drawApple(self,pos):

        """
        Tenemos en cuenta que pos representaria la esquina superior izquierda de la celda, luego tenemos que calcular 
        el centro de dicha celda
        """
        half_cell = self.cell_size /2
        center = pygame.Vector2(pos[0]*self.cell_size+half_cell,pos[1]*self.cell_size+half_cell)
        pygame.draw.circle(self.screen,APPLE_COLOR,center,self.cell_size//4)






