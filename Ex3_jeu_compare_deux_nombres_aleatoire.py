from random import randint

essai = 0
continuer = "o"

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
    