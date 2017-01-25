from .QuestionManager import questionmanager
from .MenuManager import menumanager

class contentmanager:
    def __init__(self,screen):
        self.qm = questionmanager()
        self.mm = menumanager(screen,self)
        self.stage = 0

        print(self)

    def update(self):
        if self.stage == 0:
            self.mm.update()
        elif self.stage == 1:
            pass

    def draw(self):
        if self.stage == 0:
            self.mm.draw()
        elif self.stage == 1:
            pass
