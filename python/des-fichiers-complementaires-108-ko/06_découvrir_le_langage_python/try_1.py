
OK = False

while not OK:
    try:
        n = int(input("Entrez un nombre : "))
        OK = True
    except ValueError:
        print(" Erreur de type ... ")
    else:
        print("Clause Else")
    finally:
        print("Clause Finally")

print("Sortie de la boucle")
