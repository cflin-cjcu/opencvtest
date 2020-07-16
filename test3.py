import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3), np.uint8)
#img[:,:,2]=255

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.imshow('aasa',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
