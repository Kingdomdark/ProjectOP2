import tile

class tilemanager:
    def __init__(self):
        self.tiles = [] # Tile Array to store the tiles in.

#------------------------------------------------------------------
# Adding tiles
#------------------------------------------------------------------
        # First row [0 t/m ...]
        self.tiles.append(tile(0,0,50,50))
        self.tiles.append(tile(0,0,50,50))
#------------------------------------------------------------------
# Linking the tiles
#------------------------------------------------------------------
        # First row [0 t/m ...]
        self.tiles[0].setupDirections(None, None, None, None)
        self.tiles[1].setupDirections(self.tiles[0],None,None,None)

    def draw(self):
        # For every tile in tiles, draw the tile.
        for t in tiles:
            t.draw()
