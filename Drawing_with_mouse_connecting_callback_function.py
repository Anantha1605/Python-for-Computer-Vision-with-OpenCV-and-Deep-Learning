import numpy as np
import cv2


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 250, 0), -1)


cv2.namedWindow('drawing')
cv2.setMouseCallback('drawing', draw_circle)

img = np.zeros((512, 512, 3), np.uint8)
while True:
    cv2.imshow('drawing', img)
    if cv2.waitKey(1) & 0xFF == ord('E'):
        break

cv2.destroyAllWindows()
