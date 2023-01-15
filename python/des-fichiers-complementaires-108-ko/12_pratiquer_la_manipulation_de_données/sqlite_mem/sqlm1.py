## -------------
## SQLITE MEMORY
## -------------

from sqlalchemy import select, func
from definitions import connect
from definitions import Produit

from openff import get_prod

import csv

## ----------------------
## Remplissage de la BDD
## ----------------------
def populate(session, data):
    for r in data:
        p = Produit()
        code, nom, qte, marque, nutri, generic = r
        p.code = code
        p.nom = nom
        p.qte = qte
        p.marque = marque
        p.code_nutri = nutri
        p.nom_generique = generic
        session.add(p)
    session.commit()

## ------------------------
## Utilisation des données
## ------------------------
def generate_all(session, fichier):
    s = select([Produit])
    prods = session.execute(s)
    with open(fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(prods)

def generate_marque(session, fichier):
    req = """
    select marque, count(*) from PRODUITS
    group by marque
    order by marque
    """
    prods = session.execute(req)
    with open(fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(prods)



## --------------------------
## Le traitement principal
## --------------------------
def main():
    session = connect()         # Creation + Init BDD
    print("Recup des données")
    data = get_prod()           # Recuperation de des données
    print("Transfert BDD")
    populate(session, data)     # Remplissage BDD
    print("Fichier : PRODUITS")
    fic = "PRODUITS.csv"
    generate_all(session, fic)  # Utilisation de la base de données
    print("Fichier : MARQUES")
    fic = "MARQUES.csv"
    generate_marque(session, fic)
    session.close()             # Fermeture Session + BDD

if __name__ == '__main__':
    main()
