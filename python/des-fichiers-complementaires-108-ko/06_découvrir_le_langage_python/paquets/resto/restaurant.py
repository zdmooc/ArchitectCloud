from libresto import *
from libresto.resto import bouchon_lyonnais as RESTO

nb_pers = clients.arrivée_clients()
print("Arrivée de %s clients" % nb_pers)
print(bienvenue.hello())
places.table(nb_pers)

RESTO.menu()
