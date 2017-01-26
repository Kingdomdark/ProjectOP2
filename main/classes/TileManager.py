from .Tile import tile
from .Vector2 import vector2

class tilemanager:
    def __init__(self,screen,spritemanager):
        self.screen = screen
        self.sm = spritemanager
        self.size = vector2(10,10)
        self.sides = []

#--------------------------------------------------------------------------
# Adding sides
#--------------------------------------------------------------------------
        self.sides.append(side(self.screen, self.sm.getimage("board1"), 10, 20))
        self.sides.append(side(self.screen, self.sm.getimage("board2"), 300, 20))

        #shortcodes
        tl1 = self.sides[0].tiles
#--------------------------------------------------------------------------
# Adding tiles (Bottom to up)
#--------------------------------------------------------------------------
        # Really need to sort out an algo, but can't make up of one atm due to tiredness.

        # Positional Vars
        # Row
        # Bottom
        self.bx1 = 100
        self.bx2 = 125
        self.bx3 = 152
        self.bx4 = 177

        # Columns
        self.vertspacing = 25

        # Bottom section
        self.by1 = 610
        self.by2 = self.by1 - self.vertspacing
        self.by3 = self.by2 - self.vertspacing
        self.by4 = self.by3 - self.vertspacing
        self.by5 = self.by4 - self.vertspacing
        self.by6 = self.by5 - self.vertspacing
        self.by7 = self.by6 - self.vertspacing
        self.by8 = self.by7 - self.vertspacing
        self.by9 = self.by8 - self.vertspacing
        self.by10 = self.by9 - self.vertspacing

#--------------------------------------------------------BOTTOM SECTION--------------------------------------------------------------------------------
        # 1st row [0 t/m 3] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by1, self.size.x, self.size.y, "Random Testing Ooga Booga")) # 0
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by1, self.size.x, self.size.y, None)) # 1
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by1, self.size.x, self.size.y, None)) # 2
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by1, self.size.x, self.size.y, None)) # 3
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by1, self.size.x, self.size.y, None)) # 0
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by1, self.size.x, self.size.y, None)) # 1
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by1, self.size.x, self.size.y, None)) # 2
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by1, self.size.x, self.size.y, None)) # 3

        # 2nd row [4 t/m 7] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by2, self.size.x, self.size.y, None)) # 4
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by2, self.size.x, self.size.y, None)) # 5
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by2, self.size.x, self.size.y, None)) # 6
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by2, self.size.x, self.size.y, None)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by2, self.size.x, self.size.y, None)) # 4
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by2, self.size.x, self.size.y, None)) # 5
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by2, self.size.x, self.size.y, None)) # 6
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by2, self.size.x, self.size.y, None)) # 7

        # 3rd row [8 t/m 11] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by3, self.size.x, self.size.y, None)) # 8
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by3, self.size.x, self.size.y, None)) # 9
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by3, self.size.x, self.size.y, None)) # 10
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by3, self.size.x, self.size.y, None)) # 11
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by3, self.size.x, self.size.y, None)) # 8
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by3, self.size.x, self.size.y, None)) # 9
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by3, self.size.x, self.size.y, None)) # 10
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by3, self.size.x, self.size.y, None)) # 11

        # 4th row [12 t/m 15] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by4, self.size.x, self.size.y, None)) # 12
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by4, self.size.x, self.size.y, None)) # 13
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by4, self.size.x, self.size.y, None)) # 14
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by4, self.size.x, self.size.y, None)) # 15
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by4, self.size.x, self.size.y, None)) # 12
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by4, self.size.x, self.size.y, None)) # 13
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by4, self.size.x, self.size.y, None)) # 14
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by4, self.size.x, self.size.y, None)) # 15

        # 5th row [16 t/m 19] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by5, self.size.x, self.size.y, None)) # 16
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by5, self.size.x, self.size.y, None)) # 17
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by5, self.size.x, self.size.y, None)) # 18
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by5, self.size.x, self.size.y, None)) # 19
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by5, self.size.x, self.size.y, None)) # 16
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by5, self.size.x, self.size.y, None)) # 17
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by5, self.size.x, self.size.y, None)) # 18
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by5, self.size.x, self.size.y, None)) # 19

        # 6th row [20 t/m 23] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by6, self.size.x, self.size.y, None)) # 20
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by6, self.size.x, self.size.y, None)) # 21
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by6, self.size.x, self.size.y, None)) # 22
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by6, self.size.x, self.size.y, None)) # 23
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by6, self.size.x, self.size.y, None)) # 20
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by6, self.size.x, self.size.y, None)) # 21
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by6, self.size.x, self.size.y, None)) # 22
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by6, self.size.x, self.size.y, None)) # 23

        # 7th row [24 t/m 27] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by7, self.size.x, self.size.y, None)) # 24
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by7, self.size.x, self.size.y, None)) # 25
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by7, self.size.x, self.size.y, None)) # 26
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by7, self.size.x, self.size.y, None)) # 27
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by7, self.size.x, self.size.y, None)) # 24
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by7, self.size.x, self.size.y, None)) # 25
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by7, self.size.x, self.size.y, None)) # 26
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by7, self.size.x, self.size.y, None)) # 27

        # 8th row [28 t/m 31] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by8, self.size.x, self.size.y, None)) # 28
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by8, self.size.x, self.size.y, None)) # 29
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by8, self.size.x, self.size.y, None)) # 30
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by8, self.size.x, self.size.y, None)) # 31
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by8, self.size.x, self.size.y, None)) # 28
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by8, self.size.x, self.size.y, None)) # 29
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by8, self.size.x, self.size.y, None)) # 30
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by8, self.size.x, self.size.y, None)) # 31

        # 9th row [32 t/m 35] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by9, self.size.x, self.size.y, None)) # 32
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by9, self.size.x, self.size.y, None)) # 33
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by9, self.size.x, self.size.y, None)) # 34
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by9, self.size.x, self.size.y, None)) # 35
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by9, self.size.x, self.size.y, None)) # 32
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by9, self.size.x, self.size.y, None)) # 33
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by9, self.size.x, self.size.y, None)) # 34
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by9, self.size.x, self.size.y, None)) # 35

        # 10th row [36 t/m 39] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by10, self.size.x, self.size.y, None)) # 36
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by10, self.size.x, self.size.y, None)) # 37
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by10, self.size.x, self.size.y, None)) # 38
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by10, self.size.x, self.size.y, None)) # 39
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by10, self.size.x, self.size.y, None)) # 36
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by10, self.size.x, self.size.y, None)) # 37
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by10, self.size.x, self.size.y, None)) # 38
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by10, self.size.x, self.size.y, None)) # 39





#--------------------------------------------------------------------------
# Linking the tiles (Bottom to up)
#--------------------------------------------------------------------------
        # NOTE: I seriously need to make an algorithm for this anytime soon, doubt it will be done before the
        # end of the project. So, need to be done manually for the time being.  - Jordan

        # left, up, right, down
        # First row [0 t/m 3] (Side 1 & 2)
        self.sides[0].tiles[0].setupDirections(self.gettile(1,3), self.gettile(0,4), self.gettile(0,1), None) # 0
        self.sides[0].tiles[1].setupDirections(self.gettile(0,0), self.gettile(0,5), self.gettile(0,2), None) # 1
        self.sides[0].tiles[2].setupDirections(self.gettile(0,1), self.gettile(0,6), self.gettile(0,3), None) # 2
        self.sides[0].tiles[3].setupDirections(self.gettile(0,2), self.gettile(0,7), self.gettile(1,0), None) # 2
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[0].setupDirections(self.gettile(0,3), self.gettile(1,4), self.gettile(1,1), None) # 0
        self.sides[1].tiles[1].setupDirections(self.gettile(1,0), self.gettile(1,5), self.gettile(1,2), None) # 1
        self.sides[1].tiles[2].setupDirections(self.gettile(1,1), self.gettile(1,6), self.gettile(1,3), None) # 2
        self.sides[1].tiles[3].setupDirections(self.gettile(1,2), self.gettile(1,7), self.gettile(0,0), None) # 3
#--------------------------------------------------------------------------
# Invoking functionality
#--------------------------------------------------------------------------

        print(self.sides[0].tiles[1].tiledir.left.category)

    def gettile(self,sidenr,tilenr):
        try:
            return self.sides[sidenr].tiles[tilenr]
        except:
            print("TManager : Couldn't return sides[%i].tiles[%i] ." % (sidenr,tilenr))

    def draw(self):
        # For every tile in tiles, draw the tile.
        for s in self.sides:
            s.draw()
            for t in s.tiles:
                t.draw()

    def update(self):
        # For every tile in tiles, update the tile.
        for t in tiles:
            t.update()

class side:
    def __init__(self,screen,image,x,y):
        self.screen = screen
        self.image = image
        self.pos = vector2(x,y)
        self.tiles = []

    def draw(self):
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
