import cv2
import os
import numpy as np

# Path of dataset
dataset_path = "faces"

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

label_dict = {}
current_label = 0

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

for file in os.listdir(dataset_path):
    img_path = os.path.join(dataset_path, file)

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces_rect = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces_rect:
        faces.append(gray[y:y+h,x:x+w])
        labels.append(current_label)

    label_dict[current_label] = file.split(".")[0]
    current_label += 1

recognizer.train(faces, np.array(labels))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_rect = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces_rect:

        face = gray[y:y+h,x:x+w]

        label, confidence = recognizer.predict(face)

        name = label_dict[label]

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,name,(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Face Recognition",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()