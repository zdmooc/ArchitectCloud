ENTREE = [
         "Au choix : ",
         "\tSalade Lyonnaise",
         "\tSalade de foie de volaille",
         "\tSalade de museaux",
    ]
PLAT = [ 
            "Au choix : ",
            "\tCoq au vin",
            "\tAndouillette sauc moutarde",
            "\tTablier de sapeur",
            "\tGras double",
        ]
LEGUMES = [
            "Au choix : ",
            "\tGratin Dauphinois",
            "\tHaricot vert",
            "\tBlettes au jus"
        ]
DESSERT = [
            "Au choix Fromage ou Dessert",
            "\tcervelle de canut",
            "\tCrème brulée"
        ]

def menu():
    print(" Notre menu  à 18 euros : \n")

    print("\n Pour commencer nous proposons : \n")
    for plat in ENTREE:
        print( " %s " % plat)

    print("\n Pour la suite : \n")
    for plat in PLAT:
        print( " %s " % plat)

    print("\n Accompagné de  : \n")
    for plat in LEGUMES:
        print( " %s " % plat)

    print("\n Et pour finir ...\n")
    for plat in DESSERT:
        print( " %s " % plat)

if __name__ == '__main__':
    menu()

