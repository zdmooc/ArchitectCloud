
try:
    raise NameError(" Mon Texte ...")
except NameError as err:
    print("Erreur de nom : %s " % err )
    raise
