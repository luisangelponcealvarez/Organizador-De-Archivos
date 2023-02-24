import pygame
import sys
from pygame.locals import *

# Define width and height of the window 
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Example') 
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Update the display
    pygame.display.update()
