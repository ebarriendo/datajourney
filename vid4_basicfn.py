import cv2 as cv 

#TODO: Funciones mas comunes en proyectos computer vision. 

img = cv.imread('fotos/gato1.jpg')
cv.imshow('Gato BGR', img)

#? Convertir en grises. 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gato Grises', gray)

#? Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur GaussianBlur', blur)

#? Edge Cascade
cascade = cv.Canny(img, 125, 175) #nos permite ver los bordes existentes
cv.imshow('Edge Cascade Canny', cascade)
#? si quieres reducir la cantidad de bordes que se observan, primero usa un blur. 
cascade_blur = cv.Canny(blur, 125, 175) #? nos permite ver los bordes existentes
cv.imshow('GaussianBlur + Edge Cascade',cascade_blur)

#! DILATACION DE LA IMAGEN - Usando el cascade_blur
dilated = cv.dilate(cascade_blur, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#? Eroding Adelgaza imagen reduciendo pixeles de sus bordes.  
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#? Resized
resized = cv.resize(img,(100,100))
#cv.imshow('Resized', resized)

#? Cropping - Toda imagen es un array, podemos hacer array slicing. 
crop = img[0:60, 0:90]
cv.imshow('Crop', crop)

cv.waitKey(0)

# import cv2 as cv

# capture = cv.VideoCapture(0)

# while True: 
#     isTrue, frame = capture.read()

#     frame = cv.flip(frame, 1)
#     cv.imshow('Camara',frame)

#     if cv.waitKey(40) & 0xFF == ord('p'): 
#         break

# capture.release()
# cv.destroyAllWindows

