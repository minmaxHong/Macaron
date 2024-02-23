import numpy as np

def gaussian_filter2d(width, sigma):
    
    # == Gaussian Filter -> Kernel_2d가 Gaussian Filter임 == 
    kernel_2d = np.zeros((width, width))
    distance = np.arange((width // 2) * (-1), (width // 2) + 1)

    not_exp = 2 * np.pi * (sigma ** 2)
    
    for x in range(width):
        for y in range(width):
            kernel_2d[x, y] = np.exp(-(distance[x] ** 2 + distance[y] ** 2) / (2 * (sigma ** 2))) / not_exp
    
    return kernel_2d
    
print(gaussian_filter2d(3, 3))