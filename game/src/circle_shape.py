import pygame


class Circle_Shape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, obj):
        distance = self.position.distance_to(obj.position)
        collision_point = self.radius + obj.radius

        if distance <= collision_point:
            return True
        else:
            return False

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
