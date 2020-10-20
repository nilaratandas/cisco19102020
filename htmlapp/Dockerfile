FROM  httpd
#  docker engine will pull this image from docker HUB 
MAINTAINER   ashutoshh@linux.com , 9509957594  , ashutoshh
#  if any issue is occuring then plz connect 
#  optional field 
WORKDIR  /var/www/html/
#  similar to cd command in linux 
# during image build time your docker engine will using workdir  to change directory 
COPY .  .
# copy can only take data from the location where Dockerfile is present
#  first . means from host OS where dockerfile is present it will take all the data
# second . means target location on docker image during build time 
#  bcz we have already used workdir to set / change location  
EXPOSE 80
#  it is the port number of  httpd  server 
#  if you are using the default port of app server then Expose is optional 
