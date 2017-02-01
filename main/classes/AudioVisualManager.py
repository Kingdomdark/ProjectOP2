import os
import pygame

# Spritemanager (Dictionary) which contains the sounds which can be used and has functions to return images
# which in return can be used to drawn on the screen.
class spritemanager:
    def __init__(self):
        self.imgfolder = os.path.join(os.getcwd(),"images")
        self.sprites = {

            # Menu Content
            "background" : os.path.join(self.imgfolder,"background.png"),
            "logo" : os.path.join(self.imgfolder,"logo.png"),
            "start" : os.path.join(self.imgfolder,"start.png"),
            "start_hover" : os.path.join(self.imgfolder,"start_hover.png"),
            "instructions" : os.path.join(self.imgfolder,"instructions.png"),
            "instructions_hover" : os.path.join(self.imgfolder,"instructions_hover.png"),
            "highscores" : os.path.join(self.imgfolder, "highscores.png"),
            "highscores_hover" : os.path.join(self.imgfolder, "highscores_hover.png"),
            "quitgame" : os.path.join(self.imgfolder,"quitgame.png"),
            "quitgame_hover" : os.path.join(self.imgfolder,"quitgame_hover.png"),
            "instructions1" : os.path.join(self.imgfolder, "inst1.png"),
            "instructions2" : os.path.join(self.imgfolder, "inst2.png"),
            "instructions3" : os.path.join(self.imgfolder, "inst3.png"),
            "instructions4" : os.path.join(self.imgfolder, "inst4.png"),
            "instructions5" : os.path.join(self.imgfolder, "inst5.png"),

            # Game Content
            "background_game" : os.path.join(self.imgfolder, "background_game.png"),
            "board1" : os.path.join(self.imgfolder, "board1.png"),
            "board2" : os.path.join(self.imgfolder, "board2.png"),
            "tile" : os.path.join(self.imgfolder,"tile.png"),
            "left" : os.path.join(self.imgfolder,"left.png"),
            "left_hover" : os.path.join(self.imgfolder,"left_hover.png"),
            "left_disabled" : os.path.join(self.imgfolder,"left_disabled.png"),
            "up" : os.path.join(self.imgfolder,"up.png"),
            "up_hover" : os.path.join(self.imgfolder, "up_hover.png"),
            "up_disabled" : os.path.join(self.imgfolder, "up_disabled.png"),
            "right" : os.path.join(self.imgfolder, "right.png"),
            "right_hover" : os.path.join(self.imgfolder, "right_hover.png"),
            "right_disabled" : os.path.join(self.imgfolder, "right_disabled.png"),
            "throwdice" : os.path.join(self.imgfolder, "throwdice.png"),
            "throwdice_disabled" : os.path.join(self.imgfolder, "throwdice_disabled.png"),
            "empty" : os.path.join(self.imgfolder, "empty.png"),
            "empty_hover" : os.path.join(self.imgfolder, "empty_hover.png"),
            "back" : os.path.join(self.imgfolder, "backtomenu.png"),
            "back_hover" : os.path.join(self.imgfolder, "backtomenu_hover.png"),
            "quitscreen" : os.path.join(self.imgfolder, "quitscreen.png"),
            "pausescreen": os.path.join(self.imgfolder, "pausescreen.png"),
            "winnerbg" : os.path.join(self.imgfolder, "winnerbg.png"),
            "winrar" : os.path.join(self.imgfolder, "winrar.png"),
            "upload" : os.path.join(self.imgfolder, "upload.png")
        }

        self.colors = {
            "white" : (255, 255, 255),
            "black" : (0, 0, 0),
            "yellow" : (255, 255, 0),
            "red" : (255, 0, 0),
            "green" : (0, 255, 0),
            "blue" : (0, 0, 255),
            "orange" : (255, 128, 0),
            "lightgrey": (232, 233, 234),
            "grey" : (98,98,98)
        }

    def getimage(self,imgname):
        try:
            return pygame.image.load(self.sprites[imgname.lower()])
        except:
            print("AVManager : An error occured whilst importing the image '%s', It might not exist" % imgname)

    def getcolor(self,colorname):
        try:
            return self.colors[colorname.lower()]
        except:
            print("AVManager : An error occured whilst retrieving the color '%s'" % colorname)

# Audiomanager (Dictionary) which contains the sounds which can be used and has functions to play specific sounds on
# the specified volume.
class audiomanager:
    def __init__(self):
        self.soundfolder = os.path.join(os.getcwd(),"sounds")
        self.sounds = {
            "menumusic" : os.path.join(self.soundfolder,"menu-music.mp3"),
            "menubutton" : os.path.join(self.soundfolder, "menu-button.ogg"),
            "correct" : os.path.join(self.soundfolder, "correct-answer.ogg"),
            "wrong" : os.path.join(self.soundfolder, "wrong-answer.ogg"),
            "movement" : os.path.join(self.soundfolder, "movement.ogg"),
            "clocktick" : os.path.join(self.soundfolder, "clock-tick.ogg"),
            "fall" : os.path.join(self.soundfolder, "fall.ogg"),
            "applause" : os.path.join(self.soundfolder, "applause.ogg")
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
