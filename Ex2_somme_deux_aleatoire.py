from random import randint

nb1 = randint(1,10)
nb2 = randint(1,10)

print(nb1,nb2,sep="---")

quitter = "a"
while not quitter == "q":
    somme =input("Calculer la somme des deux nombres {} et {} : ".format(nb1,nb2))
    try:
        somme = int(somme)
    except:
        print("Vous n'avez pas saisi une valeur numérique")
        somme = 0
    else:
        if somme < 0 :
            print("La somme ne peut être négative!")
            somme = 0
        else:
            if somme == nb1 +nb2:
                print("Bravo! {} + {} = {} ".format(nb1,nb2,nb1+nb2))
                quitter = "q"
            else:
                print("Faux")
                quitter = input("Taper 'Q' pour quitter ou enter pour continuer :")
