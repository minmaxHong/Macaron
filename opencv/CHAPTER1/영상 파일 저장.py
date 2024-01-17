import cv2

imageFile = "lena.png"

img = cv2.imread(imageFile)

cv2.imwrite("Lena.bmp", img)
cv2.imwrite("Lena.png", img)

# == img를 압축률 9의 png 영상으로 저장한다. ==
# == 압축률은 [0, 9]이며 압축률이 높을수록 시간이 오래걸림 ==
cv2.imwrite("Lena2.png", img,
            [cv2.IMWRITE_PNG_COMPRESSION, 9])

# == img를 90%의 품질을 갖는 jpeg 영상으로 저장한다. ==
# == 품질의 범위는 [0, 100]이며 높을수록 영상의 품질이 좋다.(default는 95)
cv2.imwrite("Lena2.jpg", img,
            [cv2.IMWRITE_JPEG_QUALITY, 90])