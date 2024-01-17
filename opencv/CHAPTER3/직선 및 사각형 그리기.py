import cv2
import numpy as np

# img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255

# == 배경으로 사용할 컬러를 지정하여 영상을 생성할 수 있다. (0, 255, 255)를 바꿔서 가능하다. == 
img = np.full((512, 512, 3), (0, 255, 255), dtype = np.uint8) 

pt1 = 100, 100
pt2 = 400, 400

# 초록색, 두께 2
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0, 0, 255), 5)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()