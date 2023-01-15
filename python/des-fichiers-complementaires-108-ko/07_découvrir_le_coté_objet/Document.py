class Document():
    def __init__(self):
        self.titre = ""
        self.auteur = ""
        self.date_mise_a_jour = ""
        self.contenu =  ""

    def __str__(self):
        tmp = """
        Document : %s 
        Crée par : %s

        %s

        """ % (self. titre, self.auteur , self.contenu )
        return tmp

if __name__ == '__main__':
    A = Document()
    A.titre = "Mon premier objet"
    A.auteur = "Chris"
    A.contenu = "Ceci est un exemple de class simple"
    print(A)

