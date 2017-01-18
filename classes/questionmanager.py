import pygame

class openquestions:
    def __init__(self , question   ,answer , cat):
        self.question = question
        self.answer  = answer
        self.cat      = cat


# Multi choise questions
class mc_questions:
    def __init__(self ,question , a ,  b , c ,d , correct  , cat ):
        self.question = question  #given question
        self.a        = a         # answer a
        self.b        = b         # answer b
        self.c        = c         # answer c
        self.d        = d         # answer d
        self.cat      = cat       # category question


        #checks correct answer
        if correct == 'a':
            self.correct = a
        elif correct == 'b':
            self.correct = b
        elif correct == 'c':
            self.correct = c
        elif correct  == 'd':
            self.correct = d
        else:
            self.correct = None


# list of multiple choise questions
mc_questions = [mc_questions("" , "" , "" , ""  , "" , "" )]


#list of open questions
openquestions = [openquestions("question"," answer", "category" )]