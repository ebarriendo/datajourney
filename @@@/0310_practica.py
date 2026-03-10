import cv2 as cv
import numpy as np

# TODO: realizar lo correspondiente a la generacion de imagenes con circulos, rectangulos, diferentes rellenos. 

#* para generar la imagen utilizamos numpy 
fondo_zeros = np.zeros((500,500,3),dtype='uint8') #lleva el tamaño, canales de color y tipo de dato. 
#? UINT8 significa enteros sin signo de 9 bits. de 0 a 255. 
#? es np.zeros debido a que genera una imagen completa de 0s (todo negro)
fondo_full = np.full((400,400,3), (255,255,255), dtype='uint8')

#! Generar formas por coordenadas dentro de la imangen. 
fondo_zeros[50:200, 100:250] = (0,0,255)
fondo_zeros[100:250, 150:300] = (0,255,0)
fondo_zeros[150:300, 200:350] = (255,0,0)

fondo_full[50:200, 100:250] = (255,0,0)
fondo_full[100:250, 150:300] = (0,255,0)
fondo_full[150:300, 200:350] = (0,0,255)

cv.rectangle(
    fondo_zeros, 
    (1,1),
    (fondo_zeros.shape[1]//10, fondo_zeros.shape[0]//10), 
    (245,39,156),
    thickness = cv.FILLED
)

cv.rectangle(
    fondo_full, 
    (0,0),
    (fondo_full.shape[1]//8, fondo_full.shape[0]//16), 
    (39,245,194),
    thickness=7
)

#! Dibujar un circulo. 
cv.circle(
    fondo_zeros, 
    (fondo_zeros.shape[1] // 2, fondo_zeros.shape[0] // 2),
    200,
    (218,245,39),
    thickness= 10
)

cv.circle(
    fondo_full, 
    (fondo_full.shape[1] // 2, fondo_full.shape[0] // 2), 
    100, 
    (10,136,255), 
    thickness= 20
)

cv.line(
    fondo_zeros, 
    (250, 50),
    (250, 250), 
    (10,136,255),
    thickness=20
)

cv.line(
    fondo_full, 
    (200,100),
    (200,200),
    (245,39,156),
    thickness=20
)

cv.putText(
    fondo_zeros, 
    'putText()', 
    (150,450), 
    cv.FONT_HERSHEY_SCRIPT_COMPLEX, 
    2, 
    (255,255,255), 
    thickness=1
)

cv.putText(
    fondo_full, 
    'putText()',
    (100,350), 
    cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 
    3, 
    (0,0,0), 
    thickness=1
)

#mostrar daots
cv.imshow('Fondo negro', fondo_zeros)
cv.imshow('Fondo Full BGR', fondo_full)

#siempre usar: 
cv.waitKey(0)


