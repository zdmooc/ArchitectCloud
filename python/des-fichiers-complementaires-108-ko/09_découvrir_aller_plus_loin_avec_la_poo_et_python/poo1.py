
class BASE(object):
    def qui_suis_je(self):
        return type(self)

class A(BASE):
    pass

class B(BASE):
    pass

class C(BASE):
    pass

class D(BASE):
    pass

def FABRIQUE(C):
    if C == 'A':
        return A()
    elif C == 'B':
        return B()
    elif C == 'C':
        return C()
    elif C == 'D':
        return D()
    else:
        return None

o1 = FABRIQUE('B')
print(o1.qui_suis_je())
o2 = FABRIQUE('D')
print(o2.qui_suis_je())
