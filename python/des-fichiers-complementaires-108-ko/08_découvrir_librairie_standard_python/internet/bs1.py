html_doc = """\
        <html>
        <head>
        <title> Ma Page Web </title>
        </head>
        <body>
        <h1> Ceci est un page WEB </h1>
        <p> Voici un petit texte a trouver </p>
        <ul>
        <li> <a href="http://example.com/lien1">Lien 1 </a> </li>
        <li> <a href="http://example.com/lien2">Lien 2 </a> </li>
        <li> <a href="http://example.com/lien3">Lien 3 </a> </li>
        <li> <a href="http://example.com/lien4">Lien 4 </a> </li>
        </ul>
        <table class='ma_class'>
            <thead>
                <td> Systeme </td>
                <td> Gouvernement </td>
                <td> Niveau technologique </td>
                <td> Population </td>
            </thead>
            <tbody> 
            <tr>    
                <td>Lave</td>
                <td>Dictature</td>
                <td>Agricultural Riche</td>
                <td>2,5 M</td>
            </tr>
            <tr>    
                <td>Teaatis</td>
                <td>Feodal</td>
                <td>Agricultural Moyen</td>
                <td>1,6 M</td>
            </tr>
            <tr>    
                <td>Riinus</td>
                <td>Communiste</td>
                <td>Industriel Moyen</td>
                <td>4,2 M</td>
            </tr>
            <tr>    
                <td>Diurezza</td>
                <td>Gouvernement multiple</td>
                <td>Industriel Riche</td>
                <td>8,5 M</td>
            </tr>
            </tbody>

        </table>
        </body>
        </html>
"""

from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(indent=4)

soup = BeautifulSoup(html_doc, 'lxml')

print("== Titre de la page  ==")
print( soup.title.text )

print("== Extraction des liens ==")
for l in soup.find_all('a'):
    print(l.text, l.get('href'))

## Extraction de la table 
data = []
table = soup.find('table', attrs={ 'class':'ma_class'})
tbody = table.find('tbody')

for row in tbody.find_all('tr'):
    cols = row.find_all('td')
    elt = [ x.text for x in cols ]
    data.append( elt )

print("== Extraction de la table ==")
print(pp.pprint(data))

