import pygame
import random
from circle_shape import Circle_Shape
from constants import PLANET_MIN_RADIUS


class Planet(Circle_Shape):
    containers = ()

    def __init__(self, x, y, radius):
        Circle_Shape.__init__(self, x, y, radius)

    def split(self):
        old_radius = self.radius

        self.kill()

        if self.radius <= PLANET_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_planet_one_vector = self.velocity.rotate(random_angle)
        new_planet_two_vector = self.velocity.rotate(-random_angle)

        new_planet_one_radius = old_radius - PLANET_MIN_RADIUS
        new_planet_two_radius = old_radius - PLANET_MIN_RADIUS

        new_planet_one = Planet(
            self.position.x, self.position.y, new_planet_one_radius)
        new_planet_two = Planet(
            self.position.x, self.position.y, new_planet_two_radius)

        new_planet_one.velocity = new_planet_one_vector * 1.2
        new_planet_two.velocity = new_planet_two_vector * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 5)

    def update(self, dt):
        self.position += self.velocity * dt
