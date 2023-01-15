## -------------------
## Script de base
## -------------------

BASE_DIR=$(pwd)

## +%j donne le no du jour dans l'année
## Permet d'avoir un fichier par jour et un historique d'un an
TS=$(date "+%j")
LOG=$BASE_DIR/log/${TS}.log

## On re dirige les flux standard

exec 2>&1
exec 1>$LOG

## -----------------------
## Petite routine de log
## -----------------------
log()
{
	msg="${1}"
	ts=$(date "+%j %X")
	printf ">>> ${ts} : ${msg}\n"
}

## Fonction principale 
compute()
{
	echo "Je bosse ..."
	sleep 5
}


## -----------
## MAIN
## -----------
log "Debut du traitement"
compute
log "Fin du traitement"
