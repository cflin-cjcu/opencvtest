import numpy as np
import cv2
cv2.Ved
cap = cv2.VideoCapture(0)

while(True):
 # Capture frame-by-frame
 ret, frame = cap.read()

 # Our operations on the frame come here
 #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

 # Display the resulting frame
 cv2.imshow('frame',frame)
 if cv2.waitKey(1) & 0xFF == ord('s'):
    cv2.imwrite('test2.jpg',frame)
    break
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break
24
25 # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()