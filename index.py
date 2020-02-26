import cv2
import numpy as np
import datetime, time
import jason
import dlib
# start the camera
cap = cv2.VideoCapture(args.src)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.h)
ret, frame = cap.read()
