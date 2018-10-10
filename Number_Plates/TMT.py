import cv2
import numpy as np


cap = cv2.VideoCapture(0)
template = cv2.imread('np0.jpeg',0)
w, h = template.shape[::-1]
while(True):
    ret, frame = cap.read()
    i= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(i,template,2)
    cv2.imshow('frame',i)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[0] + h)
    cv2.rectangle(i, top_left, bottom_right, (50, 0, 130), 2)
    cv2.imshow('output',i)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()