import cv2
import mediapipe as mp
import random
import time


mp_draw = mp.solutions.drawing_utils  # Draw the  hand pose
mp_hand = mp.solutions.hands  # solution for hand

tipIds = [4, 8, 12, 16, 20]  # to identify tip of all fingers
video = cv2.VideoCapture(0)

def toss1():
    total = ""
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
                #print("Toss One Function ic called", total)

                cv2.rectangle(image, (30, 20), (100, 95), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, str(total), (45, 80), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)

                cv2.imshow("Frame", image)
                cv2.waitKey(10)

                #if total:
                    #return total


            k = cv2.waitKey(1)
            if k == ord('t'):
                break

def counter():
    for i in range(3, 0, -1):
        print(i)
        #time.sleep(1)
        ret, image = video.read()
        cv2.rectangle(image, (30, 20), (100, 95), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str(i), (45, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
        cv2.imshow("Frame", image)
        cv2.waitKey(1000)


def odd_even():
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (55, 370), (575, 420), (39, 0, 130), cv2.FILLED)
        cv2.putText(image, ("Press e For Even o for Odd "), (65, 410), cv2.FONT_HERSHEY_DUPLEX, 1.1, (250, 88, 182), 2)
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('e'):
            print("Even")
            cv2.rectangle(image, (150, 425), (415, 455), (250, 88, 182))
            cv2.putText(image, ("Even is choosen"), (153, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 1)
            cv2.imshow("Frame",image)
            cv2.waitKey(250)
            return "Even"
        elif k == ord('o'):
            print("Odd")
            cv2.rectangle(image, (150, 425), (415, 455), (250, 88, 182))
            cv2.putText(image, ("Odd is choosen"), (153, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 1)
            cv2.imshow("Frame",image)
            cv2.waitKey(250)
            return "Odd"


def randgen():
    ra1 = random.choice([0, 1, 2, 3, 4, 5])
    print(ra1);
    ret, image = video.read()
    cv2.rectangle(image, (550, 20), (610, 90), (0, 255, 0), cv2.FILLED)
    cv2.putText(image, str(ra1), (560, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
    cv2.imshow("Frame",image)
    cv2.waitKey(1000)

    if ra1:
        return ra1

def owntoss():
    ret, image = video.read()
    cv2.rectangle(image, (125, 425), (450, 455), (250, 88, 182), cv2.FILLED)
    cv2.putText(image, ("You own the toss"), (150, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 0)
    cv2.imshow("Frame", image)
    cv2.waitKey(1000)

def prefer():
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (55, 370), (575, 420), (39, 0, 130), cv2.FILLED)
        cv2.putText(image, ("Press b For Bat and w for Bowl"), (65, 410), cv2.FONT_HERSHEY_DUPLEX, 1.1, (250, 88, 182), 2)
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('b'):
            print("Bat")
            cv2.rectangle(image, (150, 425), (415, 455), (250, 88, 182))
            cv2.putText(image, ("Bat"), (153, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 1)
            cv2.imshow("Frame",image)
            cv2.waitKey(250)
            return "Bat"
        elif k == ord('w'):
            print("Bowl")
            cv2.rectangle(image, (150, 425), (415, 455), (250, 88, 182))
            cv2.putText(image, ("Bowl"), (153, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 1)
            cv2.imshow("Frame",image)
            cv2.waitKey(250)
            return "Bowl"

def owntoss():
    ret, image = video.read()
    cv2.rectangle(image, (125, 425), (450, 455), (250, 88, 182), cv2.FILLED)
    cv2.putText(image, ("You own the toss"), (150, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 0)
    cv2.imshow("Frame", image)
    cv2.waitKey(1000)

def startg():
    ret, image = video.read()
    cv2.rectangle(image, (125, 425), (450, 455), (250, 88, 182), cv2.FILLED)
    cv2.putText(image, ("Let's start Game"), (150, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 0)
    cv2.imshow("Frame", image)
    cv2.waitKey(1000)

def tossloss():
    ret, image = video.read()
    cv2.rectangle(image, (125, 425), (450, 455), (250, 88, 182), cv2.FILLED)
    cv2.putText(image, ("You Loss the toss"), (150, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 0)
    cv2.imshow("Frame", image)
    cv2.waitKey(1000)

def vran():
    vran1 = random.choice(["bat","bowl"])
    print(vran1);
    ret, image = video.read()
    cv2.rectangle(image, (230, 425), (340, 455), (250, 88, 182))
    cv2.putText(image, str(vran1), (253, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 1)
    cv2.imshow("Frame",image)
    cv2.waitKey(1000)


def sysselect():
    ret, image = video.read()
    cv2.rectangle(image, (125, 425), (450, 455), (250, 88, 182), cv2.FILLED)
    cv2.putText(image, ("System select for"), (150, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (154, 208, 236), 0)
    cv2.imshow("Frame", image)
    cv2.waitKey(1000)




if __name__=="__main__":
    toss=odd_even()
    print("Returned value toss", toss)
    counter()
    #toss1()
    value = toss1()
    print("returned value", value)
    ran_value = randgen()
    randgen()
    if ran_value == None:
        ran_value = 0
    print("returned random value ", ran_value)
    tosstotal = ran_value+value
    print(tosstotal)
    if (((tosstotal)% 2 == 0) and (toss == "Even")) or (((tosstotal)% 2 != 0) and (toss == "Odd")):
        print("You own the tossYou own the toss")
        owntoss()
        bat_bowl = prefer()
        print("Returned value Prefer", prefer)
        startg()
    else:
        tossloss()
        sysselect()
        vran()
