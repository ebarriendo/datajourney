import cv2 as cv
import matplotlib.pyplot as pt

img = cv.imread('gato1.jpg')
cv.imshow("Gato1",img)

#! MATPLOTLIB invierte el formato de la imange, puesto que espera un RGB y OPENCV manda BGR
img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
pt.imshow(img_RGB)

fig, axes = pt.subplots(1, 2)

axes[0].imshow(img)           # colores mal
axes[0].set_title('BGR mal')

axes[1].imshow(img_RGB)       # colores bien
axes[1].set_title('RGB bien')

pt.show()

cv.waitKey(0)