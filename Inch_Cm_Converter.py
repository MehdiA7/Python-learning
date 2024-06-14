# Crée un programme de conversion d'unités
# Il doit être capable de convertir des pouces en centimètres
# et inversément.
# 1. Demander a l'utilisateur si il veut convertir en pouce ou en cm ? 
# 2. Demander la valeur
# 3. Demander si il veut quiter ou continuer le programme.
# 1 pouce = 2,54 cm
# 1 cm = 0,393701 pouce
# Fonction
def inch_cm():
    result = float(user) * 2.54
    print(f"{result} CM")
def cm_inch():
    result = float(user) * 0.393701
    print(f"{result} INCH")
# Variable
mode_check = True
# Welcome message
print("bienvenu dans le programme de conversion")
while mode_check == True:
    # Input
    mode = input("Voulez vous convertir de pouce a cm 'p' ou en centimètre a pouce 'c' ? : ")
    if mode == 'p' or mode == 'c':
        mode_check = False
        # Loop
        while True:
            user = input ("Pour quitter 'q'\nLe nombre que vous voulez convertir : ")
            # Vérification
            if user.isdigit():
                match mode:
                    case 'p':
                        inch_cm()
                    case 'c':
                        cm_inch()
            # Exit
            elif user == 'q':
                print("---BYE---")
                break
            # Error 
            else:
                print("Erreur de saisie")
    else:
        print("Ce mode n'existe pas")
