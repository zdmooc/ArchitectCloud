def ma_fonction(nom):
    return "Bonjour depuis mon module : {}".format(nom)

if __name__ == '__main__':
    ## Test local
    print( ma_fonction(" TOTO ") )
