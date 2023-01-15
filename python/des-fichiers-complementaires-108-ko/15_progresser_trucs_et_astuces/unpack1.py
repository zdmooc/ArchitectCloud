

liste = [ 
    list(range(0,10)),
    list(range(0,6)),
    list(range(0,12)),
    ]

print(liste)

for x,*y,z in liste:
    print( "x=", x)
    print( "y=", y)
    print( "z=", z)
