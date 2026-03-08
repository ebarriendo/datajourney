import cv2 as cv

capture = cv.VideoCapture(0) #? El 0 es la primer camara que encuenrtres 
#! Este while True l o puedo utilizar en MicroPython 
while True: 
    isTrue, frame = capture.read()
    frame = cv.flip(frame,1) #? gira(que cosa, de que forma)
    cv.imshow('Video',frame)
    if cv.waitKey(40) & 0xFF == ord('p'): 
        break

#! Siempre en todo cv codigo soltar la captura y destruir las ventanas.
capture.release
cv.destroyAllWindows

