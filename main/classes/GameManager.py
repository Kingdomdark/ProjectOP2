import pygame
from .textinput import TextInput
from random import randint
import time
import datetime
import threading
from .AudioVisualManager import spritemanager
from .databasemanager import databasemanager
from .AudioVisualManager import audiomanager
from .Player import player
from .Vector2 import vector2



class gamemanager:
    def __init__(self,screen,contentmanager,questionmanager,tilemanager):
        self.cm = contentmanager
        self.qm = questionmanager
        self.tm = tilemanager
        self.sm = spritemanager()
        self.am = audiomanager()
        self.dbm = databasemanager()

        self.screen = screen

        self.background =  self.cm.sm.getimage("background_game")

        # To store the popups in.
        self.popupmc = None # questionpopupmc(self.screen, self, self.qm.getrandomquestionfromcat("Sports","mc"))
        self.popupo =  None # questionpopupo(self.screen, self, self.qm.getrandomquestionfromcat("Sports","o"))
        self.qpopup = None
        self.diceinfo =  None #dicecontentthrow1(self.screen,self,4,1,"Multiple Choice")
        self.endgamepopup = None
        self.quitnow = None

        # states : (setup), pickdirection, throwdice, question, movement, drop, nextturn
        self.state = "pickdirection"
        self.paused = False
        self.pausescreen = self.sm.getimage("pausescreen")

        self.mtimernext = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)


        # Player stuff
        self.players = [
            player(self.screen, "Player 1", self.sm.getcolor("orange")),
            player(self.screen, "Player 2", self.sm.getcolor("blue")),
            player(self.screen, "Player 3", self.sm.getcolor("red")),
            player(self.screen, "Player 4", self.sm.getcolor("green"))
        ]
        self.curplayer = self.players[0]
        self.players[0].currenttile = self.tm.gettile(0,4)
        self.players[1].currenttile = self.tm.gettile(0,6)
        self.players[2].currenttile = self.tm.gettile(1,4)
        self.players[3].currenttile = self.tm.gettile(1,6)
        # self.players[2].currenttile = self.tm.gettile(0,16)
        print("%s current tile cat = %s. \n position : (%i, %i) " % (self.curplayer.name, self.curplayer.currenttile.category, self.curplayer.currenttile.pos.x, self.curplayer.currenttile.pos.y))

        self.menusize = vector2(285, self.screen.get_width())

        self.buttons = {
            "left" : button(self.screen, self.screen.get_width() - (95 * 3) - 20, 80, self.sm.getimage("left"), self.sm.getimage("left_hover"), self.sm.getimage("left_disabled"), "pickdirection", True),
            "up" : button(self.screen, self.screen.get_width() - (95 * 2) - 20, 80, self.sm.getimage("up"), self.sm.getimage("up_hover"), self.sm.getimage("up_disabled"), "pickdirection", True),
            "right" : button(self.screen, self.screen.get_width() - (95 * 1) - 20, 80, self.sm.getimage("right"), self.sm.getimage("right_hover"), self.sm.getimage("right_disabled"), "pickdirection", True),
            "throw" : button(self.screen, self.screen.get_width() - 285 - 20, 190, self.sm.getimage("throwdice"), self.sm.getimage("throwdice"), self.sm.getimage("throwdice_disabled"), "throwdice", True),
            "back" : button(self.screen, self.screen.get_width() - 285 - 50, 570, self.sm.getimage("back"), self.sm.getimage("back_hover"), self.sm.getimage("back"), "alwaysactive", True),
            "quit" : button(self.screen, self.screen.get_width() - 285 - 50, 630, self.sm.getimage("quitgame"), self.sm.getimage("quitgame_hover"), self.sm.getimage("quitgame"), "alwaysactive", True)
        }
        self.functions =  {
            "left" : self.pickleft,
            "up" : self.pickup,
            "right" : self.pickright,
            "throw" : self.throwdice,
            "back" : self.cm.switchtomenu,
            "quit" : self.createquitpopup
        }

        self.playerfont = pygame.font.SysFont("arial", 30)

    def drawbg(self):
        pygame.draw.rect(self.screen, self.curplayer.color, (self.screen.get_width() - self.menusize.x - 20, 20, self.menusize.x, 50))
        self.playerlabel = self.playerfont.render(self.curplayer.name, 1, self.sm.getcolor("white"))
        self.screen.blit(self.playerlabel,(self.screen.get_width() - self.menusize.x, 25))

        #--------------------------- BUTTON HANDLING --------------------------------------
    # Handles the button handling such when the button is clickable or not.
    def bclickhandling(self,pos):
        if not self.paused:
            if not self.state is "endgame":
                for k,v in self.buttons.items():
                    if v.rect.collidepoint(pos) and self.state == v.state or v.rect.collidepoint(pos) and v.state is "alwaysactive":
                        for i,f in self.functions.items():
                            if k == i:
                                self.am.playsound("menubutton", .8)
                                f()
                if self.popupmc is not None:
                    self.popupmc.bclickhandling(pos)

                if self.popupo is not None:
                    self.popupo.bclickhandling(pos)

                if self.qpopup is not None:
                    self.qpopup.bclickhandling(pos)

        if self.endgamepopup is not None:
            self.endgamepopup.bclickhandling(pos)

            # Button hover handling.
    def bhoverhandling(self,pos):
        if not self.paused:
            if not self.state is "endgame":
                for k,v in self.buttons.items():
                    if self.state == v.state or v.state is "alwaysactive":
                    	if v.rect.collidepoint(pos):
                    		v.imagedrawn = v.imagehover
                    	else:
                    		v.imagedrawn = v.imageidle
                    else:
                        v.imagedrawn = v.imagedis
                # Popup MC stuff
                if self.popupmc is not None:
                    self.popupmc.bhoverhandling(pos)

                # Popup O stuff
                if self.popupo is not None:
                    self.popupo.bhoverhandling(pos)

                #Quit Popup stuff
                if self.qpopup is not None:
                    self.qpopup.bhoverhandling(pos)

            if self.endgamepopup is not None:
                self.endgamepopup.bhoverhandling(pos)

    #--------------------------- BUTTON HANDLING END ----------------------------------

    #--------------------------- (BUTTON FUNCS) -----------------------------------------
    def createquitpopup(self):
        self.qpopup = quitpopup(self.screen,self)

    def pickleft(self):
        self.curplayer.direction = "left"
        print("%s has chosen direction %s" % (self.curplayer.name, self.curplayer.direction))
        self.state = "throwdice"

    def pickup(self):
        self.curplayer.direction = "up"
        self.state = "throwdice"

    def pickright(self):
        self.curplayer.direction =  "right"
        self.state = "throwdice"

    def throwdice(self):
        self.gm = self
        self.type = None

        self.thrown = 3 #randint(1,6)
        if self.thrown == 1 or self.thrown == 2:
            self.curplayer.movesleft = 1
        elif self.thrown == 3 or self.thrown == 4:
            self.curplayer.movesleft = 2
        elif self.thrown == 5 or self.thrown == 6:
            self.curplayer.movesleft = 3

        if self.thrown % 2 == 0:
            self.curplayer.qtype = "mc"
            self.type = "Multiple Choice"
        else:
            self.curplayer.qtype = "o"
            self.type = "Open Question"

        self.diceinfo = dicecontentthrow1(self.screen, self.gm, self.thrown, self.curplayer.direction, self.curplayer.movesleft, self.type)
        print("%s has thrown %i (%i) and has chosen direction %s. \n Question type = %s" % (self.curplayer.name, self.thrown, self.curplayer.movesleft, self.curplayer.direction, self.curplayer.qtype))

        self.makequestionpopup()

        self.state = "question"

    def moveplayer(self):
        if datetime.datetime.utcnow() > self.mtimernext:
            if self.curplayer.movesleft > 0:
                print("Moving, Moves left  : %i" % self.curplayer.movesleft)
                self.curplayer.move(self.curplayer.direction)
                self.am.playsound("movement", .7)
                self.curplayer.movesleft -= 1
                self.mtimernext = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)

                if self.curplayer.currenttile.category is "WinRAR":
                    self.am.playsound("applause", 1)
                    print("Winner, Winner, Chicken Dinner!")
                    self.endgamepopup = winnerpopup(self,self.screen)
                    self.state = "endgame"
            else:
                self.state = "dropcheck"
                self.dropcheck()

    def makequestionpopup(self):
        self.gm.curplayer.turns += 1
        if self.curplayer.qtype == "mc":
            self.popupmc = questionpopupmc(self.screen, self, self.qm.getrandomquestionfromcat(self.curplayer.currenttile.category,"mc"))
        elif self.curplayer.qtype =="o":
            self.popupo = questionpopupo(self.screen, self, self.qm.getrandomquestionfromcat(self.curplayer.currenttile.category,"o"))

    def dropcheck(self):
        if self.state == "dropcheck":
            self.pc = None
            for p in self.players:
                if p.name is not self.curplayer.name:
                    if p.currenttile == self.curplayer.currenttile:
                        self.pc = p

            if self.pc is not None:
                self.gm.am.playsound("fall",1)
                self.ra = randint(2,6)
                for i in range(1,self.ra):
                    self.pc.currenttile = self.pc.currenttile.tiledir.down
                self.state = "pickdirection"
                self.nextplayer()
            else:
                self.state = "pickdirection"
                self.nextplayer()



    def nextplayer(self):
        i = 0
        while True:
            print("%s ? %s" % (self.players[i].name, self.curplayer.name))
            if self.players[i].name == self.curplayer.name:
                print("Aight, found. Doing shit.")
                try:
                    print("Ayy adding 1")
                    self.curplayer = self.players[i + 1]
                    print(self.curplayer.name)
                    break
                except:
                    print("Sheeeit, going back to first.")
                    self.curplayer = self.players[0]
                    break
            else:
                i += 1

    #----------------------------------------------------------------------------------
    def update(self):
        if not self.paused:
            # for player in self.players:
            if self.popupmc is not None:
                self.popupmc.update()
            if self.popupo is not None:
                self.popupo.update()
            if self.qpopup is not None:
                self.qpopup.update()
            if self.endgamepopup is not None:
                self.endgamepopup.update()
            if self.quitnow is not None:
                self.quitnow.update()

            if self.state == "moving":
                self.moveplayer()

    def draw(self):
        # Background
        self.screen.blit(self.background,(0,0))
        # Draw the tiles from the tile manager.
        self.tm.draw()
        # Draw the Menu background
        self.drawbg()

        # Draw the buttons on the main game
        for k,v in self.buttons.items():
            v.draw()

        # Draw the players
        for p in self.players:
            p.draw()

        # Draw the popups
        if self.diceinfo is not None:
            self.diceinfo.draw()
        if self.popupmc is not None:
            self.popupmc.draw()
        if self.popupo is not None:
            self.popupo.draw()
        if self.qpopup is not None:
            self.qpopup.draw()
        if self.endgamepopup is not None:
            self.endgamepopup.draw()
        if self.paused:
            self.screen.blit(self.pausescreen,(0,0))
        if self.quitnow is not None:
            self.quitnow.draw()

class questionpopupmc:
    def __init__(self,screen,gm,mcquestion):
        self.gm = gm
        self.screen = screen
        self.question = mcquestion

        self.state = "alwaysactive"

        self.pos = vector2(50,150)
        self.size = vector2(600,400)
        self.seconds = 50
        self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1) # 1 sec tick

        self.piece = self.size.x / self.seconds # The size of each piece of the timer bar.

        # Fonts
        self.timerfont = pygame.font.SysFont("arial",40)
        self.questionfont = pygame.font.SysFont("arial", 15)
        self.answersfont = pygame.font.SysFont("arial", 18)

        # Static Labels
        self.categorylabel = self.timerfont.render(self.question.category, 1, self.gm.curplayer.color)
        self.questionlabel = self.questionfont.render(self.question.question,1, self.gm.sm.getcolor("black"))
        self.answer1label = self.answersfont.render(self.question.a, 1, self.gm.sm.getcolor("black"))
        self.answer2label = self.answersfont.render(self.question.b, 1, self.gm.sm.getcolor("black"))
        self.answer3label = self.answersfont.render(self.question.c, 1, self.gm.sm.getcolor("black"))
        self.answer4label = self.answersfont.render(self.question.d, 1, self.gm.sm.getcolor("black"))
        print(self.question.question)


        # Create a rect for the hover shit and stuff.
        self.buttons = {
             "a" : button(self.screen, self.pos.x + 10, self.pos.y + 275, self.gm.sm.getimage("empty"), self.gm.sm.getimage("empty_hover"), self.gm.sm.getimage("empty"), "alwaysactive", True),
             "b" : button(self.screen, self.pos.x + self.size.x - 290, self.pos.y + 275, self.gm.sm.getimage("empty"), self.gm.sm.getimage("empty_hover"), self.gm.sm.getimage("empty"), "alwaysactive", True),
             "c" : button(self.screen, self.pos.x + 10, self.pos.y + 330, self.gm.sm.getimage("empty"), self.gm.sm.getimage("empty_hover"), self.gm.sm.getimage("empty"), "alwaysactive", True),
             "d" : button(self.screen, self.pos.x + self.size.x - 290, self.pos.y + 330, self.gm.sm.getimage("empty"), self.gm.sm.getimage("empty_hover"), self.gm.sm.getimage("empty"), "alwaysactive", True)
        }
        self.functions = {
            "a" : self.picka,
            "b" : self.pickb,
            "c" : self.pickc,
            "d" : self.pickd
        }

    def picka(self):
        print("A picked")
        # TODO : Do shit here
        if self.question.checkanswer(self.question.a):
            self.gm.state = "moving"
            self.gm.am.playsound("correct",.8)
            self.gm.curplayer.qcorrect += 1
            print("MC : Correct!, Moving")
        else:
            self.gm.nextplayer()
            self.gm.state = "pickdirection"
            print("MC : Wrong!, Next Player")
            self.gm.am.playsound("wrong",.4)


        # Delet Dis (self)
        self.unlinkself()

    def pickb(self):
        print("B picked")
        # TODO : Do shit here.
        if self.question.checkanswer(self.question.b):
            self.gm.state = "moving"
            self.gm.curplayer.qcorrect += 1
            self.gm.am.playsound("correct",.8)
            print("MC : Correct!, Moving")
        else:
            self.gm.nextplayer()
            self.gm.state = "pickdirection"
            print("MC : Wrong!, Next Player")
            self.gm.am.playsound("wrong",.4)

        # Delet Dis (self)
        self.unlinkself()


    def pickc(self):
        print("C picked")
        # TODO : Do shit here.
        if self.question.checkanswer(self.question.c):
            self.gm.state = "moving"
            self.gm.curplayer.qcorrect += 1
            self.gm.am.playsound("correct",.8)
            print("MC : Correct!, Moving")
        else:
            self.gm.nextplayer()
            self.gm.state = "pickdirection"
            print("MC : Wrong!, Next Player")
            self.gm.am.playsound("wrong",.4)

        # Delet Dis (self)
        self.unlinkself()


    def pickd(self):
        print("D picked")
        # TODO : Do shit here.
        if self.question.checkanswer(self.question.d):
            self.gm.state = "moving"
            self.gm.am.playsound("correct",.8)
            self.gm.curplayer.qcorrect += 1
            print("MC : Correct!, Moving")
        else:
            self.gm.nextplayer()
            self.gm.state = "pickdirection"
            print("MC : Wrong!, Next Player")
            self.gm.am.playsound("wrong",.4)

        # Delet Dis (self)
        self.unlinkself()


    def bhoverhandling(self,pos):
        for k,v in self.buttons.items():
            if self.state == v.state or v.state is "alwaysactive":
            	if v.rect.collidepoint(pos):
            		v.imagedrawn = v.imagehover
            	else:
            		v.imagedrawn = v.imageidle
            else:
                v.imagedrawn = v.imagedis

    def bclickhandling(self,pos):
        for k,v in self.buttons.items():
            if v.rect.collidepoint(pos) and self.state == v.state:
                for i,f in self.functions.items():
                    if k == i:
                        self.gm.am.playsound("menubutton", .6)
                        print("Button clicked")
                        if f is not None:
                            f()
    def qtimer(self):
        if self.seconds > 0:
            if datetime.datetime.utcnow() > self.endtime:
                self.gm.am.playsound("clocktick", 0.4)
                self.seconds -= 1
                self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)

    def unlinkself(self):
        self.gm.diceinfo = None
        self.gm.popupmc = None

    def update(self):
        self.qtimer()

    def draw(self):
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("lightgrey"),(self.pos.x, self.pos.y, self.size.x, self.size.y)) # Background
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("grey"), (self.pos.x, self.pos.y, self.size.x, 5)) # Timer gutter
        pygame.draw.rect(self.screen, self.gm.curplayer.color,(self.pos.x, self.pos.y, self.piece * self.seconds, 5)) # Timerbar
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("black"),(self.pos.x, self.pos.y, self.size.x, self.size.y), 1) # Stroke overlay for background
        self.timerlabel = self.timerfont.render("%i" % self.seconds,1, self.gm.curplayer.color)
        self.screen.blit(self.timerlabel, (self.pos.x + self.size.x - 60, self.pos.y + 10))

        for n,b in self.buttons.items():
            b.draw()

        self.screen.blit(self.categorylabel, (self.pos.x + 10, self.pos.y + 10))
        self.screen.blit(self.questionlabel, (self.pos.x + 10, self.pos.y + 100))
        self.screen.blit(self.answer1label, (self.pos.x + 60, self.pos.y + 280))
        self.screen.blit(self.answer2label, (self.pos.x + 365, self.pos.y + 280))
        self.screen.blit(self.answer3label, (self.pos.x + 60, self.pos.y + 335))
        self.screen.blit(self.answer4label, (self.pos.x + 365, self.pos.y + 335))

class questionpopupo:
    def __init__(self,screen,gm,oquestion):
        self.gm = gm
        self.screen = screen
        self.question = oquestion
        self.category = None
        self.state = "alwaysactive"

        self.pos = vector2(50,150)
        self.size = vector2(600,400)
        self.seconds = 50
        self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1) # 1 sec tick

        self.piece = self.size.x / self.seconds # The size of each piece of the timer bar.

        # Fonts
        self.timerfont = pygame.font.SysFont("arial",40)
        self.questionfont = pygame.font.SysFont("arial", 15)
        self.answersfont = pygame.font.SysFont("arial", 25)
        self.enterfont = pygame.font.SysFont("arial", 30)

        self.answer = TextInput("arial",25)

        # Static Labels
        self.categorylabel = self.timerfont.render(self.question.category, 1, self.gm.curplayer.color)
        self.questionlabel = self.questionfont.render(self.question.question,1, self.gm.sm.getcolor("black"))
        self.answer1label = self.answersfont.render(self.answer.get_text(), 1, self.gm.sm.getcolor("black"))
        self.enterlabel =  self.enterfont.render("Enter", 1, self.gm.sm.getcolor("black"))

        self.buttons = {
            "enter" :  button(self.screen, self.pos.x + 305, self.pos.y + 340, self.gm.sm.getimage("empty"), self.gm.sm.getimage("empty_hover"), self.gm.sm.getimage("empty"), "alwaysactive", True)
        }
        self.functions = {
            "enter" : self.compareanswer
        }

    def compareanswer(self):
        if self.question.checkanswer(self.answer.get_text()):
            print("Open : Correct!, Moving!")
            self.gm.curplayer.qcorrect += 1
            self.gm.am.playsound("correct",.8)
            self.gm.state = "moving"
            self.unlinkself()
        else:
            print("Open : Wrong!")
            self.gm.nextplayer()
            self.gm.state = "pickdirection"
            self.gm.am.playsound("wrong",.5)
            self.unlinkself()

    def bhoverhandling(self,pos):
        for k,v in self.buttons.items():
            if self.state == v.state or v.state is "alwaysactive":
            	if v.rect.collidepoint(pos):
            		v.imagedrawn = v.imagehover
            	else:
            		v.imagedrawn = v.imageidle
            else:
                v.imagedrawn = v.imagedis

    def bclickhandling(self,pos):
        for k,v in self.buttons.items():
            if v.rect.collidepoint(pos) and self.state == v.state:
                for i,f in self.functions.items():
                    if k == i:
                        self.gm.am.playsound("menubutton", .6)
                        if f is not None:
                            f()
    def qtimer(self):
        if datetime.datetime.utcnow() > self.endtime:
            if self.seconds > 0:
                self.gm.am.playsound("clocktick", 0.4)
                self.seconds -= 1
                self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
            else:
                print("Time is up!, Switching Next Player (Open)")
                self.gm.nextplayer()
                self.gm.state = "pickdirection"
                self.unlinkself()

    def unlinkself(self):
        self.gm.diceinfo = None
        self.gm.popupo = None

    def update(self):
        self.qtimer()

    def draw(self):
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("lightgrey"),(self.pos.x, self.pos.y, self.size.x, self.size.y)) # Background
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("grey"), (self.pos.x, self.pos.y, self.size.x, 5)) # Timer gutter
        pygame.draw.rect(self.screen, self.gm.curplayer.color,(self.pos.x, self.pos.y, self.piece * self.seconds, 5)) # Timerbar
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("black"),(self.pos.x, self.pos.y, self.size.x, self.size.y), 1) # Stroke overlay for background
        self.timerlabel = self.timerfont.render("%i" % self.seconds,1, self.gm.curplayer.color)
        self.screen.blit(self.timerlabel, (self.pos.x + self.size.x - 60, self.pos.y + 10))

        pygame.draw.rect(self.screen, self.gm.sm.getcolor("white"), (self.pos.x + 20, self.pos.y + 300, 560, 40))
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("black"), (self.pos.x + 20, self.pos.y + 300, 560, 40), 1)

        self.screen.blit(self.questionlabel, (self.pos.x + 10, self.pos.y + 75))
        self.screen.blit(self.answer.get_surface(), (self.pos.x + 30, self.pos.y + 305))

        for n,b in self.buttons.items():
            b.draw()

        self.screen.blit(self.categorylabel, (self.pos.x + 10, self.pos.y + 10))
        self.screen.blit(self.enterlabel,(self.pos.x + 355, self.pos.y + 340))

class quitpopup():
    def __init__(self,screen, gm):
        self.screen = screen
        self.gm = gm
        self.pos = vector2(50,200)
        self.shutdown = False
        self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
        self.seconds = 3

        self.quitscreen = self.gm.sm.getimage("quitscreen")

        self.textfont = pygame.font.SysFont("arial", 30)
        self.buttonfont = pygame.font.SysFont("arial", 25)

        self.quittext = self.textfont.render("Weet je zeker dat je wilt stoppen met dit spel?", True, (0,0,0))
        self.no = self.buttonfont.render("Nee", True, (0,0,0))
        self.yes =  self.buttonfont.render("Ja", True, (0,0,0))

        self.buttons = {
            "no" : button(self.screen, self.pos.x + 10, self.pos.y + 250, gm.sm.getimage("empty"), gm.sm.getimage("empty_hover"), gm.sm.getimage("empty"), "alwaysactive",  True),
            "yes" : button(self.screen, self.pos.x + 300, self.pos.y + 250, gm.sm.getimage("empty"), gm.sm.getimage("empty_hover"), gm.sm.getimage("empty"), "alwaysactive", True),
        }
        self.functions = {
            "no" : self.disposeself,
            "yes" : self.startshutdown
            }

    def disposeself(self):
        self.gm.qpopup = None

    def startshutdown(self):
        self.shutdown = True

    def timer(self):
        if datetime.datetime.utcnow() > self.endtime:
            if self.seconds > 0:
                self.seconds -= 1
                self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
                print(self.seconds)
            else:
                pygame.quit()

    def bclickhandling(self,pos):
        for k,v in self.buttons.items():
            if v.rect.collidepoint(pos):
                for i,f in self.functions.items():
                    if k == i:
                        self.gm.am.playsound("menubutton", .6)
                        f()

    # Button hover handling.
    def bhoverhandling(self,pos):
        for k,v in self.buttons.items():
            if v.rect.collidepoint(pos):
                v.imagedrawn = v.imagehover
            else:
                v.imagedrawn = v.imageidle


    def draw(self):
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("lightgrey"), (self.pos.x, self.pos.y, 600, 300))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.pos.x, self.pos.y, 600, 300) , 1)
        self.screen.blit(self.quittext, (self.pos.x + 20, self.pos.y + 20))

        for k,v in self.buttons.items():
            v.draw()

        self.screen.blit(self.no, (self.pos.x + 60, self.pos.y + 255))
        self.screen.blit(self.yes, (self.pos.x + 360, self.pos.y + 255))

        if self.shutdown:
            self.screen.blit(self.quitscreen, (0,0))

    def update(self):
        if self.shutdown == True:
            self.timer()

class quitnow:
    def __init__(self,screen, gm):
        self.screen = screen
        self.gm = gm
        self.pos = vector2(50,200)
        self.shutdown = True
        self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
        self.seconds = 3
        self.quitscreen = self.gm.sm.getimage("quitscreen")

    def timer(self):
        if datetime.datetime.utcnow() > self.endtime:
            if self.seconds > 0:
                self.seconds -= 1
                self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
                print(self.seconds)
            else:
                pygame.quit()

    def update(self):
        if self.shutdown == True:
            self.timer()

    def draw(self):
        if self.shutdown:
            self.screen.blit(self.quitscreen, (0,0))

class pregamesetup:
    def __init__(self,gm):
        self.pos = vector2(50,50)
        self.size = vector2(600,400)
        self.gm = gm
        self.playercount = 0

    def unlinkself(self):
     self.gm.popupo = None

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("lightgrey"),(self.pos.x, self.pos.y, self.size.x, self.size.y)) # Background
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("black"),(self.pos.x, self.pos.y, self.size.x, self.size.y), 1) # Stroke overlay for background

class dicecontentthrow1:
    def __init__(self,screen,gm,amount,direction,steps,questiontype):
        self.gm = gm
        self.dir = direction
        self.pos = vector2(695,250)
        self.size = vector2(285,135)
        self.screen = screen
        self.amount = amount
        self.steps = steps
        self.questiontype = questiontype

        self.dicefont = pygame.font.SysFont("arial", 150)
        self.infofont = pygame.font.SysFont("arial", 30, italic=1)

        self.dicetext = self.dicefont.render(str(self.amount), True, self.gm.curplayer.color)
        self.stepstext = self.infofont.render("Steps : %s" % self.steps, True, self.gm.sm.getcolor("black"))
        self.dirtext = self.infofont.render("Direction : %s" % self.dir, True, self.gm.sm.getcolor("black"))
        self.questiontext = self.infofont.render(questiontype, True, self.gm.sm.getcolor("black"))


    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("white"),(self.pos.x, self.pos.y, self.size.x, self.size.y)) # Background
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("lightgrey"),(self.pos.x, self.pos.y, 90, self.size.y) )
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("black"),(self.pos.x, self.pos.y, self.size.x, self.size.y), 1) # Stroke overlay for background
        self.screen.blit(self.dicetext,(self.pos.x + 10, self.pos.y - 15))
        self.screen.blit(self.stepstext,(self.pos.x + 100, self.pos.y + 15))
        self.screen.blit(self.dirtext,(self.pos.x + 100, self.pos.y + 50))
        self.screen.blit(self.questiontext,(self.pos.x + 100, self.pos.y + 85))


class button:
    def __init__(self,screen,posx,posy,img,imghover,imgdisabled,state,visible=None):
        if visible == None:
            visible = False # Used for buttons which should be invisible
        self.visible = visible
        self.stage = 0
        self.state = state
        self.screen = screen
        self.pos = vector2(posx,posy)
        self.imageidle = img
        self.imagehover = imghover
        self.imagedis = imgdisabled
        self.imagedrawn = img
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.imageidle.get_size()[0], self.imageidle.get_size()[1])

    def draw(self):
        # pygame.draw.rect(self.screen,(255,0,0),self.rect)
        if (self.visible):
            self.screen.blit(self.imagedrawn,(self.pos.x, self.pos.y))

    def update(self):
        pass

class winnerpopup:
    def __init__(self,gm,screen):
        self.gm = gm
        self.screen = screen
        self.bg = self.gm.sm.getimage("winnerbg")
        self.trophy = self.gm.sm.getimage("winrar")

        self.titlefont = pygame.font.SysFont("arial", 50)
        self.infofont = pygame.font.SysFont("arial", 30, italic=1)
        self.statsfont1 = pygame.font.SysFont("arial", 27)
        self.statsfont2 = pygame.font.SysFont("arial", 22)

        self.titletext1 = self.titlefont.render("Winner,winner, chicken dinner!", True, self.gm.sm.getcolor("white"))
        self.titletext2 = self.titlefont.render("%s has won the game!" % self.gm.curplayer.name, True, self.gm.curplayer.color)
        self.statstext1 = self.statsfont1.render("Statistics :", True, self.gm.sm.getcolor("white"))
        self.statstext2 = self.statsfont2.render("Turns Taken : %s" % self.gm.curplayer.turns,True ,self.gm.sm.getcolor("white"))
        self.statstext3 = self.statsfont2.render("Questions Correct : %s" % self.gm.curplayer.qcorrect, True, self.gm.sm.getcolor("white"))

        self.answer = TextInput("arial",25)

        self.entertext = self.statsfont2.render("Enter your name below", True, self.gm.sm.getcolor("white"))

        self.buttons = {
            "upload" : button(self.screen,725,590, self.gm.sm.getimage("upload"), self.gm.sm.getimage("upload"), self.gm.sm.getimage("upload"),"alwaysactive",True)
        }

        self.functions = {
            "upload" : self.uploadscore
        }

    def uploadscore(self):
        self.gm.dbm.insertplayer(self.gm.curplayer.qcorrect, self.gm.curplayer.turns, self.answer.get_text())
        self.gm.quitnow = quitnow(self.screen, self.gm)


    def bclickhandling(self,pos):
        for k,v in self.buttons.items():
            if v.rect.collidepoint(pos):
                for i,f in self.functions.items():
                    if k == i:
                        self.gm.am.playsound("menubutton", .6)
                        f()

    # Button hover handling.
    def bhoverhandling(self,pos):
        for k,v in self.buttons.items():
            if v.rect.collidepoint(pos):
                v.imagedrawn = v.imagehover
            else:
                v.imagedrawn = v.imageidle

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.trophy, (50,190))
        self.screen.blit(self.titletext1,(400,30))
        self.screen.blit(self.titletext2,(400,90))
        self.screen.blit(self.statstext1, (400, 300))
        self.screen.blit(self.statstext2, (400, 350))
        self.screen.blit(self.statstext3, (600, 350))

        self.screen.blit(self.entertext, (400,515))
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("white"),(400, 550, 500, 40))
        pygame.draw.rect(self.screen, self.gm.sm.getcolor("black"),(400, 550, 500, 40), 1)

        self.screen.blit(self.answer.get_surface(), (410, 555))

        for k,v in self.buttons.items():
            v.draw()
