# Requirements
1. [Minikube](https://github.com/kubernetes/minikube)
    * Installation varies depending on platform, need to be able to successfully execute `minikube start`
2. Read through Louis Tiao's [walkthrough](http://louistiao.me/posts/walkthrough-deploying-a-flask-app-with-redis-queue-rq-workers-and-dashboard-using-kubernetes/), which this project follows. 

# Getting Started
1. `git clone https://github.com/DJO3/pytools.git`
2. `cd pytools/minikube`
3. `minikube start`
4. `eval $(minikube docker-env)`
5. `docker build -t djo3/web-flask-rq:v1 web-flask`
6. `docker build -t djo3/rq-worker:v1 rq-worker`
7. `docker build -t djo3/rq-dashboard:v1 rq-dashboard`
8. `kubectl create -f redis-master-deployment.yaml`
9. `kubectl create -f redis-master-service.yaml`
10. `kubectl create -f web-flask-deployment.yaml`
11. `kubectl create -f web-flask-service.yaml`
12. `kubectl create -f rq-worker-deployment.yaml`
13. `kubectl create -f rq-dashboard-deployment.yaml`
14. `kubectl create -f rq-dashboard-service.yaml`
15. To open the Kubernetes dashboard `minikube dashboard`
16. To open the Flask app `open "http://$(minikube ip):30010"`
17. To open the rq-dashboard `open "http://$(minikube ip):30020"`
18. To add a job and generate a job id `curl "http://$(minikube ip):30010/?start=23&stop=31"`
19. To check the results of a job, `curl "http://$(minikube ip):30010/results/<jobid>`
