# MOG Background Reduction
import cv2
import numpy as np

cap = cv2.VideoCapture('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\people-walking.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)

    k = cv2.waitKey(30) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()

# Test: Apply noise reduction filters/compare similar images
