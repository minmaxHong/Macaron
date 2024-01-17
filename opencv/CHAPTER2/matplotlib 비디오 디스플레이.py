import cv2
from matplotlib import pyplot as plt

def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()

def handle_close(evt):
    print("Close figure!")
    cap.release()
    

cap = cv2.VideoCapture(0)

plt.ion() # 대화 모드로 설정한다.
fig = plt.figure(figsize = (10, 6))
plt.axis("off")

# ========================================================================================
# fig.canvas.mpl_connect는 Matplotlib에서 이벤트 핸들러를 등록하는 함수이다.
# 이 함수를 사용하면 특정 이벤트가 발생했을 때 호출될 함수를 등록할 수 있다.
# fig는 Matplotlib의 Figure 객체를 나타내고, canvas는 해당 Figure의 그림을 그리는 영역이다.
# ========================================================================================

# ========================================================================================
# key_press_event : 키보드 키가 눌렀을때 발생한다.
# escape 키를 감지하고 cap.release()와 plt.close()를 호출하여 카메라 캡처를 해제하고, Matplotlub 창을 닫는다.
# ========================================================================================

# ========================================================================================
# close_event : Figure 창이 닫힐 때 발생한다.
# Close figure!를 출력하고 cap.release()를 호출하여 카메라 캡처를 해제한다.
# ========================================================================================

fig.canvas.manager.set_window_title("Video Capture")
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)

# == 첫 frame을 읽어오는 역할을 한다 == 
ret, frame = cap.read()
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Warning")
        break

    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) # 빠른 처리를 위하여 영상을 교체한다.
    fig.canvas.draw() # 캔버스를 다시 그린다. 
    fig.canvas.flush_events() # 다른 GUI 이벤트를 처리할 수 있다.

if cap.isOpened():
    cap.release()