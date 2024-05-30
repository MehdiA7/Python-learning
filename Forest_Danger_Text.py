#Le jeux comporte 2 joueurs l'utilisateur et l'enemy
#On commence tout les 2 avec 50 points de vie
#L'utilisateur dispose de 3 potions pour récupérée de la vie
#L'enemy n'a aucune potion
#chaque potion ramène de façon aléatoire entre 15 et 50 points de vie
#L'utilisateur inflige entre 5 et 10 points de vie de dégat
#l'attaque enemy entre 5 et 15
#Lorsque l'utilisateur utilise une potion il passe au prochain tour
#Dans le script il faut demander directement a l'utilisateur si il veut attaquer
# ou prendre une potion 

from random import randint

player_pv = 50
player_flask = 3
enemy_pv = 50


def enemy_attack(displayHP = False):
    enemy_damage =  randint(5,15)
    player_pv = player_pv - enemy_damage
    textHp = f"{enemy_pv}PV " if displayHP else ""
    print(f"\nLe forestier {textHp}vous a infliger ---{enemy_damage}--- points de dégats ! Il vous reste {player_pv}PV\n")

def line():
    return "-" * 75

#Welcome
print("***Bienvenu dans Forest Danger !***")
print(f"""{line()}
Vous êtes un randonneur aguérri vous venez souvent ici.
Mais encore une fois ce garde forestier vous embête... Cette fois ci,
Vous allez vous défendre ! Et pas n'importe comment !
{line()}
----AU COMBAT!----""")

#Tuto
print("Attaquez ou buvez un remontant !")
while not player_pv <= 0 or enemy_pv <= 0:

    player = input("Attaque ! (1) Boire un remontant ! (2) : ")
    if player.isdigit():
        player = int(player)
        if 0 < player <=2:
            match player:
                case 1:
                    #Player
                    player_damage = randint(5,10)
                    enemy_pv = enemy_pv - player_damage
                    print(f"\nVous avez infliger --{player_damage}-- points de dégats ! Il lui reste {enemy_pv}PV\n")
                    #----
                    print(line())
                    #enemy
                    enemy_attack()

                case 2:
                    if player_flask > 0:
                        player_flask = player_flask-1
                        player_health = randint(15,25)
                        player_pv = player_pv + player_health
                        print(f"\nVous avez gagné --{player_health}PV-- TOTAL *{player_pv}PV* Il vous reste {player_flask} remontant !")
                        #----
                        print(line())
                        #enemy
                        enemy_attack(True)
                    else:
                        print("Vous n'avez plus de remontant...")

        else:
            print("Entrez une action valide !")
    else:
        print("Entrez un chiffre !")
    if enemy_pv <= 0:
        print("VOUS AVEZ GAGNE !")
        print(f"Il vous reste {player_pv}PV et {player_flask} Remontant !\nVous ne le reverrez pas avant un bon moment !")
        if player_pv<0:
            print("\nAutant te dire que tu est quand même fort amoché...")
            break
        break

    elif player_pv <= 0:
        print("PERDU...")
        print("Tu aura peut-être plus de chance la prochaine fois...\nEn attendant tu ira te promener ailleurs")
        break
