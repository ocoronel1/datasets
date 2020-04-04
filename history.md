### Setting the environment
source activate pytorch_p36  
pip install dominate  
pip install --upgrade pip  
pip install visdom  
git clone https://github.com/ocoronel1/w210-dataset.git  
ls w210-dataset/  
cd pytorch-CycleGAN-and-pix2pix/  
mv ../w210-dataset/* ./datasets/  
ls datasets/  
cd datasets/  


### Setting up password for github 
cd ~   
touch .netrc  
vim .netrc   

### Creating folders for the pre-trained model
mkdir shine2cloudy_pretrained  
mkdir shine2rain_pretrained  
cp ./shine2rain/latest_net_G_A.pth ./shine2rain_pretrained/latest_net_G.pth  
cp ./shine2cloudy/latest_net_G_A.pth ./shine2cloudy_pretrained/latest_net_G.pth  
cd ..  
python test.py --dataroot datasets/shine2cloudy/testA --name shine2cloudy_pretrained --model test --no_dropout  
cd results/  
ls shine2cloudy_pretrained/test_latest/  
cd shine2cloudy_pretrained/  
cd test_latest/  

### Visualizing iamges
mkdir static  
mv images/ static/  
mkdir templates  
mv index.html templates/  
cp ~/app.py .  
vim ./templates/index.html   
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0  

### Testing the shine2rain model   
python test.py --dataroot datasets/shine2rain/testA --name shine2rain_pretrained --model test --no_dropout  

### Checking test results
cd results/  
cd shine2rain_pretrained/  
cd test_latest/  

### Visualizing images from test results
mv images static  
vim index.html  
mkdir templates  
mv index.html templates/  
cp ~/app.py .  
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0  


### Preparing the shin2rain model for test
cd checkpoints/
cp ./shine2rain/latest_net_D_A.pth ./shine2rain_pretrained/latest_net_G.pth
cd shine2rain_pretrained/
cd ../../..


### Testing the shine2rain model
cd pytorch-CycleGAN-and-pix2pix/
python test.py --dataroot datasets/shine2rain/testA --name shine2rain_pretrained --model test --no_dropout


### Visualizing test results  
cd results/  
cd shine2rain_pretrained/  
cd test_latest/  
mv images static  
vim index.html   
mkdir templates  
mv index.html templates/  
cp ~/app.py   
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0

### Downloading weather data and distributing it in test and train
wget https://www.cs.ccu.edu.tw/~wtchu/projects/Weather/Image.zip  
mv Image.zip datasets/  
cd datasets/  
unzip Image.zip   
cd Image/  
mkdir sunny2cloudy  
mkdir sunny2foggy  
mkdir sunny2rain  
mkdir sunny2snow  
cd sunny2cloudy/  
mkdir testA trainA testB trainB  
cd ..  
cd sunny2foggy/  
mkdir testA trainA testB trainB  
cd ..  
cd sunny2rain/  
mkdir testA testB trainA trainB  
cd ..  
cd sunny2snow/  
mkdir testA testB trainA trainB  

### Splitting a large number of files into 300 for train and 10 for testing
cd ..  
cd cloudy/  
for file in $(ls -p | grep -v /| tail -300); do cp $file ../sunny2cloudy/trainB/; done    
for file in $(ls -p | grep -v /| tail -10); do cp $file ../sunny2cloudy/testB/; donea   
cd ..  
for file in $(ls -p | grep -v /| tail -300); do cp $file ../sunny2cloudy/trainA/; done    
for file in $(ls -p | grep -v /| tail -10); do cp $file ../sunny2cloudy/testA/; donea    

### Training three models
python train.py --dataroot ./datasets/sunny2cloudy --model sunny2cloudy --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance  
python train.py --dataroot ./datasets/sunny2snow/ --name sunny2snow --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance  
python train.py --dataroot ./datasets/sunny2rain --name sunny2rain --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance  

