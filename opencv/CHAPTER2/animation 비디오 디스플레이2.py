import cv2
from matplotlib import pyplot as plt
from matplotlib import animation as animation

class Video:
    def __init__(self, device = 0):
        self.cap = cv2.VideoCapture(device)
        self.ret, self.frame = self.cap.read()
        self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        
        print("start capture")
    
    def updateFrame(self, k):
        self.ret, self.frame = self.cap.read()
        self.im.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
    
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        
        print("finish capture")
        
fig = plt.figure(figsize = (10, 6))
fig.canvas.manager.set_window_title("Video Capture")
plt.axis('off')

camera = Video()
ani = animation.FuncAnimation(fig, camera.updateFrame, interval = 50)

plt.show()

camera.close()