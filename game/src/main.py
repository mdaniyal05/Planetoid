import pygame
import time
from constants import *
from player import Player
from planet import Planet
from planet_field import Planet_Field

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

text_font = pygame.font.SysFont("monospace", 30, bold=True)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
planets = pygame.sprite.Group()


def draw_text(text, font, color, x, y):
    msg = font.render(text, True, color)

    textRect = msg.get_rect()
    textRect.center = (x, y)

    screen.blit(msg, textRect)


def main():
    running = True
    dt = 0

    Player.containers = (updatable, drawable)
    Planet.containers = (planets, updatable, drawable)
    Planet_Field.containers = (updatable)

    player = Player(x, y)
    Planet_Field()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        dt = clock.tick(FPS) / 1000

        updatable.update(dt)

        for planet in planets:
            check = player.check_collision(planet)

            if check:
                draw_text("GAME OVER!", text_font, (250, 250, 250), x, y)
                pygame.display.update()
                time.sleep(3)
                running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
