import cv2
import numpy as np

def apply_averaging_spatial_filter(image, kernel_size):
    return cv2.blur(image, kernel_size)

def apply_geometric_spatial_filter(image, kernel_size):
    image[image == 0] = 1
    return np.uint8(np.exp(cv2.boxFilter(np.float32(np.log(image)), -1, kernel_size)))

def apply_erosion(image, kernel):
    return cv2.erode(image, kernel)

def apply_dilation(image, kernel):
    return cv2.dilate(image, kernel)

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


def detect_edges(image):
    cv2.imshow("coleor", image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("1", image)
    image = cv2.bilateralFilter(image, 9, 75, 75)
    # image = cv2.GaussianBlur(image, (3,3), 1)
    cv2.imshow("2", image)
    edges = cv2.Laplacian(image, -1, ksize=3, scale=1)
    cv2.imshow("edge", edges)
    _, mask = cv2.threshold(edges, 25, 255, cv2.THRESH_BINARY)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)

def exper(image):
    Z = image.copy()
    Z = Z.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 3
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((image.shape))
    cv2.imshow('res2',res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def run_automatic_segmentation(image):
    pass


if __name__ == "__main__":
    test1 = cv2.imread("./test/test1.jpg")
    test2 = cv2.imread("./test/test2.jpg")
    test3 = cv2.imread("./test/test3.jpg")

    detect_edges(test2)
    # exper(test1)    