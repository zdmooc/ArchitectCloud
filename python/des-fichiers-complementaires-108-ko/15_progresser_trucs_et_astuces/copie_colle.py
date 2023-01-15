##
## Modifie le copie coller 
## pour passer d'un tableau scalc a un wiki
## Idee originale de JC Plat

import clipboard

## on recupére les données du clipboard
data = clipboard.paste()

## on les traite
tmp = data.split('\n')

entete = tmp.pop(0).split('\t')

tmp_data = [ '^'+x for x in entete ]+['^']

new_data = '\t'.join(tmp_data)+'\n'

for l in tmp:
    d = l.split('\t')
    tmp_data = [ '|'+x for x in d ]+['|']
    new_data += '\t'.join(tmp_data)+'\n'

# on remet dans le clipboard
clipboard.copy(new_data)
