## ----------------------------
## Generation d'un table en pug
## ----------------------------

TAB="\t"

def entete():
    print('table(class="table table-over")')

def read_data():
    data = [
            [ 'Description', 'Lien' ],
            [ 'Environnement de Production', 'http://prod', "PROD" ],
            [ 'Environnement de Pre Production', 'http://preprod', "PREPROD" ],
            [ 'Environnement de Test', 'http://test', "TEST & DEV" ],
            ]
    return data

def thead( libel ):
    print(TAB+'thead(class="thead-light")')
    print(TAB*2+'tr')
    for l in libel:
        print(TAB*3+"th %s" % l)

def tbody( data ):
    print(TAB+"tbody")
    for desc, lien, l_bouton in data:
        print(TAB+"tr")
        print(TAB*2+"td %s " % desc)
        print(TAB*2+"td")
        print(TAB*3+'a(class="btn btn-info" href="%s") %s' % (lien, l_bouton))

def main():
    entete()
    data = read_data()
    headers = data.pop(0)
    thead( headers )
    tbody( data )

if __name__ == '__main__':
    main()
