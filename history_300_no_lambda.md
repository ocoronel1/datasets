    1  aws configure
    2  aws s3 ls s3://w210-capstone-dataset/
    3  aws s3 ls s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/
    4  mkdir pytorch-CycleGAN-and-pix2pix/
    5  aws s3 cp s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/ ./pytorch-CycleGAN-and-pix2pix/
    6  aws s3 cp s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/ ./pytorch-CycleGAN-and-pix2pix/ --recursive
    7  clear
    8  ls
    9  rm -rf pytorch-CycleGAN-and-pix2pix/
   10  ls
   11  git clone https://github.com/ocoronel1/pytorch-CycleGAN-and-pix2pix.git
   12  ls
   13  cd pytorch-CycleGAN-and-pix2pix/
   14  source activate pytorch_p36
   15  ls
   16  aws s3 ls s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/
   17  aws s3 ls s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/checkpoints/
   18  aws s3 ls s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/datasets/
   19  aws s3 ls s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/datasets/Image/
   20  aws s3 cp s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/datasets/Image/  
   21  cd datasets/
   22  ls
   23  mkdir Image
   24  aws s3 cp s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/datasets/Image/  Image
   25  aws s3 cp s3://w210-capstone-dataset/pytorch-CycleGAN-and-pix2pix/datasets/Image/  Image --recursive
   26  ls
   27  rm -rf Image/
   28  wget https://www.cs.ccu.edu.tw/~wtchu/projects/Weather/Image.zip
   29  ls
   30  aws s3 cp Image.zip s3://w210-capstone-dataset/Image.zip --recursive
   31  aws s3 cp Image.zip s3://w210-capstone-dataset/ 
   32  clear
   33  ls
   34  unzip Image.zip
   35  clear
   36  ls
   37  ls Image
   38  ls
   39  cd Image/
   40  ls
   41  mkdir sunny2cloudy_50
   42  mkdir sunny2cloudy_50/trainA
   43  mkdir sunny2cloudy_50/trainB
   44  mkdir sunny2cloudy_50/testA
   45  mkdir sunny2cloudy_50/testB
   46  ls sunny2cloudy_50/
   47  cd sunny2cloudy_50/
   48  cd ..
   49  ls
   50  cd sunny
   51  ls
   52  clear
   53  for file in $(ls -p | grep -v /| tail -50); do  cp $file ../sunny2cloudy_50/trainA/; done
   54  cd ..
   55  ls sunny2cloudy_50/trainA
   56  cd cloudy/
   57  for file in $(ls -p | grep -v /|tail -50);do cp $file ../sunny2cloudy_50/trainB; do
   58  for file in $(ls -p | grep -v /|tail -50);do cp $file ../sunny2cloudy_50/trainB; done
   59  cd ..
   60  ls sunny2cloudy_50/trainB/
   61  cd sunny
   62  cd ..
   63  cd cloudy/
   64  for file in $(ls -p | grep -v /| tail -10); do 
   65  cd ..
   66  cd sunny
   67  for file in $(ls -p | grep -v /| tail -10); cp ../sunny2cloudy_50/testA/
   68  for file in $(ls -p | grep -v /| tail -10); cp $file ../sunny2cloudy_50/testA/
   69  for file in $(ls -p | grep -v /| tail -10); do cp $file ../sunny2cloudy_50/testA/; done
   70  cd ..
   71  ls sunny2cloudy_50/testA
   72  cd ..
   73  ls
   74  clear
   75  ls
   76  cd ..
   77  cd datasets/
   78  ls
   79  mkdir sunny2cloudy_100
   80  mkdir sunny2cloudy_100/testA
   81  mkdir sunny2cloudy_100/testB
   82  mkdir sunny2cloudy_100/trainA
   83  mkdir sunny2cloudy_100/trainB
   84  cd sunny
   85  ls
   86  ls -l
   87  mv sunny2cloudy_100/ Image
   88  cd Image/
   89  ls
   90  cd sunny
   91  for file in $(ls -p | grep -v / |tail -300); cp $file ../sunny2cloudy_100/trainA
   92  for file in $(ls -p | grep -v / |tail -300); do cp $file ../sunny2cloudy_100/trainA; done
   93  cd ../cloudy
   94  for file in $(ls -p | grep -v / |tail -300); do cp $file ../sunny2cloudy_100/trainB; done
   95  cd ../sunny/
   96  for file in $(ls -p | grep -v / |tail -20); do cp $file ../sunny2cloudy_100/testA; done
   97  cd ..
   98  ls
   99  mv sunny2cloudy_100 sunny2cloudy_300
  100  mv sunny2cloudy_300 ..
  101  cd ..
  102  ls
  103  clear
  104  python train.py --dataroot ./datasets/sunny2cloudy_300 --model sunny2cloudy_300 --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance 
  105  cd ..
  106  python train.py --dataroot ./datasets/sunny2cloudy_300 --model sunny2cloudy_300 --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance 
  107  clear
  108  cd checkpoints/
  109  ls
  110  cd experiment_name/
  111  ls
  112  cd ..
  113  ls
  114  clear
  115  ls
  116  pwd
  117  mkdir sunny2cloudy_pretrained
  118  ls
  119  cp ./experiment_name/latest_net_G_A.pth ./sunny2cloudy_pretrained/latest_net_G.pth
  120  ls sunny2cloudy_pretrained/
  121  cd ..
  122  clear
  123  python test.py --dataroot datasets/sunny2cloudy_300/testA --name sunny2cloudy_pretrained --model test --no_dropout
  124  cd results/
  125  ls
  126  cd sunny2cloudy_pretrained/
  127  ls
  128  cd test_latest/
  129  ls
  130  cd images/
  131  ls
  132  cd ..
  133  mkdir static
  134  mv images/ static/
  135  ls static/
  136  mkdir templates
  137  ls
  138  mv index.html templates/
  139  ls
  140  cd templates/
  141  ls
  142  vim index.html 
  143  cd ../static/
  144  ls
  145  mv images/* .
  146  ls
  147  rm -rf images/
  148  cd ..
  149  ls
  150  FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
  151  clear
  152  ls
  153  cp ~/app.py .
  154  FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
  155  history | less
  156  clear
  157  cd ..
  158  history >> history_300_no_lambda
