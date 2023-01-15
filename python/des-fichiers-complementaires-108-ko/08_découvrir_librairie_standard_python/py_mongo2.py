from pymongo import MongoClient
from faker import Faker
import random
import datetime

## création d'un client Mongo
session  = MongoClient("mongodb://localhost:27017/")

## connexion sur la base de données test
db = session.test

## On recupere la liste des collections de la base de données
colls = db.list_collection_names()

## La collection qui interesse
contacts = db.contacts

## On commence par la purger
if 'contacts' in colls:
    print("Purge de la collection")
    contacts.drop()

fake = Faker('fr_FR')
nb = 100

populate = []

for i in range(1, nb):
    g = random.choice(['Masculin','Féminin'])
    if g == 'Masculin':
        n = fake.name_male()
    else:
        n = fake.name_female()
    t = fake.phone_number()

    ##  Date de naissance 
    dd = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=75)
    dt = fake.time_object(end_datetime=None)
    d = datetime.datetime.now()
    d = d.combine( dd, dt)

    j = fake.job()

    populate.append( {
        'nom' : n,
        'téléphone' : t,
        'date_de_naissance' : d,
        'sexe' : g,
        'profession' : j,
        })

## on insere tout d'un coup !
contacts.insert_many(populate)

ed = datetime.datetime(2009, 11, 12, 12) #environ 18 ans
sd = datetime.datetime(1989, 11, 12, 12) #environ 30 ans

requete = { 
            "date_de_naissance": { "$lt": ed, "$gte" : sd } ,
            "sexe" : "Masculin"
        }

fmt  = "| {:30s} | {:20s} | {:10s} | {:10s} | {:40s} |"
for e in db.contacts.find( requete ).sort("nom"):
    print( fmt.format(e['nom'], e['téléphone'], e['date_de_naissance'].strftime("%x"), e['sexe'], e['profession'] ))
