# Praring the host for docker to run gpus
   23  sudo apt-get update
   24  sudo apt-get install yum
   26  yum-config-manager --enable
   27  sudo apt install yum-utils
   30  sudo yum install -y nvidia-container-toolkit
   31  yum repolist all

# Running docker on top of GPUs
    3  aws configure
    4  aws s3 ls s3://w210-capstone-dataset/docker/
    5  aws s3 cp s3://w210-capstone-dataset/docker/w210.2.tar .
    6  ls
    7  docker load -i w210.2.tar 
    8  docker run --help
    9  docker run --help | less
   10  docker run -td -v /home/ubuntu:/home/ubuntu -p 8097:8097 -gpus 0 
   11  docker run -td -v /home/ubuntu:/home/ubuntu -p 8097:8097 --gpus 0
   12  docker run -td -v /home/ubuntu:/home/ubuntu -p 8097:8097 --gpus 0 w210
   13  clear
   14  docker ps
   15  docker exec -it aef90f1c9e1e /bin/bash
   16  history | less
   17  history >> history_web.md
    
  
