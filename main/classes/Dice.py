import pygame
from random import randint




class Dice():
    def roll(self):
        #Define the dice roll
        dice_roll = randint(0,6)
        return dice_roll
    
    def drawdice(self):
        #Images of the eyes of the dice
        eyes1 = pygame.image.load ("images/1.png")
        eyes2 = pygame.image.load ("images/2.png")
        eyes3 = pygame.image.load ("images/3.png")
        eyes4 = pygame.image.load ("images/4.png")
        eyes5 = pygame.image.load ("images/5.png")
        eyes6 = pygame.image.load ("images/6.png")


        #Draw the dice on the screen
        if Dice.roll() == 1:
            self.screen.blit (eyes1,(350,0))
        elif Dice.roll() == 2:
            self.screen.blit (eyes2,(350,0))
        elif Dice.roll == 3:
            self.screen.blit (eyes3,(350,0))
        elif Dice.roll() == 4:
            self.screen.blit (eyes4,(350,0))
        elif Dice.roll() == 5:
            self.screen.blit (eyes5,(350,0))
        elif Dice.roll() == 6:
            self.screen.blit (eyes6,(350,0))
