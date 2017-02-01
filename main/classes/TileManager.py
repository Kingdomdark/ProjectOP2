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

        #Top
        self.bx5 = 110
        self.bx6 = 145

        # Peak
        self.bx7 = 126

        # Columns
        self.vertspacing = 25
        self.topmultiplier = 1.4

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

        # Top section
        self.by11 = self.by10 - self.vertspacing - 115
        self.by12 = self.by11 - (self.vertspacing * self.topmultiplier)
        self.by13 = self.by12 - (self.vertspacing * self.topmultiplier)
        self.by14 = self.by13 - (self.vertspacing * self.topmultiplier)
        self.by15 = self.by14 - (self.vertspacing * self.topmultiplier)

        # Peak
        self.by16 = self.by15 - (self.vertspacing * self.topmultiplier) - 75

#--------------------------------------------------------BOTTOM SECTION--------------------------------------------------------------------------------
        # 1st row [0 t/m 3] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by1, self.size.x, self.size.y, "History")) # 0
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by1, self.size.x, self.size.y, "History")) # 1
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by1, self.size.x, self.size.y, "Geography")) # 2
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by1, self.size.x, self.size.y, "Geography")) # 3
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by1, self.size.x, self.size.y, "Entertainment")) # 0
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by1, self.size.x, self.size.y, "Entertainment")) # 1
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by1, self.size.x, self.size.y, "Sports")) # 2
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by1, self.size.x, self.size.y, "Sports")) # 3

        # 2nd row [4 t/m 7] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by2, self.size.x, self.size.y, "History")) # 4
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by2, self.size.x, self.size.y, "History")) # 5
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by2, self.size.x, self.size.y, "Geography")) # 6
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by2, self.size.x, self.size.y, "Geography")) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by2, self.size.x, self.size.y, "Entertainment")) # 4
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by2, self.size.x, self.size.y, "Entertainment")) # 5
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by2, self.size.x, self.size.y, "Sports")) # 6
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by2, self.size.x, self.size.y, "Sports")) # 7

        # 3rd row [8 t/m 11] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by3, self.size.x, self.size.y, "History")) # 8
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by3, self.size.x, self.size.y, "History")) # 9
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by3, self.size.x, self.size.y, "Geography")) # 10
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by3, self.size.x, self.size.y, "Geography")) # 11
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by3, self.size.x, self.size.y, "Entertainment")) # 8
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by3, self.size.x, self.size.y, "Entertainment")) # 9
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by3, self.size.x, self.size.y, "Sports")) # 10
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by3, self.size.x, self.size.y, "Sports")) # 11

        # 4th row [12 t/m 15] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by4, self.size.x, self.size.y, "History")) # 12
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by4, self.size.x, self.size.y, "History")) # 13
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by4, self.size.x, self.size.y, "Geography")) # 14
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by4, self.size.x, self.size.y, "Geography")) # 15
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by4, self.size.x, self.size.y, "Entertainment")) # 12
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by4, self.size.x, self.size.y, "Entertainment")) # 13
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by4, self.size.x, self.size.y, "Sports")) # 14
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by4, self.size.x, self.size.y, "Sports")) # 15

        # 5th row [16 t/m 19] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by5, self.size.x, self.size.y, "History")) # 16
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by5, self.size.x, self.size.y, "History")) # 17
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by5, self.size.x, self.size.y, "Geography")) # 18
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by5, self.size.x, self.size.y, "Geography")) # 19
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by5, self.size.x, self.size.y, "Entertainment")) # 16
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by5, self.size.x, self.size.y, "Entertainment")) # 17
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by5, self.size.x, self.size.y, "Sports")) # 18
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by5, self.size.x, self.size.y, "Sports")) # 19

        # 6th row [20 t/m 23] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by6, self.size.x, self.size.y, "History")) # 20
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by6, self.size.x, self.size.y, "History")) # 21
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by6, self.size.x, self.size.y, "Geography")) # 22
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by6, self.size.x, self.size.y, "Geography")) # 23
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by6, self.size.x, self.size.y, "Entertainment")) # 20
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by6, self.size.x, self.size.y, "Entertainment")) # 21
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by6, self.size.x, self.size.y, "Sports")) # 22
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by6, self.size.x, self.size.y, "Sports")) # 23

        # 7th row [24 t/m 27] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by7, self.size.x, self.size.y, "History")) # 24
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by7, self.size.x, self.size.y, "History")) # 25
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by7, self.size.x, self.size.y, "Geography")) # 26
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by7, self.size.x, self.size.y, "Geography")) # 27
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by7, self.size.x, self.size.y, "Entertainment")) # 24
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by7, self.size.x, self.size.y, "Entertainment")) # 25
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by7, self.size.x, self.size.y, "Sports")) # 26
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by7, self.size.x, self.size.y, "Sports")) # 27

        # 8th row [28 t/m 31] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by8, self.size.x, self.size.y, "History")) # 28
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by8, self.size.x, self.size.y, "History")) # 29
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by8, self.size.x, self.size.y, "Geography")) # 30
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by8, self.size.x, self.size.y, "Geography")) # 31
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by8, self.size.x, self.size.y, "Entertainment")) # 28
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by8, self.size.x, self.size.y, "Entertainment")) # 29
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by8, self.size.x, self.size.y, "Sports")) # 30
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by8, self.size.x, self.size.y, "Sports")) # 31

        # 9th row [32 t/m 35] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by9, self.size.x, self.size.y, "History")) # 32
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by9, self.size.x, self.size.y, "History")) # 33
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by9, self.size.x, self.size.y, "Geography")) # 34
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by9, self.size.x, self.size.y, "Geography")) # 35
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by9, self.size.x, self.size.y, "Entertainment")) # 32
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by9, self.size.x, self.size.y, "Entertainment")) # 33
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by9, self.size.x, self.size.y, "Sports")) # 34
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by9, self.size.x, self.size.y, "Sports")) # 35

        # 10th row [36 t/m 39] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx1, self.by10, self.size.x, self.size.y, "History")) # 36
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx2, self.by10, self.size.x, self.size.y, "History")) # 37
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx3, self.by10, self.size.x, self.size.y, "Geography")) # 38
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx4, self.by10, self.size.x, self.size.y, "Geography")) # 39
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx1, self.by10, self.size.x, self.size.y, "Entertainment")) # 36
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx2, self.by10, self.size.x, self.size.y, "Entertainment")) # 37
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx3, self.by10, self.size.x, self.size.y, "Sports")) # 38
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx4, self.by10, self.size.x, self.size.y, "Sports")) # 39

#--------------------------------------------------------TOP SECTION--------------------------------------------------------------------------------
        # 11th row [40 t/m 41] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx5, self.by11, self.size.x, self.size.y, "Entertainment")) # 40
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx6, self.by11, self.size.x, self.size.y, "Sports")) # 41
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx5, self.by11, self.size.x, self.size.y, "History")) # 40
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx6, self.by11, self.size.x, self.size.y, "Geography")) # 41

        # 12th row [42 t/m 43] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx5, self.by12, self.size.x, self.size.y, "Entertainment")) # 42
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx6, self.by12, self.size.x, self.size.y, "Sports")) # 43
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx5, self.by12, self.size.x, self.size.y, "History")) # 42
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx6, self.by12, self.size.x, self.size.y, "Geography")) # 43


        # 13th row [44 t/m 45] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx5, self.by13, self.size.x, self.size.y, "Entertainment")) # 44
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx6, self.by13, self.size.x, self.size.y, "Sports")) # 45
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx5, self.by13, self.size.x, self.size.y, "History")) # 44
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx6, self.by13, self.size.x, self.size.y, "Geography")) # 45


        # 14th row [46 t/m 47] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx5, self.by14, self.size.x, self.size.y, "Entertainment")) # 46
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx6, self.by14, self.size.x, self.size.y, "Sports")) # 47
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx5, self.by14, self.size.x, self.size.y, "History")) # 46
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx6, self.by14, self.size.x, self.size.y, "Geography")) # 47


        # 15th row [48 t/m 49] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx5, self.by15, self.size.x, self.size.y, "Entertainment")) # 48
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx6, self.by15, self.size.x, self.size.y, "Sports")) # 49
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx5, self.by15, self.size.x, self.size.y, "History")) # 48
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx6, self.by15, self.size.x, self.size.y, "Geography")) # 49

#-------------------------------------------------------PEAK--------------------------------------------------------------------------------
        # 16th row [50] (Side 1 & 2)
        self.sides[0].tiles.append(tile(screen, self.sides[0], self.bx7, self.by16, self.size.x, self.size.y, "WinRAR")) # 50
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles.append(tile(screen, self.sides[1], self.bx7, self.by16, self.size.x, self.size.y, "WinRAR")) # 50

#--------------------------------------------------------------------------
# Linking the tiles (Bottom to up)
#--------------------------------------------------------------------------
        # NOTE: I seriously need to make an algorithm for this anytime soon, doubt it will be done before the
        # end of the project. So, need to be done manually for the time being. Funny thing is that it would most likely
        # be a simple as hell algorithm, but I just can't focus enough atm to come up with it and test it. - Jordan

        # left, up, right, down
        # 1st row [0 t/m 3] (Side 1 & 2)
        self.sides[0].tiles[0].setupDirections(self.gettile(1,3), self.gettile(0,4), self.gettile(0,1), self.gettile(0,0)) # 0
        self.sides[0].tiles[1].setupDirections(self.gettile(0,0), self.gettile(0,5), self.gettile(0,2), self.gettile(0,1)) # 1
        self.sides[0].tiles[2].setupDirections(self.gettile(0,1), self.gettile(0,6), self.gettile(0,3), self.gettile(0,2)) # 2
        self.sides[0].tiles[3].setupDirections(self.gettile(0,2), self.gettile(0,7), self.gettile(1,0), self.gettile(0,3)) # 3
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[0].setupDirections(self.gettile(0,3), self.gettile(1,4), self.gettile(1,1), self.gettile(1,0)) # 0
        self.sides[1].tiles[1].setupDirections(self.gettile(1,0), self.gettile(1,5), self.gettile(1,2), self.gettile(1,1)) # 1
        self.sides[1].tiles[2].setupDirections(self.gettile(1,1), self.gettile(1,6), self.gettile(1,3), self.gettile(1,2)) # 2
        self.sides[1].tiles[3].setupDirections(self.gettile(1,2), self.gettile(1,7), self.gettile(0,0), self.gettile(1,3)) # 3

        # 2nd row [4 t/m 7] (Side 1 & 2)
        self.sides[0].tiles[4].setupDirections(self.gettile(1,7), self.gettile(0,8), self.gettile(0,5), self.gettile(0,0)) # 4
        self.sides[0].tiles[5].setupDirections(self.gettile(0,4), self.gettile(0,9), self.gettile(0,6), self.gettile(0,1)) # 5
        self.sides[0].tiles[6].setupDirections(self.gettile(0,5), self.gettile(0,10), self.gettile(0,7), self.gettile(0,2)) # 6
        self.sides[0].tiles[7].setupDirections(self.gettile(0,6), self.gettile(0,11), self.gettile(1,4), self.gettile(0,3)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[4].setupDirections(self.gettile(0,7), self.gettile(1,8), self.gettile(1,5), self.gettile(1,0)) # 4
        self.sides[1].tiles[5].setupDirections(self.gettile(1,4), self.gettile(1,9), self.gettile(1,6), self.gettile(1,1)) # 5
        self.sides[1].tiles[6].setupDirections(self.gettile(1,5), self.gettile(1,10), self.gettile(1,7), self.gettile(1,2)) # 6
        self.sides[1].tiles[7].setupDirections(self.gettile(1,6), self.gettile(1,11), self.gettile(0,4), self.gettile(1,3)) # 7

        # 3rd row [8 t/m 11] (Side 1 & 2)
        self.sides[0].tiles[8].setupDirections(self.gettile(1,11), self.gettile(0,12), self.gettile(0,9), self.gettile(0,4)) # 4
        self.sides[0].tiles[9].setupDirections(self.gettile(0,8), self.gettile(0,13), self.gettile(0,10), self.gettile(0,5)) # 5
        self.sides[0].tiles[10].setupDirections(self.gettile(0,9), self.gettile(0,14), self.gettile(0,11), self.gettile(0,6)) # 6
        self.sides[0].tiles[11].setupDirections(self.gettile(0,10), self.gettile(0,15), self.gettile(1,8), self.gettile(0,7)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[8].setupDirections(self.gettile(0,11), self.gettile(1,12), self.gettile(1,9), self.gettile(1,4)) # 4
        self.sides[1].tiles[9].setupDirections(self.gettile(1,8), self.gettile(1,13), self.gettile(1,10), self.gettile(1,5)) # 5
        self.sides[1].tiles[10].setupDirections(self.gettile(1,9), self.gettile(1,14), self.gettile(1,11), self.gettile(1,6)) # 6
        self.sides[1].tiles[11].setupDirections(self.gettile(1,10), self.gettile(1,15), self.gettile(0,8), self.gettile(1,7)) # 7

        # 4th row [12 t/m 15] (Side 1 & 2)
        self.sides[0].tiles[12].setupDirections(self.gettile(1,15), self.gettile(0,16), self.gettile(0,13), self.gettile(0,8)) # 4
        self.sides[0].tiles[13].setupDirections(self.gettile(0,12), self.gettile(0,17), self.gettile(0,14), self.gettile(0,9)) # 5
        self.sides[0].tiles[14].setupDirections(self.gettile(0,13), self.gettile(0,18), self.gettile(0,15), self.gettile(0,10)) # 6
        self.sides[0].tiles[15].setupDirections(self.gettile(0,14), self.gettile(0,19), self.gettile(1,12), self.gettile(0,11)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[12].setupDirections(self.gettile(0,15), self.gettile(1,16), self.gettile(1,13), self.gettile(1,8)) # 4
        self.sides[1].tiles[13].setupDirections(self.gettile(1,12), self.gettile(1,17), self.gettile(1,14), self.gettile(1,9)) # 5
        self.sides[1].tiles[14].setupDirections(self.gettile(1,13), self.gettile(1,18), self.gettile(1,15), self.gettile(1,10)) # 6
        self.sides[1].tiles[15].setupDirections(self.gettile(1,14), self.gettile(1,19), self.gettile(0,12), self.gettile(1,11)) # 7

        # 5th row [16 t/m 19] (Side 1 & 2)
        self.sides[0].tiles[16].setupDirections(self.gettile(1,19), self.gettile(0,20), self.gettile(0,17), self.gettile(0,12)) # 4
        self.sides[0].tiles[17].setupDirections(self.gettile(0,16), self.gettile(0,21), self.gettile(0,18), self.gettile(0,13)) # 5
        self.sides[0].tiles[18].setupDirections(self.gettile(0,17), self.gettile(0,22), self.gettile(0,19), self.gettile(0,14)) # 6
        self.sides[0].tiles[19].setupDirections(self.gettile(0,18), self.gettile(0,23), self.gettile(1,16), self.gettile(0,15)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[16].setupDirections(self.gettile(0,19), self.gettile(1,20), self.gettile(1,17), self.gettile(1,12)) # 4
        self.sides[1].tiles[17].setupDirections(self.gettile(1,16), self.gettile(1,21), self.gettile(1,18), self.gettile(1,13)) # 5
        self.sides[1].tiles[18].setupDirections(self.gettile(1,17), self.gettile(1,22), self.gettile(1,19), self.gettile(1,14)) # 6
        self.sides[1].tiles[19].setupDirections(self.gettile(1,18), self.gettile(1,23), self.gettile(0,16), self.gettile(1,15)) # 7

        # 6th row [20 t/m 23] (Side 1 & 2)
        self.sides[0].tiles[20].setupDirections(self.gettile(1,23), self.gettile(0,24), self.gettile(0,21), self.gettile(0,16)) # 4
        self.sides[0].tiles[21].setupDirections(self.gettile(0,20), self.gettile(0,25), self.gettile(0,22), self.gettile(0,17)) # 5
        self.sides[0].tiles[22].setupDirections(self.gettile(0,21), self.gettile(0,26), self.gettile(0,23), self.gettile(0,18)) # 6
        self.sides[0].tiles[23].setupDirections(self.gettile(0,22), self.gettile(0,27), self.gettile(1,20), self.gettile(0,19)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[20].setupDirections(self.gettile(0,23), self.gettile(1,24), self.gettile(1,21), self.gettile(1,16)) # 4
        self.sides[1].tiles[21].setupDirections(self.gettile(1,20), self.gettile(1,25), self.gettile(1,22), self.gettile(1,17)) # 5
        self.sides[1].tiles[22].setupDirections(self.gettile(1,21), self.gettile(1,26), self.gettile(1,23), self.gettile(1,18)) # 6
        self.sides[1].tiles[23].setupDirections(self.gettile(1,22), self.gettile(1,27), self.gettile(0,20), self.gettile(1,19)) # 7

        # 7th row [24 t/m 27] (Side 1 & 2)
        self.sides[0].tiles[24].setupDirections(self.gettile(1,27), self.gettile(0,28), self.gettile(0,25), self.gettile(0,20)) # 4
        self.sides[0].tiles[25].setupDirections(self.gettile(0,24), self.gettile(0,29), self.gettile(0,26), self.gettile(0,21)) # 5
        self.sides[0].tiles[26].setupDirections(self.gettile(0,25), self.gettile(0,30), self.gettile(0,27), self.gettile(0,22)) # 6
        self.sides[0].tiles[27].setupDirections(self.gettile(0,26), self.gettile(0,31), self.gettile(1,24), self.gettile(0,23)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[24].setupDirections(self.gettile(0,27), self.gettile(1,28), self.gettile(1,25), self.gettile(1,20)) # 4
        self.sides[1].tiles[25].setupDirections(self.gettile(1,24), self.gettile(1,29), self.gettile(1,26), self.gettile(1,21)) # 5
        self.sides[1].tiles[26].setupDirections(self.gettile(1,25), self.gettile(1,30), self.gettile(1,27), self.gettile(1,22)) # 6
        self.sides[1].tiles[27].setupDirections(self.gettile(1,26), self.gettile(1,31), self.gettile(0,24), self.gettile(1,23)) # 7

        # 8th row [28 t/m 31] (Side 1 & 2)
        self.sides[0].tiles[28].setupDirections(self.gettile(1,31), self.gettile(0,32), self.gettile(0,29), self.gettile(0,24)) # 4
        self.sides[0].tiles[29].setupDirections(self.gettile(0,28), self.gettile(0,33), self.gettile(0,30), self.gettile(0,25)) # 5
        self.sides[0].tiles[30].setupDirections(self.gettile(0,29), self.gettile(0,34), self.gettile(0,31), self.gettile(0,26)) # 6
        self.sides[0].tiles[31].setupDirections(self.gettile(0,30), self.gettile(0,35), self.gettile(1,28), self.gettile(0,27)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[28].setupDirections(self.gettile(0,31), self.gettile(1,32), self.gettile(1,29), self.gettile(1,24)) # 4
        self.sides[1].tiles[29].setupDirections(self.gettile(1,28), self.gettile(1,33), self.gettile(1,30), self.gettile(1,25)) # 5
        self.sides[1].tiles[30].setupDirections(self.gettile(1,29), self.gettile(1,34), self.gettile(1,31), self.gettile(1,26)) # 6
        self.sides[1].tiles[31].setupDirections(self.gettile(1,30), self.gettile(1,35), self.gettile(0,28), self.gettile(1,27)) # 7


        # 9th row [32 t/m 35] (Side 1 & 2)
        self.sides[0].tiles[32].setupDirections(self.gettile(1,35), self.gettile(0,36), self.gettile(0,33), self.gettile(0,28)) # 4
        self.sides[0].tiles[33].setupDirections(self.gettile(0,32), self.gettile(0,37), self.gettile(0,34), self.gettile(0,29)) # 5
        self.sides[0].tiles[34].setupDirections(self.gettile(0,33), self.gettile(0,38), self.gettile(0,35), self.gettile(0,30)) # 6
        self.sides[0].tiles[35].setupDirections(self.gettile(0,34), self.gettile(0,39), self.gettile(1,32), self.gettile(0,31)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[32].setupDirections(self.gettile(0,35), self.gettile(1,36), self.gettile(1,33), self.gettile(1,28)) # 4
        self.sides[1].tiles[33].setupDirections(self.gettile(1,32), self.gettile(1,37), self.gettile(1,34), self.gettile(1,29)) # 5
        self.sides[1].tiles[34].setupDirections(self.gettile(1,33), self.gettile(1,38), self.gettile(1,35), self.gettile(1,30)) # 6
        self.sides[1].tiles[35].setupDirections(self.gettile(1,34), self.gettile(1,39), self.gettile(0,32), self.gettile(1,31)) # 7

        # 10th row [36 t/m 39] (Side 1 & 2)
        self.sides[0].tiles[36].setupDirections(self.gettile(1,39), self.gettile(0,40), self.gettile(0,37), self.gettile(0,32)) # 4
        self.sides[0].tiles[37].setupDirections(self.gettile(0,36), self.gettile(0,40), self.gettile(0,38), self.gettile(0,33)) # 5
        self.sides[0].tiles[38].setupDirections(self.gettile(0,37), self.gettile(0,41), self.gettile(0,39), self.gettile(0,34)) # 6
        self.sides[0].tiles[39].setupDirections(self.gettile(0,38), self.gettile(0,41), self.gettile(1,36), self.gettile(0,35)) # 7
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[36].setupDirections(self.gettile(0,39), self.gettile(1,40), self.gettile(1,37), self.gettile(1,32)) # 4
        self.sides[1].tiles[37].setupDirections(self.gettile(1,36), self.gettile(1,40), self.gettile(1,38), self.gettile(1,33)) # 5
        self.sides[1].tiles[38].setupDirections(self.gettile(1,37), self.gettile(1,41), self.gettile(1,39), self.gettile(1,34)) # 6
        self.sides[1].tiles[39].setupDirections(self.gettile(1,38), self.gettile(1,41), self.gettile(0,36), self.gettile(1,35)) # 7

        # TOP SECTION
        # 11th row [40 t/m 41] (Side 1 & 2)
        self.sides[0].tiles[40].setupDirections(self.gettile(1,41), self.gettile(0,42), self.gettile(0,41), self.gettile(0,36)) # 4
        self.sides[0].tiles[41].setupDirections(self.gettile(0,40), self.gettile(0,43), self.gettile(1,40), self.gettile(0,38)) # 5
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[40].setupDirections(self.gettile(0,41), self.gettile(1,42), self.gettile(1,41), self.gettile(1,36)) # 4
        self.sides[1].tiles[41].setupDirections(self.gettile(1,40), self.gettile(1,43), self.gettile(0,40), self.gettile(1,38)) # 5

        # 12th row [42 t/m 43] (Side 1 & 2)
        self.sides[0].tiles[42].setupDirections(self.gettile(1,43), self.gettile(0,44), self.gettile(0,43), self.gettile(0,40)) # 4
        self.sides[0].tiles[43].setupDirections(self.gettile(0,42), self.gettile(0,45), self.gettile(1,42), self.gettile(0,41)) # 5
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[42].setupDirections(self.gettile(0,43), self.gettile(1,44), self.gettile(1,43), self.gettile(1,40)) # 4
        self.sides[1].tiles[43].setupDirections(self.gettile(1,42), self.gettile(1,45), self.gettile(0,42), self.gettile(1,41)) # 5

        # 13th row [44 t/m 45] (Side 1 & 2)
        self.sides[0].tiles[44].setupDirections(self.gettile(1,45), self.gettile(0,46), self.gettile(0,45), self.gettile(0,42)) # 4
        self.sides[0].tiles[45].setupDirections(self.gettile(0,44), self.gettile(0,47), self.gettile(1,44), self.gettile(0,43)) # 5
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[44].setupDirections(self.gettile(0,45), self.gettile(1,46), self.gettile(1,45), self.gettile(1,42)) # 4
        self.sides[1].tiles[45].setupDirections(self.gettile(1,44), self.gettile(1,47), self.gettile(0,44), self.gettile(1,43)) # 5

        # 14th row [46 t/m 47] (Side 1 & 2)
        self.sides[0].tiles[46].setupDirections(self.gettile(1,47), self.gettile(0,48), self.gettile(0,47), self.gettile(0,44)) # 4
        self.sides[0].tiles[47].setupDirections(self.gettile(0,46), self.gettile(0,49), self.gettile(1,46), self.gettile(0,45)) # 5
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[46].setupDirections(self.gettile(0,47), self.gettile(1,48), self.gettile(1,47), self.gettile(1,44)) # 4
        self.sides[1].tiles[47].setupDirections(self.gettile(1,46), self.gettile(1,49), self.gettile(0,46), self.gettile(1,45)) # 5

        # 15th row [48 t/m 49] (Side 1 & 2)
        self.sides[0].tiles[48].setupDirections(self.gettile(1,49), self.gettile(0,50), self.gettile(0,49), self.gettile(0,46)) # 4
        self.sides[0].tiles[49].setupDirections(self.gettile(0,48), self.gettile(0,50), self.gettile(1,48), self.gettile(0,47)) # 5
        #------------------------------------------------------------------------------------------------------------
        self.sides[1].tiles[48].setupDirections(self.gettile(0,49), self.gettile(1,50), self.gettile(1,49), self.gettile(1,46)) # 4
        self.sides[1].tiles[49].setupDirections(self.gettile(1,48), self.gettile(1,50), self.gettile(0,48), self.gettile(1,47)) # 5



#--------------------------------------------------------------------------
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
