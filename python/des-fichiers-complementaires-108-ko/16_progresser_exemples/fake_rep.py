import os
import random
from pathlib import Path
from faker import Faker
fake = Faker('fr_FR')

## Creation d'un fichier avec nom taille et contenu aléatoire
def create_file(rep, taille=1024, max_taille=5):
    ext = random.choice([ "dat", "data", "dbf", "txt", "d" ])
    fname = fake.file_name(extension=ext)
    path = rep / fname
    print("Creation du fichier %s " % path )
    d = []
    with open("/dev/urandom", "rb") as r:
        for x in range(0, random.randint(0,max_taille)):
            b = r.read(taille)
            d.append(b)

    with open(path, "wb") as w:
        for b in d:
            w.write(b)

## retourne un objet Path() avec un nom aleatoire
def create_rep(rep):
    d = Path(fake.file_name() )
    return Path( rep , d.stem )

## Fonction récursive
def cr_niveau(parent, racine):
    niveau = parent + 1

    ## Creation du niveau courant 
    rep_courant = create_rep(racine)
    rep_courant.mkdir()
    print("Creation du repertoire %s " % rep_courant )

    ## Creation de fichier 
    for x in range(0, random.randint(0,max_files)):
        create_file(rep_courant, taille=BLOC, max_taille=MAX_BLOC)

    ## Création d'un niveau supplémentaire ?
    if random.randint(0, 100) > PC_CR_NIVEAU:
        cr_niveau(niveau, rep_courant)

## Création des répertoires top niveau
def create_top_rep(nb):
    for x in range(0, nb):
        cr_niveau(0, ROOT_DIR)


## MAIN 
ROOT_DIR = "a_sauver"
os.system('rm -fr '+ROOT_DIR)

p = Path(ROOT_DIR)
p.mkdir()

max_rep = 5         ## Nb max de repertoire de base
max_files = 5       ## Nb max fichier / rep
MAX_NIVEAU = 3      ## Max niveau d'arborescence
PC_CR_NIVEAU = 40   ## % de creation de niveau (0=toujours 100=jamais)
BLOC=1024*1024      ## Taille de bloc en octets pour la creation de fichiers
MAX_BLOC=5          ## Taille max des fichiers en nb de bloc

## Creation des répertoires TOP NIVEAU
create_top_rep( random.randint(1, max_rep) )
