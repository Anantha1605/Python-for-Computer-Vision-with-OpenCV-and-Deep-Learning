import cv2

cap = cv2.VideoCapture(0) #command to capture video from default camera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # returns float value
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read() #returns frames

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)#for color frames just replace gray in this line with frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
