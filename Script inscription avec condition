print("Ceci est un logiciel de connexion \nVous devez vous inscrire !")
#Input pour le nom d'utilisateur
maj_ok=False
while not maj_ok:
    print("Votre nom d'utilisateur doit contenir une MAJUSCULE !")
    user=input("Insérée votre nom d'utilsateur : ")
    maj_ok=any(str.isupper() for str in user)
    if maj_ok==False:
        print("VOUS N'AVEZ PAS DE MAJUSCULE")
#Comfirmation
print("Utilisateur CORRECT !")
mdpV=False
#Input pour le mot de passe 
while not mdpV:
    print("8 Caractère minimum, un CHIFFRE et une MAJUSCULE pour le mot de passe")
    mdp=input("Mot de passe : ")
    mdpV=any(str.isupper() for str in mdp) and len(mdp)>8 and any(str.isdigit() for str in mdp)
    if mdpV==False:
        print("RESPECTEZ LES CONDITIONS !!!")
#Comfirmation 2
print("Compte Crée Avec Succès !")
print(f"Votre nom est {user} et votre mot de passe {mdp} ")
