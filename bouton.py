from constants import BLACK, HEIGHT, WHITE, WIDTH
import pygame
from pygame.locals import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class button():

    #colours for button and text
    button_col = (20, 70, 100)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = BLACK
    width = 180
    height = 70

    def init(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        #add shading to button
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        #add text to button
        text_img = pygame.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action
