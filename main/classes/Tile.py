from .Vector2 import vector2
import pygame

class tile:
    def __init__(self, screen, parent, posx, posy, width, height, category, startpos=None):
        if startpos == None:
            startpos = False
        self.startpos = startpos

        self.screen = screen
        self.parent = parent
        self.pos = vector2(self.parent.pos.x + posx, self.parent.pos.y + posy)
        self.size = vector2(width, height)
        self.tiledir = None
        self.category = category

    # Pass in the tiles for the directions.
    def setupDirections(self,up,right,down,left):
        self.tiledir = tiledir(up,right,down,left)

    # Add drawing functionality here using Pygame.
    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),(self.pos.x, self.pos.y, self.size.x, self.size.y))
        pygame.draw.rect(self.screen,(0,0,0),(self.pos.x, self.pos.y, self.size.x, self.size.y), 1)


    def update(self):
        pass

# Used to store the adj. tiles.
class tiledir:
    def __init__(self,left,up,right,down):
        self.left = left
        self.up = up
        self.right = right
        self.down = down
