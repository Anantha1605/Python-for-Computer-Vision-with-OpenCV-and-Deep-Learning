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


img = cv2.imread('DATA/sammy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
display_img(img) #sample img

noise_img = cv2.imread('DATA/sammy_noise.jpg')
noise_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2RGB)
display_img(noise_img) #noisier sample img

#to fix using median blur

median = cv2.medianBlur(noise_img, 5) # 5 is a common value so start with it and work your way
display_img(median)