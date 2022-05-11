#RECOGNIZE

from datetime import datetime

import cv2
import numpy as np
import time
import sys
import playsound as ps
import os
import rec

start = time.time()
period = 20
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer1.yml')
flag = 0
id = 0
filename = 'filename'
dict = {
    'item1': 1
}

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 7)


    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, conf = recognizer.predict(roi_gray)
        cell = 2

        if (conf < 50):
            if (id == 1):
                id = 'Dharani'
                img_item = "1501.png"
                cv2.imwrite(img_item, roi_gray)
                cell += 1
                if ((str(id)) not in dict):
                    filename = rec.output1('recognized_data', 'class1', cell, '1501.png', id,str(datetime.now()), 'Recognized')
                    dict[str(id)] = str(id)

            elif (id == 3):
                id = 'Jyothika'
                img_item1 = "1502.png"
                cv2.imwrite(img_item1, roi_gray)
                cell += 1
                if ((str(id)) not in dict):
                    filename = rec.output1('recognized_data', 'class1', cell, '1502.png', id, str(datetime.now()),'Recognized')
                    dict[str(id)] = str(id)

            elif (id == 2):
                id = 'Muzammil'
                img_item2 = "1503.png"
                cell += 1
                cv2.imwrite(img_item2, roi_gray)
                if ((str(id)) not in dict):
                    filename = rec.output1('recognized_data', 'class1', cell,'1503.png', id, str(datetime.now()), 'Recognized')
                    dict[str(id)] = str(id)

        else:
            id = 'Unknown, can not recognize'
            img_item3 = "1504.png"
            cv2.imwrite(img_item3, roi_gray)
            ucell =cell+1
            filename = rec.output1('recognized_data', 'class1', ucell, '1504.png', id,str(datetime.now()), 'Not_Recognized')
            flag = flag + 1
            break

        cv2.putText(img, str(id) + " " + str(conf), (x, y - 10), font, 0.55, (120, 255, 120), 1)
        # cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255))
    cv2.imshow('frame', img)
    # cv2.imshow('gray',gray);
    if flag == 10:
        #ps.playsound('transactionSound.mp3')
        print("Transaction Blocked")
        print("UNKNOWN")
        break
    if time.time() > start + period:
        #sleep(float(durationInMS) / 1000.0)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
