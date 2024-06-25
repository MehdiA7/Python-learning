# Crée un jeux on l'on se déplace dans une foret et ou l'on a une chance sur 3
# De tomber sur un animal et une chance sur 3 de tomber sur le chasseur
from random import randint
import time
from camper import camper
from gard import gard
from animal import animal


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
    """
    Generates a random number between 1 and 50 and returns 'animal'
    if the number is less than or equal to 40, otherwise 'gard'.

    Returns:
        str: Either 'animal' or 'gard'.
    """
    algo_number = randint(1, 50)
    return 'animal' if algo_number <= 40 else 'gard'


def fight(camper_pv, enemy_name, enemy_pv):
    """
    Args
        :param camper_pv:
        :param enemy_name:
        :param enemy_pv:
    :return:
    """
    enemy_pv = enemy_pv
    print(f"\nCAMPER PV : {camper_pv}\n{enemy_name} PV : {enemy_pv}\n")
    while True:
        user_input = input("ATTACK OR HEALTH ? a/h : ")
        if user_input == 'a' or user_input == 'h':

            if enemy_name == 'ANIMAL':
                enemy_attack = animal.attack()
            else:
                enemy_attack = gard.attack()

            match user_input:

                case 'a':
                    camper_attack = camper.attack()
                    enemy_pv = enemy_pv - camper_attack
                    if enemy_pv > 0:
                        camper_pv = camper_pv - enemy_attack

                    else:
                        enemy_attack = 0

                    print(f"\nYOUR DAMAGE -> {camper_attack}\n{75*'-'}")
                    time.sleep(1)
                    print(f"ENEMY DAMAGE -> {enemy_attack}\n{75*'-'}")
                    time.sleep(2)
                    print(f"{3*'\n'}***CAMPER PV*** : {camper_pv}\n")
                    print(f"{enemy_name} PV : {enemy_pv}{3*'\n'}")
                    if enemy_pv <= 0 or camper_pv <= 0:

                        if enemy_pv <= 0:
                            print(f"YOU KILLED {enemy_name}")
                            return camper_pv
                        return camper_pv

                    else:
                        continue

                case 'h':
                    if flask != 0:
                        health = camper.flask_health()
                        camper_pv = camper_pv + health
                        print(f"\nTHIS POTION GIVES YOU {health}\n")
                        camper_pv = camper_pv - enemy_attack
                        print(f"BUT THE {enemy_name} IS THERE !!")
                        time.sleep(2)
                        print(f"ENEMY DAMAGE -> {enemy_attack}\n{75*'-'}")
                        time.sleep(1)
                        print(f"{3*'\n'}***CAMPER PV*** : {camper_pv}\n")
                        print(f"{enemy_name} PV : {enemy_pv}{3*'\n'}")
                        if camper_pv <= 0:
                            return camper_pv

                        else:
                            continue

                    else:
                        print("*** NO FLASK ***")

        else:
            print("THIS IS NOT AN ACTION")


camperPV = camper.pv
flask = camper.flask
while True:
    if camperPV >= 0:
        user_choice = input("Choice a direction 'z' 'q' 'd' : ")
        if user_choice in ['z', 's', 'q']:
            if algo() == 'animal':
                print("---OH ITS A ANIMAL---")
                camperPV = fight(camperPV, animal.character, animal.pv())

            elif algo() == 'gard':
                print("***DAMN ITS THE GARD***")
                camperPV = fight(camperPV, gard.character, gard.pv())

        else:
            print("not ok")
    else:
        print("GAME OVER")
        break
