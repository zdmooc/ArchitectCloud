## -------------------------------------
## DECLARATIONS DE LA BASE DE DONNEES
## -------------------------------------

import os
import sys
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime, Date, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

## Necessaire pour MySQL
# import pymysql_sa
# pymysql_sa.make_default_mysql_dialect()
 

## Définitions de la base de données
Base = declarative_base()

SQLITE_FILE_NAME = "data.dbf"
BASE_NAME = 'sqlite:///'+SQLITE_FILE_NAME
# BASE_NAME = 'mysql://dev:dev@localhost/DEV'

## Declarations des classes 
class BASE_TABLE():
    " Classe commune a toute les autres"
    id = Column(Integer, primary_key=True)
    d_cre = Column(DateTime, default = datetime.datetime.now() )
    d_mod = Column(DateTime, default = datetime.datetime.now(), onupdate=datetime.datetime.now() )
    status = Column(String(5), default = "OK", nullable = False )

class Contact(Base, BASE_TABLE):
    "Le fichier Contacts"
    __tablename__ = 'CONTACTS'
    nom         = Column(String(20), nullable=False)
    datnai      = Column(Date)
    genre       = Column(String(1))
    tel         = Column(String(30))
    profession  = Column(String(40))

## Creation d'un moteur 
## Pour la creation du schema
engine = create_engine(BASE_NAME)
 
## Si ce n'est pas fait alors creation du schema
Base.metadata.create_all(engine)
