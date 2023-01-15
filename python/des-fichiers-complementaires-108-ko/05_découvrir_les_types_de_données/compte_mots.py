import string
fichier = "/usr/share/games/fortunes/fortunes"

Mots = {}

with open(fichier) as f:
    lignes=f.readlines()
    for l in lignes:
        for c in string.punctuation:
            if c in l:
                l = l.replace(c, ' ')
        for m in l.split():
            mot = m.lower()
            if mot in Mots:
                Mots[mot] += 1
            else:
                Mots[mot] = 1

for cle, valeur in Mots.items():
    print(" Il y a %s %s dans le texte" % (valeur, cle))
