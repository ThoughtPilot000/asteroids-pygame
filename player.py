import pygame

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH,TURN_SPEED, PLAYER_MAX_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_ACC

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_shot = 0
        self.current_speed = 0
        self.laser_type = "red"
        self.weapon_key_pressed = False

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        weapon_key_pressed = False

        if keys[pygame.K_a]:
            self.rotate(float("-" + str(dt)))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
            if self.current_speed < PLAYER_MAX_SPEED:
                self.current_speed += PLAYER_ACC * dt
        if keys[pygame.K_s]:
            self.move(float("-" + str(dt)))
            if self.current_speed < PLAYER_MAX_SPEED:
                self.current_speed += PLAYER_ACC * dt
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_f] and not self.weapon_key_pressed:
            self.weapon_key_pressed = True
            if self.laser_type == "red":
                self.laser_type = "yellow"
            else:
                self.laser_type = "red"
        if not keys[pygame.K_f]:
            self.weapon_key_pressed = False
        

        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            if self.current_speed > 0:
                self.current_speed -= PLAYER_ACC * dt 

        self.cooldown_shot -= dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * self.current_speed * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.cooldown_shot < 0:
            if self.laser_type == "yellow":
                shot = Shot(self.position.x, self.position.y, SHOT_RADIUS * 3, self.laser_type, self.rotation - 90)
            elif self.laser_type == "red":
                shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.laser_type, self.rotation)
            else:
                raise Exception("Unknown laser type")
            shot.velocity = pygame.Vector2(0, 1)
            shot.velocity = shot.velocity.rotate(self.rotation) 
            shot.velocity *= PLAYER_SHOOT_SPEED
            self.cooldown_shot = PLAYER_SHOOT_COOLDOWN_SECONDS