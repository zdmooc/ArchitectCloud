#! /bin/bash

get_liste()
{
	LISTE=$(ls *.odt | grep -v table_des_matieres)
	for i in $LISTE
	do
		odt2txt $i | grep -i '#' | grep -i 'fichier' | grep ':'
	done
}


get_liste | cut -d: -f2 | tr -d ' '
