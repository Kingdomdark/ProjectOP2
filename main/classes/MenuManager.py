# This is going to be the menu manager.
from .Vector2 import vector2
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
		self.am.playmusicloop("menumusic", .05)

		# Get the images from the spritemanager
		self.logo = self.sm.getimage("logo")
		self.menu = self.sm.getimage("background")

		# Instructions popup > Image need to change
		self.ipopup = instructionPopup(self.screen,self.sm.getimage("background"),200,200)
		# highscores popup  Image need to change
		self.hpopup = highscorePopup(self.screen, self.sm.getimage("quitgame"), 200, 200)
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
			"highscores": button(self.screen, 20, 350, self.sm.getimage("instructions"),self.sm.getimage("instructions_hover"), "menu"),
			"quit" : button(self.screen, 20, 410, self.sm.getimage("quitgame"), self.sm.getimage("quitgame_hover"), "menu")
		}
		# Array used to link functions to the buttons.
		# Be sure not to include the () when adding the function.
		self.functions = {
			"start" : self.switchstage,
			"instructions" : self.testfunction,
			"quit" : pygame.quit
		}

#--------------------------- BUTTON HANDLING --------------------------------------
	# Handles the button handling such when the button is clickable or not.
	def bclickhandling(self,pos):
		# Doing a KVP-Loop with the buttons to go through the buttons.
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
						self.am.playsound("menubutton", .05)
						f()

    # Button hover handling.
	def bhoverhandling(self,pos):
		for k,v in self.buttons.items():
			if v.rect.collidepoint(pos) and self.state == v.parent:
				v.imagedrawn = v.imagehover
			else:
				v.imagedrawn = v.imageidle

#--------------------------- BUTTON HANDLING END ----------------------------------
	def draw(self):
		if self.state is not "inactive":
			self.sb(self.menu, (0,0))
			self.sb(self.logo, (20,20))
			# Draw the buttons (KVP-Loop)
			for k,v in self.buttons.items():
			 	v.draw()
			self.ipopup.draw()
			self.hpopup.draw()

	def update(self):
		if self.state is not "inactive":
			for k,v in self.buttons.items():
				v.update()
		


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
		# self.size = vector2(width,height)
		# self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
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
	def __init__(self ,screen,img, x , y):
		self.x = x
		self.y = y
		self.img = img
		self.screen = screen
	def draw(self):
		self.screen.blit(self.img,(self.x,self.y))


class highscorePopup:
	def __init__(self ,screen,img, x , y):
		self.x = x
		self.y = y
		self.img = img
		self.screen = screen
		# create connection with database manager

		self.dbm = databasemanager()

		self.font =pygame.font.SysFont("comicsansms",72)
	def draw(self):
		results = self.dbm.download_scores()
		for row in results:
			score = row[0]
			fname = row[1]

			self.name = self.font.render(str(fname),True,(0,128,0))
			self.score = self.font.render(str(score), True, (0, 128, 0))

			self.screen.blit(self.name, (0, 100))
			self.screen.blit(self.score, (100, 200))


