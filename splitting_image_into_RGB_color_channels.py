#import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('DATA/00-puppy.jpg')
img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img_red = img[:, :, 0]
img_blue = img[:, :, 1]
img_green = img[:, :, 2]
plt.imshow(img)
plt.show()
plt.imshow(img_red, cmap='gray')
plt.show()
plt.imshow(img_blue, cmap='gray')
plt.show()
plt.imshow(img_green, cmap='gray')
plt.show()
