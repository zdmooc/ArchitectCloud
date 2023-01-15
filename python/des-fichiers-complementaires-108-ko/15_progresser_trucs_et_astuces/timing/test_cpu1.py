import time

debut = time.time()

num_mul = 50_000_000 #environ 15s
data = range(2*num_mul)
nombre = 0

for i in data:
    nombre *= 1.0000001

fin = time.time()

print("Resultat = {}".format(nombre))
print("Temps = {}".format(fin - debut))
