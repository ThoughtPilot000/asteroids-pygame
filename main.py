import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    log_state()
    screen.fill("black")

    #always last called
    pygame.display.flip()

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
