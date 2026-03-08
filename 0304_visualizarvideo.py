import cv2 as cv

#!0 es la primer camara disponible, la de la computadora
capture = cv.VideoCapture(0)
while True: 
    isTrue, frame = capture.read()
    frame = cv.flip(frame,1)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('Video',gray)
    if cv.waitKey(40) & 0xFF == ord('a'): 
        break

capture.release()
cv.destroyAllWindows





