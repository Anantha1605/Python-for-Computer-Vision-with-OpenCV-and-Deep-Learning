import cv2
img = cv2.imread("DATA/00-puppy.jpg")
while True:
    cv2.imshow("puppy", img)
    if cv2.waitKey(1) & 0xFF == ord('&'):
        break