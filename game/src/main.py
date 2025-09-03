import pygame
from constants import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()


def main():
    running = True
    dt = 0

    Player.containers = (updatable, drawable)
    Player(x, y)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

        updatable.update(dt)

    pygame.quit()


if __name__ == "__main__":
    main()
