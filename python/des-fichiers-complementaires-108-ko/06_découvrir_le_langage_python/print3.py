contacts = [
        { "prénom" : "Dark", "nom" : "Vador" },
        { "prénom" : "Luke", "nom" : "Skywalker" },
        { "prénom" : "Han", "nom" : "Solo" },
        ]

for num, contact in enumerate(contacts):
    print( "{num:05d}|{contact[prénom]:15s}|{contact[nom]:15s}" .format( num=num, contact=contact))
