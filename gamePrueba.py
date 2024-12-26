# Example file showing a circle moving on screen
import pygame 
import snake
import random

LEFT = pygame.Vector2(-1,0)
RIGHT = pygame.Vector2(1,0)
UP = pygame.Vector2(0,1)
DOWN=pygame.Vector2(0,-1)

def generateApple(max_x,max_y):
    return pygame.Vector2(random.randint(0,max_x),random.randint(0,max_y))


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

num = 1
mysnake = snake.Snake(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))

apple = generateApple(1280,720)
#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
screen.fill("purple")
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mysnake.move(RIGHT*10)
            if event.key == pygame.K_a:
                mysnake.move(LEFT*10)
            if event.key == pygame.K_s:
                mysnake.move(UP*10)
            if event.key == pygame.K_w:
                mysnake.move(DOWN*10)


    # fill the screen with a color to wipe away anything from last frame
    

    pygame.draw.rect(screen, "red", (mysnake.head,(20,20)))
    pygame.draw.circle(screen,"blue",apple,10)
    keys = pygame.key.get_pressed()
  
    
    # flip() the display to put your work on screen

    pygame.display.flip()
   

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()

