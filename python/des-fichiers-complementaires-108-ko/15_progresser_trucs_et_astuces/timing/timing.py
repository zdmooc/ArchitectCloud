import time

## ---------------
## Classe Timing
## ---------------
class timing():
    def __init__(self, label="timing"): 
        self.debut = 0
        self.label = label
    
    def _pr(self, libelle):
        print( libelle )

    def tps_intermediaire(self, l_inter=""):
        if not l_inter:
            l_inter = self.label
        self._pr("Temps intermediaire {label:s} timing {temps:.3f}".format(label=l_inter, temps=time.time() - self.debut))

    def __enter__(self):
        self.debut = time.time()
        self._pr("Debut de %s " % self.label)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._pr("Fin de {label:s} timing {temps:.3f}".format(label=self.label, temps=time.time() - self.debut))

def test():
    import math
    with timing(label="Fonction math.sin") as t:
        for x in range(1, 500000):
            if not x % 100000:
                t.tps_intermediaire()
            y = math.sin(x)

if __name__ == "__main__":
    test()
