import cv2

cap = cv2.VideoCapture(0)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size = ', frame_size)

while True:
    
    retval, frame = cap.read()
    
    if not retval:
        print("Do not Access File")
        break
    
    cv2.imshow('frame', frame)
    
    # == ASCII CODE에서 25는 EM이라고 END OF MEDIUM(MEDIA의 END를 말함)
    key = cv2.waitKey(25)
    
    # == ASCII CODE에서 27은 ESC
    if key == 27:    
        break
    
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()