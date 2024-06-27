from random import randint


class Camper:
    def __init__(self):
        self.character = 'CAMPER'
        self.pv = 100
        self.flask = 3

    def attack(self):
        return randint(20, 30)

    def flask_health(self):
        return randint(10, 40)


camper = Camper()
character_value = camper.character
pv_value = camper.pv
flask_value = camper.flask
