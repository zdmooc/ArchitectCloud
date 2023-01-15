## --------------------
## Prise de commande
## CLIENT
## --------------------

#Etape 1 : => import 
#Etape 2 : Recup du catalogue
#Etape 3 : Choix du client 
#Etape 4 : Generation de commande

from sqlalchemy import select

from base import connect
from definitions import Client, Produit, Stock, ComCli, LigCli

import sequence as seq

import datetime
import random
#import pdb

def get_catalog():
    session = connect()
    s = select([Produit])
    p = [ (x.id, x.prix) for x in session.execute(s) ]
    session.close()
    return p

def get_client():
    session = connect()
    s = select([Client.id])
    clis = [ x.id for x in session.execute(s)]
    session.close()
    return random.choice(clis)

def get_prods(cat):
    max_cmd = len(cat)
    nb_pro_cmd = random.randint(0, max_cmd-1)+1
    pros = random.sample(cat, nb_pro_cmd)
    return pros

def gnr_comcli(cli, prods):
    print("Client : %s " % cli )
    print("Nb Produits a commandes : %s " % len(prods) )
    print("Produits commandes : %s " % sorted(prods) )
    print("Generation commande")
    session = connect()
    try:
        numcom = seq.Next_val('COMCLI')
        C = ComCli()
        C.numcom = numcom
        C.datcom = datetime.datetime.now()
        C.client_id = cli
        C.facture = 0
        session.add(C)
        print( "Commande No : " , C.numcom )
        n = 1
        for p in prods:
            L = LigCli()
            L.numcom = numcom
            L.numlig = n
            L.produit_id = p[0]
            L.qcom = random.randint(1, 5000)
            L.qliv = 0
            L.qfac = 0
            L.prix = p[1]
            print("%s : %s" % (n,L))
            n += 1
            session.add(L)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def run():
    catalog = get_catalog()
    client = get_client()
    prods_cmd = get_prods(catalog)
    gnr_comcli(client, prods_cmd)
 

if __name__ == '__main__':
    run()
