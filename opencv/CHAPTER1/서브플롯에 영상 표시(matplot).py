import cv2
from matplotlib import pyplot as plt

imgBGR1 = cv2.imread("lena.png")
imgBGR2 = cv2.imread("apple.png")
imgBGR3 = cv2.imread("dog.png")
imgBGR4 = cv2.imread("monkey.png")

imgBGR1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgBGR2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgBGR3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgBGR4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

fig, ax = plt.subplots(2, 2, figsize = (10, 10))
fig.canvas.manager.set_window_title("Sample Pictures")

ax[0][0].axis("off")
ax[0][0].imshow(imgBGR1, aspect = 'auto')

ax[0][1].axis("off")
ax[0][1].imshow(imgBGR2, aspect = 'auto')

ax[1][0].axis("off")
ax[1][0].imshow(imgBGR3, aspect = 'auto')

ax[1][1].axis("off")
ax[1][1].imshow(imgBGR4, aspect = 'auto')

plt.subplots_adjust(left = 0, right = 1,
                    bottom = 0, top = 1,
                    wspace = 0.05, hspace = 0.05)

# == bbox_inches = "tight"를 통해 모든 정보를 들어가게끔 한다 == 
plt.savefig('no_tight')
plt.show()