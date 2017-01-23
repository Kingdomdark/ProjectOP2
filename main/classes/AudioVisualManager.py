import os
import pygame

class spritemanager:
    def __init__(self):
        self.imgfolder = os.path.join(os.getcwd(),"images")
        self.sprites = {
            "background" : os.path.join(self.imgfolder,"background.png"),
            "logo" : os.path.join(self.imgfolder,"logo.png"),
            "tile" : os.path.join(self.imgfolder,"tile.png")
        }

    def getimage(self,imgname):
        try:
            return pygame.image.load(self.sprites[imgname.lower()])
        except:
            print("AVManager : An error occured whilst importing the image '%s', It might not exist" % imgname)

class audiomanager:
    def __init__(self):
        self.soundfolder = os.path.join(os.getcwd(),"sounds")
        self.sounds = {
            "wakemeup" : os.path.join(self.soundfolder,"wakemeup.mp3")
        }

    def playmusicloop(self,soundname):
        try:
            pygame.mixer.music.load(self.sounds[soundname.lower()])
            pygame.mixer.music.set_volume(.05)
            pygame.mixer.music.play(-1)
            print("AVManager : Playing %s" % soundname)
        except:
            print("AVManager : An error occured whilst trying to play the sound '%s', It might not exist." % soundname)
