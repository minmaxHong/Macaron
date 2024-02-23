import numpy as np
import cv2

def gaussian_filter2d(width, sigma):
    
    # == Gaussian Filter -> Kernel_2d가 Gaussian Filter임 == 
    kernel_2d = np.zeros((width, width))
    distance = np.arange((width // 2) * (-1), (width // 2) + 1)

    not_exp = 2 * np.pi * (sigma ** 2)
    
    for x in range(width):
        for y in range(width):
            kernel_2d[x, y] = np.exp(-(distance[x] ** 2 + distance[y] ** 2) / (2 * (sigma ** 2))) / not_exp

    # Image에 전체적인 intensity를 보존하기 위하여 Normalize
    kernel_2d /= np.sum(kernel_2d)
    
    return kernel_2d
    
def apply_gaussian_filter(image, kernel):
    filter_image = cv2.filter2D(image, -1, kernel)
    
    return filter_image

img = cv2.imread('Lane Detection Study\lena.png')
gaussian_blurImg = apply_gaussian_filter(img, gaussian_filter2d(3, 3))

cv2.imshow('Original Image', img)
cv2.imshow('Gaussian_blur_Image', gaussian_blurImg)
cv2.waitKey()
cv2.destroyAllWindows()
