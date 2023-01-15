import multiprocessing as mp
import random
import time

# Définition d'un canal de communication
output = mp.Queue()

# Fonction example avec temps d'attente + génération de nombre aléatoire
def fonction(temps, output):
    time.sleep(temps)
    data = [ random.randint(0,100) for x in range(1,1000) ]
    total = sum(data)
    output.put(total)

# Creation d'un liste de processus
processes = [mp.Process(target=fonction, args=(5, output)) for x in range(4)]

# lancement des processus
for p in processes:
    p.start()

# Fermeture des processus
for p in processes:
    p.join()

# Recuperation des données
results = [output.get() for p in processes]

print(results)

