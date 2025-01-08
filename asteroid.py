import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            pygame.Color(255, 255, 255),
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)

            a1 = Asteroid(self.position.x, self.position.y, radius)
            a1.velocity = vector1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, radius)
            a2.velocity = vector2 * 1.2