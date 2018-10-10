import cv2
import numpy as np

# img_bgr = cv2.imread("np.jpeg")
img_bgr1 = cv2.imread("np1.jpeg")

# img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_gray1 = cv2.cvtColor(img_bgr1, cv2.COLOR_BGR2GRAY)

# template = cv2.imread("np2.jpeg", 0)
template1 = cv2.imread("np3.jpeg", 0)
# w, h=template.shape[::-1]
w, h=template1.shape[::-1]

# res=cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
res1=cv2.matchTemplate(img_gray1, template1, cv2.TM_CCOEFF_NORMED)

threhold = 0.8
#loc = np.where(res >=threhold)

loc = np.where(res1 >=threhold)

while(True):
	for pt in zip(*loc[::-1]):
		# cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
		cv2.rectangle(img_bgr1, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
		
		# cv2.imshow("Detected", img_bgr)
		cv2.imshow("Detected", img_bgr1)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# cap.release()
cv2.destroyAllWindows()