import pygame
import random

from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MIN_RADIUS

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(1,360)
            first_vector = self.velocity.rotate(rand_angle)
            second_vector = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_1 = Asteroids(self.position[0], self.position[1], new_radius)
            new_2 = Asteroids(self.position[0], self.position[1], new_radius)

            new_1.velocity = first_vector * 1.2
            new_2.velocity = second_vector * 1.2
    
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt