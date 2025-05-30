import cv2
import numpy as np
import math

drawing = False
ix = -1
iy = -1


def radius(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def draw_circle(event, x, y, flags, param):
    global drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = radius(ix, iy, x, y)
            cv2.circle(img, (ix, iy), int(temp), (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        temp = radius(ix, iy, x, y)
        cv2.circle(img, (ix, iy), int(temp), (0, 0, 255), -1)


img = np.zeros((512, 512, 3))

cv2.namedWindow('drawing')
cv2.setMouseCallback('drawing', draw_circle)

while True:
    cv2.imshow('drawing', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
