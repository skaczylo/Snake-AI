import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla y el reloj
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Definir el objeto
x = 100
y = 100
speed = 100  # Velocidad del objeto en píxeles por segundo

# Bucle principal
running = True
while running:
    dt = clock.tick(30) / 1000  # delta time en segundos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del objeto
    x += speed * dt  # Mover el objeto en el eje X

    # Dibujar el fondo y el objeto
    screen.fill((0, 0, 0))  # Fondo negro
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))  # Rectángulo rojo

    pygame.display.flip()

pygame.quit()


