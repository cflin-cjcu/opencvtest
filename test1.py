import cv2
import numpy as aa
from matplotlib import pyplot as plt
img=cv2.imread('test.jpg')
aa=img[100:300,100:300]
bb=img[300:500,300:500]
dst=cv2.addWeighted(aa,0.7,bb,0.3,0)
img[200:400,200:400]=dst
# cv2.imwrite('test1.jpg',img)

# img1=cv2.imread('test.jpg')
# print(img1)
cv2.imshow('aasa',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()