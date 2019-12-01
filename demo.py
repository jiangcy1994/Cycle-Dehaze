# You need to put your dataset under "data" folder!!
# Example Usage: sh demo.sh folder_name result_folder model_name
# sh demo.sh test-ori final-models/Hazy2GT_indoor.pb --> Track1: Indoor
# sh demo.sh test-ori-out final-models/Hazy2GT_outdoor.pb --> Track2: Outdoor
import datetime
import os
import sys

from laplacian import laplacian
from resize_im import resize_im

print("Please wait ...")
today=datetime.datetime.now().strftime('%d_%m_%Y_%T')


pathInput=sys.argv[1] + '/'
pathOutput=sys.argv[2] + '/'
modelfile=sys.argv[3]

path_downscaled=pathOutput + "/temp/"

if not os.path.exists(path_downscaled):
    os.mkdir(path_downscaled)


# Create log file
sys.stderr=sys.stdout
os.mkdir('logs')
sys.stdout=open('logs/log_' + today + '.out')

# Downscaling
resize_im(pathInput, path_downscaled)

# Dehazing
for img_name in os.listdir(path_downscaled):
    os.system('python inference.py --model {0} --input {1} --output {2} --image_size 256'.format(
        modelfile, 
        path_downscaled + '/' + img_name, 
        pathOutput + img_name))

# Upscaling
laplacian(path_downscaled, pathInput, pathOutput)


if os.path.exists(path_downscaled):
    os.system('rm -rf ' + path_downscaled)
