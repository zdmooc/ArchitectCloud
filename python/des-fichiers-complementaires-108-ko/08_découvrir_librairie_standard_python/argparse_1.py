
import argparse 

def mon_programme(options):
    print("Mon programme ")
    print("Options : %s " % options )

if __name__ == '__main__':
    ## gestion des arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fichier', help='Nom de fichier' )
    parser.add_argument('-v', '--verbose', help='Mode verbeux', action='store_true' )

    options = parser.parse_args()

    mon_programme(options)
