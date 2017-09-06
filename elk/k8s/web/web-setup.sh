eval $(minikube docker-env) && \
docker run -d -p 5000:5000 --name local_registry registry || docker restart local_registry && \
docker build -t localhost:5000/elk-web:1.0.0 web && \
docker push localhost:5000/elk-web:1.0.0 && \
sed -i '' "s|PWD_WEB|$PWD/web|g" k8s/web/web-deployment.yaml && \
kubectl apply -f k8s/web/web-deployment.yaml && \
kubectl delete -f k8s/web/web-deployment.yaml && \
kubectl create -f k8s/web/web-deployment.yaml && \
kubectl apply -f k8s/web/web-service.yaml
