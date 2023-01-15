# ========================
# Affectation d'un table
# ========================

# Type de table
P2 = 2
P4 = 4
P6 = 6
P8 = 8

# Type de Salle
SALLE1 = 1
TERRASSE = 9

## Les tables un simple dictionnaire avec le no comme clé et 
## les caractéristiques nombre de place, salle dans un tuple
TABLES = {
        1: (P2, TERRASSE),
        2: (P2, TERRASSE),
        3: (P4, TERRASSE),
        4: (P4, TERRASSE),
        5: (P6, TERRASSE),
        6: (P8, TERRASSE),

        11: (P2, SALLE1),
        12: (P2, SALLE1),
        13: (P4, SALLE1),
        14: (P4, SALLE1),
        15: (P6, SALLE1),
        16: (P8, SALLE1),

        }

## Trouve une table pour n personnes
def trouve_table( nb_pers ):

    for c, t in TABLES.items():
        if nb_pers <= t[0]:
            return c

## affichage du résultat
def table(nb_pers):
    t = trouve_table(nb_pers)

    if t:
        print(" Trouve table No %s en " % t, end='')
        if TABLES[t][1] == TERRASSE:
            print("en Terrasse")
        elif TABLES[t][1] == SALLE1:
            print("dans la salle no 1")

if __name__ == '__main__':
    table(2)
