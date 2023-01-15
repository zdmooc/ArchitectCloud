#! /usr/bin/python
## --------------------------
## Recuperation des fichiers
## --------------------------

import os
import time
import ftplib

HOST="<HOTE DISTANT>"
LOGIN="<LOGIN>"
PASSE="<MOT DE PASSE>"
DEST_DIR="data/ftp_in"
REP_DATA="data"

## --------------------------------
# D'abord on change le repertoire
## --------------------------------
print( "Debut : %s " % time.asctime())
print( "Changement de repertoire : %s " % DEST_DIR)
os.chdir(DEST_DIR)

print( "Connexion : %s %s/%s " % ( HOST, LOGIN, PASSE ))
rl = ftplib.FTP(HOST)
rl.login(LOGIN, PASSE)

print( "Changement de repertoire : %s " % REP_DATA)
rl.cwd(REP_DATA)

print( "recup de la liste des fichiers")
liste=[]
rl.dir(liste.append)

fichiers=[]

for l in liste:
    if l.endswith('dat'):
        fichiers.append(l.split()[-1])

print( "Transfert des fichiers ")
for f in fichiers:
    print( "    Recup de %s " % f)
    with open( f , "wb") as fp:
        rl.retrbinary("RETR %s" % f, fp.write)

print( "Fin de la connexion")
rl.quit()
print( "Fin   : %s " % time.asctime())
