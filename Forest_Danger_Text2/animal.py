from random import randint


class Animal:
    def __init__(self):
        self.character = 'ANIMAL'

    def pv(self):
        return randint(20, 50)

    def attack(self):
        return randint(10, 15)


animal = Animal()
character_value = animal.character
