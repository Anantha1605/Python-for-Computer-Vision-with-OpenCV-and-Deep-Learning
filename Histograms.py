import cv2
import numpy as np
import matplotlib.pyplot as plt

dark_horse = cv2.imread('DATA/horse.jpg')
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('DATA/rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('DATA/bricks.jpg')
show_bricks = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)

plt.imshow(show_horse)
plt.show()
plt.imshow(show_rainbow)
plt.show()
plt.imshow(show_bricks)
plt.show()

# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
hist_values = cv2.calcHist([blue_bricks], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_values)

hist_values = cv2.calcHist([dark_horse], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_values)

# plotting the 3 color histograms
# 1
img = blue_bricks
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.ylim([0, 20000])
plt.title('Blue Bricks Image')
plt.show()

# 2
img = dark_horse
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.ylim([0, 20000])
plt.title('Dark Horse')
plt.show()

# 3
img = rainbow
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.title('Rainbow Image')
plt.show()

# MASKING
rainbow = cv2.imread('DATA/rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

mask = np.zeros(img.shape[:2], np.uint8)
plt.imshow(mask, cmap='gray')
plt.show()
mask[300:400, 100:400] = 255
plt.imshow(mask, cmap='gray')
plt.show()

masked_img = cv2.bitwise_and(img, img, mask=mask)
show_masked_img = cv2.bitwise_and(show_rainbow, show_rainbow, mask=mask)
plt.imshow(show_masked_img, cmap='gray')
plt.show()

hist_mask_values_red = cv2.calcHist([rainbow], [2], mask, [256], [0, 256])
# for comparison sake, we are gonna show without mask
hist_values_red = cv2.calcHist([rainbow], [2], None, [256], [0, 256])

plt.plot(hist_mask_values_red)
plt.title('RED CHANNEL HISTOGRAM FOR MASKED RAINBOW')
plt.show()

plt.plot(hist_values_red)
plt.title('RED CHANNEL HISTOGRAM FOR NORMAL RAINBOW')
plt.show()


#HISTOGRAM EQUALIZATION
gorilla = cv2.imread('DATA/gorilla.jpg',0)
def display(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)
    plt.show()

display(gorilla,cmap='gray')
hist_values = cv2.calcHist([gorilla],[0],None,[256], [0,256])
plt.plot(hist_values)
plt.title('HISTOGRAM FOR GORILLA')
plt.show()

eq_gorilla = cv2.equalizeHist(gorilla)
display(eq_gorilla,cmap='gray')

#FOR COLOR IMAGES
color_gorilla = cv2.imread('DATA/gorilla.jpg')
show_gorilla = cv2.cvtColor(color_gorilla,cv2.COLOR_BGR2RGB)
display(show_gorilla)

hsv = cv2.cvtColor(color_gorilla,cv2.COLOR_BGR2HSV)
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])
eq_color_gorilla = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
display(eq_color_gorilla)