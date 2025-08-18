import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
