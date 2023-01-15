## -------------------------------------
## DECLARATIONS DE LA BASE DE DONNEES
## -------------------------------------

import os
import sys
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

## Définitions de la base de données
Base = declarative_base()

#SQLITE_FILE_NAME = "data.dbf"
SQLITE_FILE_NAME = ":memory:"
BASE_NAME = 'sqlite:///'+SQLITE_FILE_NAME

## Declarations des classes 
class BASE_TABLE():
    " Classe commune a toute les autres"
    id = Column(Integer, primary_key=True)
    d_cre = Column(DateTime, default = datetime.datetime.now() )
    #d_mod = Column(DateTime, default = datetime.datetime.now(), onupdate=datetime.datetime.now() )
    #status = Column(String(5), default = "OK", nullable = False )

class Produit(Base, BASE_TABLE):
    "Les produits"
    __tablename__ = 'PRODUITS'
    code           = Column(String(20), nullable=False)
    nom            = Column(String(50), nullable=False)
    qte            = Column(String(20), default='')
    marque         = Column(String(20), default='')
    code_nutri     = Column(String(5), default='')
    nom_generique  = Column(String(50), default='')

def init_db():
    ## Creation d'un moteur 
    ## Pour la creation du schema
    engine = create_engine(BASE_NAME, echo=False)
     
    ## Si ce n'est pas fait alors creation du schema
    Base.metadata.create_all(engine)
    return engine

## Connexion
def connect():
    engine = init_db()
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
