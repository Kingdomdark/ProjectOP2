# This is going to be the menu manager.
from .Vector2 import vector2
import time
import datetime
from .AudioVisualManager import spritemanager
from .AudioVisualManager import audiomanager
from .databasemanager import databasemanager
import pygame

class menumanager:
	def __init__(self,screen,contentmanager):
		self.screen = screen
		# Load image
		self.limg = pygame.image.load
		self.sm = spritemanager()
		self.am = audiomanager()
		self.cm = contentmanager # Reference to parent used to invoke methods on the parent.

		# Play a shitty song on loop
		# TODO : Upon progressing to the game, change the music played.
		self.am.playmusicloop("menumusic", .4)

		# Get the images from the spritemanager
		self.logo = self.sm.getimage("logo")
		self.menu = self.sm.getimage("background")

		# Instructions popup > Image need to change
		self.ipopup = None
		# highscores popup  Image need to change
		self.hpopup = None
		#Quit popup
		self.qpopup = None
		# Shortcut for screenblit.
		self.sb = self.screen.blit

		# menu = Buttons on the menu are active.
		# instructions =  Buttons on the instuctions are active.
		# inactive = Don't render and handle click events of anything.
		self.state = "menu"

		# Button array for storing the buttons which can be callable
		# from a string.
		self.buttons = {
			"start" : button(self.screen, 20, 230, self.sm.getimage("start"), self.sm.getimage("start_hover"),"menu"),
			"instructions" : button(self.screen, 20, 290, self.sm.getimage("instructions"), self.sm.getimage("instructions_hover"),"menu"),
			"highscores": button(self.screen, 20, 350, self.sm.getimage("highscores"),self.sm.getimage("highscores_hover"), "menu"),
			"quit" : button(self.screen, 20, 410, self.sm.getimage("quitgame"), self.sm.getimage("quitgame_hover"), "menu")
		}
		# Array used to link functions to the buttons.
		# Be sure not to include the () when adding the function.
		self.functions = {
			"start" : self.switchstage,
			"instructions" : self.instructionsPress,
			"highscores": self.highscorePress,
			"quit" : self.quitpopupPress
		}

#--------------------------- BUTTON HANDLING --------------------------------------
	# Handles the button handling such when the button is clickable or not.
	def bclickhandling(self,pos):
		if self.hpopup is not None:
			self.hpopup.bclickhandling(pos)
		# Doing a KVP-Loop with the buttons to go through the buttons.
		if self.qpopup is not None:
			self.qpopup.bclickhandling(pos)
		for k,v in self.buttons.items():
			# Check if the mouse is in a rectangle and compare the state
			# With the parent variable. If equal, go further. This is to prevent
			# to make the button clickable when it's not supposed to.
			if v.rect.collidepoint(pos) and self.state == v.parent:
				# Doing a KVP-Loop with the functions.
				for i,f in self.functions.items():
					# If the key of the buttons KVP-Loop is the same as the
					# key of the functions KVP-Loop, execute the value of the
					# functions key. (Effectively a link.)
					if k == i:
						self.am.playsound("menubutton", .6)
						f()


    # Button hover handling.
	def bhoverhandling(self,pos):
		for k,v in self.buttons.items():
			if v.rect.collidepoint(pos) and self.state == v.parent:
				v.imagedrawn = v.imagehover
			else:
				v.imagedrawn = v.imageidle

		if self.hpopup is not None:
			for k,v in self.hpopup.buttons.items():
				if v.rect.collidepoint(pos):
					v.imagedrawn = v.imagehover
				else:
					v.imagedrawn = v.imageidle

		if self.qpopup is not None:
			self.qpopup.bhoverhandling(pos)

#--------------------------- BUTTON HANDLING END ----------------------------------
	def draw(self):
		if self.state is not "inactive":
			self.sb(self.menu, (0,0))
			self.sb(self.logo, (20,20))
			# Draw the buttons (KVP-Loop)
			for k,v in self.buttons.items():
			 	v.draw()
			#self.ipopup.draw()
			if self.ipopup is not None:
				self.ipopup.draw()
			if self.hpopup is not None:
				self.hpopup.draw()
			if self.qpopup is not None:
				self.qpopup.draw()

	def update(self):
		if self.state is not "inactive":
			for k,v in self.buttons.items():
				v.update()
		if self.qpopup is not None:
			self.qpopup.update()

	def highscorePress(self):
		self.hpopup = highscorePopup(self.screen, self, 200 , 200)

	def instructionsPress(self):
		self.ipopup = instructionPopup(self.screen, self)

	def quitpopupPress(self):
		self.qpopup = quitpopup(self.screen, self)

	def testfunction(self):
		print("Testing")

	def switchstage(self):
		self.cm.stage = 1



#------------ Class functions
# Add functions which can be invoked by the buttons.

class button:
	def __init__(self,screen,posx,posy,img,imghover,parent):
		self.stage = 0
		self.parent = parent
		self.screen = screen
		self.pos = vector2(posx,posy)
		self.imageidle = img
		self.imagehover = imghover
		self.imagedrawn = img
		self.rect = pygame.Rect(self.pos.x, self.pos.y, self.imageidle.get_size()[0], self.imageidle.get_size()[1])

	def draw(self):
		# pygame.draw.rect(self.screen,(255,0,0),self.rect)
		self.screen.blit(self.imagedrawn,(self.pos.x, self.pos.y))


	def update(self):
		pass


class instructionPopup:
	def __init__(self ,screen, mm):
		self.mm = mm
		self.size = vector2(600,300)
		self.screen = screen
		self.x = 50
		self.y = 30

		self.imgs = [
			self.mm.sm.getimage("instructions1"),
			self.mm.sm.getimage("instructions2"),
			self.mm.sm.getimage("instructions3"),
			self.mm.sm.getimage("instructions4"),
			self.mm.sm.getimage("instructions5")
		]
		self.curimg = 0

	def draw(self):
		pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.size.x, self.size.y))
		self.screen.blit(self.imgs[self.curimg],(self.x,self.y))

	def bclickhandling(self):
		if self.curimg < len(self.imgs) - 1:
			self.curimg += 1
		else:
			self.disposeself()

	def disposeself(self):
		self.mm.ipopup = None


class highscorePopup:
	def __init__(self ,screen, mm, x , y):
		self.mm = mm
		self.x = 100
		self.y = 120
		self.screen = screen
		# create connection with database manager

		self.dbm = databasemanager()

		self.buttons = {
			"back" : button(self.screen, self.x + 410, self.y + 400, mm.sm.getimage("empty"), mm.sm.getimage("empty_hover"), None)
		}
		self.functions = {
		 	"back" : self.disposeself
		}

		#highscores
		self.columnfont = pygame.font.SysFont("arial", 30)
		self.font = pygame.font.SysFont("arial",25)

		#title
		self.title = pygame.font.SysFont("arial", 70)

		self.results = self.dbm.download_top_score()
		self.hscores = []
		for i in range(0,len(self.results)):
			self.hscores.append(hscore(self.results[i][2],int(self.results[i][0]), int(self.results[i][1])))

	def disposeself(self):
		self.mm.hpopup = None

	# Handles the button handling such when the button is clickable or not.
	def bclickhandling(self,pos):
		# Doing a KVP-Loop with the buttons to go through the buttons.
		for k,v in self.buttons.items():
			# Check if the mouse is in a rectangle and compare the state
			# With the parent variable. If equal, go further. This is to prevent
			# to make the button clickable when it's not supposed to.
			if v.rect.collidepoint(pos):
				# Doing a KVP-Loop with the functions.
				for i,f in self.functions.items():
					# If the key of the buttons KVP-Loop is the same as the
					# key of the functions KVP-Loop, execute the value of the
					# functions key. (Effectively a link.)
					if k == i:
						self.mm.am.playsound("menubutton", .06)
						f()

	# Button hover handling.
	def bhoverhandling(self,pos):
		for k,v in self.buttons.items():
			if v.rect.collidepoint(pos) and self.state == v.parent:
				v.imagedrawn = v.imagehover
			else:
				v.imagedrawn = v.imageidle

	def draw(self):
		pygame.draw.rect(self.screen, self.mm.sm.getcolor("lightgrey"), (self.x, self.y, 700, 450))
		pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 700, 450) , 1)
		#Highscore title
		self.highscoreTitle = self.title.render("TOP 5 ", True, (255,255,255))
		# self.closep = self.columnfont.render("Close Popup", True, (255,255,255)
		# columns
		self.columnName = self.columnfont.render("Name", True, (0, 0, 0))
		self.columnCQ = self.columnfont.render("Correct questions", True, (0, 0, 0))
		self.columnT = self.columnfont.render("Turns", True, (0, 0, 0))


		self.screen.blit(self.highscoreTitle, (self.x + 10, self.y + 10))
		# drawing columns
		self.screen.blit(self.columnName, (self.x + 20, self.y + 120))
		self.screen.blit(self.columnCQ, (self.x + 200, self.y + 120))
		self.screen.blit(self.columnT, (self.x + 500, self.y + 120))
		self.spacing = 40

		for k,v in self.buttons.items():
			v.draw()

		self.screen.blit(self.columnfont.render("Close Popup", True, (0,0,0)),(self.x + 460, self.y + 400))
		for i in range(0, len(self.hscores)):
			self.name = self.font.render(str(self.hscores[i].name), True, (0, 0, 0))
			self.Cquestions = self.font.render(str(self.hscores[i].cquestions), True, (0, 0, 0))
			self.turns = self.font.render(str(self.hscores[i].turns), True, (0, 0, 0))

			self.screen.blit(self.name, (self.x + 20, self.y + 170 + (self.spacing * i)))
			self.screen.blit(self.Cquestions, (self.x + 275, self.y + 170 + (self.spacing * i)))
			self.screen.blit(self.turns, (self.x + 520, self.y + 170 + (self.spacing * i)))

class quitpopup():
	def __init__(self,screen, mm):
		self.screen = screen
		self.mm = mm
		self.pos = vector2(350,200)
		self.shutdown = False
		self.endtime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
		self.seconds = 3

		self.quitscreen = self.mm.sm.getimage("quitscreen")

		self.textfont = pygame.font.SysFont("arial", 30)
		self.buttonfont = pygame.font.SysFont("arial", 25)

		self.quittext = self.textfont.render("Weet je zeker dat je wilt stoppen met dit spel?", True, (0,0,0))
		self.no = self.buttonfont.render("Nee", True, (0,0,0))
		self.yes =  self.buttonfont.render("Ja", True, (0,0,0))

		self.buttons = {
		 	"no" : button(self.screen, self.pos.x + 10, self.pos.y + 250, mm.sm.getimage("empty"), mm.sm.getimage("empty_hover"), None),
		 	"yes" : button(self.screen, self.pos.x + 300, self.pos.y + 250, mm.sm.getimage("empty"), mm.sm.getimage("empty_hover"), None),
		}
		self.functions = {
			"no" : self.disposeself,
			"yes" : self.startshutdown
		}

	def disposeself(self):
		self.mm.qpopup = None

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
						self.mm.am.playsound("menubutton", .6)
						f()

	# Button hover handling.
	def bhoverhandling(self,pos):
		for k,v in self.buttons.items():
			if v.rect.collidepoint(pos):
				v.imagedrawn = v.imagehover
			else:
				v.imagedrawn = v.imageidle


	def draw(self):
		pygame.draw.rect(self.screen, self.mm.sm.getcolor("lightgrey"), (self.pos.x, self.pos.y, 600, 300))
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




class hscore:
	def __init__(self, name, cquestions, turns):
		self.name = name
		self.cquestions = cquestions
		self.turns = turns
