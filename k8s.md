

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
