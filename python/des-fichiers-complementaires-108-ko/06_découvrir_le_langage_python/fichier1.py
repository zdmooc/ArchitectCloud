
fichier = "data.txt"

f = open(fichier)

for l in f.readlines():
    print("l=%s" % l, end='')

f.close()
