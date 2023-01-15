import random

## Creation d'un paquet de 32 cartes
paquet = [x for x in range(1, 32)]

melange = []


print(paquet)

while paquet:
    melange.append(
            paquet.pop(
                paquet.index(
                    random.choice(paquet)
                    )
                )
            )

print(melange)
