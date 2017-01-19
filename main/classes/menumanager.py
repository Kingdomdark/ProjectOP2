import pygame
import sys
from classes.gamemanager import  gamemanager
class menumanager:
    def __init__(self ,screen):
        self.screen = screen

    def drawbuttons(self , screen):

        # images button
        bt_start = pygame.image.load("images/start-bt.png")
        bt_high  = pygame.image.load("images/highscore-bt.png")
        bt_exit  = pygame.image.load("images/exit-bt.jpg")
        bt_inst  = pygame.image.load("images/instr-bt.png")

        #print on screen
        start = self.screen.blit(bt_start, (350 ,0))
        high  = self.screen.blit(bt_high, (310, 80))
        instr = self.screen.blit(bt_inst, (350, 300))
        exit  = self.screen.blit(bt_exit, (350, 500))


        # add button handlers
        self.buttonClick(start,high,instr , exit)

    def buttonClick(self, start,high,instr , exit):
            gm = gamemanager()
            page = ""
            #mouse buttons
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    pos = pygame.mouse.get_pos()
                    # start button is pressed > Open Game
                    if start.collidepoint(pos):
                         page = "start"
                    # Highscore button is pressed > Open Highscore
                    elif high.collidepoint(pos):
                        page = "highscore"
                    elif instr.collidepoint(pos):
                        page = "instructions"
                    # Exit button is pressed > Exit game
                    elif exit.collidepoint(pos):
                           pygame.quit();
                           sys.exit();
                    print (page)







