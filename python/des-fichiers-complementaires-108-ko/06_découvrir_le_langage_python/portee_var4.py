
def fonction():
    global a
    a = 12
    print(" La variable dans la fonction a = {}".format(a) )


a = 5
fonction()
print(" La variable a = {}".format(a) )
a="DEUX"
fonction()
print(" La variable a = {}".format(a) )
