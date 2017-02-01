from .QuestionManager import questionmanager
from .MenuManager import menumanager
from .GameManager import gamemanager
from .TileManager import tilemanager
from .AudioVisualManager import spritemanager

class contentmanager:
    def __init__(self,screen):
        self.qm = questionmanager()
        self.sm = spritemanager()
        self.tm = tilemanager(screen,self.sm)
        self.mm = menumanager(screen,self)
        self.gm = gamemanager(screen,self,self.qm,self.tm)
        self.stage = 0

    def switchtogame(self):
        self.stage = 1

    def switchtomenu(self):
        self.stage = 0

    def update(self):
        if self.stage == 0:
            self.mm.update()
        elif self.stage == 1:
            self.gm.update()

    def draw(self):
        if self.stage == 0:
            self.mm.draw()
        elif self.stage == 1:
            self.gm.draw()
