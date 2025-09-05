import pygame
from circle_shape import Circle_Shape


class Bullet(Circle_Shape):
    containers = ()

    def __init__(self, x, y, radius):
        Circle_Shape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 3)

    def update(self, dt):
        self.position += self.velocity * dt
