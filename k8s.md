create kubernetes cluster
minikube version
minikube start
kubectl version
kuectk cluster-info
kubectl get nodes

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
