# Fonction
# Method
def addition():
    result = a + b
    return result
def soustraction():
    result = a - b
    return result
def multiplication():
    result = a * b
    return result
def division():
    result = a / b 
    return result
# Number to calculate
restart = True
while restart == True:
    while True:
        try:
            a = int(input("Entrez le premier chiffre : "))
            b = int(input("Entrez un autre chiffre : "))
            break
        except ValueError:
            print("Saisir un chiffre !")
# Choice of method
    while True:
        select = input("Addition 'a'/ Soustraction 's'/ Multiplication 'm'/ Division 'd' : ")
        match select:
            case 'a':
                methode = "l'addition"
                result = addition()
                break
            case 's':
                methode = "la soustraction"
                result = soustraction()
                break
            case 'm':
                methode = "la multiplication"
                result = multiplication()
                break
            case 'd':
                methode = "la division"
                result = division()
                break
            case _:
                print("ERROR methode doesn't exist")
# print the result
    print(f"Le résultat de {methode} de {a} et {b} est --{result}--")
# Restart request
    restart = input("Voulez vous recommencer ? y/n : ")
    if restart == "y":
        restart = True
    else:
        print("A la prochaine !")
        restart = False
