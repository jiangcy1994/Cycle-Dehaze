from cv2 import imread, imresize, imwrite, IMWRITE_JPEG_QUALITY
import os
import sys

def resize_im(input_dir, output_dir):
    input_imgs = os.listdir(input_dir)
    
    for imgs_name in os.listdir(input_dir):
        C = imresize(imread(input_dir + '/' + imgs_name), (256, 256))
        imwrite(output_dir + '/' + imgs_name, C, [IMWRITE_JPEG_QUALITY, 100])

