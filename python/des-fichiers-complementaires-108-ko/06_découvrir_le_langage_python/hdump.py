#! /home/chris/.virtualenvs/lps/bin/python
## ----------------------------------
## HDUMP dump d'un fichier en hexa
## ----------------------------------

import os
import sys
import string

BUFFER = 32

## ----------------------
## Affichage de l'usage
## ----------------------
def usage():
    u = """usage: %s nom_de_fichier
    """
    print( u % sys.argv[0])

## --------------------------------------------
## Lecture et affichage du fichier en mode hexa
## --------------------------------------------
def hdump(fichier):
    EOF = False
    nol = 0
    f = open(fichier, 'rb')
    while not EOF:
        record = f.read(BUFFER)
        if len(record) != BUFFER:
            EOF = True
        nol += 1
        print("%03d | " % nol, end='')
        for c in record:
            print("%02X " % c, end='')
        if EOF:
            for n in range(0, BUFFER - len(record)):
                print('   ', end='')
        print(" | ", end='')
        for c in record:
            if chr(c) in string.whitespace:
                print(' ', end='')
            elif chr(c) in string.printable:
                print(chr(c), end='')
            else:
                print('.', end='')
        print()

    f.close()


## ------------
## HDUMP MAIN
## ------------

if __name__ == '__main__':
    if len(sys.argv)==2:
        fichier = sys.argv[1]
        if os.path.exists(fichier):
            hdump(fichier)
        else:
            print("Fichier inexistant : %s" % fichier)
            usage()
    else:
        print("nom de fichier : argument obligatoire")
        usage()
