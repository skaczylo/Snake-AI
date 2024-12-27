import pygame
import snake
import drawGame

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Variables del juego
        self.serpiente = snake.Snake(pygame.Vector2(3, 1))
        self.tablero = snake.Tablero(10, 10, self.serpiente)
        self.board = drawGame.DrawBoard(self.tablero, 20, "Green", "White")

        self.frecuency = 5  # Frecuencia: casillas por segundo
        self.elapsed_time = 0.0  # Tiempo acumulado para mover la serpiente

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event == snake.ENDGAMEEVENT:
                self.running = False
            elif event == snake.BODYCRASH:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.tablero.snakeChangesToward(snake.RIGHT)
                if event.key == pygame.K_a:
                    self.tablero.snakeChangesToward(snake.LEFT)
                if event.key == pygame.K_s:
                    self.tablero.snakeChangesToward(snake.DOWN)
                if event.key == pygame.K_w:
                    self.tablero.snakeChangesToward(snake.UP)

    def update(self, dt):
        self.elapsed_time += dt
        if self.elapsed_time >= 1 / self.frecuency:  # 1 / frecuency = T periodo
            # Actualizar la posición de la serpiente
            self.tablero.snakeEats()
            self.tablero.snakeMoves()
            self.board.drawBoard()
            self.board.drawSnake()
            self.board.drawApple(self.tablero.apple)
            self.elapsed_time -= 1 / self.frecuency  # Reducir el tiempo acumulado

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  # Delta time en segundos (para 60 FPS)
            self.handle_events()
            self.update(dt)

            # flip() the display to mostrar en pantalla
            pygame.display.flip()

        pygame.quit()

# Ejecutar el juego si el archivo es ejecutado directamente
if __name__ == "__main__":
    game = Game()
    game.run()
           
    
