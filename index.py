import cv2
import numpy as np
import datetime, time
import json
import dlib
mport cv2
# start the camera
cap = cv2.VideoCapture(args.src)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.h)
ret, frame = cap.read()

 #face detection and recognition
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0)  
while 1:  
    ret, img = cap.read()   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
  
    for (x,y,w,h) in faces:  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
    cv2.imshow('img',img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release()  
cv2.destroyAllWindows() 
