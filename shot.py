import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Shot(CircleShape):

    def __init__(self, x,y,radius, type):
        super().__init__(x,y,radius)
        self.type = type
        self.rotation = 0

    def rectangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius * 10 / 3) / 1.5

        a = self.position + forward * self.radius + right
        b = self.position + forward * self.radius - right
        c = self.position - forward * self.radius - right
        d = self.position - forward * self.radius + right

        return [a, b, c, d]

    def draw(self, surface):
        if self.type == "red":
            pygame.draw.circle(surface, "red", self.position, self.radius, LINE_WIDTH)
        elif self.type == "yellow":
            pygame.draw.polygon(surface, "yellow", self.rectangle(), LINE_WIDTH)
        else:
            raise Exception("Unknown laser type")

    def update(self, dt):
        self.position += self.velocity * dt