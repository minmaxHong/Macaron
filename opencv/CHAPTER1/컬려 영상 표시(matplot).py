import cv2
from matplotlib import pyplot as plt

imageFile = "Lena.png"

imgBGR = cv2.imread(imageFile)
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis("off")
plt.imshow(imgRGB)
plt.show()
