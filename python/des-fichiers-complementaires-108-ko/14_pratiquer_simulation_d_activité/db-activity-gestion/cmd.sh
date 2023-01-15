:
## -----------------------------------
## Lancement d'une commande par cron
## -----------------------------------

PYTHON=/home/chris/.virtualenvs/lps2/bin/python

## ------------------------
## Petite routine de log
## ------------------------
log()
{
	stamp=$(date "+%j %X")
	echo ">>> $stamp : $1 "
}


DIR_BASE=/home/chris/dvp/scripting_linux_python/scripting_python_linux/src/db-activity-gestion
DIR_BIN=$DIR_BASE
DIR_LOG=$DIR_BASE/log

TS=$(date "+%j_%H%M%S")

FONCTION="${1-null}"
FIC_LOG=$DIR_LOG/${TS}_${FONCTION}.log

exec 1>$FIC_LOG
exec 2>&1

log "Debut du traitement"

if [ -f $DIR_BIN/${FONCTION}.py ]
then
	log "Execution commande : $FONCTION"
	( cd $DIR_BIN ; $PYTHON ${FONCTION}.py )
else
	log "Erreur Fonction : $FONCTION inexistante"
fi
log "Fin du traitement"
