import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0  # Initialize delta time
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 

        screen.fill("black")  # Fill the screen with black
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000.0  # Calculate delta time

if __name__ == "__main__":
    main()
