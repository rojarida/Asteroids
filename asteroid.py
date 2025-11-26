import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first = pygame.math.Vector2.rotate(self.velocity, angle)
        second = pygame.math.Vector2.rotate(self.velocity, -angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_split = Asteroid(self.position.x, self.position.y, new_radius)
        second_split = Asteroid(self.position.x, self.position.y, new_radius)

        first_split.velocity = first * 1.2
        second_split.velocity = second * 1.2
