
-> Kubernetes : pourquoi ? <-


pour orchestrer : comme swarm (lancement orchestré de multiples conteneurs)
pour créer de l'abstraction avec la notion de service (plus en IP)
pour apporter de la haute disponibilité (maintenir les conteneurs up)
pour scaler : lancer de multiples instances en fonction de paramètres (à la main ou en automatique)

----------------
 Kubernetes : notions <-


Kubernetes apporte beaucoup de notions et de concepts

noeuds (serveurs) : physiques ou virtuels
- master ou simple noeud d'exécution

pods : pierre centrale de K8S
- ensemble cohérent de conteneurs
- un ou plusieurs conteneurs
- une instance de K8S

service : abstraction des pods
- permet d'éviter la communication par ip (changeante car on est en conteneurs)
- service > ip/port > pods
- service = ip et port fixe

-> Suites des notions <-

volumes: persistents ou non
- lieux d'échanges entre pods
- intérieur de pods = non persistent
- extérieur = persistent

deployments : objets de gestion des déploiments
- création/suppression
- scaling : gestion de paramètres pour la montée en charge (ou réduction)

namespaces : cluster virtuel (ensemble de services)
- sous ensemble pour cloisonner dans K8S

-----------------------
%title: Kubernetes 
%author: xavki
%Vidéos: [Formation Kubernetes](https://www.youtube.com/playlist?list=PLn6POgpklwWqfzaosSgX2XEKpse5VY2v5)
%blog: [Xavki Blog](https://xavki.blog)


-> Kubernetes : Prérequis <-


<br>

* Recommandations :

```
2 Gb ram
2 CPU
ouverture réseau large entre les 2 machines
Ports master : 6443 2379-2380 10250 10251 10252
Ports node : 10250 30000-32767
pas de swap
```

<br>

* prérequis : installation de docker

```
curl -fsSL https://get.docker.com | sh;
sudo usermod -aG docker $USER

groupadd -g 500000 dockremap && 
groupadd -g 501000 dockremap-user && 
useradd -u 500000 -g dockremap -s /bin/false dockremap && 
useradd -u 501000 -g dockremap-user -s /bin/false dockremap-user

echo "dockremap:500000:65536" >> /etc/subuid && 
echo "dockremap:500000:65536" >>/etc/subgid

echo "
  {
   \"userns-remap\": \"default\"
  }
" > /etc/docker/daemon.json

systemctl daemon-reload && systemctl restart docker

```

--------------------------------------------------------------------------------------------

-> Kubernetes : installation  <-

* désactivation du swap

<br>

```
swapoff -a
vim /etc/fstab
```

<br>

* mise en place du dépôt apt :

```
apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
sudo add-apt-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
```

<br>

* installation des binaires kubernetes :

```
sudo apt-get install -y kubelet kubeadm kubectl kubernetes-cni
systemctl enable kubelet
```

	- kubeadm : installation du cluster
	- kubelet : service qui tourne sur les machines (lancement pods...)
	- kubectl : permet la communication avec le cluster



---------------------------




creation d'un deployement ( deployer des applications sur un cluster avec kubectl)
  indique comment créer et maj des instances des applis
  
 kube-sheduler planifier des instances app sur les noueds
 Controler
 
 Déploiements Kubernetes
Une fois que vous avez un cluster Kubernetes en cours d'exécution, vous pouvez déployer vos applications conteneurisées par dessus. 
Pour ce faire, vous créez une configuration de Déploiement (Deployments) Kubernetes. 
Le déploiement instruit Kubernetes de comment créer et mettre à jour des instances de votre application. 
Une fois que vous avez créé un déploiement, le plannificateur de Kubernetes (kube-scheduler) planifient les instanciations d'application sur des nœuds du cluster.

Une fois les instances d’application créées, un contrôleur de déploiement Kubernetes surveille en permanence ces instances. 
Si le nœud hébergeant une instance tombe en panne ou est supprimé, le contrôleur de déploiement remplace l'instance par une instance située sur un autre nœud du cluster. 
Ceci fournit un mécanisme d'auto-réparation pour faire face aux pannes ou à la maintenance de la machine.


The goal of this interactive scenario is to deploy a local development Kubernetes cluster using minikube

minikube version
minikube start
kubectl version
kuectk cluster-info
kubectl get nodes



The goal of this scenario is to help you deploy your first app on Kubernetes using kubectl. You will learn the basics about kubectl cli and how to interact with your application.

    2  kubectl version
    3  kubectl get nodes
    4  kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
    5  kubectl get deployments
    
    sur un 2 ee terminal
      1  echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n"; 
      2  kubectl proxy

     sur le premier terminal
  
    7  curl http://localhost:8001/version
    9  curl http://localhost:8001/api/v1/namespaces/default/pods/$P
    
  un pod contient des resources suivantes :
   Stockage partagé, en tant que volumes
    Mise en réseau, en tant qu'adresse IP de cluster unique
    Informations sur l'exécution de chaque conteneur, telles que la version de l'image du conteneur ou les ports spécifiques à utiliser
    
  Chaque nœud Kubernetes exécute au moins :

    Kubelet, un processus responsable de la communication entre le plan de contrôle Kubernetes et le nœud ; il gère les Pods et les conteneurs s'exécutant sur une machine.
Un environnement d'exécution de conteneur (comme Docker) chargé d'extraire l'image du conteneur d'un registre, de décompresser le conteneur et d'exécuter l'application.

kubectl get - répertorie les ressources
kubectl describe - affiche des informations détaillées sur une ressource
kubectl logs - imprime les journaux d'un conteneur dans un pod
kubectl exec - exécute une commande sur un conteneur dans un pod 


 troubleshoot Kubernetes applications using the kubectl get, describe, logs and exec commands.
 
 a completer
 
 Using a Service to Expose Your App
 
Un service dans Kubernetes
Comprendre comment les étiquettes et les objets LabelSelector sont liés à un service
Exposer une application en dehors d'un cluster Kubernetes à l'aide d'un service

Les pods Kubernetes sont mortels. Les pods ont un cycle de vie . Lorsqu'un nœud de travail meurt, les pods exécutés sur le nœud sont également perdus.
Un ReplicaSet peut alors ramener dynamiquement le cluster à l'état souhaité via la création de nouveaux pods pour maintenir votre application en cours d'exécution.


Bien que chaque pod ait une adresse IP unique, ces adresses IP ne sont pas exposées en dehors du cluster sans service. Les services permettent à vos applications de recevoir du trafic. Les services peuvent être exposés de différentes manières en spécifiant a typedans la ServiceSpec :

ClusterIP (par défaut) - Expose le service sur une adresse IP interne dans le cluster. Ce type rend le service uniquement accessible depuis le cluster.
NodePort - Expose le service sur le même port de chaque nœud sélectionné dans le cluster à l'aide de NAT.
Rend un service accessible depuis l'extérieur du cluster à l'aide de <NodeIP>:<NodePort>. Surensemble de ClusterIP.
LoadBalancer - Crée un équilibreur de charge externe dans le cloud actuel (si pris en charge) et attribue une adresse IP externe fixe au service. 
	Surensemble de NodePort.
ExternalName - Mappe le Service sur le contenu du externalNamechamp (par exemple foo.bar.example.com), en renvoyant un CNAMEenregistrement avec sa valeur.
	Aucun proxy d'aucune sorte n'est mis en place. Ce type nécessite la version 1.7 ou supérieure de kube-dns, ou la version 0.0.8 ou supérieure de CoreDNS.
	

	Exposer votre application
--------------------------------
	    2  kubectl get pods
    3  kubectl get services
    4  kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
    5  kubectl get services
    6  kubectl describe services/kubernetes-bootcamp
    7  export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
    8  echo NODE_PORT=$NODE_PORT
    9  curl $(minikube ip):$NODE_PORT
   10  kubectl describe deployment
   11  kubectl get pods -l app=kubernetes-bootcamp
   12  kubectl get services -l app=kubernetes-bootcamp
   13  export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
   14  echo Name of the Pod: $POD_NAME
   15  kubectl label pods $POD_NAME version=v1
   16  kubectl describe pods $POD_NAME
   17  kubectl get pods -l version=v1
   19  kubectl get pods
   20  kubectl get services
   21  kubectl describe deployment
 
 
	
	------------------------------------
	Mise à l'échelle de votre application
	
	    2  kubectl get deployments
    3  kubectl get rs
    4  kubectl scale deployments/kubernetes-bootcamp --replicas=4
    5  kubectl get deployments
    6  kubectl get pods -o wide
    7  kubectl describe deployments/kubernetes-bootcamp
    8  kubectl describe services/kubernetes-bootcamp
    9  export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
   10  echo NODE_PORT=$NODE_PORT
   11  curl $(minikube ip):$NODE_PORT
   12  kubectl scale deployments/kubernetes-bootcamp --replicas=2
   13  kubectl get deployments
   14  kubectl get pods -o wide
	
	
	--------------------------------------------------
