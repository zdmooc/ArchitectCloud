##
## LIVRAISON CLIENT
##


# Pour toutes les lignes de commandes a livrer 
#  (Par client / Par Produit  ... )
#  - Allouer en fonction de la date de commande
#  - et si QTOCK - QCOM > 0
#  - decrementer le stock

from sqlalchemy import select
 
from base import connect
from definitions import Client, Produit, Fourn, Stock, ComCli, LigCli, LigFou

import sequence as seq

import datetime
import random
import pdb

## Retourne les lignes de commandes a livrer
def get_bl_aliv():
    session = connect()
    r = """
        select numcom, numlig, produit_id, qcom, qliv
        from LIGCLI
        where qcom-qliv > 0
        order by numcom, numlig
    """
    b = session.execute(r)
    bls = [ (x.numcom, x.numlig, x.produit_id, x.qcom, x.qliv) for x in b ]
    session.close()
    return bls

def get_stock(depot, pro):
    session = connect()
    s = select([Stock]).where(Stock.produit_id==pro).where(Stock.depot==depot)
    r = session.execute(s)
    f = r.fetchone()
    session.close()
    return f.qstock

def allocate(ncom, nlig, depot, prod, qte):
    session = connect()
    ## debut de transaction
    try:
        ## destockage de la qte
        stock = session.query(Stock).filter( Stock.depot==depot, Stock.produit_id==prod ).first()
        ## Controle de stock : ici
        stock.qstock -= qte
        ligc = session.query(LigCli).filter( LigCli.numcom==ncom, LigCli.numlig==nlig ).first()
        ligc.qliv += qte
        ## mise a jour de la commande
        session.add(ligc)
        session.add(stock)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def run():
    DEPOT = 'D1'
    ## Pour toute les lignes de commandes a livrer
    b = get_bl_aliv()
    for l in b:
        print(" Je traite : ", l)
        ncom, nlig, prod, qcom, qliv = l
        ## On recupere le stock
        s = get_stock(DEPOT, prod)
        print("Stock Pro Depot %s : %s = %s " % (DEPOT, prod, s))
        if s >= (qcom-qliv):
            print("Allocation %s %s %s %s " % (ncom, nlig, prod, qcom-qliv))
            allocate( ncom, nlig, DEPOT, prod, qcom-qliv )

if __name__ == '__main__':
    run()
