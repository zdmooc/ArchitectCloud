import pyexcel as pe
from fake_contact import fake_contact


Feuilles = [ "INVITES", "FAMILLE", "VIP" ]

data = {}

entete = [ "NOM", "DATE_NAI", "ADRESSE", "TEL", "COMMENT" ]

for F in Feuilles:
    page = []
    page.append( entete )
    for x in range(0, 5):
        n,d,a,t,c = fake_contact()
        page.append( [n, d.strftime('%Y-%m-%d'), a, t, c ] )
    data[F] = page

pe.save_book_as(bookdict=data, dest_file_name="LISTE_INVITES.ods")
