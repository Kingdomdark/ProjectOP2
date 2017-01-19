import pygame
import sys

class menumanager:
    def __init__(self ,screen):
        self.screen = screen

    def drawbuttons(self , screen):

        # images button
        bt_start = pygame.image.load("images/start-bt.png")
        bt_high  = pygame.image.load("images/highscore-bt.png")
        bt_exit  = pygame.image.load("images/exit-bt.jpg")

        #print on screen
        start = self.screen.blit(bt_start, (350 ,100))
        high  = self.screen.blit(bt_high, (310, 250))
        exit  = self.screen.blit(bt_exit, (350, 470))

        # add button handlers
        self.buttonClick(start,high,exit)

    def buttonClick(self, start,high,exit):

            #mouse buttons
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    pos = pygame.mouse.get_pos()
                    # start button is pressed > Open Game
                    if start.collidepoint(pos):
                        print ("Start button is pressed")
                    # Highscore button is pressed > Open Highscore
                    elif high.collidepoint(pos):
                        print("highscore button is pressed")
                    # Exit button is pressed > Open Game
                    elif exit.collidepoint(pos):
                           pygame.quit();
                           sys.exit();
                    # exit game
                    elif e.type == pygame.QUIT:
                            pygame.quit();
                            sys.exit();






