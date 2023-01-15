
import sqlite3

db = sqlite3.connect(':memory:')

c = db.cursor()

c.execute('create table contact( id integer, nom varchar(30), tel varchar(30), datnai date) ')

c.execute(' insert into contact values (1, "linux Torvalds", "06 01 02 03 04", "28-12-1969") ')

db.commit()

for row in c.execute('select * from contact'):
    print(row)

db.close()
