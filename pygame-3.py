import pygame

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
done = False

while not done:
    # this loop will continue until the user exits the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
