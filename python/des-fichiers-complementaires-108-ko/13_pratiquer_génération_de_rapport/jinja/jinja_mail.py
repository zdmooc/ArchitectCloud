from jinja2 import Template
import random
import datetime

tmpl = """

Le {{ data.date_jour }}

Un fichier : {{ data.fichier }} est arrivé 

Il contient {{ data.enregs }} enregistrements

Voici la répartition : 

Pro | Description                    | Nbr  | Qte
===================================================
{%- for l in data.lignes %}
{{ l.fam_pro }} | {{ l.desc_fpro }} | {{ "%4d" % l.nb_fpro}} | {{ "%4d" % l.qte_fpro}}
{%- endfor %}
===================================================
                       Total         | {{ "%4d" % data.total}} | {{"%4d" % data.totqt}}

Cordialement
Votre serveur bien aimé

"""

date_jour = datetime.datetime.now().strftime("%x à %X")
fichier =  "TEST.DAT"

## Lecture du fichier en mode slurp
with open(fichier) as f:
    ligs = f.readlines()

FAM = {}

enregs = len(ligs)

for l in ligs:
    l = l.rstrip()
    f, d, q = l.split(':')
    q = int(q)
    if f in FAM:
        FAM[f] = ( FAM[f][0], FAM[f][1]+q , FAM[f][2]+1)
    else:
        FAM[f] = (d, q, 1)

lignes = []
total = 0
totqt = 0
for x in sorted(FAM):
    total += FAM[x][1]
    totqt += FAM[x][2]
    lignes.append( { 
        'fam_pro'   : x,
        'desc_fpro' : FAM[x][0],
        'nb_fpro'   : FAM[x][1],
        'qte_fpro'  : FAM[x][2],
        } )

T = Template( tmpl )

print(T.render( data={ 
        'date_jour': date_jour,
        'fichier': fichier,
        'total': total,
        'totqt': totqt,
        'enregs': enregs,
        'lignes': lignes,
        }
        )
        )
