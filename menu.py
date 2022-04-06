# Importation des libraires et autres classes
import pygame
from constants import *

from constants import HEIGHT, WIDTH

# Initilalisation de la fenêtre
pygame.init()
screen=pygame.display.set_mode(WINDOW_SIZE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()