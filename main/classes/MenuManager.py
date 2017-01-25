# This is going to be the menu manager.
from .Vector2 import vector2
from .AudioVisualManager import spritemanager
from .AudioVisualManager import audiomanager
import pygame

class menumanager:
	def __init__(self,screen,gamemanager):
		self.screen = screen
		# Load image
		self.limg = pygame.image.load
		self.sm = spritemanager()
		self.am = audiomanager()
		self.gm = gamemanager # Reference to parent used to invoke methods on the parent.
		print(self.gm)

		# Play a shitty song on loop
		# TODO : Upon progressing to the game, change the music played.
		self.am.playmusicloop("menumusic", .05)

		# Get the images from the spritemanager
		self.logo = self.sm.getimage("logo")
		self.menu = self.sm.getimage("background")

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
			"quit" : button(self.screen, 20, 350, self.sm.getimage("quitgame"), self.sm.getimage("quitgame_hover"), "menu")
		}
		# Array used to link functions to the buttons.
		# Be sure not to include the () when adding the function.
		self.functions = {
			"start" : self.testfunction,
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

	def update(self):
		if self.state is not "inactive":
			for k,v in self.buttons.items():
				v.update()
		


	def testfunction(self):
		print("Testing")



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