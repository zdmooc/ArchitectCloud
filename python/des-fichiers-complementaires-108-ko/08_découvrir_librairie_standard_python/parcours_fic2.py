
from path import Path   ## il faut lancer pip install path.py

p = Path('/') / 'etc'
print('Parcours de %s ' % p)
for l in p.walkfiles(errors='ignore'):
    print(l)
