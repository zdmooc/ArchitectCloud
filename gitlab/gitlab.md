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


%title: GITLAB
%author: xavki


# GITLAB : 10 - Wikis


<br>

Wikis :

		* par projet

		* visualisation de l'historique

		* markdown + mermaid
      https://mermaid-js.github.io/mermaid/#/

		* spécifier le code (ex: python)

		* modifier la sidebar

		* linker d'autres pages

		* éditer le dépôt

-----------------------------------------------------------------------------------------

# GITLAB : 10 - Wikis


<br>

\```mermaid
graph TD;
  A-->B;
  A-->C;
\```


\```mermaid
gantt
dateFormat  YYYY-MM-DD
title Xavki's Week
section A section
Prepare Videos            :done,    des1, 2021-11-14,2d
Record Videos             :active,  des2, 2021-11-15, 4d
Publish videos            :active,  des3, 2021-11-16, 2d
\```


%title: GITLAB
%author: xavki


# GITLAB : 11 - Repositories : Définitions 


<br>

Dépôt :

		* dépôt git (gestionnaire de versions)

		* accessible via une adresse : ssh / https

		* différents niveau d'accès

		* peut contenir tout type de fichiers (préférences pour du code/configuration)

		* certains langages sont interprétés (markdown pour la mise en forme)

----------------------------------------------------------------------------------

# GITLAB : 11 - Repositories : Définitions 


<br>

Gitaly :

		* outil d'accès distant à un dépôt Git

		* RPC (Remote Procedure Call)

		* cf project admin area

----------------------------------------------------------------------------------

# GITLAB : 11 - Repositories : Définitions 

<br>

Commit :

		* ensemble d'ajouts/modifications/suppressions dans un dépôt git

		* points de retours possibles

		* ajout d'un commentaire pour identifier ce point

<br>

Remote :

		* dépôt distant (projet de notre gitlab)

----------------------------------------------------------------------------------

# GITLAB : 11 - Repositories : Définitions 

<br>

Branch :

		* ligne de développement d'un projet

		* features = temporaires le temps de développer

		* main / preprod / staging / development ...

		* organisation des branches en flow

----------------------------------------------------------------------------------

# GITLAB : 11 - Repositories : Définitions 

<br>

Flow : 

		* comment faire évoluer une évolution vers la production

		* suivant le type d'évolution : fix / bug / développement...

		* gitflow, gitlab flow...

<br>

Tags :

		* représente une version 

		* se rapporte toujours au même objet

https://git-flow.readthedocs.io/fr/latest/presentation.html

----------------------------------------------------------------------------------

# GITLAB : 11 - Repositories : Définitions 

<br>

Push/Pull :

		* pousser ou ramener des modification depuis/vers le remote

<br>

Merge/Rebase :

		* synchronisation d'une branche avec une autre

----------------------------------------------------------------------------------

# GITLAB : 11 - Repositories : Définitions 

<br>

Revert/Reset :

		* retour arrière avec ou sans conservation de l'historique

<br>

Fork :

		* copie d'un dépôt git sous un autre groupe/user



%title: GITLAB
%author: xavki


# GITLAB : 12 - Flows


<br>

v<major>.<minor>.<patch>

Where

    major : is a version number where you introduced breaking modifications (modifications of your new version are NOT compatible with previous versions);
    minor : is a version number that is compatible with previous versions;
    patch : is an increment for a bug fix or a patch fix done on your software.

<br>

Branch :

		* ligne de développement d'un projet

		* features = temporaires le temps de développer

		* main / preprod / staging / development ...

		* organisation des branches en flow

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

<br>

Flow : 

		* comment faire évoluer une évolution vers la production

		* suivant le type d'évolution : fix / bug / développement...

		* gitflow, gitlab flow...

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

<br>

Tags :

		* représente une version 

		* se rapporte toujours au même objet

https://git-flow.readthedocs.io/fr/latest/presentation.html

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows



https://raw.githubusercontent.com/darpan-jain/git-cheat-sheet/master/Img/git-flow-commands-without-flow.png

* initialisation (histoire d'avoir un début)

```
git tag
git tag -a v0.1.0 -m "première release en production"
git push v0.1.0
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows


* création de la branche de developpement

```
git checkout main
git pull
git checkout -b develop
git push origin develop
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

```
git checkout -b xp-feature-file1
vim file1.txt
git status
git add file1.txt
git commit -m "ajout de fichier"
git push origin xp-feature-file1
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

* hotfix

```
git checkout main
git pull
git checkout -b hotfix-v0.1.1
vim myfix.txt
git add myfix.txt
git commit -m "hotfix - résolution xxx"
git push -u origin hotfix-v0.1.1
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

* merge main

```
git checkout main
git pull
git merge hotfix-v0.1.1
git tag -a v0.1.1 -m "hotfix - résolution xxx"
git push origin v0.1.1
git branch
git branch -d hotfix-v0.1.1
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

* merge develop

```
git checkout develop
git pull
git merge hotfix-v0.1.1
git push -u origin develop
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

* sync et merge de develop

```
git checkout xp-feature-file1
vim file2.txt
git add file2.txt
git commit -m "développement de la feature
git merge develop
vim file3.txt
git add file3.txt
git commit -m "développement de la feature - fin"
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

* fin de dev de la feature on merge vers develop

```
git checkout develop
git pull
git merge xp-feature-file1
git push -u origin develop
```

-------------------------------------------------------------------------------------------

# GITLAB : 12 - Flows

* validation de l'env de developpement merge vers master et tag de version

```
git checkout main
git pull
git merge develop
git tag -a v1.0.0 -m "MVP"
git push --tags
```


%title: GITLAB
%author: xavki


# GITLAB : 13 - Merge Request




%title: GITLAB
%author: xavki


# GITLAB : 14 - Roles et Permissions


<br>

https://docs.gitlab.com/ee/user/permissions.html
http://xavki.gitlab/help/user/permissions

<br>

Roles :

		Guest

		Reporter

		Developper

		Maintainer

		Owner

----------------------------------------------------------------------------------------------------

# GITLAB : 14 - Roles et Permissions


<br>

Type de projet :

		Private : cloné et vu par les membres du projets sauf guests

		Internal : cloné par les users authentifiés

		Public : tout le monde

Ajout membres à partir d'un rôle de maintainer/owner/admin

Project information > members

Group information > members

----------------------------------------------------------------------------------------------------

# GITLAB : 14 - Roles et Permissions


<br>

Projet ou groupe :

0 - Rappel : private / internal / public

A - ajout d'un utilisteur simple à un projet
		* date expiration
		* import d'un autre projet
		* role max
		* classement des utilisateurs/tri
		* source

B - ajout d'un user au groupe

C - ajout d'un groupe à un projet/group

D - si suppression du groupe membre > les users restent 


%title: GITLAB
%author: xavki


# GITLAB : 15 - GitLab-Ci : Présentation


<br>

Continuous Integration :

		* action sur push du nouveau code

		* aider les développeurs dans la phase de développement (code quality...)

		* création de l'applicatif final (binaire...)

		* vérification du code (tests unitaires...) pour trouver d'éventuelles régression
				* découverte le plus tôt possible

<br>

Continuous Delivery :

		* tests complémentaires dans un environnement proche de la production

		* permet de releaser (versionner) avant mise en production

------------------------------------------------------------------------------------------------------------------

# GITLAB : 15 - GitLab-Ci : Présentation


<br>

Continuous deployment :

		* déploiement automatisé en production

<br>

		Pipeline = moyen technique pour dérouler ces étapes (et pas seulement)

		https://docs.gitlab.com/ee/ci/introduction/

------------------------------------------------------------------------------------------------------------------

# GITLAB : 15 - GitLab-Ci : Présentation

<br>

	Runners :

			* ressources/serveurs/conteneurs

			* permet de lancer les jobs

			* applicatifs nécessaires à l'exécution (docker, ansible, maven...)

			* recommandé d'utiliser une machine différente du host Gitlab

			* GO langage

			* dépendance de la version de Gitlab

			* nécessité de l'enregistrer

			* scope d'un runner (shared, group, specific)

			* tag sur les runners (langages, builder...)

			* gitlab.com : runner publique limité en temps d'utilisation (2000min/pipeline/mois)
			
			* doc : https://docs.gitlab.com/runner/

------------------------------------------------------------------------------------------------------------------

# GITLAB : 15 - GitLab-Ci : Présentation


<br>

	Executor :

			* type de runner adapté au job

			* SSH, shell, powershell, docker, kubernetes, virtualbox...
				https://docs.gitlab.com/runner/executors/index.html#selecting-the-executor


<br>

	Pipeline :

			* déclenché par trigger ou par tâcehs récurrentes (cron)

			* suite de tâches à réaliser en vue d'une action finale

			* découpé en stages (étapes)

			* décrit dans un fichier yaml à la racine : .gitlab-ci.yaml

------------------------------------------------------------------------------------------------------------------

# GITLAB : 15 - GitLab-Ci : Présentation


<br>

	Stage :

			* étapes d'un pipeline

			* constitué de 1 à plusieurs jobs

			* regroupement logique

<br>

	Job :

			* tâche précise à réaliser dans un environnement spécifique à celle-ci

			* possibilité de fixer des contraintes : environnement, conditions...

			* consitué d'un script : les commandes réalisées
					before/after possibles

<br>

Simplement :

		Pipeline > Stage(s) > Job(s) > Script

https://about.gitlab.com/blog/2018/01/22/a-beginners-guide-to-continuous-integration/

%title: GITLAB
%author: xavki


# GITLAB : 16 - Activation & premier runner SHELL sur VM


<br>

Gitlab > settings > CI/CD > Runners

Specific/Shared runners

Doc : https://docs.gitlab.com/runner/install/index.html
Linux : https://docs.gitlab.com/runner/install/linux-manually.html

```
curl -LJO "https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb"
sudo dpkg -i gitlab-runner_amd64.deb
sudo gitlab-runner status
```

Rq : amd64/arm/arm64

----------------------------------------------------------------------------------------------------

# GITLAB : 16 - Activation & premier runner SHELL sur VM


<br>

* Enregistrement du runner

```
export REGISTRATION_TOKEN="TPGHnuzJ3a4fyJ2RntRR"
gitlab-runner register --url http://xavki.gitlab/ --registration-token $REGISTRATION_TOKEN
```

* quelques arguments utiles

```
  --non-interactive
  --url "http://xavki.gitlab/"
  --registration-token "TPGHnuzJ3a4fyJ2RntRR"
  --executor "shell"
  --description "runner1"
  --tag-list "shell,runner"
  --run-untagged
  --locked="false"
```

----------------------------------------------------------------------------------------------------

# GITLAB : 16 - Activation & premier runner SHELL sur VM


<br>

* Exemple de saisie

```
Runtime platform  arch=amd64 os=linux pid=12293 revision=de104fcd version=14.5.1
Running in system-mode.                            
Enter the GitLab instance URL (for example, https://gitlab.com/):
[http://xavki.gitlab/]: 
Enter the registration token:
[TPGHnuzJ3a4fyJ2RntRR]: 
Enter a description for the runner:
[runner1]: test
Enter tags for the runner (comma-separated):
simple,linux 
Registering runner... succeeded                     runner=TPGHnuzJ
Enter an executor: docker, ssh, virtualbox, docker+machine, custom, docker-ssh, parallels, shell, docker-ssh+machine, kubernetes:
shell
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded! 
```

----------------------------------------------------------------------------------------------------

# GITLAB : 16 - Activation & premier runner SHELL sur VM


<br>

* Fichier de configuration de runner

```
cat /etc/gitlab-runner/config.toml 
concurrent = 1
check_interval = 0
[session_server]
  session_timeout = 1800
[[runners]]
  name = "test"
  url = "http://xavki.gitlab/"
  token = "ii7j5dugPta5Wzits7Cy"
  executor = "shell"
```

----------------------------------------------------------------------------------------------------

# GITLAB : 16 - Activation & premier runner SHELL sur VM


<br>

* Acivation/Désactivation de gitlab-ci par défaut

```
vim gitlab.rb
gitlab_rails['gitlab_default_projects_features_builds'] = false
gitlab-ctl reconfigure
```

Rq : sinon par projet

----------------------------------------------------------------------------------------------------

# GITLAB : 16 - Activation & premier runner SHELL sur VM


<br>

* Premier .gitlab-ci.yaml

Project > CI/CD > Editor

Bloqué > run untag job

sinon utiliser les tags pour chaque jobs (liste)



https://docs.gitlab.com/runner/install/index.html


%title: GITLAB
%author: xavki


# GITLAB : 17 - lancer un runner sous docker


<br>

Gitlab > settings > CI/CD > Runners

Specific/Shared runners

Doc : https://docs.gitlab.com/runner/install/index.html
Linux : https://docs.gitlab.com/runner/install/linux-manually.html

Note : dns vers l'instance gitlab

```
mkdir -p /data/
docker run -d  \
   --name gitlab-runner \
   --restart always \
   -v /var/run/docker.sock:/var/run/docker.sock \
   -v /data/gitlab-runner:/etc/gitlab-runner \
   gitlab/gitlab-runner:latest
```

-----------------------------------------------------------------------------------------

# GITLAB : 17 - lancer un runner sous docker


docker exec -it gitlab-runner gitlab-runner register

-----------------------------------------------------------------------------------------

# GITLAB : 17 - lancer un runner sous docker
Test:
  stage: test
  image: debian:latest
  script:
    - echo "Start..."
    - sleep 60
    - echo "ended !!"



%title: GITLAB
%author: xavki


# GITLAB : 18 - Runner kubernetes


<br>

* installation d'un mini cluster kubernetes

```
sudo snap install microk8s --classic
sudo usermod -a -G microk8s vagrant
sudo chown -f -R vagrant ~/.kube
microk8s kubectl config view --raw > ~/.kube/config
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 18 - Runner kubernetes

* installation de kubectl

```
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt update && sudo apt install -y kubectl
kubectl get nodes
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 18 - Runner kubernetes

* installation de helm

```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
sudo chmod +x get_helm.sh
./get_helm.sh
helm list
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 18 - Runner kubernetes


* installation du dépôt de charts gitlab

```
sudo vim /etc/hosts
helm repo add gitlab https://charts.gitlab.io
helm repo update
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 18 - Runner kubernetes


* édit des valeurs

```
cat values.yaml (https://gitlab.com/gitlab-org/charts/gitlab-runner/blob/main/values.yaml)
gitlabUrl: "http://xavki.gitlab"
runnerRegistrationToken: "ra7jHgHxjKqF1HsU-ios"
metrics:
  enabled: false
runners:
  config: |
    [[runners]]
      pre_clone_script = "echo '192.168.12.40 xavki.gitlab' >> /etc/hosts"
      name = "kub1"
      executor = "kubernetes"
      [runners.kubernetes]
        namespace = "gitlab-runner"
        poll_timeout = 600
        cpu_request = "1"
        service_cpu_request = "200m"
        [[runners.kubernetes.volumes.host_path]]
            name = "docker"
            mount_path = "/var/run/docker.sock"
            host_path = "/var/run/docker.sock"
hostAliases:
  - ip: "192.168.12.40"
    hostnames:
    - "xavki.gitlab"
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 18 - Runner kubernetes

* installation

```
kubectl create ns gitlab-runner
helm install --namespace gitlab-runner gitlab-runner gitlab/gitlab-runner -f values.yaml
```

* test


%title: GITLAB
%author: xavki


# GITLAB : 19 - Les runners partagés


<br>

* niveau admin

Deux manières :

		* soit à la création Admin > overview > runners

		* soit à partir d'un runner déjà existant


%title: GITLAB
%author: xavki


# GITLAB : 20 - Les Variables


<br>

* très importantes et utiles :
		* secrets
		* sha1 commit
		* taguer des images
		* partager entre les jobs

* différents types de variables :
		* les variables prédéfinies
		* du fichier gitlab-ci : local vs global (job)
		* du projet (settings > cicd)
		* du groupe
		* de l'instance

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables



VARIABLES PREDEFINIES


<br>

* liste : https://docs.gitlab.com/ee/ci/variables/predefined_variables.html

<br>

* sans stage (juste des jobs)

```
start-job: 
  tags:
    - shell     
  script:
    - echo "Start..."
    - echo "$CI_JOB_ID"
end-job:
  tags:
    - shell     
  script:
    - echo "ended !!"  
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

VARIABLES GILAB-CI

<br>

* variables globales

```
variables:
  GLOBAL_VAR: "Hello"
start-job: 
  tags:
    - shell     
  script:
    - echo "Start..."
    - echo "$GLOBAL_VAR"
    - echo "ended !!"
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

<br>

* variables locales (à un job)

```
variables:
  GLOBAL_VAR: "Hello"
start-job: 
  tags:
    - shell
  variables:
    LOCAL_VAR: "Hello Xavki !!" 
  script:
    - echo "Start..."
    - echo "$LOCAL_VAR"
    - echo "ended !!"
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

<br>

* local vs global

```
variables:
  VAR: "Hello"
start-job: 
  tags:
    - shell
  variables:
    VAR: "Hello Xavki !!" 
  script:
    - echo "Start..."
    - echo "$VAR"
    - echo "ended !!"
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

<br>

GROUP & PROJET & FORM

* settings > CICD > Variables

```
start-job: 
  tags:
    - shell
  script:
    - echo "Start..."
    - echo "$PIPELINE_VAR"
    - echo "ended !!"
```


%title: GITLAB
%author: xavki


# GITLAB : 20 - Les Variables


<br>

* très importantes et utiles :
		* secrets
		* sha1 commit
		* taguer des images
		* partager entre les jobs

* différents types de variables :
		* les variables prédéfinies
		* du fichier gitlab-ci : local vs global (job)
		* du projet (settings > cicd)
		* du groupe
		* de l'instance

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables



VARIABLES PREDEFINIES


<br>

* liste : https://docs.gitlab.com/ee/ci/variables/predefined_variables.html

<br>

* sans stage (juste des jobs)

```
start-job: 
  tags:
    - shell     
  script:
    - echo "Start..."
    - echo "$CI_JOB_ID"
end-job:
  tags:
    - shell     
  script:
    - echo "ended !!"  
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

VARIABLES GILAB-CI

<br>

* variables globales

```
variables:
  GLOBAL_VAR: "Hello"
start-job: 
  tags:
    - shell     
  script:
    - echo "Start..."
    - echo "$GLOBAL_VAR"
    - echo "ended !!"
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

<br>

* variables locales (à un job)

```
variables:
  GLOBAL_VAR: "Hello"
start-job: 
  tags:
    - shell
  variables:
    LOCAL_VAR: "Hello Xavki !!" 
  script:
    - echo "Start..."
    - echo "$LOCAL_VAR"
    - echo "ended !!"
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

<br>

* local vs global

```
variables:
  VAR: "Hello"
start-job: 
  tags:
    - shell
  variables:
    VAR: "Hello Xavki !!" 
  script:
    - echo "Start..."
    - echo "$VAR"
    - echo "ended !!"
```

--------------------------------------------------------------------------

# GITLAB : 19 - Les Variables

<br>

GROUP & PROJET & FORM

* settings > CICD > Variables

```
start-job: 
  tags:
    - shell
  script:
    - echo "Start..."
    - echo "$PIPELINE_VAR"
    - echo "ended !!"
```


%title: GITLAB
%author: xavki


# GITLAB : 21 - Les Architectures de pipelines


<br>

Doc Gitlab : https://docs.gitlab.com/ee/ci/pipelines/pipeline_architectures.html

<br>

3 archis :

		* Basic pipelines

		* Direct Acyclic Graph (DAG) pipelines

		* Parent/enfants pipelines : place à votre imagination...


-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

BASIC PIPELINE

<br>

		Etapes		Stage1		Stage2		Stage3
		Jobs
						Job1		Job3			Job5
						Job2		Job4			Job6

-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

```
stages:
  - stage1
  - stage2
job1:
  stage: stage1
  script:
    - echo "stage1 - job1"
job2:
  stage: stage1
  script:
    - echo "stage1 - job2"
job3:
  stage: stage2
  script:
    - echo "stage2 - job3"
job4:
  stage: stage2
  script:
    - echo "stage2 - job4"
...
```

-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

DAG PIPELINE

```
		Stage1	>		Stage2	>		Stage3		

		Job1		>		Job2		>		Job3

		Job3		>		Job5		>		Job6
```

Note : ordre des jobs mais dépendances respectées

-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

```
stages:
  - stage1
  - stage2
  - stage3
job1:
  stage: stage1
  script:
    - echo "stage1 - job1"
    - exit 1
job4:
  stage: stage1
  script:
    - echo "stage1 - job4"
job2:
  stage: stage2
  needs: [job1]
  script:
    - echo "stage2 - job2"
job5:
  stage: stage2
  needs: [job4]
  script:
    - echo "stage2 - job5"
...
```

-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

PARENT/ENFANTS PIPELINE

* découper en différent gitlab-ci
* gestion de déclenchement suivant des répertoires spécifiques
* gestion de blocs


Pipeline

		caseA : stage1	stage2	stage3
		caseB : stage21	stage22	stage23

-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

```
stages:
    - stage1
    - stage2
    - stage3
job1:
    stage: stage1
    script:
        - echo "caseA - job1"
job2:
    stage: stage2
    needs: [job1]
    script:
        - echo "caseA - job2"
job3:
    stage: stage3
    needs: [job2]
    script:
        - echo "caseA - job3"
```


-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

```
stages:
  - triggers

caseAjob:
  stage: triggers
  trigger:
    include: caseA/.gitlab-ci.yaml


caseBjob:
  stage: triggers
  needs: [caseAjob]
  trigger:
    include: caseB/.gitlab-ci.yaml
```

-----------------------------------------------------------------------------------------------------------------

# GITLAB : 21 - Les Architectures de pipelines


<br>

* règles de trigger

```
  rules:
    - changes:
        - caseA/*
```

%title: GITLAB
%author: xavki


# GITLAB : 22 - KeyWords : only, excepts & rules


<br>

Doc : https://docs.gitlab.com/ee/ci/yaml/#only--except

* Keyword de jobs

* only : quand un job doit être lancé

* except : quand un job NE DOIT PAS être lancé

```
only and except are not being actively developed. 
rules is the preferred keyword to control when to add jobs to pipelines.
```

-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

Applicable à 4 sous keywords :

		* refs

		* variables

		* changes

		* kubernetes 

-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>


REFS

* nom de branches (nom ou regex) ou type de pipeline (merge_requests, api, schedules...)

* 2 types d'écriture :

```
  only:
    refs:
      - branches
```

ou

```
  only:
    - branches
```

-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* exemple :

```
stages:
    - build
    - test
    - deploy
build:
    stage: build
    script:
        - echo "build"
    only:
        refs:
            - tags
test:
    stage: test
    script:
        - echo "test"
    except:
        refs:
            - tags
deploy:
    stage: deploy
    script:
        - echo "deploy"
    except:
        refs:
            - /^xp-.*$/
```

-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>


VARIABLES

* utilisation de variables définies et leurs expressions dans la CI/CD

```
$VARIABLE == "some value"		# à une valuer
$VARIABLE_1 == $VARIABLE_2	# à une autre variable
$VARIABLE == null						# si la variable est définie
$VARIABLE 									# si la variable existe
$VARIABLE =~ /^content.*/		# un pattern
$VARIABLE1 =~ /^content.*/ || $VARIABLE2 =~ /thing$/ && $VARIABLE3 # combinaison
$CI_COMMIT_BRANCH == "my-branch" || (($VARIABLE1 == "thing" || $VARIABLE2 == "thing") && $VARIABLE3)
```

-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* exemple

```
build:
    stage: build
    script:
        - echo "build"
    only:
        variables:
            - $VARIABLE1 == "xavki" && $VARIABLE2 == "xavki"
```


-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* exemple

```
build:
    stage: build
    script:
        - echo "build"
    only:
        variables:
            - $VARIABLE1 == "xavki"
        refs:
            - /^xp-.*$/
```


-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

CHANGES

* observation une partie spécifique du dépôt (répertoires, fichiers

* prend des valeurs :
		* chemin de fichiers
		* avec wildcard case1/*/*
		* avec du glob case1/*/*.{yaml,yml}

-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* exemple

```
    except:
        changes:
            - ".gitlab-ci.*"
```

-----------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>


KUBERNETES

* si le service kubernetes de gitlab est activé

```
deploy:
  only:
    kubernetes: active
```

%title: GITLAB
%author: xavki


# GITLAB : 23 - Les Services


<br>

Doc : https://docs.gitlab.com/ee/ci/services/


* services nécessaires dans le cadre de la CI : build, test
		* base de données
		* réponse d'api...

* par défaut : mysql, postgres, redis, gitlab

-----------------------------------------------------------------------------------------------

# GITLAB : 23 - Les Services


<br>

* exemple postgresql

```
variables:
  POSTGRES_DB: postgres
  POSTGRES_USER: runner
  POSTGRES_PASSWORD: postgres
  POSTGRES_HOST_AUTH_METHOD: trust
stages:    
  - test
Testing:
  stage: test
  image: debian:latest
  services:
    - postgres
  script:
    - apt update && apt install -y postgresql-client
    - PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h postgres -d postgres -c "\l"
  tags:
  - docker
```

-----------------------------------------------------------------------------------------------

# GITLAB : 23 - Les Services


<br>


```
  services:
    - name: postgres:14.1-alpine
      alias: mydb
```

-----------------------------------------------------------------------------------------------

# GITLAB : 23 - Les Services


<br>


```
Testing:
  stage: test
  image: debian:latest
  services:
    - name: postgres:14.1-alpine
      alias: mydb1
    - name: postgres:10.19-stretch
      alias: mydb2
    - name: postgres:9-alpine3.14
      alias: mydb3
  script:
    - apt update && apt install -y postgresql-client
    - PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h mydb1 -d postgres -c "SELECT version();"
    - PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h mydb2 -d postgres -c "SELECT version();"
    - PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h mydb3 -d postgres -c "SELECT version();"
  tags:
  - docker
```

-----------------------------------------------------------------------------------------------

# GITLAB : 23 - Les Services


<br>

* pour mysql


```
variables:
  MYSQL_DATABASE: "db_name"
  MYSQL_ROOT_PASSWORD: "dbpass"
  MYSQL_USER: "username"
  MYSQL_PASSWORD: "dbpass"
  MYSQL_HOST: mysql
stages:    
  - test
Testing:
  image: debian:latest
  services:
    - mysql
  stage: test
  script:
    - apt update && apt install -y mariadb-client
    - echo "SHOW tables;" | mysql -u root -p"$MYSQL_ROOT_PASSWORD" -h mysql "${MYSQL_DATABASE}"
    - echo "CREATE TABLE toto (field1 int);" | mysql -u root -p"$MYSQL_ROOT_PASSWORD" -h mysql "${MYSQL_DATABASE}"
    - echo "SHOW tables;" | mysql -u root -p"$MYSQL_ROOT_PASSWORD" -h mysql "${MYSQL_DATABASE}"
  tags: 
    - docker
```

-----------------------------------------------------------------------------------------------

# GITLAB : 23 - Les Services


<br>

* autre image

```
Testing:
  stage: test
  image: debian:latest
  services:
    - name: nginx:latest
      alias: mynginx
  script:
    - apt update -qq 2>&1 >/dev/null && apt -qq install -y curl 2>&1 >/dev/null
    - curl mynginx
  tags:
  - docker
```


%title: GITLAB
%author: xavki


# GITLAB : 24 - Le CACHE


<br>

Deux modes de stockage pour gitlabci :

		* cache

		* artifacts

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

CACHE

		* stocker et partager des libs et des packages

		* au niveau du runner (utiliser le même pour les jobs)

	  * réutilisable (intérêt du tag)

		* organiser éventuellement en fonction de vos workflows

		* cache distribué via du stockage objet S3 (multi-runners)

		* utilisation de clef pour définir diff caches

		* CACHE_FALLBACK_KEY (variable) pour définir une clef par défaut

		* désactivable sur demande ( cache:[] )

		* utilisation des ancres possibles

		* définition de policy possibles

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* exemple simple (avec/sans fichier)

cache:
  - key:
      #files:
      #  - xavki.txt
    paths:
      - .lib
stages:
  - step1
  - step2
j1:
  stage: step1
  script:
    - mkdir -p .lib 
    - echo toto > .lib/xavki.txt
  tags:
    - docker
j2:
  stage: step2
  script: cat .lib/xavki.txt
  tags:
    - docker

Rq : clear cache

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules


<br>

* si ajout d'une branche

```
cache
  - key: 
    paths:
      - .lib
stages:
  - step1
  - step2
j1:
  stage: step1
  script:
    - mkdir -p .lib 
    - echo toto > .lib/test.txt
  tags:
    - docker
  only:
    - main
j2:
  stage: step2
  script: cat .lib/test.txt
  tags:
    - docker
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* solution = utilisation des variables comme clefs

```
cache:
  - key: $CI_COMMIT_REF_SLUG
    paths:
      - .lib
stages:
  - step1
  - step2
j1:
  stage: step1
  script:
    - mkdir -p .lib 
    - echo $CI_COMMIT_REF_SLUG > .lib/$CI_COMMIT_REF_SLUG.txt
  tags:
    - docker
j2:
  stage: step2
  script: 
    - cat .lib/$CI_COMMIT_REF_SLUG.txt
    - ls .lib/
  tags:
    - docker
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* idem pour les stage

```
stages:
  - step1
  - step2
j1-1:
  stage: step1
  script:
    - mkdir -p .lib 
    - echo $CI_COMMIT_REF_SLUG-$CI_JOB_STAGE > .lib/$CI_COMMIT_REF_SLUG-$CI_JOB_STAGE.txt
  cache:
    - key: $CI_JOB_STAGE-$CI_COMMIT_REF_SLUG
      paths:
        - .lib
  tags:
    - docker
j1-2:
  stage: step1
  script:
    - cat .lib/$CI_COMMIT_REF_SLUG-$CI_JOB_STAGE.txt
    - ls .lib/
  cache:
    - key: $CI_JOB_STAGE-$CI_COMMIT_REF_SLUG
      paths:
        - .lib
  tags:
    - docker
...
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

Plus généralement :

* par branche cache

cache:
  key: $CI_COMMIT_REF_SLUG

* par job et branche

cache:
  key: "$CI_JOB_NAME-$CI_COMMIT_REF_SLUG"

* par stage et branche

cache:
  key: "$CI_JOB_STAGE-$CI_COMMIT_REF_SLUG"

* pour le partager entre le job de diff branches

cache:
  key: $CI_JOB_NAME

* pour le partager partout (branches, jobs...)

cache:
  key: one-key-to-rule-them-all


---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules


CLEAN

<br>

* repartir avec un cache vide > changer de key

sinon

    On the top bar, select Menu > Projects and find your project.
    On the left sidebar, select CI/CD > Pipelines page.
    In the top right, select Clear runner caches. 

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

POLICIES

<br>

* différentes policy


    pull : récupère le cache (début de job) mais le met pas à jour
    push : ne récupère pas mais pousse dans le cache (find e job)
    pull-push (default) 

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* désactivé la mise à jour du cache (clean avant pour tester)

```
stages:
  - step1
  - step2
j1-1:
  stage: step1
  script:
    - mkdir -p .lib 
    - echo $CI_COMMIT_REF_SLUG-$CI_JOB_STAGE > .lib/$CI_COMMIT_REF_SLUG-$CI_JOB_STAGE.txt
  cache:
    - key: $CI_JOB_STAGE-$CI_COMMIT_REF_SLUG
      paths:
        - .lib
      policy: pull
  tags:
    - docker
j1-2:
  stage: step1
  script:
    - cat .lib/$CI_COMMIT_REF_SLUG-$CI_JOB_STAGE.txt
    - ls .lib/
  cache:
    - key: $CI_JOB_STAGE-$CI_COMMIT_REF_SLUG
      paths:
        - .lib
  tags:
    - docker
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* cache masqué

```
stages:
  - step1
.dependencies_cache:
  cache:
    - key: $CI_COMMIT_SHA
      paths:
        - .lib
j1-1:
  stage: step1
  script:
    - mkdir -p .lib 
    - echo "toto" > .lib/test.txt
  extends: .dependencies_cache
  tags:
    - docker

j1-2:
  stage: step1
  script:
    - ls .lib 
    - cat .lib/test.txt
  extends: .dependencies_cache
  tags:
    - docker
```

---------------------------------------------------------------------------------------------------------

# GITLAB : 22 - KeyWords : only, excepts & rules

<br>

* exemple  service/cache

```
variables:
  VARIABLES_FILE: ./myapp1/variables.txt
  POSTGRES_DB: postgres
  POSTGRES_USER: runner
  POSTGRES_PASSWORD: postgres
  POSTGRES_HOST_AUTH_METHOD: trust
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository -Dstyle.color=always"
cache:
  paths:
    - .m2
stages:
    - test
    - build_jar
Test:
  stage: test
  image: maven:3.5.0-jdk-8
  services:
    - postgres
  script:
    - mvn ${MAVEN_OPTS} -B clean test
    - MVN_VERSION=$(mvn --non-recursive help:evaluate -Dexpression=project.version | grep -v '\[.*')
    - echo $MVN_VERSION
    - echo "export MVN_VERSION=$MVN_VERSION" > variables.txt
  tags:
  - docker
Build_Jar:
  stage: build_jar
  image: maven:3.5.0-jdk-8
  services:
    - postgres
  script:
    - 'mvn ${MAVEN_OPTS} -Drevision=x.y.z-SUFFIX -B clean install ' 
  tags:
  - docker
```

%title: GITLAB
%author: xavki


# GITLAB : 25 - Les ARTIFACTS


<br>

Deux modes de stockage pour gitlabci :

		* cache : sur les runners (cf vidéos précédentes)

		* artifacts : sur l'instance gitlab

Artifacts : disponible une fois le pipeline terminé

		* pour les jobs

		* pour les pipelines (en fin) : coverage


Attention stockage :
		
		* gitlab.yml (suppression par défaut)

Changement de localisation :

```
artifacts:
  enabled: true
  path: /mnt/storage/artifacts
```

-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

Options des artifacts :

		* expire_in : temps de conservation

		* untracked : ajout des fichiers untracked à votre artifact

		* exclude : exclure certains fichiers

		* paths : répertoire complet

		* expose_as : mettre à disposition dans les MR

		* name : nom associé (stratégie comme cache)


-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

* simple exemple

```
job1:
  script:
    - echo "toto" > file.txt
  artifacts:
    paths:
      - file.txt
```

-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

* avec expiration

```
job1:
  script:
    - echo "toto" > file.txt
  artifacts:
    paths:
      - file.txt
    expire_in: 1m
```

Note : non supprimé si pas de nouveaux artifacts

-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

* définir un nom

```
job1:
  script:
    - echo "toto" > file.txt
  artifacts:
    paths:
      - file.txt
    expire_in: 1m
    name: "$CI_JOB_NAME"
```

-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

* exclure des fichiers ou répertoires

```
job1:
  script:
    - echo "toto" > file.txt
  artifacts:
    paths:
      - ./
    expire_in: 1m
    name: "$CI_JOB_NAME"
    exclude: 
      - "*.yml"
      - ".git/**"
```

-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

* download via pipeline

```
job1:
  script:
    - echo "toto" > file.txt
  artifacts:
    paths:
      - file.txt
    expire_in: 1m
    name: $CI_JOB_NAME
job2:
  script:
    - echo "toto" > file2.txt
  artifacts:
    paths:
      - file2.txt
    expire_in: 1m
    name: $CI_JOB_NAME
```


-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>


* joindre à une MR

```
job1:
  script:
    - echo "toto" > file.txt
  artifacts:
    paths:
      - file.txt
    expire_in: 1m
    name: $CI_JOB_NAME
    expose_as: file_job
```

-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

* exemple pratique :

```
variables: 
  POSTGRES_DB: postgres
  POSTGRES_USER: runner
  POSTGRES_PASSWORD: postgres
  POSTGRES_HOST_AUTH_METHOD: trust
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository -Dstyle.color=always"
Build_Jar:
  image: maven:3.5.0-jdk-8
  services:
    - postgres
  script:
    - cd myapp1/
    - 'mvn ${MAVEN_OPTS} -Drevision=x.y.z-SUFFIX -B clean install ' 
  tags:
  - docker
  artifacts:
    paths:
      - myapp1/target/*.jar
    expire_in: 7 days
```


-----------------------------------------------------------------------------------

# GITLAB : 25 - Les ARTIFACTS


<br>

* ne conserver que le dernier par défaut

    Menu > Projects
    Settings > CI/CD
    Expand Artifacts
    Clear the Keep artifacts from most recent successful jobs checkbox

<br>

* remove artifact

		aller sur la page de job
		en haut à droite au-dessus des logs
		Erase job log


%title: GITLAB
%author: xavki


# GITLAB : 26 - SSH runner vers target


<br>

Pré-requis :

		* créer une paire de clefs

		* créer un user (avec les droits souhaités)

		* ajouter la clef publique sur le serveur cible


----------------------------------------------------------------------------

# GITLAB : 26 - SSH runner vers target

<br>

* création du user

```
ssh-keygen -t ecdsa -b 521
sudo adduser
sudo usermod -aG sudo gitlab
sudo su - gitlab
mkdir .ssh
vim .ssh/authorized_keys
```

----------------------------------------------------------------------------

# GITLAB : 26 - SSH runner vers target

<br>

PIPELINE

* création des variables

```
SSH_PRIVATE
SSH_TARGET
SSH_USER
SUDO_USER_PWD
```

----------------------------------------------------------------------------

# GITLAB : 26 - SSH runner vers target

<br>

* configuration de SSH dans notre runner (docker ou non)

```
image: debian:latest
job1:
  before_script:
    - 'command -v ssh-agent >/dev/null || ( apt update && apt install -y openssh-client )' 
    - eval $(ssh-agent -s)
    - echo "$SSH_PRIVATE" | tr -d '\r' | ssh-add -
    - mkdir -p ~/.ssh
    - chmod 700 ~/.ssh
    - ssh-keyscan $SSH_TARGET >> ~/.ssh/known_hosts
    - chmod 644 ~/.ssh/known_hosts
```

----------------------------------------------------------------------------

# GITLAB : 26 - SSH runner vers target

<br>

* test de ssh

```
  script:
  - ssh $SSH_USER@$SSH_TARGET "hostname"
  tags:
    - docker
```

----------------------------------------------------------------------------

# GITLAB : 26 - SSH runner vers target

<br>

* et ansible ???

```
  script:
  - ansible -i "$SSH_TARGET," all -u $SSH_USER -m command -a uptime
```

----------------------------------------------------------------------------

# GITLAB : 26 - SSH runner vers target

<br>

* adaptation

```
...
        - echo "[all]" > inventory.ini
        - echo "$SSH_TARGET" >> inventory.ini
        - ANSIBLE_BECOME_PASS=$SUDO_USER_PWD ansible-playbook -i inventory.ini -l $SSH_TARGET -u $SSH_USER play.yml
```

```
-   name: my playbook
    hosts: all
    become: yes
    tasks:
    - name: t1
      apt: 
        name: nginx
        state: latest
```

%title: GITLAB
%author: xavki


# GITLAB : 27 - Les ANCRES pour gérer la répétition

<br>

Pour l'exemple :

		* duplication du serveur target1

		* user spécifique

		* ip spécifique

YAML > les ancres

----------------------------------------------------------------------

# GITLAB : 27 - Les ANCRES pour gérer la répétition

<br>

* définition d'un ancre

```
.ssh: &ssh
  - cmd1
  - cmd2
...
```

<br>

* utilisation d'un ancre

```
    before_script: *ssh
```

%title: GITLAB
%author: xavki


# GITLAB : 28 - La REGISTRY Docker

<br>

* problématique :

		* activer la registry

		* bénéficier d'une registry vérified via https

		* génération d'un certificat auto-signé

------------------------------------------------------------------------------

# GITLAB : 28 - La REGISTRY Docker


<br>

* configuration de gitlab

```
gitlab_rails['gitlab_default_projects_features_container_registry'] = true

registry_external_url 'https://registry.xavki.gitlab'

gitlab_rails['registry_enabled'] = true
gitlab_rails['registry_host'] = "registry.xavki.gitlab"


registry_nginx['enable'] = true
registry_nginx['listen_port'] = 443
registry_nginx['ssl_certificate'] = "/etc/gitlab/registry.xavki.gitlab.cert"
registry_nginx['ssl_certificate_key'] = "/etc/gitlab/registry.xavki.gitlab.key"
```

------------------------------------------------------------------------------

# GITLAB : 28 - La REGISTRY Docker


<br>

* génération du certificat auto-signé

```
sudo openssl req   -newkey rsa:4096 -nodes -sha256 -keyout registry.xavki.gitlab/registry.xavki.gitlab.key  -addext "subjectAltName = DNS:registry.xavki.gitlab" -x509 -days 365 -out registry.xavki.gitlab/registry.xavki.gitlab.cert
```

<br>

* reconfigure de gitlab

```
gitlab-ctl reconfigure
```

------------------------------------------------------------------------------

# GITLAB : 28 - La REGISTRY Docker


<br>

* gestion du cert auto-signé pour un client

```
docker login registry.xavki.gitlab
openssl s_client -showcerts -connect registry.xavki.gitlab:443 < /dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ca.crt
cat ca.crt
sudo cp ca.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
systemctl restart docker
docker login registry.xavki.gitlab
```


%title: GITLAB
%author: xavki


# GITLAB : 29 - CI : build + push

<br>

Build d'une image 

		* utilisation de docker in docker

		* attention au certificat de la registry

---------------------------------------------------------------------------------------------

# GITLAB : 29 - CI : build + push

<br>

* ajout du certificat sur la vm du runner

```
openssl s_client -showcerts -connect registry.xavki.gitlab:443 < /dev/null | sed -ne '/-BEGIN CERT
IFICATE-/,/-END CERTIFICATE-/p' > /usr/local/share/ca-certificates/registry.crt
update-ca-certificates
```

<br>

* changement de la conf du runner

```
    volumes = ["/cache", "/etc/ssl/certs:/etc/ssl/certs:ro"]
```

```
docker restart gitlab-runner
```

---------------------------------------------------------------------------------------------

# GITLAB : 29 - CI : build + push

<br>

````
stages:
    - build
build image:
    stage: build
    image: docker
    services:
        - name: docker:dind
          alias: docker
    variables:
        DOCKER_BUILDKIT: "1"
        DOCKER_DRIVER: overlay2
        DOCKER_HOST: tcp://docker:2375
        DOCKER_TLS_CERTDIR: ""
    script:
        - docker build  -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
                        -t $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
                        .
        - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
        - docker push   $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
        - docker push   $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
    tags:
        - docker
```

%title: GITLAB
%author: xavki


# GITLAB : 30 - CI : MultiProject Pipeline - Base

<br>

Objectif : 

		* à part d'un projet déclencher le pipeline d'un autre projet

		* transmettre une variable d'un gitlab-ci à un autre

Doc : https://docs.gitlab.com/ee/ci/pipelines/multi_project_pipelines.html


-------------------------------------------------------------------------------------------------

# GITLAB : 30 - CI : MultiProject Pipeline - Base


<br>

* job amont (déclenché) - projet : pipeline2


```
image: debian:latest
job1:
    except:
        changes:
            - ".gitlab-ci.*"
    only:
        - pipelines
    script:
        - echo $VAR1
        - echo $VAR2
    tags:
        - docker
```

-------------------------------------------------------------------------------------------------

# GITLAB : 30 - CI : MultiProject Pipeline - Base


<br>

* job aval (déclencheur) - pojet : pipeline1

```
stages:
    - s1
    - s2
j1:
    stage: s1
    image: docker
    script:
        - echo "Mon premier job !!!"
    tags:
        - docker
    except:
        changes:
            - ".gitlab-ci.*"
j2:
    variables:
        VAR1: "variable1"
        VAR1: "variable1"
    stage: s2
    trigger:
        project: xavki/pipeline2
        branch: main
        strategy: depend
    except:
        changes:
            - ".gitlab-ci.*"
```

-------------------------------------------------------------------------------------------------

# GITLAB : 30 - CI : MultiProject Pipeline - Base


<br>

Prochaine vidéo :

		pipeline 1 > pipeline 2 (ansible db/user Postgres)




