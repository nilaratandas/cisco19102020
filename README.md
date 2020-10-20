# Containerization 

##  Convert an app/code/webserver/db/networkapp into container format 

<img src="cformat.png">

## Install docker again 

```
  5  sudo  yum install  docker  -y
    6  history 
    7  sudo systemctl start  docker 
    8  sudo systemctl status docker 
    9  history 
   10  sudo systemctl status docker 
   11  history 
   12  sudo systemctl enable  docker 

```

## Adding a non root user into docker group for Docker engine access

```
[ec2-user@ip-172-31-58-55 ~]$ grep  docker    /etc/group   
docker:x:993:
[ec2-user@ip-172-31-58-55 ~]$ 
[ec2-user@ip-172-31-58-55 ~]$ 
[ec2-user@ip-172-31-58-55 ~]$ whoami
ec2-user
[ec2-user@ip-172-31-58-55 ~]$ 
[ec2-user@ip-172-31-58-55 ~]$ 
[ec2-user@ip-172-31-58-55 ~]$ sudo  usermod  -a  -G  docker  ec2-user
[ec2-user@ip-172-31-58-55 ~]$ 
[ec2-user@ip-172-31-58-55 ~]$ grep  docker    /etc/group   
docker:x:993:ec2-user
[ec2-user@ip-172-31-58-55 ~]$ 

```

## Webapp Source Code into Docker image

<img src="s2i.png">

## web server overview

<img src="webserver.png">


## Building Docker image

```
[ec2-user@ip-172-31-58-55 beginner-html-site-styled]$ docker  build  -t   http:ashuappv1  . 
Sending build context to Docker daemon     64kB
Step 1/5 : FROM  httpd
latest: Pulling from library/httpd
bb79b6b2107f: Pull complete 
26694ef5449a: Pull complete 
7b85101950dd: Pull complete 
da919f2696f2: Pull complete 
3ae86ea9f1b9: Pull complete 
Digest: sha256:b82fb56847fcbcca9f8f162a3232acb4a302af96b1b2af1c4c3ac45ef0c9b968
Status: Downloaded newer image for httpd:latest
 ---> 3dd970e6b110
Step 2/5 : MAINTAINER   ashutoshh@linux.com , 9509957594  , ashutoshh
 ---> Running in 4378c1da9fa0
Removing intermediate container 4378c1da9fa0
 ---> 20297490d511
Step 3/5 : WORKDIR  /var/www/html/
 ---> Running in 86f0e69c2259
Removing intermediate container 86f0e69c2259
 ---> 1771cce3f316
Step 4/5 : COPY .  .
 ---> 03c914bdf111
Step 5/5 : EXPOSE 80
 ---> Running in 6b752c32b199
Removing intermediate container 6b752c32b199
 ---> 46d3fcf3d21e
Successfully built 46d3fcf3d21e
Successfully tagged http:ashuappv1

```

## Now creating container 

```
 docker  run -d --name x2  -p 1111:80  http:dasv1 
 
 ```
 
 ## html app with Dockerfile 
 
 ```
 FROM  centos
MAINTAINER  ashutoshh@linux.com
RUN  yum  install  httpd mod_ssl  -y
#  httpd  is just for hosting app in http proto 
# mod_ssl will give an option for hosting app in https 
WORKDIR   /var/www/html/
#COPY project-html-website    .
ADD  project-html-website    .
EXPOSE 80 
ENTRYPOINT  httpd -DFOREGROUND 
#  systemctl  start  httpd  ---> using program  "httpd -DFOREGROUND"
#  systemctl we can't use bcz this is dependent process 
#  

```

 ## Building docker image 
 
 ```
  docker build  -t   httpd:ashuv002  . 
  
  ```
  
  ## Creating a container 
  
  ```
   docker run  --name  ashxc2  -d  -p 2222:80  d915a21cc32f
   
   ```
   
   ## access running container  and making changes 
   
   ```
  [ec2-user@ip-172-31-58-55 microsoftapp]$ docker  exec  -it   ashxc2  bash 
[root@ba2e2b20794d html]# 
[root@ba2e2b20794d html]# whoami
root
[root@ba2e2b20794d html]# pwd
/var/www/html
[root@ba2e2b20794d html]# yum install vim -y
Failed to set locale, defaulting to C.UTF-8
Last metadata expiration check: 0:05:46 ago on Tue Oct 20 07:22:48 2020.
Package vim-enhanced-2:8.0.1763-13.el8.x86_64 is already installed.
Dependencies resolved.
Nothing to do.
Complete!
[root@ba2e2b20794d html]# ls
LICENSE  README.md  css  fonts	img  index.html
[root@ba2e2b20794d html]# 

```


## COnvert a container into Docker image 

```
docker  commit  -m  "few changes"  ashxc2   httpd:ashuv003

```

## Pushing docker image on Docker HUb 

```
215  docker  tag  httpd:ashuv003  dockerashu/httpd:ashuv003
  216  docker  login -u  dockerashu 
  217  docker  push  dockerashu/httpd:ashuv003
  218  history 
  219  docker  logout 
```


   
   ```
   
   ## Now 
