from datetime import datetime
import random


class Document:
    def __init__(self, titre="Titre du document", auteur="root"):
        self.titre = titre
        self.auteur = auteur
        self.date_creation = datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
        self.contenu = None

    def retourne_contenu(self):
        if self.contenu == None:
            t = "<VIDE>"
        elif type(self.contenu) is str:
            t = self.contenu
        elif type(self.contenu) is list:
            t = "\n".join(self.contenu)
        return t

    def __str__(self):
        t = """
Titre : %s

%s

Creé le : %s par %s

        """ % (
            self.titre,
            self.retourne_contenu(),
            self.date_creation,
            self.auteur,
        )
        return t

    def __repr__(self):
        return "<Document : %s  : %d >" % (self.titre, id(self))


if __name__ == "__main__":

    D = Document("Resultat des sauvegardes de la semaine", "root")
    D.contenu = []
    fmt_ligne = "%10s %10s %10s %10s"
    entete = fmt_ligne % ("Date", "PROD", "RECETTE", "DEV & TEST")
    D.contenu.append(entete)
    ligne = "-" * len(entete)
    D.contenu.append(ligne)

    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    result = ["Ok", "Erreur", "<VIDE>"]

    for n in range(0, 5):
        ligne = fmt_ligne % (
            jours[n],
            random.choice(result),
            random.choice(result),
            random.choice(result),
        )
        D.contenu.append(ligne)
    print(D)
