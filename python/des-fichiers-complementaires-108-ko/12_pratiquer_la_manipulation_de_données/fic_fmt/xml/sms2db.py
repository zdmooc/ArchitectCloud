## ==================================================
## Utilisation de SQL Alchemy + SQLITE
## ==================================================

import os
import sys

from sqlalchemy import sql
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime, Date, Numeric, BigInteger, Float
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
import datetime

import xmltodict
import pprint

import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

## ===============================
## Creation BASE + DEFINITIONS 
## ===============================
Base = declarative_base()

class BASE_TABLE():
    " Classe commune a toute les autres"
    u_id = Column(Integer, primary_key=True)

class SMS(Base, BASE_TABLE):
    "Table des SMS"
    __tablename__ = "SMS"
    address          = Column("address", String(30))
    sms_time         = Column("sms_time", DateTime)
    typ              = Column("typ", String(5))
    service_center   = Column("service_center", String(20))
    name             = Column("name", String(20))
    body             = Column("body", Text)

## ---------------
## Creation base 
## ---------------

SQLITE_FILE_NAME = "SMS.dbf"
BASE_NAME = 'sqlite:///'+SQLITE_FILE_NAME

engine = create_engine(BASE_NAME)

Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

## ==========================
## Creation d'enregistrements 
## ==========================

fichier = 'sms_20200111092211.xml'

with open(fichier) as fd:
    doc = xmltodict.parse(fd.read(), process_namespaces=True)

for sms in doc['allsms']['sms']:
    s = SMS()
    s.address = sms['@address']
    ts = sms['@time']
    if 'avr.' in ts:
        ts = ts.replace('avr.', 'avril')
    d = datetime.datetime.strptime(ts, '%d %b %Y %H:%M:%S')
    s.sms_time = d
    if sms['@type'] == "1":
        s.typ = "Recv"
    elif sms['@type'] == "2":
        s.typ = "Emis"
    else:
        s.typ = "<?>"
    s.service_center = sms['@service_center']
    s.name = sms['@name']
    s.body = sms['@body']
    session.add(s)
session.commit()
