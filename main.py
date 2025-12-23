import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot
from drawtext import draw_text

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    score = 0
    dt = 0

    pygame.init()

    dock_1 = pygame.image.load("assets/small_laser_equ.png")
    dock_2 = pygame.image.load("assets/big_laser_equ.png")
    dock_1 = pygame.transform.scale(dock_1, (200, 100))
    dock_2 = pygame.transform.scale(dock_2, (200, 100))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    docks = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    text_font = pygame.font.SysFont("Firacode", 30)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    deltaclock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    def initialize():
        nonlocal score, dt
        score = 0
        dt = 0
        for i in asteroids:
            i.kill()

        player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    initialize()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game over!")
                print(f"Your score was {score}!")
                return 

        updatable.update(dt)

        #collision checks
        for i in asteroids:
            if i.collide_with(player):
                log_event("player_hit")

                print("Game over!")
                print(f"Your score was {score}!")
                initialize()

        for asteroid_object in asteroids:
            for x in shots:
                if x.collide_with(asteroid_object):
                    log_event("asteroid_shot")
                    if not x.type == "yellow":
                        x.kill()
                    asteroid_object.split()

                    if asteroid_object.golden:
                        score += asteroid_object.radius * 3
                    else:
                        score += asteroid_object.radius
        
        #rendering
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        if player.laser_type == "red":
            screen.blit(dock_1, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 250))
        elif player.laser_type == "yellow":
            screen.blit(dock_2, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 250))
        else:
            raise Exception("Unknown laser type")

        
        draw_text("Score: " + str(score), text_font, "white", SCREEN_WIDTH / 2 - 65 , SCREEN_HEIGHT - (SCREEN_HEIGHT - 50), screen)

        #always last called
        pygame.display.flip()
        dt = deltaclock.tick(60) / 1000


if __name__ == "__main__":
    main()
