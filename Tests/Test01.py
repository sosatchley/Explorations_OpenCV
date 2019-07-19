# Personal Test Number 1
# Many of these examples have left me wanting sliders to manipulate parameters
#   in realtime. OpenCV has a module for just such a feature.
# My first personal test is to create a small program that implements two track-
#   bar sliders which affect the first and second thresholds in Canny detection.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
window = 'Variable Canny'
thresh1 = 0
thresh2 = 0
threshMax = 500

def slideOne(val):
    global thresh1
    thresh1 = val

def slideTwo(val):
    global thresh2
    thresh2 = val

cv2.namedWindow(window)

cv2.createTrackbar('Thresh1', window, 0, threshMax, slideOne)
cv2.createTrackbar('Thresh2', window, 0, threshMax, slideTwo)

while(1):
    _, frame = cap.read()

    canny = cv2.Canny(frame, thresh1, thresh2)
    cv2.imshow(window, canny)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
