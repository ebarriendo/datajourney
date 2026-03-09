import cv2 as cv
import numpy as np
#! escribir y dibujar en imagenes

blank = np.zeros((500,500,3),dtype='uint8') #? el 3 significa los canales de colores disponibles. 
cv.imshow('Blank',blank)

# img = cv.imread('fotos/gato1.jpg')
# cv.imshow('Cat',img)

#? Paint the img a certain colr
blank[:] = 0,255,0
cv.imshow('Green',blank)

#? Colorear una porcion especifica de la imagen. 
blank[200:300, 300:400] = 255,0,0
cv.imshow('Cuadro',blank)

#? Dibujar un rectangulo dentro
fondo = np.zeros((500,500,3),dtype='uint8')
#cv.rectangle(fondo,(0,0),(200,100),(0,0,255),thickness=2)
#cv.rectangle(fondo,(0,0),(200,100),(0,0,255),thickness=-1)
cv.rectangle(fondo,(0,0),
             (fondo.shape[1]//2,fondo.shape[0]//2),
             (0,0,255),
             thickness=cv.FILLED)

# cv.rectangle(fondo,(0,0),(200,100),(0,0,255),thickness=cv.FILLED)

#? Draw a circle 
cv.circle(fondo,
          (fondo.shape[1]//2,fondo.shape[0]//2),
          60,
          (300,300,300),
          thickness=3)


cv.line(fondo,
        (0,0),
        (fondo.shape[1]//2, fondo.shape[0]//3),
        (0,255,0),
        thickness=3
)


#? Text on a img
cv.putText(fondo,
           'Hello my name is Emmanuel',
           (50,400),
           cv.FONT_HERSHEY_TRIPLEX,
           1.0,
           (255,0,0),
           thickness=2
           )

cv.imshow('Rectangulo y circulo.',fondo)

cv.waitKey(0)