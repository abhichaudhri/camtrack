import numpy as np
import cv2
from openalpr import Alpr
import sys

alpr = Alpr("eu", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(1)
#alpr.set_default_region("eu")

#cap = cv2.VideoCapture("http://91.190.227.198/mjpg/video.mjpg")
# cap = cv2.VideoCapture("numPlates.mpg")

# while(True):    
#     ret, frame = cap.read() 

#     if ret:    
def preprocess(img):
    cv2.imshow('Number Plate', img)
    imgBlurred = cv2.GaussianBlur(img, (5,5), 0)
    gray = cv2.cvtColor(imgBlurred, cv2.COLOR_BGR2GRAY) 
#cv2.imshow("img.jpg", 1)   

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

#cv2.imwrite("abc.png", img)
results = alpr.recognize_file("car1.jpg")
#results1 = alpr.recognize_file("np.jpeg")
#print(results)
i = 0
        
for plate in results['results']:
    i += 1
    #print("Plate #%d" % i)
    #print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

            print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))    


        print(candidate['plate'])   

for plate in results1['results1']:
    i += 1
    #print("Plate #%d" % i)
    #print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

            print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))    


        print(candidate['plate'])   
    #When everything done, release the capture
# cap.release()
# alpr.unload()
#print(results)

cv2.waitKey(0)
cv2.destroyAllWindows()