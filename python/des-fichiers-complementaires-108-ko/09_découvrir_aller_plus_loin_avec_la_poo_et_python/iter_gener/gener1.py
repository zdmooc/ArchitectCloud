
def MonRange(debut, fin, pas=1):
    i = debut
    while i < fin:
        i += pas
        yield i


def test():
    for i in MonRange(0,10):
        print(i)

if __name__ == '__main__':
    test()
