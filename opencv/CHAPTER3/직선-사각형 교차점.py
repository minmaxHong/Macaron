import cv2
import numpy as np

img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255

x1, x2 = 100, 400
y1, y2 = 100, 400
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

pt1 = 120, 50
pt2 = 300, 500
cv2.line(img, pt1, pt2, (255, 0, 0), 2)

# x1, y1은 직사각형의 upper left의 꼭지점 좌표를 나타낸다.
# x2 - x1은 가로, y2-y1은 세로
# imgRect는 (x, y, width, height)형태로 직사각형의 왼쪽 위 꼭지점 좌표와 가로, 세로 길이를 표현한다.
imgRect = (x1, y1, x2 - x1, y2 - y1)
ret, rpt1, rpt2 = cv2.clipLine(imgRect, pt1, pt2)

if ret:
    # thickness가 -1이면 도형 내부를 채우게 된다.
    cv2.circle(img, rpt1, radius = 5, color = (0, 255, 0), thickness = -1)
    cv2.circle(img, rpt2, radius = 5, color = (0, 255, 0), thickness = -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
