import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)
mpHands= mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0
while True:
    success, img = cap.read()

    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #lm-landmark (in form of decimals)
                # print(id,lm)
                h,w,c=img.shape #gives us width and height (for converting lm into pixels )
                cx,cy=int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id==4:
                    cv2.circle(img, (cx,cy),15,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    #frame per sec
    fps=1/(cTime-pTime)
    pTime=cTime
    #reflect fps on screen
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_ITALIC,3,(255,0,255),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)