
##
## Boucle while simple
##
import pdb 

compteur = 1

while compteur <= 10:
    print("Compteur : %s " % compteur)
    compteur += 1

pdb.set_trace()
for n in [1,2,3]:
    print(n)

##
## Boucle for
##

f = open("/etc/group")
for l in f.readlines():
    print(l)
f.close()
