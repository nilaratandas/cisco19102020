# Packaging and Namespace 

## Best practise to deploy application in k8s

## Deploying app in specific namespace 

## File 

```❯ cat package.yml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: ashuns
spec: {}
status: {}

---


apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: ashudep11
  name: ashudep11
  namespace: ashuns  #  adding namespace line 
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ashudep11
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: ashudep11
    spec:
      containers:
      - image: dockerashu/httpd:ashuappv2
        name: httpd
        resources: {}
status: {}

---

apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    app: ashusvcday5
  name: ashusvcday5
  namespace: ashuns # adding namespace line 
spec:
  ports:
  - name: 4444-80
    port: 4444
    protocol: TCP
    targetPort: 80
  selector:
    app: ashudep11  #  same as label of POD 
  type: LoadBalancer
status:
  loadBalancer: {}

```
===

```
❯ kubectl  apply -f  package.yml
namespace/ashuns created
deployment.apps/ashudep11 created
service/ashusvcday5 created
```

## history 

```
 371  kubectl  create  namespace  ashuns  --dry-run=client -o yaml  >package.yml 
  372  cat  package.yml
  373  hist
  374  history
  375  kubectl  create  deployment  ashudep11 --image=dockerashu/httpd:ashuappv2 --dry-run=client -o yaml >>package.yml
  376  hist
  377  history
  378  vim package.yml
  379  clear
  380  kubectl create service  loadbalancer  ashusvcday5  --tcp 4444:80  --dry-run=client -o yaml >>package.yml
  381  vim  package.yml
  382  kubectl get  ns
  383  kubectl  apply -f  package.yml 
  384  cat package.yml
  385  clear
  386  kubectl  get  ns
  387  kubectl  get  all  -n ashuns 
  388  kubectl  get  deploy,pod,svc -n ashuns
  389  kubectl get ns
  390  kubectl  get  deploy,pod,svc -n nikhilns
  391  kubectl  get  deploy,pod,svc -n ashuns
  392  kubectl delete all --all -n ashuns 
  393  kubectl apply -f  package.yml
  394  kubectl  get  deploy,pod,svc -n ashuns
  
 ```
 
 ## Database with persistent storage
 
 ```
 docker  run -d  --name mydb  -e  MYSQL_ROOT_PASSWORD=cisco123  -p 1234:3306 -v ashudbvol:/var/lib/mysql  mysql
 ```
 
 ## On kubenetes 
 
 ```
 ❯ kubectl  run   ashudb  --image=mysql --port 3306  --namespace  ashuns --dry-run=client -o yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: ashudb
  name: ashudb
  namespace: ashuns
spec:
  containers:
  - image: mysql
    name: ashudb
    ports:
    - containerPort: 3306
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
❯ kubectl  run   ashudb  --image=mysql --port 3306  --namespace  ashuns --dry-run=client -o yaml  >ashudb.yml

```

## using configMap to store variable data

```
kubectl  create  configmap  mydbpass   --from-literal  x=cisco1234 -n ashuns

