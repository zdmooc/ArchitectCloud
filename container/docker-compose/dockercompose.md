%title: Docker compose
%author: xavki

-> Docker compose : premiers pas <-
=========

-> Intérêts, pourquoi ? <-

* lancer des conteneurs à coordonner c'est pas facile (cf vidéo précédente microservices)

* meilleure gestion des dépendances (réseau, volumes...)

* un service comprend 1 à plusieurs conteneurs

* comme pour dockerfile : partage facile, versionning...

<br>
-> Installation <-

```
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

------------------------------------------------

->  Principales commandes <-

* un répertoire avec docker-compose.yml

* commandes similaires à docker (intuitives)

<br>
Lancement du service :

* docker-compose build
	- construction uniquement des images

* docker-compose up
	- build et run des images

* docker-compose up -d
	- mode détaché (docker run -d)

------------------------------------------------

->  Principales commandes <-

Gestion du service :

* docker-compose ps
	- état des services

* docker-compose start

* docker-compose stop

* docker-compose rm

------------------------------------------------

-> Plus fort... <-

* docker-compose scale SERVICE=3
	- lance 3 instances

* docker-compose pull
	- maj des images


------------------------------------------------

-> Exemple docker-compose.yml

```
version: '3'

services:
  myfirstservice:
    image: alpine
    restart: always
    container_name: MyAlpine
    entrypoint: ps aux

```



%title: Docker compose - première appli
%author: xavki - code/slides => lien description

-> Deployer une application <-
=========

<br>
-> L'application <-

* applicatif flask (python) = serveur web + applicatif
	- port 5000
	- réception html de GET/POST

* database redis (update/select)

<br>
* 4 fichiers :
	- docker-compose : orchestration
	- Dockerfile : créer image applicative
	- appl.py
	- requirements.txt : liste des module pip (pour l'image)
	- script shell de test


------------------------------------------------

->  Le docker-compose.yml <-

```
version: '3'
services:
  app:
    build: .
    image: flask-redis:1.0
    environment:
      - FLASK_ENV=development
    ports:
      - 5000:5000
  redis:
    image: redis:4.0.11-alpine

```


------------------------------------------------

-> Le Dockerfile <-

```
FROM python:3.7.0-alpine3.8
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
CMD flask run --host=0.0.0.0
```

-> Le requirements.txt <-

```
flask
redis
```

network


%title: Docker compose - volumes
%author: xavki - code/slides => lien description

-> Les volumes avec docker-compose <-
=========




* docker = définir un volume persistent externe
	- en cas de perte du conteneur = pas de perte data

* partager entre conteneur (cf exemple)

------------------------------------------------
-> Si gestion par docker <-

```
  redis:
    image: redis:4.0.11-alpine
    networks:
      - backend
    volumes:
      - dbdata:/data
```

et définition du volume

```
volumes:
  dbdata:
```

------------------------------------------------

-> Si chemin spécifique <-

un peu plus poussé...

```
volumes:
  dbdata:
    driver: local
    driver_opts:
      type: 'none'
      o: 'bind'
      device: '/srv/redis'

```

------------------------------------------------

-> Avantage multi-conteneurs <-

```
version: '3'
services:
  app:
    build: .
    image: flask-redis:1.0
    environment:
      - FLASK_ENV=development
    ports:
      - 5000:5000
    networks:
      - backend
      - frontend
    volumes:
      - dbdata:/data
  redis:
    image: redis:4.0.11-alpine
    networks:
      - backend
    volumes:
      - dbdata:/data

```

