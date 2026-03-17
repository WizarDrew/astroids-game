import pygame
from constants import *
from player import Player
from logger import log_state

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    clock = pygame.time.Clock()
    dt = 0


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        updatable.update(dt)
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

