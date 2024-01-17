import cv2

cap = cv2.VideoCapture(0)

# == 화면 size 조정 == 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Warning")
        break
    
    cv2.imshow("Frame", frame)
    
    # == 1초마다 key 입력 대기 ==
    key = cv2.waitKey(1000)
    if key == 27:
        break
    
if cap.isOpened():
    cap.isrelease()

cv2.destroyAllWindows()
