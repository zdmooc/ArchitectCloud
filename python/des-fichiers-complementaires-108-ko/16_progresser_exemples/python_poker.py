import random

symbole = [ "Coeur", "Pique", "Carreau", "Trèfle" ]
valeur_carte = [ "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi", "As" ]

suite = []

for n in range(0,9):
    suite.append([ valeur_carte.index(x) for x in valeur_carte[n:n+5] ])

Jeu_52_Cartes = [ (valeur, couleur) for valeur in valeur_carte for couleur in symbole ]

while True:
    melange = []

    paquet = list(Jeu_52_Cartes)

    print("Melange des cartes")
    while paquet:
        melange.append( paquet.pop( paquet.index (random.choice(paquet) ) ) )

    # nb joueurs max(10)
    nb_joueur = 10
    main = []
    for m in range(0, nb_joueur):
        main.append( [] )

    print("distribution des cartes")
    for c in range(0,5):
        for m in range(0, nb_joueur):
            main[m].append(melange.pop())



    for m in range(0, nb_joueur):
        print("Joueur %s : %s " % (m, main[m]) )
        couleur = dict()
        valeur  = dict()
        for c in main[m]:
            ## Couleur
            if c[1] in couleur:
                couleur[c[1]] += 1
            else:
                couleur[c[1]] = 1
            ## Valeur
            if c[0] in valeur:
                valeur[c[0]] += 1
            else:
                valeur[c[0]] = 1
        valeur_main = sorted(valeur.values())
        #print("== > Valeur  = %s " % valeur_main )
        #print("== > Couleur = %s " % couleur )
        ## Pair et double pair
        p = valeur_main.count(2)
        if p == 1:
            print("PAIRE")
        elif p == 2:
            print("DOUBLE PAIRE")
        ## Full et BRELAN
        if valeur_main.count(3) == 1:
            if p == 1:
                print("FULL")
            else:
                print("BRELAN")
        ## Carre 
        if valeur_main.count(4) == 1:
            print("CARRE")

        ## Suite
        v_main = sorted([ valeur_carte.index(x[0]) for x in main[m] ])
        print("V_MAIN = %s " % v_main)
        if v_main in suite:
            q = True
            print("QUINTE")
        ## Flush
        f = 5 in couleur
        if f:
            print("FLUSH")
        ## Suite + Flush
        if f and q:
            print("QUINTE FLUSH")
        print("===============================")
    #v = input("suite")


