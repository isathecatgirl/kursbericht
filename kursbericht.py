# https://github.com/isathecatgirl/kursbericht

import random, time

class Lehrer:
    def begruessen(self, schuelerli):
        print("Hallo " + schuelerli.name)

    def erklaeren(self):
        erklärung = random.randint(1, 5)
        if (erklärung == 1):
            print("Ich habe euch was auf moodle hochgeladen")
        elif (erklärung == 2):
            print("Öffnet Inf-Schule bei Kapitel " + str(random.randint(1, 15)))
        else:
            print("Schaut mal kurz nach vorne")
            
        if (random.randint(1, 256) == 16):
            isa.aktion("fällt vom Stuhl")
            
    def frage_stellen(self):
        fragen = [
            "Was ist das Ziel von Komunikation?",
            "Was sind die Anforderungen an Datenbanken?",
            "Was ist ein guter Programmierstil?"
        ]
        print(random.choice(fragen))

    def aufrufen(self, schuelerli):
        print(schuelerli.name + " versuchs mal")
    
    def unterricht_beenden(self):
        print("Schöner Tag noch, Tschüss")
 
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
        print(self.name + " " + aktion)

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

nele.aktion("schwätzt")
chiara.aktion("schwätzt")
isa.aktion("passt nicht auf")

# "Die Wandreihe"
time.sleep(random.randint(128, 512))

Schuelerli("Janis").move("in den Unterricht")
Schuelerli("Andreas").move("in den Unterricht")
Schuelerli("Joel").move("in den Unterricht")

if random.randint(1, 10) == 10:
    memmer = Schuelerli("Elias")
    memmer.move("in den Unterricht")

david.aktion("stellt eine Frage")
bernd.erklaeren()
johannes.aktion("gibt Zusatzinfos")

# Stillarbeit
time.sleep(32)
bernd.frage_stellen()

auswahl = random.randint(0, 2)
if (auswahl == 0):
    david.aktion("beantwortet die Frage")
elif (auswahl == 1):
    johannes.aktion("beantwortet die Frage")
else:
    ziel = random.choice(Schuelerlis[5:])
    bernd.aufrufen(ziel)
    ziel.aktion("schweigt")

    david.aktion("beantwortet die Frage")

# Glocke ertönt
time.sleep(128)
bernd.unterricht_beenden()
