
class A(object):

    def __init__(self):
        self.ingredients = []
        self.status = None

    def __getattr__(self, attr):
        if attr == 'nom':
            return "Je fais ce que je veux avec nom"
        else:
            return "Inexistant"


if __name__ == '__main__':
    soupe = A()
    print("soupe.nom = ", soupe.nom)
    print("soupe.inexistant = ", soupe.inexistant)



