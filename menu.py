# Importation des libraires et autres classes
from tkinter import CENTER
import main
import pygame
import sys
from constants import *
from constants import HEIGHT, WIDTH

# Initilalisation de la fenêtre
pygame.init() 
res = (HEIGHT,WIDTH) 
screen = pygame.display.set_mode(res)  
smallfont = pygame.font.SysFont('Corbel',35) 
text = smallfont.render('Adresse IP locale :', True, BLUE)
while True: 
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                pygame.quit()
    mouse = pygame.mouse.get_pos()
    if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
        pygame.draw.rect(screen,WHITE,[WIDTH,HEIGHT,400,1000])
    else:
        pygame.draw.rect(screen,BLUE,[WIDTH,HEIGHT,400,1000])
    screen.blit(text,(WIDTH/2-100,HEIGHT/2-50))
    pygame.display.update()