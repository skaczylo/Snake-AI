import pygame
import snake
import drawGame


ROWS = 10
COLS = 10
X_SNAKE = 3 #Siempre va a ser 3
Y_SNAKE = ROWS//2
FRECUENCY = 5
FPS = 60


class Game:

    def __init__(self):

        num_apples = 0
        self.snake = snake.Snake(pygame.Vector2(X_SNAKE,Y_SNAKE))
        self.board =snake.Tablero(ROWS,COLS,self.snake)
        self.graphics = drawGame.DrawBoard(self.board)
        self.end = False


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end = True
            elif event == snake.ENDGAMEEVENT:
                self.end = True
            elif event == snake.BODYCRASH:
                self.end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.board.snakeChangesToward(snake.RIGHT)
                if event.key == pygame.K_a:
                    self.board.snakeChangesToward(snake.LEFT)
                if event.key == pygame.K_s:
                    self.board.snakeChangesToward(snake.DOWN)
                if event.key == pygame.K_w:
                    self.board.snakeChangesToward(snake.UP)

    def update(self):
        
            # Actualizar la posición de la serpiente
            self.board.snakeEats()
            self.board.snakeMoves()
            self.graphics.drawBoard()
            self.graphics.drawSnake()
            self.graphics.drawApple(self.board.apple)
            

    def run(self):
         # pygame setup
        pygame.init()
        clock = pygame.time.Clock()
        self.graphics.drawBoard()
        elapsed_time = 0.0  # Tiempo acumulado para mover la serpiente

        try:
            while not self.end:
                dt = clock.tick(FPS) / 1000  # Delta time en segundos (para 60 FPS)
            
                elapsed_time += dt
                if elapsed_time >= 1 / FRECUENCY:  # 1 / frecuency = T periodo
                    self.update()
                    elapsed_time -= 1 / FRECUENCY  # Reducir el tiempo acumulado

                self.handle_events()
                # flip() the display to mostrar en pantalla
                pygame.display.flip()
        except snake.GameOverException as e:
            print(f"Game over")
        pygame.quit()

# Ejecutar el juego si el archivo es ejecutado directamente
if __name__ == "__main__":
    game = Game()
    game.run()
           
    