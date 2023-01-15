class Couleur:
    def __init__(self, r, v, b):
        self.rouge = r
        self.vert  = v
        self.bleu  = b

    def __str__(self):
        return "Couleur"+str((self.rouge, self.vert, self.bleu))

    @staticmethod
    def blanc():
        return Couleur(255, 255, 255)

    @staticmethod
    def noir():
        return Couleur(0, 0, 0)


c = Couleur.blanc()
print(c)                # affiche (255, 255, 255)
c = Couleur.noir()
print(c)                # affiche (0, 0, 0)
