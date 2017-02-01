from classes.MenuManager import menumanager
from classes.ContentManager import contentmanager
import math
import pygame
import sys

class Main:
    def __init__(self):
        # Resolution
        self.width = 1000
        self.height = 700
        self.size = (self.width,self.height)

        # Start Pygame
        pygame.init()

        # Set the Resolution
        self.screen = pygame.display.set_mode(self.size)

        # managers
        self.cm = contentmanager(self.screen)

        # Mouse position
        self.pos = pygame.mouse.get_pos()

        # pass events
        self.events = pygame.event.get()

        # Set window title
        pygame.display.set_caption("Euromast Game","Euromast Game")

    # Update everything
    # NOTE / TODO : To keep things tidy, create managers for handling
    def update(self):
        self.cm.update()


    # Draw everything
    # NOTE / TODO : To keep things tidy, create managers for handling
    def draw(self):
        #Clear the screen
        self.screen.fill((0 , 0 , 0 ))

        #---- BEGIN DRAW LOGIC ----
        self.cm.draw()


        #----- END DRAW LOGIC -----

        #Flip screen
        pygame.display.flip()

    def gameloop(self):
        # TODO : This is the incorrect way of handling events,
        # but it's currently allowed since the only event at the moment
        # is the 'Quit' events. Should we manage multiple events, we
        # need to fix process_events. - Jordan
        while True:
            self.process_events()
            self.update()
            self.draw()


    # Handle pygame events
    def process_events(self):
        self.pos = pygame.mouse.get_pos()
        self.events = pygame.event.get()
        if self.cm.gm.popupo is not None:
            if not self.cm.gm.paused:
                self.cm.gm.popupo.answer.update(self.events)
        if self.cm.gm.endgamepopup is not None:
            self.cm.gm.endgamepopup.answer.update(self.events)
        for event in self.events:
            # Quit game
            if event.type == pygame.QUIT:
                pygame.quit()

            # Main Menu Handling
            if self.cm.stage == 0:
                # Mouse hover handling
                self.cm.mm.bhoverhandling(self.pos)
                # Mouse button down handling
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #If on menu, check for menu events @ Buttons.
                    self.cm.mm.bclickhandling(self.pos)
                    if self.cm.mm.ipopup is not None:
                        self.cm.mm.ipopup.bclickhandling()

            # Game stuff
            elif self.cm.stage == 1:
                self.cm.gm.bhoverhandling(self.pos)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.cm.gm.bclickhandling(self.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.cm.gm.paused = not self.cm.gm.paused






# Main program logic
def program():
    game = Main()
    game.gameloop()

program()
