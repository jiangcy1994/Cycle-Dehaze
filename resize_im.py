import cv2
import os
import sys

def resize_im(input_dir, output_dir):
    
    for img_name in os.listdir(input_dir):
        img = cv2.resize(cv2.imread(input_dir + '/' + img_name), (256, 256))
        cv2.imwrite(output_dir + '/' + img_name, img, [cv2.IMWRITE_JPEG_QUALITY, 100])

