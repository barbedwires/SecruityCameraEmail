import time
import cv2 
import datetime as dt 


capture = cv2.VideoCapture(0)

face_rec = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_rec = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")


recongnized = False
recongnized_time = False
timer = False
RECORD_AFTER_RECONGNITION = 7

frame_size = (int(capture.get(3)), int(capture.get(4)))
cc = cv2.VideoWriter_fourcc(*"mp4v")


while True:
    z, frame = capture.read()

    gray_screen = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_rec.detectMultiScale(gray_screen, 1.1, 5)

    if len(faces) > 0:
        if recongnized:
            timer = False
        else:
            recongnized = True
            current_time = dt.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            videoOutput = cv2.VideoWriter(f"{current_time}.mp4", cc, 20, frame_size)
            print("Recording has begun")
    elif recongnized:
        if timer:
            if time.time() - recongnition_stopped_time >= RECORD_AFTER_RECONGNITION:
                recongnized = False
                timer = False
                videoOutput.release()
                print("No longer recording")
        else:
            timer = True
            recongnition_stopped_time = time.time()

    if recongnized:
        videoOutput.write(frame)

 

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord(']'):
        break

videoOutput.release()
capture.release()
cv2.destroyAllWindows()