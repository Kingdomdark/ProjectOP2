from random import randint

class questionmanager:
    def __init__(self):
        self.categories = []

        # TODO : Add the categories and attach the questions to it in this class.

        # Example. ([0] = sports, [1] = technology etc., it's an array.)
        self.categories.append(category("Sports"))
        self.categories[0].addoquestion("MAGA?","Ofcourse!")
        self.categories[0].addoquestion("Another one.","You special.")

        self.categories[0].addmcquestion("Mudkipz?","Ayy","Bee","See","Mudkipz!","d")



        self.categories.append(category("Technology"))



    # TODO : Add functionality and shit for the questionmanager itself.

    # Function to get a random question from a category
    # category : The category to look for.
    # qtype : The type of question. mc = Multiple Choice, o = Open.
    def getrandomquestionfromcat(self,category,qtype):
        # check if there are categories present.
        if len(self.categories) > 0:
            # For each category, check if the name of the category
            # corresponds with the input. Return a question from that
            # category as a result.
            for cat in self.categories:
                if cat.name.lower() == category.lower():
                    # Using the type input to retrieve the correct type.
                    if qtype.lower() == "o":
                        return cat.randomoquestion()
                    elif qtype.lower() == "mc":
                        return cat.randommcquestion()
                    else:
                        print("Incorrect type (%s) filled in, cannot attempt to retrieve question." % qtype)
                        return None

            # If nothing has been found. Return None and print an error message.
            # This only gets accessed when there is no category corresponding with the user input.
            print("Cannot find category : '%s' , Have you made a typo?" % category)
            return None

        else:
            print("There are no categories.")
            return None

    #----------------------- DEBUG COMMANDS -------------------------
    # TODO / EXTRA: Add debug functions to print the lists,cats,questions
    def printcats(self):
        s = ""
        if len(self.categories) > 0:
            print("There are %i categories." % len(self.categories))
            for cat in self.categories:
                s += cat.name + ","
            print (s)
        else:
            print("There are no categories.")



# Category class which contains the questions for each category,
# Both open questions and multiple choice questions.
class category:
    def __init__(self,name):
        self.name = name
        self.oquestions = []
        self.mcquestions = []

    # Logic for picking a random question from the category.
    def randomoquestion(self):
        return self.oquestions[randint(0,len(self.oquestions) - 1)]

    def randommcquestion(self):
        return self.mcquestions[randint(0,len(self.mcquestions) - 1)]

    # Logic for adding questions to a category
    # Creates a new question in the appropriate array.
    def addoquestion(self,question,answer):
        self.oquestions.append(oquestion(question,answer))

    def addmcquestion(self,question,a,b,c,d,answer):
        self.mcquestions.append(mcquestion(question,a,b,c,d,answer))


    #----------------------- DEBUG COMMANDS -------------------------
    # Print the open questions list in this category with question and answer.
    def printolist(self):
        if len(self.oquestions) > 0:
            print(" \n There are %i questions in '%s'" % (len(self.oquestions), self.name))
            for o in self.oquestions:
                o.printquestion()
        else:
            print("There are no open questions for '%s'.", self.name)

    # Print the multiple choice questions list of this category with the options and answer.
    def printmclist(self):
        if len(self.mcquestions) > 0:
            print("\n There are %i questions '%s'" % (len(self.mcquestions), self.name))
            for mc in self.mcquestions:
                mc.printquestion()
        else:
            print("There are no multiple choice questions for '%s'." % self.name)



# Open question class which contains the question and answer
# Also has logic to check the answer.
class oquestion:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer

    # compares the given input with the actual answer in lowercase
    def checkanswer(self,answer):
        if self.answer.lower() == answer.lower():
            return True
        else:
            return False

    #----------------------- DEBUG COMMANDS -------------------------
    def printquestion(self):
        print("-----------------------------------------------")
        print("Q: %s, A: %s" % (self.question, self.answer))
        print("-----------------------------------------------")


# Multiple choice question class, contains the question
# and values of a,b,c,d and the correct choice the player
# should make (a,b,c,d).
class mcquestion:
    def __init__(self,question,a,b,c,d,answer):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        # logic to store the answer for easy comparison.
        # cloning the content of the right answer to answer.
        # Forcing to lower a extra precaution.
        if answer.lower() == 'a':
            self.answer = a
        elif answer.lower() == 'b':
            self.answer = b
        elif answer.lower() == 'c':
            self.answer = c
        elif answer.lower() == 'd':
            self.answer = d
        else:
            self.answer = None
            print("question : %s isn't set up correctly. Please fix." % self.question)

    # compares the given input with the actual answer in lowercase
    def checkanswer(self,answer):
        if self.answer.lower() == answer.lower():
            return True
        else:
            return False

    def printquestion(self):
        print("-----------------------------------------------")
        print("Q: %s" % self.question)
        print("A: %s  B: %s " % (self.a,self.b))
        print("C: %s  D: %s " % (self.c,self.d))
        print("Answer: %s" % (self.answer))
        print("-----------------------------------------------")



# Debugging stuff (Don't actually use globals kids, just testing purposes only!!!)
# Only to test the actual logic!!!!


qm = questionmanager()
qm.printcats()
q = qm.getrandomquestionfromcat("SpOrts","o")
print("Q: %s, A: %s" % (q.question,q.answer))
qm.categories[0].printolist()
qm.categories[0].printmclist()
