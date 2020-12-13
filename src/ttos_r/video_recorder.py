import cv2
import pyautogui
import numpy as np

class VideoRecorder(object):
    
    def __init__(self,output="video.avi"):
        self.output = output
        self.img = pyautogui.screenshot()
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
        self.height,self.width,_= self.img.shape
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(self.output, self.fourcc, 20.0, (self.width, self.height))
    
    def start_recording(self):
        while True:
            self.img = pyautogui.screenshot()
            self.frame = np.array(self.img)
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR)
            self.out.write(self.frame)
            cv2.imshow("Live", self.frame)
            if cv2.waitKey(1) == ord("q"):
                break
        

    def release_recording(self):
        cv2.destroyAllWindows()
        self.out.release()

videoRecorder=VideoRecorder()
try:
    videoRecorder.start_recording()
except KeyboardInterrupt as e:
    videoRecorder.release_recording()
        

    


