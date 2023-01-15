import signal
import os
import time

def alarme(signal, contexte):
    print("Réception du signal no %s " % signal )
    raise OSError("ALARME !!!")

MAX_TIME = 5

signal.signal(signal.SIGALRM, alarme)
signal.alarm(MAX_TIME)

print("Debut du temps d'attente ...")
try:
    time.sleep(15)	# ici le traitement qui ne doit pas excéder
                   # MAXTIME
except:
    pass		# Ici l'interception de l'erreur
			# mais aussi de l'alarme

# sinon on continue
print("Fin du temps d'attente ...")

signal.alarm(0)
