import cv2
import numpy as np
#from matplotlib import pyplot as plt

#cap = cv2.VideoCapture('2017-10-27-164957.webm')
cap = cv2.VideoCapture(0)


#img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image',img)
#cv2.waitKey(0)
print "before"
while(cap.isOpened()):
	print "Inside while"
	ret, frame = cap.read()
	
  if ret==True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		cv2.imshow('frame', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	else:
		break
    
cap.release()
cv2.destroyAllWindows()
