import cv2
import numpy as np

imageFile = "lena.png"

color_img = cv2.imread(imageFile)
gray_img = cv2.imread(imageFile, 0)

cv2.imshow("Lena Color", color_img)
cv2.imshow("Lean Gray", gray_img)

# == # 0이 default == 
cv2.waitKey(0) 

# == 키보드를 임의의 키를 터치하면 모든 윈도우를 파괴 ==
cv2.destroyAllWindows() 