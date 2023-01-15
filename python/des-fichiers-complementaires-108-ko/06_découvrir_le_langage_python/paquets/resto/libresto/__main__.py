from libresto import *

def choix_resto():
    print("""
    1 - Fast Food
    2 - Salade Bar
    3 - Bouchon Lyonnais

    """)
    r = input("Votre choix : ")
    return r

r = int(choix_resto())

if r == 1:
    from libresto.resto import fast_food as RESTO
elif r == 2:
    from libresto.resto import salade_bar as RESTO
else:
    from libresto.resto import bouchon_lyonnais as RESTO

nb_pers = clients.arrivée_clients()
print("Arrivée de %s clients" % nb_pers)
print(bienvenue.hello())
places.table(nb_pers)

RESTO.menu()
