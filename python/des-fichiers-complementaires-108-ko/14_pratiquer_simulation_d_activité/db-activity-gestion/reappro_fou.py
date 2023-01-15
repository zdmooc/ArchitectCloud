## --------------------
## REAPPRO
## --------------------

# Etape 1 : recup de la liste des besoins
# Etape 2 : pour chaque produit selectionner 1 fourn
# Etape 3 : generer les commandes

from sqlalchemy import select

from base import connect
from definitions import Client, Produit, Fourn, Stock, ComCli, LigCli, LigFou

import sequence as seq

import datetime
import random

def get_besoins():
    """
    Calcul des besoins en commande
    """
    session = connect()
    r = """
        select produit_id, sum(qcom) 'qte'
        from LIGCLI
        where qcom-qliv > 0
        group by produit_id
        order by produit_id
    """
    ligs = session.execute(r)
    besoin = [ x for x in ligs ]
    session.close()
    return besoin

def get_qcom_fou(p):
    session = connect()
    r = """
    select produit_id, sum(qcom)
    from LIGFOU
    where qcom-qrecu > 0
    and produit_id = %s
    """ % p
    ligs = session.execute(r)
    r = [ x for x in ligs ]
    session.close()
    if r[0][1]:
        return r[0][1]
    else:
        return 0

def get_fourn():
    session = connect()
    s = select([Fourn.id])
    fous = session.execute(s)
    l = [ x[0] for x in fous]
    session.close()
    return random.choice(l)

def get_delai(fou):
    session = connect()
    s = select([Fourn]).where(Fourn.id==fou)
    r = session.execute(s)
    f = r.fetchone()
    session.close()
    return f.delai

def gnr_comfou(besoin):
    session = connect()
    #pdb.set_trace()
    for b in besoin:
        qcomfou = get_qcom_fou(b[0])
        if qcomfou < b[1]:
            f = get_fourn()
            delai = get_delai(f)
            C = LigFou()
            C.numcom = seq.Next_val('COMFOU')
            C.numlig = 1
            C.produit_id = b[0]
            C.fou_id = f
            C.qcom = b[1]
            C.prix = 0
            C.qrecu = 0
            C.dprevu = datetime.datetime.now()
            C.dprevu += datetime.timedelta(days=delai)
            print(" Cde %s fou=%s pro=%s qte=%s " % ( C.numcom, C.fou_id, C.produit_id, C.qcom ))
            session.add(C)
        else:
            print("  *Pas de Cde pro=%s qte=%s qcomfou=%s" % ( b[0], b[1], qcomfou))

    session.commit()
    session.close()

def run():
     b = get_besoins()
     gnr_comfou(b)
 

if __name__ == '__main__':
    run()
