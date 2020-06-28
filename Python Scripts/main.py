from datetime import datetime
import sqlite3
import os
import cv2
from OCCLUSION import Occlusion
from SPOOF import Spoof


def run(cardnumber):
    # Database Connectivity
    conn = sqlite3.connect('tran.db')
    cursor = conn.cursor()
    timestamp = datetime.now()

    # Initialize webcam module
    video = cv2.VideoCapture(0)

    # Load Models
    face_cascade = cv2.CascadeClassifier("..\\models\\haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("..\\models\\haarcascade_eye.xml")
    nose_cascade = cv2.CascadeClassifier("..\\models\\haarcascade_mcs_nose.xml")
    mouth_cascade = cv2.CascadeClassifier("..\\models\\haarcascade_mcs_mouth.xml")

    # Initialize LBP object

    occ = Occlusion(face_cascade, mouth_cascade, nose_cascade, eye_cascade)
    spo = Spoof(0)

    a = 1
    flag = 0
    count = 0
    no_occ = 0
    real = 0
    fake = 0

    while True:
        a = a + 1

        check, frame = video.read()
        if check is True:
            b, l, n = frame.shape

            cv2.line(frame, (int(l * 0.25), int(b * 0.25)), (int(l * 0.25), int(b * 0.375)), (0, 255, 255), 2)
            cv2.line(frame, (int(l * 0.25), int(b * 0.625)), (int(l * 0.25), int(b * 0.75)), (0, 255, 255), 2)

            cv2.line(frame, (int(l * 0.75), int(b * 0.25)), (int(l * 0.75), int(b * 0.375)), (0, 255, 255), 2)
            cv2.line(frame, (int(l * 0.75), int(b * 0.625)), (int(l * 0.75), int(b * 0.75)), (0, 255, 255), 2)

            cv2.line(frame, (int(l * 0.25), int(b * 0.25)), (int(l * 0.343), int(b * 0.25)), (0, 255, 255), 2)
            cv2.line(frame, (int(l * 0.656), int(b * 0.25)), (int(l * 0.75), int(b * 0.25)), (0, 255, 255), 2)

            cv2.line(frame, (int(l * 0.25), int(b * 0.75)), (int(l * 0.343), int(b * 0.75)), (0, 255, 255), 2)
            cv2.line(frame, (int(l * 0.656), int(b * 0.75)), (int(l * 0.75), int(b * 0.75)), (0, 255, 255), 2)

            roi_gray, count, ret = occ.occlusion(frame, count)

            if ret is True:
                no_occ = no_occ + 1
                result = spo.spoof(roi_gray)
                if (result == "real"):
                    real += 1
                    fake = 0
                elif (result == "fake"):
                    fake += 1
                    real = 0

            if (no_occ >= 10 and real >= 10):
                flag = 1
            elif (fake >= 10):
                flag = 2
            elif (count >= 15):
                flag = -1
            elif (a >= 40):
                flag = 3

            cv2.imshow('capturing', frame)
            cv2.waitKey(1)

            if (flag == 1):
                success, image = video.read()
                cv2.imwrite("frame.jpg", image)
                with open('frame.jpg', 'rb') as f:
                    data = f.read()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Trance (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,cardnumber BIGINT, picture BLOP, timestamp TEXT)
                """)
                cursor.execute("""
                INSERT INTO Trance (cardnumber,picture,timestamp) VALUES (?,?,?)
                """, (cardnumber, data, timestamp))
                os.remove("frame.jpg")
                print("Access Granted!")
                conn.commit()
                cursor.close()
                conn.close()
                break
            elif flag == -1:
                print("Access Denied!")
                break
            elif flag == 2:
                print("Access Denied!")
                break
            elif flag == 3:
                break

    video.release()
    cv2.destroyAllWindows()
    return flag
