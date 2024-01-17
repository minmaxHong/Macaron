"""
웹캠 스트리밍 구현하기
종료조건 : 'q'키를 눌렀을 때

[Hint]
- 프레임을 하나하나 송출한다고 생각
- while문 사용
- cv2.VideoCapture 사용
- cv2.imshow 사용
- cv2.waitKey 사용
"""


# == 문풀 완료 ==

import cv2

def main():
    
    cap = cv2.VideoCapture(0) 
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Warning")
            break
        
        cv2.imshow('frame', frame)
        
        #  키보드 입력 대기 (25 / 1000(second))
        key = cv2.waitKey(25)
        
        # 27은 ESC(ASCII CODE)
        if key == ord('q'):
            break
        
    if cap.isOpened():
        cap.release()
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()