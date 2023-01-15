
import sqlite3
import os
from faker import Faker
import random


def open_db(db_name):
    return sqlite3.connect(db_name)

def create_table(db, table_name):
    c = db.cursor()
    r = "SELECT name FROM sqlite_master WHERE type='table' AND name='%s';" % table_name
    c.execute(r)
    result = c.fetchone()
    if not result:
        print("Creation de la table : %s " % table_name)
        r = "create table %s (id integer, nom varchar(30), tel varchar(30), genre varchar(1), datnai date, profession varchar(30));"
        c.execute( r % table_name )


def populate(db, table_name, nb):
    c = db.cursor()
    fake = Faker('fr_FR')

    for i in range(1, nb):
        g = random.choice(['M','F'])
        if g == 'M':
            n = fake.name_male()
        else:
            n = fake.name_female()
        t = fake.phone_number()
        d = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=75)
        j = fake.job()
        ## attention le formattage de la date est important pour sqlite
        c.execute("insert into %s values (?, ?, ?, ?, ?, ?)" % table_name, (i, n, t, g, d.strftime("%Y-%m-%d"), j))
    db.commit()


def main():
    db_name = 'test.dbf'
    db = open_db(db_name)
    table = 'CONTACTS'
    create_table(db, table)
    nb = 1000
    populate(db, table, nb)

    c = db.cursor()

    requete = """ select id, nom, tel, genre, date(datnai), (strftime('%Y', 'now') - strftime('%Y', datnai)) 
                    from CONTACTS 
                    where 
                            genre='M' 
                        and date(datnai) < date('now', '-18 year') 
                        and date(datnai) >= date('now', '-25 year') 
                    order by 6;
             """
    print("=== Requete 1 ====")
    for row in c.execute(requete):
        if 'Pierre' in row[1]:
            print( row )

    requete = "select profession, count(*) from CONTACTS group by profession order by 2 desc limit 10;"
    print("=== Requete 2 ====")
    for row in c.execute(requete):
            print( row )

    db.close()

if __name__ == '__main__':
    main()
