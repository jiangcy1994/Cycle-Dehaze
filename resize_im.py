from cv2 import imread, imresize, imwrite
import os
import sys

def resize_im(input_dir, output_dir):
    input_imgs = os.listdir(input_dir)
    
    for imgs_name in os.listdir(input_dir):
        C = imresize(imread(input_dir + '/' + imgs_name), (256, 256))
        imwrite(C, output_dir + '/' + imgs_name, 'Mode', 'lossless')

