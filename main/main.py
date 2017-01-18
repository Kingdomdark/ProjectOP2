import math
import pygame

class Game:
    def __init__(self):
        # Resolution
        width = 1000
        height = 700
        size = (width,height)

        # Start Pygame
        pygame.init()

        # Set the Resolution
        self.screen = pygame.display.set_mode(size)
        # Set window title
        pygame.display.set_caption("ProjectOP2","ProjectOP2")

    # Update everything
    # NOTE / TODO : To keep things tidy, create managers for handling
    def update(self):
        pass

    # Draw everything
    # NOTE / TODO : To keep things tidy, create managers for handling
    def draw(self):
        #Clear the screen
        self.screen.fill((0,0,0))

        #---- BEGIN DRAW LOGIC ----


        #----- END DRAW LOGIC -----

        #Flip screen
        pygame.display.flip()

    def gameloop(self):
        # TODO : This is the incorrect way of handling events,
        # but it's currently allowed since the only event at the moment
        # is the 'Quit' events. Should we manage multiple events, we
        # need to fix process_events. - Jordan
        while not process_events():
            self.update()
            self.draw()


# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit the game.
            return True
    return False

# Main program logic
def program():
    game = Game()
    game.gameloop()

program()
