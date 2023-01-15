
def f1( *args, **kwargs ):
    if kwargs:
        print("Voici la liste des arguments (kwargs) :" )
        for n,(cle, valeur) in enumerate(kwargs.items()):
            print("argument no %s : clé=%s / valeur=%s" % (n, cle, valeur))
    if args:
        print("Voici la liste des arguments (args) :" )
        for n,a in enumerate(args):
            print("argument no %s : %s" % (n, a))


print("=> Les arguments en liste")
f1( 1,2,3 )

print("=> Les arguments en dictionnaire")
f1( arg1=1, arg2=2, arg3=3 )


print("=> Les 2 en même temps !!!")
f1( 1,2,3, arg1=1, arg2=2, arg3=3 )
