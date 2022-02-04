import cv2
import mediapipe as mp
import random
import time


mp_draw = mp.solutions.drawing_utils  # Draw the  hand pose
mp_hand = mp.solutions.hands  # solution for hand

tipIds = [4, 8, 12, 16, 20]  # to identify tip of all fingers
video = cv2.VideoCapture(0)

def toss1():
    with mp_hand.Hands(min_detection_confidence=0.5,
                       min_tracking_confidence=0.5) as hands:
        while True:
            ret, image = video.read()  # return image or video
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)  # again return the processed image
            image.flags.writeable = True  # again write process image
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # processed image color convertor
            lmList = []
            if results.multi_hand_landmarks:  # hand land mark https://media.geeksforgeeks.org/wp-content/uploads/20210802154942/HandLandmarks.png
                for hand_landmark in results.multi_hand_landmarks:
                    myHands = results.multi_hand_landmarks[0]  # strating point of a landmark
                    for id, lm in enumerate(myHands.landmark):  # coordinate of the axis in landmarl
                        h, w, c = image.shape  # height and weight of frame
                        cx, cy = int(lm.x * w), int(lm.y * h)  # coordinate axis  value
                        lmList.append([id, cx, cy])  # list for coordinate
                    mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)  # hand coco model
            fingers = []
            if len(lmList) != 0:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total = fingers.count(1)
                print(total)
                

                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, str(total), (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)

            cv2.imshow("Frame", image)
            cv2.waitKey(1)

            k = cv2.waitKey(1)
            if k == ord('t'):
                break


def counter():
    for i in range(3, 0, -1):
        print(i)
        #time.sleep(1)
        ret, image = video.read()
        cv2.rectangle(image, (20, 100), (70, 125), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str(i), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

        cv2.imshow("Frame", image)
        cv2.waitKey(1000)


def odd_even():
    while True:
        ret, image = video.read()
        cv2.putText(image, ("Press e For Even o for Odd "), (45, 275), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 2)
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('e'):
            print("Even")
            cv2.putText(image, ("Even is choosen"), (45, 175), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
            cv2.imshow("Frame",image)
            cv2.waitKey(5)
            break
        elif k == ord('o'):
            print("Odd")
            cv2.putText(image, ("Odd is choosen"), (45, 175), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
            cv2.imshow("Frame",image)
            cv2.waitKey(5)
            break


def randgen():
    ra1 = random.choice([0, 1, 2, 3, 4, 5])
    print(ra1);
    ret, image = video.read()
    cv2.rectangle(image, (20, 100), (70, 125), (0, 255, 0), cv2.FILLED)
    cv2.putText(image, str(ra1), (45, 175), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
    cv2.imshow("Frame",image)
    cv2.waitKey(6)

if __name__=="__main__":
    odd_even()
    counter()
    toss1()
    randgen()