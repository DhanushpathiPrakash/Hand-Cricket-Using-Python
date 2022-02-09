from multiprocessing import Process
import cv2
import numpy as np
img = np.zeros([512,512,1],dtype=np.uint8)
img.fill(255)# Create a dummy image
video = cv2.VideoCapture(0)

def func2():
    while True and video.isOpened():
        ret, image = video.read()
        cv2.imshow("Frame", image)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
def func1():
    for i in range(3, 0, -1):
        print(i)
        cv2.rectangle(img, (30, 20), (100, 95), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(i), (45, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
        cv2.imshow('a', img)
        cv2.waitKey(1000)

#while True:
#    cv2.imshow('a',img)
#    k = cv2.waitKey(0)
#    print(k)
#    if k == ord('q'):
#        break
if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()
cv2.destroyAllWindows()