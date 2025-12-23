import pygame

def draw_text(text, font, color,x,y,screen):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))