
import os
import tempfile
import glob
from path import Path   ## il faut lancer pip install path.py

def create_dir(d_base, nom):
    d = os.path.join( d_base, nom)
    os.mkdir(d)
    return d

def create_fic( rep, nom ):
    fichier = os.path.join( rep, nom )
    with open(fichier, 'w+') as fic:
        fic.write( "fichier : %s \n" % nom )


with tempfile.TemporaryDirectory() as dir_base:
    ## creons des répertoires
    rep = []
    rep.append( create_dir(dir_base, 'DIR1') )
    rep.append( create_dir(dir_base, 'DIR2') )
    rep.append( create_dir(dir_base, 'DIR3') )

    # puis des fichiers 
    fic = []
    fic.append( create_fic(rep[0], "fichier1" ) )
    fic.append( create_fic(rep[1], "fichier2" ) )
    fic.append( create_fic(rep[1], "fichier2_1" ) )
    fic.append( create_fic(rep[1], "fichier2_2" ) )
    fic.append( create_fic(rep[2], "fichier3" ) )
    fic.append( create_fic(rep[2], "fichier3_1" ) )
    fic.append( create_fic(rep[2], "fichier3_2" ) )
    fic.append( create_fic(rep[2], "fichier3_3" ) )

    # et des sous répertoires
    srep = []
    srep.append( create_dir(rep[1], 'SDIR1') )
    srep.append( create_dir(rep[1], 'SDIR2') )
    srep.append( create_dir(rep[1], 'SDIR3') )

    fic.append( create_fic(srep[0], "sfichier1" ) )
    fic.append( create_fic(srep[1], "sfichier2" ) )


    print("=== Parcours avec os.walk ===")
    for l in os.walk( dir_base ):
        print( l )

    print("=== parcours avec glob ===")
    for l in glob.glob( dir_base+'/**', recursive=True):
        print(l)

    print("=== Parcours avec path ===")
    for l in Path(dir_base).walkfiles():
        print(l)
