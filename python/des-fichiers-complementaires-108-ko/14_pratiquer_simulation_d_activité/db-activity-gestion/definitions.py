## -------------------------------------
## DEFINITIONS DE LA BASE DE DONNEES
## -------------------------------------

import os
import sys
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime, Date, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

BASE_NAME = 'sqlite:///data.dbf'

class BASE_TABLE():
    " Classe commune a toute les autres"
    id = Column(Integer, primary_key=True)
    d_cre = Column(DateTime, default = datetime.datetime.now() )
    d_mod = Column(DateTime, default = datetime.datetime.now(), onupdate=datetime.datetime.now() )

class Compteur(Base, BASE_TABLE):
    "Table des compteurs"
    __tablename__ = "COMPTEURS"
    nom = Column(String(20), nullable=False, unique=True)
    val = Column(Integer)

    def __repr__(self):
        return "< compteur : {0:} / {1:} >".format( self.nom, self.val )

class Client(Base, BASE_TABLE):
    "Le fichier client"
    __tablename__ = 'CLIENTS'
    nom = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return "< client : {0:} >".format(self.nom)

class Produit(Base, BASE_TABLE):
    "Les produits"
    __tablename__ = 'PRODUITS'
    desig = Column(String(30), nullable=False, unique=True)
    prix = Column(Float(12,2))

    def __repr__(self):
        return "< produit : {0:} / {1:} >".format(self.desig, self.prix)

class Fourn(Base, BASE_TABLE):
    "Les fournisseurs"
    __tablename__ = 'FOURN'
    nom = Column(String(20), nullable=False, unique=True)
    delai = Column(Integer)

    def __repr__(self):
        return "< fourn : {0:}/{1:} >".format(self.nom, self.delai)

class Stock(Base, BASE_TABLE):
    "Le stock par depot"
    __tablename__ = 'STOCK'
    depot = Column(String(10), nullable=False)
    produit_id = Column(Integer, ForeignKey('PRODUITS.id'))
    produit = relationship(Produit)
    qstock = Column(Integer)

    def __repr__(self):
        return "< Stock : {0:}/{1:}/{2:} >".format(self.depot, self.produit_id, self.qstock )

class ComCli(Base, BASE_TABLE):
    "Les commandes clients"
    __tablename__ = 'COMCLI'
    numcom = Column(Integer, unique=True)
    datcom = Column(DateTime, default = datetime.datetime.now() )
    client_id = Column(Integer, ForeignKey('CLIENTS.id'))
    client = relationship(Client)
    facture = Column(Integer)

    def __repr__(self):
        return "< Comcli : {0:}/{1:}/{2:}/{3:} >".format(self.numcom, self.datcom, self.client_id, self.facture )

class LigCli(Base, BASE_TABLE):
    "Les lignes de commandes clients"
    __tablename__ = 'LIGCLI'
    numcom = Column(Integer)
    numlig = Column(Integer)
    produit_id = Column(Integer, ForeignKey('PRODUITS.id'))
    produit = relationship(Produit)
    qcom = Column(Integer)
    prix = Column(Float(12,2))
    qliv = Column(Integer)
    qfac = Column(Integer)

    def __repr__(self):
        return "< ligcli : {0:}/{1:}/{2:}/{3:} >".format(self.numcom, self.numlig, self.produit_id, self.qcom )

class LigFou(Base, BASE_TABLE):
    "Les commandes fournissuers"
    __tablename__ = 'LIGFOU'
    numcom = Column(Integer, unique=True)
    numlig = Column(Integer)
    fou_id = Column(Integer, ForeignKey('FOURN.id'))
    fou = relationship(Fourn)
    produit_id = Column(Integer, ForeignKey('PRODUITS.id'))
    produit = relationship(Produit)
    qcom = Column(Integer)
    prix = Column(Float(12,2))
    dprevu = Column(Date)
    qrecu = Column(Integer)

    def __repr__(self):
        return "< ligfou : {0:}/{1:}/{2:}/{3:}/{4:} >".format(self.numcom, self.numlig, self.fou_id, self.produit_id, self.qcom )

# Création de la base de données
engine = create_engine(BASE_NAME)
 
# Création des tables dans la base de données
Base.metadata.create_all(engine)
