##
## Clients : Arrivée d'un nombre aléatoire de clients
## 

import random

def arrivée_clients():
    return random.randrange(1,5)

if __name__ == '__main__':
    print("Arrivée de %s client(s)" % arrivée_client())
