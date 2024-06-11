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
# Where the files will be created
path = Path.cwd()
# Function that allows you to CREATE folders
def dirs_creator_here():
    for key, value in DIRS_NAME.items():
        output_dir_key = path / key

        for object in value:
            output_dir_value = output_dir_key / object
            output_dir_value.mkdir(exist_ok=True, parents=True)
# Function that allows you to REMOVE folders
def dirs_delete():
    for key in DIRS_NAME.keys():
        delete = path / key
        shutil.rmtree(delete)
# Welcome message
print("""Bienvenue dans le crateur de dossier de 
---CORPODELIA---""")
# Menu
while True:
    choice = input("Voulez vous crée votre environnement ou le script est lancer ? y/n : ")
    if choice == 'y' or choice == 'n':
        match choice:
# Create Dirs
            case 'y':
                dirs_creator_here()
                print("Création terminée ! Aurevoir.")
                break
# Bye or Remove dirs
# Remove Dirs
            case 'n':
                delete = input("Voulez vous supprimer les dossiers ? y/n : ")
                if delete == 'y':
                    dirs_delete()
                    print("Vos dossiers on bien été supprimer. Aurevoir.")
                    break
# Bye
                else:
                    print("Vous aviez décider de rien crée. Aurevoir")
                    break
# Wrong string
    else:
        print("Mauvaise saisie !")
