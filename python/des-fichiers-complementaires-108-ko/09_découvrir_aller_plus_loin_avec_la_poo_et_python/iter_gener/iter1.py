
class MonRange():
    def __init__(self, debut, fin, pas=1):
        self.etat = None
        self.debut = debut
        self.fin   = fin
        self.pas   = pas

    def __iter__(self):
        print("Fonction Iter ")
        self.etat = self.debut
        return self

    def __next__(self):
        print("Fonction next")
        self.etat += self.pas
        if self.etat > self.fin:
            print(" Stop ")
            raise StopIteration
        return self.etat


def test():
    a = MonRange(0,10,2)
    for i in a:
        print(i)

if __name__ == '__main__':
    test()
