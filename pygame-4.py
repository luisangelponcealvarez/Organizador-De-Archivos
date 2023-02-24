import pygame 

# Initialize the game
pygame.init()
# Create the game window
screen = pygame.display.set_mode((600, 600))
running = True
while running:
    # quit when window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen 
    pygame.display.update()
# imports 
import pygame 

# Initialize the game
pygame.init()

# Create the game window
screen = pygame.display.set_mode((600, 600))

# Main loop
running = True
while running:
    # quit when window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen 
    pygame.display.update()
