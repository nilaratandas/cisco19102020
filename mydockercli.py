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
