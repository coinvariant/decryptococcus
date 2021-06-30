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

def eliminate_blue_objects(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    res = cv2.inRange(image, (90, 0, 0), (110, 255, 255))
    replacement = np.mean(image, axis=(0,1))
    print(replacement)

    h = res // 255 * replacement[0].astype("uint8")
    s = res // 255 * replacement[1].astype("uint8")
    v = res // 255 * replacement[2].astype("uint8")

    print(h.dtype)

    image = cv2.bitwise_and(image, image, mask = ~res)

    image[:, :, 0] += h
    image[:, :, 1] += s
    image[:, :, 2] += v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    return image


def detect_edges(image):
    cv2.imshow("coleor", image)
    bl = eliminate_blue_objects(image)
    cv2.imshow('blue', bl)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("1", image)
    # image = cv2.bilateralFilter(image, 9, 75, 75)
    image = cv2.GaussianBlur(image, (3,3), 1)
    cv2.imshow("2", image)
    edges = cv2.Laplacian(image, -1, ksize=3, scale=1)
    cv2.imshow("edge", edges)
    _, mask = cv2.threshold(edges, 25, 255, cv2.THRESH_BINARY)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)
    return mask

def analyze_connected_components(image):
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(image)


def run_automatic_segmentation(image):
    components = detect_edges(image)
    data = analyze_connected_components(components)


if __name__ == "__main__":
    test1 = cv2.cvtColor(cv2.imread("./test/test1.jpg"), cv2.COLOR_BGR2RGB)
    test2 = cv2.cvtColor(cv2.imread("./test/test2.jpg"), cv2.COLOR_BGR2RGB)
    test3 = cv2.cvtColor(cv2.imread("./test/test3.jpg"), cv2.COLOR_BGR2RGB)

    detect_edges(test2)
    # exper(test1)    