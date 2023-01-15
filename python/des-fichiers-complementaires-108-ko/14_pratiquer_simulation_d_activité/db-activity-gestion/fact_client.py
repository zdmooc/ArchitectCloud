##
## Facture Client
##

# Pour toutes les lignes de commandes livrees
# QFAC = QLIV 
# Generation d'une facture pour le client

from sqlalchemy import select
 
from base import connect
from definitions import Client, Produit, Fourn, Stock, ComCli, LigCli, LigFou

import sequence as seq

import datetime
import random

##
## Si une commande a ete facture 
## elle a un numero de facture 
## et donc on peut chercher dans les lignes 
## si elle est complete
##
def get_ccl_a_facturer():
    ccl_a_facturer = []
    session = connect()
    ccl = select([ComCli]).where(ComCli.facture == 0)
    for c in session.execute(ccl):
        lcl = select([LigCli]).where(LigCli.numcom == c.numcom)
        nb_lig = nb_lig_liv = 0
        for l in session.execute(lcl):
            #print(l.numcom, l.numlig, l.qcom, l.qliv)
            nb_lig += 1
            nb_lig_liv += (l.qcom == l.qliv)
        ## si toutes les lignes sont livrees alors
        if nb_lig == nb_lig_liv:
            ## creation d'un facture a partir de la commande
            ccl_a_facturer.append(l.numcom)
    session.close()
    return ccl_a_facturer

## ----------------------------------------------
## Creation d'un facture a partir d'une commande
## ----------------------------------------------
def facture_ccl(nccl):
    session = connect()
    try:
        numfac = seq.Next_val('FACTURE')
        ccl = session.query(ComCli).filter(ComCli.numcom==nccl).\
                update({ComCli.facture: numfac}, synchronize_session=False)

        lcl = session.query(LigCli).filter(LigCli.numcom==nccl).\
                update({LigCli.qfac: LigCli.qliv}, synchronize_session=False)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    return numfac


def run():
    list_ccl = get_ccl_a_facturer()
    for c in list_ccl:
        print("facture : %s / %s " % (c, facture_ccl(c)))
if __name__ == '__main__':
    run()
