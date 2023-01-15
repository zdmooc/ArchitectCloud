
import signal
import sys

def interruption(signal, contexte):
    print("Fermeture suite à CTRL-C")
    sys.exit(0)

signal.signal(signal.SIGINT, interruption)

print("Début de la boucle infinie ...")
while True:
    pass
