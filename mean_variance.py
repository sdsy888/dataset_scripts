import cv2
from PIL import Image
import numpy as np
from tqdm import tqdm
import os

def compute_mean(img_list):
    r_mean,g_mean,b_mean = np.float64(0.),np.float64(0.),np.float64(0.)
    pixel_count = np.float64(0.)
    for i in tqdm(img_list):
        im = cv2.imread(i)
        # im=im[: , : , : : -1]
        pixel_count += im.shape[0]*im.shape[1]

        # r = np.reshape(im[:,:,2], -1)/255
        r_mean += np.sum(im[:,:,2])
        g_mean += np.sum(im[:,:,1])
        b_mean += np.sum(im[:,:,0])

    # r_mean,g_mean,b_mean = r_mean/pixel_count,g_mean/pixel_count,b_mean
    return np.array([r_mean,g_mean,b_mean])/pixel_count

def compute_std(img_list,mean_array):
    """`mean_array` should be ndarray (float64)
    """
    # r_std,g_std,b_std
    std = np.array([0,0,0],np.float64)
    pixel_count = np.float64(0.)
    for i in tqdm(img_list):
        im = cv2.imread(i)
        pixel_count += im.shape[0]*im.shape[1]
        sq = (im-mean_array)**2

        std[0] += np.sum(sq[:,:,2])
        std[1] += np.sum(sq[:,:,1])
        std[2] += np.sum(sq[:,:,0])

        # std += np.array(r_mean,g_mean,b_mean)
    return np.sqrt(std/pixel_count)

data_dir = '/home/dataset_folder'
file_list = file_list = [
    os.path.join(root, f)
    for root, _, file_list in list(os.walk(data_dir))
    for f in file_list
    if f.endswith('jpg')
]

rgb_mean = compute_mean(file_list)
rgb_std = compute_std(file_list,rgb_mean)

print('rgb_mean', rgb_mean,rgb_mean/255)
print('rgb_std', rgb_std,rgb_std/255)


# rgb_mean = [0.51433625 0.51443946 0.51435369]
