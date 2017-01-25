import os
import pygame

# Spritemanager (Dictionary) which contains the sounds which can be used and has functions to return images
# which in return can be used to drawn on the screen.
class spritemanager:
    def __init__(self):
        self.imgfolder = os.path.join(os.getcwd(),"images")
        self.sprites = {
            "background" : os.path.join(self.imgfolder,"background.png"),
            "logo" : os.path.join(self.imgfolder,"logo.png"),
            "start" : os.path.join(self.imgfolder,"start.png"),
            "start_hover" : os.path.join(self.imgfolder,"start_hover.png"),
            "instructions" : os.path.join(self.imgfolder,"instructions.png"),
            "instructions_hover" : os.path.join(self.imgfolder,"instructions_hover.png"),
            "quitgame" : os.path.join(self.imgfolder,"quitgame.png"),
            "quitgame_hover" : os.path.join(self.imgfolder,"quitgame_hover.png"),
            "tile" : os.path.join(self.imgfolder,"tile.png")
        }

    def getimage(self,imgname):
        try:
            return pygame.image.load(self.sprites[imgname.lower()])
        except:
            print("AVManager : An error occured whilst importing the image '%s', It might not exist" % imgname)

# Audiomanager (Dictionary) which contains the sounds which can be used and has functions to play specific sounds on
# the specified volume.
class audiomanager:
    def __init__(self):
        self.soundfolder = os.path.join(os.getcwd(),"sounds")
        self.sounds = {
            "menumusic" : os.path.join(self.soundfolder,"menu-music.mp3"),
            "menubutton" : os.path.join(self.soundfolder, "menu-button.ogg")
        }

    def playmusicloop(self,soundname,volume):
        try:
            pygame.mixer.music.load(self.sounds[soundname.lower()])
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
            print("AVManager : Playing %s" % soundname)
        except:
            print("AVManager : An error occured whilst trying to play the sound '%s', It might not exist." % soundname)

    def playsound(self,soundname,volume):
        try:
            s = pygame.mixer.Sound(self.sounds[soundname.lower()])
            s.set_volume(volume)
            s.play(0)
            print("AVManager : Playing %s" % soundname)
        except:
            print("AVManager : An error occured whilst trying to play the sound '%s', It might not exist." % soundname)
