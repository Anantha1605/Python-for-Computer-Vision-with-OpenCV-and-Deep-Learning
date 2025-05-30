import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_img():
    img = cv2.imread('DATA/bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def display_img(i):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(i, cmap='gray')
    plt.show()

i = load_img()
display_img(i)

#gamma correction
gamma1 = 1/6
gamma2 = 6
np.power(i,gamma1)
display_img(i)
np.power(i,gamma2)
display_img(i)


#blurring
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = 'bricks', org = (10,600), fontFace = font, fontScale=10, color=(255,0,0), thickness =4)

display_img(img)


kernel = np.ones(shape = (5,5),dtype=np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
display_img(dst)



#inbuilt blur
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = 'bricks', org = (10,600), fontFace = font, fontScale=10, color=(255,0,0), thickness =4)
blurred = cv2.blur(img, ksize=(5,5))
display_img(blurred)

#gaussian blur
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = 'bricks', org = (10,600), fontFace = font, fontScale=10, color=(255,0,0), thickness =4)
blurred = cv2.GaussianBlur(img, (5,5), 10)
display_img(blurred)

#median blur
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = 'bricks', org = (10,600), fontFace = font, fontScale=10, color=(255,0,0), thickness =4)
blurred = cv2.medianBlur(img, 5)
display_img(blurred)

#bilateral filter
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = 'bricks', org = (10,600), fontFace = font, fontScale=10, color=(255,0,0), thickness =4)
blurred = cv2.bilateralFilter(img, 9, 75, 75)
display_img(blurred)