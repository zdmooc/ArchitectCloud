
def f1( *args ):
    print("Voici la liste des arguments :" )
    for n,a in enumerate(args):
        print("argument no %s : %s" % (n, a))


liste = [ 1, "deux", [ 't','r','o','i','s' ], 4.0 ]
f1( *liste )
