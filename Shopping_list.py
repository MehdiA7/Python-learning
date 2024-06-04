import json
from pathlib import Path
#Save and verification for save
if not Path("list_save.json").is_file():
    with open("list_save.json", 'w', encoding='utf-8') as f:
        course_list = json.dump([], f)
else:
    with open("list_save.json", 'r', encoding='utf-8') as f:
        course_list = json.load(f)

def save():
    with open("list_save.json", 'w', encoding='utf-8') as f:
        json.dump(course_list, f)


#Welcome
print("Bienvenu dans votre liste de course personnel !\nChoisissez l'une des 5 options")
#Instruction
while True:
    print("1. Ajouter\n2. Retirer \n3. Afficher\n4. Vider \n5. Quitter")
#Selector
    while True:
        menu=input("Votre choix : ")
        
        if menu.isdigit():
            break
        else:
            print("SAISIR UN CHIRRE ENTRE 1 ET 5 !")
        command=""
#Add item
    match menu:
        case '1':
            more=True
            while more:
                if course_list==None:
                    course_list=[]
                command=input("Que voulez vous ajouté ? : ")
                course_list.append(command)
                print(f"Vous avez ajouté {command} a la liste !")
                more=input("Voulez vous ajouter encore des articles ? y/n : ")
                if more=='y':
                    more=True
                else:
                    more=False
#Remove
        case '2':
            if course_list!=None:
                see_list="\n".join([f"{index}. {item}" for index, item in enumerate(course_list, start=1)])
                print(see_list)
                while True:
                    try:
                        command=input("Que voulez vous retirer ? : ")
                        
                        index_remove=int(command)-1
                        if 0<= index_remove < len(course_list):
                            course_list.pop(index_remove)
                            print("Supression comfirmé !")
                            break
                        else:
                            print("Erreur cette article n'existe pas")
                    except ValueError:
                        print("ERREUR ENTREZ UN NUMERO VALIDE")
            else:
                print("Votre liste est déjà vide !")
            input("Taper n'importe ou pour continuer : ")
#View
        case '3':
                if course_list!=None:
                    see_list="\n".join([f"{index}. {item}" for index, item in enumerate(course_list, start=1)])
                    print(f"Votre liste\n---------\n{see_list}\n---------\n")
                else:
                    print("Votre liste est vide")
                input("Taper n'importe ou pour continuer : ")
#Clear
        case '4':
            if course_list!=None:
                course_list=course_list.clear()
                print("Votre liste a été supprimer")
            else:
                print("Votre liste est déjà vide")
            input("Taper n'importe ou pour continuer : ")
#Stop and save
        case '5':
            save()
            print("A bientôt !")
            break
