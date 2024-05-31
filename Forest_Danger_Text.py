#Le jeux comporte 2 joueur l'utilisateur et l'ennemi
#On commence tout les 2 avec 50 points de vie
#L'utilisateur dispose de 3 potions pour récupérée de la vie
#L'ennemi n'a aucune potion
#chaque potion ramène de façon aléatoire entre 15 et 50 points de vie
#L'utilisateur inflige entre 5 et 10 points de vie de dégat
#l'attaque ennemi entre 5 et 15
#Lorsque l'utilisateur utilise une potion il passe au prochain tour
#Dans le script il faut demander directement a l'utilisateur si il veut attaquer
# ou prendre une potion 

import random

player_pv = 50
player_flask = 3
enemy_pv = 50

#Welcome
print("***Bienvenu dans Forest Danger !***")
print("""-----------------------------------------------------------------------
Vous êtes un randonneur aguérri vous venez souvent ici.
Mais encore une fois ce garde forestier vous embête... Cette fois ci,
Vous allez vous défendre ! Et pas n'importe comment !
-----------------------------------------------------------------------
----AU COMBAT!----""")
#Tuto
print("Attaquez ou buvez un remontant !")
while not player_pv <= 0 or enemy_pv <= 0:

    player = input("Attaque ! (1) Boire un remontant ! (2) : ")
    if player.isdigit():
        player = int(player)
        if 0 < player <=2:
            match player:

                #Attack
                case 1:
                    #Player
                    player_damage = random.randint(5,10)
                    enemy_pv = enemy_pv - player_damage
                    print(f"\nVous avez infliger --{player_damage}-- points de dégats ! Il lui reste {enemy_pv}PV\n")
                    #----
                    print("-" * 75)
                    #Enemy
                    enemy_damage =  random.randint(5,15)
                    player_pv = player_pv - enemy_damage
                    print(f"\nLe forestier vous a infliger ---{enemy_damage}--- points de dégats ! Il vous reste {player_pv}PV\n")

                #Health
                case 2:
                    #Player
                    if player_flask > 0:
                        player_flask = player_flask-1
                        player_health = random.randint(15,25)
                        player_pv = player_pv + player_health
                        print(f"\nVous avez gagné --{player_health}PV-- TOTAL *{player_pv}PV* Il vous reste {player_flask} remontant !  ")
                    #Enemy
                        enemy_damage =  random.randint(5,15)
                        player_pv = player_pv - enemy_damage
                        print(f"\nLe forestier {enemy_pv}PV vous a infliger ---{enemy_damage}--- points de dégats ! Il vous reste {player_pv}PV\n")

                    #ERROR Empty flask
                    else:
                        print("Vous n'avez plus de remontant...")
        #Error is digit but is not "1" or "2"
        else:
            print("Entrez une action valide !")
    #Error is not digit
    else:
        print("Entrez un chiffre !")

    #Win
    if enemy_pv <= 0:
        print("VOUS AVEZ GAGNE !")
        print(f"Il vous reste {player_pv}PV et {player_flask} Remontant !\nVous ne le reverrez pas avant un bon moment !")
        if player_pv<0:
            print("\nAutant te dire que tu est quand même fort amoché...")
            break
        break

    #Loose
    elif player_pv <= 0:
        print("PERDU...")
        print("Tu aura peut-être plus de chance la prochaine fois...\nEn attendant tu ira te promener ailleurs")
        break
