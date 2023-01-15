t1 = (1, 2, 3, 4, 5)
t2 = ('a','b','c', 'd', 'e')
t3 = (100, 200, 300, 400, 500)

liste_de_liste = [ t1, t2, t3 ]

print(" v1 |  v2 |  v3 |  v4 |  v5  " )
print("=============================" )
for v1, v2, v3, v4, v5 in liste_de_liste:
    print( "%3s | %3s | %3s | %3s | %3s " % (v1, v2,v3,v4,v5))

print()

print("Nb | v1  |  v2 |  v3 |  v4 |  v5  " )
print("=================================" )
for nb, (v1, v2, v3, v4, v5) in enumerate(liste_de_liste):
    print( "%2s | %3s | %3s | %3s | %3s | %3s " % (nb, v1, v2,v3,v4,v5))

