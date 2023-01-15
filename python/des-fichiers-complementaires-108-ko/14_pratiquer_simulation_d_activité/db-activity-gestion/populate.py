from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Client, Produit, Fourn, Stock, Compteur
import datetime
import random

from faker import Faker
fake = Faker('fr_FR')
import FakeProduit

## -------------------------
## Creation de la session
## -------------------------
 
engine = create_engine(BASE_NAME)
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

## ------------------------
## Creation des Compteurs 
## ------------------------
def compteurs():
    r = Compteur()
    r.nom = "FACTURE"
    r.val = 1
    session.add(r)

    r = Compteur()
    r.nom = "COMCLI"
    r.val = 1
    session.add(r)

    r = Compteur()
    r.nom = "COMFOU"
    r.val = 1
    session.add(r)
    session.commit()

## ---------------------
## Creation des clients
## ---------------------
def clients(nb):
    for c in range(1,nb):
        r = Client()
        t = random.choice( [ 'Ets', 'Sté' ] )
        r.nom = "%s %s" % (t, fake.company())
        print("Creation Client de %s " % r.nom)
        session.add(r)
        try:
            session.commit()
        except:
            session.rollback()

#Fourn
def fourn(nb):
    for c in range(1,nb):
        r = Fourn()
        t = random.choice( [ 'Ets', 'Sté' ] )
        #r.delai = random.randint(5, 30)
        ## pour test reappro
        r.delai = 0
        r.nom = "%s %s" % (t, fake.company())
        print("Creation Fou de %s " % r.nom)
        session.add(r)
        try:
            session.commit()
        except:
            session.rollback()


#Produit
def produits(nb):
    ## Preparation des produits
    FakeProduit.init()
    for c in range(1,nb):
        r = Produit()
        fp = FakeProduit.genere()
        r.desig = fp.desig
        r.prix = fp.prix
        print("Creation de %s " % r.desig)
        session.add(r)
        try:
            session.commit()
        except:
            session.rollback()


#Stock
def stock( depot ):
    prods = session.query(Produit).all()
    for p in prods:
        r = Stock()
        r.depot = depot
        r.produit = p
        r.qstock = 10000
        print("Creation de %s/%s " % (r.depot,p.desig))
        session.add(r)
        try:
            session.commit()
        except:
            session.rollback()

def main():
    compteurs()
    clients(10)
    fourn(10)
    produits(10)
    stock('D1')

if __name__ == '__main__':
    main()
