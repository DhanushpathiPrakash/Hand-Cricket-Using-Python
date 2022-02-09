from multiprocessing import Process
import cv2
video = cv2.VideoCapture(0)

def func2():
    global ret, image
    while True and video.isOpened():
        ret, image = video.read()
        cv2.imshow("Frame", image)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break

def func1():
    for i in range(3, 0, -1):
        print(i)
        fn =  func2()
        cv2.rectangle(fn.image, (30, 20), (100, 95), (0, 255, 0), cv2.FILLED)
        cv2.putText(fn.image, str(i), (45, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
        cv2.waitKey(1000)

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p1.join()
  p2.join()