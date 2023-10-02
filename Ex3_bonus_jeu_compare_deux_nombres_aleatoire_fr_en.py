from random import randint

essai = 0
continuer = "o"
langue =""
while langue =="":
    langue = input("Taper fr pour le français/ Tape en for English: ")
    if langue == "fr":
        while  continuer == "o":
            print("\ntirage des deux nombres")
            nb1 = randint(1,20)
            nb2 = randint(1,20)
            essai += 1
            if nb1 == nb2:
                print(f"\nBravo! Vous avez gagné au bout de {essai} essai(s).")
                break
            else:
                print("Nombre d'essais : %d"%(essai))
                print("Vous avez perdu")

            continuer = input("\nTaper 'o' pour continer ou autre pour quitter: ")
    elif langue == "en":
        while  continuer == "o":
            print("\nDraw of the two numbers")
            nb1 = randint(1,20)
            nb2 = randint(1,20)
            essai += 1
            if nb1 == nb2:
                print(f"\nWell done! You won after  {essai} trying.")
                break
            else:
                print("Number of trials : %d"%(essai))
                print("You lost")

            continuer = input("\nType 'o' to continue or other to quit: ")
