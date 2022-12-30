
> GIT : intérêt <-
=========

* microvidéos

<br>
* versionner : retour arrière, gestion version

* dépot local et/ou distant(s) => github / gitlab


-------------------------------------------------

-> Premières commandes <-


* sudo apt-get install git

* git init : initialisation du dépôt local
	- .git : tout le versionning

* git add <nom fichier> : ajouter des fichiers
	- éviter git add .

* git commit : pour commenter les git add

* git status : état du dépôt (actions à faire)

-> GIT : config <-
=========

<br>
Où ? :
	- 1. /etc/gitconfig  : à tous les users/machine
	- 2. ~/.gitconfig  : à un utilisateur
	- 3. <dir_depot>/.git/config : à un dépôt/utilisateur

-------------------------------------------------

-> Commandes à retenir <-


* git config --list : pour lister les variables

* git config --global user.email "mail"  : pour définir email


			  -> GIT : logs <-
=========

* essentiel pour un outil de versionning
<br>

* git log

* git log --oneline

* git log --oneline --graph

* git log --oneline --graph --name-status

Perso :

git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Cblue - %cn %Creset' --abbrev-commit --date=relative


	
-> GIT : différences entre commit <-
=========

* à savoir faire :
	- incident : quelqu'un a fait évoluer un fichier de conf : mais quelle ligne ?

<br>

* git diff <commit1> <commit2>

* git diff <branch1>..<branch2>

* dans le même genre :
	-	git log --graph -p

<br>
	-> GIT : le revert <-
=========

<br>
* git revert permet de revenir en arrière (un ou plusieurs commit)
	- c'est la manière propre (différence de reset)
		- car on garde une trace des commits (git reset non)

<br>
état final : 	commit1 -- commit2 -- commit3

objectif revenir à commit1

revert :      commit1 -- commit2 -- commit3 -- commit2 -- commit1
reset :				commit1

<br>

* git revert <num_dernier_commit> : revenir au denrier commit

* git revert HEAD~2..HEAD : revenir de 2 commits en arrière

* ATTENTION : ne pas confondre avec git checkout <fichier> (à faire avant indexation)

	<br>
	-> GIT : le blame <-
=========

<br>
* git blame : permet de lister les dernières modifications de chaque ligne d'un fichier

* git blame <fichier> 

* git blame -L l1,l2 <fichier>    : de la ligne l1 à l2

* git log -S "ligne" --pretty=format:'%h %an %ad %s'   : recherche les logs concernant des lignes contenant "lignes

	<br>
-> GIT : les branches <-
=========

<br>
* permet meilleure gestion des versions (espace de travail)

* permet de travailler plus facilement à plusieurs

* permet d'organiser les mises en production (notion de tags...)

<br>

Commandes :

git branch <nom_branche>   : création d'une branche

git checkout <nom_branche> : changement de branche

git merge <branche_source> : import d'une branche source vers ma branche actuelle

	https://raw.githubusercontent.com/darpan-jain/git-cheat-sheet/master/Img/git-flow-commands-without-flow.png
	
	<br>
	
	-> GIT : éditeur TIG <-
=========

<br>
* visualiser un dépot (git log --graph)

* naviguer dans les commit

* visualiser en instantané les commits

* éditer

<br>

Commandes :

* tig : navigation dépôt

* tig show : dernier commit en détail

* tig status : détails git status

* tig log : git log plus détaillé et en couleur

* tig -- <fichier> : focus sur un fichier

* tig blame -C <fichier> : git blame plus sympa (couleur, lignes détaillées)
<br>
	-> GIT : gitignore <-
=========

<br>
* principe ne pas gitter certains fichiers ou répertoires

* .gitignore : à la racine du dépot comme le répertoire .git/

```
# on ignore le répertoire de logs
logs/
```

<br>

* Astuce :
	- avoir à gérer une liste longue
	- faire l'inverse : lister uniquement les répertoires ou fichiers à gitter (acte volontaire)

Contenu du gitignore :

on ignore tout sauf "scripts/"

```
# tout
/*
# sauf scripts/
!/scripts/

```
