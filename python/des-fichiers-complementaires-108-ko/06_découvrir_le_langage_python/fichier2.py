
fichier = "data.txt"

f = open(fichier, "w")

for n in range(1, 6):
    f.write("Ligne No %s du fichier\n" % n)

f.close()
