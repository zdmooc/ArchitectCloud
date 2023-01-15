from pymongo import MongoClient

## création d'une session
client  = MongoClient("mongodb://localhost:27017/")

## connexion sur la base de données test
db = session.test

## La collection qui interesse
contacts = db.contacts

## On commence par la purger
contacts.drop()

## Création d'un contact
first_contact = {
        'name' : 'Linus Torvalds',
        'tel' : '06 01 02 03 04',
        'date_nai' : '28-12-1969'
        }

result = contacts.insert_one(first_contact)

## Puis d'un autre contact
autre_contact = {
        'name' : 'Luke Skywalker',
        'tel' : '06 01 02 03 04',
        'date_nai' : '28-12-1969',
        'comment' : 'Chevalier Djedi'
        }
result = contacts.insert_one(autre_contact)

## Affichage des contacts créés
for e in db.contacts.find():
    print(e)
