from random import randint

class questionmanager:
    def __init__(self):
        self.categories = []

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
        self.addmcquestion.append(mcquestion(question,a,b,c,d,answer))


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


# Debugging stuff (Don't actually use globals kids, just testing purposes only!!!)
# Only to test the actual logic!!!!
c  = category("Random")
print (c.name)
c.addoquestion("MAGA?","Yes")
c.addoquestion("Ayy?","Lmao!")
c.addoquestion("Dank memes?", "Fast as fuck boi.")
print("There are %i open questions in the category '%s'." % (len(c.oquestions),c.name))
for q in c.oquestions:
    print("-----------------------------------------------")
    print("Q: %s, A: %s" % (q.question, q.answer))
    print("-----------------------------------------------")
rq = c.randomoquestion()
print("Random Q :  Q : %s, A: %s " % (rq.question, rq.answer))
