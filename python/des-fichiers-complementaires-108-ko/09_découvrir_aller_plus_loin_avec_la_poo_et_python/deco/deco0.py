def mon_deco(fonction):
    return fonction

@mon_deco
def fonction1():
    print("Je suis la fonction 1 ")

@mon_deco
def fonction2():
    print("Je suis la fonction 2 ")

@mon_deco
def fonction3():
    print("Je suis la fonction 3 ")


fonction1()
fonction2()
fonction3()
fonction1()
