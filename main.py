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
    
    score = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    text_font = pygame.font.SysFont("Arial", 30)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    deltaclock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        updatable.update(dt)

        #collision checks
        for i in asteroids:
            if i.collide_with(player):
                log_event("player_hit")

                print("Game over!")
                print(f"Your score was {score}!")
                sys.exit()

        for asteroid_object in asteroids:
            for x in shots:
                if x.collide_with(asteroid_object):
                    log_event("asteroid_shot")
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

        draw_text("Score: " + str(score), text_font, "white", SCREEN_WIDTH / 2 - 65 , SCREEN_HEIGHT - (SCREEN_HEIGHT - 70), screen)

        #always last called
        pygame.display.flip()
        dt = deltaclock.tick(60) / 1000


if __name__ == "__main__":
    main()
