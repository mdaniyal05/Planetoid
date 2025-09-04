import pygame
from circle_shape import Circle_Shape


class Planet(Circle_Shape):
    containers = ()

    def __init__(self, x, y, radius):
        Circle_Shape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
