
class MonException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__ (self):
        return "MonException msg=%s" % self.message


try:
    print("Avant l'erreur")
    raise MonException("MESSAGE D'ERREUR")
    print("Apres l'erreur")
except MonException as err:
    print("Erreur : [%s]" % err )


