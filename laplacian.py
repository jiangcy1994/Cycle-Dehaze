from cv2 import impyramid, imread, imresize, imwrite
import os
import sys

def laplacian(input_dir, original_dir, out_dir):

    for img_name in os.listdir(input_dir):
        A = double(imread(original_dir + '/' + img_name));
        C = double(imread(input_dir + '/' + img_name));
     
        Ad1 = impyramid(A, 'reduce');
        Ad2 = impyramid(Ad1, 'reduce');
        Ad3 = impyramid(Ad2, 'reduce');
        Ad4 = impyramid(Ad3, 'reduce');

# TODO: check impyramid and imresize args

        L1 = A - imresize(Ad1, [size(A,1), size(A,2)]);
        L2 = Ad1 - imresize(Ad2, [size(Ad1,1), size(Ad1,2)]);
        L3 = Ad2 - imresize(Ad3, [size(Ad2,1), size(Ad2,2)]);
        L4 = Ad3 - imresize(Ad4, [size(Ad3,1), size(Ad3,2)]);

        Cu1 = imresize(C, [size(Ad3,1), size(Ad3,2)]) + L4;
        Cu2 = imresize(Cu1, [size(Ad2,1), size(Ad2,2)]) + L3;
        Cu3 = imresize(Cu2, [size(Ad1,1), size(Ad1,2)]) + L2;
        Cu4 = imresize(Cu3, [size(A,1), size(A,2)]) + L1;

        imwrite(uint8(Cu4), out_dir + '/' + img_name, 'Mode', 'lossless')
