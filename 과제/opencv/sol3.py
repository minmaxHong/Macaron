"""
1. 웹캠 스트리밍해서 1초에 사진 한장씩 특정 폴더에 다른 이름으로 이미지 저장하기
2. 이미지 이름은 이름 + time.time() 으로 저장하기(ex: image16882230564706147,image16882230586506147, .......)
3. q 누르면 shutdown

[Hint]
- 구글의 도움 받기
"""
""" 사용된 알고리즘
    1초의 시간을 갖고 캡쳐를 해야함으로
    이전의 시간을 기록하고 현재의 시간을 받아와서
    그 값들의 차가 1이상이 될때 캡쳐를 한다.
"""
import cv2
import time

def main():

    cap = cv2.VideoCapture(0)
    
    start = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Warning !!")
            break
        
        end = time.time()
        
        if end - start >= 1:
            cv2.imwrite("img" + str(time.time()) +".png", frame)
            start = end
            
        key = cv2.waitKey(1)
        cv2.imshow("frame", frame)
        
        if key == ord("q"):
            print("Stop Capture")
            break
        
    if cap.isOpened():
        cap.release()
        
if __name__ == "__main__":
    main()