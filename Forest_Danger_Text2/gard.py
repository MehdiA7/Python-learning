from random import randint


class Gard:
    def __init__(self):
        self.character = 'GARD'

    def pv(self):
        return 100

    def attack(self):
        return randint(10,30)


gard = Gard()
character_value = gard.character
