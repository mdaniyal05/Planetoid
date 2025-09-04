import pygame
from constants import *
from player import Player
from planet import Planet
from planet_field import Planet_Field

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
planets = pygame.sprite.Group()


def main():
    running = True
    dt = 0

    Player.containers = (updatable, drawable)
    Planet.containers = (planets, updatable, drawable)
    Planet_Field.containers = (updatable)

    Player(x, y)
    Planet_Field()

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
