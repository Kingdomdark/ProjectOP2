from .Vector2 import vector2
from .AudioVisualManager import spritemanager
import pygame

class player:
    def __init__(self, screen, name, color):
        self.screen = screen
        self.name = name
        self.color = color
        self.size = vector2(12,12)
        self.sm = spritemanager()

        self.turns = 0
        self.qcorrect = 0

        self.direction = None
        self.movesleft = None
        self.qtype = None

        self.prevtile = None # Used to go back to once the person answers the question incorrectly
        self.currenttile = None
        self.tiledestination = None

    def resetturn(self):
        self.turns += 1
        self.direction = None
        self.qtype = None
        self.movesleft = None
        self.prevtile = None
        self.tiledestination = None

    def move(self,direction):
        if direction is "left" and self.currenttile.tiledir.left is not None:
            self.currenttile =  self.currenttile.tiledir.left
        elif direction is "up" and self.currenttile.tiledir.up is not None:
            self.currenttile = self.currenttile.tiledir.up
        elif direction is "right" and self.currenttile.tiledir.right is not None:
            self.currenttile = self.currenttile.tiledir.right
        elif direction is "down" and self.currenttile.tiledir.down is not None:
            self.currenttile = self.currenttile.tiledir.down


    def draw(self):
        if self.currenttile is not None:
            pygame.draw.rect(self.screen, self.color, (self.currenttile.pos.x - 1,  self.currenttile.pos.y, self.size.x, self.size.y))
            pygame.draw.rect(self.screen, self.sm.getcolor("black"), (self.currenttile.pos.x -1, self.currenttile.pos.y, self.size.x, self.size.y),1 )
