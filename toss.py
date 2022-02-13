import cv2
import mediapipe as mp
import random
import time
import numpy as np

mp_draw = mp.solutions.drawing_utils  # Draw the  hand pose
mp_hand = mp.solutions.hands  # solution for hand

tipIds = [4, 8, 12, 16, 20]  # to identify tip of all fingers
video = cv2.VideoCapture(0)
video.set(3, 1366)
video.set(4, 768)

def logo():
    prev = time.time()
    TIMER = int(1)
    logo1 = cv2.imread('HPL.png')
    size = 350
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    while video.isOpened() and TIMER >= 0:
        ret, image = video.read()
        if ret:
            #image = cv2.flip(image, 0)
            roi = image[-size - 250:-250, -size - 500:-500]
            roi[np.where(mask)] = 0
            roi += logo1
            cv2.imshow('Frame', image)
            cv2.waitKey(30)
            cur = time.time()
            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER - 1

#temp_scroe1 = 0;
def toss1():
    #global temp_scroe1
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
                # print("Toss One Function ic called", total)


                cv2.rectangle(image, (20, 300), (270, 425), (189, 51, 13), cv2.FILLED)
                cv2.putText(image, str(total), (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (243, 255, 242), 5)

                cv2.imshow("Frame", image)
                cv2.waitKey(10)

                if total:
                    return total
                elif total == 0:
                    return total

        # k = cv2.waitKey(1)
        # if k == ord('t'):
        #   break

def counter():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    prev = time.time()
    TIMER = int(3)
    while TIMER >= 0:
        #print(TIMER)
        # time.sleep(1)
        ret, image = video.read()
        cv2.circle(image, (45, 45), 35, (255, 255, 255), -1)
        cv2.putText(image, str(TIMER), (25, 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (127, 30, 12), 3)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        cv2.waitKey(100)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def counter2():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    prev = time.time()
    TIMER = int(2)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.circle(image, (45, 45), 35, (255, 255, 255), -1)
        cv2.putText(image, str(TIMER), (25, 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (127, 30, 12), 3)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        cv2.waitKey(10)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def odd_even():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (378, 598), (902, 652), (27, 91, 240), 2)
        cv2.rectangle(image, (380, 600), (900, 650), (3, 201, 250), cv2.FILLED)
        cv2.putText(image, ("Press e For Even o for Odd "), (390, 635), cv2.FONT_HERSHEY_DUPLEX, 1.1, (148, 89, 18), 2)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('e'):
            print("Even")
            cv2.rectangle(image, (478, 658), (762, 702), (0, 0, 0), 2)
            cv2.rectangle(image, (480, 660), (760, 700), (252, 249, 178), cv2.FILLED)
            cv2.putText(image, ("Even is choosen"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (9, 19, 83), 1)
            roi = image[-size - 10:-10, -size - 10:-10]
            roi[np.where(mask)] = 0
            roi += logo1
            cv2.imshow("Frame" ,image)
            cv2.waitKey(250)
            return "Even"
        elif k == ord('o'):
            print("Odd")
            cv2.rectangle(image, (478, 658), (762, 702), (0, 0, 0), 2)
            cv2.rectangle(image, (480, 660), (760, 700), (252, 249, 178), cv2.FILLED)
            cv2.putText(image, ("Odd is choosen"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (9, 19, 83), 1)
            roi = image[-size - 10:-10, -size - 10:-10]
            roi[np.where(mask)] = 0
            roi += logo1
            cv2.imshow("Frame" ,image)
            cv2.waitKey(250)
            return "Odd"


def randgen():
    ra1 = random.choice([0, 1, 2, 3, 4, 5])
    print(ra1);
    ret, image = video.read()
    #cv2.rectangle(image, (550, 20), (610, 90), (0, 255, 0), cv2.FILLED)
    #cv2.putText(image, str(ra1), (560, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
    cv2.imshow("Frame" ,image)
    cv2.waitKey(10)

    if ra1:
        return ra1

def prefer():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (348, 598), (992, 652), (53, 96, 137), 2)
        cv2.rectangle(image, (350, 600), (990, 650), (37, 19, 184), cv2.FILLED)
        cv2.putText(image, ("Press 'b' For Bat and 'w' for Bowl"), (360, 635), cv2.FONT_HERSHEY_DUPLEX, 1.1, (113, 171, 205),2)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('b'):
            print("Bat")
            cv2.rectangle(image, (498, 658), (762, 702), (20, 22, 31))
            cv2.rectangle(image, (500, 660), (760, 700), (86, 32, 58), cv2.FILLED)
            cv2.putText(image, ("Bat"), (600, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (92, 202, 234), 1)
            roi = image[-size - 10:-10, -size - 10:-10]
            roi[np.where(mask)] = 0
            roi += logo1
            cv2.imshow("Frame",image)
            cv2.waitKey(250)
            return "Bat"
        elif k == ord('w'):
            print("Bowl")
            cv2.rectangle(image, (496, 656), (764, 704), (20, 22, 31))
            cv2.rectangle(image, (498, 658), (762, 702), (86, 32, 58), cv2.FILLED)
            cv2.putText(image, ("Bowl"), (600, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (92, 202, 234), 1)
            roi = image[-size - 10:-10, -size - 10:-10]
            roi[np.where(mask)] = 0
            roi += logo1
            cv2.imshow("Frame",image)
            cv2.waitKey(250)
            return "Bowl"

def owntoss():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    ret, image = video.read()
    cv2.rectangle(image, (478, 658), (802, 702),(89, 45, 134),2)
    cv2.rectangle(image, (480, 660), (800, 700), (231, 177, 222), cv2.FILLED)
    cv2.putText(image, ("You own the toss"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (74, 11, 41), 1)
    roi = image[-size - 10:-10, -size - 10:-10]
    roi[np.where(mask)] = 0
    roi += logo1
    cv2.imshow("Frame", image)
    cv2.waitKey(1000)

def startg():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    ret, image = video.read()
    cv2.rectangle(image, (480, 660), (800, 700), (231, 177, 222), cv2.FILLED)
    cv2.putText(image, ("Let's start Game"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (74, 11, 41), 1)
    roi = image[-size - 10:-10, -size - 10:-10]
    roi[np.where(mask)] = 0
    roi += logo1
    cv2.imshow("Frame", image)
    cv2.waitKey(1000)

def vran():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    prev = time.time()
    TIMER = int(1)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (478, 658), (802, 702),(89, 45, 134),2)
        cv2.rectangle(image, (480, 660), (800, 700), (231, 177, 222), cv2.FILLED)
        cv2.putText(image, ("You Loss the toss"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (74, 11, 41), 1)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        cv2.waitKey(30)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1
    prev = time.time()
    TIMER = int(1)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (478, 658), (792, 702), (89, 45, 134), 2)
        cv2.rectangle(image, (480, 660), (790, 700), (231, 177, 222), cv2.FILLED)
        cv2.putText(image, ("System select for"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (74, 11, 41), 1)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        cv2.waitKey(30)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

    prev = time.time()
    TIMER = int(1)
    vran1 = random.choice(["Bat", "Bowl"])
    print(vran1);
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (496, 656), (764, 704), (20, 22, 31))
        cv2.rectangle(image, (498, 658), (762, 702), (86, 32, 58), cv2.FILLED)
        cv2.putText(image, str(vran1), (600, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (92, 202, 234), 1)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame",image)
        cv2.waitKey(30)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1
    return vran1

def temp_score1(temp_score,ball):
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    prev = time.time()

    bat = cv2.imread('bat.png')
    sizeb = 100
    bat = cv2.resize(bat, (sizeb, sizeb))
    img2gray = cv2.cvtColor(bat, cv2.COLOR_BGR2GRAY)
    ret, maskb = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

    ball1 = cv2.imread('ball.png')
    sizel = 50
    ball1 = cv2.resize(ball1, (sizel, sizel))
    img2gray = cv2.cvtColor(ball1, cv2.COLOR_BGR2GRAY)
    ret, maskl = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

    TIMER = int(1)
    while TIMER >= 0:
        ret, image = video.read()

        cv2.rectangle(image, (98, 563), (162, 702), (240, 240, 240), 2)
        cv2.rectangle(image, (100, 565), (160, 700), (94, 50, 33), cv2.FILLED)
        roib = image[-sizeb - 5:-5, -sizeb - 1100:-1100]
        roib[np.where(maskb)] = 0
        roib += bat
        cv2.putText(image, str(temp_score), (110, 625), cv2.FONT_HERSHEY_SIMPLEX,2, (10, 208, 241), 3)

        cv2.rectangle(image, (1173, 18), (1237, 137), (240, 240, 240), 2)
        cv2.rectangle(image, (1175, 20), (1235, 135), (94, 50, 33), cv2.FILLED)
        roil = image[-sizel - 585:-585, -sizel - 50:-50]
        roil[np.where(maskl)] = 0
        roil += ball1
        cv2.putText(image, str(ball), (1185, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (10, 208, 241), 3)

        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)

        cv2.waitKey(100)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def out_scr(score):
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    prev = time.time()
    TIMER = int(1)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (448, 618), (777, 682),(10, 208, 241))
        cv2.rectangle(image, (450, 620), (775, 680), (94, 50, 33), cv2.FILLED)
        cv2.putText(image, str("Score:" + str(score)), (460, 670), cv2.FONT_HERSHEY_SIMPLEX, 2, (10, 208, 241), 2)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        cv2.waitKey(100)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def ready():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (350, 600), (910, 650), (231, 239, 228), cv2.FILLED)
        cv2.putText(image, ("Press r to start 2nd Innings !"), (370, 635), cv2.FONT_HERSHEY_DUPLEX, 1.1, (32, 68, 6),2)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('r'):
            print("Ready !")
            break

def final_result():
    logo1 = cv2.imread('HPL.png')
    size = 100
    logo1 = cv2.resize(logo1, (size, size))
    img2gray = cv2.cvtColor(logo1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    prev = time.time()
    TIMER = int(2)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (370, 440), (770, 495), (185, 70, 45), cv2.FILLED)
        cv2.putText(image, str(display), (390, 480), cv2.FONT_HERSHEY_DUPLEX, 1.1, (255, 255, 255), 3)
        roi = image[-size - 10:-10, -size - 10:-10]
        roi[np.where(mask)] = 0
        roi += logo1
        cv2.imshow("Frame", image)
        cv2.waitKey(50)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

if __name__ =="__main__":
    logo()
    toss = odd_even()
    print("User Preference:", toss)
    counter()
    value = toss1()
    print("User Value:", value)
    ran_value = randgen()
    if ran_value == None:
        ran_value = 0
    print("System Value:", ran_value)
    tosstotal = ran_value +value
    print("Total:",tosstotal)
    score_1 = 0
    score_2 = 0
    if (((tosstotal) % 2 == 0) and (toss == "Even")) or (((tosstotal) % 2 != 0) and (toss == "Odd")):
        print("You own the toss")
        owntoss()
        #prefer = str(input("Type b for Bat and w for Bowl"))
        #print(prefer)
        prefer = prefer()
        print("Let's start the game")
        if prefer == "Bat":
            while True:
                counter2()
                batting = toss1()
                bowling = randgen()
                if bowling == None:
                    bowling = 0
                print("1st Innings Batting:", batting)
                print("1st Innings Bowling:", bowling)
                temp_score1(batting,bowling)
                if batting == bowling:
                    print("Out !! 1st Innings Score:", score_1)
                    out_scr(score_1)
                    break
                score_1 += batting
            ready()
            while True:
                counter2()
                batting = randgen()
                bowling = toss1()
                if batting == None:
                    batting = 0
                if (bowling == batting) or (score_1 < score_2):
                    print("Out !! 2nd Innings score:", score_2)
                    out_scr(score_2)
                    break
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                score_2 += batting
            if (score_1 > score_2):
                print("You are the winner")
                display = ("You are the winner")
                final_result()
            elif (score_1 == score_2):
                print("Draw")
                display = ("Match Draw")
                final_result()
            else:
                print("System own the match")
                display = ("System Own the Match")
                final_result()

        elif prefer == "Bowl":
            while True:
                counter2()
                batting = randgen()
                bowling = toss1()
                if batting == None:
                    batting = 0
                print("1st Innings Batting:", batting)
                print("1st Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                if bowling == batting:
                    print("Out !! 1st Innings Score:", score_1)
                    out_scr(score_1)
                    break
                score_1 += batting
            ready()
            while True:
                counter2()
                batting = toss1()
                bowling = randgen()
                if bowling == None:
                    bowling = 0
                if (bowling == batting) or (score_1 < score_2):
                    print("Out !! 2nd Innings score:", score_2)
                    out_scr(score_2)
                    break
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                score_2 += batting
            if (score_1 < score_2):
                print("You are the winner")
                display = ("You are the winner")
                final_result()
            elif (score_1 == score_2):
                print("Match Draw")
                display = ("Match Draw")
                final_result()
            else:
                print("You are the losser")
                display = ("System Own the Match")
                final_result()

    else:
        score_5 = 0
        score_6 = 0
        system_pick = vran()
        print("Let's start the game")
        if system_pick == "Bat":
            while True:
                counter2()
                batting = randgen()
                bowling = toss1()
                if batting == None:
                    batting = 0
                print("1st Innings Batting:", batting)
                print("1st Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                if batting == bowling:
                    print("Out !! 1st Innings Score:", score_5)
                    out_scr(score_5)
                    break
                score_5 += batting
            ready()
            while True:
                counter2()
                batting = toss1()
                bowling = randgen()
                if bowling == None:
                    bowling = 0
                if (bowling == batting) or (score_5 < score_6):
                    print("Out !! 2nd Innings score:", score_6)
                    out_scr(score_6)
                    break
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                score_6 += batting
            if (score_5 < score_6):
                print("You are the winner")
                display = ("You are the Winner")
                final_result()
            elif (score_5 == score_6):
                print("Draw")
                display = ("Draw")
                final_result()
            else:
                print("System own the match")
                display = ("System own the Match")
                final_result()

        elif system_pick == "Bowl":
            while True:
                counter2()
                batting = toss1()
                bowling = randgen()
                if bowling == None:
                    bowling = 0
                print("1st Innings Batting:", batting)
                print("1st Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                if bowling == batting:
                    print("Out !! 1st Innings Score:", score_5)
                    out_scr(score_5)
                    break
                score_5 += batting
            ready()
            while True:
                counter2()
                batting = randgen()
                bowling = toss1()
                if batting == None:
                    batting = 0
                if (bowling == batting) or (score_5 < score_6):
                    print("Out !! 2nd Innings score:", score_6)
                    out_scr(score_6)
                    break
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                score_6 += batting
            if (score_5 > score_6):
                print("You are the winner")
                display = ("You are the Winner")
                final_result()
            elif (score_5 == score_6):
                print("Match Draw")
                display = ("Match Draw")
                final_result()
            else:
                print("You are the losser")
                display = ("System Own the Match")
                final_result()

video.release()
cv2.destroyAllWindows()