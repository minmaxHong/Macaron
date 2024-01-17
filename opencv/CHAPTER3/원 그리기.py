import cv2
import numpy as np

img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255

cx = img.shape[0] // 2
cy = img.shape[1] // 2

for radius in range(200, 0, -100):
    cv2.circle(img, (cx, cy), radius, (0, 0, 0), thickness = 1)

cv2.circle(img, (cx, cy), 50, (0, 0, 0), thickness = -1)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()