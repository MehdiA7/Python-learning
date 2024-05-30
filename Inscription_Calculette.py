print("J'ai envie de coder...")
retry=True    
print("Alors c'est parti !")
while retry==True:

    choice=input("Que veux tu faire ? Calculer ? 'c' ou T'inscrire ? 'i' : ")

#CONNEXION
    if choice=='i':
        print("Ceci est un logiciel de connexion\nVous devez vous inscrire !")

        maj_ok = mdpV = False
        while not maj_ok:
            user = input("Votre nom d'utilisateur doit contenir une MAJUSCULE !\nInsérée votre nom d'utilisateur : ")
            maj_ok = any(c.isupper() for c in user)
            print("VOUS N'AVEZ PAS DE MAJUSCULE" if not maj_ok else "Utilisateur CORRECT !")

        while not mdpV:
            mdp = input("8 Caractère minimum, un CHIFFRE et une MAJUSCULE pour le mot de passe\nMot de passe : ")
            mdpV = any(c.isupper() for c in mdp) and len(mdp) > 8 and any(c.isdigit() for c in mdp)
            print("RESPECTEZ LES CONDITIONS !!!" if not mdpV else "Compte Crée Avec Succès !")

            print(f"Votre nom est {user} et votre mot de passe {mdp}")
        retry=input("Voulez vous retourner au menu principale ? y/n : ")
        if retry=='y':
            retry=True
        else:
            retry=False

#CALCULATRICE

    if choice=='c':
        print("Bienvenu dans la Calculatrice !")

        encore=True
        while encore:
            choix_methode=print("Choisir un méthode :\nAddition 'a'\nSoustraction 's'\nMultiplication 'm'\nDivision 'd'")

            erreur=True
            while erreur:
                methode=input("Entrez la methode que vous voulez : ")
                if methode=='a' or methode=='s' or methode=='m' or methode=='d':
                    erreur=False
                else:
                    print("SAISIE MAUVAISE 'a','s','m','d'")

            erreur=True
            while erreur:
                a=input("Saisir le premier nombre : ")
                b=input("Saisir le deuxième nombre : ")
                if a.isdigit() and b.isdigit():
                    erreur=False
                else:
                    print("VEUILLEZ ENTRER DE NOMBRE !")

            a, b=int(a), int(b)

            if methode=='a':
                print(f"Le résultat de l'addition est {a} + {b} = {a+b}")

            elif methode=='s':
                print(f"Le résultat de la soustraction est {a} - {b} = {a-b}")

            elif methode=='m':
                print(f"Le résultat de la multiplication est {a} x {b} = {a*b}")

            elif methode=='d':
                a, b=float(a), float(b)
                print(f"Le résultat de la division est {a} : {b} = {a/b}")
            encore=input("Encore un calcule ? 'y'/'n'")
            if encore=='y':
                encore=True
            else:
                encore=False
                print("Aurevoir !")
                retry=input("Voulez vous retourner au menu principale ? y/n : ")
    if retry=='y':
        retry=True
    else:
        print("SAISIE INCORRECT !")
