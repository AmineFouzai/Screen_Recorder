from tkinter import *
# from video_recorder import VideoRecorder
from multiprocessing import Process
import cv2
import pyautogui
import numpy as np




class VideoAudioRecordingApp(object):
    

    def __init__(self):
        super().__init__()
        self.state = False
        self.timer = [0, 0, 0]
        self.pattern = '{0:02d}:{1:02d}:{2:02d}'
        self.app = Tk()
        self.app.title("Welcome to Screen Recording App")
        self.app.geometry('350x200')
        self.btn = Button(self.app, text="Record", command=self.callBack,bg="Black",fg="red", height = 3, width = 15,font=("Helvetica", 10))
        self.btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.lbl = Label(self.app, text="00:00:00",font=("Helvetica", 32))
        self.lbl.pack()
    

    def updateTimer(self):
        
        if (self.state):
            self.timer[2] += 1
            
            if (self.timer[2] >= 100):
                self.timer[2] = 0
                self.timer[1] += 1

            if (self.timer[1] >= 60):
                self.timer[0] += 1
                self.timer[1] = 0
     
            timeString = self.pattern.format(self.timer[0], self.timer[1], self.timer[2])
            self.lbl.configure(text=timeString)

        self.app.after(10, self.updateTimer)

    def callBack(self):
    
        self.btn.config(text="Stop")
        self.btn.config(command=self.terminateCallback)

        self.setTimerState()
       

    def terminateCallback(self):
            
            quit(self)

    def setTimerState(self):
        
        self.state = True
    
    def start(self):
        self.app.mainloop()

if __name__ == "__main__":

    app=VideoAudioRecordingApp()
    app.updateTimer()
    app.start() 