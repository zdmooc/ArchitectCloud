#! /bin/bash

RND=$((RANDOM%5+1))

NB_ESSAI=0

FOUND=false

while [ $FOUND != true ]
do
	echo "Tapez un chiffre de 1 à 5"
	read essai
	if [ "$essai" == "$RND" ]
	then
		echo "TROUVE !"
		
		FOUND=true
	else
		echo "Essayez encore ..."
	fi
	NB_ESSAI=$(($NB_ESSAI+1))
done
echo "BRAVO Trouve en $NB_ESSAI essai(s)"
