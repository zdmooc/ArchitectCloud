
from path import Path
import re

d = Path('/proc')

memoire = {}

for p in d.glob('*/stat'):
    if p.isfile():
        with open(p) as f:
            m = re.search(r'^([0-9]*)\s\((.*)\)(.*)$', f.readline())
            pid, comm, le_reste = m.groups()
            data = le_reste.split()
            vsize = int(data[20])/1024
            cle = pid
            if cle in memoire:
                memoire[cle] += vsize
            else:
                memoire[cle] = vsize

p = [ (v,k) for k,v in memoire.items() ]
for v,k in sorted(p):
    if v:
        print("%20s : %10d Kb" %(k,v) )
