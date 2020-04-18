    1  aws configure  
    2  aws s3 ls s3://w210-capstone-datascience/  
    3  aws s3 ls  
    4  aws s3 ls s3://w210-capstone-dataset/  
    5  aws s3 cp s3://w210-capstone-dataset/docker/ . --recursive  
    6  ls  
    7  docker --help  
    8  docker -v  
    9  echo $?  
   10  docker save -o w210.tar  
   11  docker save -o w210.tar w210  
   12  docker -v  
   13  echo $?  
   14  ls  
   15  clear  
   16  ls -ltrh  
   17  docker save -o w210.tar w210  
   18  docker-machine active  
   19  docker images  
   20  docker ps -a  
   21  docker run -it --name test1 ubuntu /bin/bash  
   22  docker ps  
   23  docker ls  
   24  docker ps  
   25  docker ps -a  
   26  docker kill c77f5f659db2   
   27  docker rm c77f5f659db2   
   28  docker ps -a  
   29  docker -it --name test1 ubuntu /bin/bash  
   30  docker run -it --name test1 /bin/bash  
   31  docker run -it --name test1 ubuntu /bin/bash  
   32  ls  
   33  ls -ltrh  
   34  docker cp test1:/test.txt .  
   35  ls -lhtr  
   36  rm test.txt  
   37  docker ls test1:/  
   38  docker ps test1:/  
   39  docker cp test1:/test.txt .  
   40  ls -lthr  
   41  rm test.txt   
   42  toach test1.txt  
   43  ls -lthr  
   44  touch test1.txt  
   45  ls -ltrh  
   46  docker cp ./test1.txt test1:/  
   47  docker ps  
   48  docker ps -a  
   49  docker start test1  
   50  docker ps  
   51  docker exec -it test1 /bin/bash  
   52  docker ps  
   53  docker exce -ti test1 /bin/bash  
   54  clear  
   55  docker ps  
   56  docker exec -it test1  /bin/bash  
   57  docker ps  
   58  docker rm test1  
   59  docker stop test1  
   60  docer ps  
   61  docker ps  
   62  docker rm test1  
   63  docker ps -a  
   64  docker save -h  
   65  ls w210  
   66  docker ps -a  
   67  ls   
   68  docker save -o w210.tar w210  
   69  ls -sh   
   70  ls -hs   
   71  ls -hs w210.tar  
   72  docker save -o w210.tar w210_file  
   73  clear  
   74  ls -trhl  
   75  rm test1.txt   
   76  docker -v  
   77  docker load -i w210.tar w210  
   78  docker load -i w210.tar  
   79  pwd  
   80  docker run -it -v /home/ubuntu:/home  -p 8097:8097 --rm --gpus all w210  
   81  docker ps -a  
   82  docker run -it -v /home/ubuntu:/home/ubuntu  -p 8097:8097 --rm --gpus all w210  
   83  history  
   84  history | less  
   85  docker ps  
   86  docker ps -a  
   87  docker images  
   88  source activate pytorch_p36  
   89  ls  
   90  ls -d */  
   91  history >> history.md  
