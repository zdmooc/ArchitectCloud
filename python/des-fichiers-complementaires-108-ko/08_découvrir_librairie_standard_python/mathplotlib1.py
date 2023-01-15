import matplotlib.pyplot as plt
import random

data = [ random.randint(5, 25) for x in range(0,20) ]

plt.title(" Données Aléatoires")
plt.plot(data)
plt.ylabel('Label axe des Y')
plt.xlabel('Label axe des X')
plt.show()
