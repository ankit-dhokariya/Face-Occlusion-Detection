import cv2


class Occlusion:
    def __init__(self, face_cascade, mouth_cascade, nose_cascade, eye_cascade):
        self.face_cascade = face_cascade
        self.mouth_cascade = mouth_cascade
        self.nose_cascade = nose_cascade
        self.eye_cascade = eye_cascade

    def occlusion(self, frame, count):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
        if (len(faces) != 0):
            for x, y, w, h in faces:
                count = count + 1
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                m = int(round(y + (h / 2)))
                roi_gray_mouth = gray[m:y + h, x:x + w]
                roi_color_mouth = frame[m:y + h, x:x + w]

                mouth = self.mouth_cascade.detectMultiScale(roi_gray_mouth)
                if (len(mouth) != 0):
                    for (mx, my, mw, mh) in mouth:
                        #cv2.rectangle(roi_color_mouth, (mx, my), (mx + mw, my + mh), (255, 0, 0), 2)

                        nose = self.nose_cascade.detectMultiScale(roi_gray)
                        if (len(mouth) != 0 and len(nose) != 0):
                            for (nx, ny, nw, nh) in nose:
                                #cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 255, 0), 2)

                                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                                if (len(mouth) != 0 and len(nose) != 0 and len(eyes) != 0):
                                    for (ex, ey, ew, eh) in eyes:
                                        #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 0), 2)
                                        count = 0
                                        return roi_gray, count, True
        else:
            count = 0

        return None, count, False
