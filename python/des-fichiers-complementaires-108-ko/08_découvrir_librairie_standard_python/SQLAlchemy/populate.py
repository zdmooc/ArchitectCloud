from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
 
from definitions import Base, BASE_NAME, SQLITE_FILE_NAME
from definitions import Contact


from faker import Faker
fake = Faker('fr_FR')

import datetime
import random
import os

import pudb
 
engine = create_engine(BASE_NAME)
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()


def populate( n ):

    for c in range(1,n):

        g = random.choice(['M','F'])
        if g == 'M':
            n = fake.name_male()
        else:
            n = fake.name_female()
        t = fake.phone_number()
        d = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=75)
        j = fake.job()

        r = Contact()
        r.nom = n
        r.genre = g
        r.datnai = d
        r.tel = t
        r.profession = j
        session.add(r)

    ## On valide tout d'un coup
    session.commit()

def liste_contact():
    #pudb.set_trace()
    s = select([Contact])
    result = session.execute(s)

    titre  = "| {:30s} | {:20s} | {:10s} | {:5s} | {:30s} |".format( "Nom", "Telephone", "Date N.", "Sexe", "Profession" )
    print("=" * len(titre))
    print(titre)
    print("=" * len(titre))
    fmt  = "| {nom:30s} | {tel:20s} | {datnai:%d/%m/%Y} | {genre:5s} | {profession:30s} |"
    for row in result:
        print( fmt.format(**row) )
    print("=" * len(titre))


if __name__ == "__main__":
    if session.query(Contact).count() == 0:
        populate( 20 )
    liste_contact()
