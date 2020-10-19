# Docker Pre 

# DNS understanding 

<img src="dns.png">

## Web server

<img src="web.png">

## VMS vs Containers

<img src="vmc.png">

## containers platform provides


<img src="cpt.png">

# Installing Docker engine 

```
[ec2-user@ip-172-31-59-169 ~]$ sudo  yum  install  docker  
Failed to set locale, defaulting to C
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
amzn2-core                                                         | 3.7 kB  00:00:00     
Resolving Dependencies
--> Running transaction check
---> Package docker.x86_64 0:19.03.6ce-4.amzn2 will be installed
--> Processing Dependency: runc >= 1.0.0 for package: docker-19.03.6ce-4.amzn2.x86_64
--> Processing Dependency: containerd >= 1.3.2 for 
```

## Starting Docker engine 

```
[ec2-user@ip-172-31-59-169 ~]$ sudo systemctl  start  docker
[ec2-user@ip-172-31-59-169 ~]$ sudo systemctl  status  docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor preset: disabled)
   Active: active (running) since Mon 2020-10-19 07:14:14 UTC; 9s ago
     Docs: https://docs.docker.com
  Process: 3845 ExecStartPre=/usr/libexec/docker/docker-setup-runtimes.sh (code=exited, status=0/SUCCESS)
  Process: 3832 ExecStartPre=/bin/mkdir -p /run/docker (code=exited, status=0/SUCCESS)
 Main PID: 3855 (dockerd
 
 ```
 
 ## Docker architecture
 
 <img src="darch.png">
 
 ## Docker client options 
 
 <img src="dockerclients.png">
 
 ## Docker images are stored in PUblic/private Registries 
 
 ### Docker Hub 
 ###  Quay.io
 ###  GCR 
 
## Docker parent process understanding 

<img src="dockerpp.png">

