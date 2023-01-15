symbole = [ "Coeur", "Pique", "Carreau", "Trèfle" ]
valeur_carte = [ "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi", "As" ]
 
Jeu_52_Cartes = [ (valeur, couleur) for valeur in valeur_carte for couleur in symbole ]

## Crée une liste avec 52 tuples (valeur, couleur)
print( Jeu_52_Cartes )
