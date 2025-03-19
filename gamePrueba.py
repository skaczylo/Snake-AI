import pygame

# Definición de colores
COLOR_CELL1 = (144, 238, 144)
COLOR_CELL2 = (34, 139, 34)
COLOR_FRAME = (102, 158, 102)
CELL_SIZE = 30
FRAME_MARGIN = 50

# Inicializar Pygame
pygame.init()

# Crear la pantalla principal
screen = pygame.display.set_mode((CELL_SIZE*10 + FRAME_MARGIN * 2, CELL_SIZE*10 + FRAME_MARGIN * 2))

# Crear una Surface para el tablero
board = pygame.Surface((CELL_SIZE*10, CELL_SIZE*10))

# Reloj del juego para controlar los FPS
clock = pygame.time.Clock()

# Dibujar el tablero
for row in range(10):
    for col in range(10):
        color = COLOR_CELL1 if (row + col) % 2 == 0 else COLOR_CELL2
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(board, color, rect)

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar la pantalla con un color de fondo (blanco en este caso)
    screen.fill(COLOR_FRAME)

    # Dibujar el marco alrededor del tablero
    #pygame.draw.rect(screen, COLOR_FRAME, (FRAME_MARGIN, FRAME_MARGIN, CELL_SIZE*10, CELL_SIZE*10), 5)

    # Colocar el tablero en la pantalla (con el margen añadido)
    screen.blit(board, (FRAME_MARGIN, FRAME_MARGIN))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(60)

# Finalizar Pygame
pygame.quit()
