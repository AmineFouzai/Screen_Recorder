import cv2
import numpy as np
import pyautogui
from tkinter import *
from multiprocessing import Process
from time import time
from random import randint

def update_time_text():
    if (state):
        global timer

        timer[2] += 1

        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1

        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
     
        timeString = pattern.format(timer[0], timer[1], timer[2])

        lbl.configure(text=timeString)

    window.after(10, update_time_text)

def increment():
    global state
    state = True

def record():
    output = "video.avi"
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    height,width,_= img.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
    while True:
        lbl.config(text=str(randint(0,100)))
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
        cv2.imshow("Live", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()
    out.release()


process=Process(target=record)

def terminate():
    process.terminate()
    quit()


def clicked():

    btn.config(text="Stop")
    btn.config(command=terminate)
    process.start()
    increment()
   
   

state = False
timer = [0, 0, 0]
pattern = '{0:02d}:{1:02d}:{2:02d}'
window = Tk()
window.title("Welcome to Screen Recording App")
window.geometry('350x200')
btn = Button(window, text="Record", command=clicked,bg="Black",fg="red", height = 3, width = 15,font=("Helvetica", 10))
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl = Label(window, text="00:00:00",font=("Helvetica", 32))
lbl.pack()

if __name__ == "__main__":
    update_time_text()
    window.mainloop()

