import cv2 as cv 
#! Captura de video, redimension y escalar de imangen

capture = cv.VideoCapture(0)

def rescaleFrame(frame, scale=0.75): 
    #!Tomamos la altura y el ancho del video 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


#!Leer y mostrar imagen. 
img_gato1 = cv.imread('fotos\gato1.jpg') #!deben estar a la misma altura, porque sino no la detecta.
cv.imshow('Gato 1', img_gato1)
cv.waitKey(0)

while True: 
    isTrue, frame = capture.read()
    frame = cv.flip(frame,1)
    frame_resized = rescaleFrame(frame,0.50)
    cv.imshow("CAMARA", frame)
    cv.imshow("CAMARA_0.50",frame_resized)

    if cv.waitKey(40) & 0xFF == ord('p'): 
        break

capture.release()
cv.destroyAllWindows


# def rescaleFrame(frame, scale = 0.75): 
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = width, height

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# while True: 
#     isTrue, frame = capture.read()
#     frame = cv.flip(frame,1)
#     cv.imshow('Video_',frame)

#     if cv.waitKey(40) & 0xFF == ord('p'): 
#         break

# capture.release()
# cv.destroyAllWindows
