# Crée un jeux on l'on se déplace dans une foret et ou l'on a une chance sur 3
# De tomber sur un animal et une chance sur 3 de tomber sur le chasseur

from random import randint
import camper
import gard
import animal


def move(macro):
    """
    Args:
        macro(str): The macro input to determine the return value
    Return:
        int: The value corresponding to the macro input
    """
    while True:
        match macro:
            case 'z':
                return 1
            case 'q':
                return 2
            case 'd':
                return 3


def algo():
    algo_number = randint(1, 50)
    return 'animal' if algo_number <= 40 else 'gard'


camper_pv = camper.pv


while True:
    user_choice = input("Choice a direction 'z' 'q' 'd' : ")
    if user_choice in ['z', 's', 'q']:
        if algo() == 'animal':
            print("---OH ITS A ANIMAL---")
            # import stat
            pv = animal.pv
        elif algo() == 'gard':
            print("***DAMN ITS THE GARD***")
            # import stat
            pv = gard.pv
        break
    else:
        print("not ok")
