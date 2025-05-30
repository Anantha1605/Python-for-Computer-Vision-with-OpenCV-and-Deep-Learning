import numpy as np
import cv2
import matplotlib.pyplot as plt


def load_img():
    blank_img = np.zeros((600, 600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img, text='ABCDE', org=(50, 300), fontFace=font, fontScale=5, color=(255, 255, 255), thickness=25,
                lineType=cv2.LINE_AA)
    return blank_img


def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


img = load_img()
display_img(img)

# erosion - erodes the boundary
kernel = np.ones((5, 5), np.uint8)
erosion1 = cv2.erode(img, kernel, iterations=1)
display_img(erosion1)

# 5 -iteration erosion
img = load_img()
kernel = np.ones((5, 5), np.uint8)
erosion5 = cv2.erode(img, kernel, iterations=4)
display_img(erosion5)

# opening - erosion followed by dilation
img = load_img()
white_noise = np.random.randint(low=0, high=2, size=(600, 600))
white_noise *= 255
noise_img = white_noise + img
display_img(noise_img) #noised image
opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
display_img(opening)

#closing
img = load_img()
black_noise = np.random.randint(low=0, high=2, size=(600, 600))
black_noise *= -255
black_noise_img = img + black_noise
display_img(black_noise_img) #noised image
opening = cv2.morphologyEx(black_noise_img, cv2.MORPH_OPEN, kernel)
display_img(opening)
closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)
display_img(closing)

#gradient
img = load_img()
display_img(img)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
display_img(gradient)
