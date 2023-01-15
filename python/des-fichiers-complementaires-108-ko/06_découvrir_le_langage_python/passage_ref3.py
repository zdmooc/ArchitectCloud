
def f1( arg1 ):
    arg1.append("UN")
    return arg1

a = [1,2,3,4]
b = f1(a[:])
print("Apres la fonction a = ", a)
print("Apres la fonction b = ", b)
