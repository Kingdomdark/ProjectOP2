import tile

class tilemanager:
    def __init__(self):
        self.size = vector2(25,25)
        self.sides = []

#--------------------------------------------------------------------------
# Adding sides
#--------------------------------------------------------------------------
        self.sides.append(side(0,0))

        #shortcodes
        tl1 = self.sides[0].tiles
#--------------------------------------------------------------------------
# Adding tiles
#--------------------------------------------------------------------------
        # First row [0 t/m ...]
        self.sides[0].tiles.append(tile(0,0,self.size.x,self.size.y))
        self.sides[0].tiles.append(tile(0,0,self.size.x,self.size.y))

#--------------------------------------------------------------------------
# Linking the tiles
#--------------------------------------------------------------------------
        # First row [0 t/m ...]
        self.sides[0].tiles[0].setupDirections(None, None, None, None)
        self.sides[0].tiles[1].setupDirections(self.sides[0].tiles[0],None,None,None)
#--------------------------------------------------------------------------
# Invoking functionality
#--------------------------------------------------------------------------
    def draw(self):
        # For every tile in tiles, draw the tile.
        for t in tiles:
            t.draw()

    def update(self):
        # For every tile in tiles, update the tile.
        for t in tiles:
            t.update()

class side:
    def __init__(self,boardimage,x,y):
        self.tiles = []
