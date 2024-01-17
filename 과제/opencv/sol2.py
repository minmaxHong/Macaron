"""
1. 사진을 불러오고 컬러 포맷 변환하기 (BGR -> RGB)
2. 저장하기
3. type 출력하기
4. shape 출력하기

[Hint]
- cv2.imread/cv2.imwrite 사용
- numpy 사용
- 구글의 도움 받기
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    
    img = cv2.imread("lena.png")
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    height, width, channel = imgRGB.shape
    print(f'height = {height}\nwidth = {width}\nchannel = {channel}')
    print('type = ', type(imgRGB))
    
    cv2.imwrite('lenaRGB.png', imgRGB)
    
    plt.axis("off")
    plt.imshow(imgRGB)
    plt.show()


if __name__ == "__main__":
    main()