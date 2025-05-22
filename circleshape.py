import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y) # position of the object
        self.velocity = pygame.Vector2(0, 0) # velocity of the object
        self.radius = radius # radius of the object

    def draw(self, screen):
        # sub-classes must override
        _ = screen
        pass
        

    def update(self, dt):
        # sub-classes must override
        _ = dt
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius