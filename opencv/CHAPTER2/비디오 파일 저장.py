import cv2

cap = cv2.VideoCapture(0)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame size = ', frame_size)

fourcc = cv2.VideoWriter_fourcc(*'XVID')


out1 = cv2.VideoWriter('record0.mp4', fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter('record1.mp4', fourcc, 20.0, frame_size, isColor = False)

while True:
    ret, frame = cap.read()
    if not ret:
        print('Warning')
        break
    
    # == color image == 
    out1.write(frame)
    
    # == gray image == 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    key = cv2.waitKey(25)
    if key == 27:
        print("Stop")
        break

if cap.isOpened():
    cap.release()

if out1.isOpened():
    out1.release()

if out2.isOpened():
    out2.release()

cv2.destroyAllWindows()