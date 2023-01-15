import re
from path import Path
import matplotlib.pyplot as plt

dir_base = '/var/log/sysstat'

data = {}

STORE=False

### recuperation des données
for f in Path(dir_base).glob('sar*'):
    with open(f) as fic:
        ligs = fic.readlines()
        for l in ligs:
            d = re.findall( r'\S+', l)
            if '%idle' in d:
                STORE = True
                continue
            if 'Moyenne' in d:
                STORE = False
                continue
            if STORE:
                if 'all' in d:
                    t = d[0]
                    pcu = 100 - int(float(d[-1].replace(',','.')))
                    cle = f.basename()
                    if cle in data:
                        data[cle][0].append(t)
                        data[cle][1].append(pcu)
                    else:
                        data[cle] = [ [t], [pcu] ]
    break  # un seul fichier

## affichage en mode graphique
cle = list(data.keys())[0]
x = data[cle][0]
y = data[cle][1]
plt.plot(x,y)
## Suppression des libellés sur l'axe X sinon illisible
plt.xticks([],[])
plt.show()

