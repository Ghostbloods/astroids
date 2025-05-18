import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0  # Initialize delta time
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    # Instantiate player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 

        screen.fill("black")  # Fill the screen with black
        player.draw(screen) # Draw the player
        pygame.display.flip()  # Update the display
        

        dt = clock.tick(60) / 1000.0  # Calculate delta time

        


if __name__ == "__main__":
    main()
