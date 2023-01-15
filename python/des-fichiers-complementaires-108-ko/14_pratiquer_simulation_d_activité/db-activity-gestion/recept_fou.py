## -------------------------
## Reception Fournisseur
## -------------------------

# Pour toutes les commandes a receptionner
# - On receptionne la Qte (QREC)
# - On incremente le STOCK

from sqlalchemy import select
 
from base import connect
from definitions import Client, Produit, Fourn, Stock, ComCli, LigCli, LigFou

import sequence as seq

import datetime
import random

def get_cfou_ar(date_jour):
    session = connect()
    r = select([LigFou]).where(LigFou.qcom-LigFou.qrecu > 0).where(LigFou.dprevu <= date_jour)
    cfouar = session.execute(r).fetchall()
    c = [ x for x in cfouar]
    session.close()
    return cfouar

def reception( ncom, nlig, pro, qte, depot):
    session = connect()
    try:
         stock = session.query(Stock).filter( Stock.depot==depot, Stock.produit_id==pro ).first()
         stock.qstock += qte
         ligfou = session.query(LigFou).filter( LigFou.numcom == ncom, LigFou.numlig == nlig).first()
         ligfou.qrecu += qte
         session.add(stock)
         session.add(ligfou)
         session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def run():
    DEPOT = 'D1'
    djour = datetime.datetime.now()
    #djour = datetime.date(2017,2,16)
    cde = get_cfou_ar(djour)
    for c in cde:
        print(" Cde a rec :  %s %s | pro=%s | qte=%s | date=%s " % (c.numcom, c.numlig, c.produit_id, c.qcom, c.dprevu))
        reception( c.numcom, c.numlig, c.produit_id, c.qcom, DEPOT)

if __name__ == '__main__':
    run()
