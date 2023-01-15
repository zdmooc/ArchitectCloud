##
##
def pc(montant, total):
    assert total > 0, 'total doit être strictement positif'
    assert 0 <= montant, 'montant doit être positif'
    assert montant <= total, 'montant doit être inférieur à total'
    return (montant / total) * 100



if __name__ == '__main__':
    print( "=> %3.2f%%" % pc(15, 100))
    print( "=> %3.2f%%" % pc(35, 67))
    print( "=> %3.2f%%" % pc(23, 124))
    print( "=> %3.2f%%" % pc(7, 0))

