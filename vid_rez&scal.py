import cv2 as cv 
#! Resizing & ReScaling. 
#? Se ura para reducir el procesamiento.  Archivos grandes necesita mucho procesamiento, lo que hacemos es quitar un poco de informacion.  

def _rescaleFrame(frame, scale=0.75): 
    #! Imagen, Video y LiveVideo
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, 
                     dimensions, 
                     interpolation=cv.INTER_AREA)

def _changeRes(width, height):
    #! LiveVideo
    capture.set(3,width) 
    capture.set(4,height)



img = cv.imread('fotos\gato3.jpeg')
cv.imshow(F'CAT {img}',img)
resize_image = _rescaleFrame(img)
cv.imshow('CAT', resize_image)


capture = cv.VideoCapture(0)
#capture = cv.VideoCapture('videos\perros_parque.mp4')
while True: 
    isTrue, frame = capture.read()
    frame = cv.flip(frame,1)

    frame_resized = _rescaleFrame(frame)
    frame_resized_20 = _rescaleFrame(frame, 0.20) 

    cv.imshow('Video',frame)
    cv.imshow('Resize Video', frame_resized)
    cv.imshow('Resize Video 0.20', frame_resized_20)

    if cv.waitKey(40) & 0xFF == ord('a'): 
        break




capture.release()
cv.destroyAllWindows()
