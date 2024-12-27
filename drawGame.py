import pygame
import snake

COLOR_CELL1 =(144, 238, 144)
COLOR_CELL2 = (34, 139, 34)
CELL_SIZE = 30

SNAKE_COLOR = "Red"
APPLE_COLOR = "Blue"

APPLE_IMAGE = "Imagenes/apple.png"
BODY_BOTTOMLEFT = "Imagenes/body_bottomleft.png"
BODY_BOTTOMRIGHT = "Imagenes/body_bottomright.png"
BODY_HORIZONTAL = "Imagenes/body_horizontal.png"
BODY_TOPLEFT = "Imagenes/body_topleft.png"
BODY_TOPRIGHT = "Imagenes/body_topright.png"
BODY_VERTICAL = "Imagenes/body_vertical.png"
HEAD_DOWN = "Imagenes/head_down.png"
HEAD_LEFT = "Imagenes/head_left.png"
HEAD_RIGHT = "Imagenes/head_right.png"
HEAD_UP = "Imagenes/head_up.png"
TAIL_DOWN = "Imagenes/tail_down.png"
TAIL_LEFT = "Imagenes/tail_left.png"
TAIL_RIGHT = "Imagenes/tail_right.png"
TAIL_UP = "Imagenes/tail_up.png"



class DrawBoard:

    def __init__(self,board):

        self.board = board
        self.cell_size = CELL_SIZE
        self.rows = board.rows
        self.cols = board.cols
        self.snake = board.snake

        #Establece el tamanyo de la pantalla
        self.screen = pygame.display.set_mode((CELL_SIZE*self.cols, CELL_SIZE*self.rows))


    def drawBoard(self):

        for row in range(self.rows):
            for col in range(self.cols):
                color = COLOR_CELL1 if (row + col) % 2 == 0 else COLOR_CELL2
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size) #Rect(esquina_sup_izq,ancho,alto)
                pygame.draw.rect(self.screen, color, rect)


    def drawSnake(self):

        #Dibujamos la cabeza
        head_rect = pygame.Rect(int(self.snake.head[0])*self.cell_size,int(self.snake.head[1])*self.cell_size,self.cell_size,self.cell_size)
        if self.snake.toward == snake.RIGHT:
           self.screen.blit(pygame.transform.scale(pygame.image.load(HEAD_RIGHT), (self.cell_size, self.cell_size)),head_rect)
        if self.snake.toward == snake.LEFT:
            self.screen.blit(pygame.transform.scale(pygame.image.load(HEAD_LEFT), (self.cell_size, self.cell_size)),head_rect)
        if self.snake.toward == snake.UP:
            self.screen.blit(pygame.transform.scale(pygame.image.load(HEAD_UP), (self.cell_size, self.cell_size)),head_rect)    
        if self.snake.toward == snake.DOWN:
            self.screen.blit(pygame.transform.scale(pygame.image.load(HEAD_DOWN), (self.cell_size, self.cell_size)),head_rect)

        #Dibujamos el resto del cuerpo: Tenemos que tener en cuenta si hay giros o no
        for i in range(1,self.snake.length-1):
            previous_body = self.snake.body[i-1]
            current_body = self.snake.body[i]
            next_body = self.snake.body[i+1]

            rect = pygame.Rect(int(self.snake.body[i][0])*self.cell_size,
                               int(self.snake.body[i][1])*self.cell_size,
                               self.cell_size,self.cell_size)
            
            #No hay giros
            if previous_body[0] == current_body[0] and current_body[0] == next_body[0]: #Cuerpo vertical 
                self.screen.blit(pygame.transform.scale(pygame.image.load(BODY_VERTICAL), (self.cell_size, self.cell_size)),rect)
            if previous_body[1] == current_body[1] and next_body[1] == current_body[1] : #Cuerpo Horizontal
                self.screen.blit(pygame.transform.scale(pygame.image.load(BODY_HORIZONTAL), (self.cell_size, self.cell_size)),rect)

            
            if (current_body[0]+1 == previous_body[0] and current_body[1]-1==next_body[1]) or (current_body[1]-1 == previous_body[1]and next_body[0]==current_body[0]+1):
                self.screen.blit(pygame.transform.scale(pygame.image.load(BODY_TOPRIGHT), (self.cell_size, self.cell_size)),rect)
            
            if(current_body[0]+1 == next_body[0] and previous_body[1]==current_body[1]+1) or (next_body[1]==current_body[1]+1 and previous_body[0] == current_body[0]+1):
                self.screen.blit(pygame.transform.scale(pygame.image.load(BODY_BOTTOMRIGHT), (self.cell_size, self.cell_size)),rect)
            
            if (next_body[0] == current_body[0]-1 and previous_body[1] == current_body[1]+1) or (previous_body[0] == current_body[0]-1 and next_body[1] == current_body[1]+1):
                 self.screen.blit(pygame.transform.scale(pygame.image.load(BODY_BOTTOMLEFT), (self.cell_size, self.cell_size)),rect)
            
            if (next_body[1] == current_body[1]-1 and previous_body[0] == current_body[0]-1) or (previous_body[1]==current_body[1]-1 and next_body[0] == current_body[0]-1):
                self.screen.blit(pygame.transform.scale(pygame.image.load(BODY_TOPLEFT), (self.cell_size, self.cell_size)),rect)

            
            #Dibujamos la cola
            if next_body == self.snake.tail:
                rectTail = pygame.Rect(int(next_body[0])*self.cell_size,
                               int(next_body[1])*self.cell_size,
                               self.cell_size,self.cell_size)
                
                if next_body[1] + 1== current_body[1]:
                    self.screen.blit(pygame.transform.scale(pygame.image.load(TAIL_UP), (self.cell_size, self.cell_size)),rectTail)

                if next_body[1] - 1== current_body[1]:
                    self.screen.blit(pygame.transform.scale(pygame.image.load(TAIL_DOWN), (self.cell_size, self.cell_size)),rectTail)

                if next_body[0] - 1== current_body[0]:
                    self.screen.blit(pygame.transform.scale(pygame.image.load(TAIL_RIGHT), (self.cell_size, self.cell_size)),rectTail)

                if next_body[0] + 1== current_body[0]:
                    self.screen.blit(pygame.transform.scale(pygame.image.load(TAIL_LEFT), (self.cell_size, self.cell_size)),rectTail)
        

    def drawApple(self,pos):

        rect = pygame.Rect(int(pos[0])*self.cell_size,
                               int(pos[1])*self.cell_size,
                               self.cell_size,self.cell_size)
        self.screen.blit(pygame.transform.scale(pygame.image.load(APPLE_IMAGE), (self.cell_size, self.cell_size)),
                         rect)








