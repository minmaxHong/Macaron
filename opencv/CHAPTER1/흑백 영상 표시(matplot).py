import cv2 
from matplotlib import pyplot as plt

imageFile = "lena.png"
# imgGray = cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)
imgGray = cv2.imread(imageFile, 0)

'''
cv2.imshow("Gray", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

plt.axis("off")

# == imgGray를 통해 gray로 읽고 bicubic으로 intepolation 한다. ==
plt.imshow(imgGray, cmap = "gray", interpolation = "bicubic")
plt.show()