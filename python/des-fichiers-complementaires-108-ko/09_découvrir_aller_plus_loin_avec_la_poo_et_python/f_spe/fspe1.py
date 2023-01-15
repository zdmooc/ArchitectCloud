
class A(object):

    def __init__(self):
        self.ingredients = []
        self.status = None

    def __getattribute__(self, attr):
        __dict__ = object.__getattribute__(self, '__dict__')
        if attr in __dict__:
            return object.__getattribute__(self, attr)
        else:
            if attr == 'nom':
                if self.status:
                    s = self.status
                else:
                    s = "Soupe"
                if len(self.ingredients) > 1:
                    s += " de "
                    s += " ,".join(self.ingredients[:-1])
                    s += " et de "+self.ingredients[-1]
                elif len(self.ingredients) == 1:
                    s += " de "+self.ingredients[0]
                return s


if __name__ == '__main__':
    soupe = A()
    soupe.ingredients.append("Potiron")
    soupe.ingredients.append("Carotte")
    soupe.ingredients.append("Patate")
    soupe.status = "Mouliné"
    print(soupe.nom)

    soupe = A()
    soupe.ingredients.append("Carotte")
    soupe.ingredients.append("Potiron")
    soupe.status = "Consommé"
    print(soupe.nom)

    soupe = A()
    soupe.ingredients.append("Carotte")
    print(soupe.nom)



