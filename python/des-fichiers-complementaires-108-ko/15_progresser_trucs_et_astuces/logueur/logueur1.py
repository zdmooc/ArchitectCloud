
def logueur(function):
    def fonction_interne( *args, **kwargs):
        print("============ LOGUEUR ============")
        print("Fonction : {}".format(function.__name__))
        print("Argument transmis : ")
        print("  args    : {} ".format(args))
        print("  kwargs  : {} ".format(kwargs))
        print("================================")
        return( function(*args, **kwargs) )
    return fonction_interne


@logueur
def test1( a, b ,c):
    print(a, b ,c)

@logueur
def test2(a="?", b="?" , c="?"):
    print(a,b,c)



test1( 1, 2, 3)
test2( a="salut", b="chris")
