import pygame
import snake
import drawGame

ROWS = 10
COLS = 10
X_SNAKE = 3 #Siempre va a ser 3
Y_SNAKE = ROWS//2
SPEED = 5


class Game:

    def __init__(self):

        self.score = 0
        self.snake = snake.Snake(pygame.Vector2(X_SNAKE,Y_SNAKE))
        self.board =snake.Tablero(ROWS,COLS,self.snake)
        self.graphics = drawGame.DrawGame(self)
        self.end = False
    
        
    def handle_events(self):
        direction = self.snake.direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end = True
            elif event == snake.ENDGAMEEVENT:
                self.end = True
            elif event == snake.BODYCRASH:
                self.end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    direction =  snake.RIGHT
                if event.key == pygame.K_a:
                   direction =  snake.LEFT
                if event.key == pygame.K_s:
                    direction =  snake.DOWN
                if event.key == pygame.K_w:
                    direction =  snake.UP
        
        return direction

    def update_graphics(self):
        self.graphics.drawGame(self.score)
        pygame.display.flip() # flip() the display to mostrar en pantalla
        
     
    def gameOver(self,pos):
        return self.board.bodyCrash(pos) or self.board.bodyOutOfBoard(pos)
    
    
    def next_step(self,direction):
        self.board.snakeChangeDirection(direction)
        self.score += self.board.snakeEats()
        self.board.snakeMoves()


    
    






    
    
           
    