import cv2
from itertools import accumulate
import numpy as np
import os
from skimage.transform import pyramid_gaussian

def laplacian(input_dir, original_dir, out_dir):

    for img_name in os.listdir(input_dir):
        A = cv2.imread(original_dir + '/' + img_name).astype(np.double);
        C = cv2.imread(input_dir + '/' + img_name).astype(np.double);

        Ads = pyramid_gaussian(A, max_layer=4, multichannel=True)
        Ls = [Ads[i] - cv2.resize(Ads[i + 1], Ads[i].shape[:2]) for i in range(4)]
        Cus = accumulate([C] + Ls[::-1], lambda x, y: cv2.resize(x, y.shape[:2]) + y)

        cv2.imwrite(out_dir + '/' + img_name, Cus[-1].astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 100])
