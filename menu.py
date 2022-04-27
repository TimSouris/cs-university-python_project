# Importation des libraires et autres classes
from ctypes.wintypes import RGB
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
input_rect = pygame.Rect(200, 250, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active=False
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
    pygame.draw.rect(screen, color, input_rect)
    text_surface = smallfont.render('', True, (255,255,255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+200))
    input_rect.w = max(100, text_surface.get_width()+10)
    screen.blit(text,(WIDTH/2-100,HEIGHT/2-50))
    pygame.display.flip()
    pygame.display.update()