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

### Testing the shine2rain model   
python test.py --dataroot datasets/shine2rain/testA --name shine2rain_pretrained --model test --no_dropout  

### Checking test results  
cd results/  
cd shine2rain_pretrained/  
cd test_latest/  
