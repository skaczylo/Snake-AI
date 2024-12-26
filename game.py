# Example file showing a circle moving on screen
import pygame 
import snake
import drawGame



# pygame setup
pygame.init()

clock = pygame.time.Clock()
dt = 0
num = 1
running = True

serpiente = snake.Snake(pygame.Vector2(1,1))
tablero = snake.Tablero(10,10,serpiente)
board = drawGame.DrawBoard(tablero,30,"Green","White")
speed = 0.00000000001

frecuency = 1 #frecuencia: numero de casillas que ha de avanzar la serpiente en un segundo

elapsed_time = 0.0  # Tiempo acumulado para mover la serpiente
while running:

    dt = clock.tick(60) / 1000  # Delta time en segundos (para 60 FPS)
    elapsed_time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event == snake.ENDGAMEEVENT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                tablero.snakeChangesToward(snake.RIGHT)
            if event.key == pygame.K_a:
                tablero.snakeChangesToward(snake.LEFT)
            if event.key == pygame.K_s:
                tablero.snakeChangesToward(snake.UP)
            if event.key == pygame.K_w:
                tablero.snakeChangesToward(snake.DOWN)



    if elapsed_time >= 1 / frecuency:  #1/frecuency = T periodo
        # Actualizar la posición de la serpiente
        tablero.snakeMoves()
        elapsed_time -= 1 / frecuency  # Reducir el tiempo acumulado

   
    board.drawBoard()
    board.drawSnake()
    board.drawApple(tablero.apple)
    # flip() the display to put your work on screen

    pygame.display.flip()
   

pygame.quit()