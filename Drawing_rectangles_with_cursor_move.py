import cv2
import numpy as np

drawing = False
ix = -1
iy = -1


def draw_rectangle(event, x, y, flags, param):
    global drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)


img = np.zeros((512, 512, 3))

cv2.namedWindow('drawing')
cv2.setMouseCallback('drawing', draw_rectangle)

while True:
    cv2.imshow('drawing', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
