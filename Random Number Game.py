import random
#Objectif
mystery_number=random.randint(1,100)

print("---Welcome to the mystery number games !---")
retry=True
while retry:
    play_count = 5

    while not play_count == 0:
        print(f"You have {play_count} PV !")
        player=input("Enter a number : ")
#Verification
        if player.isdigit():
            play_count = play_count-1
            player = int(player)
#Condition
            if player < mystery_number:
                print("Your number is too small !")
            elif player > mystery_number:
                print("Your number is too big !")
#Victory
            else:
                print("YOU WIN !!")
                retry=input("Restart ? y/n : ")
#Restart Victory
                if retry == 'y':
                    mystery_number = random.randint(1,100)
                    retry = True
                    break
                else:
                    retry = False
                    print("-BYE-")
                    break
#ERROR Verification line 16
        else:
            print("ENTER A NUMBER")
#Loose
    if play_count == 0:
        print(f"GAME OVER MYSTERY NUMBER IS {mystery_number}")
        retry = input("Restart ? y/n : ")
#Restart Loose
        if retry == 'y':
            mystery_number = random.randint(1,100)
            retry = True
        else:
            print("-BYE-")
            retry = False
