# Importation des libraires et autres classes
import main
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
    screen.fill((20,102,200))
    pygame.draw.rect(screen,BLUE,(30,250,440,100))
    main.window_update(screen,(20,102,200),CLOCK,False)
pygame.quit()