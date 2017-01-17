from vector2 import vector2

class tile:
    def __init__(self, posx,posy,width,height):
        self.position = vector2(posx,posy)
        self.size = vector2(width,height)
