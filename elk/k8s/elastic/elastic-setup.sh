eval $(minikube docker-env) && \
kubectl apply -f k8s/elastic/elastic-manifest.yaml && \
kubectl delete -f k8s/elastic/elastic-deployment.yaml && \
kubectl create -f k8s/elastic/elastic-deployment.yaml
