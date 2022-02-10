from multiprocessing import Process
#import Tkinter
import cv2
import time
import numpy as np
#root = Tkinter.Tk()
#width = root.winfo_screenwidth()
#height = root.winfo_screenheight()
video = cv2.VideoCapture(0)
#wCam, hCam = 640, 480
video.set(3, 1366)
video.set(4, 768)
def counter():
    prev = time.time()
    TIMER = int(20)
    while TIMER >= 0:
        print(TIMER)
        # time.sleep(1)
        ret, image = video.read()
        cv2.rectangle(image, (30, 20), (100, 95), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str(TIMER), (45, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
        cv2.imshow("Frame", image)
        cv2.waitKey(100)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1


if __name__ == '__main__':
    counter()
cv2.destroyAllWindows()