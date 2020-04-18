    1  aws configure  
    2  aws s3 ls s3://w210-capstone-datascience/  
    3  aws s3 ls  
    4  aws s3 ls s3://w210-capstone-dataset/  
    5  aws s3 cp s3://w210-capstone-dataset/docker/ . --recursive  
    6  ls  
    8  docker -v  
    9  echo $?  
   18  docker load -i w210.tar  
   79  pwd  
   81  docker ps -a  
   82  docker run -it -v /home/ubuntu:/home/ubuntu  -p 8097:8097 --rm --gpus all w210  
