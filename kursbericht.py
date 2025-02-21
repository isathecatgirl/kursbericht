# https://github.com/isathecatgirl/kursbericht

import random, time

class Lehrer:
    def erklaeren(_):
        pass

ziele = {
    "aus dem Kurs": 0,
    "in den Unterricht": 1
}

class Schuelerli:
    def __init__(self, name):
        self.name = name
        self.in_kurs = True

    def move(schuelerli, ziel):
        if (ziel == ziele["aus dem Kurs"]):
            schuelerli.in_kurs = False

bernd = Lehrer()

# Too repetitive?
# TODO: make this look nicer / remove?
abwaehler = [
    Schuelerli("Max"),
    Schuelerli("Jan"),
    Schuelerli("Carolin")
]

for schuelerli in abwaehler:
    schuelerli.move(ziele["aus dem Kurs"])

# Needs approval
wandreihe = [
    Schuelerli("Janis"),
    Schuelerli("Andreas"),
    Schuelerli("Joel"),
    Schuelerli("Elias")
]

for schuelerli in wandreihe:
    if schuelerli.name == "Elias" and random.randint(1, 10) > 9:
        continue

    time.sleep(random.randint(180, 420))
    schuelerli.move(ziele["in den Unterricht"])
