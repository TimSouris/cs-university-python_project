from dis import Instruction
from platform import python_branch
from turtle import Screen, color
from ctypes.wintypes import RGB
from tkinter import CENTER
import main
import pygame
import sys
from constants import *
from constants import HEIGHT, WIDTH


pygame.init()
screen=pygame.display.set_mode(WINDOW_SIZE)
base_font = pygame.font.Font(None, 45)
base_font2= pygame.font.Font(None, 20)
titre='Jeu de Dames !'
ordre='Entre ton adresse réseau local pour jouer avec un ami (si tu en as)'
user_text=''
input_rect = pygame.Rect(150,200,100,32)
color=pygame.Color('blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text=user_text[:-1]
            elif event.key == pygame.K_KP_ENTER:
                print(user_text)
            else:
                user_text+=event.unicode
    
    screen.fill((0,0,0))
    #Titre
    text_titre=base_font.render(titre,True,BLUE)
    screen.blit(text_titre,(150,70))
    #consigne d'entrer l'IP
    text_ordre=base_font2.render(ordre,True,BLUE)
    screen.blit(text_ordre,(50,150))
    #champ de saisie
    pygame.draw.rect(screen,color,input_rect)
    text_surface=base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surface,(input_rect.x +5,input_rect.y+5))
    #pour redimensionner le champ de saisie
    input_rect.w=max(200,text_surface.get_width()+10)
    pygame.display.flip()
    CLOCK.tick(60)