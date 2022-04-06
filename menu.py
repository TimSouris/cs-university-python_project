# Importation des libraires et autres classes
import pygame
import main
import Board
import Pawns

# Initilalisation de la fenêtre
pygame.init()
screen=pygame.display.set_mode()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()

def main(): 
    return