
# Jenkins : sommaire







<br>


## 1- Introduction et installation

<br>

%title: Jenkins
%author: xavki

-> Jenkins <-
========


<br>


* ordonnanceur / Scheduleur

- run de jobs

- pipeline d'intégration continue : build / run / test

- java / open source

- utilisé en devops (comme gitlab ci)

- 1000 plugins

- GUI : port 8080

- CLI possible

<br>


* site

```
https://jenkins.io/
```

----------------------------------------------------------------------------------------

-> Installation jenkins <-



<br>


* installation par paquet


```
https://pkg.jenkins.io/debian-stable/

```

ou


```
wget -q -O -http://pkg.jenckins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt-get update

sudo apt-get install jenkins
```


Attention à la clef : 

```
/var/jenkins_home/secrets/initialAdminPassword
```

----------------------------------------------------------------------------


Key:
eda4060eb8404c3d985800c96c7841e8


------------------------------------------------------------

## 2. Premier job

<br>


## 3. Configuration générale

<br>


## 4. Gestion des utilisateurs et des rôles

<br>

* ajout du plugin : Role-based Authorization Strategy




* permet :
		* roles (groupes d'ensemble de users)
		* users



* affectation de tâches à un rôle
 
Par exemple : développeurs, sysadmin...

* affectation d'un pattern de jobs à un rôle : Java. Python.


## 5. Triggers et remote url

-> Jenkins : Trigger et lancement distant <-
========



<br>


* trigger :
		* sur échec
		* sur réussite
		* dans tous les cas

<br>

 
* exemple :

1er job :

```
echo "Hello World"
```

2ème job :


```
Merci !!
```

----------------------------------------------------------------------------


-> Mode remote via url <-



* pour lancer un job via une autre machine

* pour lancer un job via un site



<br>



* exemple avec MonPremierJob

* création d'un token


<br>


## 6. Planification de build

<br>


## 7. Les variables de build


------------------------------------------------------------



## 8. Premier : build / run / test

<br>


## 9. Plugin : Git

<br>


## 10. Trigger Git

<br>


## 11. Git push automatique

<br>


## 12. Les vues

<br>


## 13. Plugin : delivery pipeline

<br>


## 14. Maven : packager un projet avec jenkins

<br>


## 15. Premier pipeline

---------------------------------------------------------------



## 16. Pipeline : générateur de syntax

<br>


## 17. Pipeline : premier jenkinsfile

<br>


## 18. Docker : run d'un conteneur

<br>


## 19. Docker : build d'une image

<br>


## 20. Docker : push vers une registry

<br>

>
## 21. Pipeline : build maven, build docker et push registry

<br>


## 22. Ansible : première utilisation

<br>


## 23. Ansible : transmettre des variables

---------------------------------------------------------------


# Jenkins : sommaire


<br>


## 24. Pipeline: git, maven, docker et ansible

<br>


## 25. API : Liste déroulante auto-alimentée

<br>


## 26. API : Liste déroulante en cascade

<br>


## 27. API : utilisation des liste dans ansible

<br>


## 28. Jmeter : installation et plugin

<br>


## 29. Jmeter : création d'un plan de test

<br>


## 30. Jmeter : déploiement avec un plan de test final




