import pygame

class gamemanager:
    def __init__(self,screen,contentmanager,questionmanager,tilemanager):
        self.cm = contentmanager
        self.qm = questionmanager
        self.tm = tilemanager

        self.screen = screen

        self.background =  self.cm.sm.getimage("background_game")


    def draw(self):
        self.screen.blit(self.background,(0,0))

        # Draw the tiles from the tile manager.
        self.tm.draw()
        pass

    def update(self):
        pass
