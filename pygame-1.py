import pygame

# inicializa la librería pygame
pygame.init()

# crea una ventana de 800 x 600
screen = pygame.display.set_mode((800, 600))

# loop principal del juego
while True:
    # mira los eventos del mouse (clic, mover, arrastrar)
    for event in pygame.event.get():
        # comprueba si se hace click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Se ha hecho clic")

    # actualiza la pantalla
    pygame.display.update()
