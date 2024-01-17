import cv2
from matplotlib import pyplot as plt

imageFile = "lena.png"

imgGray = cv2.imread(imageFile, 0)

plt.figure(figsize = (6, 6))

plt.subplots_adjust(left = 0, right = 1,
                    bottom = 0, top = 1)

plt.imshow(imgGray, cmap = "gray")
plt.axis("off")
plt.savefig('0205.png')
plt.show()