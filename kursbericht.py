# https://github.com/isathecatgirl/kursbericht

import random, time

class Lehrer:
    def erklaeren(_):
        pass

class Schuelerli:
    def __init__(self, name):
        self.name = name
        self.in_kurs = True

    def abwaehlen(schuelerli):
        schuelerli.in_kurs = False

    def unterricht_besuchen(schuelerli):
        print(schuelerli.name + " ist da")

bernd = Lehrer()

# TODO: make this look nicer / remove?
max = Schuelerli("Max")
max.abwaehlen()
jan = Schuelerli("Jan")
jan.abwaehlen()
carolin = Schuelerli("Carolin")
carolin.abwaehlen()

# Needs approval; TODO: do async if not too disgusting?
wand_reihe = [
    Schuelerli("Janis"),
    Schuelerli("Andreas"),
    Schuelerli("Joel"),
    Schuelerli("Elias")
]

for schuelerli in wand_reihe:
    if schuelerli.name == "Elias" and random.randint(1, 10) > 9:
        continue

    time.sleep(random.randint(180, 420))
    schuelerli.unterricht_besuchen()
    
