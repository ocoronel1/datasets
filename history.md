# Training for shine2cloud

## Preparing to run python train.py 
      git clone https://github.com/ocoronel1/pytorch-CycleGAN-and-pix2pix.git
      aws configure
      aws s3 ls
      source activate pytorch_p36
      pip install dominate
      pip install --upgrade pip
      pip install visdom
      git clone https://github.com/ocoronel1/w210-dataset.git
      mv w210-dataset/* datasets/
      cd shine2cloudy/
      unzip shine2cloudy.zip 
      cd pytorch-CycleGAN-and-pix2pix/

## Running python train.py
      python train.py --dataroot ./datasets/shine2rain/ --name shine2rain --model cycle_gan --gpu 0,1,2,3  --batch_size 16 --norm instance
