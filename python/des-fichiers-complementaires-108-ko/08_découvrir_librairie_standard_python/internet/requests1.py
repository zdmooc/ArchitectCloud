
import requests
from bs4 import BeautifulSoup

while mot := input("Mot à rechercher : "):
    if mot != "quit":
        url = "https://fr.wiktionary.org/wiki/%s" % mot + "#Fran%C3%A7ais"
        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "lxml")
            print(" Titre : %s " % soup.h1.text )
            ol = soup.find_all('ol')[0]
            print(ol.text)
            print("-" * 70 )
        except:
            print("Erreur ...")
    else:
        break
