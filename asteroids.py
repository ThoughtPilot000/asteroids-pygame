import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, surface, x , y, radius):
        pygame.draw.circle(surface, "white", x, y, radius, LINE_WIDTH)

    def update(self, dt):
        pass
        #to do