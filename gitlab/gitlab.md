%title: GITLAB
%author: xavki


# GITLAB : INTRODUCTION


<br>

Basé sur Git - première version 2011

Créé par Dmitriy Zaporozhets et Valery Sizov

Langages : Ruby & Go


-------------------------------------------------------------------------------------------------------

# GITLAB : INTRODUCTION

<br>

GitLab :

		* dépôts Git

		* gestion de tickets (comme redmine...)

		* organisation du travail (comme trello...)

		* wiki et pages web

		* intégration continue

		* déploiement continue

		* sécurité applicative

		* API pour de nombreux services

=> couvre une grande partie des facettes du devops

-------------------------------------------------------------------------------------------------------

# GITLAB : INTRODUCTION

<br>

Différents entités :

		* GitLab Inc : compagnie, en bourse

		* GitLab CE : produit community edition (gratuit)

		* GitLab EE : produit enterprise edition (payant)
										* premium : 19$/user/mois
										* ultimate : 99$/user/mois
										+ complément storage et ci/cd minutes

-------------------------------------------------------------------------------------------------------

# GITLAB : INTRODUCTION

<br>

GitLab intègre de nombreuses technologies :

		* redis

		* nginx

		* postgres

		* registry docker
		
		* Ruby on rails

		* Go

		* prometheus (interne)

		* exporters

-------------------------------------------------------------------------------------------------------

# GITLAB : INTRODUCTION

<br>

Installation : 

		* multiples OS

		* conteneurisée ou non

		* https://about.gitlab.com/install/


-------------------------------------------------------------------------------------------------------

%title: GITLAB
%author: xavki


# GITLAB : INSTALLATION


<br>

Sans docker

```
apt-get update -qq
apt-get install -qq -y vim git wget curl >/dev/null
```

```
curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
apt-get update -qq
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

```
apt install -y gitlab-ce
```

```
sed -i s/"gitlab.example.com"/"${1}"/g /etc/gitlab/gitlab.rb
gitlab-ctl reconfigure
```


-------------------------------------------------------------------------------------------------------

# GITLAB : INTRODUCTION

<br>

Avec docker & docker-compose :

cf fichier joint



%title: GITLAB
%author: xavki


# GITLAB : 03 - GUI


<br>

Premier user : root

Password > vim /etc/gitlab/initial_root_password

<br>

* Organisation découpé en fonction :

	1 Group = 1/+ Project

	Users

	Interface d'administration




# GITLAB : 04 - Premier user

# GITLAB : 05 - Premier Dépôt

%title: GITLAB
%author: xavki


# GITLAB : 06 - Premier Git Clone


<br>

git clone (ssh|https)

3 types d'accès :

		* ssh

		* https : variables d'environnement
				http://${GIT_USER}:${GIT_PASSWORD}@gitlaburl

		* token (Personnal/Project)
				https://<token-name>:<token>@gitlaburl



%title: GITLAB
%author: xavki


# GITLAB : 07 - Issues - Basics


<br>

Doc : https://docs.gitlab.com/

* gestion des tickets

* approche par projets et par utilisateurs

* 3 sous rubriques :

		* List : liste des tickets

		* Boards : vision sous forme de tableau des avancées des tickets

		* Service Desk : permet l'utilisation via solution externes (mails par exemple)

		* Milestones : tracking de certains tickets éventuellement couplé aux MR

----------------------------------------------------------------------------------------------

# GITLAB : 07 - Issues - Basics

<br>

* référence à des users ou groupes @{user}

* lien vers des commits : #{num_commit}

* intégration de code `` ou <code>

* time tracking : /estimate et  /spent
  

  %title: GITLAB
%author: xavki


# GITLAB : 08 - Issues Templates


<br>

* Templates de ticket

	* doc : https://docs.gitlab.com/ee/user/project/description_templates.html

	* .gitlab/issue_templates/

	* format markdown

* add to do (issues, merge requests, epics, design)
	* ou avec la référence @ en début de ligne (important)

* move issue

* delete issue

%title: GITLAB
%author: xavki


# GITLAB : 09 - Labels


<br>

* Labels

	* Project information > Labels (description, couleur, suscribe)

	* génération d'un jeu de labels par défaut

	* catégories pour issues, merge requests, epics

	* intégration aux boards et à la recherche

	* promote Labels en Groupes

	* prioriser les labels
