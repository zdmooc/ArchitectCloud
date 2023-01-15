import re
from path import Path
import matplotlib.pyplot as plt

dir_base = '/var/log/sysstat' # debian ubuntu
dir_base = '/var/log/sa'      # RedHat
dir_base = 'sar_data'
### Modifier le nom des machines ###

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
                    t = d[0][0:2]
                    pcu = 100 - int(float(d[-1].replace(',','.')))
                    cle = f.basename()
                    if cle in data:
                        data[cle][0].append(t)
                        data[cle][1].append(pcu)
                    else:
                        data[cle] = [ [t], [pcu] ]
## affichage en mode graphique
moyenne = {}
for cle in data.keys():
    #print( "==== %s ====" % cle )
    #print("time : ", data[cle][0])
    #print("%cpu : ", data[cle][1])
    for i,c in enumerate(data[cle][0]):
        h = data[cle][0][i]
        v = data[cle][1][i]
        if h in moyenne:
            t_v, t_nb = moyenne[h]
            moyenne[h] = ( t_v + v, t_nb+1 )
        else:
            moyenne[h] = (v,1)

for m in moyenne.keys():
    t_v, t_nb = moyenne[m]
    moyenne[m] = ( t_v, t_nb, round(t_v/t_nb))
    #print( "Moyenne : %s / %s " % (m,moyenne[m]))

for cle in data.keys():
    x = data[cle][0]
    y = data[cle][1]
    plt.plot(x,y, '.b', markersize=3)
for cle in moyenne.keys():
    x = cle
    y = moyenne[cle][2]
    plt.plot(x, y, 'or', markersize=10)
plt.gcf().autofmt_xdate()
plt.show()

