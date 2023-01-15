
def f1( **kwargs ):
    print("Voici la liste des arguments :" )
    for n,(cle, valeur) in enumerate(kwargs.items()):
        print("argument no %s : clé=%s / valeur=%s" % (n, cle, valeur))

dico = {
         "arg1" : 1,
         "arg2" : "deux",
         "arg3" : [ 'trois' ],
         "arg4" : 4.0
        }

f1(**dico)
