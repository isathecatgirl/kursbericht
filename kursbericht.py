# https://github.com/isathecatgirl/kursbericht

import random

class Schuelerli:
    def __init__(self, name):
        self.name = name
        self.in_kurs = True

    def abwaehlen(schuelerli):
        schuelerli.in_kurs = False

    def unterricht_besuchen(_):
        pass


carolin = Schuelerli("Carolin")
carolin.abwaehlen()

memmer = Schuelerli("Elias")
if (random.randint(1, 10) == 10):
    memmer.unterricht_besuchen()