#practicando funciones basicas pero con video por camara. 
#! gray, gaussianblur, canny (bordes), cannyblur
import cv2 as cv

capture = cv.VideoCapture(0)

def rescaleFrame(frame, scale=0.75): 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    frame = cv.flip(frame, 1)
    frame = rescaleFrame(frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #! elkernel debe ser impar. PORQUE NECESITA UN CENTRO EXACTO. 
    blur = cv.GaussianBlur(frame, (9,9), cv.BORDER_DEFAULT)
    cascade = cv.Canny(blur,125,125)

    cv.imshow('Gray', gray)
    cv.imshow('GussianBlur', blur)
    cv.imshow('Camara Normal', frame)
    cv.imshow('Canny Cascade',cascade)

    if cv.waitKey(40) & 0xFF == ord('p'): 
        break

capture.release()
cv.destroyAllWindows