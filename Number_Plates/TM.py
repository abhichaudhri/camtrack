import cv2
#from matplotlib import pyplot as plt
import numpy as np


cap = cv2.VideoCapture(0) #Webcam Capture
f = 0
while(True):

	ret, frame = cap.read()
	#ret1, frame1 = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

	#for i in range(2):
		
	template = cv2.imread('np.jpeg',0)
	template1 = cv2.imread('np1.jpeg',0)
	w, h = template.shape[::-1]
	w, h = template1.shape[::-1]
	res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
	res1 = cv2.matchTemplate(gray,template1,cv2.TM_CCOEFF_NORMED)

	threshold = 0.47
	loc = np.where(res >=threshold)
	loc1 = np.where(res1 >=threshold)

	#for pt in zip(*loc[::-1]):
	#	cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
		# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

		# top_left = min_loc
		# bottom_right = (top_left[0] + w, top_left[1] + h)

		# cv2.rectangle(frame,top_left, bottom_right, 255, 1)
		# cv2.putText(frame, 'Detected Number Plate: ', (top_left[0],top_left[1]-10), 
		# 		cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))
	for pt in zip(*loc[::-1]):
		cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), (255,230,230), 2)
		cv2.imwrite("adad.png",template)
		print("Plate Saved!")
		f = 1
	#cv2.imshow('Test',frame)

	for pt in zip(*loc1[::-1]):
	 	cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), (255,230,230), 10)
	 	cv2.imwrite("adad1.png",template1)

	cv2.imshow('Test1',frame)
	
	if f==1:
		break

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows() 