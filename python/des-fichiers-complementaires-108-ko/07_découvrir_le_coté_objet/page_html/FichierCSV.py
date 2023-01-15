import Document
import random


class CSV(Document.Document):
    def __init__(self, titre="Page HTML"):
        super().__init__(titre)
        self.contenu = []
        self.separateur = ";"
        self.fin_de_ligne = "\n"

    def __str__(self):
        t = ""
        t += self.titre + self.fin_de_ligne
        ## copie de l'attribut contenu dans une variable temporaire
        tmp = list(self.contenu)

        ## Extraction des entetes
        for e in tmp.pop(0):
            t += "%s" % e
            t += self.separateur
        t += self.fin_de_ligne

        ## Les données
        for l in tmp.pop():
            for d in l:
                t += "%s" % d
                t += self.separateur
            t += self.fin_de_ligne
        return t

    def __repr__(self):
        return "<CSV : %s  : %d >" % (self.titre, id(self))


if __name__ == "__main__":
    P = CSV()
    P.titre = "RESULTAT DES SAUVEGARDES"
    entete = ["Date", "PROD", "RECETTE", "DEV & TEST"]

    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    result = ["Ok", "Erreur", ""]

    Data = []
    for n in range(0, 5):
        d = [
            jours[n],
            random.choice(result),
            random.choice(result),
            random.choice(result),
        ]
        Data.append(d)

    P.contenu.append(entete)
    P.contenu.append(Data)

    print(P)
