import pygame

def draw_text(text:str, font, color,x,y,screen):
    text2render = font.render(text, True, color)
    screen.blit(text2render, (x, y))