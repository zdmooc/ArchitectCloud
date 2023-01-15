import random

import pudb

symbole = [ "Coeur", "Pique", "Carreau", "Trèfle" ]
valeur_carte = [ "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi", "As" ]

Jeu_52_Cartes = [ (valeur, couleur) for valeur in valeur_carte for couleur in symbole ]

melange = []

paquet = list(Jeu_52_Cartes)

print("Melange des cartes")
while paquet:
    melange.append( paquet.pop( paquet.index (random.choice(paquet) ) ) )


print("Distribution")
j1 = []
j2 = []
while melange:
    j1.append( melange.pop() )
    j2.append( melange.pop() )

tmp = []

#pudb.set_trace()

while j1 and j2:
    c1 = j1.pop(0)
    c2 = j2.pop(0)
    v_c1 = valeur_carte.index( c1[0] )
    v_c2 = valeur_carte.index( c2[0] )
    print( "j1 %25s / j2 %25s = " % (c1, c2), end='')
    if v_c1 > v_c2:
        print("J1 Gagne ", end='')
        j1.extend( [c1, c2] )
        if tmp:
            j1.extend( tmp )
            tmp = []
    elif v_c1 < v_c2:
        print("J2 Gagne ", end='')
        j2.extend( [c1, c2] )
        if tmp:
            j2.extend( tmp )
            tmp = []
    else:
        print("BATAILLE ", end='')
        tmp = [c1, c2, j1.pop(0), j2.pop(0)]
        print(tmp, end='')
    print(" Paquets : %02d / %02d " % ( len(j1), len(j2) ))
    #print(j1, j2)

## FIN DE LA PARTIE
if j1:
    print(" J1 GAGNE LA PARTIE")
if j2:
    print(" J2 GAGNE LA PARTIE")
