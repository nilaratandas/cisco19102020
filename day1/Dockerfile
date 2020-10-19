FROM  python 
#  it will pull  python docker image if not present 
MAINTAINER   ashutoshh@linux.com
RUN   mkdir   /myapps
COPY  ashu.py  /myapps/ashu.py 
#  is to copy data from host to Docker image 
#  location of Dockerfile and code will be same 
#CMD  python  /myapps/ashu.py 
ENTRYPOINT  python  /myapps/ashu.py 
#  CMD is for  default parent process if not define by user 
#  if  User is not defining  during container creation time 
