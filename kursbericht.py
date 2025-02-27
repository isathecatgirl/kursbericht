# https://github.com/isathecatgirl/kursbericht

import random, time

class Lehrer:
    def begruessen(self, schuelerli):
        print("Hallo " + schuelerli.name)

    def erklaeren(self):
        pass

    def frage_stellen(self):
        pass

    def aufrufen(self, schuelerli):
        print(schuelerli.name)

bernd = Lehrer()
Schuelerlis = []

class Schuelerli:
    def __init__(self, name):
        self.name = name
        self.in_kurs = True
        Schuelerlis.append(self)

    def move(self, ziel):
        if (ziel == "aus dem Kurs"):
            self.in_kurs = False
            Schuelerlis.remove(self)
        elif (ziel == "in den Unterricht"):
            bernd.begruessen(self)

    def aktion(self, aktion):
        pass

# todo: implement Lehrer.weinen()
Schuelerli("Max").move("aus dem Kurs")
Schuelerli("Jan").move("aus dem Kurs")
Schuelerli("Carolin").move("aus dem Kurs")

# "Die Profis"
david = Schuelerli("David")
david.move("in den Unterricht")
johannes = Schuelerli("Johannes")
johannes.move("in den Unterricht")
isa = Schuelerli("Isabelle")
isa.move("in den Unterricht")

# Unterricht startet
bernd.erklaeren()

# "Die Mittelguten"
nele = Schuelerli("Nele")
nele.move("in den Unterricht")
chiara = Schuelerli("Chiara")
chiara.move("in den Unterricht")

bernd.erklaeren()

nele.aktion("schwätzen")
chiara.aktion("schwätzen")
isa.aktion("nicht aufpassen")

# "Die Wandreihe"
time.sleep(random.randint(180, 420))

Schuelerli("Janis").move("in den Unterricht")
Schuelerli("Andreas").move("in den Unterricht")
Schuelerli("Joel").move("in den Unterricht")

if random.randint(1, 10) == 10:
    memmer = Schuelerli("Elias")
    memmer.move("in den Unterricht")

david.aktion("frage stellen")
bernd.erklaeren()
johannes.aktion("zusatzinfo geben")

bernd.frage_stellen()

auswahl = random.randint(0, 2)
if (auswahl == 0):
    david.aktion("frage beantworten")
elif (auswahl == 1):
    johannes.aktion("frage beantworten")
else:
    ziel = random.choice(Schuelerlis[5:])
    bernd.aufrufen(ziel)
    ziel.aktion("schweigen")

    david.aktion("frage beantworten")
