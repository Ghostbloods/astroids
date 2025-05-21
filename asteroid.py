import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        # Draw the asteroid on the screen
        # using its position and radius
    def update(self, dt): 
        self.position += self.velocity * dt


    