from vector2 import vector2
from pygame

class tile:
    def __init__(self, posx,posy,width,height):
        self.position = vector2(posx,posy)
        self.size = vector2(width,height)
        self.tiledirections = None

    # Pass in the tiles for the directions.
    def setupDirections(self,up,right,down,left):
        self.tiledirections = tiledirections(up,right,down,left)

    # Add drawing functionality here using Pygame.
    def draw(self):
        pass

# Used to store the adj. tiles.
class tiledirections:
    def __init__(self,up,right,down,left):
        self.up = up
        self.right = right
        self.down = down
        self.left = left
