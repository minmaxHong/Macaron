import cv2
from matplotlib import pyplot as plt

imageFile = "Lena.png"

# == opencv는 BGR로 img 반환한다 == 
imgBGR = cv2.imread(imageFile)
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

cv2.imshow("imgBGR", imgBGR)
cv2.imshow("imgRGB", imgRGB)

cv2.waitKey(0)
cv2.waitDestroyAllWindows()