import random

fichier = "TEST.DAT"

with open(fichier, 'w') as f:
    for x in range(1,random.randint(1,100)):
        fam       = random.randint(1,9)
        fam_pro   = "F%02d" % fam
        desc_fpro = "Famille Produit %02d" % fam
        qte       = random.randint(0,100)
        ligne = "%3s:%-30s:%s\n" % (fam_pro, desc_fpro, qte )
        f.write( ligne )

