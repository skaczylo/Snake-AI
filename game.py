# Example file showing a circle moving on screen
import pygame 
import snake
import random
import drawGame

LEFT = pygame.Vector2(-1,0)
RIGHT = pygame.Vector2(1,0)
UP = pygame.Vector2(0,1)
DOWN=pygame.Vector2(0,-1)

# pygame setup
pygame.init()

clock = pygame.time.Clock()
dt = 0
num = 1
running = True

serpiente = snake.Snake(pygame.Vector2(1,1))
tablero = snake.Tablero(10,10,serpiente)
board = drawGame.DrawBoard(tablero,30,"Green","White")

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                serpiente.move(RIGHT)
            if event.key == pygame.K_a:
                serpiente.move(LEFT)
            if event.key == pygame.K_s:
                serpiente.move(UP)
            if event.key == pygame.K_w:
                serpiente.move(DOWN)

    tablero.snakeEats(LEFT)
    
    board.drawBoard()
    board.drawSnake()
    board.drawApple(tablero.apple)
    # flip() the display to put your work on screen

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()