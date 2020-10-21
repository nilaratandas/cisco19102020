# Docker Build Process revesion 

<img src="dbuild.png">

## Docker client with Unix &. TCP socket 

<img src="docker_client.png">

## Starting docker Engine In tcp Socket 

```
[ec2-user@ip-172-31-58-55 ~]$ cd  /etc/sysconfig/
[ec2-user@ip-172-31-58-55 sysconfig]$ ls
acpid       clock     docker          init        modules          nfs            rpc-rquotad  run-parts  sysstat.ioconf
atd         console   docker-storage  irqbalance  netconsole       raid-check     rpcbind      selinux
authconfig  cpupower  grub            keyboard    network          rdisc          rsyncd       sshd
chronyd     crond     i18n            man-db      network-scripts  readonly-root  rsyslog      sysstat
[ec2-user@ip-172-31-58-55 sysconfig]$ sudo vim  docker 
[ec2-user@ip-172-31-58-55 sysconfig]$ cat  docker
# The max number of open files for the daemon itself, and all
# running containers.  The default value of 1048576 mirrors the value
# used by the systemd service unit.
DAEMON_MAXFILES=1048576

# Additional startup options for the Docker daemon, for example:
# OPTIONS="--ip-forward=true --iptables=true"
# By default we limit the number of open files per container
OPTIONS="--default-ulimit nofile=1024:4096   -H  tcp://0.0.0.0:2375"

# How many seconds the sysvinit script waits for the pidfile to appear
# when starting the daemon.
DAEMON_PIDFILE_TIMEOUT=10

```

## docker enginre reload 

```
[ec2-user@ip-172-31-58-55 sysconfig]$ sudo systemctl daemon-reload 
[ec2-user@ip-172-31-58-55 sysconfig]$ sudo systemctl restart  docker
[ec2-user@ip-172-31-58-55 sysconfig]$ sudo netstat -nlpt
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      3345/rpcbind        
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      4644/sshd           
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      4172/master         
tcp        0      0 127.0.0.1:44605         0.0.0.0:*               LISTEN      4055/containerd     
tcp6       0      0 :::2375                 :::*                    LISTEN      5597/dockerd        
tcp6       0      0 :::111                  :::*                    LISTEN      3345/rpcbind        
tcp6       0      0 :::22                   :::*                    LISTEN      4644/sshd 
```

## connecting Docker engine using python client 

```
ashutoshhs-MacBook-Air:Desktop fire$ cat mydockercli.py 
import  docker
import time
# if you want to connect  Docker locally running on Mac / w /Linux 

client=docker.DockerClient(base_url='tcp://100.25.45.150:2375')

## code for listing image 

for  i in  client.containers.list():
	print i
	
## list of images 
for  i in  client.images.list():
	print i


```

