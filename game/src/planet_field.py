import pygame
import random
from planet import Planet
from constants import *


class Planet_Field(pygame.sprite.Sprite):
    containers = ()

    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-PLANET_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + PLANET_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -PLANET_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + PLANET_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        planet = Planet(position.x, position.y, radius)
        planet.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > PLANET_SPAWN_RATE:
            self.spawn_timer = 0

            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, PLANET_KINDS)
            self.spawn(PLANET_MIN_RADIUS * kind, position, velocity)
