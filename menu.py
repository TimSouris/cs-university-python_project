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
base_font = pygame.font.Font(None, 32)
user_text=''

input_rect = pygame.Rect(200,200,140,32)
color=pygame.Color('blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text=user_text[:-1]
            else:
                user_text+=event.unicode
    screen.fill((0,0,0))
    pygame.draw.rect(screen,color,input_rect)
    text_surface=base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surface,(input_rect.x +5,input_rect.y+5))
    input_rect.w=max(100,text_surface.get_width()+10)
    pygame.display.flip()
    clock.tick(60)