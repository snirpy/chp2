continuer = True
while continuer:
    moyenne = input("Entrer votre moyenne: ")
    try:
        moyenne = int(moyenne)
    except:
        print("Vous n'avez pas saisi une valeur numérique")
       
    else:
        if moyenne < 0 :
            print("La moyenne ne peut être négative!")
            
        elif moyenne > 20:
            print("La moyenne ne peut être supériure à 20!")
            
        else:
            if moyenne >= 18:
                print(f"Excellent! Vous avez eu {moyenne} de moyenne")
            elif 14 <= moyenne < 18:
                print(f"Très bien! Vous avez eu {moyenne} de moyenne")
            elif 10 <= moyenne < 14:
                print(f"Assez bien! Vous avez eu {moyenne} de moyenne")
            elif 5 <= moyenne < 10:
                print(f"Insuffisant! Vous avez eu {moyenne} de moyenne")
            elif moyenne < 5:
                print(f"Catastrophique! Vous avez eu {moyenne} de moyenne")
            continuer = False
            

