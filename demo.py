# You need to put your dataset under "data" folder!!
# Example Usage: sh demo.sh folder_name result_folder model_name
# sh demo.sh test-ori final-models/Hazy2GT_indoor.pb --> Track1: Indoor
# sh demo.sh test-ori-out final-models/Hazy2GT_outdoor.pb --> Track2: Outdoor
import datetime
import os
import sys


print("Please wait ...")
today=datetime.datetime.now().strftime('%d_%m_%Y_%T')


pathInput=sys.argv[1] + '/'
pathOutput=sys.argv[2] + '/'
modelfile=sys.argv[3]

path_downscaled=pathOutput + "/temp"

if not os.path.exists(path_downscaled):
    os.mkdir(path_downscaled)


#Create log file
sys.stderr=sys.stdout
os.mkdir('logs')
sys.stdout=open('logs/log_' + today + '.out')

#Downscaling
exec('resize_im.py', pathInput, path_downscaled)

#Dehazing
exec('convertHazy2GT.py', path_downscaled, modelfile)

#Upscaling
exec('laplacian.py', pathInput, pathOutput)


if os.path.exists(path_downscaled):
    exec('rm -rf ' + path_downscaled)
