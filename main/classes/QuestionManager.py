from random import randint

class questionmanager:
    def __init__(self):
        self.categories = []

        # TODO : Add the categories and attach the questions to it in this class.

        # Example. ([0] = sports, [1] = technology etc., it's an array.)
        #self.categories.append(category("Sports"))
        #self.categories[0].addoquestion("MAGA?","Ofcourse!")
        #self.categories[0].addoquestion("Another one.","You special.")
         # sport mp questions 10
        self.categories.append(category("Sport"))
        self.categories[0].addmcquestion(". Hoe lang duurt een professionele voetbalwedstrijd?","120 min","60 min","90 min","140 min","c"),
        self.categories[0].addmcquestion("Bij welke sport horen de termen “strike” en “spare”?","bowlen","hockey","voetbal","tennis","a"),
        self.categories[0].addmcquestion("Hoe heet de Haagse voetbalclub?","Ado kek","FC haag","Ado Den Haag","Cmi boys","c"),
        self.categories[0].addmcquestion("Om de hoeveel jaar worden de Olympische zomerspelen gehouden?","3 jaar","6 jaar","8 jaar","4 jaar","d"),
        self.categories[0].addmcquestion("Hoe wordt de watervariant van handbal genoemd?","waterbal","handwater","waterpolo","polowater","c"),
        self.categories[0].addmcquestion("Bij welke sport horen de woorden cap en amazone?","paardensport","voetbal","tennis","pingpong","a"),
        self.categories[0].addmcquestion("Hoe wordt een beoefenaar van de vechtkunst karate genoemd?","karetekan","karateka","shinobi","kaizoku","b"),
        self.categories[0].addmcquestion("Hoe worden de stokken waarmee geslagen wordt bij golf genoemd?","pipos","katana","clubs","kunai","c"),
        self.categories[0].addmcquestion("Hoe heet het gedeelte van een berg dat geprepareerd is om te skiën?","piste","python","java","pistachio","d"),
        self.categories[0].addmcquestion("Hoe wordt een beoefenaar van judo genoemd?","nani","judoka","bakayaro","orewatemekoroshta","b"),


    # sport open questions 10
        self.categories[0].addoquestion("Waar vonden de dramatische Spelen van '72 plaats?","Munchen"),
        self.categories[0].addoquestion("Welke bokser beet er ooit een stuk uit het oor van bokser Evander Holyfield tijdens een titelgevecht?","Mike tyson"),
        self.categories[0].addoquestion("Bij welke wintersport probeert de skip de steen zo dicht mogelijk bij de dolly te schuiven, terwijl zijn teamgenoten de richting en snelheid van de steen met borstels proberen te beïnvloeden?","curling"),
        self.categories[0].addoquestion("Hoeveel spikes draagt een normale golfschoen?","4"),
        self.categories[0].addoquestion("In welk land ligt het circuit van Zandvoort?","Nederland"),
        self.categories[0].addoquestion("Hoelang duurt een Hockeywedstrijd?","70 min"),
        self.categories[0].addoquestion("Bestaat er in de atletiek naast de 100 meter sprint ook de 100 meter horden?","ja"),
        self.categories[0].addoquestion("Bij welke watersport bestaat een wedstrijd uit 4 maal 7 minuten?","waterpolo"),
        self.categories[0].addoquestion("Welk gemengd balspel is van Nederlandse oorsprong?","korfbal"),
        self.categories[0].addoquestion("Welk land werd in 2000 Europees kampioen voetbal?","Frankrijk"),




        self.categories.append(category("Geography"))
        #geo mc q 10
        self.categories[1].addmcquestion("Van welk land is Paramaribo de hoofdstad?","Suriname","Pakistan","Nederland","Trinidad en tobago","a")
        self.categories[1].addmcquestion("In welke stad brandde het Olympische vuur voor het eerst?","Barcelona","Lahore","Rome","Amsterdam","d")
        self.categories[1].addmcquestion("Hoeveel minuten duurt een ronde bij een bokswedstrijd?","3 min","6 min","5 min","8 min","a")
        self.categories[1].addmcquestion("In welke Nederlands e stad is de beroemde restaurant Konak te vinden","Amsterdam","Rotterdam","Gouda","Utrecht","b")
        self.categories[1].addmcquestion("Welke stad wordt als enige genoemd in het Wilhelmus?","Maastricht","Den haag","Rotterdam,","Utrecht","a")
        self.categories[1].addmcquestion("Welk land wordt de parel van Afrika genoemd?","Angola","Ghana","Oeganda","Senegal","d")
        self.categories[1].addmcquestion("Welke Russische stad heette tot 1991 Leningrad?","Moscow","Sint-Petersburg","Perm","Podolsk","b")
        self.categories[1].addmcquestion("Welke rivier wordt ook wel China’s verdriet genoemd?","De gele rivier","De Chung rivier","heppy helloween","xuan chi","a")
        self.categories[1].addmcquestion("Wat is de hoogst gelegen hoofdstad van Europa?","Madrid","Amsterdam","Oslo","Boekarest","d")
        self.categories[1].addmcquestion("Wat is de hoofdstad van Burundi?","Gitega","Rumonge","See","Mukike","d")

        #geo open q 10
        self.categories[1].addoquestion("Hoe noemt met de hoeveelheid tijd waarin de Aarde één maal om de zon beweegt?","Een siderisch jaar")
        self.categories[1].addoquestion("Wat is het meest bezochte park in de Verenigde Staten?","Central park")
        self.categories[1].addoquestion("In welk land zijn de breedbandverbindingen voor internet het best?","Japan")
        self.categories[1].addoquestion("Hoe heette Myanmar voor 1989?","Birma")
        self.categories[1].addoquestion("In welke stad staat de grootste loempiafabriek van Europa?","Katwijk")
        self.categories[1].addoquestion("In welke stad vind je de Chatuckakmarkt, één van de grootste markten ter wereld?","Bangkok")
        self.categories[1].addoquestion("Waar staat het grootste reuzenrad ter wereld?","Singapore")
        self.categories[1].addoquestion("Wat is de hoofdstad van de VS","Washington")
        self.categories[1].addoquestion("Wat is de hoofdstad van Japan","Tokyo")
        self.categories[1].addoquestion("Wat is de hoofdstad van China","Beijing")

        self.categories.append(category("Entertainment"))
        #ent mc q 10
        self.categories[2].addmcquestion("Welk bedrijf maakte als eerst een volledige 3d-animatiefilm?","Pixar","disney","studio ghibli","dreamworks","a")
        self.categories[2].addmcquestion("In wie veranderde Miley Stewart wanneer zij haar blonde pruik opzette?","Alexis Texas","Hannah montaa","Binh","Jordan","b")
        self.categories[2].addmcquestion("Welke actrice speelde Lara Croft in de filmreeks van Tomb Raider?","Riley reid","Angelina Jolie","D.va","Mei","b")
        self.categories[2].addmcquestion("Wat is de naam van de hond in de tv-serie Family Guy?","Brian","Pappa Franku","Genji","Wouta","b")
        self.categories[2].addmcquestion("Wat was de naam van het kanaal Disney XD voor 2010?","Jetix","Pyton","plagiaat","memes","a")
        self.categories[2].addmcquestion("der welke naam is de filmprijs Academy Award beter bekend?","harambe","buntu","oscar","Ricky","c")
        self.categories[2].addmcquestion("Wat is de naam van de rode race-auto uit de animatiefilm “Cars”?","CMI","konak","lightning mqking","lightning mcqueen","d")
        self.categories[2].addmcquestion("Uit welk Noord-Brabants dorp kwamen de hangjongeren uit New Kids?","Village hidden in the memes","Maaskantje","joggerdam","konakkers","b")
        self.categories[2].addmcquestion("Welke actrice speelde Monica Gellar in de serie Friends?","Courteney Cox","Remy lacroix","Celine dion","Meg turney","a")
        self.categories[2].addmcquestion("Wat is de naam van het tweede deel uit The Matrix trilogie?","The matrix ayy lmao","reloaded the matrix","matrix the return of harambe","The Matrix Reloaded","d")
        # ent o q 10
        self.categories[2].addoquestion("Welk televisienetwerk begon als eerst met het non-stop uitzenden van videoclips?","MTV")
        self.categories[2].addoquestion("In welke stad speelt de serie CSI: Crime Scene Investigation zich af?","las vegas")
        self.categories[2].addoquestion("Hoe heet de radioversie van Studio Sport?","NOS Langs de Lijn")
        self.categories[2].addoquestion("Wat wordt bedoeld met 90210 in de tienersoap Beverly Hills, 90210?","De postcode")
        self.categories[2].addoquestion("Welke kleur heeft de teletubbie Tinky Winky?","paars")
        self.categories[2].addoquestion("Wat zijn Meowth, Rattata en Bulbasaur?","Pokemon")
        self.categories[2].addoquestion("In welke film vind je de personages Will Turner en Elizabeth Swann?","Pirates of the Caribbean")
        self.categories[2].addoquestion("Hoe wordt de mysterieuze coureur in het programma Top Gear genoemd?","The Stig")
        self.categories[2].addoquestion("Wat is de naam van de eerste Nederlandse 3D-film?","Nova Zembla")
        self.categories[2].addoquestion("Van welk sprookje werd in 2010 een film met o.a. Johnny Depp uitgebracht?","Alice in Wonderland")

        self.categories.append(category("History"))
        # hist mc q 10
        self.categories[3].addmcquestion("Wanneer eindigde de eerste wereldoorlog?","1918","1917","1915","1921","b")
        self.categories[3].addmcquestion("Hoe heette de vader van Anne Frank?","Otto","Fabian","Liwei","Maher","a")
        self.categories[3].addmcquestion("Welk land stuurde de eerste mens de ruimte in?","Canada","India","VS","Sovjet-Unie","d")
        self.categories[3].addmcquestion("Wanneer begon de tweede wereldoorlog?","1929","1931","1932","1939","d")
        self.categories[3].addmcquestion("Naar welk land vluchtte koningin Wilhelmina tijdens de tweede wereldoorlog?","Belgie","Engeland","Spanje","Frankrijk","b")
        self.categories[3].addmcquestion("Welke dictator werd op 30 december 2006 in Bagdad geëxecuteerd?","Chung chin","Mao zedong","Saddam Hoessein","Ho chi minh","c")
        self.categories[3].addmcquestion("Uit welk land kwam de schrijver en filosoof Plato?","Griekenland","Italie","Spanje","Belgie","a")
        self.categories[3].addmcquestion("Waar dacht Christoffel Columbus dat hij was toen hij in 1492 Amerika ontdekte?","Engeland","India","Suriname","China","b")
        self.categories[3].addmcquestion("Wie was de eerste vrouwelijke huisarts?","Frankina","Binhinni","Lisa ann","Aletta Jacobs","d")
        self.categories[3].addmcquestion("In welke bunker pleegde Adolf Hitler op 30 april 1945 zelfmoord?","Scheizenbach","Overwatchingzung","Führerbunker","Hamburger","c")

        # hist o q 10
        self.categories[3].addoquestion("In welk jaar overleed prins Bernhard?","2004")
        self.categories[3].addoquestion("Wat was het beroep van Frans Hals?","schilder")
        self.categories[3].addoquestion("Hoe worden Romeinen genoemd die in amfitheaters vochten als leedvermaak?","gladiatoren")
        self.categories[3].addoquestion("Welk werelddeel werd ooit Nieuw-Holland genoemd?","Australie")
        self.categories[3].addoquestion("Welk object liet keizer Qin Shi Huangdi bouwen om het Chinese keizerrijk te beschermen?","De Chinese Muur")
        self.categories[3].addoquestion("Bij welke kunstenaar ging Gerrit (ook wel Gerard genoemd) Dou in de leer?","Rembrandt")
        self.categories[3].addoquestion("Welk land werd vroeger “Het land van het Midden” genoemd omdat de bewoners dachten dat het het middelpunt op aarde was?","China")
        self.categories[3].addoquestion("Waarvan is het leger gemaakt dat staat bij het graf van Keizer Qin Shi Huangdi?","Klei")
        self.categories[3].addoquestion("Hoe werden de volgelingen van Calvijn en Luther, die hun eigen kerken vormden genoemd?","De protestanten")
        self.categories[3].addoquestion("Waarvoor staat de afkorting VOC?","Verenigde Oostindische Compagnie")








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

# 
# qm = questionmanager()
# qm.printcats()
# q = qm.getrandomquestionfromcat("SpOrts","o")
# print("Q: %s, A: %s" % (q.question,q.answer))
# qm.categories[0].printolist()
# qm.categories[0].printmclist()
