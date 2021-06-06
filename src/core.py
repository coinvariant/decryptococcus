import cv2
import numpy as np

def apply_averaging_spatial_filter(image, kernel_size):
    return cv2.blur(image, kernel_size)

def apply_geometric_spatial_filter(image, kernel_size):
    image[image == 0] = 1
    return np.uint8(np.exp(cv2.boxFilter(np.float32(np.log(image)), -1, kernel_size)))

def apply_erosion(image, *args):
    pass

def apply_dilation(image, *args):
    pass

def apply_log_transform(image, c):
    norm = image / 255   # normalization to [0..1]                  
    out = c * np.log(1 + norm)
    out *= 255
    return out.astype('uint8')

def apply_gamma_transform(image, c, y):
    norm = image / 255   # normalization to [0..1]
    out = c * np.power(norm, y)
    out *= 255
    return out.astype('uint8')

def run_automatic_segmentation(image):
    pass
