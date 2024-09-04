import pygame
import constants

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()

        #set framerate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
