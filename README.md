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
