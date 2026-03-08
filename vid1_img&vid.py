import cv2 as cv

# imagen1 = cv.imread('fotos/gato2.jpg') 
# #si tienes imagenes muy grandes, probablemente se van fuera de la pantalla. 
# cv.imshow('Gato1',imagen1)
# cv.waitKey(0)

capture = cv.VideoCapture(0) #instancia del video [El 0 esta asignado a nuestra camara de computadora]
#El 0 es el "Primera camara disponible"
while True: 
    isTrue, frame = capture.read() #se lee frame by frame el video
    #capture.read() devuelve dos valores, boolean y el frame. por eso recibimos ambos. 
    cv.imshow('Video',frame) #se muestra cada frame del video. 
    if cv.waitKey(200) & 0xFF == ord('d'): #el waitKey(20) es esperar 20 milisegundos entre frame. y luego d para detner el ciclo. 
        #waitKey(n) se puede cambiar la cantidad de frames. 
        break

#Siempre es importante no dejar recursos ocupados. 
capture.release() #liberar la variable
cv.destroyAllWindows() #cerrar la ventana


