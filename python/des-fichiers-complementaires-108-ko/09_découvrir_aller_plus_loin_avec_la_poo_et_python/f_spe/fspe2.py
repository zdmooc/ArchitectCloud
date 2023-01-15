
class A(object):

    def __init__(self):
        self.ingredients = []
        self.status = None

    def __gt__(self, other):
        self.status = other
        return self

    def __add__(self, other):
        self.ingredients.append(other)
        return self

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
    soupe += "carotte"
    soupe += "Potiron"
    soupe += "Patate"
    soupe > "Mouliné"
    print(soupe.nom)

    soupe = A()
    soupe += "carotte"
    soupe > "Consommé"
    print(soupe.nom)

    soupe = A()
    soupe += "potiron"
    print(soupe.nom)



