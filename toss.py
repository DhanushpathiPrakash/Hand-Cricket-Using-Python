import cv2
import mediapipe as mp
import random
import time


mp_draw = mp.solutions.drawing_utils  # Draw the  hand pose
mp_hand = mp.solutions.hands  # solution for hand

tipIds = [4, 8, 12, 16, 20]  # to identify tip of all fingers
video = cv2.VideoCapture(0)
video.set(3, 1366)
video.set(4, 768)

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


                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, str(total), (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)

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
    prev = time.time()
    TIMER = int(3)
    while TIMER >= 0:
        #print(TIMER)
        # time.sleep(1)
        ret, image = video.read()
        cv2.circle(image, (45, 45), 35, (255, 255, 255), -1)
        cv2.putText(image, str(TIMER), (25, 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (127, 30, 12), 3)
        cv2.imshow("Frame", image)
        cv2.waitKey(100)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def counter2():
    prev = time.time()
    TIMER = int(2)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.circle(image, (45, 45), 35, (255, 255, 255), -1)
        cv2.putText(image, str(TIMER), (25, 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (127, 30, 12), 3)
        cv2.imshow("Frame", image)
        cv2.waitKey(10)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def odd_even():
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (380, 600), (900, 650), (116, 132, 255), cv2.FILLED)
        cv2.putText(image, ("Press e For Even o for Odd "), (390, 635), cv2.FONT_HERSHEY_DUPLEX, 1.1, (114, 61, 88), 2)
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('e'):
            print("Even")
            cv2.rectangle(image, (480, 660), (760, 700), (252, 249, 178), cv2.FILLED)
            cv2.putText(image, ("Even is choosen"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (9, 19, 83), 1)
            cv2.imshow("Frame" ,image)
            cv2.waitKey(100)
            return "Even"
        elif k == ord('o'):
            print("Odd")
            cv2.rectangle(image, (480, 660), (760, 700), (252, 249, 178), cv2.FILLED)
            cv2.putText(image, ("Odd is choosen"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (9, 19, 83), 1)
            cv2.imshow("Frame" ,image)
            cv2.waitKey(100)
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
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (350, 600), (950, 650), (163, 111, 103), cv2.FILLED)
        cv2.putText(image, ("Press b For Bat and w for Bowl"), (360, 635), cv2.FONT_HERSHEY_DUPLEX, 1.1, (98, 225, 255),2)
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('b'):
            print("Bat")
            cv2.rectangle(image, (500, 660), (760, 700), (109, 76, 76), cv2.FILLED)
            cv2.putText(image, ("Bat"), (600, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (148, 225, 255), 1)
            cv2.imshow("Frame",image)
            cv2.waitKey(250)
            return "Bat"
        elif k == ord('w'):
            print("Bowl")
            cv2.rectangle(image, (500, 660), (760, 700), (109, 76, 76), cv2.FILLED)
            cv2.putText(image, ("Bowl"), (600, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (148, 225, 255), 1)
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


def vran():
    prev = time.time()
    TIMER = int(2)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (480, 660), (800, 700), (0, 181, 248), cv2.FILLED)
        cv2.putText(image, ("You Loss the toss"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (127, 34, 94), 1)
        cv2.imshow("Frame", image)
        cv2.waitKey(30)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1
    prev = time.time()
    TIMER = int(2)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (480, 660), (790, 700), (0, 181, 248), cv2.FILLED)
        cv2.putText(image, ("System select for"), (490, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (127, 34, 94), 1)
        cv2.imshow("Frame", image)
        cv2.waitKey(30)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

    prev = time.time()
    TIMER = int(2)
    vran1 = random.choice(["Bat", "Bowl"])
    print(vran1);
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (590, 660), (680, 700), (109, 76, 76), cv2.FILLED)
        cv2.putText(image, str(vran1), (600, 690), cv2.FONT_HERSHEY_DUPLEX, 1, (148, 225, 255), 1)
        cv2.imshow("Frame",image)
        cv2.waitKey(30)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1
    return vran1

def temp_score1(temp_score,ball):
    prev = time.time()
    TIMER = int(1)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (20, 620), (370, 690), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str("Batting: " + str(temp_score)), (40, 675), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 3)
        cv2.rectangle(image, (900, 20), (1250, 90), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str("Bowling: " + str(ball)), (920, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow("Frame", image)
        cv2.waitKey(100)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def out_scr(score):
    prev = time.time()
    TIMER = int(1)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (20, 300), (300, 395), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str("Score:" + str(score)), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow("Frame", image)
        cv2.waitKey(100)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

def ready():
    while True:
        ret, image = video.read()
        cv2.rectangle(image, (350, 600), (910, 650), (231, 239, 228), cv2.FILLED)
        cv2.putText(image, ("Press r to start 2nd Innings !"), (370, 635), cv2.FONT_HERSHEY_DUPLEX, 1.1, (32, 68, 6),2)
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('r'):
            print("Ready !")
            break

def final_result():
    prev = time.time()
    TIMER = int(2)
    while TIMER >= 0:
        ret, image = video.read()
        cv2.rectangle(image, (350, 600), (910, 650), (231, 239, 228), cv2.FILLED)
        cv2.putText(image, str(display), (370, 635), cv2.FONT_HERSHEY_DUPLEX, 1.1, (32, 68, 6), 2)
        cv2.imshow("Frame", image)
        cv2.waitKey(50)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1



if __name__ =="__main__":
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
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:", bowling)
                temp_score1(batting,bowling)
                if (bowling == batting) or (score_1 < score_2):
                    print("Out !! 2nd Innings score:", score_2)
                    out_scr(score_2)
                    break
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
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:",bowling)
                temp_score1(batting,bowling)
                if (bowling == batting) or (score_1 < score_2):
                    print("Out !! 2nd Innings score:", score_2)
                    out_scr(score_2)
                    break
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
                display = ("You are the losser")
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
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                if (bowling == batting) or (score_5 < score_6):
                    print("Out !! 2nd Innings score:", score_6)
                    out_scr(score_6)
                    break
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
                display = ("System own the match")
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
                print("2nd Innings Batting:", batting)
                print("2nd Innings Bowling:", bowling)
                temp_score1(batting, bowling)
                if (bowling == batting) or (score_5 < score_6):
                    print("Out !! 2nd Innings score:", score_6)
                    out_scr(score_6)
                    break
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
                display = ("You are the losser")
                final_result()

video.release()
cv2.destroyAllWindows()