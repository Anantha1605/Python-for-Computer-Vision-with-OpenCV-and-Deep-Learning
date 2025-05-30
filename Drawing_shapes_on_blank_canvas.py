import numpy as np
import matplotlib.pyplot as plt
import cv2

img = np.zeros((512, 512, 3), np.uint16)
plt.imshow(img)
plt.show()

cv2.rectangle(img, (100, 100), (350, 350), color=(127, 234, 56), thickness=8)
plt.imshow(img)


cv2.circle(img, (256,256), 64, color=(255,0,0), thickness= 8)
plt.imshow(img)


cv2.circle(img, (326,256), 64, color=(255,35,234), thickness= -1)
plt.imshow(img)


cv2.line(img, (0,0), (512,512), color= (255,230,0), thickness=10)
plt.imshow(img)
plt.show()
# cv2.rectangle(<img>, (x1,y1), (x2,y2), color = (R, G, B), thickness = T)
# cv2.circle(<img>, center: (x,y), radius, color=(R, G, B), thickness= T)
# cv2.line(img, start point, end point, color=(R, G, B), thickness= T)