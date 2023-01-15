import random

nombre_au_hasard = random.randint(1,5)

TROUVE = False
nombre_essai = 0

while not TROUVE:

    essai = input("Tapez un nombre de 1 à 5 : ")

    if int(essai) == nombre_au_hasard:
        print("\n Trouvé !")
        TROUVE = True
    else:
        print("\n Désolé ...\n")

    nombre_essai += 1

print("\n Bravo vous avez trouve en %s essai(s)" % nombre_essai )
