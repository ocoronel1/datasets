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
ls
unzip shine2cloudy.zip 
cd ..
mv pytorch-CycleGAN-and-pix2pix/datasets/shine* w210-dataset/
cd ~
touch .netrc
vim .netrc 
mv history.md ~/w210-dataset/
cd ~/w210-dataset/
mv ./w210-dataset/shine* pytorch-CycleGAN-and-pix2pix/datasets/
cd pytorch-CycleGAN-and-pix2pix/datasets/
unzip shine2cloudy.zip 
unzip shine2rain.zip 
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
ls images/
mkdir static
mv images/ static/
mkdir templates
mv index.html templates/
cp ~/app.py .
vim ./templates/index.html 
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
python test.py --dataroot datasets/shine2rain/testA --name shine2rain_pretrained --model test --no_dropout
cd results/
ls shine2rain_pretrained/
cd shine2rain_pretrained/
cd test_latest/
mv images static
vim index.html 
mkdir templates
mv index.html templates/
cp ~/app.py .
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
cd datasets/
cd shine2rain/
mkdir static 
mv test? static/
mv train? static/
mkdir templates
cp ~/app.py  .
cp ~/index.html .
mv index.html templates/
vim templates/index.html 
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
rm app.py 
cd results/
cd shine2rain_pretrained/
cd test_latest/
cd checkpoints/
ls shine2rain_pretrained/
cd shine2rain
cd web/
ls templates/
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
cd results/
cd shine2rain_pretrained/
cd test_latest/
ls ~/pytorch-CycleGAN-and-pix2pix/checkpoints/
cd ../..
cd ..
cd checkpoints/
cp ./shine2rain/latest_net_D_A.pth ./shine2rain_pretrained/latest_net_G.pth
cd shine2rain_pretrained/
cd ../../..
cd pytorch-CycleGAN-and-pix2pix/
python test.py --dataroot datasets/shine2rain/testA --name shine2rain_pretrained --model test --no_dropout
cd results/
cd shine2rain_pretrained/
cd test_latest/
mv images static
vim index.html 
mkdir templates
mv index.html templates/
cp ~/app.py .
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
wget https://www.cs.ccu.edu.tw/~wtchu/projects/Weather/Image.zip
mv Image.zip datasets/
cd datasets/
unzip Image.zip 
unzip Image.zip 
cd Image/
ls cloudy/ | wc -l
mkdir sunny2cloudy
mkdir sunny2foggy
mkdir sunny2rain
mkdir sunny to snow
mkdir sunny2snow
cd cloudy/
ls ../
cd ..
cd sunny2cloudy/
mkdir testA trainA testB trainB
cd ..
cd sunny2foggy/
mkdir testA trainA testB trainB
cd ..
cd sunny2rain/
mkdir testA testB trainA trainB
cd ..
ls sunny2cloudy/
ls sunny2rain/
ls sunny2foggy/
cd sunny2snow/
mkdir testA testB trainA trainB
cd ..
cd cloudy/
ls ../sunny2cloudy/
for file in $(ls -p | grep -v /| tail -300); do cp $file ../sunny2cloudy/trainB/; done
ls ../sunny2cloudy/trainB/ | wc -l
for file in $(ls -p | grep -v /| tail -10); do cp $file ../sunny2cloudy/testB/; done
ls ../sunny2cloudy/testB/ | wc -l
cd ..
for file in $(ls -p | grep -v /| tail -300); do cp $file ../sunny2cloudy/trainA/; done
for file in $(ls -p | grep -v /| tail -10); do cp $file ../sunny2cloudy/testA/; done
cd ..
python train.py --dataroot ./datasets/sunny2cloudy --model sunny2cloudy --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance
cd datasets/
ls Image
mv sunny2snow ..
ls sunn*
cd datasets/
ls
ls Image
mv ./Image/sunny2snow/ ..
ls
cd ..
ls
mv sunny2snow/ ./datasets/
ls datasets/
clear
python train.py --dataroot ./datasets/sunny2snow/ --name sunny2snow --model cylce_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance
python train.py --dataroot ./datasets/sunny2snow/ --name sunny2snow --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance
cd checkpoints/
ls
ls -l
ls -lthr
ls -lth
cd sunny2snow/
ls
cd web/
ls
mkdir templates
vim index.html 
ls
mv index.html  templates/
ls
mv images static
ls
cp ~/app.py .
ls
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
cd ~/pytorch-CycleGAN-and-pix2pix/
clear
ls datasets/
ls datasets/Image
python train.py --dataroot ./datasets/sunny2rain --name sunny2rain --model cycle_gan --gpu_ids 0,1,2,3 --norm instance
ls datasets/sunny2rain
cd datasets/
ls
mv ./Image/sunny2rain/ .
ls
ls sunny2rain/
ls sunny2rain/trainA
cd ..
python train.py --dataroot ./datasets/sunny2rain --name sunny2rain --model cycle_gan --gpu_ids 0,1,2,3 --norm instance
python train.py --dataroot ./datasets/sunny2rain --name sunny2rain --model cycle_gan --gpu_ids 0,1,2,3 --batch_size 16 --norm instance
cd checkpoints/
ls
ls -ltr
cd sunny2rain/
ls
cd web/
ls
mv images/static
ls
mv images/ static
ls
vim index.html 
ls
mkdir templates
mv index.html templates/
ls
cp ~/app.py .
ls
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
ls
ls static/
cd ..
ls
clear
cd web/
ls
cd templates/
ls
vim index.html 
cd ..
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
cd ..
ls -ltr
cd sunny2rain/
ls
cd web/
ls
FLASK_APP=app FLASK_DEBUG=1 flask run --port 5000 --host 0.0.0.0
cd ~/pytorch-CycleGAN-and-pix2pix/
clear
cd datasets/
ls
ls Image
cd ../checkpoints/
ls
cd ..
histopy
history
history >> history_2.md
vim history_2.md 
less history_2.md 
vim history_2.md 
rm history_2.md 
history
history | cut -c
history | cut -c 8-
man cut 
history
history | cut -c 8-
history | cut -c 8- >> history_2.md
