from vector2 import vector2
import pygame

class tile:
    def __init__(self,posx,posy,width,height,category):
        self.position = vector2(posx,posy)
        self.size = vector2(width,height)
        self.tiledirections = None
        self.category = category

    # Pass in the tiles for the directions.
    def setupDirections(self,up,right,down,left):
        self.tiledirections = tiledirections(up,right,down,left)

    # Add drawing functionality here using Pygame.
    def draw(self):
        pass

    def update(self):
        pass

# Used to store the adj. tiles.
class tiledirections:
    def __init__(self,up,right,down,left):
        self.up = up
        self.right = right
        self.down = down
        self.left = left
