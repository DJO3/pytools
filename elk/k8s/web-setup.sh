eval $(minikube docker-env) && \
docker run -d -p 5000:5000 --name local_registry registry || docker restart local_registry && \
docker build -t localhost:5000/elk-web:1.0.0 web && \
docker push localhost:5000/elk-web:1.0.0 && \
kubectl apply -f k8s/web-deployment.yaml && \
kubectl delete -f k8s/web-deployment.yaml && \
kubectl create -f k8s/web-deployment.yaml && \
kubectl apply -f k8s/web-service.yaml