
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

-> Jenkins : Planification <-
========


* scheduler : dans "ce qui déclenche le build"


<br>


* même typo que les crons linux

```
MINUTE   HOUR   DOM   MONTH   DOW


MINUTE	Minutes within the hour (0–59)
HOUR	The hour of the day (0–23)
DOM	The day of the month (1–31)
MONTH	The month (1–12)
DOW	The day of the week (0–7) where 0 and 7 are Sunday.


``` 

------------------------------------------------------------



-> Exemples <-



* toutes les minutes

```
* * * * *
```


* toutes les 15 minutes

```
H/15 * * * *
```


* tous les lundis à 13h00

```
00 13 * * 1
```

<br>


## 7. Les variables de build

-> Jenkins : Paramètres <-
========

* plusieurs choix :

	- mot de passe : masqué lors de la saisie

	- string : classique

	- booléen : True/False

	- choix : liste

	- paramètre d'exécution

	- identifiants : gestion de secrets

	- fichiers

	- texte


## 8. Premier : build / run / test


mkdir -p /tmp/xavki/
rm -rf /tmp/xavki/*
echo '
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
'  >/tmp/xavki/Main.java
javac /tmp/xavki/Main.java
```


-------------------------------------------------------


-> RUN <-



* lancement du java avec écriture dans un fichier du résultat

* attention dépendance avec le build



```
cd /tmp/xavki/
java Main >test.file
```

-------------------------------------------------------



-> TEST <-


* dépendant du déclenchement du RUN

* un principe

* on affiche le contenu du fichier test.file (on pourrait faire des tests dessus)


```
cd /tmp/xavki/
echo "###### contenu du test.file ######"
cat test.file

<br>


## 9. Plugin : Git

-> Jenkins : Git et son trigger <-
-> Jenkins : Git et son trigger <-
========


<br>


* un dépôt :
https://github.com/priximmo/jenkins-helloworld

<br>


* build sans utilisation du plugin GIT

```
# clone
git clone https://github.com/priximmo/jenkins-helloworld

# déplacement
cd jenkins-helloworld

# compilation
javac Main.java

# lancement run
java Main
```

-------------------------------------------------------------


-> Avec Plugin GIT <-


<br>


* Gestion de Code Source : GIT


<br>


* git clone n'est plus nécessaire


* préciser bien la branche


* attention aux droits sur votre dépôt = credentials si nécessaire


<br>


* et directement placé dans le répertoire cloné


<br>


* build réduit :

```
javac Main.java

java Main
```


-------------------------------------------------------------



-> GIT - Trigger <-


<br>


* trigger : check à intervales réguliers 



* Ce qui déclenche le build : Scrutation de l'outil de gestion de version



* ajouter l'interval




## 10. Trigger Git

-> Jenkins : Git et son trigger <-
========


<br>


* un dépôt :
https://github.com/priximmo/jenkins-helloworld

<br>


* build sans utilisation du plugin GIT

```
# clone
git clone https://github.com/priximmo/jenkins-helloworld

# déplacement
cd jenkins-helloworld

# compilation
javac Main.java

# lancement run
java Main
```

-------------------------------------------------------------


-> Avec Plugin GIT <-


<br>


* Gestion de Code Source : GIT


<br>


* git clone n'est plus nécessaire


* préciser bien la branche


* attention aux droits sur votre dépôt = credentials si nécessaire


<br>


* et directement placé dans le répertoire cloné


<br>


* build réduit :

```
javac Main.java

java Main
```


-------------------------------------------------------------



-> GIT - Trigger <-


<br>


* trigger : check à intervales réguliers 



* Ce qui déclenche le build : Scrutation de l'outil de gestion de version



* ajouter l'interval

<br>


## 11. Git push automatique

-> Jenkins : Git push auto <-
========


<br>


* credentials à ajouter : login/mdp + ID


* exemple : si build = Ok => push d'un nouveau tag


* possiblité de pusher sur une autre branche


```
git config --global user.email "xav@moi.fr"
git config --global user.name "xavki"

javac Main.java
java Main
```

Rq : config git particulier


----------------------------------------------------------------


-> Action à la suite du build <-




* si succès



* TAG

```
Tag to push : VERSION-$BUILD_ID

Tag message : Jenkins Job

create new tag

update new tag


Target remote Name à définir et utiliser

```


<br>


## 12. Les vues
-> Jenkins : Les Vues<-


objectif : organiser le classement des jobs




soit une vue personnaliée


soit des vues de classement




permet de filtrer les files de lanceurs et de constructions



peut être alimentée par une regex de filtre (Java_ ...)
<br>


## 13. Plugin : delivery pipeline

-> Jenkins : Plugin Delivery<-

https://wiki.jenkins.io/display/JENKINS/Delivery+Pipeline+Plugin
<br>


## 14. Maven : packager un projet avec jenkins

-> Jenkins : Maven <-
Dépôt : https://github.com/priximmo/mvn-helloworld


install jenkins hors docker


https://jenkins.io/doc/book/installing/




install java :


sudo add-apt-repository ppa:linuxuprising/java
sudo apt-get update
sudo apt-get install oracle-java11-installer
sudo vim /etc/environment 

JAVA_HOME="/usr/lib/jvm/java-11-oracle/"



install maven :


sudo apt-get install maven



-> Maven dans jenkins <-


configuration global des outils



configuration maven



maven : MAVEN_HOME à définir


-> Pour un build <-



ajout d'un dépôt git avec un projet maven : pom.xml


build : définir les actions


post step :



java -jar target/helloworld-app-1.0-SNAPSHOT.jar
<br>


## 15. Premier pipeline


-> Jenkins : premier pipeline <-



pipeline: chaine d'actions / jobs décrits par du code (groovy)


modèle : https://jenkins.io/doc/book/pipeline/



pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // 
            }
        }
        stage('Test') { 
            steps {
                // 
            }
        }
        stage('Deploy') { 
            steps {
                // 
            }
        }
    }
}



Jenkinsfile : intégre directement ce script dans le dépôt


-> Exemple : clone / build / run <-



java helloworld


groovy :



pipeline {
    agent any 
    stages {
        stage('clone') { 
            steps {
                sh "rm -rf *"
                sh "git clone https://github.com/priximmo/jenkins-helloworld"
            }
        }
        stage('build') { 
            steps {
                sh "cd jenkins-helloworld/ && javac Main.java"
            }
        }
        stage('run') { 
            steps {
                sh "cd jenkins-helloworld/ && java Main"
            }
        }
    }
}



## 16. Pipeline : générateur de syntax

-> Jenkins Pipeline : générateur de syntax <-


modèle : https://jenkins.io/doc/book/pipeline/



pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // 
            }
        }
        stage('Test') { 
            steps {
                // 
            }
        }
        stage('Deploy') { 
            steps {
                // 
            }
        }
    }
}



-> Utilisateur de l'éditeur <-


java helloworld


https://github.com/priximmo/jenkins-helloworld/



groovy :


node {
    stage('clone') {
    git 'https://github.com/priximmo/jenkins-helloworld.git'
    sh label: '', script: '''ls
    javac Main.java
    java Main'''
}
}
<br>


## 17. Pipeline : premier jenkinsfile

-> Jenkins Pipeline : Jenkinsfile <-



Jenkinsfile : versionner


déclaratif


facile à utiliser sur d'autres serveurs



-> Toujours : clone / build / run <-


groovy :


pipeline {
    agent any
    stages {
        stage('Pull') {
            steps {
                checkout([$class: 'GitSCM',
                branches: [[name: '*/master']],
                doGenerateSubmoduleConfigurations: false,
                extensions: [],
                submoduleCfg: [],
                userRemoteConfigs: [[url: 'https://github.com/priximmo/jenkins-helloworld.git']]])
                sh "ls"
            }
        }
        stage('Build') {
            steps {
                sh "javac Main.java"
            }
        }
        stage('Run') {
            steps {
                sh "java Main"
            }
        }
    }
<br>


## 18. Docker : run d'un conteneur

-> Jenkins Pipeline : Docker <-



pourquoi ?


runner des conteneurs et travailler dedans (environnement personnalisé - ex: ubuntu:1804)


runner des conteneurs pour faire des test dessus


construire des images pour livrer et déployer en production


intégrer des tests sur conteneurs


attention : sudo usermod -aG docker $USER


si on simplifie, deux cas :
* agent : on travaille dans le conteneur (le conteneur est un host)
* node : on travaille de l'extérieur du conteneur (le conteneur est une cible)




doc : https://jenkins.io/doc/book/pipeline/docker/



->  Run d'un nginx <-

cas du node : on est à l'extérieur


node {
        docker.image('nginx:latest').withRun('-p 80:80') { c ->

        sh 'docker ps'

        sh 'curl localhost'

    }
}



cas de l'agent : on est dedans


pipeline {
    agent {
        docker {
            image 'nginx:latest'
            args '-p 80:80'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'cat /etc/nginx/conf.d/default.conf'
            }
        }
    }
}
<br>


## 19. Docker : build d'une image

-> Jenkins Pipeline : Docker Build<-


node{
  def app

    stage('Clone') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("xavki/nginx")
    }

    stage('Test image') {
        docker.image('xavki/nginx').withRun('-p 80:80') { c ->
        sh 'docker ps'
        sh 'curl localhost'
	     }
    }
}
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




