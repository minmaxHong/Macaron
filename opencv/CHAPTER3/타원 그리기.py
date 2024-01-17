import cv2
import numpy as np

img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255
ptCenter = img.shape[0] // 2, img.shape[1] // 2
size = 200, 100

cv2.ellipse(img, center = ptCenter, axes = size, angle = 0, startAngle = 0, endAngle = 360, color = (255, 0, 0))
cv2.ellipse(img, center = ptCenter, axes = size, angle = 45, startAngle = 0, endAngle = 360, color = (255, 0, 0))

# == 회전 사각형의 내접하는 타원 그리기 ==
box = (ptCenter, size, 0)
cv2.ellipse(img, box, (0, 0, 0), 5)

box = (ptCenter, size, 45)
cv2.ellipse(img, box, (0, 0, 0), 5)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()