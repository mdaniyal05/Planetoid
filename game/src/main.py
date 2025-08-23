import pygame
from constants import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2


def main():
    running = True
    dt = 0
    player = Player(x, y)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

        player.update(dt)

    pygame.quit()


if __name__ == "__main__":
    main()
