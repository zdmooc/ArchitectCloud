

contacts = [
        { "prénom" : "Dark", "nom" : "Vador" },
        { "prénom" : "Luke", "nom" : "Skywalker" },
        { "prénom" : "Han", "nom" : "Solo" },
        ]

for num, contact in enumerate(contacts):
    contact['num'] = num
    print( "%(num)05d | %(nom)20s | %(prénom)20s |" % contact)
