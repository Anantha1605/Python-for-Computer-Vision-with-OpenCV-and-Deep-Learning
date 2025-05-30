import cv2
import matplotlib.pyplot as plt


# function to display the image

def show_pic(i):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(i, cmap='gray')
    plt.show()


img = cv2.imread("DATA/crossword.jpg", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img, cmap='gray')
plt.show()

show_pic(img)

# to make the parts with ink black and the ones without ink white, to remove any non usage gray
ret, th1 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
show_pic(th1)

# ADAPTIVE THRESHOLD
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # done as adaptive threshold needs image in grayscale
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

show_pic(th2)

'''
The function applies adaptive thresholding, 
which determines the threshold for each pixel based on the local region around it.

Key Points:
cv2.adaptiveThreshold: Applies thresholding locally, making it effective for images with varying lighting.
Parameters:
255: Maximum value for the binary output (white).
cv2.ADAPTIVE_THRESH_MEAN_C: Threshold is the mean of neighboring pixel values minus a constant.
cv2.THRESH_BINARY: Pixels above the threshold become 255 (white); below become 0 (black).
blockSize: Size of the neighborhood used for threshold calculation.(has to be odd)
C: Constant subtracted from the mean to fine-tune the result.
'''

# blended values
blended = cv2.addWeighted(src1=th1, alpha=0.6, src2=th2, beta=0.4, gamma=0)
show_pic(blended)
