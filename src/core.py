import cv2
import numpy as np

def apply_averaging_spatial_filter(image, kernel_size):
    return cv2.blur(image, kernel_size)

def apply_geometric_spatial_filter(image, *args):
    pass

def apply_erosion(image, *args):
    pass

def apply_dilation(image, *args):
    pass

def run_automatic_segmentation(image):
    pass