# Crée un script qui crée une hiérarchie de dossier qui est 
# repris dans DIRS_NAME.

from pathlib import Path
import shutil

DIRS_NAME = {"Films": ["Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
    "Employes": ["Paul",
                "Pierre",
                "Marie"],
    "Exercices": ["les_variables",
                "les_fichiers",
                "les_boucles"]}

def dirs_creator_here():
    path = Path.cwd()

    for key, value in DIRS_NAME.items():
        output_dir_key = path / key

        for object in value:
            output_dir_value = output_dir_key / object
            output_dir_value.mkdir(exist_ok=True, parents=True)

def dirs_delete():


print("""Bienvenue dans le crateur de dossier de 
---CORPODELIA---""")

while True:
    choice = input("Voulez vous crée votre environnement ou le script est lancer ? y/n : ")
    if choice == 'y' or choice == 'n':
        match choice:
            case 'y':
                dirs_creator_here()
                print("Création terminée ! Aurevoir.")
                break

            case 'n':
                print("Vous aviez décider de rien crée. Aurevoir")
                break
    else:
        print("Mauvaise saisie !")
